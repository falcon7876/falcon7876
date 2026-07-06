# Government Contracts Wiki — Agent Instructions

This is a Karpathy-style LLM wiki: a personal knowledge base for government
contracts work, made of plain markdown files that an LLM agent (you) builds
and maintains. The human curates sources and asks questions; you do the
synthesis, cross-referencing, and bookkeeping.

## Directory layout

```
gov-contracts-wiki/
├── CLAUDE.md            ← this file: the schema. Conventions live here.
├── README.md            ← human-facing explanation of the wiki
├── index.md             ← catalog of every wiki page, one line each
├── log.md               ← append-only timeline of every wiki operation
├── deadlines.md         ← rolling tracker of dates that matter
├── raw/                 ← IMMUTABLE source documents. Read, never modify.
├── wiki/
│   ├── summaries/       ← one page per raw source
│   ├── contracts/       ← one page per contract / task order / IDIQ
│   ├── entities/        ← agencies, offices, vendors, people
│   ├── concepts/        ← FAR/DFARS clauses, processes, recurring themes
│   ├── cases/           ← GAO/COFC/CAFC decisions and board cases
│   └── sources/         ← source maps for large reference works
└── templates/           ← starting skeletons for each page type
```

## Ground rules

1. **`raw/` is immutable.** Never edit, rename, or delete anything in it.
   The human puts files there; you only read them.
2. **Every claim traces to a source.** Wiki pages cite the raw file(s) they
   came from, e.g. `(source: raw/2026-07-01-mod-p00003.pdf)`. If the human
   tells you something verbally in chat, cite it as `(source: conversation,
   YYYY-MM-DD)`.
3. **Wikilinks connect pages.** Use relative markdown links like
   `[GSA](../entities/gsa.md)`. When you mention an entity, contract, or
   concept that has a page, link it. When one should exist but doesn't,
   create at least a stub.
4. **Frontmatter on every wiki page:**
   ```yaml
   ---
   type: contract | entity | concept | summary
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   sources: [raw/filename, ...]
   tags: [far, idiq, option-exercise, ...]
   ---
   ```
5. **File naming:** lowercase kebab-case. Contracts by short name or number
   (`wiki/contracts/47qtca-25-d-0042.md`), people by full name
   (`wiki/entities/jane-smith.md`), summaries prefixed with the raw file's
   date (`wiki/summaries/2026-07-01-mod-p00003.md`).
6. **Contradictions are flagged, not silently resolved.** If a new source
   contradicts an existing page, note both versions with dates and mark the
   section `⚠️ CONFLICT`, then tell the human.
7. **Never fabricate contract data.** No invented clause numbers, dollar
   figures, dates, or names. If a source is ambiguous, say so on the page.

## Sensitivity rule (read this twice)

This wiki is for the owner's personal work notes. **Do not place CUI,
classified information, source-selection-sensitive data (FAR 3.104),
contractor bid/proposal information, or anything under an NDA into this
wiki**, and warn the human if a raw source appears to contain such
material before summarizing it. When in doubt, ask before ingesting.

## Operations

### Ingest (human drops a file in `raw/`, or says "ingest X")
1. Read the source fully. Briefly discuss key takeaways with the human.
2. Write `wiki/summaries/<date>-<name>.md` — what it is, key facts, dates,
   dollar amounts, parties, obligations, and anything unusual.
3. Update or create the affected `contracts/`, `entities/`, and `concepts/`
   pages. One source often touches many pages — that's expected.
4. Pull any dates (option exercise windows, deliverable due dates, PoP
   ends, protest deadlines) into `deadlines.md`.
5. Update `index.md`; append one line to `log.md`.

### Ingest — large reference works (deskbooks, treatises, 100+ page guides)
Do NOT exhaustively summarize. Instead:
1. Read the table of contents (and index if present). Build a **source
   map** page in `wiki/sources/` — chapter-by-chapter list of what the
   work covers, with page ranges, so the wiki knows what's in it.
2. Compile lazily: when a question or contract touches a topic the work
   covers, read that chapter (in ~20-page passes), then write or enrich
   the relevant `concepts/` and `cases/` pages, citing the work with
   page numbers.
3. The human may name priority chapters to compile up front.
4. **Do not commit the reference PDF itself to git** — large binary,
   likely copyrighted. It stays in `raw/` locally, gitignored. Only the
   derived notes are committed.

### Query (human asks a question)
1. Start from `index.md` to locate relevant pages; follow links.
2. Answer with citations to wiki pages and underlying raw sources.
3. If the answer required real synthesis that isn't yet written down,
   offer to file it back into the wiki (usually as a concept page).

### Lint (human says "lint the wiki", or run after big ingests)
- Broken or missing wikilinks; orphan pages nothing links to.
- Contradictions and stale claims (e.g., a PoP end date that has passed).
- `deadlines.md` entries that are past due or within 30 days — surface
  these to the human every time.
- Entities mentioned on 2+ pages that have no entity page.
- `index.md` entries that drifted from actual page contents.
Report findings; fix the mechanical ones, ask about the judgment calls.

### Log format (`log.md`, append-only, newest last)
```
- 2026-07-06 — ingested raw/2026-07-01-mod-p00003.pdf → updated 4 pages
  (summary, contracts/47qtca-25-d-0042, entities/acme-corp, deadlines)
```

## Page-type notes

- **contracts/**: the workhorse. Track contract number, vehicle, type
  (FFP/T&M/CPFF...), agency & office, prime/subs, PoP with option years,
  ceiling/funded values, CLIN structure, key personnel, mods (table, newest
  first), deliverables, and open issues.
- **entities/**: who/what they are, role, contact info if known, and a
  "relationships" section linking to contracts and other entities.
- **concepts/**: FAR/DFARS clauses (what they require in plain English,
  which of our contracts include them), processes (option exercise, REA,
  closeout), and cross-contract themes. Cite the actual regulation
  (e.g., FAR 52.217-9) so claims are checkable.
- **cases/**: one page per decision (GAO, COFC, CAFC, ASBCA/CBCA).
  Include the full citation and date, the holding in one line, the facts
  in 2-3 sentences, why it matters to our work, and links to affected
  concepts/contracts. File by citation slug (e.g.,
  `cases/gao-b-424012-gsh-of-alabama.md`).
- **sources/**: one map page per large reference work — bibliographic
  info, chapter list with page ranges, and a "compiled so far" checklist
  linking to the concept/case pages derived from it.

The wiki should compound: prefer updating an existing page over creating a
near-duplicate, and prefer linking over repeating.
