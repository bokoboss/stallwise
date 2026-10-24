> **Archive note (added on import, 2026-10-24).** Second, focused Phase 0 research report (OQ-01…08, 11, 12, 16), kept verbatim as the evidence record. Remaining `cite…` markers do not resolve; the URLs in the tables are the usable references.
> Independently checked on import: the `transnetlab/parking-lot-design` repository has no licence file, lists 325 lot IDs, and its `config.py` expects a `parking_lots_data.csv` that is not in the repository. The Royal Gazette and BMA PDF links could not be opened from the import environment and still need a human check (see OQ-08).

# Stallwise Focused Deep Research: Thai Parking Rules, Imagery Rights, and Benchmark Corpus

**Research date:** 24 October 2026  
**Repository:** <https://github.com/bokoboss/stallwise>  
**Repository inputs reviewed first, as requested:**

- <https://github.com/bokoboss/stallwise/blob/main/docs/OPEN_QUESTIONS.md>
- <https://github.com/bokoboss/stallwise/blob/main/docs/rules/TH_RULESET_DRAFT.md>

This report is limited to **OQ-08, OQ-03, OQ-06, OQ-07, OQ-11, OQ-12 and OQ-16**, plus a search for **published interpretations only** for **OQ-01, OQ-02, OQ-04 and OQ-05**.

Two evidence levels are deliberately separated throughout:

- **Source fact** means the proposition can be tied to an identified statute, official agency publication, provider terms, paper, or public repository.
- **Recommendation** means a proposed Stallwise product/engineering treatment and is not represented as Thai law.

For statutory wording, the tables below give clause-level pinpoints and short exact Thai extracts where I could verify the wording. I do **not** silently reconstruct missing Thai text. Where the exact Gazette header or exact wording could not be re-opened and independently checked, it is marked **unverified** rather than guessed. The complete original provisions should be read at the full Royal Gazette URLs supplied below.

## Original legal sources

### Primary-source table

| Instrument | Royal Gazette volume / issue / page / publication date | Verification | Full primary URL |
|---|---|---|---|
| **Ministerial Regulation No. 7 B.E. 2517** | Vol. **91**, Issue **86**, p. **220**, **21 May B.E. 2517 (1974)** | **Verified from Gazette header** | <https://ratchakitcha.soc.go.th/documents/1304859.pdf> |
| **Ministerial Regulation No. 41 B.E. 2537** | Vol. **111**, Issue **37 ก**, p. **25**, **31 August B.E. 2537 (1994)** | **Verified from Gazette header** | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> |
| **Ministerial Regulation No. 64 B.E. 2555** | Vol. **129**, Issue **112 ก**, p. **20**, **30 November B.E. 2555 (2012)** | **Verified from Gazette header** | <https://ratchakitcha.soc.go.th/documents/1952330.pdf> |
| **Ministerial Regulation No. 33 B.E. 2535** | Legacy Gazette file encodes B.E. 2535 / issue **011** / p. **6**. The volume and publication date were **not independently re-verified from the Gazette header in this research pass**. | **Partly verified; metadata remainder unverified** | <https://www.ratchakitcha.soc.go.th/DATA/PDF/2535/A/011/6.PDF> |
| **Bangkok Metropolitan Administration Ordinance on Building Control B.E. 2544** | Legacy Gazette file encodes B.E. 2544 / special issue **075** / p. **18**. The volume and publication date were **not independently re-verified from the Gazette header in this research pass**. | **Partly verified; metadata remainder unverified** | <https://www.ratchakitcha.soc.go.th/DATA/PDF/2544/E/075/18.PDF> |
| **Ministerial Regulation prescribing facilities in buildings for persons with disabilities or impairments and elderly persons B.E. 2548** | Vol. **122**, Issue **52 ก**, p. **4**, **2 July B.E. 2548 (2005)** | **Verified** | <https://ratchakitcha.soc.go.th/documents/166141.pdf> |
| **Same regulation, No. 2 B.E. 2564** | Vol. **138**, Issue **16 ก**, p. **19**, **4 March B.E. 2564 (2021)** | **Verified from Gazette header** | <https://ratchakitcha.soc.go.th/documents/17159462.pdf> |

The Gazette pages confirm the first three publication records above and the 2564 accessibility amendment. citeturn58view0turn58view1turn58view2turn58view3

For working with the Bangkok text, BMA also publishes an official readable copy here:

<https://webportal.bangkok.go.th/public/user_files_editor/75/basic_info/Laws/03_Yota/Legis_Building_2544.pdf>

The BMA copy contains the parking provisions in clauses 83 onward, including the parking-supply and dimensional sections used by Stallwise. citeturn34view0turn58view4

### Relevant provisions and short exact extracts

The following is the legally material structure found in the primary texts. Where a quotation appears in quotation marks it is a short **verbatim Thai extract**; the rest is a clause-level paraphrase and should not be treated as quoted statutory language.

