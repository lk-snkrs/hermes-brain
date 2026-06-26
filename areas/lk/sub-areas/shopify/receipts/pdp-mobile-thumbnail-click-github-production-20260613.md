# PDP mobile thumbnail click — GitHub production receipt

Date: 2026-06-13 11:22 UTC
Profile: lk-shopify
Scope approved by Lucas: merge Production

## Change

- Source approval path: GitHub `dev` PR #69 already merged.
- Production PR: https://github.com/lk-snkrs/lk-new-theme/pull/70
- Merge target: `production`
- Merge commit: `6a40105a27b292dca23ca013c7dbb1a11184543b`
- File changed: `sections/lk-pdp.liquid`

## Summary

Promoted the approved PDP mobile thumbnail click fix to the GitHub `production` branch as a scoped cherry-pick, instead of merging all current `dev` drift into `production`.

## Verification

- Before PR: `git diff --check origin/production...HEAD` passed.
- PR file list: only `sections/lk-pdp.liquid` (`+24`, `-2`).
- PR state readback: `MERGED`.
- `origin/production` fetched/read back at merge commit `6a40105`.
- `origin/production:sections/lk-pdp.liquid` includes `syncMobileGallery` markers and thumbnail-click calls.

## Guardrails

- GitHub `production` branch merge only.
- No Shopify theme upload/publication was performed in this step.
- Broad `dev` → `production` merge was intentionally avoided because `dev` contains unrelated drift; only the scoped PDP fix was promoted.

## Rollback

- Revert PR #70 / merge commit `6a40105a27b292dca23ca013c7dbb1a11184543b` on `production`, or apply the reverse patch for the `syncMobileGallery` change in `sections/lk-pdp.liquid`.
