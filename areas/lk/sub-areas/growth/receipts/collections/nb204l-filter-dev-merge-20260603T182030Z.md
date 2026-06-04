# NB 204L Filter UX — PR #20 merged into dev

Timestamp: 2026-06-03T18:20:30Z

## Scope

Approved by Lucas: merge PR #20.

This execution merged the collection filter UX patch into the GitHub `dev` branch only.

## PR

- Repository: `lk-snkrs/lk-new-theme`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/20
- Title: `fix(collection): hide single-value filters on NB 204L preview`
- Base: `dev`
- Head: `fix/nb204l-filter-ux`
- Precheck: `mergeable=true`, `mergeable_state=clean`, `draft=false`
- Checks: none reported by GitHub check-runs endpoint

## Result

- Merge method: squash
- Merge commit SHA: `ae849f3645f5ebaf8e9862bc1e09907bacb0118d`
- PR state after merge: `closed`, `merged=true`
- Remote feature branch deletion: successful (`HTTP 204`)
- Verification: merge commit is ancestor of `origin/dev`

## Boundaries

- No Shopify production theme write executed.
- No Shopify product/metafield write executed.
- No production branch/theme promotion executed.
- Dev/unpublished preview upload/readback had already been completed separately before this merge.

## Rollback

If the `dev` branch needs rollback, revert the squash merge commit:

```bash
git checkout dev
git pull origin dev
git revert ae849f3645f5ebaf8e9862bc1e09907bacb0118d
git push origin dev
```

If the Dev Shopify theme preview needs rollback, restore the prior remote asset backup from the earlier receipt directory:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/collections/nb204l-filter-dev-preview-20260603T1810Z/`

## Next decision

Separate approval is still required for either:

1. Product/metafield writes to fill `shopify.color-pattern` for NB 204L color filters.
2. Any future production theme promotion.
