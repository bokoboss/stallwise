# Research Brief — Phase 0

This brief is for the research and planning pass that reviews this repository before development starts. Please answer each question with **sources** (links, regulation numbers with clause and edition, library versions and licences) and flag anything uncertain. Proposed changes to `SPEC.md`, `ARCHITECTURE.md` or `ROADMAP.md` are welcome.

Development will be done with Claude, following `CLAUDE.md`.

---

## A. Regulations and design standards (Thailand first)

- **A1.** Which Thai regulations govern parking stall dimensions, aisle widths by parking angle, and minimum parking supply? Identify the current ministerial regulations under the Building Control Act (including the parking-related ministerial regulation of B.E. 2517 and all later amendments), with clause numbers and the current values.
- **A2.** Bangkok Metropolitan Administration (BMA) building control regulations: do they modify or add to the national values?
- **A3.** Accessible parking: required number/ratio, stall dimensions, access aisle, location rules — current ministerial regulation on facilities for persons with disabilities and the elderly, with edition.
- **A4.** Requirements for ramps, turning radii, clear height, and entry/exit widths that affect surface-lot layout.
- **A5.** Fire-access lane requirements that would create no-parking zones.
- **A6.** Motorcycle parking dimensions, if regulated.
- **A7.** EV charging stall requirements or guidance, if any.
- **A8.** For comparison/fallback rule sets: commonly used international references (e.g. US, UK, Japan, Singapore) — names, editions and how they differ.

Deliverable: a table of values with citation per value, ready to become the "Thai regulatory" rule set (SPEC RS-2).

## B. Prior art and algorithms

- **B1.** How do existing tools (TestFit, ParkCAD, and others) approach automatic parking layout? Only publicly documented behaviour — no reverse engineering.
- **B2.** Academic and open-source work on parking layout optimisation: strip/module packing, orientation search, multi-zone decomposition, metaheuristics, graph-based circulation checks. Summarise approaches, reported results and complexity.
- **B3.** Recommended baseline algorithm for Phase 1 and the best upgrade path for Phase 6.
- **B4.** Good reference test sites or benchmarks with known optimal or published stall counts.

## C. Technology choices

- **C1.** Rust polygon libraries: compare `geo`, `geo-clipper`, `clipper2` bindings, `i_overlay`, and others for robust boolean and offset operations — licence, WASM support, robustness, maintenance status.
- **C2.** DXF in the browser: compare `dxf-parser` (JS), Rust DXF crates compiled to WASM, and CADCraft's DXF/DWG stack (acadrust) — read/write coverage, licence, compatibility with AGPL.
- **C3.** Canvas editor: PixiJS vs Konva vs plain SVG/Canvas for thousands of editable stalls.
- **C4.** Map stack: MapLibre GL JS + Terra Draw; open basemap and satellite-imagery options and their terms of use for an AGPL, possibly hosted web app.
- **C5.** CRS: correct EPSG codes and transformation parameters for Thai datums still found in older CAD (Indian 1975 UTM 47N/48N) vs WGS 84 UTM; expected accuracy of proj4js transformations.

## D. CAD plugin targets (input for the Phase 5 decision)

For **IngeTrazo**, **IngeCAD** and **CADCraft**:

- **D1.** Licence (IngeCAD's licence is not yet confirmed).
- **D2.** Plugin/extension mechanism, language, documentation, stability promises.
- **D3.** How an external process could be called (subprocess, JSON channel, MCP, etc.).
- **D4.** Entity model: how to read a closed boundary and write polylines/hatches/blocks on named layers.
- **D5.** Project activity and maturity (release cadence, contributors, issue backlog).
- **D6.** Licence implications of distributing an AGPL Stallwise adapter for each host.

## E. Product and UX

- **E1.** Which outputs do Thai engineers and authorities expect in a parking study (tables, drawings, ratios)?
- **E2.** Typical site sizes and complexity, to set realistic performance targets (SPEC NFR-2).
- **E3.** Editing interactions that matter most in practice (based on public tool documentation and user feedback).

---

## Output format requested

1. Findings per question, with sources.
2. A list of concrete edits to `SPEC.md`, `ARCHITECTURE.md`, `ROADMAP.md`.
3. Proposed ADRs for confirmed technology choices.
4. Remaining open questions, with who should answer them.
