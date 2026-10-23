# Stallwise — Roadmap

- **Document status:** Draft v0.1 (Phase 0)
- Each phase ends with explicit **exit criteria**. A phase is not done until all of them pass in CI or are signed off.
- Durations are not fixed; phases are ordered by dependency.

---

## Phase 0 — Specification and planning ◀ current

**Goal:** Agree what to build and how, before writing code.

- [x] Repository created, AGPL-3.0-or-later licence
- [x] Draft SPEC, ARCHITECTURE, ROADMAP, ADRs, research brief
- [ ] Research pass (external review) answers the questions in `RESEARCH_BRIEF.md`
- [ ] Spec and architecture updated with research findings
- [ ] Technology choices confirmed (ADR per major choice)
- [ ] Draft JSON Schema v0 for project/site/layout

**Exit criteria:** SPEC v0.2 and ARCHITECTURE v0.2 reviewed; open questions either answered or explicitly deferred with an owner and phase.

---

## Phase 1 — Core engine: single-module layouts

**Goal:** A Rust crate that generates valid 90° layouts on simple polygons.

- Cargo workspace; `crates/core` with CI (fmt, clippy, test, `cargo-deny`)
- Geometry primitives, parkable-region construction (setback, obstacles)
- Double- and single-loaded modules, 90°, two-way
- Orientation and offset search
- Validity checks GEN-R1 (no overlap, inside region)
- Reference fixtures: rectangle, L-shape, trapezoid, site with holes; hand-checked stall counts
- Property tests: no overlaps, determinism
- Benchmarks on fixtures

**Exit criteria:** All fixtures pass validity; counts match hand-checked references within agreed tolerance; generation for each fixture < 1 s native.

---

## Phase 2 — Angles, circulation, CLI, WASM

**Goal:** Full parameter set in the engine and the first two shells.

- Angled parking (60°, 45°, 30°), parallel parking, one-way aisles
- Access points; aisle graph; connectivity validation GEN-R2; dead-end detection
- Stall types and required counts (accessible, EV, compact, motorcycle)
- Scoring with explainable components
- `crates/cli`: `generate`, `validate`, `serve --stdio`
- `crates/wasm`: generate/validate in a Web Worker with progress and cancel
- JSON Schema v1 frozen for the MVP; schema round-trip tests

**Exit criteria:** CLI and WASM produce byte-identical results for all fixtures; connectivity check catches seeded failures; schema v1 tagged.

---

## Phase 3 — Web app MVP (Local mode)

**Goal:** Usable end-to-end in the browser without a map.

- React + Vite app shell, Thai/English UI, "Source" link (AGPL §13)
- DXF import: unit confirmation, layer selection, clean-up report
- Local canvas: draw/edit boundary, obstacles, access points
- Parameter panel with rule sets (Thai draft profile clearly labelled)
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
- Georeferenced CAD import with CRS presets
- Aligned CAD: control-point pairs, rigid transform, residuals/RMS, manual fine-tune
- GeoJSON export
- Precision: local-origin shift; CRS round-trip ≤ 1 mm

**Exit criteria:** SPEC §11 acceptance criterion 2 passes; aligned-CAD export overlays the original DXF exactly; imagery licence notes documented.

---

## Phase 5 — CAD plugin(s)

**Decision gate at start of phase:** choose order among **IngeTrazo**, **IngeCAD**, **CADCraft** using the criteria in ADR-0004, re-checked against each project's state at that time.

- Plugin adapters over `stallwise-cli serve --stdio`
- Python adapter shared by IngeTrazo and IngeCAD (if both chosen)
- CADCraft adapter via its JSON control channel / CLI
- Licence review per host

**Exit criteria:** For each chosen host: select boundary → generate → layout drawn as native entities on proper layers → round-trip edit and regenerate.

---

## Phase 6 — Beyond surface lots (candidate)

- Multi-zone optimisation and metaheuristic search
- Multi-storey structures: floor plates, column grids, ramps
- Swept-path checks with vehicle templates (possible link to a vehicle-dimension database)
- IFC export

Scope to be decided after Phase 5.
