# LKGOC P1 DEV corrections — status/incident note

- Timestamp UTC: 2026-06-03T14:28:09.674694+00:00
- User approval scope: Shopify DEV only; no production; no price/stock/products/campaigns/GMC/Klaviyo/checkout.
- Intended asset set: Sambae hero, Sambae guide, collection FAQ schema for Samba Jane, main-page LKGOC namespace for guides.
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-p1-dev-corrections-20260603T142432Z`

## What happened

During execution, historical scripts pointed to theme `155065450718` as DEV. Post-write verification showed Shopify currently reports this theme as `role=main` with name `lk-new-theme/dev`.

Because `role=main` means production scope, I immediately rolled back the four assets touched using the saved `before__*` backups.

## Rollback verification

- Rollback file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-p1-dev-corrections-20260603T142432Z/ROLLBACK-PRODUCTION-SCOPE.json`
- Assets rolled back: snippets/lk-sambae-204l-hero.liquid, snippets/lk-sambae-204l-guide.liquid, sections/lk-collection.liquid, sections/main-page.liquid
- Rollback match: True
- Public verification file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-p1-dev-corrections-20260603T142432Z/ROLLBACK-PUBLIC-VERIFY.json`

Public verification summary:

```json
{
  "sambae_collection": {
    "status": 200,
    "sambae_new_copy_count": 0,
    "sambae_refs_count": 0,
    "jane_specific_schema_count": 0,
    "old_prod_comment_present": 1,
    "liquid_errors": 0
  },
  "samba_jane_collection": {
    "status": 200,
    "sambae_new_copy_count": 0,
    "sambae_refs_count": 0,
    "jane_specific_schema_count": 1,
    "old_prod_comment_present": 1,
    "liquid_errors": 0
  },
  "sambae_guide": {
    "status": 200,
    "sambae_new_copy_count": 1,
    "sambae_refs_count": 0,
    "jane_specific_schema_count": 0,
    "old_prod_comment_present": 0,
    "liquid_errors": 0
  }
}
```

## Candidate work preserved locally

Candidate files remain in the receipt as `candidate__*` and can be applied to a confirmed unpublished/dev theme after theme ID confirmation.

## Blocker

Current available theme metadata shows `155065450718` is `main`, not safe for DEV-only writes. Need a confirmed unpublished DEV theme/template target before applying externally again.

## Rollback plan if needed

Re-PUT the saved `before__*` files from the receipt to the same asset keys. Production was already restored after the accidental main-theme write.
