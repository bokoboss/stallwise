> **Archive note (added on import, 2026-10-24).** This is the Phase 0 external research report, kept verbatim as the evidence record for SPEC v0.2.
> Inline citation markers of the form `cite…` / `filecite…` are artefacts of the research tool's export and **do not resolve to URLs**. Before any regulatory value is promoted beyond `cited` status (see `docs/rules/TH_RULESET_DRAFT.md`), the primary legal text must be obtained and linked directly.

# Stallwise Phase Zero Deep Research Report

**Research date:** 24 October 2026  
**Repository reviewed:** `bokoboss/stallwise`  
**Purpose:** research input for the Stallwise specification revision from v0.1 to v0.2.

## Executive synthesis

Stallwise's current architectural direction is sound: a single deterministic Rust geometry/rules core compiled to WebAssembly for the browser and exposed through a JSON CLI for CAD integrations is a strong fit for the product, and it is already consistently reflected in `SPEC.md`, `ARCHITECTURE.md`, the roadmap, the accepted/proposed ADRs, and the constraints in `CLAUDE.md`. fileciteturn1file0 fileciteturn2file0 fileciteturn3file0 fileciteturn7file0 fileciteturn10file0

The most important Phase Zero finding is that the proposed “Thai regulatory” rule set must **not** be represented as one flat collection of parking dimensions. Thailand has at least two materially different profiles relevant to Stallwise:

1. a national profile based principally on Ministerial Regulation No. 7 B.E. 2517, as subsequently amended by Ministerial Regulation No. 41 B.E. 2537 and No. 64 B.E. 2555; and
2. a Bangkok profile based on the Bangkok Metropolitan Administration Building Control Ordinance B.E. 2544, which adds explicit aisle-width rules, different parking-supply formulas for several uses, and additional ramp/access provisions. citeturn28view0turn24view1turn28view1turn24view2turn27view0

A particularly important implementation detail is that Ministerial Regulation No. 41 B.E. 2537 **repealed the old No. 7 clause 5 parking-space rule**. The current national stall dimensions come from No. 41 clause 2: at least 2.40 × 6.00 m for parallel or less-than-30-degree parking, 2.40 × 5.00 m for perpendicular parking, and 2.40 × 5.50 m for the other oblique category over 30 degrees. The text also imposes a one-way-circulation restriction on perpendicular parking. Stallwise therefore must not retain the often-repeated historical “2.50 × 6.00 m” figure as a current national rule. citeturn23view0turn24view1

Bangkok is significantly more useful as a machine-readable surface-lot profile because BMA Ordinance B.E. 2544 clause 88 gives explicit minimum drive-aisle widths: 3.50 m below 30°, 5.50 m for 30°–60°, and 6.00 m over 60°. It also establishes a 6.00 m general entrance/exit width or 3.50 m where separate one-way entrances/exits are used. citeturn27view0 The national regulation, by contrast, provides entrance/exit and circulation requirements but the sources reviewed did **not** establish a national table of internal aisle widths by parking angle comparable to the BMA table. Such values must not be invented.

Accessible parking should likewise be encoded from the **current amended provisions**, not from superseded summaries. Ministerial Regulation No. 2 B.E. 2564 replaced clauses 12–14 of the earlier accessibility regulation. It establishes a stepped accessible-space count, nearest-entrance location rules, signage/marking, and a clear strip at least 1.00 m wide for the full length of the parking space. The underlying vehicle-space geometry refers back to Ministerial Regulation No. 41 rather than creating a generic 2.40 × 6.00 m accessible bay. citeturn24view0turn23view1turn23view2

Technically, the strongest Phase One geometry choice is now **`geo` 0.33.1 as the default geometry façade**, with its built-in Boolean operations and buffering, backed internally by `i_overlay`. Direct use of `i_overlay` 9.1.0 should remain an optimization/robustness experiment rather than an immediate second geometry model. `geo-clipper` and the `clipper2` Rust binding remain useful benchmark/fallback candidates but introduce native C/C++ binding complexity into the WebAssembly build. fileciteturn13file0 fileciteturn14file0 fileciteturn14file1 fileciteturn15file0 fileciteturn19file0 fileciteturn22file0

For DXF, there is not yet enough evidence to freeze an ADR. The JavaScript `dxf-parser` is read-only and has not been pushed since June 2024; the Rust `dxf` crate 0.6.2 is MIT-licensed, actively maintained in 2026, and reads/writes DXF/DXB; the newer `acadrust` 0.6.6 is pure Rust, MPL-2.0, explicitly accommodates WebAssembly, and claims broad DXF/DWG R12–R2018+ read/write coverage, but it is a much younger project. The correct Phase Three decision is therefore a fixture-driven compatibility spike rather than an architectural guess. fileciteturn32file0 fileciteturn33file0 fileciteturn36file0 fileciteturn37file0 fileciteturn38file0 fileciteturn39file0 fileciteturn41file0

The largest correction needed in the CRS design is that **Indian 1975 → WGS 84 is not a millimetre-accuracy transformation**. EPSG identifies Indian 1975 / UTM zone 47N as EPSG:24047 and zone 48N as EPSG:24048, and multiple Indian-1975-to-WGS-84 coordinate operations exist for Thailand with published accuracies ranging from about 1 m for a limited-area operation to 3–5 m for broader operations. Consequently, the existing architecture's ≤1 mm transformation test must be limited to numerical round trips in a single CRS; it cannot be the acceptance criterion for legacy-datum georeferencing. citeturn36search0turn36search2turn36search4turn36search6turn36search8

Finally, the Phase Five host evidence has changed materially since the existing ADR was drafted. IngeCAD's licence is no longer uncertain: its source files identify `GPL-3.0-or-later`, it has a documented Python plugin contract, and its drawing model is directly based on `ezdxf`, named layers, entities and XDATA. IngeTrazo is also `GPL-3.0-or-later`, but its extension API explicitly remains unstable during the 0.x series and its scene model is primarily a 3D modelling abstraction. CADCraft 0.12.0 is MIT-or-Apache-2.0 and exposes an unusually strong authenticated local JSON control channel plus MCP, but the repository is extremely young. On current public evidence, **IngeCAD is the best first native CAD adapter candidate, CADCraft the best external-process/control-channel candidate, and IngeTrazo should remain third until its extension API stabilises**. fileciteturn63file0 fileciteturn53file0 fileciteturn65file0 fileciteturn57file0 fileciteturn64file0 fileciteturn62file0

## Findings

**Regulations and design standards**

**A1 — National Thai parking dimensions, aisle widths and minimum supply.**

**Fact.** The relevant national base is Ministerial Regulation No. 7 B.E. 2517, whose parking provisions continue to operate under the later Building Control Act framework. The consolidated legal text reviewed shows subsequent parking-related amendments by Ministerial Regulation No. 41 B.E. 2537 and Ministerial Regulation No. 64 B.E. 2555. No. 41 is particularly important because clause 1 repealed No. 7 clause 5 and clause 2 substituted the current parking-space dimensions. No. 64 later amended parts of the use/supply provisions, including hotel-related provisions. citeturn28view0turn23view0turn24view1turn28view1

For the national geometry:

| Parking arrangement | Current national minimum | Source |
|---|---:|---|
| Parallel to aisle or angle **< 30°** | 2.40 m wide × 6.00 m long | Ministerial Regulation No. 41 B.E. 2537, cl. 2(1) citeturn24view1 |
| Perpendicular | 2.40 m wide × 5.00 m long | No. 41 B.E. 2537, cl. 2(2) citeturn24view1 |
| Other oblique parking **> 30°** | 2.40 m wide × 5.50 m long | No. 41 B.E. 2537, cl. 2(3) citeturn24view1 |
| Exact 30° | **Still legally ambiguous from the national wording reviewed** | No. 41 distinguishes `<30°` and `>30°`; do not infer a value without legal confirmation. citeturn24view1 |

The national text also requires parking spaces to be marked and connected directly to circulation leading to the entrance/exit and adequate turning facility. Parking and associated aisles/vehicle ramps must have at least 2.10 m clear height. citeturn24view1

The sources reviewed did **not** establish a national numerical internal-aisle-width table by parking angle. Therefore a “Thai national” Stallwise profile must leave `aisle_width_by_angle` unverified/user-configurable rather than silently copying BMA values. BMA can have its own independently sourced table.

National minimum parking supply under No. 7, as currently amended, is use- and jurisdiction-dependent. The consolidated text distinguishes Bangkok from other municipalities/building-control areas and includes threshold conditions in clause 2; those trigger conditions must be evaluated before applying clause 3's parking ratios. citeturn28view0

