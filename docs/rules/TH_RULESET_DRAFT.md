# Thai Rule Sets — Draft Dataset

- **Document status:** Draft for SPEC v0.2 (Phase 0). **Not legal advice. Not yet legally reviewed.**
- **Profiles:** `TH_NATIONAL` (Ministerial Regulations under the Building Control Act) and `TH_BMA` (Bangkok Metropolitan Administration Building Control Ordinance B.E. 2544). They are separate profiles; one must never silently fill gaps in the other (SPEC RS-4).
- **Evidence record:** [`docs/research/2026-10-24-phase0-deep-research.md`](../research/2026-10-24-phase0-deep-research.md)

## Verification status vocabulary

Every value carries exactly one status (SPEC RS-4):

| Status | Meaning | May the engine use it? |
|---|---|---|
| `unverified` | No source established, or source wording is ambiguous | No — the rule returns `unverified_rule`; the user must supply a project value |
| `cited` | A specific regulation and clause is named by the research pass, but the primary text has not yet been linked in this repo | Yes, labelled **Draft — verify** in UI and outputs |
| `cross-checked` | `cited`, and independently confirmed against a second source (government-hosted text or peer-reviewed paper quoting the text) | Yes, labelled **Draft — verify** |
| `legally-reviewed` | Confirmed current by a Thai building-control lawyer or competent authority, with date and reviewer recorded | Yes, without draft label |

No value is `legally-reviewed` yet.

## 1. Stall geometry

| Key | Profile | Value | Source (regulation, clause) | Status |
|---|---|---|---|---|
| `stall.parallel_or_lt30.width` | TH_NATIONAL | ≥ 2.40 m | Ministerial Regulation No. 41 B.E. 2537, cl. 2(1) | `cited` |
| `stall.parallel_or_lt30.length` | TH_NATIONAL | ≥ 6.00 m | No. 41 B.E. 2537, cl. 2(1) | `cited` |
| `stall.perpendicular.width` | TH_NATIONAL | ≥ 2.40 m | No. 41 B.E. 2537, cl. 2(2) | `cross-checked` ¹ |
| `stall.perpendicular.length` | TH_NATIONAL | ≥ 5.00 m | No. 41 B.E. 2537, cl. 2(2) | `cross-checked` ¹ |
| `stall.oblique_gt30.width` | TH_NATIONAL | ≥ 2.40 m | No. 41 B.E. 2537, cl. 2(3) | `cited` |
| `stall.oblique_gt30.length` | TH_NATIONAL | ≥ 5.50 m | No. 41 B.E. 2537, cl. 2(3) | `cited` |
| `stall.exactly_30` | TH_NATIONAL | — | No. 41 wording distinguishes `< 30°` and `> 30°` only | `unverified` |
| `stall.perpendicular` | TH_BMA | ≥ 2.40 × 5.00 m | BMA Ordinance B.E. 2544, cl. 86 | `cited` |
| `stall.parallel_or_lt30` | TH_BMA | ≥ 2.40 × 6.00 m | BMA Ordinance B.E. 2544, cl. 86 | `cited` |
| `stall.oblique_ge30` | TH_BMA | ≥ 2.40 × 5.50 m | BMA Ordinance B.E. 2544, cl. 86 | `cited` |

¹ Confirmed by a peer-reviewed Thai paper quoting No. 41 directly ("กว้างไม่น้อยกว่า 2.40 เมตร และความยาวไม่น้อยกว่า 5.00 เมตร"), which also notes the superseded No. 7 figure of 2.50 × 6.00 m. The old 2.50 × 6.00 m figure MUST NOT be used as a current national rule.

## 2. Circulation and access

