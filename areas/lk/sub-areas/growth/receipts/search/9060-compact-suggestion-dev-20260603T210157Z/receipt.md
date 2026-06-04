# Receipt — Dev preview: compact 9060 search suggestion

Date UTC: 20260603T210157Z

## Approval
Lucas approved: `aprovo` after the proposed scope to refactor the ugly collection card into a compact suggestion inside the search banner.

## Scope executed
- Shopify Dev/unpublished theme only.
- Theme ID: `155065450718`
- Theme name: `lk-new-theme/dev`
- Theme role verified before upload: `unpublished`
- Asset: `sections/lk-search.liquid`

## Non-actions
- Production theme was not changed.
- No Shopify product, collection, price, stock, checkout, app, Search & Discovery, GMC, Klaviyo, Meta, WhatsApp or campaign setting was changed.

## Technical change
Changed the 9060 search collection module from a large off-white card below the banner to a compact inline suggestion inside the black search banner.

Rendered copy:
- `Coleção sugerida:`
- `New Balance 9060`
- `Ver coleção completa →`
- Link: `/collections/new-balance-9060`

## Readback evidence
- Dev before SHA-16: `08a64a88375c3c4a`
- Target/local SHA-16: `521ff5570755ddc4`
- Dev after/readback SHA-16: `521ff5570755ddc4`
- Production before SHA-16: `dcb60b4ab1cc6818`
- Production after SHA-16: `dcb60b4ab1cc6818`
- `dev_readback_matches_target`: `True`
- `production_unchanged`: `True`

## QA
- Old large-card copy removed: `True`
- Compact copy present: `True`
- Suggestion markup is inside the search banner before the toolbar: `True`
- Search remains product-only: `True`
- Product grid render remains via `lk-product-card`.

## Preview
Authenticated Dev preview URL:
`https://lksneakers.com.br/search?q=9060&preview_theme_id=155065450718`

Note: public unauthenticated Shopify preview may serve live HTML/cache and drop the dev module. Use authenticated Shopify preview for visual review.

## Rollback
Re-upload `dev_before.liquid` from this receipt folder to theme `155065450718`, asset `sections/lk-search.liquid`, then verify SHA returns to `08a64a88375c3c4a`.