| Instrument / clause | What the provision establishes | Short exact Thai extract where independently verified |
|---|---|---|
| No. 7, cl. 3 | Minimum car-parking supply by use, with separate Bangkok and other-area calculations; later affected by No. 64. | See primary PDF; long clause not reproduced here. |
| No. 7, cl. 4 | Mixed-use parking calculation / aggregation. | See primary PDF. |
| No. 7, cl. 6 | Permits required parking to be provided outside the building/site subject to a route-distance limit of 200 m. | See primary PDF. |
| No. 7, cl. 7 | Requires adequate vehicle turning; provides a one-way entrance-to-exit situation in which a turnaround need not be provided. | See primary PDF. |
| No. 7, cl. 8 | General vehicle entrance/exit width is 6.00 m; separately arranged one-way entrance and exit may each be 3.50 m. | See primary PDF. |
| No. 41, cl. 1 | Repeals the old No. 7 clause 5 parking-space dimensions. | See primary PDF. |
| No. 41, cl. 2(1) | Parallel or angle below 30°: 2.40 m × 6.00 m minimum. | The statutory category expressly uses **less than 30°**. |
| No. 41, cl. 2(2) | Perpendicular: 2.40 m × 5.00 m minimum, followed by the disputed one-way language relevant to OQ-02. | **“จะต้องไม่จัดให้มีทางเข้าออกของรถเป็นทางเดินรถทางเดียว”** |
| No. 41, cl. 2(3) | Other oblique parking at an angle above 30°: 2.40 m × 5.50 m minimum. | The statutory category expressly uses **more than 30°**. |
| No. 41, cl. 3 | Parking-space marking and circulation/direct connection to entrance/exit and turning facilities. | See primary PDF. |
| No. 41, cl. 4 | Parking, circulation and vehicle ramp clear height at least 2.10 m. | See primary PDF. |
| No. 64, cls. 1–7 | Amends the No. 7 applicability and parking-supply provisions, particularly hotel and hall calculations; it does **not** replace the No. 41 stall dimensions. | See primary PDF. |
| No. 33, cl. 3 | For high-rise or extra-large buildings, requires uncovered road/open space at least 6.00 m around the building and convenient fire-engine access. | **“ถนนหรือที่ว่างปราศจากสิ่งปกคลุมโดยรอบอาคารกว้างไม่น้อยกว่า ๖.๐๐ เมตร”** |
| BMA 2544, cls. 83–85 | Applicability, use-specific minimum parking supply, mixed-use/large-building calculation and rounding. | See official BMA/Gazette PDF. |
| BMA 2544, cl. 86 | 2.40 × 5.00 m perpendicular; 2.40 × 6.00 m parallel/<30°; 2.40 × 5.50 m at 30° or more. | See official BMA/Gazette PDF. |
| BMA 2544, cl. 88 | Entrance/exit widths and aisle widths of 3.50 / 5.50 / 6.00 m according to parking-angle bands. | See official BMA/Gazette PDF. |
| BMA 2544, cls. 89–91 | Public-road interface constraints, including the 20 m intersection/curve rule, ≥15-space access-road provision, and bridge-ramp separation. | See official BMA/Gazette PDF. |
| BMA 2544, cl. 99 | Straight-ramp maximum 15%; curved-ramp maximum 12%; curved-ramp inner radius at least 6.00 m. | See official BMA/Gazette PDF. |
| BMA 2544, cl. 100 | Parking-area gradient maximum 5%. | See official BMA/Gazette PDF. |
| Accessibility B.E. 2548, former cls. 12–14 | Original accessible-parking provisions. | **Superseded** by the 2564 amendment; do not encode these old clauses as the current rule. |
| Accessibility No. 2 B.E. 2564, cl. 9 replacing cl. 12 | Current stepped count of accessible parking spaces. | See primary PDF. |
| Replacement cl. 13 | Location near accessible entrance/exit, level/smooth accessible route, symbols/signage. | See primary PDF. |
| Replacement cl. 14 | Base parking-space geometry is tied to No. 41 clauses 2–3 and requires a side clear area. | **“กว้างไม่น้อยกว่า ๑.๐๐ เมตร ตลอดความยาวของที่จอดรถ”** |

No. 41's three geometric categories and 2.10 m clear height are confirmed directly by its Gazette text. citeturn58view1turn24view1 No. 64's operative amendments affect the No. 7 hotel/hall and applicability provisions rather than replacing those No. 41 dimensions. citeturn58view2turn38search2 No. 33 clause 3 establishes the 6 m uncovered fire-access condition for the relevant high-rise/extra-large building class. citeturn24view3

The 2564 accessibility amendment expressly replaced the earlier clauses 12–14. Current clause 12 contains the stepped count; clause 13 deals with location and access; clause 14 refers back to No. 41 for the vehicle-space geometry and adds the minimum 1.00 m full-length side clear area. citeturn29view0turn30view0turn30view1turn30view2

## Draft rule verification

I checked the entries whose status in `TH_RULESET_DRAFT.md` is specifically **`cited`**. I found **no numerical contradiction** in the cited values that could be checked against the primary provisions. There are, however, several **scope/semantic corrections** that should be made before treating the data model as a literal representation of the statute:

1. `offsite_parking.max_distance = 200 m` must preserve the regulation's route-to-building concept; it should not silently mean a 200 m Euclidean radius.
2. `access_road.width.ge15_spaces = 6 m` should describe the BMA **public-way connection condition**, not be mistaken for an arbitrary internal drive aisle.
3. `fire_access.corridor.width = 6 m` captures the dimension, but No. 33 also requires the relevant road/open space to be uncovered and usable conveniently by fire vehicles; “6 m buffer” alone is incomplete.
4. The English label **“Covered condominium / family units”** is not good statutory terminology. The numerical rule is supported, but the label should be rewritten around *condominium/family unit* and its applicability predicate.

