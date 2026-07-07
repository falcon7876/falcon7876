---
type: concept
created: 2026-07-07
updated: 2026-07-07
sources: [raw/deskbook-chapters/ch27-intellectual-property.pdf]
tags: [intellectual-property, data-rights, dfars-227, technical-data, computer-software, bayh-dole, patents, sbir]
---

# Intellectual Property & Data Rights

**One-line:** The Government almost never owns contractor IP — it takes
a license whose breadth follows the money (who funded development), and
its rights are only as good as the assertion tables, markings, and
challenge deadlines that police them.

*Compiled from 2026 Acquisition Attorneys Deskbook ch. 27 (whole
chapter).*

## IP background (the substrate)
- **Patents** (35 U.S.C.): 20-year exclusion right (15 design); must be
  eligible subject matter (*Alice* two-step for abstract ideas),
  useful, novel (1-year U.S. grace period), non-obvious (*Graham*/
  *KSR*). Only natural persons can be inventors (*Thaler* — no AI).
- **Trade secrets**: value from secrecy + reasonable protective
  efforts; no time limit; no protection from independent discovery or
  reverse engineering (contract around it). Federal layer: Economic
  Espionage Act, DTSA (private federal cause of action), Trade
  Secrets Act (18 U.S.C. § 1905 — criminalizes federal-employee
  leaks).
- **Copyright**: original works fixed in a tangible medium; life+70;
  registration required to sue. **No copyright in U.S. Government
  works**, though the Government can take assignment (17 U.S.C. § 105).
- **Trademarks** (Lanham Act): source identifiers; DoD brands and
  licenses its marks (10 U.S.C. § 2260).

## Data rights fundamentals
- Data rights = copyright/trade-secret law + contract; **separate from
  patent rights**. The Government takes a nonexclusive **license**,
  not ownership.
- **Deliverables vs. rights**: CDRLs define what's delivered; license
  clauses define what the Government may do with it. Rights without a
  deliverable are "inchoate" — cure with deferred delivery/ordering
  clauses.
- Two regimes that must never be mixed in one contract: **FAR Part
  27** (civilian; DoD is exempt) and **DFARS Part 227** (defense).
  Framework questions: civilian or defense? technical data or computer
  software? commercial or noncommercial?
- Policy: take the **minimum** deliverables and rights needed (but
  think lifecycle: competition, organic maintenance, reprocurement).
  **Technical data ≠ the end item** — absent a contractual bar, the
  Government may reverse engineer hardware even when the data package
  is restricted (*Night Vision Corp.*).

## DFARS noncommercial licenses (the follow-the-funding table)
| Development funding | Technical data (252.227-7013) | Software (252.227-7014) |
|---|---|---|
| Exclusively Government | **Unlimited rights** | Unlimited rights |
| Mixed | **GPR** (→ unlimited after 5 yrs, extendable) | GPR |
| Exclusively private | **Limited rights** | **Restricted rights** |
- **Unlimited**: any purpose, anyone — but the contractor keeps
  ownership and copyright (whether trade-secret status survives is
  contested — *L-3 Westwood* vs. *GlobeRanger*).
- **GPR**: anything within Government + release to third parties for
  **Government purposes** (competitive reprocurement, FMS — never
  commercial); recipients sign NDAs or hold 7025 contracts.
- **Limited/restricted**: inside the Government only; no manufacture;
  narrow escape hatches (emergency repair & overhaul, **covered
  Government support contractors**); restricted software = one
  computer at a time, minimum backup copies, no reverse engineering by
  recipients.
- "Developed" = exists and is **workable** (less than patent reduction
  to practice); private expense = IR&D/B&P/indirect pools (charging
  choices respected, *ATK Thiokol*); FFP overruns don't count as
  Government funding. **Segregability**: funding is determined at the lowest
  practicable sub-component/sub-routine — DFARS only, no FAR analog.
- **Unlimited regardless of funding**: specified test/study data,
  **form-fit-function data**, **OMIT data** (operations/maintenance/
  installation/training, minus detailed manufacturing data),
  corrections to GFI, publicly released data, expired GPR.
- Specially negotiated licenses OK but never below limited/restricted
  rights (deviation requires DPAP). Source selection may **evaluate**
  offered rights (*Keuffel & Esser*) but can never **require** more
  than the Government is entitled to as a condition of award
  (10 U.S.C. § 3771(a)(8)).

## Commercial items (DFARS)
- **Commercial technical data** (252.227-7015): Government gets only
  what's customarily provided to the public (plus FFF, repair/
  install/operation data, Government-funded modification data); rights
  ≈ limited rights. Commercial items are **presumed developed at
  private expense** for challenge purposes.
- **Commercial software**: no standard clause — take the vendor's
  standard license unless inconsistent with federal law or needs.
  Scrub for the usual offenders: click/browse-wrap (end users can't
  bind the Government), open-ended indemnification (unenforceable per
  52.212-4), choice of forum, auto-renewal, unilateral amendment.
  GSA's 552.212-4 deviation neutralizes many by rule.

