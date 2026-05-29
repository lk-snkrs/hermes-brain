# Mexico 66 → 204L Desktop Parity — Production Publish Validation

- Timestamp UTC: 2026-05-28T19:14:50Z
- Theme production: `155065417950` (`lk-new-theme/production`, role `main`)
- Collection: `onitsuka-tiger-mexico-66`
- Public URL: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66

## Published assets

- `layout/theme.liquid`: production readback contains Mexico 66 desktop parity rules.
- `assets/lk-204l-hero-fix-20260527-1545.css`: Admin readback contains high-specificity hotfix. Public CDN edge may still serve the previous asset, but the live public HTML now contains the inline parity CSS, so visual geometry is applied.

## Live storefront validation

Cache-busted URL used:

- https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?lkqa=prod-publish-20260528-01

Browser computed style result:

- `.coll-banner`
  - `padding-top`: `40px`
  - `padding-bottom`: `18px`
  - `top`: `100`
  - `bottom`: `243`
- `.lk-next-coll-preview--onitsuka-tiger-mexico-66`
  - `padding-top`: `20px`
  - `padding-bottom`: `18px`
  - `top`: `243`
  - `bottom`: `573`
  - `height`: `330`

SEO/GEO validation:

- `FAQPage` JSON-LD count: `1`
- Guide block present: `true`

## Rollback

Primary rollback file:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/mexico66-desktop-204l-parity-20260528-190610/layout__theme.before.liquid`

Rollback instruction:

- Restore `layout/theme.liquid` from `layout__theme.before.liquid` to theme `155065417950`.