### Stall and circulation values

| Key | Draft value | Statutory value | Statutory provision / text | Full URL | Result |
|---|---:|---:|---|---|---|
| `stall.parallel_or_lt30.width` | ≥2.40 m | ≥2.40 m | No. 41 cl. 2(1), parallel or <30° | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> | **MATCH** |
| `stall.parallel_or_lt30.length` | ≥6.00 m | ≥6.00 m | No. 41 cl. 2(1) | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> | **MATCH** |
| `stall.oblique_gt30.width` | ≥2.40 m | ≥2.40 m | No. 41 cl. 2(3), >30° oblique category | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> | **MATCH** |
| `stall.oblique_gt30.length` | ≥5.50 m | ≥5.50 m | No. 41 cl. 2(3) | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> | **MATCH** |
| `stall.perpendicular` — TH_BMA | ≥2.40 × 5.00 m | ≥2.40 × 5.00 m | BMA cl. 86 | <https://www.ratchakitcha.soc.go.th/DATA/PDF/2544/E/075/18.PDF> | **MATCH** |
| `stall.parallel_or_lt30` — TH_BMA | ≥2.40 × 6.00 m | ≥2.40 × 6.00 m | BMA cl. 86 | <https://www.ratchakitcha.soc.go.th/DATA/PDF/2544/E/075/18.PDF> | **MATCH** |
| `stall.oblique_ge30` — TH_BMA | ≥2.40 × 5.50 m | ≥2.40 × 5.50 m | BMA cl. 86 uses the 30°-and-above category | <https://webportal.bangkok.go.th/public/user_files_editor/75/basic_info/Laws/03_Yota/Legis_Building_2544.pdf> | **MATCH** |
| `aisle.width.lt30` — TH_BMA | ≥3.50 m | ≥3.50 m | BMA cl. 88, angle <30° | same BMA URL above | **MATCH** |
| `aisle.width.30_to_60` — TH_BMA | ≥5.50 m | ≥5.50 m | BMA cl. 88, 30° through 60° | same BMA URL above | **MATCH** |
| `aisle.width.gt60` — TH_BMA | ≥6.00 m | ≥6.00 m | BMA cl. 88, >60° | same BMA URL above | **MATCH** |
| `entry_exit.width.general` — TH_NATIONAL | ≥6.00 m | ≥6.00 m | No. 7 cl. 8 | <https://ratchakitcha.soc.go.th/documents/1304859.pdf> | **MATCH** |
| `entry_exit.width.separate_one_way` — TH_NATIONAL | ≥3.50 m | ≥3.50 m each | No. 7 cl. 8, separately arranged one-way entrance/exit | same No. 7 URL | **MATCH** |
| `entry_exit.width.general` — TH_BMA | ≥6.00 m | ≥6.00 m | BMA cl. 88 | BMA Gazette URL above | **MATCH** |
| `entry_exit.width.separate_one_way` — TH_BMA | ≥3.50 m | ≥3.50 m | BMA cl. 88 | BMA Gazette URL above | **MATCH** |
| `entry_exit.distance_from_curve_start` | ≥20 m, centreline | ≥20 m | BMA cl. 89; applies to the entrance/exit mouth relative to the public-road intersection curve/corner | BMA Gazette URL above | **MATCH** |
| `entry_exit.distance_from_bridge_ramp` | ≥50 m, exceptions | ≥50 m, with stated exceptions | BMA cl. 91 | BMA Gazette URL above | **MATCH** |
| `access_road.width.ge15_spaces` | ≥6.00 m | ≥6.00 m | BMA cl. 90 | BMA Gazette URL above | **MATCH numeric; scope clarification required** |
| `clear_height` — TH_NATIONAL | ≥2.10 m | ≥2.10 m | No. 41 cl. 4 | <https://ratchakitcha.soc.go.th/documents/1646617.pdf> | **MATCH** |
| `offsite_parking.max_distance` | ≤200 m | ≤200 m along the statutory route-to-building condition | No. 7 cl. 6 | <https://ratchakitcha.soc.go.th/documents/1304859.pdf> | **MATCH numeric; distance semantics must be explicit** |
| `ramp.slope.straight` — TH_BMA | ≤15% | ≤15% | BMA cl. 99 | BMA Gazette URL above | **MATCH** |
| `ramp.slope.curved` — TH_BMA | ≤12% | ≤12% | BMA cl. 99 | BMA Gazette URL above | **MATCH** |
| `ramp.curved.inner_radius` — TH_BMA | ≥6.00 m | ≥6.00 m | BMA cl. 99, specifically curved/spiral ramp geometry | BMA Gazette URL above | **MATCH; draft correctly says this is not a general turning radius** |
| `parking_surface.slope` — TH_BMA | ≤5% | ≤5% | BMA cl. 100 | BMA Gazette URL above | **MATCH** |

The BMA dimensional and circulation values are supported by clauses 86 and 88–100 of the official text. citeturn34view0turn27view0

### Accessible and fire-access cited values

