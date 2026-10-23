# Architecture Decision Records

One file per decision: `NNNN-short-title.md`. Status is one of **Proposed**, **Accepted**, **Superseded by NNNN**, **Deprecated**.
Decisions are not edited after acceptance (only the Status line changes); a new ADR supersedes an old one. A DXF library ADR is deliberately deferred to the Phase 3 bake-off (OQ-13).

| ADR | Title | Status |
|---|---|---|
| [0001](0001-license-agpl.md) | License: AGPL-3.0-or-later | Accepted |
| [0002](0002-rust-core-wasm.md) | Single Rust core, shipped as WASM and CLI | Proposed |
| [0003](0003-coordinate-model.md) | Coordinate model: source frame + separate transform | Proposed |
| [0004](0004-cad-plugin-targets.md) | CAD plugin targets and deferred decision | Superseded by 0009 |
| [0005](0005-polygon-engine.md) | Default polygon engine: `geo` | Proposed |
| [0006](0006-plan-renderer.md) | Browser plan renderer: PixiJS | Proposed |
| [0007](0007-map-stack.md) | Map and drawing stack | Proposed |
| [0008](0008-legacy-crs-accuracy.md) | Legacy Thai CRS and accuracy model | Proposed |
| [0009](0009-cad-plugin-targets-update.md) | CAD plugin targets: updated evidence | Accepted |

Template:

```markdown
# NNNN — Title
- Status:
- Date:
## Context
## Decision
## Consequences
## Alternatives considered
```