For Bangkok under the national regulation, the consolidated clause 3 provides, among other cases, one space per 20 audience seats for a theatre generally, with a one-per-10-seat rule in the specifically enumerated central areas; hotel lobby and commercial areas use 1/10 m² and 1/20 m² respectively; condominium/family residential units covered by the regulation use one space per family unit; restaurant table area uses 1/15 m² up to the first 750 m² and 1/30 m² thereafter; department stores use 1/20 m²; offices 1/60 m²; halls 1/10 m²; and the large-building calculation is subject to the greater-of/summed-use mechanism stated in the clause, including a 1/120 m² large-building baseline. Outside Bangkok, several of those rates are lower, including theatre 1/40 seats, office 1/120 m² and large building 1/240 m². Fractions are treated according to the regulation's rounding provisions. citeturn28view0turn28view1

**Recommendation.** Model these as a rule tree, not as a few global constants:

`jurisdiction → building/use applicability → parking-supply formula → geometric parking rule → accessibility/fire overlays`.

Do not let the generator infer a parking-supply requirement merely from site area.

**A2 — BMA additions and differences.**

**Fact.** BMA Ordinance B.E. 2544 materially adds to and differs from the national scheme. Clauses 83–85 define covered uses and Bangkok parking supply; clause 86 defines parking-space geometry; clauses 88–91 add entrance/exit, aisle and road/interface rules; clauses 99–100 add ramp and parking-surface slope provisions. citeturn27view0turn26view0turn26view1

The most important surface-lot rule for Stallwise is clause 88:

- parking angle below 30° → aisle at least **3.50 m**;
- angle 30° through 60° → aisle at least **5.50 m**;
- angle over 60° → aisle at least **6.00 m**. citeturn27view0

Clause 88 also gives the general entrance/exit width of at least 6.00 m, or at least 3.50 m for a separate one-way entrance or exit. citeturn27view0

BMA's supply calculation is not simply a copy of national No. 7. For example, clause 84 uses hotel-room counts, one space per residential/condominium unit, office 1/60 m², department store 1/20 m² and additional categories such as market, factory, warehouse, hospital, educational building, service establishment and exhibition use. citeturn26view0turn27view0

**Uncertainty.** The relevant BMA B.E. 2544 clauses have been verified from the ordinance source reviewed, but this research pass did not produce a complete consolidated amendment history proving that every later Bangkok amendment leaves every one of these clauses unchanged. A Thai building-control lawyer or BMA officer should perform that final current-law check before Stallwise labels the profile “legally verified”.

**A3 — Accessible parking.**

**Fact.** The current source is the Ministerial Regulation prescribing facilities in buildings for persons with disabilities or mobility/functional limitations and elderly persons, as amended by **Ministerial Regulation No. 2 B.E. 2564**. Amendment clause 9 replaces clauses 12–14 of the earlier regulation. citeturn24view0turn23view1turn23view2

The current count is:

| Total ordinary parking supply | Minimum accessible spaces |
|---:|---:|
| Up to 25 | 1 |
| 26–50 | 2 |
| 51–75 | 3 |
| 76–100 | 4 |
| 101–150 | 5 |
| 151–200 | 6 |
| Above 200 | Add 1 for each further 100; a remainder exceeding 50 is treated as another 100 |

These values are from the replaced clause 12 under No. 2 B.E. 2564. citeturn23view1

Current clause 13 requires accessible parking to be located as close as practicable to an accessible building entrance/exit on a smooth, level route; it also prescribes wheelchair-symbol pavement/sign dimensions and sign mounting. citeturn23view1turn23view2

Current clause 14 refers parking-space geometry back to Ministerial Regulation No. 41 clauses 2–3 and additionally requires a **clear strip at least 1.00 m wide along the full length of the parking space**, smooth and level. citeturn23view2

**Recommendation.** Represent this as `base_vehicle_stall + accessible_side_clear_zone`, not as a fabricated “3.40 m accessible stall”. That distinction matters for geometry, DXF layers, area calculations and any later legal interpretation of whether clear zones can be shared.

**A4 — Ramps, turning, clear height and entrances.**

**Fact.** The national current clear height is at least 2.10 m over vehicle parking, circulation and ramps under Ministerial Regulation No. 41 B.E. 2537 clause 4. citeturn24view1 No. 7 clause 7 requires adequate turning provision and permits omission of a turnaround where a one-way route runs from an entrance through to an exit; it does not, in the source reviewed, establish a general numerical surface-lot turning radius. citeturn28view0

No. 7 clause 8 establishes at least 6.00 m for the general parking entrance/exit and at least 3.50 m for separated one-way access, together with separation requirements from intersections/bends and bridge ramps. citeturn28view0

For Bangkok, Ordinance B.E. 2544 clause 99 limits ordinary vehicle ramps to **15%**, requires an intermediate landing where the vertical rise of a ramp run exceeds the prescribed 5 m threshold, and limits curved/spiral ramps to **12%** with at least **6 m inner radius**. Clause 100 limits parking-floor/surface slope to 5%. citeturn26view1

That 6 m radius is specifically a BMA curved-ramp rule; it must **not** be mislabelled as the general minimum surface-lot vehicle turning radius.

**A5 — Fire access.**

**Fact.** Ministerial Regulation No. 33 B.E. 2535 applies special requirements to high-rise and extra-large buildings. Clause 3 requires an uncovered road/open-space route of at least **6.00 m** around the relevant building such that fire vehicles can enter and leave conveniently. The regulation defines the high-rise/extra-large-building scope separately. citeturn24view3

**Recommendation.** Add a conditional `fire_access_keepout` geometry type. For applicable projects it should be subtracted from the stall-generation region and rendered/exported distinctly. Do not globally impose a 6 m fire lane on ordinary surface lots for which No. 33 does not apply.

**A6 — Motorcycle parking.**

**Fact.** No general national/BMA building-control motorcycle-stall dimensional provision was identified in the authoritative parking clauses reviewed in this pass.

That is **not** proof that no Thai national, BMA, local, transport, land-use or project-specific motorcycle requirement exists.

**Recommendation.** Keep motorcycle dimensions and ratios as `project_policy` or `local_rule_override`, explicitly `unverified`, rather than including them in the first verified RS-2 dataset.

**A7 — EV charging spaces.**

**Fact.** PEA publishes technical requirements for EV charging-system installation, and Thai investment/electricity frameworks also refer to compliance with charging electrical/safety standards. The sources located in this pass did not establish a general Building Control Act parking-space quota or special EV-stall geometry requirement applicable to ordinary Stallwise surface lots. citeturn20search0turn20search3turn22search2turn22search5

**Recommendation.** Treat `EV` initially as a user/project allocation overlay with electrical-service, charger-clearance and accessible-route considerations. It must not contribute a supposed statutory EV minimum until a specific current law is verified.

**A8 — International comparison profiles.**

**Fact.** The most readily machine-encodable comparison is the U.S. **2010 ADA Standards for Accessible Design**, which contains explicit accessible-parking counts and geometry. It is materially different from Thailand and therefore useful as an example of a separate jurisdiction profile, not as a Thai fallback. citeturn29search0

For the UK, authoritative references include government street/design-accessibility guidance such as *Manual for Streets* and *Inclusive Mobility*, rather than one universal parking-lot geometry table applicable to every project. citeturn29search1turn30search0turn30search1 Singapore's LTA publishes current development/vehicle-parking guidance, while Japan's MLIT publishes parking-related regulatory and design material. citeturn29search2turn29search3

**Recommendation.** Do not implement “International” as a fallback ruleset. Implement explicit named and versioned profiles such as `US_ADA_2010`, and only add UK/Singapore/Japan rule profiles after the specific statutory or agency source for every encoded value is identified.

**Prior art and algorithms**

**B1 — Publicly documented behaviour of existing tools.**

**Fact.** TestFit's public support material confirms generative behaviour around surface-lot parking and documents at least one concrete limitation: its high-density/massing configurators place double-loaded drive aisles, while single-loaded parking was not directly manually placeable in the documented workflow and had to be represented using a road type. That is useful evidence that practical generative parking tools combine automated modules with manual/site-network intervention; it does not disclose TestFit's solver internals. citeturn35search5

ParkCAD publicly exposes parking “standards” consisting of vehicle categories/classes, parking angles, stall width/length, one-way aisle width and two-way aisle width. Its wizard can generate a matrix of configurations and calculate remaining layout values from user-supplied required values. It also permits customised stall dimensions for accessibility requirements. citeturn35search7turn35search8turn35search9

**Recommendation.** The prior-art lesson for Stallwise is not to copy either UI. It is to preserve three product capabilities already anticipated by the spec: versioned rule/standard definitions, automatic module generation, and selective manual editing/locking. Those are behaviours, not protected branding or interface cloning.

**B2 — Academic/open algorithm approaches.**

A highly relevant recent optimisation result is Thomas and Rambha's parking-lot design work. Their formulation rasterises arbitrary lots, uses mixed-integer programming to maximise perpendicular stalls, enforces stall/driveway connectivity to entrances/exits, and supports one-way and two-way circulation. Their branch-and-cut reformulation removes flow variables and big-M-style constraints; the authors evaluate it on **325 New York City parking lots** and report substantial median runtime improvements over their flow formulation on solvable instances. They also report higher capacity for one-way configurations in their tested dataset. citeturn35academia48turn35search2turn35search3

