# Mobile read-more fix — 2002R LKGOC DEV

Data UTC: 20260613T123926Z

## Feedback Lucas
"Ainda tá errado, tá faltando botar um ler mais no mobile."

## Action
Updated PR #72 branch and synced only the changed hero snippet to DEV/unpublished via Shopify CLI.

## GitHub
PR: https://github.com/lk-snkrs/lk-new-theme/pull/72
New commit: `98847c5 Add mobile read-more control to 2002R LKGOC hero`

## DEV theme
Theme: `lk-new-theme/dev`
Theme ID: `155065450718`
Role: `unpublished`
Sync method: Shopify CLI `theme push`, not Shopify Admin API direct write.
File synced:
- `snippets/lk-goc-new-balance-2002r-hero-204l-clone.liquid`

## Fix
Added explicit mobile CSS for 2002R:
- `style#lk-goc-2002r-mobile-read-more-20260613`
- button `.lk-goc-read-more.lk-204l-read-more` displays as inline-flex on mobile
- button hides after `.is-open`

## QA
Remote theme pull confirmed the DEV snippet contains:
- mobile read-more style ID
- section class `lk-goc-coll-preview--204l lk-goc-coll-preview--2002r`

Preview readback with preview cookie confirmed storefront contains:
- `lk-goc-2002r-mobile-read-more`: OK
- `lk-goc-coll-preview--204l lk-goc-coll-preview--2002r`: OK
- old non-golden section marker absent: OK

## Note
Direct fetching the collection URL without first establishing the Shopify preview cookie can still return stale/production-like HTML. For QA, open the preview root URL first or use a fresh browser session with preview cookie.
