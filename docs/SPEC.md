# Stallwise — Product Specification

- **Document status:** Draft v0.3 (Phase 0) — revised with Phase 0 research ([first](research/2026-10-24-phase0-deep-research.md), [focused](research/2026-10-24-phase0-focused-research.md))
- **Scope of this version:** Surface (single-level) parking lots. Multi-storey structures are out of scope until Phase 6.
- **Normative language:** MUST / SHOULD / MAY as in RFC 2119.

---

## 1. Purpose

Stallwise produces parking-lot layouts automatically from a site boundary and a set of design rules, and lets the designer edit the result without losing the automation. It is intended for **concept and feasibility design**: quickly answering "how many stalls fit, and in what arrangement?" and producing a layout that can be taken into CAD for detailed design.

It is not a substitute for detailed design, survey, or regulatory approval. Every output MUST be reviewed by a qualified engineer or architect.

## 2. Users and primary use cases

| User | Typical question |
|---|---|
| Traffic / transport engineer | How many stalls does this site yield under the applicable rules? Does it meet the required supply? |
| Architect / planner | Which building footprint leaves the most parking? What does each layout option look like? |
| Developer / client advisor | What is the parking yield of this plot, roughly, before commissioning design? |

Use cases:

- **UC-1 Feasibility from a map.** Find a site on a map, trace the boundary, generate a layout, read the stall count.
- **UC-2 Layout from survey CAD.** Import a DXF of the plot, generate a layout, export the layout as DXF back into the same drawing.
- **UC-3 Option comparison.** Generate several layouts (different angles, one-way vs two-way) and compare yield and circulation.
- **UC-4 Constrained redesign.** Keep part of an existing layout fixed and regenerate the rest.

## 3. Glossary

| Term | Meaning |
|---|---|
| **Site** | The parkable region: boundary polygon minus setbacks and obstacles. |
| **Obstacle** | Area where stalls and aisles cannot go (building, tree, column, utility). |
| **Stall** | One parking space, defined by width, depth and angle. |
| **Aisle** | Drive lane giving access to stalls. One-way or two-way. |
| **Module** | Repeating strip: stall row + aisle + stall row (double-loaded) or stall row + aisle (single-loaded). |
| **Bay** | A run of stalls along one side of an aisle. |
| **Access point** | Entry, exit, or combined entry/exit on the site boundary. |
| **Rule set** | A named, versioned set of dimensional parameters and requirements (e.g. a Thai regulatory profile). |
| **Jurisdiction profile** | A rule set encoding law for one jurisdiction, e.g. `TH_NATIONAL`, `TH_BMA`. Values are legal minimums/maximums. |
| **Project design standard** | The designer's own dimensions (e.g. 2.50 × 5.00 m stalls), layered over a jurisdiction profile. Must satisfy it. |
| **Keep-out** | Area where stalls are forbidden, optionally aisles too (fire access, clear strips, user zones). |
| **Lock** | User marking that a zone or element must not be changed by regeneration. |

## 4. Inputs

### 4.1 Site acquisition modes

| ID | Mode | Description | Coordinate frame |
|---|---|---|---|
| IN-1 | **Local** | Import DXF, or draw on a blank canvas. No map. | The file's own coordinates (or canvas metres) |
| IN-2 | **Georeferenced CAD** | Import DXF already in a projected CRS; user declares the CRS (EPSG code). | Declared CRS |
| IN-3 | **Map draw** | Draw boundary/obstacles on a web map. | Auto-selected projected CRS (UTM zone of the site) |
| IN-4 | **Aligned CAD** | Import a floating DXF and align it to the map with control-point pairs. | File's own coordinates + stored transform |

Requirements:

