# Repro user-flow after Lucas reported failure

Data: 2026-06-17
values_printed=false

## Trigger
Lucas reported: `não funcionou` after Dev upload/QA.

## Action
Reproduced a more realistic user flow in Chromium mobile viewport `390x844`:

1. Opened Dev preview PDP:
   `https://www.lksneakers.com.br/products/air-jordan-1-mid-wolf-grey?preview_theme_id=155065450718`
2. Cleared only the browser-session cart.
3. Added 8 available variants to the browser-session cart using storefront `/cart/add.js`.
4. Clicked the visible header cart icon `#lk-cart-icon`, instead of artificially dispatching only `cart:open`.
5. Captured drawer state and screenshot.
6. Cleared the browser-session cart at the end.

No production/theme/product/stock/price/checkout write was performed.

## Result from repro
Source JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/repro-user-flow/repro.json`

Last measured state after visible cart click:

- `drawerOpen`: `cart-drawer open`
- `drawerDisplay`: `flex`
- `bodyExists`: true
- `itemsExists`: true
- `itemsCount`: 8
- `bodyDisplay`: `flex`
- `bodyMinHeight`: `0px`
- `itemsOverflowY`: `auto`
- `itemsMinHeight`: `0px`
- `itemsOverscroll`: `contain`
- `itemsRect.scrollHeight`: 1313
- `itemsRect.clientHeight`: 183
- `ctaRect.b`: 668 inside viewport height 844
- `liquidError`: false

## Interpretation
The agent-side reproduction of the real click flow passed. Lucas's failure is therefore likely one of these divergences:

1. Lucas tested a different surface than Dev preview, possibly production/live.
2. Lucas saw a specific issue not covered by the two original targets, e.g. add-to-cart auto-open, scroll gesture behavior, specific phone/browser, or a specific product.
3. Preview/cookie context differs in Lucas's browser.

## Screenshot
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/repro-user-flow/user-flow-after-cart-click.png`

## Next needed evidence
Ask Lucas for what specifically failed and ideally a screenshot/video/URL. Do not promote to production.
