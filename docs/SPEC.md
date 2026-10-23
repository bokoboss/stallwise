# Stallwise — Product Specification

- **Document status:** Draft v0.1 (Phase 0)
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
- **IN-R7** Common CRSs for Thailand MUST be offered as presets: WGS 84 / UTM 47N (EPSG:32647), WGS 84 / UTM 48N (EPSG:32648). Legacy Indian 1975 UTM zones SHOULD be offered; exact EPSG codes and datum transformation parameters are a research item (see RESEARCH_BRIEF).

### 4.2 Site elements

- Boundary: one outer polygon; holes allowed.
- Setback: uniform distance, or per-edge distances.
- Obstacles: polygons, circles (columns/trees) and polylines with a buffer width.
- Access points: a point or segment on the boundary, with type (entry / exit / both) and lane count.
- No-parking zones: areas where aisles are allowed but stalls are not (e.g. fire lanes, drop-off).

### 4.3 Design parameters

| Parameter | Type | Notes |
|---|---|---|
| Stall width, depth | metres | Per stall type |
| Parking angle | 90°, 60°, 45°, 30°, 0° (parallel) | 30° optional |
| Aisle width | metres | Per angle and per one-way/two-way; defaults come from the active rule set |
| Circulation | one-way / two-way | One-way only valid for angled parking |
| Stall types | standard, accessible, compact, EV, motorcycle | Each with dimensions and required count or ratio |
| Layout orientation | auto search, or fixed angle | |
| End islands / landscaping | optional | Spacing, size |
| Search resolution | degrees, metres | Trade-off between quality and time |

Rule sets:

- **RS-1** Parameters MUST be grouped into named, versioned rule sets. Users MAY create custom rule sets.
- **RS-2** A Thai regulatory rule set will be provided, **but every value in it MUST cite the specific regulation, clause and edition**, and MUST be verified before it is marked as non-draft. Until verified, the app labels it "Draft — verify against current regulations".
- **RS-3** Each project MUST record which rule set and version produced each layout.

## 5. Layout generation

### 5.1 Baseline algorithm (Phase 1–2)

1. Build the parkable region: boundary ⊖ setback ⊖ obstacles (with buffers).
2. For each candidate orientation θ (configurable step, default 1°) and each strip offset (configurable step):
   1. Tile the region with parallel modules perpendicular to θ.
   2. Clip each module to the region; place stalls along bays where the full stall footprint fits.
   3. Remove stalls whose aisle is not connected to an access point.
3. Score each candidate (§5.3); keep the best N.
4. Post-process: end islands, accessible stalls nearest to the designated location, perimeter stalls along edges where they fit.

### 5.2 Later improvements (Phase 3+)

- Multi-zone layouts: split irregular sites into sub-regions with different orientations.
- Perimeter loop aisle + interior modules.
- Heuristic / metaheuristic search (e.g. simulated annealing, genetic algorithm) over zone splits.
- Constraint-based partial regeneration around locked elements.

### 5.3 Scoring

The score MUST be explainable — the app shows each component, not only the total.

| Component | Direction |
|---|---|
| Usable stall count (by type) | maximise |
| Required counts met (accessible, EV, …) | hard constraint |
| Dead-end aisles | minimise (penalty), or forbid |
| Aisle length per stall | minimise |
| Connectivity: every stall reachable from an entry and to an exit | hard constraint |
| Turning feasibility at aisle ends | hard constraint (simplified check in Phase 2) |

### 5.4 Validity requirements

- **GEN-R1** No stall or aisle may overlap an obstacle, another stall, or leave the parkable region (tolerance configurable, default 1 mm).
- **GEN-R2** Every stall MUST be reachable via the aisle graph from at least one entry and to at least one exit, respecting one-way direction.
- **GEN-R3** Generation MUST be deterministic: same input + same rule set + same engine version → identical output.
- **GEN-R4** Generation MUST be cancellable from the UI and MUST report progress.

## 6. Editing

- **ED-1** Select, move, delete and add individual stalls; snap to bays.
- **ED-2** Draw, move and delete aisles; stalls re-fill along edited aisles.
- **ED-3** Lock a zone (polygon) or individual elements. Regeneration MUST NOT alter locked elements and MUST treat them as obstacles/fixed aisles.
- **ED-4** Every edit is re-validated live against GEN-R1/R2; violations are highlighted, not silently fixed.
- **ED-5** Unlimited undo/redo within a session.
- **ED-6** Keep multiple named layout options per project and compare them side by side.

## 7. Outputs

| ID | Output | Notes |
|---|---|---|
| OUT-1 | Stall summary | Count by type, by zone; ratio to site area; required vs provided |
| OUT-2 | DXF | Separate layers for stalls, aisles, markings, islands, annotations, access; in source coordinates (IN-R5) |
| OUT-3 | GeoJSON | WGS 84 for web/GIS use (only when georeferenced) |
| OUT-4 | PDF / PNG | Scaled plan with title block and summary table |
| OUT-5 | Project file | JSON per `schemas/`, includes inputs, rule set, layouts, engine version |

## 8. Map mode

- **MAP-1** Base map via MapLibre GL JS. Default basemap MUST be one whose licence permits the intended use (open data such as OpenStreetMap-derived tiles). Satellite imagery providers are configurable; their terms of use are the deployer's responsibility and MUST be documented.
- **MAP-2** Place search (geocoding) through a configurable provider.
- **MAP-3** Drawing tools for boundary, obstacles, access points.
- **MAP-4** The app MUST state that imagery-based tracing is approximate and suitable for feasibility only.
- **MAP-5** Projected CRS is selected automatically from the site centroid (UTM zone) and can be overridden.

## 9. CAD integration

- **CAD-1** DXF import/export is the universal integration and ships before any plugin.
- **CAD-2** `stallwise-cli` accepts a project/site JSON and returns layout JSON, so any CAD program can call the engine as a separate process.
- **CAD-3** Plugin targets (decision deferred to Phase 5): **IngeTrazo**, **IngeCAD**, **CADCraft**. See ADR-0004.

## 10. Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-1 | Runs fully in the browser; no server needed for computation. Project data stays on the user's device unless they export it. |
| NFR-2 | Generation for a typical site (≤ 2 ha, ≤ 50 boundary vertices, ≤ 20 obstacles) completes within 5 s on a mid-range laptop at default resolution. (Target; to be benchmarked in Phase 1.) |
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
5. All outputs carry the engine version and rule-set version.

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
| Regulatory values entered wrongly | Citation required per value; draft label until verified; rule-set versioning |
| Satellite imagery licensing | Configurable providers; open default; deployer responsibility documented |
| Plugin host APIs are young and may change | Plugins are thin adapters over the CLI/JSON contract; decision deferred |
| Optimisation runtime on large sites | Coarse-to-fine search; Web Worker; cancellation; benchmarks in CI |
