# 0004 — CAD plugin targets and deferred decision

- Status: Superseded by 0009
- Date: 2026-10-23

## Context
Besides the web app, Stallwise should integrate with open-source CAD. Candidates reviewed in Phase 0 (state as of October 2026, from project websites and repositories):

| Host | Kind | Licence | Extension mechanism | Notes |
|---|---|---|---|---|
| IngeTrazo | 3D modeller (SketchUp-style), Python/PySide6 | GPL-3.0 | Python files in an extensions folder; Python console | 0.x; plugin API may change between minor versions |
| IngeCAD | 2D CAD (AutoCAD-style), Qt + ezdxf | Not confirmed | Plugin folders adding menus, commands, tools | Same family as IngeTrazo; Linux-first |
| CADCraft | 2D/3D CAD, pure Rust, WASM build | MIT or Apache-2.0 | JSON control channel, MCP server, `cadcraft-cli`, LISP, scripts | Early development, large community |

Dropped from consideration: FreeCAD, QCAD, LibreCAD (owner decision; LibreCAD also has a limited plugin API and a stalled LibreCAD 3 rewrite).

## Decision
- Target hosts: **IngeTrazo, IngeCAD, CADCraft**.
- Build no plugin until the web app and DXF round-trip are stable (start of Phase 5).
- All plugins are thin adapters over `stallwise-cli` and the JSON schema.
- Choose the order at the Phase 5 gate using: API stability, ease of calling an external process, entity model fit for 2D layouts, licence, user base, project activity.

## Consequences
- The CLI and JSON-lines protocol must be designed for plugin use from Phase 2.
- Inge* hosts may share one Python adapter package.
- DXF remains the fallback integration for every CAD program.
