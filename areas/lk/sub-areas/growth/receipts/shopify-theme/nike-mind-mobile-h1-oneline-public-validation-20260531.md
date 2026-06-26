# LK Nike Mind — Mobile H1 One-Line Correction

- Timestamp: 2026-05-31
- Approval basis: Lucas: `Corrigir: Nike Mind 001/002 Deve ficar em uma linha só na versão móbile, não em duas`
- Target: Shopify production/main theme `155065417950`
- URL: https://www.lksneakers.com.br/collections/nike-mind-001

## Change

CSS-only scoped correction in `assets/lk-collection-v2.css`:

```css
@media(max-width:749px){
  body:has(.lk-collection-v2--nike-mind-redo) .coll-banner__title{
    font-size:clamp(26px,7.45vw,31px)!important;
    line-height:1!important;
    letter-spacing:-.055em!important;
    white-space:nowrap!important;
    max-width:calc(100vw - 28px)!important;
    overflow:visible!important;
  }
}
```

## Validation

- Shopify Admin readback: production asset contains the scoped mobile rule.
- Public CDN CSS: served CSS contains the rule, minified by Shopify.
- H1 remains: `Nike Mind 001/002`.
- Fit simulation using page font family and mobile rule:
  - 320px viewport: text width ~169px / available 292px — fits
  - 360px viewport: text width ~174px / available 332px — fits
  - 375px viewport: text width ~182px / available 347px — fits
  - 390px viewport: text width ~189px / available 362px — fits
  - 430px viewport: text width ~202px / available 402px — fits

## Rollback

Primary backup receipt:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-mobile-h1-oneline-20260531T133552Z/receipt.json`

Rollback: restore `assets__lk-collection-v2.css.before` to `assets/lk-collection-v2.css` in theme `155065417950`.