| Key | Draft value | Statutory value | Statutory provision / text | Full URL | Result |
|---|---|---|---|---|---|
| `accessible.stall_geometry` | No. 41 base stall + ≥1.00 m side strip; not a generic widened stall | Current replacement cl. 14 refers to No. 41 cls. 2–3 and separately requires ≥1.00 m clear space for the full stall length | Accessibility No. 2 B.E. 2564, cl. 9 replacing cl. 14 | <https://ratchakitcha.soc.go.th/documents/17159462.pdf> | **MATCH** |
| `fire_access.corridor.width` | ≥6.00 m uncovered around building | ≥6.00 m road/open area, uncovered, around applicable high-rise/extra-large building, with convenient fire-engine access | No. 33 cl. 3 | <https://www.ratchakitcha.soc.go.th/DATA/PDF/2535/A/011/6.PDF> | **MATCH numeric; retain access condition** |

The accessible-space data model is therefore correct to avoid inventing a universal “3.40 m accessible stall.” The legal structure is **base parking space + separate side clear area**, subject to the regulation's applicability rules. citeturn30view1turn30view2

### National parking-supply values

These are the `cited` TH_NATIONAL values in the draft. The current result has to be read as **No. 7 as amended, including No. 64**, not as the unamended 2517 text alone. citeturn38search2turn58view2

| Key / use | Draft value | Statutory value | Provision | Full URL | Result |
|---|---|---|---|---|---|
| Theatre — Bangkok general | 1 / 20 seats | 1 / 20 seats | No. 7 cl. 3(1)(ก) | <https://ratchakitcha.soc.go.th/documents/1304859.pdf> | **MATCH** |
| Theatre — specified central Bangkok areas | 1 / 10 seats | 1 / 10 seats in the enumerated districts | No. 7 cl. 3(1)(ก) | same No. 7 URL | **MATCH; draft still needs the district predicate encoded** |
| Theatre — elsewhere | 1 / 40 seats | 1 / 40 seats | No. 7 cl. 3(2) | same No. 7 URL | **MATCH** |
| Hotel lobby — Bangkok | 1 / 10 m² | 1 / 10 m² | No. 7 cl. 3 as amended by No. 64 | <https://ratchakitcha.soc.go.th/documents/1952330.pdf> | **MATCH** |
| Hotel lobby — elsewhere | 1 / 30 m² | 1 / 30 m² | No. 64 amendment | same No. 64 URL | **MATCH** |
| Hotel commercial area — Bangkok | 1 / 20 m² | 1 / 20 m² | No. 64 amendment | same No. 64 URL | **MATCH** |
| Hotel commercial area — elsewhere | 1 / 40 m² | 1 / 40 m² | No. 64 amendment | same No. 64 URL | **MATCH** |
| Condominium/family unit — Bangkok | 1 / unit | 1 / family unit within the statutory applicability scope | No. 7 cl. 3(1) | No. 7 URL | **MATCH; rename English label** |
| Condominium/family unit — elsewhere | 1 / 2 units | 1 / 2 family units within scope | No. 7 cl. 3(2) | No. 7 URL | **MATCH** |
| Restaurant table area — Bangkok | 1 / 15 m² first 750 m²; 1 / 30 m² beyond | Same | No. 7 cl. 3(1) | No. 7 URL | **MATCH** |
| Restaurant — elsewhere | 1 / 40 m² | 1 / 40 m² | No. 7 cl. 3(2) | No. 7 URL | **MATCH** |
| Department store — Bangkok | 1 / 20 m² | 1 / 20 m² | No. 7 cl. 3(1) | No. 7 URL | **MATCH** |
| Department store — elsewhere | 1 / 40 m² | 1 / 40 m² | No. 7 cl. 3(2) | No. 7 URL | **MATCH** |
| Office — Bangkok | 1 / 60 m² | 1 / 60 m² | No. 7 cl. 3(1) | No. 7 URL | **MATCH** |
| Office — elsewhere | 1 / 120 m² | 1 / 120 m² | No. 7 cl. 3(2) | No. 7 URL | **MATCH** |
| Hall — Bangkok | 1 / 10 m² | 1 / 10 m² within the amended applicability wording | No. 64 amendment | No. 64 URL | **MATCH; applicability predicate required** |
| Hall — elsewhere | 1 / 30 m² | 1 / 30 m² | No. 64 amendment | No. 64 URL | **MATCH** |
| Large-building baseline — Bangkok | 1 / 120 m², greater-of rule | Same, subject to statutory exceptions/use aggregation | No. 7 cl. 3(1) | No. 7 URL | **MATCH; scope/greater-of logic required** |
| Large-building baseline — elsewhere | 1 / 240 m², greater-of rule | Same, subject to statutory exceptions/use aggregation | No. 7 cl. 3(2) | No. 7 URL | **MATCH; scope/greater-of logic required** |

The central-Bangkok theatre provision in the current consolidated scheme enumerates the districts that trigger the higher 1-per-10-seat requirement. The current draft correctly says that this district list still has to be encoded rather than treating all Bangkok theatres as 1/10. The rule engine therefore needs a jurisdiction/subdistrict predicate, not just `province == Bangkok`. citeturn28view0

### Bangkok parking-supply values

