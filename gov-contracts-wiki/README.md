# Government Contracts Wiki

A personal, LLM-maintained knowledge base for government contracts work,
built on Andrej Karpathy's "LLM wiki" pattern
([original gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)).

## The idea in one paragraph

You collect source material — contract award docs, mods, RFPs, meeting
notes, emails you've exported — into `raw/` and never touch it again. An
LLM agent (Claude Code, pointed at this folder) "compiles" those sources
into an interlinked wiki of markdown pages: one summary per source, one
page per contract, per agency/vendor/person, per FAR clause or process.
The agent keeps the index, the cross-links, and the deadline tracker
current, and flags contradictions. Unlike RAG, nothing gets re-discovered
from scratch on every question — knowledge compounds.

## How to use it

1. Open a terminal in this folder and run `claude` (Claude Code). The
   `CLAUDE.md` file teaches it the rules automatically.
2. Drop a document into `raw/` (PDFs, .docx, .md, .txt, .eml all work) and
   say: **"ingest the new file in raw/"**.
3. Ask questions: *"what's the status of the Acme task order?"*, *"which
   of my contracts have 52.217-9 and when are the option windows?"*,
   *"what did we agree to in the June kickoff?"*
4. Every week or two, say: **"lint the wiki"** — it checks for broken
   links, stale claims, and upcoming deadlines.

## Map of the repo

| Path | What it is |
|---|---|
| `CLAUDE.md` | The schema: rules the agent follows. Edit to change behavior. |
| `index.md` | Catalog of every wiki page with one-line summaries. |
| `log.md` | Append-only history of everything the agent did. |
| `deadlines.md` | Rolling tracker of option windows, deliverables, PoP ends. |
| `raw/` | Your source documents. Immutable — the agent only reads. |
| `wiki/summaries/` | One page per raw source. |
| `wiki/contracts/` | One page per contract, task order, or IDIQ. |
| `wiki/entities/` | Agencies, contracting offices, vendors, people. |
| `wiki/concepts/` | FAR/DFARS clauses, processes, cross-contract themes. |
| `templates/` | Skeletons the agent copies when creating new pages. |

## ⚠️ Sensitivity

This is a personal notes tool. **Keep CUI, classified material,
source-selection-sensitive information, and third-party proprietary data
out of it** — especially if this folder syncs to a cloud service or a
remote git host. The agent is instructed to warn you, but you are the
control.

## Why git?

Commit after each ingest session (`git add -A && git commit -m "ingest:
mod P00003"`). You get history, diffs of what the agent changed, and
free backup if you add a private remote.
