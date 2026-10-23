# 0008 — Legacy Thai CRS and accuracy model

- Status: Proposed
- Date: 2026-10-24

## Context
Older Thai CAD may use Indian 1975 / UTM 47N (EPSG:24047) or 48N (EPSG:24048). EPSG lists several Indian 1975 → WGS 84 operations for Thailand with published accuracies of roughly 1–5 m. v0.1 implied millimetre-level CRS round trips, conflating numerical precision with datum accuracy.

## Decision
- Offer EPSG:24047 / 24048 as source CRS presets alongside EPSG:32647 / 32648.
- Persist the chosen datum operation, its published accuracy and provenance (SPEC IN-R8).
- Use ≤ 1 mm tests only for numerical invariants and same-operation round trips.
- Never present an Indian 1975 → WGS 84 result as millimetre-accurate unless the project supplies survey control that establishes it.

## Consequences
- UI shows a legacy-datum warning and operation metadata.
- Two drawings with the same EPSG code may have different provenance (e.g. local control fit).
- CRS tests use control coordinates with operation-appropriate tolerances.

## Alternatives considered
- One hard-coded `towgs84`: rejected — several operations exist with different areas and accuracies.
- Not supporting Indian 1975: rejected — legacy CAD is a stated requirement.
