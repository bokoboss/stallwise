# 0006 — Browser plan renderer: PixiJS

- Status: Proposed (accept after Phase 3 benchmark)
- Date: 2026-10-24

## Context
The editor shows and edits thousands of stalls plus aisles, zones, handles and overlays. PixiJS 8.22.0 (MIT) and Konva 10.9.0 (MIT) are both current.

## Decision
- Use PixiJS as the preferred renderer.
- Domain state, selection, snapping, commands, undo/redo and IDs are renderer-independent; Pixi objects are projections, never the stored document.
- Benchmark against Konva with 1k / 5k / 10k-object scenes (select, drag, redraw) before accepting. These tiers are engineering benchmarks, not claims about typical projects.

## Consequences
- GPU-oriented path for large scenes.
- Stallwise owns more interaction logic than it would with Konva.
- The renderer stays replaceable.

## Alternatives considered
- Konva: richer interaction API — benchmark alternative.
- SVG: for export and small overlays only.
- Raw Canvas: no dependency, but Stallwise would own hit testing and invalidation.
