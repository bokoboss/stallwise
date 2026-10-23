# Stallwise — Architecture

- **Document status:** Draft v0.1 (Phase 0)

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
| `crates/core` | Polygon operations, module tiling, search, validation, scoring, rule-set evaluation | Do I/O, parse DXF, know about maps or UI |
| `crates/wasm` | Expose core to JS; serialise JSON; progress/cancel callbacks | Contain layout logic |
| `crates/cli` | Read JSON (file/stdin), run core, write JSON; optional long-running JSON-lines mode | Contain layout logic |
| `apps/web` | UI, map, drawing, editing, DXF/GeoJSON/PDF I/O, CRS handling, persistence | Re-implement geometry rules in TypeScript |
| `plugins/*` | Convert host CAD entities ⇄ Stallwise JSON; call the CLI | Contain layout logic |

## 3. Candidate technology choices

These are proposals to be confirmed during the Phase 0 research pass (see RESEARCH_BRIEF).

| Concern | Candidate | Notes |
|---|---|---|
| Polygon boolean / offset | `geo` + `geo-clipper` or `clipper2` (Rust) | Need robust offset and boolean ops with integer or fixed-precision coordinates |
| Spatial index | `rstar` | Collision checks between stalls and obstacles |
| Graph / connectivity | `petgraph` | Aisle network reachability, one-way direction |
| Serialization | `serde`, `serde_json`, `schemars` | Generate JSON Schema from Rust types, or validate against hand-written schema |
| WASM | `wasm-bindgen`, `wasm-pack` | Run in a Web Worker |
| Web framework | React + TypeScript + Vite | |
| Canvas editor | PixiJS or Konva | Must handle thousands of stalls smoothly |
| Map | MapLibre GL JS | Open source |
| Map drawing | Terra Draw | Works with MapLibre |
| CRS | proj4js + EPSG definitions | Only in the web shell, never in core |
| DXF read (web) | `dxf-parser` or a Rust DXF crate compiled to WASM | Research item; CADCraft's DXF/DWG stack (acadrust) also worth evaluating |
| DXF write (web) | Custom writer or library | Must control layers, units and coordinates exactly |
| PDF | `pdf-lib` or print-to-PDF from SVG | |
| Python binding (optional) | PyO3 + maturin | Only if CLI-based plugins prove too limited |

## 4. Data model (conceptual)

```
Project
├─ meta            id, name, created, engine_version, schema_version
├─ frame           source_units, source_crs? (EPSG), map_transform? (rigid 2D + residuals)
├─ site
│  ├─ boundary     Polygon (with holes)
│  ├─ setbacks     uniform | per-edge
│  ├─ obstacles[]  Polygon | Circle | BufferedPolyline (+ kind)
│  ├─ no_parking[] Polygon
│  └─ access[]     Point | Segment, type (entry/exit/both), lanes
├─ rule_sets[]     id, version, status (draft/verified), parameters, citations[]
└─ layouts[]
   ├─ id, name, rule_set_ref, params_override, seed
   ├─ locks[]      zone polygons and element ids
   ├─ stalls[]     id, type, polygon, angle, bay_id, locked
   ├─ aisles[]     id, centerline, width, direction, locked
   ├─ islands[]    polygon
   ├─ graph        nodes, edges (for connectivity)
   └─ report       counts by type/zone, score components, validation issues
```

All coordinates in `site` and `layouts` are in the **source frame** (`frame.source_units`). The web shell converts to and from map coordinates using `frame`.

## 5. Coordinate handling

| Mode | Source frame | To engine | To map display | DXF export |
|---|---|---|---|---|
| Local | DXF coordinates × unit factor → metres | as-is (metres) | not shown | inverse unit factor |
| Georeferenced CAD | Declared EPSG (projected, metres) | as-is | proj4: EPSG → WGS 84 | as-is |
| Map draw | Auto UTM zone | as-is | proj4: UTM → WGS 84 | UTM coordinates |
| Aligned CAD | DXF coordinates (metres) | as-is | rigid transform → UTM → WGS 84 | as-is (transform not applied) |

Large coordinate values (e.g. UTM northings ≈ 1,500,000 m) are shifted to a local origin before entering the engine and shifted back afterwards, to protect floating-point precision. The origin is stored in the project.

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
| Fixture / golden (core) | Reference sites with hand-checked stall counts; snapshot of layout JSON |
| Schema | Round-trip: Rust types ⇄ JSON Schema ⇄ TypeScript types |
| Web | Component tests; DXF import/export round-trip; CRS round-trip within 1 mm |
| Performance | Benchmarks on reference sites tracked in CI (`criterion`) |
| End-to-end | Playwright: import → generate → edit → export |

## 10. Licensing notes

- Stallwise is AGPL-3.0-or-later (ADR-0001).
- All dependencies must be AGPL-compatible. Permissive (MIT, Apache-2.0, BSD) and LGPL/GPL-3.0 libraries are generally compatible; GPL-2.0-only libraries are **not** compatible with GPL-3.0/AGPL-3.0 and must be avoided. Licence compatibility is checked in CI (`cargo-deny`, and a JS licence checker). This is engineering guidance, not legal advice.