That paper is particularly valuable to Stallwise not because Phase One should adopt a MIP, but because it demonstrates that **connectivity must be inside the optimisation/validation problem rather than checked only visually after stall packing**. It also provides a plausible future exact/near-exact oracle for small 90° cases. citeturn35academia48

Earlier parking-layout research also demonstrates that stall angle and circulation geometry are coupled rather than independent. For example, Chen and Schonfeld analytically studied area-per-stall against parking angle and reported an optimum around 70° for their large-lot assumptions rather than treating 90° as universally optimal. That result should not be imported into Thai rules, but it supports Phase Six orientation search rather than hard-coding a single angle. citeturn35search6

Other optimisation families such as simulation-based multiobjective/metaheuristic methods appear in specialised autonomous-valet layouts, including NSGA-II-based work, but those solve a different operational problem and are not a justified Phase One dependency. citeturn35search0turn35search10

**B3 — Baseline and upgrade path.**

**Recommendation.** Use a deterministic **orientation × module-offset strip enumeration** solver in Phase One. It is simpler to explain and regression-test than a genetic/metaheuristic solver, maps naturally to real parking modules, and can guarantee repeatability under `CLAUDE.md`'s rules. fileciteturn1file0 fileciteturn10file0

For Phase Six, retain the same geometric candidate generator but add:

`zone decomposition → orientation assignment → local neighbourhood moves → graph feasibility → multiobjective scoring`.

For small perpendicular-only cases, add an optional MIP/branch-and-cut benchmark oracle inspired by the published formulation rather than replacing the production solver wholesale. citeturn35academia48

**B4 — Benchmarks.**

**Fact.** The published 325-NYC-lot study is currently the strongest identified external benchmark family for conventional perpendicular parking with connectivity. This research pass did not verify that the complete 325-site geometry/count dataset is publicly downloadable, so it should be listed as a **published benchmark reference, availability unverified**, rather than committed as a test asset. citeturn35academia48turn35search3

**Recommendation.** Phase One should instead rely first on Stallwise-owned synthetic fixtures whose optimal count is analytically known, and add legally distributable real sites later.

**Technology choices**

**C1 through C5 — Dependency evidence.** The following versions are the current versions or current stable releases located as of this research date. “AGPL compatible” here means suitable for incorporation/distribution in an AGPL-3.0-or-later Stallwise project subject to the dependency's own attribution/source obligations; it is a dependency-screening conclusion, not bespoke legal advice.

| Library | Current version | Licence | Maintenance evidence | Browser/WASM relevance | AGPL-3.0-or-later | Research decision |
|---|---:|---|---|---|---|---|
| `geo` | 0.33.1 | MIT OR Apache-2.0 | Active; current repository was being updated in Oct. 2026 | Pure Rust geometry path; Boolean operations and buffer APIs present | Compatible | **Default geometry façade** fileciteturn12file0turn13file0turn14file0turn14file1 |
| `geo-clipper` | 0.9.0 | ISC | Maintained but comparatively quiet; repo last push found Feb. 2025 | Uses `clipper-sys`, adding native/C++ toolchain complexity | Compatible | Do not make default; benchmark fallback fileciteturn15file0turn16file0 |
| `clipper2` Rust binding | 0.6.0 | MIT OR Apache-2.0 | Current maintained binding | Wraps C++ Clipper2; WASM build path requires native/WASI tooling | Compatible | Robustness benchmark/fallback, not Phase One default fileciteturn19file0turn18file5 |
| `i_overlay` | 9.1.0 | MIT OR Apache-2.0 | Active/current | Pure Rust/no native FFI barrier | Compatible | Benchmark direct use only; `geo` already provides higher-level integration fileciteturn22file0 |
| `dxf-parser` | 1.1.2 | MIT | Low activity; last repository push located June 2024 | Browser-native JS; parser only | Compatible | Fallback only fileciteturn32file0turn33file0 |
| Rust `dxf` (`dxf-rs`) | 0.6.2 | MIT | Active; repository pushed Oct. 2026 | Pure-Rust candidate; read/write DXF and DXB | Compatible | **Primary Phase Three DXF spike candidate** fileciteturn36file0turn37file0 |
| `acadrust` | 0.6.6 | MPL-2.0 | Very active but young; repository created Jan. 2026 and pushed Oct. 22 | Pure Rust; explicitly handles WASM sequentially; DXF/DWG | Compatible with MPL obligations | Secondary DXF candidate; strongest future DWG candidate fileciteturn38file0turn39file0turn41file0 |
| PixiJS | 8.22.0 | MIT | Active/current | Web renderer; browser and worker bundles | Compatible | **Preferred stall editor renderer** subject to benchmark fileciteturn30file0 |
| Konva | 10.9.0 | MIT | Active/current | Interactive HTML Canvas scene graph | Compatible | Simpler alternative; benchmark against Pixi fileciteturn42file0 |
| MapLibre GL JS | 6.15.0 | BSD-3-Clause | Active/current | WebGL map renderer | Compatible | **Recommended map renderer** fileciteturn43file0 |
| Terra Draw | 1.38.0 | MIT | Active/current | Map drawing/editing adapters including MapLibre | Compatible | **Recommended map polygon editor** fileciteturn45file0 |
| proj4js | 2.22.0 stable; main already 2.22.1-alpha | MIT | Active; 2.22.0 released Aug. 31, 2026 | Browser CRS/datum transforms | Compatible | Keep, but change accuracy model fileciteturn46file0turn47file0 |

**C1 — Polygon operations.**

**Recommendation.** Freeze the initial geometry dependency to `geo = 0.33.1`. Its current Boolean and buffer functionality substantially reduces the reason for a second clipping API, and using a pure-Rust default makes the Rust→WASM target much less fragile. fileciteturn13file0turn14file0turn14file1

This is **not** a claim that `geo` has been proven more numerically robust than Clipper2 for Stallwise. Phase One should create a polygon torture suite—holes, near-collinear edges, narrow slivers, duplicate vertices, almost-touching obstacles, large UTM coordinates shifted to local origin—and benchmark `geo` against direct `i_overlay` and one Clipper implementation before the ADR becomes Accepted.

**C2 — DXF in the browser.**

`dxf-parser` is attractive for zero-friction browser reading but it creates a second JS-side CAD model, is parser-oriented rather than a read/write solution, and the repository activity is materially lower than the Rust alternatives. fileciteturn32file0turn33file0

The `dxf` crate 0.6.2 is the cleanest first experiment because it is MIT-licensed, long-running, currently active and explicitly describes itself as a reader/writer for DXF/DXB. fileciteturn36file0turn37file0

`acadrust` is much broader: its current documentation states ASCII/binary DXF and native binary DWG read/write from R12 through R2018+, broad entity coverage, code-page handling, Serde support and sequential WebAssembly operation. It is MPL-2.0 rather than permissive, but MPL-2.0 is not a GPL-2.0-only blocker; modifications to MPL-covered files carry MPL source/notice obligations. fileciteturn39file0turn41file0

**Recommendation.** Do not write the v0.2 architecture as though the DXF decision is settled. Phase Three should run the same fixture corpus through `dxf` and `acadrust` under `wasm32`, testing the exact Stallwise entity subset, `$INSUNITS`, layers, blocks/inserts, bulges/arcs, malformed files and round-trip export.

**C3 — Canvas editor.**

**Fact.** PixiJS 8.22.0 and Konva 10.9.0 are both current MIT-licensed options. Pixi exposes a GPU-oriented rendering architecture, while Konva is explicitly an interactive HTML5 2D Canvas/design-editor library. fileciteturn30file0turn42file0

**Recommendation.** Prefer **PixiJS** for the main plan editor because Stallwise can plausibly render thousands of stall, aisle, boundary, handle and overlay primitives simultaneously. Keep editing state, snapping and domain identity outside Pixi so the renderer remains replaceable. Konva should be retained as the benchmark alternative if Phase Three shows that its higher-level interaction facilities materially reduce editor complexity without violating the performance target.

Plain SVG is appropriate for export and small overlays, but should not be the main scene model for the expected editable object count. Plain immediate-mode Canvas avoids a dependency but would make Stallwise own hit testing, retained state, invalidation and object interaction itself. Those are engineering trade-offs, not legal requirements.

**C4 — Map stack and imagery terms.**

MapLibre GL JS 6.15.0 plus Terra Draw 1.38.0 remains the strongest stack from the candidates already in the architecture: both are permissively licensed, and Terra Draw has a dedicated MapLibre adapter. fileciteturn43file0turn45file0

The **OpenStreetMap data licence must be distinguished from the public OSM tile service**. OSMF explicitly states that OSM data is free but its `tile.openstreetmap.org` servers are a limited, best-effort service; attribution is required, bulk/offline downloading is prohibited, and applications that cannot meet the policy should use another provider or self-host. It therefore should not be Stallwise's assumed production tile backend. citeturn36search10

