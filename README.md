# Stallwise

**Automatic parking-lot layout for concept and feasibility design.**
Draw or import a site, set the design rules, and Stallwise generates a parking layout that you can then lock, edit and regenerate.

> Status: **Phase 0 — specification v0.2, awaiting owner review.** No working code yet.
> See [`docs/ROADMAP.md`](docs/ROADMAP.md).

---

## What it will do

1. **Bring in a site** — import a CAD file (DXF), draw on a map, or draw in a plain local canvas.
2. **Set the rules** — pick a jurisdiction profile (Thai national or BMA) and your project standard: stall size, parking angle (90° / 60° / 45° / parallel), aisle width, one-way or two-way, accessible-stall ratio, setbacks.
3. **Generate** — the engine searches orientations and offsets for the layout with the most usable stalls that still meets the circulation rules.
4. **Edit** — lock zones, move aisles, add or delete stalls; only unlocked areas are regenerated.
5. **Export** — DXF back into CAD at its original coordinates, GeoJSON, PDF and a stall-count summary.

## Three ways to work with a site

| Mode | When to use | Coordinates |
|---|---|---|
| **Local** | CAD file without real-world coordinates, or no map needed | File's own coordinates |
| **Georeferenced CAD** | CAD already in a projected CRS (e.g. UTM 47N/48N) | Declared CRS |
| **Map** | Concept study on satellite/street map, or floating CAD aligned with control points | Projected metric CRS derived from the map |

Geometry is always computed in metres in a projected/local frame — never in latitude/longitude.

## Planned repository layout

```
stallwise/
├─ crates/
│  ├─ core/     Rust geometry and layout engine (no I/O, no UI)
│  ├─ wasm/     WebAssembly bindings for the web app
│  └─ cli/      stallwise-cli: JSON in → JSON out (used by CAD plugins)
├─ apps/
│  └─ web/      React web app: map, canvas editor, import/export
├─ plugins/     CAD integrations (decided after the web app is stable)
├─ schemas/     Shared JSON Schemas (project, site, parameters, layout)
└─ docs/        Spec, architecture, roadmap, ADRs, research brief
```

## Documents

- [`docs/SPEC.md`](docs/SPEC.md) — product specification and acceptance criteria
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — system design, data model, coordinate handling
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — phased development plan with exit criteria
- [`docs/rules/TH_RULESET_DRAFT.md`](docs/rules/TH_RULESET_DRAFT.md) — Thai national and BMA rule values with citation and verification status
- [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) — unresolved legal, geospatial, technical and product questions
- [`docs/RESEARCH_BRIEF.md`](docs/RESEARCH_BRIEF.md) and [`docs/research/`](docs/research/) — Phase 0 research brief and findings
- [`docs/adr/`](docs/adr/) — architecture decision records
- [`CLAUDE.md`](CLAUDE.md) — working rules for AI-assisted development in this repo

## License

Stallwise is licensed under the **GNU Affero General Public License v3.0 or later** — see [`LICENSE`](LICENSE).
Because the web app is used over a network, any hosted version must offer its users the corresponding source code (AGPL §13). The web app will include a visible "Source" link for this purpose.

---

## สรุปภาษาไทย

Stallwise คือเว็บแอปสำหรับจัดผังลานจอดรถอัตโนมัติ ใช้กับงานออกแบบแนวคิดและศึกษาความเป็นไปได้ ผู้ใช้นำเข้าไฟล์ CAD (DXF) หรือวาดขอบเขตพื้นที่บนแผนที่ แล้วตั้งค่ามุมจอด ขนาดช่องจอด และความกว้างทางวิ่ง ระบบจะสร้างผังที่ได้จำนวนช่องจอดสูงสุดให้ ผู้ใช้ล็อกบางโซน แก้ไขผัง แล้วให้ระบบสร้างผังใหม่เฉพาะส่วนที่ยังไม่ล็อกได้ และ export กลับเป็น DXF ที่ตำแหน่งตรงกับไฟล์เดิม

- **สถานะ:** เฟส 0 spec v0.2 รอเจ้าของโปรเจกต์ตรวจทาน ยังไม่มีโค้ดที่ใช้งานได้
- **กฎการออกแบบ:** แยกเป็นโปรไฟล์กฎหมาย (ระดับประเทศ / กทม.) กับมาตรฐานของโครงการ เช่น ช่องจอด 2.50 × 5.00 ม. ซึ่งต้องไม่ต่ำกว่าค่าขั้นต่ำตามกฎหมาย
- **โครงสร้างระบบ:** geometry engine เขียนด้วย Rust เป็นแกนกลางชิ้นเดียว ทำงานบนเว็บผ่าน WASM และต่อกับโปรแกรม CAD ผ่าน CLI แบบ JSON
- **Plugin ที่วางเป้าไว้:** IngeCAD, CADCraft และ IngeTrazo ยืนยันลำดับเมื่อเริ่มเฟส 5
- **License:** AGPL-3.0-or-later