| Key | Profile | Value | Source | Status |
|---|---|---|---|---|
| `aisle.width_by_angle` | TH_NATIONAL | — | No national numeric table identified | `unverified` |
| `aisle.perpendicular.one_way_allowed` | TH_NATIONAL | `false` | No. 41 B.E. 2537, cl. 2(2) — "จะต้องไม่จัดให้มีทางเข้าออกของรถเป็นทางเดินรถทางเดียว" | `cross-checked` ², interpretation pending legal review |
| `aisle.width.lt30` | TH_BMA | ≥ 3.50 m | BMA Ordinance B.E. 2544, cl. 88 | `cited` |
| `aisle.width.30_to_60` | TH_BMA | ≥ 5.50 m | BMA Ordinance B.E. 2544, cl. 88 | `cited` |
| `aisle.width.gt60` | TH_BMA | ≥ 6.00 m | BMA Ordinance B.E. 2544, cl. 88 | `cited` |
| `entry_exit.width.general` | TH_NATIONAL | ≥ 6.00 m | Ministerial Regulation No. 7 B.E. 2517, cl. 8 | `cited` |
| `entry_exit.width.separate_one_way` | TH_NATIONAL | ≥ 3.50 m | No. 7 B.E. 2517, cl. 8 | `cited` |
| `entry_exit.width.general` | TH_BMA | ≥ 6.00 m | BMA Ordinance B.E. 2544, cl. 88 | `cited` |
| `entry_exit.width.separate_one_way` | TH_BMA | ≥ 3.50 m | BMA Ordinance B.E. 2544, cl. 88 | `cited` |
| `entry_exit.distance_from_curve_start` | TH_BMA | ≥ 20 m (centreline) | BMA Ordinance B.E. 2544, cl. 89 | `cited` |
| `entry_exit.distance_from_bridge_ramp` | TH_BMA | ≥ 50 m, subject to clause exceptions | BMA Ordinance B.E. 2544, cl. 91 | `cited` |
| `access_road.width.ge15_spaces` | TH_BMA | ≥ 6.00 m | BMA Ordinance B.E. 2544, cl. 90 | `cited` |
| `clear_height` | TH_NATIONAL | ≥ 2.10 m | No. 41 B.E. 2537, cl. 4 | `cited` |
| `offsite_parking.max_distance` | TH_NATIONAL | ≤ 200 m | No. 7 B.E. 2517, cl. 6 | `cited` |
| `turning_radius.surface_lot` | TH_NATIONAL | — | No. 7 cl. 7 requires adequate turning; no number | `unverified` |
| `ramp.slope.straight` | TH_BMA | ≤ 15 % | BMA Ordinance B.E. 2544, cl. 99 | `cited` |
| `ramp.slope.curved` | TH_BMA | ≤ 12 % | BMA Ordinance B.E. 2544, cl. 99 | `cited` |
| `ramp.curved.inner_radius` | TH_BMA | ≥ 6.00 m — curved ramps only, **not** a general turning radius | BMA Ordinance B.E. 2544, cl. 99 | `cited` |
| `parking_surface.slope` | TH_BMA | ≤ 5 % | BMA Ordinance B.E. 2544, cl. 100 | `cited` |

² The quoted phrase is confirmed by the same peer-reviewed paper; how it maps to aisle direction in the generator still needs legal interpretation (OQ-02).

## 3. Accessible parking (both profiles)

Source: Ministerial Regulation on facilities for persons with disabilities and the elderly, as amended by **Ministerial Regulation (No. 2) B.E. 2564** (replacing original cl. 12–14).

| Key | Value | Status |
|---|---|---|
| `accessible.count` — total ≤ 25 | ≥ 1 | `cross-checked` ³ |
| 26–50 | ≥ 2 | `cross-checked` ³ |
| 51–75 | ≥ 3 | `cross-checked` ³ |
| 76–100 | ≥ 4 | `cross-checked` ³ |
| 101–150 | ≥ 5 | `cross-checked` ³ |
| 151–200 | ≥ 6 | `cross-checked` ³ |
| > 200 | +1 per further 100; remainder > 50 counts as 100 | `cross-checked` ³ |
| `accessible.clear_strip.width` | ≥ 1.00 m, full stall length, smooth and level | `cross-checked` ³ |
| `accessible.stall_geometry` | Refers to No. 41 B.E. 2537 cl. 2–3 (base stall) — modelled as base stall + side clear strip, **not** a widened stall | `cited` |
| `accessible.location` | As close as practicable to an accessible entrance, on a smooth level route | `cross-checked` ³ |
| `accessible.clear_strip.shared` | Whether adjacent bays may share one strip | `unverified` (OQ-04) |