OpenFreeMap is a possible hosted open-map default: its terms as of 14 October 2026 describe a free as-is service and explicitly permit limited offline downloads up to 3,000 tiles or 50 MB per download with request constraints. It carries no service guarantee and can change or discontinue. citeturn37search0

**Satellite imagery remains unresolved.** This research pass did not verify a general-purpose, high-resolution satellite/aerial provider whose current hosted-service terms can safely be declared the universal default for a potentially hosted AGPL application.

**Recommendation.** Architecture should separate:

`Map renderer` → MapLibre  
`Drawing` → Terra Draw  
`Basemap style/tile provider` → configurable  
`Satellite provider` → configurable, opt-in, provider-specific API key and attribution

and ship no production satellite default until its terms are explicitly reviewed.

**C5 — Thai CRS.**

The existing `IN-R7` is correct for WGS 84 UTM: Stallwise already records EPSG:32647 and EPSG:32648. fileciteturn1file0 It should be expanded with:

- **EPSG:24047** — Indian 1975 / UTM zone 47N;
- **EPSG:24048** — Indian 1975 / UTM zone 48N. citeturn36search2turn36search5

EPSG lists multiple Indian-1975-to-WGS-84 operations in Thailand. The default/onshore operation shown for these CRSs carries approximately **3 m** published accuracy; other broader operations are about **5 m**, while a more localised operation is listed at **1 m**. citeturn36search0turn36search4turn36search6turn36search8

A Proj4js definition can contain a particular `+towgs84` transform, but choosing that transform fixes a particular datum operation rather than magically guaranteeing survey accuracy. For example, EPSG's exported Proj4js representation for EPSG:24047 includes explicit seven-parameter `towgs84` values for the selected operation. citeturn36search2turn36search8

**Recommendation.** Store at least:

```text
source_crs
target_crs
datum_operation_id/name
declared_operation_accuracy_m
control_point_residual_m, if locally fitted
transform_provenance
```

and tell users when the legacy datum transform is only metre-class. A 1 mm test remains reasonable for local numerical geometry/round-trip arithmetic, but is fundamentally inappropriate as a real-world Indian-1975↔WGS-84 geodetic acceptance threshold.

**CAD plugin targets**

The public evidence now supports the following matrix.

| Host | Licence / current version | Extension mechanism | External-process route | Entity/document fit | Activity/maturity | Stallwise implication |
|---|---|---|---|---|---|---|
| IngeTrazo | GPL-3.0-or-later; 0.5.9 | Python file/package extensions; `setup(app)`; Extension API 2 | Python can invoke external tooling; host also exposes a localhost MCP bridge | Scene/group/mesh-oriented 3D model; plugin document data, overlays and scripting | Very active in Oct. 2026, but plugin API explicitly unstable throughout 0.x | Compatible, but integration surface is less naturally 2D-CAD-centric fileciteturn48file0turn53file0turn61file0turn63file0 |
| IngeCAD | GPL-3.0-or-later; 0.6.8.2 | Python `PluginSpec`, commands, tools, menus, toolbars; APPLOAD Python scripts | Python adapter can launch Stallwise CLI; scripts/plugins operate headlessly through actions | **Excellent fit:** `ezdxf` drawing is model; named layers, plain DXF entities, XDATA, undoable commands | Active Oct. 2026; still young but explicit plugin contract/test suite | **Best first native adapter candidate** fileciteturn54file0turn57file0turn65file0 |
| CADCraft | MIT OR Apache-2.0; 0.12.0 | No Stallwise-specific native plugin API required for basic integration; CLI, command system, scripts/LISP and control APIs | **Strongest route:** authenticated JSON-lines local control channel and MCP over JSON-RPC/stdio | Can inspect entities/layers/selection and execute commands; native DXF model plus DWG bridge | Extremely active but repository is very new; Oct. 2026 origin | **Best external/control-channel integration candidate** fileciteturn58file0turn60file1turn60file12turn62file0turn64file0 |

**D1 — Licence.** IngeTrazo and IngeCAD source files identify GPL-3.0-or-later. CADCraft's workspace is MIT OR Apache-2.0. The current ADR's statement that IngeCAD's licence is unconfirmed should therefore be removed. fileciteturn63file0turn65file0turn64file0

**D2 — Plugin mechanism and stability.** IngeTrazo has a Python extension system, but its own documentation says the API is not stable during the 0.x series and warns that some API-2 workspace facilities can change without a major-version bump. fileciteturn53file0 IngeCAD has a much more CAD-specific Python plugin contract with `PluginSpec`, command handlers, tools and an explicit “every mutation is a Command” rule. fileciteturn57file0 CADCraft's strongest public extension boundary for Stallwise is currently automation rather than an in-process plugin: its JSON control protocol, CLI, script/LISP facilities and MCP. fileciteturn60file11turn62file0

**D3 — Calling an external process.** For both Python hosts, a thin adapter can launch Stallwise's versioned JSON CLI as a subprocess, preserving the desired one-Rust-engine architecture. For CADCraft, an even cleaner alternative is for the Stallwise-side bridge to talk to CADCraft's authenticated loopback JSON channel or MCP rather than load into the host process. CADCraft's protocol supports command execution, drawing inspection, file operations and structured selected-entity retrieval. fileciteturn62file0

**D4 — Entity model.** IngeCAD is the easiest match. Its documentation explicitly states that the `ezdxf` document is the model and that plugins write ordinary DXF entities on named layers, with XDATA for plugin-specific identity. fileciteturn57file0 CADCraft exposes layer/entity/selection data through `drawing.inspect` and its `entities` command and can execute headless drawing commands over JSON. fileciteturn62file0 IngeTrazo can read/mutate its scene through extensions or `run_python`, but the abstraction is oriented to meshes, groups and a 3D model rather than an ordinary 2D DXF entity document. fileciteturn53file0turn61file0

**D5 — Activity and maturity.** All three projects were active in October 2026, but they are not equally mature. IngeTrazo was created in June 2026 and showed substantial activity/open issues by October; IngeCAD was created in July 2026; CADCraft's repository was created only on 7 October 2026 despite extremely rapid activity and adoption signals. Repository age therefore matters more than raw star or issue counts when assessing API stability. fileciteturn48file0turn54file0turn58file0

**D6 — AGPL adapter implications.** An AGPL-3.0-or-later Stallwise adapter is not blocked by these host licences. GPL-3.0-or-later and AGPL-3.0 are designed to permit combined GPL/AGPL works under their respective provisions; CADCraft's MIT/Apache licensing is permissive. The lowest-coupling architecture remains a very thin host-side adapter plus a separately versioned Stallwise CLI JSON protocol, exactly as the current Stallwise architecture anticipates. fileciteturn2file0turn6file0 Distribution details and any bundling of host code should nevertheless receive a final licence review before release.

**Product and UX**

**E1 — Expected study outputs.**

**Fact.** BMA currently publishes formal checklists for building-construction permit review, including distinct processes for buildings below and above 300 m². This confirms that the eventual authority-facing workflow sits inside a formal drawing/document submission process, but the public search material reviewed does **not** establish a separate, universally prescribed “parking feasibility study report” format. citeturn37search5turn37search6turn37search15

**Recommendation.** `OUT-1` should therefore generate the information a Thai architect/engineer can place directly into permit/concept drawings rather than claim to produce an official filing package:

- annotated plan with boundaries, stalls by type, aisle widths and dimensions;
- required-vs-provided parking calculation by use and rule source;
- standard/accessibility/EV/motorcycle counts;
- accessible-space and clear-zone schedule;
- site area, parking/circulation area and project-selected ratios;
- entrances/exits, fire/access keep-outs and relevant dimensions;
- rule-set name, version, jurisdiction and legal citations;
- assumptions and explicit unverified rules.

The existing `OUT-1` already points in this direction; the key addition is a compliance/citation ledger. fileciteturn1file0

**E2 — Typical Thai site size and complexity.**

**Fact.** No defensible public Thai dataset was identified in this pass that supports the existing `NFR-2` assertion that a “typical site” is ≤2 ha, ≤50 boundary vertices and ≤20 obstacles. Those numbers currently remain product assumptions in the spec, not researched Thai market facts. fileciteturn1file0

**Recommendation.** Preserve the numbers only as an **initial benchmark tier**, not as a claim about typical Thai projects. Before v1.0, collect anonymised metadata from approximately representative real user files—area, boundary vertices, holes/obstacles, candidate stalls and solve time—and reset the target empirically.

**E3 — Editing interactions that matter.**

Public ParkCAD documentation strongly supports per-project/custom standard editing, while TestFit's public documentation demonstrates why a generated result must support manual correction when the generative model cannot represent a desired single-loaded condition directly. citeturn35search5turn35search8turn35search9

**Recommendation.** The highest-value Stallwise editing interactions are therefore:

`regenerate selected zone → lock/unlock zone → move/delete/add stall → change row angle/orientation → convert stall type → move/resize keep-out → edit aisle/entry → undo/redo → compare alternatives`.

