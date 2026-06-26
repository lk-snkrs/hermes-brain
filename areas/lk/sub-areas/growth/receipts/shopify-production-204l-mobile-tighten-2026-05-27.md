# Shopify production — New Balance 204L mobile tighten

- Date: 2026-05-27
- Scope: production collection banner on `new-balance-204l`
- Request: reduce collection title size by ~15% and tighten `Curadoria LK`
- Change applied: mobile-only override in `sections/lk-collection.liquid`

## What changed
- `body:has(.lk-204l-coll-preview) .coll-banner__title` set to `44px` on mobile (`max-width: 989px`)
- `.lk-204l-kicker` reduced from `9px` to `8px` on mobile
- Editorial body section `h2` kept at `24px`

## Backup
- Backup folder: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-mobile-tighten-20260527-135706`
- Pre-change asset: `sections__lk-collection.liquid`
- Readback receipt: `receipt-api-readback.json`

## Validation
- Live theme asset confirmed through Shopify Admin API readback
- Existing 204L page is served from the updated theme asset

## Notes
- Change is scoped to the 204L collection preview block
- No production theme template outside the 204L block was modified
