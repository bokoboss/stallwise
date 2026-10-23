# 0001 — License: AGPL-3.0-or-later

- Status: Accepted
- Date: 2026-10-23

## Context
Stallwise is a web application whose core value is its layout engine. It will also integrate with open-source CAD hosts, some of which are GPL-3.0 (e.g. IngeTrazo).

## Decision
License the whole repository under **GNU AGPL-3.0-or-later**.

## Consequences
- Anyone who runs a modified Stallwise as a network service must offer its users the corresponding source (§13). The web app shows a visible "Source" link.
- Dependencies must be AGPL-compatible. GPL-2.0-only dependencies are excluded. Checked in CI.
- Plugins for GPL-3.0 hosts are licence-compatible with AGPL-3.0 (GPL-3.0 §13 / AGPL-3.0 §13 allow combination).
- Third-party contributions are accepted under the same licence (inbound = outbound). Whether to add a CLA (to keep relicensing options open) is an open question.

## Alternatives considered
- **Proprietary core + open plugins** — more commercial flexibility, but conflicts with the open-source host ecosystem and adds licence-boundary complexity.
- **MIT/Apache-2.0** — maximum adoption, but allows closed hosted forks.

_This is an engineering record, not legal advice._