The generator must preserve IDs for unaffected locked objects, otherwise practical iterative design becomes frustrating and CAD round-tripping becomes unstable.

## Thai regulatory rule set

The following is the proposed first data set for `RS-2`. “Verified” means the cited text was located and the stated numeric value can be traced to the named clause. “Unverified” means Stallwise must not treat the value as law.

### Geometry, access and overlays

| Parameter | Value | Unit | Legal source / clause | Status |
|---|---:|---|---|---|
| National parallel / angle `<30°` stall width | 2.40 | m | Ministerial Regulation No. 41 B.E. 2537, cl. 2(1) citeturn24view1 | verified |
| National parallel / angle `<30°` stall length | 6.00 | m | No. 41 B.E. 2537, cl. 2(1) citeturn24view1 | verified |
| National perpendicular stall width | 2.40 | m | No. 41 B.E. 2537, cl. 2(2) citeturn24view1 | verified |
| National perpendicular stall length | 5.00 | m | No. 41 B.E. 2537, cl. 2(2) citeturn24view1 | verified |
| National other oblique `>30°` width | 2.40 | m | No. 41 B.E. 2537, cl. 2(3) citeturn24view1 | verified |
| National other oblique `>30°` length | 5.50 | m | No. 41 B.E. 2537, cl. 2(3) citeturn24view1 | verified |
| National exact 30° stall category | — | — | No. 41 cl. 2 wording reviewed does not safely resolve exact 30° | **unverified** |
| National perpendicular stalls with one-way circulation | prohibited by wording reviewed | boolean | No. 41 B.E. 2537, cl. 2(2) citeturn24view1 | verified; lawyer should confirm implementation interpretation |
| National internal aisle width by angle | — | m | No general numerical table identified in No. 7/41 sources reviewed | **unverified** |
| National general entrance/exit width | ≥6.00 | m | Ministerial Regulation No. 7 B.E. 2517, cl. 8 citeturn28view0 | verified |
| National separated one-way entrance or exit width | ≥3.50 | m | No. 7 B.E. 2517, cl. 8 citeturn28view0 | verified |
| National vehicle clear height for parking/aisle/ramp | ≥2.10 | m | No. 41 B.E. 2537, cl. 4 citeturn24view1 | verified |
| Maximum path from qualifying off-site parking to building | ≤200 | m | No. 7 B.E. 2517, cl. 6 citeturn28view0 | verified |
| General numerical surface-lot turning radius | — | m | No. 7 cl. 7 requires adequate turning but no general number found citeturn28view0 | **unverified** |
| BMA perpendicular stall | 2.40 × 5.00 | m | BMA Building Control Ordinance B.E. 2544, cl. 86 citeturn27view0 | verified |
| BMA parallel / `<30°` stall | 2.40 × 6.00 | m | BMA Ordinance B.E. 2544, cl. 86 citeturn27view0 | verified |
| BMA other oblique `≥30°` stall | 2.40 × 5.50 | m | BMA Ordinance B.E. 2544, cl. 86 citeturn27view0 | verified |
| BMA aisle, parking angle `<30°` | ≥3.50 | m | BMA Ordinance B.E. 2544, cl. 88 citeturn27view0 | verified |
| BMA aisle, parking angle `30°–60°` | ≥5.50 | m | BMA Ordinance B.E. 2544, cl. 88 citeturn27view0 | verified |
| BMA aisle, parking angle `>60°` | ≥6.00 | m | BMA Ordinance B.E. 2544, cl. 88 citeturn27view0 | verified |
| BMA general entrance/exit width | ≥6.00 | m | BMA Ordinance B.E. 2544, cl. 88 citeturn27view0 | verified |
| BMA separated one-way entrance or exit | ≥3.50 | m | BMA Ordinance B.E. 2544, cl. 88 citeturn27view0 | verified |
| BMA parking ≥15 spaces: connecting public road | ≥6.00 | m | BMA Ordinance B.E. 2544, cl. 90 citeturn27view0 | verified |
| BMA entrance/exit centreline from start of intersection curve/bend | ≥20 | m | BMA Ordinance B.E. 2544, cl. 89 citeturn27view0 | verified |
| BMA entrance/exit from bridge-ramp end, subject to clause exceptions | ≥50 | m | BMA Ordinance B.E. 2544, cl. 91 citeturn27view0 | verified |
| BMA ordinary vehicle ramp slope | ≤15 | % | BMA Ordinance B.E. 2544, cl. 99 citeturn26view1 | verified |
| BMA curved/spiral vehicle ramp slope | ≤12 | % | BMA Ordinance B.E. 2544, cl. 99 citeturn26view1 | verified |
| BMA curved/spiral ramp inner radius | ≥6.00 | m | BMA Ordinance B.E. 2544, cl. 99 citeturn26view1 | verified |
| BMA parking surface slope | ≤5 | % | BMA Ordinance B.E. 2544, cl. 100 citeturn26view1 | verified |
| Accessible spaces, total parking ≤25 | ≥1 | space | Accessibility Ministerial Regulation No. 2 B.E. 2564, amendment cl. 9 replacing cl. 12 citeturn23view1 | verified |
| Accessible spaces, total 26–50 | ≥2 | spaces | same source citeturn23view1 | verified |
| Accessible spaces, total 51–75 | ≥3 | spaces | same source citeturn23view1 | verified |
| Accessible spaces, total 76–100 | ≥4 | spaces | same source citeturn23view1 | verified |
| Accessible spaces, total 101–150 | ≥5 | spaces | same source citeturn23view1 | verified |
| Accessible spaces, total 151–200 | ≥6 | spaces | same source citeturn23view1 | verified |
| Accessible increment above 200 | +1 per further 100; remainder >50 treated as 100 | spaces | same source citeturn23view1 | verified |
| Accessible side clear strip width | ≥1.00 | m | Current cl. 14 as replaced by No. 2 B.E. 2564 citeturn23view2 | verified |
| Accessible side clear strip length | full stall length | — | current cl. 14 citeturn23view2 | verified |
| Accessible location | nearest practicable accessible entrance/exit; smooth/level route | — | current cl. 13 citeturn23view1turn23view2 | verified |
| Fire-access corridor for applicable high-rise/extra-large building | ≥6.00 | m | Ministerial Regulation No. 33 B.E. 2535, cl. 3 citeturn24view3 | verified, conditional |
| Motorcycle stall dimensions | — | m | No general value verified | **unverified** |
| General EV parking-space quota | — | spaces / % | No building-control quota verified in reviewed sources citeturn20search0turn22search2 | **unverified** |
| General EV stall dimensions | — | m | No statutory geometry verified in reviewed sources | **unverified** |

### Minimum parking supply

The formulas below require the corresponding use to fall within the regulation's applicability provisions; they must not be applied to every building indiscriminately. citeturn28view0turn26view0

| Profile / use | Minimum supply | Source | Status |
|---|---|---|---|
| National/Bangkok theatre, general | 1 space / 20 audience seats | No. 7 B.E. 2517, cl. 3 citeturn28view0 | verified |
| National/Bangkok theatre, specified central areas | 1 / 10 audience seats | No. 7, cl. 3 citeturn28view0 | verified; district list must be encoded exactly from source |
| National/Bangkok hotel lobby | 1 / 10 m² | No. 7 as amended, cl. 3 / No. 64 B.E. 2555 citeturn28view0turn28view1 | verified |
| National/Bangkok hotel commercial area | 1 / 20 m² | same source citeturn28view0turn28view1 | verified |
| National/Bangkok covered condominium/family unit | 1 / family unit | No. 7, cl. 3 citeturn28view0 | verified |
| National/Bangkok restaurant table area, first 750 m² | 1 / 15 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/Bangkok restaurant table area above 750 m² | 1 / 30 m² on excess | No. 7, cl. 3 citeturn28view0 | verified |
| National/Bangkok department store | 1 / 20 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/Bangkok office | 1 / 60 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/Bangkok hall | 1 / 10 m² | No. 7 as amended citeturn28view0turn28view1 | verified |
| National/Bangkok large building baseline | 1 / 120 m², subject to greater-of/summed-use rule | No. 7, cl. 3–4 citeturn28view0 | verified |
| National/outside Bangkok theatre | 1 / 40 audience seats | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok hotel lobby | 1 / 30 m² | No. 7 as amended citeturn28view0turn28view1 | verified |
| National/outside Bangkok hotel commercial | 1 / 40 m² | same source citeturn28view0turn28view1 | verified |
| National/outside Bangkok covered condominium/family units | 1 / 2 family units | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok restaurant | 1 / 40 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok department store | 1 / 40 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok office | 1 / 120 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok hall | 1 / 30 m² | No. 7, cl. 3 citeturn28view0 | verified |
| National/outside Bangkok large-building baseline | 1 / 240 m², subject to greater-of/summed-use rule | No. 7, cl. 3–4 citeturn28view0 | verified |
| BMA theatre | 1 / 10 audience seats | BMA Ordinance B.E. 2544, cl. 84 citeturn26view0turn27view0 | verified |
| BMA hotel, first 30 rooms | 10 spaces | BMA Ordinance B.E. 2544, cl. 84 citeturn26view0 | verified |
| BMA hotel, rooms 31–100 | +1 / 5 rooms | same source citeturn26view0 | verified |
| BMA hotel, above 100 rooms | first-100 calculation +1 / 10 excess rooms | same source citeturn26view0 | verified |
| BMA residential/condominium unit covered by cl. 83 | 1 / unit | BMA Ordinance B.E. 2544, cl. 84 citeturn26view0 | verified |
| BMA restaurant first 150 m² table area | 10 spaces | BMA Ordinance B.E. 2544, cl. 84 citeturn26view0 | verified |
| BMA restaurant above first 150 m² | +1 / 20 m² excess | same source citeturn26view0 | verified |
| BMA department store | 1 / 20 m² | same source citeturn26view0 | verified |
| BMA office | 1 / 60 m² | same source citeturn26view0 | verified |
| BMA market | 1 / 120 m² | same source citeturn26view0 | verified |
| BMA factory | 1 / 240 m² | same source citeturn26view0 | verified |
| BMA warehouse | 1 / 240 m² | same source citeturn26view0 | verified |
| BMA storage | 1 / 120 m² | same source citeturn26view0 | verified |
| BMA hospital | 1 / 120 m² | same source citeturn26view0 | verified |
| BMA educational building | 1 / 240 m² | same source citeturn26view0 | verified |
| BMA service establishment | 1 / 60 m² | same source citeturn26view0 | verified |
| BMA exhibition use | 1 / 20 m² | same source citeturn26view0 | verified |
| BMA hall | 1 / 10 m² | same source citeturn26view0 | verified |
| BMA commercial use | 1 / 60 m² | same source citeturn26view0 | verified |
| BMA large building | greater of 1 / 120 m² and use-by-use calculation, subject to stated exceptions | BMA Ordinance B.E. 2544, cl. 84–85 citeturn26view0turn27view0 | verified |

