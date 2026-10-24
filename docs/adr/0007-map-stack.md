# 0007 — Map and drawing stack

- Status: Proposed
- Date: 2026-10-24

## Context
Map mode needs a basemap and polygon drawing without tying project geometry to a commercial provider. MapLibre GL JS 6.15.0 (BSD-3-Clause), Terra Draw 1.38.0 (MIT, MapLibre adapter). The OSMF public tile service is best-effort, attribution-bound and forbids bulk/offline use.

## Decision
- MapLibre GL JS for rendering; Terra Draw for drawing.
- Tile, style and imagery providers are runtime configuration. Candidates: hosted open-map services within their terms (e.g. OpenFreeMap), self-hosted OSM-derived vector tiles, or a licensed commercial provider.
- `tile.openstreetmap.org` is not a production default.
- Satellite imagery is opt-in per provider (key + attribution) and off by default until its terms are reviewed (OQ-11).
- Each imagery source declares capability flags (SPEC MAP-6); tracing, caching and export are gated per flag, because provider terms can restrict tracing/derivation itself, not only export (focused research, 2026-10-24).
- PDF/raster exports contain geometry only unless the source permits imagery export.

## Consequences
- Provider-neutral core; attribution rendered per provider.
- A deployment must configure a tile provider.

## Alternatives considered
- Public OSM raster tiles as default: rejected (usage policy).
- A provider SDK as the core: rejected (vendor lock-in).