| Key / use | Draft value | Statutory value | Provision | Full URL | Result |
|---|---|---|---|---|---|
| Theatre | 1 / 10 seats | 1 / 10 seats | BMA cl. 84 | <https://webportal.bangkok.go.th/public/user_files_editor/75/basic_info/Laws/03_Yota/Legis_Building_2544.pdf> | **MATCH** |
| Hotel | 10 for first 30 rooms; +1 / 5 rooms for 31–100; +1 / 10 thereafter | Same tiered formula | BMA cl. 84 | same BMA URL | **MATCH** |
| Residential / condominium unit | 1 / unit | 1 / unit within cl. 83 applicability | BMA cls. 83–84 | same BMA URL | **MATCH; applicability must remain explicit** |
| Restaurant | 10 for first 150 m² table area; +1 / 20 m² beyond | Same | BMA cl. 84 | same BMA URL | **MATCH** |
| Department store | 1 / 20 m² | 1 / 20 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Office | 1 / 60 m² | 1 / 60 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Market | 1 / 120 m² | 1 / 120 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Factory | 1 / 240 m² | 1 / 240 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Warehouse | 1 / 240 m² | 1 / 240 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Storage | 1 / 120 m² | 1 / 120 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Hospital | 1 / 120 m² | 1 / 120 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Educational building | 1 / 240 m² | 1 / 240 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Service establishment | 1 / 60 m² | 1 / 60 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Exhibition | 1 / 20 m² | 1 / 20 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Hall | 1 / 10 m² | 1 / 10 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Commercial | 1 / 60 m² | 1 / 60 m² | BMA cl. 84 | same BMA URL | **MATCH** |
| Large building | greater of 1 / 120 m² or use-by-use sum, subject to exceptions | Same structure, with statutory exceptions | BMA cls. 84–85 | same BMA URL | **MATCH; encode exceptions rather than only the number** |

The official BMA text supports these use-specific formulas and the separate large-building/mixed-use treatment. citeturn58view4turn34view0

**Verification conclusion:** I found **no cited numerical value that should presently be changed to a different number**. The main corrections are to **semantics, labels, predicates and legal-confidence status**, not to the numbers themselves. This does **not** justify promotion to `legally-reviewed`; OQ-03 and the unresolved interpretation questions still matter.

## Published interpretations and Thai-law open questions

### Status summary

| OQ | Research result | Status |
|---|---|---|
| **OQ-01** — exactly 30° under No. 41 | No qualifying published official interpretation located | **Not found** |
| **OQ-02** — perpendicular stalls and one-way aisle | No qualifying published official interpretation located | **Not found** |
| **OQ-03** — later BMA amendments to cls. 83–100 | No amending provision affecting those clauses was located; absence is not sufficiently proved for legal sign-off | **Partially answered** |
| **OQ-04** — shared 1.00 m accessible strip | No qualifying published interpretation located | **Not found** |
| **OQ-05** — parking within No. 33 fire-access area | No qualifying published interpretation located | **Not found** |
| **OQ-06** — motorcycle dimensions / ratios | Motorcycle-specific parking rules exist in operational contexts, but no general TH_NATIONAL/BMA building-design dimension or ratio was established | **Partially answered** |
| **OQ-07** — mandatory EV parking ratio | No enacted nationwide/BMA building-control parking quota was established in this research pass | **Partially answered** |
| **OQ-08** — primary legal texts | Primary links obtained for all requested instruments; two legacy Gazette metadata records remain incompletely header-verified | **Partially answered** |

The interpretation search was deliberately restricted to things that could qualify under the user's rule: published circulars, rulings, agency guidance/manuals, or similarly attributable authority material. Search venues included the Royal Gazette, Department of Public Works and Town & Country Planning, Bangkok Metropolitan Administration, Office of the Council of State and the central legal portal:

<https://ratchakitcha.soc.go.th/>  
<https://www.dpt.go.th/>  
<https://webportal.bangkok.go.th/>  
<https://www.ocs.go.th/>  
<https://law.go.th/>

### Exact thirty-degree question

**Source facts.** Ministerial Regulation No. 41 clause 2 uses one category for parallel parking or parking at an angle **less than 30°**, and another oblique category for an angle **greater than 30°**. The primary wording therefore creates the question already recorded in Stallwise. citeturn58view1turn24view1

BMA clause 86 separately has its own treatment of 30° in the Bangkok ordinance, but that is a **separate Bangkok legal rule**; it is not evidence of an authoritative interpretation of No. 41 for the national profile. citeturn34view0

**Published interpretation result:** **Not found.** I did not locate a circular, Council-of-State ruling, DPT manual, BMA ruling, or other official published interpretation resolving **exactly 30° under No. 41**.

**Recommendation:** Keep `stall.exactly_30` **unverified in `TH_NATIONAL`**. Do not infer either `<30` or `>30` treatment from engineering convenience.

### One-way aisle question

**Source fact.** No. 41 clause 2(2) contains the exact phrase:

> “จะต้องไม่จัดให้มีทางเข้าออกของรถเป็นทางเดินรถทางเดียว”

The regulation itself is the source of the ambiguity between a prohibition concerning the circulation serving perpendicular stalls and a narrower entrance/exit interpretation. citeturn58view1

**Published interpretation result:** **Not found.** I did not locate a qualifying published official interpretation saying that this sentence either:

- categorically forbids a one-way drive aisle serving perpendicular stalls, or
- applies only to the site/building entrance and exit.

Accordingly, neither interpretation should be promoted as a verified legal rule.

**Recommendation:** `aisle.perpendicular.one_way_allowed = false` should **not** be promoted beyond its present draft/interpretation-pending status solely from this research.

