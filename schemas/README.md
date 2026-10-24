# schemas

Versioned JSON Schemas (Draft 2020-12) shared by every shell: web app, `stallwise-cli`, and CAD plugins.
**v0 is a draft for review.** It will be frozen as v1 at the end of Phase 2; until then breaking changes are allowed but must be noted in the PR.

Validate schemas and examples:

```bash
python3 scripts/validate_schemas.py schemas/v0   # needs jsonschema >= 4.18
```

## Files (`v0/`)

| Schema | Purpose | SPEC / ADR |
|---|---|---|
| `common.schema.json` | Ids, points, polygons, shapes, intervals, citations, rule refs, issues | — |
| `rule-set.schema.json` | Jurisdiction profile or project design standard; rule values with condition, quantity, basis, status, citations; prohibitions | RS-1…RS-7 |
| `project.schema.json` | Self-contained project file: frame, site, use program, embedded rule sets, layouts | IN-*, OUT-5, ADR-0003, ADR-0008 |
| `layout.schema.json` | Params, stalls, clear strips, aisles, islands, circulation graph, report and compliance ledger | GEN-*, ED-7, OUT-1 |
| `cli.schema.json` | `stallwise-cli` request / response / progress event (one JSON per line in `serve --stdio`) | CAD-2, GEN-R4 |
| `imagery-source.schema.json` | Deployment-level imagery capability record (not in project files) | MAP-6, ADR-0007 |

`examples/` holds valid documents; `examples/invalid/` holds documents that **must** be rejected (named `<reason>.<schema-prefix>.json`).

## Design decisions in v0

1. **Geometry units and frame.** Coordinates are metres in the **source frame** (source axes and origin, multiplied by `frame.source_unit_to_m`). CRS, datum operation and map transform are stored in `frame` and never applied to stored geometry (ADR-0003). `local_origin` is an engine-side precision shift; stored geometry is not shifted.
2. **Rings** are closed implicitly (first point not repeated). Orientation is normalised by the engine.
3. **Stalls** are four-corner rings whose first edge faces the aisle — enough for DXF export and editing without re-deriving geometry.
4. **Rule values** have a `basis`: `statute` (needs `citations` and a `status`) or `project_policy` (needs a value, has no legal status). An `unverified` statute rule carries **no value** — the engine returns `unverified_rule` (RS-4).
5. **Conditions** use explicit inclusive/exclusive intervals for angles, so `< 30°`, `30°–60°` and `> 60°` are encoded exactly as written (RS-5).
6. **Quantities** are `min`, `max`, `equals`, stepped counts (accessible spaces) or tiered rates (parking supply).
7. **Provenance.** Stalls, aisles, clear strips, issues and ledger lines carry `rule_refs` back to a rule-set id, version and value id (RS-3).
8. **Projects embed** every rule set they use, so a project file reproduces offline.
9. **Imagery rights** live in deployment config, not in project files.

## Checked by the engine, not by the schema

JSON Schema cannot express these; the engine (and later a schema-level test suite) must enforce them:

- Ids are unique within their collection; every `*_id` / `rule_refs` target exists.
- A `project_standard` satisfies the jurisdiction it `extends` (e.g. stall width ≥ legal minimum) — RS-6.
- `active_rules` refer to rule sets embedded in the project.
- Conditions in one rule set do not overlap ambiguously for the same key.
- Polygon validity (no self-intersection, holes inside outer ring), setback `per_edge` length equals the number of outer edges.
- Geometric rules: GEN-R1, GEN-R2.
