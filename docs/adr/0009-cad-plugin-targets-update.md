# 0009 — CAD plugin targets: updated evidence

- Status: Accepted (supersedes 0004)
- Date: 2026-10-24

## Context
Phase 0 research (October 2026) updated the host facts in ADR-0004:

| Host | Licence · version | Integration route | Fit |
|---|---|---|---|
| IngeCAD | GPL-3.0-or-later · 0.6.8.2 | Python `PluginSpec` (commands, tools, menus); APPLOAD scripts; adapter can launch `stallwise-cli` | Best entity fit: the `ezdxf` document is the model; named layers, plain DXF entities, XDATA, undoable commands |
| CADCraft | MIT OR Apache-2.0 · 0.12.0 | Authenticated local JSON-lines control channel, MCP, CLI, scripts/LISP | Strongest external-process route; very young repository (Oct 2026) |
| IngeTrazo | GPL-3.0-or-later · 0.5.9 | Python extensions (API 2), localhost MCP bridge | Extension API explicitly unstable through 0.x; scene model is 3D-oriented |

All three hosts are licence-compatible with an AGPL-3.0-or-later adapter.

## Decision
- Targets remain IngeCAD, CADCraft and IngeTrazo.
- Provisional order: **IngeCAD → CADCraft → IngeTrazo**, confirmed by the owner at the Phase 5 gate (OQ-19, OQ-20).
- Plugins remain thin adapters over `stallwise-cli` and the JSON schema; no plugin before Phase 5.

## Consequences
- Generated elements carry stable IDs and rule provenance so they can be stored as XDATA (IngeCAD) or equivalent.
- Adapter compatibility policy for young host APIs is still open (OQ-21).
