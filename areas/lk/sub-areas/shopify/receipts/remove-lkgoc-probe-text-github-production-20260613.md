# Remove LKGOC probe text — GitHub production receipt

Date: 2026-06-13 11:46 UTC
Profile: lk-shopify
Scope approved by Lucas: corrigir GitHub dev e fazer merge para Production

## Issue

Visible test/probe text appeared on the Onitsuka Tiger collection page between the LKGOC hero and the collection toolbar:

`LKGOC_PROBE_TEXT_20260613T111300Z`

## Source state

- `origin/dev`: already clean; no `LKGOC_PROBE_TEXT_20260613T111300Z` / `LKGOC-PROD-PROBE` markers in `sections/lk-collection.liquid`.
- `origin/production`: contained temporary probe comments plus the visible probe text in `sections/lk-collection.liquid`.

## Change

- Production PR: https://github.com/lk-snkrs/lk-new-theme/pull/71
- Merge target: `production`
- Merge commit: `1f600aee9919bb11514bc76a740e7d2f98010bef`
- File changed: `sections/lk-collection.liquid`
- Diff: removed 3 probe lines:
  - `<!-- LKGOC-PROD-PROBE-2002R-20260613T110600Z ... -->`
  - `<!-- LKGOC-PROD-PROBE-2002R-20260613T111000Z ... -->`
  - `LKGOC_PROBE_TEXT_20260613T111300Z`

## Verification

- `git diff --check origin/production...HEAD` passed before merge.
- PR file list: only `sections/lk-collection.liquid` (`+0`, `-3`).
- PR state readback: `MERGED`.
- `origin/production` fetched/read back at merge commit `1f600ae`.
- `git grep` on `origin/dev` and `origin/production` found no remaining `LKGOC_PROBE_TEXT_20260613T111300Z` or `LKGOC-PROD-PROBE` in `sections/lk-collection.liquid`.
- Public read-only fetch of `https://lksneakers.com.br/collections/onitsuka-tiger` did not contain the visible probe text; page content showed normal Onitsuka Tiger collection text and `149 itens`.

## Guardrails

- GitHub branch merge only.
- No Shopify theme upload/publication was performed in this step.
- Because `origin/dev` was already clean, no dev PR was necessary; production was corrected to match the clean state for this scoped marker.

## Rollback

- Revert PR #71 / merge commit `1f600aee9919bb11514bc76a740e7d2f98010bef` on `production` if needed.
