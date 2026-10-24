# Stallwise — Architecture

- **Document status:** Draft v0.2 (Phase 0) — revised with Phase 0 research

## 1. Principles

1. **One engine, many shells.** All geometry and layout logic lives in one Rust crate. The web app, the CLI and CAD plugins are thin shells around it.
2. **The JSON contract is the product boundary.** Shells talk to the engine only through versioned JSON documents defined in `schemas/`.
3. **Metric, planar computation only.** The engine never sees latitude/longitude.
4. **Source coordinates are sacred.** Imported geometry is stored in its own frame; transforms are stored separately.
5. **Deterministic and testable.** No randomness without an explicit seed; no I/O in the core.
6. **Local-first.** The web app computes in the browser; no backend is required.

## 2. Component overview

```
                 ┌──────────────────────────────┐
                 │        crates/core (Rust)    │
                 │  geometry · layout · rules   │
                 │  validation · scoring        │
                 └──────┬───────────────┬───────┘
                        │               │
            ┌───────────▼───┐     ┌─────▼──────────┐
            │ crates/wasm   │     │ crates/cli     │
            │ wasm-bindgen  │     │ stallwise-cli  │
            └───────┬───────┘     │ JSON ⇄ JSON    │
                    │             └──┬──────────┬──┘
        ┌───────────▼──────────┐     │          │
        │ apps/web             │     │          │
        │ React · Web Worker   │  ┌──▼───────┐ ┌▼──────────────┐
        │ MapLibre · canvas    │  │ CADCraft │ │ Python adapter│
        │ DXF import/export    │  │ adapter  │ │ IngeTrazo /   │
        └──────────────────────┘  └──────────┘ │ IngeCAD       │
                                               └───────────────┘
```

| Component | Responsibility | Must not |
|---|---|---|
| `crates/core` | Polygon operations, module tiling, search, validation, scoring, **all legal/rule evaluation and compliance calculation** (so web and CLI give identical results) | Do I/O, parse DXF, know about maps or UI |
| `crates/wasm` | Expose core to JS; serialise JSON; progress/cancel callbacks | Contain layout logic |
| `crates/cli` | Read JSON (file/stdin), run core, write JSON; optional long-running JSON-lines mode | Contain layout logic |
| `apps/web` | UI, map, drawing, editing, DXF/GeoJSON/PDF I/O, CRS handling, persistence | Re-implement geometry rules in TypeScript |
| `plugins/*` | Convert host CAD entities ⇄ Stallwise JSON; call the CLI | Contain layout logic |

## 3. Technology choices

Versions checked against crates.io / npm on 2026-10-24. "Status" refers to the ADR.

| Concern | Choice | Version · licence | Status |
|---|---|---|---|
| Geometry façade (boolean, buffer) | `geo` (uses `i_overlay` internally) | 0.33.1 · MIT OR Apache-2.0 | Proposed — ADR-0005; accept after torture suite (OQ-15) |
| Geometry benchmarks only | direct `i_overlay`; `clipper2` | 9.1.0 · MIT/Apache · 0.6.0 · MIT/Apache | Benchmark only — never exposed in domain APIs |
| Spatial index | `rstar` | — | Proposed |
| Graph / connectivity | `petgraph` | — | Proposed |
| Serialization | `serde`, `serde_json`, `schemars` | — | Proposed |
| WASM | `wasm-bindgen`, `wasm-pack`, Web Worker | — | ADR-0002 |
| Web framework | React + TypeScript + Vite | — | Proposed |
| Plan renderer | **PixiJS**; Konva as benchmark alternative | 8.22.0 · MIT / 10.9.0 · MIT | Proposed — ADR-0006 |
| Map renderer + drawing | MapLibre GL JS + Terra Draw | 6.15.0 · BSD-3-Clause / 1.38.0 · MIT | Proposed — ADR-0007 |
| Tiles / imagery | Configurable providers; not `tile.openstreetmap.org` in production; satellite opt-in | — | ADR-0007, OQ-11 |
| CRS | proj4js (web shell only) | 2.22.0 · MIT | Proposed — ADR-0008 for accuracy model |
| DXF read/write | **Unresolved** — bake-off of Rust `dxf` vs `acadrust` under `wasm32` in Phase 3 | 0.6.2 · MIT / 0.6.6 · MPL-2.0 | Deferred (OQ-13). JS `dxf-parser` 1.1.2 is read-only and low-activity: fallback only |
| PDF | `pdf-lib` or print-from-SVG | — | Open |
| Python binding (optional) | PyO3 + maturin | — | Only if CLI-based plugins prove too limited |

Renderer rule: editor state, selection, snapping, commands, undo/redo and IDs are renderer-independent. Pixi objects are projections of domain objects, never the stored document.

## 4. Data model (conceptual)

