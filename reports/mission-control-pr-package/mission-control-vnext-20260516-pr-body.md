# PR body — Mission Control vNext COO Desk

## Summary

This local PR package rebuilds Mission Control into a read-only COO desk for Lucas, with a Decision Inbox first, A1-A4 approval gates, source-aware action packets, a restricted operating kanban, feed quality validation and a local QA gate.

## What changed

- Rebuilt the home page around `Decision Inbox · Lucas Queue` instead of a module catalog.
- Added source, safe next gesture, blocked action and gate to each decision packet.
- Connected UI state to generated `ops-state` data.
- Added Action API receipt surface with allowlisted, no-external-write behavior.
- Added feed quality checks to the Mission Control watchdog.
- Added regression tests for feed quality failures.
- Added `npm run qa:local` as a local pre-PR/pre-deploy gate.
- Polished Decision Inbox copy, hierarchy and readability after visual review.

## QA evidence

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

```text
npx impeccable detect --fast --json src
[]
```

Additional verification:

- `git diff --check` passed.
- Local production build served on port 3010 for browser/visual review.
- Correct public production verification target is `https://mission.lucascimino.com/`.
- Current production URL check: `https://mission.lucascimino.com/?check=pr-3` returns HTTP 200 on Vercel and renders Mission Control.
- Important: the production URL is not proof that this PR head is deployed. Final post-merge/deploy verification must re-check `mission.lucascimino.com` for this PR's Decision Inbox markers.
- Independent pre-commit review passed with no security concerns or blocking logic issues.
- Forward and rollback patches are generated locally for review.

## Rollback

Use the rollback patch in the local package directory, then run:

```bash
npm run qa:local
```

If already deployed, promote previous known-good Vercel deployment or redeploy a rollback commit.

## Explicit exclusions

This package does not execute or authorize:

- GitHub push, merge or deployment without explicit approval;
- Vercel production deploy or env changes;
- Docker/VPS/gateway restarts;
- Shopify/Tiny/Merchant/Meta/Google writes;
- customer/client/external sends;
- secret printing or credential changes.
