#!/usr/bin/env python3
"""Split a TJAGLCS-style deskbook PDF into one PDF per chapter.

Chapter starts are found from the PDF's bookmark outline when present,
otherwise by scanning each page's text for a "CHAPTER 12" / "CHAPTER 15A"
heading near the top of the page. Pages before the first chapter are
saved as ch00-front-matter.pdf.

Usage:
    python3 split_deskbook.py path/to/deskbook.pdf [output_dir]

Output defaults to a "deskbook-chapters" folder next to the input file.
Requires: pip install pypdf
"""
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

CHAPTER_RE = re.compile(r"\bCHAPTER\s+(\d{1,2}\s?[AB]?)\b", re.IGNORECASE)


def slugify(text: str, max_len: int = 60) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return text[:max_len].rstrip("-") or "untitled"


def outline_chapters(reader: PdfReader) -> list[tuple[int, str, str]]:
    """Return (page_index, chapter_number, title) from bookmarks, if any."""
    found = []

    def walk(items):
        for item in items:
            if isinstance(item, list):
                walk(item)
                continue
            title = (item.title or "").strip()
            m = CHAPTER_RE.search(title)
            if m:
                try:
                    page_idx = reader.get_destination_page_number(item)
                except Exception:
                    continue
                num = m.group(1).replace(" ", "").upper()
                found.append((page_idx, num, title))

    try:
        walk(reader.outline)
    except Exception:
        pass
    return found


def scanned_chapters(reader: PdfReader) -> list[tuple[int, str, str]]:
    """Fallback: find pages whose top text starts a new chapter."""
    found = []
    seen = set()
    for i, page in enumerate(reader.pages):
        try:
            head = (page.extract_text() or "")[:200]
        except Exception:
            continue
        m = CHAPTER_RE.search(head)
        if not m:
            continue
        num = m.group(1).replace(" ", "").upper()
        # Only take the FIRST page where each chapter number appears as a
        # heading; later hits are cross-references or running headers.
        if num not in seen:
            seen.add(num)
            found.append((i, num, f"Chapter {num}"))
    return found


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    outdir = Path(sys.argv[2]) if len(sys.argv) > 2 else src.parent / "deskbook-chapters"
    outdir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(src)
    total = len(reader.pages)
    print(f"{src.name}: {total} pages")

    chapters = outline_chapters(reader)
    method = "bookmarks"
    if len(chapters) < 5:  # outline missing or unhelpful
        chapters = scanned_chapters(reader)
        method = "text scan"
    if not chapters:
        sys.exit("No chapter headings found by bookmarks or text scan.")

    chapters.sort(key=lambda c: c[0])
    # Deduplicate chapter numbers, keeping the earliest page for each.
    unique = {}
    for page_idx, num, title in chapters:
        unique.setdefault(num, (page_idx, num, title))
    chapters = sorted(unique.values(), key=lambda c: c[0])
    print(f"found {len(chapters)} chapters via {method}\n")

    # Front matter = everything before the first chapter page.
    first_page = chapters[0][0]
    segments = []
    if first_page > 0:
        segments.append((0, first_page, "00", "front-matter"))
    for idx, (page_idx, num, title) in enumerate(chapters):
        end = chapters[idx + 1][0] if idx + 1 < len(chapters) else total
        label = re.sub(CHAPTER_RE, "", title).strip(" -–—:") or f"chapter-{num}"
        segments.append((page_idx, end, num.zfill(2) if num[-1].isdigit() else num.zfill(3), slugify(label)))

    for start, end, num, slug in segments:
        writer = PdfWriter()
        for p in range(start, end):
            writer.add_page(reader.pages[p])
        name = f"ch{num}-{slug}.pdf"
        with open(outdir / name, "wb") as fh:
            writer.write(fh)
        size_mb = (outdir / name).stat().st_size / 1e6
        print(f"  {name:<55} pages {start + 1}-{end}  ({size_mb:.1f} MB)")

    print(f"\nwrote {len(segments)} files to {outdir}/")


if __name__ == "__main__":
    main()
