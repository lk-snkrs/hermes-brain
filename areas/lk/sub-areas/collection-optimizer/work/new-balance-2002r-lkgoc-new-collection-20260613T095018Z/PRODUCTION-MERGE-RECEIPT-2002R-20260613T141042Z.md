# Production merge receipt — LKGOC New Balance 2002R

Data UTC: 20260613T141042Z

## Approval
Lucas approved via Telegram: "Aprovado fazer merge na Production".

## Shopify production write
Store: `lk-sneakerss.myshopify.com`
Production theme: `lk-new-theme/production`
Theme ID: `155065417950`
Role from Shopify CLI output: `live`

Uploaded files:
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-2002r-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-2002r-guide-panel.liquid`

Scope of section change:
- replaced inline 2002R hero block with snippet render
- replaced inline 2002R guide block with snippet render
- no production-wide redesign intended

Backup path before write:
- `/opt/data/backups/lk-shopify-production-lkgoc-2002r-20260613T140706Z`

Deploy staging path:
- `/tmp/lk-prod-2002r-deploy-20260613T140824Z`

## GitHub
PR #72: https://github.com/lk-snkrs/lk-new-theme/pull/72
Merged at: `2026-06-13T14:10:18Z`
Merge commit: `cd2c9848f5135fc6fd7caaa8d9d49e23409676ce`
Base: `dev`

## Production QA after Shopify write
Production storefront URL checked without preview:
- https://lksneakers.com.br/collections/new-balance-2002r

Readback passed:
- 204L/2002R hero alias present: OK
- mobile read-more CSS present: OK
- guide present: OK
- mobile FAQ CSS present: OK
- 4 FAQ `<details>` inside guide: OK
- old FAQ grid classes absent: OK

## Rollback
If rollback is requested:
1. Push backed-up `sections/lk-collection.liquid` from `/opt/data/backups/lk-shopify-production-lkgoc-2002r-20260613T140706Z` back to live theme `155065417950` with `--allow-live --nodelete`.
2. The two 2002R snippets can remain inert because the backed-up section does not render them. If a full cleanup is required, remove the snippets in a scoped Shopify theme operation after approval.
3. Re-check the production collection URL and record a rollback receipt.

## Impact review
Schedule/check in ~7 days:
- mobile UX around hero reveal/read-more
- FAQ accordion engagement if available
- GSC/GA4 collection trend if authenticated data available
- no visual regressions on surrounding collection template