```
Project
├─ meta            id, name, created, engine_version, schema_version
├─ use_program[]   building uses + quantities (area, seats, rooms, units) for supply calculation
├─ frame           source_units, local_origin, source_crs? (EPSG),
│                  crs_operation? {id, name, accuracy_m, provenance},
│                  map_transform? (rigid 2D + residuals)
├─ site
│  ├─ boundary     Polygon (with holes)
│  ├─ setbacks     uniform | per-edge
│  ├─ obstacles[]  Polygon | Circle | BufferedPolyline (+ kind)
│  ├─ no_parking[] Polygon
│  ├─ keepouts[]   Polygon + kind (fire_access | clear_strip | user) + applies_to (stalls | stalls_and_aisles)
│  └─ access[]     Point | Segment, type (entry/exit/both), lanes
├─ rule_sets[]     id, version, kind (jurisdiction | project_standard), jurisdiction, authority,
│                  edition_year_be, as_of, values[] {key, value, unit, citation, status}
└─ layouts[]
   ├─ id, name, rule_set_ref, params_override, seed
   ├─ locks[]      zone polygons and element ids
   ├─ stalls[]     id (stable across regeneration), type, polygon, angle, bay_id, locked, rule_refs[]
   ├─ clear_strips[] polygon, serves[] stall ids
   ├─ aisles[]     id, polygon, centerline, width, direction, locked, rule_refs[]
   ├─ islands[]    polygon
   ├─ graph        nodes, edges (for connectivity)
   └─ report       counts by type/zone, score components, validation issues,
                   compliance ledger {requirement, required, provided, citation, status}
```

All coordinates in `site` and `layouts` are metres in the **source frame** (`frame.source_unit_to_m` applied, no shift or rotation). The web shell converts to and from map coordinates using `frame`. Formal definition: [`schemas/v0`](../schemas/README.md).

## 5. Coordinate handling

| Mode | Source frame | To engine | To map display | DXF export |
|---|---|---|---|---|
| Local | DXF coordinates × unit factor → metres | as-is (metres) | not shown | inverse unit factor |
| Georeferenced CAD | Declared EPSG (projected, metres) | as-is | proj4: EPSG → WGS 84 | as-is |
| Map draw | Auto UTM zone | as-is | proj4: UTM → WGS 84 | UTM coordinates |
| Aligned CAD | DXF coordinates (metres) | as-is | rigid transform → UTM → WGS 84 | as-is (transform not applied) |

Large coordinate values (e.g. UTM northings ≈ 1,500,000 m) are shifted to a local origin before entering the engine and shifted back afterwards, to protect floating-point precision. The origin is stored in the project.

**Two different accuracy notions — never mix them (ADR-0008):**

| Quantity | Target | Tested by |
|---|---|---|
| Numerical precision (local shift, unit scaling, same-operation round trip) | ≤ 1 mm | Unit/property tests |
| Datum-operation accuracy (e.g. Indian 1975 → WGS 84) | Published value of the chosen EPSG operation, typically 1–5 m | Control-point fixtures with operation-appropriate tolerance; shown to the user |

## 6. Engine API (sketch)

```text
generate(site, rule_set, params, locks, options) -> LayoutResult[]
validate(site, layout, rule_set)                -> ValidationReport
refill_bay(site, layout, aisle_id, rule_set)    -> Layout
summarize(layout, rule_set)                     -> Report
```

- `options` includes search resolution, max candidates, seed, and time budget.
- Progress and cancellation via a callback (WASM) or JSON-lines events (CLI).

## 7. CLI contract (sketch)

```bash
stallwise-cli generate --input project.json --output result.json
stallwise-cli validate --input project.json --layout L1
stallwise-cli serve --stdio     # JSON-lines request/response for plugins
```

Exit codes and error objects are part of the schema.

## 8. Repository layout

```
stallwise/
├─ crates/core/       Cargo workspace member
├─ crates/wasm/
├─ crates/cli/
├─ apps/web/          pnpm workspace member
├─ plugins/           added in Phase 5
├─ schemas/           JSON Schemas, versioned (v0, v1, …)
├─ docs/              spec, architecture, roadmap, ADRs
├─ Cargo.toml         workspace (added in Phase 1)
└─ package.json       workspace (added in Phase 2)
```

## 9. Testing strategy

| Level | What |
|---|---|
| Unit (core) | Polygon ops, module tiling, stall fitting, graph reachability |
| Property-based (core) | No overlaps, all stalls inside region, determinism — via `proptest` |
| Fixture / golden (core) | Analytic rectangles with known optimum; irregular sites with golden counts; polygon torture suite; rule-engine fixtures (BMA 90°, national one-way negative test, accessible-count boundaries, 30° `unverified` lookup) |
| Schema | Round-trip: Rust types ⇄ JSON Schema ⇄ TypeScript types |
| Web | Component tests; DXF import/export round-trip; same-CRS numeric round-trip within 1 mm; datum-operation fixtures at their published accuracy |
| Performance | Benchmarks on reference sites tracked in CI (`criterion`) |
| End-to-end | Playwright: import → generate → edit → export |

## 10. Licensing notes

- Stallwise is AGPL-3.0-or-later (ADR-0001).
- All dependencies must be AGPL-compatible. Permissive (MIT, Apache-2.0, BSD) and LGPL/GPL-3.0 libraries are generally compatible; GPL-2.0-only libraries are **not** compatible with GPL-3.0/AGPL-3.0 and must be avoided. Licence compatibility is checked in CI (`cargo-deny`, and a JS licence checker). This is engineering guidance, not legal advice.
