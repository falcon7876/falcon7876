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
- 2026-07-07 — full Deskbook PDF obtained (via GitHub branch upload,
  then removed from git; lives in gitignored raw/). Wrote and tested
  scripts/split_deskbook.py; split the 1,651-page PDF into 37 chapter
  PDFs + front matter in raw/deskbook-chapters/. Rebuilt the source-map
  chapter table from actual in-book headings (the printed Summary of
  Contents is stale; chs. 2 and 3 are near-duplicate "Contract Format
  and the FAR" variants; Contract Changes is ch. 18).
- 2026-07-07 — first compile tranche ingested (5 chapters → 4 concept
  pages): ch. 7 → concepts/contract-types; ch. 15A →
  concepts/bid-protests; ch. 18 → concepts/contract-changes; chs. 20-21
  → concepts/terminations. Index and source-map checklist updated.
- 2026-07-07 — tranche 2 ingested: ch. 15B → concepts/cofc-protest-litigation;
  chs. 19A-19B → concepts/contract-disputes-act; ch. 22 → concepts/adr.
- 2026-07-07 — tranche 3 ingested: ch. 4 → concepts/authority-to-contract;
  ch. 5 → concepts/funding-and-fund-limitations; ch. 6 → concepts/competition.
- 2026-07-07 — tranche 4 ingested: ch. 8 → concepts/sealed-bidding;
  ch. 9 → concepts/negotiated-procurements; ch. 10 →
  concepts/simplified-acquisitions; ch. 11 →
  concepts/commercial-products-services. Index and source map updated.
- 2026-07-07 — tranche 5 ingested: ch. 12 →
  concepts/responsibility-timeliness-oci; ch. 13 →
  concepts/contract-pricing; ch. 14 → concepts/socioeconomic-policies.
  Index and source map updated.
- 2026-07-07 — tranche 6 ingested: ch. 16 →
  concepts/inspection-acceptance-warranty; ch. 17 →
  concepts/contract-payment. Index and source map updated.
- 2026-07-07 — tranche 7 ingested: ch. 23 → concepts/ethics; ch. 24 →
  concepts/procurement-fraud; ch. 25 → concepts/labor-standards.
  Index and source map updated.
- 2026-07-07 — tranche 8 ingested: ch. 26 →
  concepts/competitive-sourcing-privatization; ch. 27 →
  concepts/intellectual-property; ch. 28 →
  concepts/construction-contracting. Index and source map updated.
- 2026-07-07 — ingested Deskbook tranche 9 (chs. 29-32, special topics II) →
  created concepts/contingency-contracting (chs. 29-30),
  concepts/army-naf-contracting (ch. 31),
  concepts/interagency-transactions (ch. 32); updated source map + index
