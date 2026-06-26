# Receipt — Onitsuka Tiger dev preview published to production theme

- Timestamp UTC: 20260617T133433Z
- Production theme: `lk-new-theme/production` / `155065417950`
- Source dev theme: `lk-new-theme/dev` / `155065450718`
- Assets published: `layout/theme.liquid`, `sections/lk-collection.liquid`
- Scope respected: no products, price, stock, feed/GMC, campaigns, checkout, Klaviyo/WhatsApp, or other assets.
- Public URL: `https://lk-sneakerss.myshopify.com/collections/onitsuka-tiger-todos-os-modelos`

## QA

- Assets synced from dev to production: `True`
- Desktop QA passed: `True`
- Mobile QA passed: `True`
- New title present: `True`
- New meta present: `True`
- New hero present: `True`
- Old hero absent: `True`
- New FAQ present: `True`
- Secret scan hits: `[]`

## Rollback

Restore production backups in this folder:

- `prod-before__layout__theme.liquid`
- `prod-before__sections__lk-collection.liquid`

## Impact review

- D+7: 2026-06-24
- D+14: 2026-07-01
- Metrics: GSC page/query CTR, position, clicks, impressions; GA4/Shopify organic landing/PDP/add-to-cart/revenue when available.
