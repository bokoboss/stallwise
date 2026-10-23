# Architecture Decision Records

One file per decision: `NNNN-short-title.md`. Status is one of **Proposed**, **Accepted**, **Superseded by NNNN**, **Deprecated**.
Decisions are not edited after acceptance; a new ADR supersedes an old one.

| ADR | Title | Status |
|---|---|---|
| [0001](0001-license-agpl.md) | License: AGPL-3.0-or-later | Accepted |
| [0002](0002-rust-core-wasm.md) | Single Rust core, shipped as WASM and CLI | Proposed |
| [0003](0003-coordinate-model.md) | Coordinate model: source frame + separate transform | Proposed |
| [0004](0004-cad-plugin-targets.md) | CAD plugin targets and deferred decision | Accepted |

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
