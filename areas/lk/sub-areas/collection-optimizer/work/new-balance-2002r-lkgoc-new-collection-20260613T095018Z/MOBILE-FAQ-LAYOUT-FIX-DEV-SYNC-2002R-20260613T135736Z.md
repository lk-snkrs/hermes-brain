# Mobile FAQ layout fix — 2002R LKGOC DEV

Data UTC: 20260613T135736Z

## Feedback Lucas
"Arrumar o layout do perguntas frequentes no mobile, está errado."

## Action
Fixed the 2002R guide FAQ mobile layout in DEV/unpublished and updated PR #72.

## GitHub
PR: https://github.com/lk-snkrs/lk-new-theme/pull/72
Commit: `9c57636 Fix 2002R guide FAQ mobile layout`

## DEV theme
Theme: `lk-new-theme/dev`
Theme ID: `155065450718`
Role confirmed by Shopify CLI push output: `unpublished`
File synced:
- `snippets/lk-goc-new-balance-2002r-guide-panel.liquid`

## Fix
- Replaced the old standalone FAQ grid (`lk-goc-faq-grid` / `lk-goc-faq-item`) with the standard LKGOC guide FAQ pattern:
  - `lk-goc-guide-faq lk-guide-standard-faq`
  - 4 `<details>` accordion items
  - schema microdata preserved
- Moved FAQ into the main guide card, matching 530/9060 canonical pattern.
- Added scoped mobile CSS:
  - `style#lk-goc-2002r-faq-mobile-layout-20260613`
  - single-column mobile layout
  - proper spacing, border top, full-width details cards, readable summary/p text

## QA
Remote DEV pull confirmed:
- mobile CSS present: OK
- details count = 4: OK
- old FAQ grid absent: OK
- FAQ inside main guide card before comparison card: OK

Storefront preview readback with Shopify preview cookie confirmed:
- guide present: OK
- mobile CSS present: OK
- 4 FAQ details in guide: OK
- old grid absent: OK

No production write.
