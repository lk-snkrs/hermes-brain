# Shopify production — 204L mobile override fix

- Date: 2026-05-27
- Collection: `/collections/new-balance-204l`
- Issue reported: previous mobile size changes appeared not applied.

## Root cause
A later production hotfix block still forced:

`body:has(.lk-204l-coll-preview) .coll-banner__title{font-size:52px!important;}`

Because it appeared later in `sections/lk-collection.liquid`, it overrode the earlier mobile `44px` rule.

## Production changes
1. Replaced the stale global `52px` title hotfix with a mobile-only hierarchy correction:
   - H1: `44px!important`, `line-height:1.02`, `margin-bottom:6px`
   - Kicker: `8px!important`, `letter-spacing:.14em`, `margin:0 0 7px`
2. Added a high-specificity force block to `assets/lk-product-card.css` as a fallback for stale section HTML/CSS order.

## Backups
- Section backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-mobile-override-fix-20260527-141554`
- CSS asset backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-css-asset-force-20260527-141849`

## Validation
- Shopify Admin API readback confirms section asset no longer contains the stale exact `52px` override.
- Public HTML probes with cachebuster confirmed final mobile rules:
  - H1 rule: `font-size:44px!important; line-height:1.02!important; margin-bottom:6px!important;`
  - Kicker rule: `font-size:8px!important; letter-spacing:.14em!important; margin:0 0 7px!important;`
- Ten public cachebuster probes returned the corrected section rules and no stale `52px` title rule.

## Notes
- Browser session used by Hermes had an inconsistent Shopify/CDN edge cache during validation, but direct public probes with fresh query strings returned the corrected HTML consistently after the final patch.
