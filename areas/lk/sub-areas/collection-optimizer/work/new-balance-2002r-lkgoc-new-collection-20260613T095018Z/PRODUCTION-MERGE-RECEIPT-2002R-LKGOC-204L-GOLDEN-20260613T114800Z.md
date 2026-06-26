# Production merge receipt — New Balance 2002R LKGOC aligned to 204L golden

Status: PRODUCTION WRITE EXECUTED / ADMIN READBACK OK / STOREFRONT CACHE PARTIAL
Data UTC: 20260613T114800Z
Approval: Lucas — "Aprovo 1"

## Scope approved
Promote corrected 2002R LKGOC layout to Production to align with New Balance 204L golden standard.

## Theme roles verified before write
- Production: `lk-new-theme/production`, ID `155065417950`, role `main`
- DEV source: `lk-new-theme/dev`, ID `155065450718`, role `unpublished`

## Production assets touched
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`
- `templates/collection.new-balance-2002r.json`

## Collection updated
- Collection ID: `gid://shopify/Collection/1128114815198`
- Handle: `new-balance-2002r`
- Template suffix set to: `new-balance-2002r`

## Admin/API readback
Confirmed in Production asset source:
- 2002R hero block exists with `lk-goc-coll-preview--2002r`
- 2002R headline exists: `Retrô running, presença urbana.`
- 2002R hero keeps 204L golden aliases/classes including `lk-204l-coll-preview`
- 2002R guide exists with `id="lk-guia-new-balance-2002r"`
- 2002R FAQ schema exists
- Collection template suffix readback: `new-balance-2002r`

## Storefront verification
Storefront/section endpoint showed Shopify edge cache inconsistency after production write:
- Some section-render responses already show the new 2002R hero (`lk-goc-coll-preview--2002r`, headline present).
- Other edge responses still serve the previous cached section without 2002R hero/guide.
- Full collection URL was still returning cached HTML during verification window.

## Risk / next check
This is a cache propagation issue after production asset write, not an Admin readback failure. Next validation should re-fetch public storefront after cache propagation and verify:
- hero 2002R present above toolbar/grid;
- guide 2002R present after product grid;
- FAQ schema present;
- mobile/desktop visual parity with 204L golden.

## Rollback
Backups created in the same work folder before each Production asset write. Rollback path:
1. Restore `sections/lk-collection.liquid` from the latest `before_PROD` backup.
2. Restore `snippets/lk-goc-collection.liquid` from latest `before_PROD` backup.
3. Reset collection `templateSuffix` to null if needed.
4. Delete `templates/collection.new-balance-2002r.json` if no longer used.
