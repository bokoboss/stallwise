# CLAUDE.md — Working rules for Stallwise

Stallwise is an automatic parking-lot layout tool. Read `docs/SPEC.md`, `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` before starting any task. The current phase is shown at the top of `docs/ROADMAP.md`.

## Hard rules

1. **Layout logic lives only in `crates/core`.** The web app, CLI and plugins must not re-implement geometry or rules.
2. **The engine works in metres on a planar frame.** Never pass latitude/longitude into `crates/core`. CRS handling belongs to `apps/web`.
3. **Never change source coordinates on import.** Store transforms separately (ADR-0003).
4. **Determinism.** Same input + rule set + engine version → identical output. Any randomness takes an explicit seed.
5. **No invented regulatory values.** Every number in a regulatory rule set needs a citation (regulation, clause, edition) and a status from SPEC RS-4 (`unverified` / `cited` / `cross-checked` / `legally-reviewed`). Source of truth: `docs/rules/TH_RULESET_DRAFT.md`. Never fill a gap in one profile with another profile's value. If unknown, mark `unverified` and add to `docs/OPEN_QUESTIONS.md` — do not guess.
6. **Jurisdiction vs project standard.** Legal values are minimums/maximums; the project standard (default 90° stall 2.50 × 5.00 m) is a separate layer that must satisfy them (SPEC RS-6).
7. **JSON schema is a contract.** Any change to `schemas/` needs a version bump and a migration note.
8. **Licence.** AGPL-3.0-or-later. Do not add GPL-2.0-only or otherwise AGPL-incompatible dependencies. Note the licence of every new dependency in the PR.
9. **Stay in phase.** Do not build features from later phases unless the task says so.

## Workflow

- Branch per task: `phase-N/short-topic`. Small, reviewable PRs.
- Every PR states: what changed, which SPEC requirement IDs it covers, how it was tested, known limitations.
- Tests come with the code. Core changes need unit tests; geometry changes need property or fixture tests.
- Update docs in the same PR when behaviour or decisions change. New decisions → new ADR in `docs/adr/`.

## Commands (to be filled in as the workspace is created)

| Task | Command |
|---|---|
| Rust format / lint / test | `cargo fmt --all` · `cargo clippy --all-targets -- -D warnings` · `cargo test --workspace` |
| Licence check | `cargo deny check` |
| Web | _added in Phase 3_ |

## Language

- Code, identifiers, commit messages and technical docs: English.
- UI text: Thai and English via i18n files, never hard-coded.
