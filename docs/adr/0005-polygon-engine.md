# 0005 — Default polygon engine: `geo`

- Status: Proposed (accept after the Phase 1 torture suite, OQ-15)
- Date: 2026-10-24

## Context
The core needs polygon difference/intersection, buffering, containment and holes, natively and in `wasm32`. Candidates (versions checked 2026-10-24): `geo` 0.33.1 (MIT OR Apache-2.0, pure Rust, boolean ops via `i_overlay`), direct `i_overlay` 9.1.0 (MIT OR Apache-2.0), `clipper2` 0.6.0 (MIT OR Apache-2.0, wraps C++), `geo-clipper` 0.9.0 (ISC, wraps C++).

## Decision
- Use `geo = 0.33.1` as the only geometry façade in domain APIs.
- Never expose Clipper- or `i_overlay`-specific types in Stallwise APIs.
- Keep a benchmark harness comparing `geo`, direct `i_overlay` and `clipper2` on the same fixtures (holes, near-collinear edges, slivers, duplicate vertices, near-touching obstacles, large shifted coordinates). Switch only on measured evidence.

## Consequences
- Pure-Rust WASM build; one geometry representation.
- `geo` is pinned and upgraded deliberately.
- No claim yet that `geo` is more robust than Clipper2 — that is what the torture suite decides.

## Alternatives considered
- `clipper2` / `geo-clipper`: licence-compatible, but native C++ toolchain in the WASM build.
- Direct `i_overlay`: pure Rust, but duplicates what `geo` already wraps.
