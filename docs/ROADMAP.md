# Stallwise — Roadmap

- **Document status:** Draft v0.2 (Phase 0)
- Each phase ends with explicit **exit criteria**. A phase is not done until all of them pass in CI or are signed off.
- Durations are not fixed; phases are ordered by dependency.

---

## Phase 0 — Specification and planning ◀ current

**Goal:** Agree what to build and how, before writing code.

- [x] Repository created, AGPL-3.0-or-later licence
- [x] Draft SPEC, ARCHITECTURE, ROADMAP, ADRs, research brief
- [x] Research pass answers `RESEARCH_BRIEF.md` ([report](research/2026-10-24-phase0-deep-research.md))
- [x] SPEC and ARCHITECTURE v0.2 drafted from research findings
- [x] Thai rule dataset drafted with citation and status per value ([TH_RULESET_DRAFT](rules/TH_RULESET_DRAFT.md))
- [x] Open questions logged with owner and deadline ([OPEN_QUESTIONS](OPEN_QUESTIONS.md))
- [x] Proposed ADRs 0005–0009
- [ ] Owner review of v0.2 documents
- [ ] Draft JSON Schema v0 for project / site / rule set / layout

**Exit criteria:** v0.2 documents reviewed by the owner; every Thai numeric rule is citation-complete or explicitly `unverified`; legal review list exists (OQ-01…OQ-08).

---

## Phase 1 — Core engine: single-module layouts

**Goal:** A Rust crate that generates valid 90° layouts on simple polygons.

- Cargo workspace; `crates/core` with CI (fmt, clippy, test, `cargo-deny`)
- Geometry primitives, parkable-region construction (setback, obstacles)
- Double- and single-loaded modules, 90°, two-way; default project standard 2.50 × 5.00 m stalls
- Orientation search (1° sweep + dominant edge bearings) and event-derived offsets
- Complete-stall placement only; aisles as first-class geometry; circulation graph (GEN-R2)
- Lexicographic scoring (SPEC §5.3)
- Rule engine: profiles `TH_NATIONAL` / `TH_BMA`, project-standard layer (RS-6), statuses (RS-4), provenance on generated elements (RS-3), accessible **count** calculation
- Fixtures: analytic rectangles (known optimum), sub-stall remainder, rotated rectangle, L-shape, trapezoid, holes, narrow throat (connectivity), sliver polygon, large UTM-like coordinates, boundary-touching stall
- Rule fixtures: BMA 90° (aisle ≥ 6.00 m), national perpendicular + one-way → error, accessible counts at 25/26, 50/51, 100/101, 150/151, 200/201/251, national 30° → `unverified_rule`, BMA 30° → 5.50 m aisle category
- Polygon torture suite; benchmark `geo` against direct `i_overlay` and `clipper2` (OQ-15)
- Property tests: no overlaps, translation/rotation invariance, determinism
- Benchmarks on fixtures

**Exit criteria:** Zero overlaps / out-of-region stalls (1 mm internal tolerance); every retained stall reachable; exact optimum on analytic rectangles; golden counts stable; invalid input never panics; every rule result carries profile version and clause; < 1 s native per fixture; licence manifest clean; ADR-0005 accepted or replaced.

---

## Phase 2 — Angles, circulation, CLI, WASM

**Goal:** Full parameter set in the engine and the first two shells.

- Angled parking (60°, 45°, 30° — national exact-30° gated by OQ-01), parallel parking, one-way aisles (gated by OQ-02 for perpendicular)
- Access points; aisle graph; connectivity validation GEN-R2; dead-end detection
- Stall types: accessible allocation with geometric clear-strip check (OQ-04); EV, compact, motorcycle as project policy
- Scoring with explainable components
- `crates/cli`: `generate`, `validate`, `serve --stdio`
- `crates/wasm`: generate/validate in a Web Worker with progress and cancel
- JSON Schema v1 frozen for the MVP; schema round-trip tests

**Exit criteria:** CLI and WASM produce byte-identical results for all fixtures; connectivity check catches seeded failures; schema v1 tagged.

---

## Phase 3 — Web app MVP (Local mode)

**Goal:** Usable end-to-end in the browser without a map.

- React + Vite app shell, Thai/English UI, "Source" link (AGPL §13)
- **DXF bake-off first:** Rust `dxf` vs `acadrust` under `wasm32` on a fixture corpus ($INSUNITS, layers, blocks/inserts, bulges/arcs, malformed files, round-trip export) → DXF ADR (OQ-13, OQ-14)
- DXF import: unit confirmation, layer selection, clean-up report
- Local canvas: draw/edit boundary, obstacles, access points
- Parameter panel: jurisdiction profile + project standard; draft labels per RS-4; use program for supply calculation
- Compliance ledger output (OUT-1)
- Generate, compare options, stall summary
- Editing: select/move/delete/add stalls, edit aisles, lock zones, regenerate unlocked areas, undo/redo
- Export: DXF (source coordinates, layered), PDF/PNG, project JSON
- Local persistence (browser storage + file save/open)

**Exit criteria:** SPEC §11 acceptance criteria 1, 3, 4, 5 pass; Playwright end-to-end test import → generate → lock → regenerate → export.

---

## Phase 4 — Map mode and georeferencing

**Goal:** Work on a real-world map.

- MapLibre base map, configurable providers, place search
- Map drawing (Terra Draw); auto UTM zone
- Georeferenced CAD import with CRS presets incl. EPSG:24047/24048, datum-operation choice and accuracy warnings (ADR-0008, OQ-09)
- Aligned CAD: control-point pairs, rigid transform, residuals/RMS, manual fine-tune; locally fitted Helmert if OQ-10 says yes
- GeoJSON export
- Precision: local-origin shift; same-CRS numeric round-trip ≤ 1 mm; datum fixtures at published accuracy
- Imagery capability flags (SPEC MAP-6); satellite layer only after provider terms review (OQ-11, OQ-12); geometry-only PDF by default

**Exit criteria:** SPEC §11 acceptance criterion 2 passes; aligned-CAD export overlays the original DXF exactly; imagery licence notes documented.

---

## Phase 5 — CAD plugin(s)

**Decision gate at start of phase:** confirm order (current evidence suggests **IngeCAD → CADCraft → IngeTrazo**, ADR-0009) re-checked against each project's state at that time (OQ-19…OQ-21).

- Plugin adapters over `stallwise-cli serve --stdio`
- Python adapter shared by IngeTrazo and IngeCAD (if both chosen)
- CADCraft adapter via its JSON control channel / CLI
- Licence review per host

**Exit criteria:** For each chosen host: select boundary → generate → layout drawn as native entities on proper layers → round-trip edit and regenerate.

---

## Phase 6 — Beyond surface lots (candidate)

- Multi-zone decomposition → per-zone orientation → local row shifts → angle changes → circulation-aware neighbourhood search, measured against the Phase 1 baseline
- Small-instance MIP / branch-and-cut oracle for 90° cases; metaheuristic only if justified
- External benchmark: rebuild the 325-lot NYC set from NYC Open Data (record URL, terms, retrieval date) using the published ID list; store references or clearly licensed fixtures only; do not copy the unlicensed research code (OQ-16)
- Multi-storey structures: floor plates, column grids, ramps
- Swept-path checks with vehicle templates (possible link to a vehicle-dimension database)
- IFC export

Scope to be decided after Phase 5.
