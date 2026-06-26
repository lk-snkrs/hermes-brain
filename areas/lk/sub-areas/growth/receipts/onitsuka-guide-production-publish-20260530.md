# Receipt — Onitsuka Tiger premium collection + guide published to production

Date: 2026-05-30
Approved by: Lucas in current Telegram turn
Production theme: `155065417950`
Dev source theme: `155065450718`
Asset: `sections/lk-collection.liquid`
Production URL: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`

## Scope published
Promoted the approved dev version of `sections/lk-collection.liquid` to the production theme.

Included production changes:

- Onitsuka Tiger broad collection premium/204L-style hero.
- Onitsuka after-grid Guia Editorial LK.
- Integrated guide FAQ with single `FAQPage` JSON-LD.
- Legacy `.coll-faq` suppressed for the integrated guide handles.
- Base `.lk-guide-standard-media` helper note changed to light/white background standard.

## Production backup / rollback
Pre-publish production asset backup:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-prod/onitsuka-guide-publish-20260530T180055/sections__lk-collection.before-production.liquid`

Rollback: upload that backup file back to production theme `155065417950` as `sections/lk-collection.liquid`.

## Admin readback
After propagation readback:

- production bytes: `228741`
- production sha256: `4da427677ee8902180e89764bc3984e0ca4e801e2c004c5fbe9c222ed1cdb203`
- dev sha256: `4da427677ee8902180e89764bc3984e0ca4e801e2c004c5fbe9c222ed1cdb203`
- match: true
- light helper note standard present: true
- broad Onitsuka guide condition present: true

Note: first immediate readback was stale and returned the previous production SHA. Second readback after a short delay matched the published dev asset.

## Storefront verification — production, no preview theme
URL checked:
`https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos?lkqa=prod-publish-180055`

Browser DOM/computed checks:

- `preview_theme_id`: absent / production clean URL
- `#lk-guia-onitsuka-tiger`: present
- `.lk-204l-coll-preview`: present
- H1: `Onitsuka Tiger`
- helper note background: `rgb(255, 255, 255)`
- helper note text color: `rgb(23, 23, 23)`
- helper note border: `1px rgb(226, 219, 208)`
- CTA href: `/pages/onitsuka-tiger-original-brasil-guia-lk`
- guide FAQ count: `5`
- `FAQPage` JSON-LD count: `1`
- legacy `.coll-faq`: false

Visual check confirmed:

- hero premium active;
- product grid remains product-first;
- Guia Editorial LK appears below grid;
- “Para aprofundar...” block is light/white;
- CTA is black.