- **IN-R1** All layout computation MUST happen in a metric, planar frame. Latitude/longitude MUST NOT be passed to the engine.
- **IN-R2** For DXF, the importer MUST read `$INSUNITS`, propose a unit, and require the user to confirm it before generation.
- **IN-R3** For IN-4, alignment MUST default to a **rigid transform (translate + rotate, scale locked to 1)**. Free scale MAY be offered behind an explicit toggle with a warning.
- **IN-R4** For IN-4 with ≥ 3 point pairs, the app MUST show per-point residuals and the RMS error, and warn when RMS exceeds a configurable threshold (default 0.5 m).
- **IN-R5** Geometry MUST be stored in its source frame with the transform kept separately, so DXF export lands at the original CAD coordinates regardless of map alignment.
- **IN-R6** The DXF importer MUST let the user choose which layers/entities become boundary, obstacles and access points, and MUST report geometry it could not use (open polylines, self-intersections, unsupported entities).
- **IN-R7** CRS presets for Thailand MUST include WGS 84 / UTM 47N (EPSG:32647), WGS 84 / UTM 48N (EPSG:32648), Indian 1975 / UTM 47N (EPSG:24047) and Indian 1975 / UTM 48N (EPSG:24048). For Indian 1975, the user MUST choose (or accept a default) **datum operation**, and the app MUST state its published accuracy — EPSG operations for Thailand are **metre-class (≈1–5 m)**, not survey-grade (ADR-0008).
- **IN-R8** Every CRS conversion MUST record `source_crs`, `target_crs`, datum operation id/name, declared operation accuracy (m), control-point residuals if fitted, and provenance. The app MUST warn when declared accuracy exceeds a user threshold.

### 4.2 Site elements

- Boundary: one outer polygon; holes allowed.
- Setback: uniform distance, or per-edge distances.
- Obstacles: polygons, circles (columns/trees) and polylines with a buffer width.
- Access points: a point or segment on the boundary, with type (entry / exit / both) and lane count.
- No-parking zones: areas where aisles are allowed but stalls are not (e.g. drop-off).
- Keep-outs: `fire_access_keepout` (conditional, No. 33 B.E. 2535 for applicable buildings — not applied to ordinary lots; full keep-out is a conservative project policy, flagged as such), accessible clear strips, user zones. Exported on their own layers.
- Each rule carries a `basis`: `statute` (cited law) or `project_policy` (Stallwise or user choice where the law is silent or unclear), shown in the compliance ledger.

### 4.3 Design parameters

| Parameter | Type | Notes |
|---|---|---|
| Stall width, depth | metres | Per stall type; from the project design standard, checked against the jurisdiction minimum |
| Parking angle | 90°, 60°, 45°, 30°, 0° (parallel) | Exactly 30° is blocked under `TH_NATIONAL` until OQ-01 is resolved (RS-5) |
| Aisle width | metres | Per angle and per one-way/two-way; from the project standard, checked against the jurisdiction minimum where one exists |
| Circulation | one-way / two-way | One-way only valid for angled parking |
| Stall types | standard, accessible, compact, EV, motorcycle | Accessible = base stall **+ separate side clear strip** (not a widened stall). EV and motorcycle are project policy only (no verified Thai rule). |
| Layout orientation | auto search, or fixed angle | |
| End islands / landscaping | optional | Spacing, size |
| Search resolution | degrees, metres | Trade-off between quality and time |

Rule sets:

- **RS-1** Parameters MUST be grouped into named, versioned rule sets with metadata `{id, version, jurisdiction, authority, title, edition_year_be, as_of, citations[], status}`. Users MAY create custom rule sets.
- **RS-2** Thai law is provided as **two separate jurisdiction profiles**: `TH_NATIONAL` and `TH_BMA`. Each value cites regulation, clause and edition. Draft dataset: [`docs/rules/TH_RULESET_DRAFT.md`](rules/TH_RULESET_DRAFT.md). Parking-supply formulas are modelled as a rule tree: `jurisdiction → use applicability → supply formula → geometric rules → accessibility / fire overlays`. Supply is never inferred from site area alone.
- **RS-3** Each project MUST record which rule set(s) and versions produced each layout, and each generated element MUST carry the provenance of the rules that sized it (e.g. "BMA B.E. 2544 cl. 88, angle > 60°").
- **RS-4** Each regulatory value has a status: `unverified`, `cited`, `cross-checked` or `legally-reviewed`. An `unverified` rule returns `unverified_rule` and requires a project value; the engine MUST NOT substitute another jurisdiction's value. Anything below `legally-reviewed` is labelled **Draft — verify** in UI and outputs.
- **RS-5** Angle intervals have explicit boundary semantics per profile. Under `TH_NATIONAL`, exactly 30° is `unverified` until OQ-01 is answered; `TH_BMA` uses its own intervals as written.
- **RS-6** **Project design standard.** The designer's dimensions are a separate layer over the jurisdiction profile. Every project value MUST satisfy the profile (e.g. stall width ≥ legal minimum); a value below the minimum is a validation error, not a silent override. The built-in default project standard is **stall 2.50 × 5.00 m for 90° parking** (the project owner's usual design practice, above the 2.40 m legal minimum); other defaults are filled from the profile minimums until the user sets them.
- **RS-7** Prohibited combinations in the active profile are rejected at validation, e.g. perpendicular stalls with one-way circulation under `TH_NATIONAL` (No. 41 cl. 2(2)), pending legal interpretation OQ-02.

