# 0007 — Map and drawing stack

- Status: Proposed
- Date: 2026-10-24

## Context
Map mode needs a basemap and polygon drawing without tying project geometry to a commercial provider. MapLibre GL JS 6.15.0 (BSD-3-Clause), Terra Draw 1.38.0 (MIT, MapLibre adapter). The OSMF public tile service is best-effort, attribution-bound and forbids bulk/offline use.

## Decision
- MapLibre GL JS for rendering; Terra Draw for drawing.
- Tile, style and imagery providers are runtime configuration. Candidates: hosted open-map services within their terms (e.g. OpenFreeMap), self-hosted OSM-derived vector tiles, or a licensed commercial provider.
- `tile.openstreetmap.org` is not a production default.
- Satellite imagery is opt-in per provider (key + attribution) and off by default until its terms are reviewed (OQ-11); imagery in exports depends on OQ-12.

## Consequences
- Provider-neutral core; attribution rendered per provider.
- A deployment must configure a tile provider.

## Alternatives considered
- Public OSM raster tiles as default: rejected (usage policy).
- A provider SDK as the core: rejected (vendor lock-in).
