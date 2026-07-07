# Log

Append-only timeline of wiki operations, newest last. One line per
operation; never edit past entries.

- 2026-07-06 — wiki initialized: schema (CLAUDE.md), templates, and worked
  example pages created. No raw sources ingested yet.
- 2026-07-06 — schema extended for reference works: added wiki/cases/ and
  wiki/sources/ page types, case template, lazy-compile rules for large
  reference PDFs, and .gitignore keeping raw/ local-only. Attempted ingest
  of "2026 Acquisition Attorneys Deskbook.pdf" — upload was a 78-byte
  share-link stub, not the PDF; awaiting the actual file.
- 2026-07-07 — Deskbook source-map pass complete: real PDF (17.5 MB)
  reached via Google Drive; full Summary of Contents extracted → created
  wiki/sources/2026-acquisition-attorneys-deskbook.md (35 chapters,
  3 volumes, 0 compiled). Full PDF not in raw/ yet — env limits capped
  extraction at front matter + ~3 chapters; deep compilation deferred to
  the local machine per reference-work rules.