## 5. Layout generation

### 5.1 Baseline algorithm (Phase 1–2)

1. Build the parkable region: boundary ⊖ setback ⊖ obstacles (with buffers).
2. For each candidate orientation θ — a 1° sweep over [0°, 90°) for 90° stalls **plus** the bearings of dominant site edges — and each strip offset derived from projected boundary/obstacle vertices modulo module depth (not a fixed metric grid):
   1. Tile the region with parallel modules perpendicular to θ.
   2. Place **only complete stalls** whose full footprint fits; never count clipped fragments.
   3. Remove stalls whose aisle is not connected to an access point.
3. Score each candidate lexicographically (§5.3); keep the best N.
4. Post-process: compute required accessible count from the profile, then allocate accessible stalls deterministically by route distance to the accessible entrance, checking clear strips geometrically; end islands; perimeter stalls where they fit.

### 5.2 Later improvements (Phase 3+)

- Multi-zone layouts: split irregular sites into sub-regions with different orientations.
- Perimeter loop aisle + interior modules.
- Local neighbourhood search (row shifts, per-zone orientation, angle changes), benchmarked against a small-instance MIP / branch-and-cut oracle; a metaheuristic only if those prove insufficient.
- Constraint-based partial regeneration around locked elements.

### 5.3 Scoring

Phase 1–2 scoring is **lexicographic**, with no hidden weights, so fixture failures are explainable:

1. Maximise compliant stall count.
2. Minimise unreachable / discarded modules.
3. Minimise aisle length or fragmentation.
4. Deterministic tie-break on orientation, then offset.

Hard constraints (never traded off): GEN-R1, GEN-R2, required counts by type, profile prohibitions (RS-7). Weighted multi-objective scores MAY be added in Phase 6 with every component shown.

### 5.4 Validity requirements

- **GEN-R1** No stall or aisle may overlap an obstacle, keep-out, another stall, or leave the parkable region. Tolerance default 1 mm — an **internal planar geometry tolerance**, not a statement about real-world/geodetic accuracy.
- **GEN-R2** Aisles are first-class geometry. Every stall MUST map to a serving aisle component, and every aisle component MUST reach at least one declared entry and one exit through the circulation graph, respecting one-way direction. Unreachable stalls are removed and reported.
- **GEN-R3** Generation MUST be deterministic: same input + same rule set + same engine version → identical output.
- **GEN-R4** Generation MUST be cancellable from the UI and MUST report progress.
- **GEN-R5** Invalid input (self-intersecting, degenerate) returns a structured error or repair warning — never a panic.

## 6. Editing

- **ED-1** Select, move, delete and add individual stalls; snap to bays.
- **ED-2** Draw, move and delete aisles; stalls re-fill along edited aisles.
- **ED-3** Lock a zone (polygon) or individual elements. Regeneration MUST NOT alter locked elements and MUST treat them as obstacles/fixed aisles.
- **ED-4** Every edit is re-validated live against GEN-R1/R2; violations are highlighted, not silently fixed.
- **ED-5** Unlimited undo/redo within a session.
- **ED-6** Keep multiple named layout options per project and compare them side by side.
- **ED-7** Regeneration MUST preserve the IDs of unaffected and locked elements, so iterative editing and CAD round-trips stay stable.
- **ED-8** Priority interactions: regenerate selected zone, lock/unlock zone, move/delete/add stall, change row angle, convert stall type, move/resize keep-out, edit aisle/entry.

## 7. Outputs

| ID | Output | Notes |
|---|---|---|
| OUT-1 | Stall summary + **compliance ledger** | Counts by type/zone; required vs provided by use with the clause behind each requirement; rule-set id/version/status; accessible stall and clear-strip schedule; entries/exits and keep-outs; site, parking and circulation areas; assumptions and every `unverified` rule. It supports professional review; it is not an official filing. |
| OUT-2 | DXF | Separate layers for stalls, aisles, markings, islands, annotations, access; in source coordinates (IN-R5) |
| OUT-3 | GeoJSON | WGS 84 for web/GIS use (only when georeferenced) |
| OUT-4 | PDF / PNG | Scaled plan with title block and summary table. Third-party imagery is **excluded by default** and included only when the source's `may_export_pdf` / `may_export_raster` is true, with its attribution. |
| OUT-5 | Project file | JSON per `schemas/`, includes inputs, rule set, layouts, engine version |