### Bangkok amendment question

**Source facts.** The BMA continues to publish the B.E. 2544 Building Control Ordinance through its official web infrastructure, and clauses 83–100 in the available official text contain the parking provisions used in the Stallwise draft:

<https://webportal.bangkok.go.th/public/user_files_editor/75/basic_info/Laws/03_Yota/Legis_Building_2544.pdf>

The Royal Gazette original is:

<https://www.ratchakitcha.soc.go.th/DATA/PDF/2544/E/075/18.PDF>

The provisions themselves were recoverable and internally consistent with the draft. citeturn34view0turn58view4

**Amendment-history result:** I did **not** locate a later BMA ordinance amending clauses 83–100 during this search. That negative search result is useful but is **not strong enough to assert conclusively that no relevant amendment exists**, particularly because a complete official consolidated amendment table was not obtained.

**Status:** **Partially answered.**

**Recommendation:** Keep `TH_BMA` at `cited`/draft legal-confidence level until a BMA building-control officer or Thai building-control lawyer performs a dated current-law consolidation check. The numerical verification above can still be retained as evidence.

### Accessible clear-strip sharing question

**Source facts.** Current replacement clause 14 requires the accessible parking geometry to follow No. 41 clauses 2–3 and adds a side clear area at least 1.00 m wide for the full parking-space length. citeturn30view2

**Published interpretation result:** **Not found.** I did not locate an official circular, published ruling or agency manual explicitly stating that **two adjacent accessible bays may share one 1.00 m strip**, nor one expressly prohibiting sharing.

The statutory wording by itself is **not being interpreted here** to answer that question, in accordance with the research instruction.

**Recommendation:** Keep `accessible.clear_strip.shared` **unverified**. A generator may conservatively allocate one strip per bay as project policy, but should not label that choice as the legal interpretation.

### Fire-access and marked-parking question

**Source fact.** No. 33 clause 3 requires the relevant high-rise or extra-large building to have an uncovered road/open area around it at least 6.00 m wide with convenient fire-engine access. citeturn24view3

Primary source:

<https://www.ratchakitcha.soc.go.th/DATA/PDF/2535/A/011/6.PDF>

**Published interpretation result:** **Not found.** I did not locate a qualifying published official interpretation specifically answering whether a marked parking bay may occupy some portion of that statutory fire-access road/open area while still satisfying clause 3.

**Recommendation:** Stallwise's current **full keep-out treatment is a conservative engineering policy**, not a verified statement that the statute expressly says “no parking anywhere within the 6 m area.” Keep that distinction in the rule metadata.

### Motorcycle parking question

**Source facts.** The national and BMA building-control parking provisions reviewed for this research did not establish a general motorcycle stall dimension or a general motorcycle-to-car / motorcycle-to-floor-area supply ratio suitable for inclusion in `TH_NATIONAL` or `TH_BMA`.

Bangkok does have a separate **BMA ordinance on regulation of vehicle parking B.E. 2564**, covering operational/designated public-parking matters and including motorcycles within its vehicle-parking context. It is not a substitute for a building-design motorcycle stall/supply rule:

<https://webportal.bangkok.go.th/public/user_files_editor/121/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3%20%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%20%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9A%E0%B8%B5%E0%B8%A2%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%AD%E0%B8%94%E0%B8%A3%E0%B8%96%20%E0%B8%9E.%E0%B8%A8.%202564.pdf>

The Gazette metadata recovered for that separate parking-management ordinance is Vol. 138, Special Issue 282 ง, published 17 November 2564. It concerns the regulation of parking, rather than supplying a general building-control motorcycle geometry rule.

A separate ministerial regulation concerning local parking fees also addresses motorcycle parking as an operational category, not building geometry:

<https://ratchakitcha.soc.go.th/documents/17162066.pdf>

**Result:** No authoritative general building-design motorcycle dimension or mandatory ratio suitable for the Stallwise Thai profiles was established.

**Status:** **Partially answered**, rather than “none exists,” because municipality-specific, transport-facility, EIA/project-class or permit-authority requirements may exist outside the general building-control provisions searched here.

**Recommendation:** Leave motorcycle geometry and supply as `project_policy` / `unverified_rule`. Architect the schema so a later `authority_overlay` or project-class rule can provide motorcycle requirements without modifying the national car-parking model.

### EV parking-ratio question

**Source facts.** Searches of the current official legal sources did not establish an enacted nationwide or Bangkok building-control rule requiring a general percentage/number of parking bays to be EV spaces as of **24 October 2026**.

Thai legal and policy material does regulate or promote EV charging infrastructure. For example, a Board of Investment announcement addresses EV charging-station activity, but that is not a building-control parking-space quota:

<https://ratchakitcha.soc.go.th/documents/17218253.pdf>

The existence of EV charging standards, electrical requirements, investment incentives or charging-station rules should not be transformed into a parking **quota** unless the instrument actually imposes one. Earlier Stallwise research similarly did not establish such a building-control quota. citeturn20search0turn22search2

**Result:** **No enacted general EV parking ratio was found in this research pass.** This is a negative-search conclusion, not a categorical legal opinion that no project-specific requirement can exist anywhere in Thailand.

**Status:** **Partially answered.**

**Recommendation:** Keep:

```text
EV parking quota     = unverified / project policy
EV stall geometry    = unverified / project policy
```