³ Confirmed against a government-hosted handbook of the B.E. 2564 amendment.

## 4. Fire access (conditional overlay)

| Key | Value | Applies when | Source | Status |
|---|---|---|---|---|
| `fire_access.corridor.width` | ≥ 6.00 m, uncovered, around the building | High-rise or extra-large building as defined by the regulation | Ministerial Regulation No. 33 B.E. 2535, cl. 3 | `cited` |

Not applied to ordinary surface lots. Whether parking may overlap any part of the corridor is `unverified` (OQ-05); the generator treats it as a full keep-out.

## 5. Motorcycle and EV

| Key | Status |
|---|---|
| Motorcycle stall dimensions and ratios | `unverified` — project policy only |
| EV parking quota | `unverified` — project policy only |
| EV stall geometry | `unverified` — project policy only |

## 6. Minimum parking supply

Supply formulas depend on **applicability predicates** (No. 7 cl. 2; BMA cl. 83), mixed-use and large-building "greater of" rules, and rounding (No. 7 cl. 4; BMA cl. 85). These predicates must be encoded before any supply value is used. All supply values below are `cited`, pending primary-text linking.

### TH_NATIONAL — Bangkok column / elsewhere column (No. 7 B.E. 2517 cl. 3, as amended incl. No. 64 B.E. 2555)

| Use | Bangkok | Elsewhere |
|---|---|---|
| Theatre (general) | 1 / 20 seats | 1 / 40 seats |
| Theatre (specified central areas) | 1 / 10 seats — district list to be encoded from source | — |
| Hotel lobby | 1 / 10 m² | 1 / 30 m² |
| Hotel commercial area | 1 / 20 m² | 1 / 40 m² |
| Covered condominium / family units | 1 / unit | 1 / 2 units |
| Restaurant table area | 1 / 15 m² (first 750 m²), 1 / 30 m² beyond | 1 / 40 m² |
| Department store | 1 / 20 m² | 1 / 40 m² |
| Office | 1 / 60 m² | 1 / 120 m² |
| Hall | 1 / 10 m² | 1 / 30 m² |
| Large building baseline | 1 / 120 m² (greater-of rule) | 1 / 240 m² (greater-of rule) |

### TH_BMA (BMA Ordinance B.E. 2544 cl. 84–85)

| Use | Requirement |
|---|---|
| Theatre | 1 / 10 seats |
| Hotel | 10 for first 30 rooms; +1 / 5 rooms for rooms 31–100; +1 / 10 rooms beyond 100 |
| Residential / condominium unit (cl. 83 scope) | 1 / unit |
| Restaurant | 10 for first 150 m² table area; +1 / 20 m² beyond |
| Department store | 1 / 20 m² |
| Office | 1 / 60 m² |
| Market | 1 / 120 m² |
| Factory | 1 / 240 m² |
| Warehouse | 1 / 240 m² |
| Storage | 1 / 120 m² |
| Hospital | 1 / 120 m² |
| Educational building | 1 / 240 m² |
| Service establishment | 1 / 60 m² |
| Exhibition | 1 / 20 m² |
| Hall | 1 / 10 m² |
| Commercial | 1 / 60 m² |
| Large building | greater of 1 / 120 m² and use-by-use sum, subject to exceptions |

## 7. To promote values from `cited`

1. Obtain the primary text (Royal Gazette / BMA publication) for No. 7, No. 41, No. 64, No. 33, BMA B.E. 2544 and the accessibility regulation with its B.E. 2564 amendment; store links (not copies, unless licence permits) in this file.
2. Check BMA B.E. 2544 for later amendments affecting cl. 83–100 (OQ-03).
3. Record reviewer, date and scope when any value becomes `legally-reviewed`.