## FAR (civilian) regime — key contrasts
Single clause **52.227-14** for all data: Government takes **unlimited
rights in everything delivered**; contractors protect limited-rights
data/restricted software by **withholding it and delivering FFF data
instead** (Alternates II/III allow marked delivery). No GPR, no
segregability, no funding analysis. SBIR data: Government-purpose-only
protection for 4 years post-acceptance (FAR) vs. **20 years** from
project completion with limited/restricted-rights treatment (DFARS
SBIR/STTR, 252.227-7104); SBIR rights attach **regardless of funding
source**, even in Phase III.

## Data rights in practice (where cases are won)
- **Assert early, mark correctly**: unlisted or unmarked = unlimited
  rights. DFARS offers require a **rights assertion table**
  (252.227-7017) attached to the contract; post-award additions only
  for new info or inadvertent omissions that wouldn't have changed
  source selection.
- **Markings**: only prescribed legends restrict rights, but
  extraneous markings that don't restrict Government rights aren't
  violations (*Boeing v. Air Force*, Fed. Cir. 2020). Unmarked data:
  contractor may seek permission to cure within 6 months.
  Nonconforming legends: Government notifies; uncorrected after 60
  days it may strike them (itself a CDA-appealable act, *Alenia*).
- **Challenges/validation** (252.227-7019/-7037): CO needs reasonable
  grounds (and must show Government funding to attack the commercial
  presumption); pre-challenge RFI → written challenge → contractor's
  justification (a **certified CDA claim** regardless of amount) →
  CO final decision (restriction honored 90 days pending appeal).
  Challenge window: 3 years from delivery or final payment (RFO: 6).
- **Tools**: deferred delivery (2 years), deferred ordering (3 years
  post-termination; pay only conversion/reproduction costs);
  **payment withholding** up to 10% for late/deficient technical data
  (DFARS 252.227-7030; FAR version capped at lesser of $100K/5%).
- **OTs**: Bayh-Dole and 10 U.S.C. §§ 3771-86 don't apply — IP terms
  are fully negotiable.

## Patents under contracts (Bayh-Dole, 35 U.S.C. §§ 200-212)
- Applies to **subject inventions** (conceived or first actually
  reduced to practice in performance of the funding agreement);
  statute covers small/nonprofit contractors, extended to all by
  executive order; N/A to OTs.
- Contractor pipeline: **disclose** (2 months from inventor
  disclosure; piecemeal disclosure forfeits title, *Campbell
  Plastics*) → **elect title** (2 years) → **file** the patent
  application. Miss a step and the Government may take title.
- Government keeps a nonexclusive, irrevocable, **paid-up license**
  worldwide; **march-in rights** (agency head only, due process) to
  force licensing; **domestic manufacture** condition on exclusive
  U.S. licenses. Bayh-Dole allocates Government-contractor rights at
  every tier — primes can't strip subs' inventions via the
  subcontract. FAR 52.227-13 (title to the Government) for foreign-
  controlled contractors, intel work, and other exceptional cases.

## Patent "infringement" by the Government (28 U.S.C. § 1498)
- Government use = eminent-domain taking of a compulsory license; the
  patentee's **exclusive** remedy is compensation at the **COFC**.
  Contractors working "for the Government... with authorization or
  consent" are **immune from district-court suit** (*Richmond Screw
  Anchor*), including from indirect-infringement claims (*Astornet*).
- Authorization & consent may be express (52.227-1, narrow or broad
  Alt. I) or implied; in service contracts it's found where avoiding
  infringement would breach the contract (*Sevenson*). The Government
  pairs it with **indemnification** (52.227-3) and **notice &
  assistance** (52.227-2) clauses to push liability back.
- Compensation = reasonable royalty (*Georgia-Pacific* factors) +
  possibly fees/costs; **no injunctions, no treble damages** — a
  patent can never cut the Government off from a supply source
  (*Trojan*). DoD can also settle infringement claims
  administratively (10 U.S.C. § 3793; DFARS 227.70).

## Connects to
- [Commercial Products & Services](commercial-products-services.md) —
  commercial license acceptance and tailoring
- [Contract Disputes Act](contract-disputes-act.md) — marking
  challenges as certified claims
- [Competition](competition.md) — data rights as the key to
  competitive reprocurement; patents don't justify sole source
- [Contract Pricing](contract-pricing.md) — IR&D allowability and the
  private-expense determination
- Source: [2026 Acquisition Attorneys Deskbook](../sources/2026-acquisition-attorneys-deskbook.md), ch. 27

## Gotchas / lessons learned
- Never mix FAR 52.227-14 and DFARS 252.227-7013 in one instrument —
  the regimes conflict, and mixed clauses are a standing ambiguity
  (common failure in GSA/GWAC orders by DoD).
- The assertion table is the contractor's whole case: unasserted =
  unmarked = unlimited rights, and post-award additions are tightly
  limited.
- For the Government, buy OMIT and FFF data deliberately — they carry
  unlimited rights regardless of funding and often cover the
  sustainment mission without a data-rights war.
- GPR's 5-year sunset is a quiet Government win: calendar it, then
  compete the reprocurement with the now-unlimited data.
- A contractor's patent is not a sole-source justification, and § 1498
  means patent threats can't stop a competitor from performing a
  Government contract.