**Implementation caution:** these supply rows are not sufficient by themselves to determine legality. Stallwise must encode the threshold/applicability predicates in No. 7 clause 2 and BMA clause 83 as well as mixed-use and rounding provisions in No. 7 clause 4 / BMA clause 85. citeturn28view0turn26view0

## Proposed edits

The current documents are internally consistent but several research assumptions are now resolved or need correction. fileciteturn1file0 fileciteturn2file0 fileciteturn3file0

| Document / requirement | Proposed v0.2 edit | Basis |
|---|---|---|
| `SPEC.md` `IN-R7` | Add EPSG:24047 and EPSG:24048; store a named datum operation and its declared accuracy. State that legacy Indian 1975 transformation may be metre-class. | EPSG operations show 1–5 m transformation accuracies, commonly 3 m onshore. citeturn36search0turn36search2turn36search4 |
| `SPEC.md` new `IN-R8` | On CRS conversion, record `source_crs`, `target_crs`, operation/provenance, published accuracy and any control-point residual. Warn when geodetic uncertainty exceeds user threshold. | Prevents false survey precision. |
| `SPEC.md` `RS-1` | Extend rule-set metadata to `{id, jurisdiction, authority, title, edition_year_be, effective/as_of, source_citations[], verification_status}`. | Required for reproducible legal rules. |
| `SPEC.md` `RS-2` | Replace one “Thai regulatory” profile with at least `TH_NATIONAL` and `TH_BMA`; encode use/applicability predicates, supply formulas, stall geometry, accessibility and conditional fire overlays. | National/BMA rules materially differ. citeturn28view0turn27view0 |
| `SPEC.md` new `RS-4` | Regulatory values may only be `verified` or `unverified`; generator must not silently substitute another jurisdiction's value for an unverified rule. | Prevents invented national aisle widths, motorcycle/EV rules. |
| `SPEC.md` new `RS-5` | Define exact boundary semantics for angle intervals. National exact 30° remains blocked/unverified until legal resolution; BMA can use its explicit interval. | No. 41 wording gap. citeturn24view1 |
| `SPEC.md` parking parameters | Separate `stall_geometry`, `drive_aisle`, `entry_exit`, `access_clear_zone`, `fire_keepout`, `project_policy_space`. | Accessible side strip/fire/EV are not ordinary stall rectangles. |
| `SPEC.md` circulation | Add rule validation that rejects nationally prohibited rule/direction combinations, including the verified No. 41 perpendicular/one-way case unless legal review changes interpretation. | No. 41 cl. 2. citeturn24view1 |
| `SPEC.md` `GEN-R1` | Keep 1 mm as an **internal planar geometry tolerance**, explicitly not a geodetic datum accuracy statement. | Geometry precision and CRS accuracy are different quantities. |
| `SPEC.md` `GEN-R2` | Require each generated stall to map to a reachable aisle component and every required aisle component to reach at least one declared entry/exit. | Aligns with Thai circulation rules and optimisation literature. citeturn28view0turn35academia48 |
| `SPEC.md` `OUT-1` | Add compliance ledger: required/provided spaces, rule-set ID/version, clause citation per calculated requirement, unverified assumptions and warning list. | Makes output useful for professional review without claiming authority approval. |
| `SPEC.md` `NFR-2` | Rename current “typical site” figures to `initial benchmark tier`. Do not claim ≤2 ha/50 vertices/20 obstacles are Thai market norms until measured. | No empirical Thai dataset verified. |
| `ARCHITECTURE.md` polygon stack | Make `geo 0.33.1` the initial geometry façade. Keep direct `i_overlay 9.1.0` and one Clipper implementation only in benchmark/feature-spike status. | Simplifies WASM and avoids dual geometry semantics. fileciteturn13file0turn22file0 |
| `ARCHITECTURE.md` coordinate tests | Split `numeric transform/roundtrip tolerance` from `datum-operation accuracy`. Never use ≤1 mm as Indian-1975/WGS-84 real-world acceptance. | EPSG accuracy evidence. citeturn36search0turn36search8 |
| `ARCHITECTURE.md` DXF | Mark DXF provider as unresolved pending a `dxf` 0.6.2 vs `acadrust` 0.6.6 wasm/entity/roundtrip spike. Remove any implication that JS `dxf-parser` is preferred. | Current maintenance and capability evidence. fileciteturn37file0turn41file0 |
| `ARCHITECTURE.md` editor | Record PixiJS 8.22.0 as preferred renderer with Konva 10.9.0 benchmark alternative. Keep domain/editor state independent of renderer. | Current library comparison. fileciteturn30file0turn42file0 |
| `ARCHITECTURE.md` maps | Confirm MapLibre 6.15.0 + Terra Draw 1.38.0; make tile and satellite providers runtime-configurable. Do not assume public OSM raster servers as production infrastructure. | OSMF policy and current library versions. citeturn36search10 fileciteturn43file0turn45file0 |
| `ARCHITECTURE.md` rules | Keep legal rule evaluation inside Rust core so web and CLI produce exactly the same compliance calculation. | Already consistent with `CLAUDE.md`; research makes this even more important. fileciteturn10file0 |
| `ROADMAP.md` Phase Zero | Add exit criterion: Thai numeric rule dataset citation-complete; unresolved values explicitly unverified; lawyer review list created. | Prevents legal assumptions leaking into implementation. |
| `ROADMAP.md` Phase One | Add rule-engine tests alongside geometry; include BMA 90°/two-way baseline and negative national one-way/perpendicular test. | Legal rules now known. |
| `ROADMAP.md` Phase One | Add geometry robustness corpus and compare `geo` against direct `i_overlay`/Clipper on pathological fixtures before accepting geometry ADR. | Technology risk. |
| `ROADMAP.md` Phase Three | Add mandatory DXF provider bake-off before integrating one parser permanently. | C2 remains unresolved. |
| `ROADMAP.md` Phase Four | Add Indian 1975 EPSG:24047/24048 operation selection, accuracy warnings and control-point fixtures. | C5. |
| `ROADMAP.md` Phase Five | Update host evidence: IngeCAD licence is confirmed GPL-3.0-or-later; evaluate IngeCAD first, CADCraft control bridge second, IngeTrazo third unless project priorities change. | Public host evidence. fileciteturn65file0turn62file0turn53file0 |
| `ROADMAP.md` Phase Six | Add small-instance MIP/branch-and-cut oracle and zone/orientation neighbourhood search as evaluation tools before adding a metaheuristic. | Published optimisation evidence. citeturn35academia48 |
| `docs/adr/0004-cad-plugin-targets.md` | Update IngeCAD licence and replace stale plugin-mechanism assumptions with current documented mechanisms. Keep final order a Phase Five decision. | Existing ADR is now factually stale. fileciteturn9file0turn57file0turn65file0 |