and retain the existing requirement to re-run the legal check immediately before a production release. Electrical/charger requirements should be modeled separately from parking-space-count requirements.

## Hosted imagery and PDF-export research

### Provider terms relevant to the Stallwise workflow

The important legal/product distinction is not merely **“can the map be displayed?”** Stallwise needs separate permissions for at least:

`display` → `cache` → `trace/derive geometry` → `print/export`

A provider may permit the first and prohibit one or more of the others.

| Provider / source | Hosted display | Caching | Tracing / derived site geometry | PDF / print/export | Stallwise assessment |
|---|---|---|---|---|---|
| **Google Maps Platform** | Available subject to service/API terms | General storage/prefetch/rehosting is restricted except where service-specific terms permit it | Public terms contain explicit restrictions relevant to tracing/digitizing content from Google Maps, including satellite-map use | Printing guidance exists, but does not create a blanket right to export/rehost API imagery | **Do not use as the default tracing imagery provider** |
| **MapTiler Cloud** | Commercial use requires the appropriate paid plan | Temporary end-user caching is permitted only within stated limits; server-side proxy/cache requires appropriate contractual rights | Standard cloud terms impose restrictions on extraction/derivative use | “Limited Prints” exist under stated terms; broader export use may require a custom agreement | **Use only if the chosen contract expressly covers Stallwise tracing/export** |
| **Mapbox** | Commercial use subject to its terms/order | Service/product-specific rights matter | General ToS alone did not establish the rights Stallwise needs | General ToS alone is insufficient to clear arbitrary exported imagery | **Candidate only after commercial/legal confirmation** |
| **Customer-owned / separately licensed orthophoto, XYZ, WMTS/WMS** | Depends on source licence | Depends on source licence | Can be permitted if customer's/source licence expressly grants derivative-use rights | Can be permitted if licence grants redistribution/print rights | **Best architecture target because rights can be explicit per source** |

Google Maps Platform terms:

<https://cloud.google.com/maps-platform/terms>

Google Geo Guidelines:

<https://about.google/brand-resource-center/products-and-services/geo-guidelines/>

The Maps Platform terms impose restrictions on extracting, storing, redistributing and creating certain derived content from Google Maps content. Those restrictions are directly material to a product whose normal workflow is to look at satellite imagery and draw the site's physical geometry from it. citeturn52view0turn52view1turn52view2 Google's separate Geo Guidelines discuss permitted presentation/printing contexts, but those guidelines do not replace the contractual Maps Platform terms. citeturn52view3

MapTiler Cloud terms:

<https://www.maptiler.com/terms/cloud/>

The standard terms distinguish commercial plans, limited printing, end-user-device caching, server/proxy caching, export, and extraction/derivative uses. In particular, the standard terms are not a clean blanket authorization for a commercial parking-design application to derive geometry from imagery and then freely export the imagery; a custom agreement may be needed. citeturn50search2

Mapbox general terms:

<https://www.mapbox.com/legal/tos>

The general Mapbox terms reviewed also flag separate commercial licensing considerations for some production application categories, including real-estate-related applications. They do not, by themselves, establish the complete cache/trace/PDF rights needed to close Stallwise's question. citeturn54view0

### Hosted-provider decision

**OQ-11 status: Partially answered.**

**Source-based conclusion:** none of the public standard terms reviewed provides a sufficiently clean basis to say:

> “Stallwise may use this commercial satellite layer, let users trace geometry from it, cache it as needed, and embed the imagery in arbitrary exported PDFs.”

Google is especially unsuitable as a default for the core **trace-from-satellite** workflow because the derivative/tracing restriction is relevant before PDF export is even considered. MapTiler could become viable through a suitable commercial/custom agreement. Mapbox needs service/order-specific licensing confirmation before approval.

**Recommendation:** Stallwise should implement a **provider-neutral imagery capability contract**, rather than hard-code “satellite imagery = Google/Mapbox/MapTiler.” A provider configuration should declare, independently:

```text
may_display
may_cache_client
may_cache_server
may_trace_or_derive
may_export_pdf
may_export_raster
attribution_required
max_cache_duration
contract_reference
terms_checked_at
```

A hosted deployment should enable an operation only when the selected imagery source explicitly permits it.

### PDF imagery decision

**OQ-12 status: Partially answered.**

The legally safe generic rule is **not** “imagery may always be used for tracing but not PDF.” Public provider terms show that **tracing itself can be a separately restricted act**. citeturn52view0turn50search2

**Recommendation:** default Stallwise behaviour should therefore be:

```text
PDF vector/site geometry export: enabled
Third-party satellite/aerial raster in PDF: disabled by default
Tracing from third-party imagery: entitlement-gated
PDF imagery export: provider/contract-gated
Attribution: mandatory whenever provider licence requires it
```

When `may_export_pdf == false`, the generated PDF should contain Stallwise/user geometry only. When imagery export is contractually permitted, the export path should preserve provider attribution and any print-resolution/circulation limits.

This recommendation is a **product/legal-risk control**, not a statement that Thai law itself prohibits map imagery in PDFs.

## Benchmark-corpus research

### What the published study actually provides

OQ-16 refers to the branch-and-cut parking-lot study:

**Helen Thomas and Tarun Rambha, “A Branch-and-Cut Algorithm for the Optimal Design of Parking Lots with One-way and Two-way Lanes.”**

