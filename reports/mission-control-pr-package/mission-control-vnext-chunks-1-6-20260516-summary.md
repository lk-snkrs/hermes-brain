# Mission Control vNext PR package — chunks 1–6 — 2026-05-16

## Status

Local PR package prepared. **No GitHub push, PR creation, Vercel deploy, Docker/VPS/gateway restart, external write, or secret exposure executed.**

## Branch and base

- Repo: `lk-snkrs/mission-control-cimino`
- Local branch: `rebuild/mission-control-zero-tenacitos-20260516`
- Base commit/tag: `fabae1a` / `rollback/mission-control-pre-zero-tenacitos-20260516-145015`
- Head commit: `836b602 chore: add mission control local qa gate`

## Package files

- Forward patch: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-vnext-chunks-1-6-20260516.patch`
- Rollback patch: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-vnext-chunks-1-6-20260516-rollback.patch`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-vnext-chunks-1-6-20260516-summary.md`

## Commit range included

```text
d8c074f feat: rebuild mission control COO desk vnext
800ca98 feat: connect mission control queue to ops state
4894986 fix: harden mission control ops state feed
5bb28b9 chore: wire feed quality into mission watchdog
0c71307 test: cover mission feed quality watchdog
836b602 chore: add mission control local qa gate
```

## Scope

This package consolidates Mission Control vNext chunks 1–6:

1. Zero PRD / audit and vNext TenacitOS-style rebuild artifacts.
2. Mission Control COO desk vNext surface in the existing app.
3. Generated ops-state feed connected to the UI and Brain JSON mirror.
4. `feedQuality` wired into the Mission Control silent watchdog.
5. Regression fixtures proving broken `feedQuality` produces actionable alerts.
6. `npm run qa:local` local QA gate for pre-PR/pre-deploy checks.

## Changed areas

- `src/components/modules/MissionPages.tsx`
- `src/components/modules/CommandActionPanel.tsx`
- `src/data/vnext-operating-system.ts`
- `src/data/ops-state.generated.ts`
- `src/app/globals.css`
- `scripts/mission_control_ops_state.py`
- `scripts/mission_control_ops_watchdog.py`
- `scripts/mission_control_qa_gate.py`
- `tests/test_mission_control_ops_watchdog.py`
- `tests/test_mission_control_qa_gate.py`
- `package.json`
- `docs/rebuild/*chunk*` and zero/audit reports

## QA evidence

Latest local gate:

```text
npm run qa:local
PASS python unittest watchdog fixtures
PASS python py_compile watchdog scripts
PASS mission watchdog silent OK
PASS git diff whitespace check
PASS git staged diff whitespace check
PASS npm lint
PASS npm build
PASS diff secret scan
Mission Control QA gate passed
```

Additional verification for this package:

- Forward patch generated from `fabae1a..HEAD`.
- Rollback patch generated from `HEAD..fabae1a`.
- Patch check: `git apply --check` on a temporary worktree from base.
- Rollback patch check: `git apply --check` on a temporary worktree from head.
- Secret scan against patch artifacts.

## Rollback

If the package is later pushed/deployed and must be reverted:

1. Apply rollback patch:

```bash
git apply /opt/data/hermes_bruno_ingest/hermes-brain/reports/mission-control-pr-package/mission-control-vnext-chunks-1-6-20260516-rollback.patch
```

2. Run:

```bash
npm run qa:local
```

3. If deployed on Vercel, promote previous known-good deployment or redeploy the rollback commit.

## Explicit exclusions

This package does **not** authorize or execute:

- GitHub push / PR creation / merge;
- Vercel deploy or env changes;
- Docker/VPS/gateway restarts;
- Shopify/Tiny/Merchant/Meta/Google writes;
- client/customer/external sends;
- secrets printing or credential changes.