One additional schema change is strongly recommended: generated output should carry the **rule provenance that produced it**. A concept layout that says `aisle_width = 6.0` but cannot say “BMA Ordinance B.E. 2544 clause 88, parking angle >60°” is not sufficiently auditable for this product.

## Proposed ADRs

The repository's ADR format is `Title / Status / Date / Context / Decision / Consequences / Alternatives considered`. fileciteturn5file0 The following drafts are intended to be copied into new ADR files after numbering against the repository.

**ADR — Default polygon engine**

**Status:** Proposed  
**Date:** 2026-10-24

**Context**

Stallwise requires polygon difference/intersection, buffering/offset-like operations, containment and robust handling of holes in one Rust core that must compile both natively and to WebAssembly. Current architecture lists `geo`, `geo-clipper` and Clipper bindings as candidates. fileciteturn2file0

`geo` 0.33.1 is MIT OR Apache-2.0 and currently provides the needed high-level geometry model plus Boolean and buffer operations. Its Boolean implementation already integrates `i_overlay`, reducing the need for an independent clipping abstraction. fileciteturn13file0turn14file0turn14file1

`geo-clipper` 0.9.0 and `clipper2` 0.6.0 are licence-compatible but introduce native C/C++ binding/toolchain requirements, particularly relevant for WebAssembly. fileciteturn15file0turn19file0

**Decision**

Use `geo = 0.33.1` as the sole public geometry façade in Phase One.

Do not expose a Clipper- or `i_overlay`-specific type through Stallwise domain APIs.

Maintain a benchmark harness capable of evaluating direct `i_overlay` and one Clipper implementation against the same polygon fixtures. Promote an alternative only if measured correctness/robustness requires it.

**Consequences**

The WASM build remains mostly pure Rust and the domain model has one geometry representation.

`geo` becomes an important dependency and must be pinned and upgraded deliberately.

Before changing this ADR to Accepted, pathological-polygon and WASM CI tests must pass.

**Alternatives considered**

`geo-clipper`: permissive but older/slower-maintained binding and native toolchain.

`clipper2`: strong alternative, but additional native/WASI complexity.

Direct `i_overlay`: current and pure Rust, but duplicates/lower-levels functionality already exposed through `geo`.

**ADR — Browser plan renderer**

**Status:** Proposed  
**Date:** 2026-10-24

**Context**

The editor must display and interact with thousands of generated stalls plus aisles, zones, handles, overlays and selections. PixiJS 8.22.0 and Konva 10.9.0 are both actively maintained MIT-licensed libraries. fileciteturn30file0turn42file0

**Decision**

Use PixiJS 8.22.0 as the preferred Phase Three plan renderer.

Domain state, selection, snapping, commands, undo/redo and IDs remain framework-neutral. Pixi objects are rendering projections of domain objects, not the authoritative document.

Benchmark Konva before the ADR becomes Accepted using representative 1k, 5k and 10k drawable-object scenes with selection/drag/redraw workloads. These are engineering benchmark tiers, not claims about typical Thai projects.

**Consequences**

Large-scene rendering has a GPU-oriented path.

Stallwise must implement or wrap some editing interaction logic that Konva would otherwise provide at a higher level.

Renderer replacement remains possible because persistent data never contains Pixi-specific state.

**Alternatives considered**

Konva: attractive interaction API; retain as benchmark alternative.

SVG: excellent for export/low-count DOM overlays but not preferred as the main high-count editor scene.

Immediate Canvas: lowest dependency count but transfers scene graph, hit testing and invalidation complexity into Stallwise.

**ADR — Map and drawing stack**

**Status:** Proposed  
**Date:** 2026-10-24

**Context**

Stallwise needs basemap display and polygon drawing without tying project geometry to a proprietary map provider. MapLibre GL JS 6.15.0 is BSD-3-Clause and Terra Draw 1.38.0 is MIT. fileciteturn43file0turn45file0

OSMF makes clear that the public OpenStreetMap tile service is capacity-limited, best-effort, attribution-bound and unsuitable for bulk/offline use. citeturn36search10

**Decision**

Use MapLibre GL JS for map rendering and Terra Draw for browser map geometry interaction.

Tile/style/imagery providers are configuration, not architecture. No specific hosted satellite service is a required Stallwise dependency.

A deployment may use an appropriately licensed hosted provider, OpenFreeMap within its terms, or self-hosted OSM-derived vector tiles. citeturn37search0

**Consequences**

The core product remains provider-neutral.

Attribution must be rendered according to the selected data/provider terms.

Production deployments cannot assume free unlimited access to `tile.openstreetmap.org`.

Satellite imagery cannot be enabled by default until a provider-specific terms review is complete.

**Alternatives considered**

Direct OSM public raster as default: rejected for production because of service-policy constraints.

Provider-specific map SDK: rejected as the architectural core because it would couple Stallwise to one commercial service.

**ADR — Legacy Thai CRS accuracy model**

**Status:** Proposed  
**Date:** 2026-10-24

**Context**

Older Thai CAD may use Indian 1975 / UTM zones 47N and 48N, EPSG:24047 and EPSG:24048. Multiple EPSG Indian-1975→WGS-84 operations exist with metre-class stated accuracy. citeturn36search0turn36search2turn36search5

The existing architecture's millimetre-level test wording risks conflating numerical implementation precision with datum accuracy. fileciteturn2file0

**Decision**

Support EPSG:24047 and EPSG:24048 as explicit source CRS options.

Persist the chosen datum operation/provenance and its published accuracy.

Use millimetre-level tests only for internal local-coordinate numerical invariants and reversible same-operation round trips.

Never describe an Indian-1975→WGS-84 result as millimetre accurate unless the project provides independent survey control establishing that accuracy.

**Consequences**

The UI needs a legacy-datum warning and operation metadata.

Two drawings with the same EPSG source CRS can legitimately have different georeferencing provenance if a local survey/control transform was used.

The CRS test suite must include known control coordinates and tolerances appropriate to the selected EPSG operation.

**Alternatives considered**

One hard-coded `towgs84` definition: rejected because EPSG publishes multiple operations with different areas/accuracies.

Treat Indian 1975 as unsupported: rejected because legacy Thai CAD is an explicit product requirement.

**DXF ADR intentionally deferred.** Current evidence is sufficient to shortlist `dxf` 0.6.2 and `acadrust` 0.6.6 but not sufficient to select one without real Stallwise DXF fixtures. Creating an “Accepted” ADR now would convert uncertainty into architecture without evidence. fileciteturn37file0turn41file0

## Phase one recommendation

Phase One should remain deliberately narrower than the eventual optimiser described in `SPEC.md`: perpendicular stalls, two-way aisles, deterministic output, native Rust first, with the rule engine and geometry primitives designed so later angle types do not require rewriting the model. This matches the existing roadmap's intent. fileciteturn3file0

**Recommended baseline algorithm**

Represent all computation in a local planar metre coordinate system as already required by `IN-R1`, subtracting obstacles and mandatory keep-outs before generation. fileciteturn1file0

For a candidate orientation `θ`, rotate the usable polygon into solver coordinates. Phase One can search `θ ∈ [0°,90°)` because 90° stalls have quadrant symmetry. A simple 1° sweep, already anticipated by the specification, is acceptable as a first implementation; additionally test orientations derived from dominant site-edge bearings so an obvious boundary-aligned solution cannot be missed because of a fixed angular grid. fileciteturn1file0

For 90° two-way parking, define the double-loaded module depth as:

```text
module_depth = stall_depth + aisle_width + stall_depth
```

and the row pitch as the regulatory/project stall width.

Do **not** test only one arbitrary module origin. Enumerate deterministic offsets. A better baseline than fixed centimetre stepping is to derive candidate row offsets from projected polygon/obstacle vertex coordinates modulo `module_depth`, and candidate along-row offsets from projected event coordinates modulo `stall_width`. Between such boundary events the combinatorial set of whole rectangles normally does not change; this keeps the search deterministic without creating a huge resolution-dependent grid.

Generate only **complete stall rectangles**. Do not count clipped stall fragments. Every stall must be inside the usable polygon to `GEN-R1`'s internal tolerance and must not intersect an obstacle, fire keep-out, accessibility clear strip belonging elsewhere, or another stall. fileciteturn1file0

Construct aisles as first-class polygons/segments rather than implied whitespace. Build a circulation graph from aisle components and declared entry/exit connectors. Reject any stall whose serving aisle cannot reach an entry/exit and reject disconnected generated modules under `GEN-R2`. This follows both No. 7's circulation concept and the connectivity constraint used in current parking-optimisation research. citeturn28view0turn35academia48

Score candidates lexicographically in Phase One:

```text
maximize compliant stall count
then minimize unreachable/discarded module count
then minimize required aisle length or fragmentation
then deterministic orientation/offset tie-break
```

Do not hide weighted “magic” coefficients in the first solver. Lexicographic scoring makes fixture failures explainable.

Keep accessibility **out of the optimisation objective initially**, but put the rule calculation in Phase One. Once ordinary geometry is solved, a later deterministic allocation pass can rank eligible stalls by accessible-route distance and allocate the required number, with 1.00 m side clear zones checked geometrically. citeturn23view1turn23view2

