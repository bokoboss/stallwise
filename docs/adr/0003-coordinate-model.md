# 0003 — Coordinate model: source frame + separate transform

- Status: Proposed
- Date: 2026-10-23

## Context
Sites come from CAD files with or without real-world coordinates, from CAD files that must be aligned to a map by hand, and from map drawings. Exports must land exactly on the original CAD drawing.

## Decision
- Store all site and layout geometry in the **source frame** (file coordinates, converted to metres).
- Store the CRS (EPSG) and/or a **rigid 2D transform** (translation + rotation, scale = 1 by default) separately in the project.
- The engine only receives metric planar coordinates, shifted to a local origin for precision.
- Map display and GeoJSON export apply the transform and CRS in the web shell; DXF export never applies them.

## Consequences
- DXF round-trip is exact regardless of map alignment.
- Re-aligning to the map never changes the design.
- The web shell owns all CRS logic (proj4js); the core stays CRS-agnostic.

## Alternatives considered
- **Convert everything to WGS 84 / Web Mercator on import** — breaks exact CAD round-trip and distorts distances.
- **Convert everything to UTM on import** — loses the original CAD frame for floating drawings.
