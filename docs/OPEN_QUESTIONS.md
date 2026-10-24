# Open Questions

Tracked decisions and facts that are not yet settled. Each has an owner and the phase by which it must be answered. Close an item by recording the answer, date and evidence, then updating the referenced documents.

Sources: Phase 0 research ([first report](research/2026-10-24-phase0-deep-research.md), [focused report](research/2026-10-24-phase0-focused-research.md)) plus earlier ADRs.

**Focused research (2026-10-24):** no published official interpretation was found for OQ-01, 02, 04, 05 — they stay with a lawyer/authority. Partial answers are noted inline.

## Legal / regulatory

| ID | Question | Blocks | Owner | Needed by |
|---|---|---|---|---|
| OQ-01 | How is a parking angle of **exactly 30°** treated under No. 41 B.E. 2537, which distinguishes only `< 30°` and `> 30°`? | National 30° rule (`stall.exactly_30`) | Thai building-control lawyer / authority — *no published interpretation found* | Phase 2 |
| OQ-02 | Does No. 41 cl. 2(2) prohibit serving perpendicular stalls from a **one-way aisle**, or only one-way entrances/exits? | Generator angle × direction combinations | Thai building-control lawyer — *no published interpretation found* | Phase 2 |
| OQ-03 | Have later BMA amendments changed BMA Ordinance B.E. 2544 **cl. 83–100**? | `TH_BMA` profile promotion | Lawyer / BMA building-control officer — *partial: no amendment found in search; not proof of absence* | Phase 3 |
| OQ-04 | May adjacent accessible bays **share one 1.00 m clear strip**? | Accessible allocation geometry (default policy: one strip per bay) | Accessibility / building-control lawyer — *no published interpretation found* | Phase 2 |
| OQ-05 | May any part of a No. 33 **fire-access corridor** be used for marked parking? | Fire keep-out semantics (full keep-out as conservative policy) | Fire / building-control specialist — *no published interpretation found* | Phase 3 |
| OQ-06 | Are there municipal or project-class **motorcycle** stall dimensions or ratios to include? | Motorcycle rules (project policy only) | Legal researcher + domain engineer — *partial: no general building-control rule found* | Phase 3 |
| OQ-07 | Has any Thai law introduced mandatory **EV** parking ratios? Re-check before release. | EV rules (project policy only) | Legal / electrical engineer — *partial: no enacted general quota found as of 2026-10-24* | Before v1.0 |
| OQ-08 | Primary texts: **links obtained** (TH_RULESET_DRAFT §0); no numeric mismatch reported. Remaining: a person opens the PDFs to confirm values, and the Gazette headers for No. 33 and BMA 2544. | Promoting values to `cross-checked` | Bosskung | Phase 1 |

## Geospatial

| ID | Question | Blocks | Owner | Needed by |
|---|---|---|---|---|
| OQ-09 | Which **Indian 1975 → WGS 84 operation** do the user's legacy drawings actually assume? | Default operation for EPSG:24047/24048 | Bosskung / survey engineer | Phase 4 |
| OQ-10 | Support **locally fitted Helmert / similarity transforms** from survey control in addition to EPSG operations? | Aligned-CAD workflow scope | Bosskung + geospatial engineer | Phase 4 |
| OQ-11 | Which **satellite/aerial provider** may a hosted deployment use? *Partial:* public standard terms of Google Maps Platform, MapTiler and Mapbox do not cleanly permit trace + cache + PDF; Google is unsuitable as default tracing source. Architecture answer: provider-neutral capability flags (SPEC MAP-6). Remaining: pick a provider / contract. | Enabling satellite in a hosted deployment | Product owner + legal | Phase 4 |
| OQ-12 | May map imagery appear in **exported PDFs**? *Partial:* tracing itself can be restricted, not only export. Default: geometry-only PDF; imagery in PDF only where the provider grants it (SPEC MAP-6, OUT-4). | OUT-4 with imagery | Product owner + legal | Phase 4 |

## Technical

| ID | Question | Blocks | Owner | Needed by |
|---|---|---|---|---|
| OQ-13 | Which DXF library (**`dxf` 0.6.2 vs `acadrust` 0.6.6**) passes the Stallwise fixture set under `wasm32`? | DXF ADR | Stallwise engineering | Phase 3 (bake-off) |
| OQ-14 | Is **DWG** a browser requirement or only a CAD-host concern? | Weight of acadrust's DWG support | Product owner | Phase 3 |
| OQ-15 | Does `geo` 0.33.1 pass the polygon **torture suite** vs direct `i_overlay` / Clipper? | Accepting ADR-0005 | Stallwise engineering | End of Phase 1 |
| OQ-16 | Use the **325-lot NYC corpus** (Thomas & Rambha, arXiv 2506.09961)? *Partial (checked):* `transnetlab/parking-lot-design` has no licence, lists 325 lot IDs, ships only an example CSV. Plan: rebuild from NYC Open Data after checking its terms; never vendor the unlicensed code. | Phase 6 benchmarking | Research / engineering | Phase 6 |

## Product

| ID | Question | Blocks | Owner | Needed by |
|---|---|---|---|---|
| OQ-17 | What are real Thai **project sizes** (area, vertices, obstacles, stall count)? | Re-setting NFR-2 | Bosskung — collect anonymised metadata | Before v1.0 |
| OQ-18 | What **parking schedule** does a real Bangkok permit submission need? | OUT-1 compliance ledger format | Bosskung / architect / permit consultant | Phase 3 |
| OQ-19 | Does the first CAD integration need an **embedded UI**, or is "select boundary → run → insert" enough? | Phase 5 host choice | Bosskung | Phase 5 gate |
| OQ-20 | Confirm Phase 5 order **IngeCAD → CADCraft → IngeTrazo**? | Phase 5 plan | Bosskung | Phase 5 gate |
| OQ-21 | What compatibility promise for adapters against young / unstable host APIs? | Adapter maintenance policy | Engineering + host maintainers | Phase 5 |
| OQ-22 | Require a **CLA** for contributions to keep relicensing options open? | Contribution policy | Bosskung | Before accepting external PRs |