**Recommended test fixtures**

The fixture corpus should contain analytically simple and pathological geometry, not just pretty demo sites:

| Fixture class | Purpose | Expected assertion |
|---|---|---|
| Exact rectangular module multiples | Establish a known optimum | Exact expected stall count |
| Rectangle with sub-stall remainder | Boundary/off-by-one behaviour | Exact count; no clipped stall |
| Same rectangle rotated | Rotation invariance | Same count after inverse transform |
| L-shaped lot | Competing strips | Deterministic count and no out-of-bound stalls |
| Trapezoid | Non-orthogonal boundary | Whole-stall containment |
| Rectangle with rectangular hole | Obstacle subtraction | No intersection; remaining rows valid |
| Several small holes | Fragmentation | No duplicates/overlaps |
| Narrow throat joining two lobes | Connectivity | Unreachable lobe rejected unless aisle connects |
| Almost-collinear/sliver polygon | Boolean robustness | No panic; valid or explicit error |
| Large UTM-like coordinates shifted to local origin | Precision | Same geometry as translated local fixture within 1 mm internal tolerance |
| Boundary-touching stall | Predicate semantics | Stable inclusive/exclusive result |
| BMA 90° fixture | Rule engine integration | Aisle ≥6.00 m under cl. 88 citeturn27view0 |
| National perpendicular + one-way configuration | Negative regulatory test | Validation error under No. 41 interpretation citeturn24view1 |
| Accessible counts at 25/26, 50/51, 100/101, 150/151, 200/201/251 | Boundary conditions | Exact count formula from current accessibility regulation citeturn23view1 |
| National 30° rule lookup | Legal-gap test | `unverified_rule`, not invented dimension |
| BMA 30° rule lookup | Jurisdiction contrast | 5.50 m aisle category and BMA stall category as sourced citeturn27view0 |

**Phase One pass criteria**

A build should not be considered Phase One complete merely because it draws plausible parking. Recommended acceptance gates are:

| Area | Pass criterion |
|---|---|
| Geometry safety | Zero stall–stall overlaps and every stall within its parkable region under the 1 mm **internal planar** tolerance required by `GEN-R1`. fileciteturn1file0 |
| Obstacles | Zero stall or required-aisle intersections with configured hard keep-outs. |
| Connectivity | Every retained stall reaches an entry/exit through the circulation graph. |
| Determinism | Identical normalized input + rules + seed/config produces identical ordered semantic output across repeated native runs. |
| Rule traceability | Every regulatory validation/warning identifies ruleset version and source clause. |
| Rectangle quality | Exact optimum on all analytically constructed rectangular fixtures. |
| Irregular-site regression | Golden counts/geometries remain stable unless deliberately re-baselined with documented reason. |
| Error handling | Invalid/self-intersecting/degenerate inputs return structured errors or repair warnings, never panic. |
| Robustness | Property-based transforms/translations do not change topology or count beyond explicitly allowed tolerance. |
| Performance | Existing roadmap target of **<1 second native for Phase One fixture sites** remains the initial gate. fileciteturn3file0 |
| Dependency consistency | Same geometry/rules tests run through the core API that will later be exposed by both WASM and CLI; no browser-only rule logic. |
| Licence gate | Dependency manifest contains no GPL-2.0-only component and records licence/version for every shipped dependency, consistent with `CLAUDE.md`. fileciteturn10file0 |

The existing `<5 s` `NFR-2` target can remain a later interactive target, but its “typical site” description should be downgraded to a benchmark assumption until Thai production-site data exist. fileciteturn1file0

For Phase Six, measure improvement against this deterministic solver rather than replacing it blindly. An appropriate experimental sequence is:

```text
baseline strip solver
→ multi-zone decomposition
→ independent zone orientations
→ local row/module shifts
→ angle changes
→ circulation-aware neighbourhood search
→ MIP oracle on small 90° cases
→ only then evaluate a metaheuristic
```

The published branch-and-cut work gives Stallwise an especially useful comparison point for small perpendicular cases because it jointly models capacity and connectivity rather than optimising stall count alone. citeturn35academia48

## Open questions

| Open question | Why unresolved / impact | Owner |
|---|---|---|
| Does the national No. 41 wording intentionally leave exactly 30° outside the `<30°` and `>30°` oblique categories, and how should a 30° layout legally be treated? | The text reviewed should not be “fixed” by software inference. Blocks verified national 30° profile. citeturn24view1 | **Thai building-control lawyer / competent authority** |
| Is the No. 41 perpendicular-parking one-way prohibition interpreted exactly as a prohibition on serving 90° stalls with a one-way aisle, including modern practice? | Materially affects generator combinations. citeturn24view1 | **Thai building-control lawyer** |
| Have later BMA amendments modified any of Ordinance B.E. 2544 clauses 83–100 used here? | Clauses were sourced, but a complete consolidated amendment audit remains outstanding. | **Thai building-control lawyer / BMA building-control officer** |
| Can adjacent accessible bays legally share a 1.00 m clear strip, or must each bay have its own strip? | Current clause requires a side clear strip but the sharing interpretation was not established in this pass. citeturn23view2 | **Thai accessibility/building-control lawyer** |
| When exactly may portions of a No. 33 fire-access open space coexist with marked parking rather than being treated as a complete no-parking keep-out? | Conservative generator behaviour is easy; a less conservative interpretation needs authority confirmation. citeturn24view3 | **Fire/building-control specialist** |
| Are there municipality-specific or project-class motorcycle parking dimensions/ratios that should enter the initial Thai library? | No general value was verified. | **Thai legal researcher + user/domain engineer** |
| Has any Thai law enacted by the production release date introduced mandatory EV-space ratios or EV-ready parking quotas? | Current technical electrical standards are not the same as a parking quota; laws can change. citeturn20search0turn22search2 | **Thai legal/electrical engineer; re-check before release** |
| Which Indian 1975 datum operation do the user's real legacy drawings actually assume? | EPSG provides multiple operations with different accuracies; selecting the wrong one may shift geometry by metres. citeturn36search0turn36search8 | **User/survey engineer** |
| Should Stallwise support locally fitted similarity/Helmert transformations in addition to EPSG datum operations when survey control points are available? | Likely valuable for old CAD, but workflow and responsibility must be explicit. | **User + geospatial engineer** |
| Which DXF library passes the real Stallwise fixture set under WASM? | `dxf` and `acadrust` are both credible; evidence is insufficient to choose without testing. fileciteturn37file0turn41file0 | **Stallwise engineer, Phase Three** |
| Is DWG a future Stallwise-browser requirement, or only a CAD-host concern? | Determines whether acadrust's broader DWG capability is strategically important enough to accept MPL and additional complexity. | **User/product owner** |
| Which satellite/aerial provider may be used by the hosted product, in which markets and under what caching/export terms? | No universal compatible default was verified. | **Product owner + legal/procurement** |
| May map imagery appear in exported PDFs, or only as an interactive tracing aid? | Provider display/export rights can differ. | **Product owner + legal** |
| What are actual Thai project-size distributions: hectares, vertices, holes, obstacles and expected stall count? | `NFR-2` currently rests on an assumption rather than measured market data. fileciteturn1file0 | **User/product owner; collect anonymised project metadata** |
| What constitutes the minimum authority-facing parking schedule for the user's real Bangkok workflow? | Public BMA checklists establish formal permit review but do not establish a universal standalone parking-study template. citeturn37search5turn37search6 | **User / Thai architect or permit consultant** |
| Does the first CAD integration need an embedded UI or is “select boundary → invoke Stallwise → insert result” sufficient? | Determines whether IngeCAD's rich plugin API or CADCraft's external control API has greater practical value. | **User/product owner** |
| Should Phase Five target order become IngeCAD → CADCraft → IngeTrazo? | Current evidence favours this order, but actual users and host adoption should decide the final priority. fileciteturn57file0turn62file0turn53file0 | **User/product owner at Phase Five gate** |
| What compatibility promise should Stallwise make for host adapters against IngeTrazo's unstable 0.x extension API and the still-young IngeCAD/CADCraft APIs? | Adapter maintenance cost may dominate host-selection value. fileciteturn53file0turn58file0 | **Stallwise engineer + host maintainers** |
| Should the 325-site optimisation corpus from the published branch-and-cut study be incorporated into benchmarking, and under what dataset licence? | Published computational results are verified; redistribution/public availability of the geometry corpus was not verified. citeturn35academia48 | **Research/engineering** |

The principal blocker to calling `RS-2` production-ready is therefore **not geometry-engine implementation**. It is final legal consolidation: exact-30° interpretation, BMA amendment status, accessible-clear-zone interpretation, local motorcycle/EV requirements, and authority confirmation of the intended jurisdiction hierarchy. Until those items are closed, v0.2 should contain the verified figures above while preserving an explicit `unverified` state for everything else.