## 8. Map mode

- **MAP-1** Base map via MapLibre GL JS; tile, style and imagery providers are configuration, not architecture (ADR-0007). The public `tile.openstreetmap.org` service MUST NOT be the production default (OSMF tile policy). Satellite imagery is opt-in, per-provider (key + attribution), and **off by default** until a provider's terms are reviewed (OQ-11).
- **MAP-2** Place search (geocoding) through a configurable provider.
- **MAP-3** Drawing tools for boundary, obstacles, access points.
- **MAP-4** The app MUST state that imagery-based tracing is approximate and suitable for feasibility only.
- **MAP-5** Projected CRS is selected automatically from the site centroid (UTM zone) and can be overridden.
- **MAP-6** **Imagery capability contract.** Every imagery source is configured with explicit flags: `may_display`, `may_cache_client`, `may_cache_server`, `may_trace_or_derive`, `may_export_pdf`, `may_export_raster`, `attribution_required`, `max_cache_duration`, `contract_reference`, `terms_checked_at`. The app enables an operation (tracing, caching, export) only when the active source permits it. Customer-owned or separately licensed orthophoto / XYZ / WMTS / WMS sources are first-class. Google Maps Platform imagery is not a default tracing source.

## 9. CAD integration

- **CAD-1** DXF import/export is the universal integration and ships before any plugin.
- **CAD-2** `stallwise-cli` accepts a project/site JSON and returns layout JSON, so any CAD program can call the engine as a separate process.
- **CAD-3** Plugin targets: **IngeCAD**, **CADCraft**, **IngeTrazo**; final order decided at the Phase 5 gate (ADR-0009, OQ-20).

## 10. Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-1 | Runs fully in the browser; no server needed for computation. Project data stays on the user's device unless they export it. |
| NFR-2 | **Initial benchmark tier** (an assumption, not measured Thai data — see OQ-17): site ≤ 2 ha, ≤ 50 boundary vertices, ≤ 20 obstacles generates within 5 s on a mid-range laptop at default resolution. |
| NFR-3 | UI stays responsive during generation (computation in a Web Worker). |
| NFR-4 | Bilingual UI: Thai and English. |
| NFR-5 | Works in current Chrome, Edge, Firefox and Safari. Desktop-first; tablet usable for viewing. |
| NFR-6 | Visible "Source" link to the corresponding source code (AGPL §13). |
| NFR-7 | Engine version and rule-set version are embedded in every export. |

## 11. Acceptance criteria — MVP (end of Phase 3)

1. A user can import a DXF plot, confirm units, select boundary and obstacle layers, generate a 90° two-way layout, and export DXF that overlays the source drawing exactly.
2. A user can trace a site on a map, generate a layout, and read the stall summary.
3. A user can lock one zone, change parameters, regenerate, and the locked zone is unchanged.
4. For the reference test sites in `crates/core/tests/fixtures/` (to be created in Phase 1), generated layouts pass all validity checks (GEN-R1/R2) and stall counts are within an agreed tolerance of hand-checked reference layouts.
5. All outputs carry the engine version, rule-set ids/versions/status, and a compliance ledger (OUT-1).
6. With `TH_BMA` and the default project standard, a 90° two-way layout uses 2.50 × 5.00 m stalls and aisles ≥ 6.00 m; setting a stall width below 2.40 m is rejected (RS-6).

## 12. Out of scope (for now)

- Multi-storey parking structures, ramps, structural grids (Phase 6+).
- Vehicle swept-path simulation beyond a simplified turning check.
- Drainage, grading, lighting, pavement design.
- Cost estimation.
- Cloud accounts, multi-user collaboration.

## 13. Risks

| Risk | Mitigation |
|---|---|
| Real-world DXF is messy (open polylines, mixed layers, wrong units) | Dedicated clean-up step; explicit user confirmation; clear error report |
| "Max stalls" layouts may be poor to drive | Circulation terms in the score; dead-end penalty; user review |
| Regulatory values entered wrongly or out of date | Citation per value; four-level status (RS-4); separate national/BMA profiles; legal review list in OPEN_QUESTIONS |
| False precision from legacy datums | Datum operation + accuracy recorded and shown (IN-R7/R8) |
| Satellite imagery licensing | Configurable providers; open default; deployer responsibility documented |
| Plugin host APIs are young and may change | Plugins are thin adapters over the CLI/JSON contract; decision deferred |
| Optimisation runtime on large sites | Coarse-to-fine search; Web Worker; cancellation; benchmarks in CI |