Paper:

<https://arxiv.org/abs/2506.09961>  
<https://arxiv.org/html/2506.09961v3>

Public authors' repository:

<https://github.com/transnetlab/parking-lot-design>

The September 2026 arXiv revision reports experiments on **325 real-world NYC parking-lot polygons** obtained from NYC open data, covering lots in lower/midtown Manhattan and parts of Brooklyn and Queens; the paper reports a lot-area range of approximately **6,011–28,436 ft²**. citeturn56view0turn57view3

The public repository contains an ID list:

<https://github.com/transnetlab/parking-lot-design/blob/main/downtown_nyc_lot_ids.txt>

and the repository exposes the lot IDs used by the study. It also contains a **single example geometry CSV**:

<https://github.com/transnetlab/parking-lot-design/blob/main/parking_lots_data_example.csv>

The example has the expected NYC-style `SOURCE_ID`, feature-code, geometry and area fields. The public repository itself confirms this example file and the ID list. The research code, however, expects a file named `parking_lots_data.csv`, while the repository root contains only `parking_lots_data_example.csv`; therefore the full 325-polygon corpus is **not bundled in the repository in a directly runnable form**.

Repository code path demonstrating that expected filename:

<https://github.com/transnetlab/parking-lot-design/blob/main/config.py>

The code calls the NYC lot loader using `parking_lots_data.csv`, and its configuration contains the published ID list workflow.

### Licence status

The **paper** is published on arXiv under the licence indicated by the arXiv record; that licence governs the paper, not automatically the software or external NYC dataset. citeturn56view0

For the GitHub repository, the root listing inspected on 24 October 2026 contains the source files, lot-ID list and example CSV but **no `LICENSE` file and no explicit repository-wide software/data licence**. A repository search also returned no licence declaration.

Repository root:

<https://github.com/transnetlab/parking-lot-design>

That means Stallwise should **not assume that the authors' Python implementation or their checked-in example data is MIT/BSD/CC-licensed merely because the repository is public**.

The fact that the study says the source polygons came from **NYC Open Data** also does not automatically license the authors' source code. Conversely, the licence/terms applying to the original municipal dataset have to be checked against the precise NYC dataset before Stallwise republishes a derived benchmark fixture set. I did not establish that exact dataset licence strongly enough in this pass to label the complete 325-lot corpus redistributable.

### Suitability for Stallwise

**OQ-16 status: Partially answered.**

**Source facts:**

- The 325-instance benchmark is real and published. citeturn56view0turn57view3
- The lot identifiers are public in the authors' repository.
- One example polygon is public.
- The authors' code expects a full `parking_lots_data.csv` that is not present in the public repository.
- No explicit repository software/data licence was found.
- The research formulation is not a Thai regulatory benchmark: the public configuration, for example, uses a 3 m vehicle-width modelling parameter and 3 m driveway parameter for its grid model, rather than Stallwise's Thai statutory rule profiles.

**Recommendation:** use this corpus as a **Phase 6 benchmark candidate, not as vendored test data yet**.

A defensible Stallwise benchmark workflow would be:

1. independently identify and download the exact NYC Open Data source;
2. record the source dataset URL, terms/licence and retrieval date;
3. reproduce the 325-lot selection using the published `SOURCE_ID` list;
4. store either the source references or only those derived fixtures whose redistribution is clearly licensed;
5. do **not** copy the unlicensed research implementation into Stallwise;
6. compare Stallwise on geometry robustness, runtime, determinism and achievable stall count, while explicitly noting that Thai rule compliance and the paper's optimisation model are different problems.

That preserves the scientific value of the paper without importing an uncertain software/data licence into Stallwise's **AGPL-3.0-or-later** repository.

## Research disposition

The most important repo-level conclusions from this focused pass are:

| Item | Disposition for Stallwise |
|---|---|
| `cited` numeric values in `TH_RULESET_DRAFT.md` | **No numerical contradiction found** in the values checked against the identified primary provisions |
| National exact 30° | **Keep unverified; no published interpretation found** |
| National perpendicular + one-way aisle | **Keep interpretation-pending; no published interpretation found** |
| BMA cls. 83–100 amendment history | **Do not promote to legally reviewed yet** |
| Accessible-strip sharing | **Keep unverified; no published interpretation found** |
| No. 33 parking overlap | **Keep full keep-out only as conservative project policy, not sourced legal interpretation** |
| Motorcycle dimensions / quota | **Keep project-policy only** |
| General EV parking quota | **No enacted general quota established; keep unverified and re-check before release** |
| Third-party imagery | **Provider-neutral and entitlement-gated** |
| Imagery in PDFs | **Off by default; enable only where contract/licence explicitly permits it** |
| Google satellite for tracing | **Do not select as Stallwise's default tracing source under the public terms reviewed** |
| NYC 325-lot corpus | **Good benchmark candidate, but full corpus availability and redistribution licence are not yet cleared** |
| OQ-08 primary-text work | **Substantially completed, but No. 33 and BMA legacy Gazette header metadata still need direct primary-header confirmation before marking the OQ fully closed** |

The remaining legal uncertainty is concentrated in **interpretation and current-law validation**, rather than in the core dimensional numbers. No published official interpretation was found for OQ-01, OQ-02, OQ-04 or OQ-05; those questions should therefore remain open rather than being resolved by software inference.