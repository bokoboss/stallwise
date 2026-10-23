# 0002 — Single Rust core, shipped as WASM and CLI

- Status: Proposed (confirm after Phase 0 research, question C1)
- Date: 2026-10-23

## Context
The layout engine must run in the browser (web app) and be callable from several CAD hosts written in Python (IngeTrazo, IngeCAD) and Rust (CADCraft). Re-implementing geometry per host would diverge and multiply bugs.

## Decision
Implement all geometry, layout, validation and scoring in one Rust crate (`crates/core`) with no I/O. Ship it as:
- `crates/wasm` — WebAssembly for the browser, run in a Web Worker.
- `crates/cli` — `stallwise-cli`, JSON in / JSON out, plus a JSON-lines `serve --stdio` mode for plugins.

A Python binding (PyO3) is optional and only added if the CLI proves insufficient.

## Consequences
- One test suite defines correctness for every shell.
- Plugins are thin adapters and do not need native builds per host Python version.
- The JSON schema becomes a hard compatibility contract and must be versioned.
- Contributors need Rust in addition to TypeScript.

## Alternatives considered
- **TypeScript core** — simplest for the web, but harder to share with Python hosts and slower for search.
- **Python core** — natural for Inge* hosts, but cannot run in the browser without heavy runtimes (Pyodide).
