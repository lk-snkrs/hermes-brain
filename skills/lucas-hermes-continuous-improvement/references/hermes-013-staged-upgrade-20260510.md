# Hermes 0.13 staged upgrade lesson — 2026-05-10

## Context
Lucas approved a daily 02:00 BRT continuous-improvement protocol for Hermes/LK, but production/infra/Docker/secrets/banco remain approval-gated. Current runtime was Hermes Agent v0.12.0 under `/opt/hermes`; `/opt/hermes` was not a git repository, so native `hermes update --check` failed with `Not a git repository`.

## Safe pattern established
1. Do not update in-place when runtime is not a git checkout or when Hermes is part of Lucas's active operational stack.
2. Prepare the new Hermes release in parallel under `/opt/data/hermes_bruno_ingest/`.
3. Preserve local reliability patches before build/deploy. For v0.13, keep the context-compression retry patch for transient provider/network failures such as `incomplete chunked read`, `peer closed connection`, `RemoteProtocolError`, EOF, resets, and timeouts.
4. Validate the patch with syntax check and targeted tests before any container/runtime swap.
5. Document decisions and test results in Hermes Brain reports.
6. Only then propose build + smoke tests + rollback + planned restart; do not swap gateway/container without explicit approval.

## v0.13 facts from the session
- Target release/tag: `v2026.5.7` / Hermes Agent 0.13 “The Tenacity Release”.
- Local parallel clone: `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0`.
- Runtime still active after prep: v0.12.0.
- Patch files: `agent/context_compressor.py` and `tests/agent/test_context_compressor.py`.
- Targeted test command passed: `python -m py_compile ... && python -m pytest tests/agent/test_context_compressor.py -q -o 'addopts='` with `70 passed`.
- Brain report created: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-013-continuous-improvement-2026-05-10.md`.

## Features to adopt after controlled deploy
- `/goal` for long tasks that otherwise depend on repeated “seguir”.
- Multi-Agent Kanban / Mission Control for LK growth operations.
- Shopify optional skill read-only first; no writes until approved.
- Dashboard local-only or via SSH tunnel; not public by default.
- `no_agent` watchdog crons for cheap daily checks.

## Pitfall
Do not treat successful clone + targeted tests as production readiness. Full config compatibility, dependency audit, Docker build, smoke tests, and rollback must still happen before switching the active gateway.