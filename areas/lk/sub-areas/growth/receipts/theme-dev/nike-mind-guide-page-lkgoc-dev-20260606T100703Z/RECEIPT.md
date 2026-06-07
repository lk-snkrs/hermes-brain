# Receipt DEV — Nike Mind guia dedicado LKGOC rewrite

Data UTC: 2026-06-06T10:14Z
Pedido: Lucas pediu para seguir e postar no DEV o guia `/pages/guia-nike-mind-001-002`.

## Escopo executado

- Publicado apenas no tema DEV `155065450718` — `lk-new-theme/dev`.
- `role` verificado antes do write: `unpublished`.
- Asset alterado no DEV: `sections/main-page.liquid`.
- Branch condicional por `page.handle == 'guia-nike-mind-001-002'`.
- Página/produção global Shopify **não alterada**.
- Sem alteração de preço, estoque, produto, coleção, apps, campanha, Merchant, Klaviyo ou checkout.

## Preview DEV

https://lk-sneakerss.myshopify.com/pages/guia-nike-mind-001-002?_ab=0&_fd=0&_sc=1&preview_theme_id=155065450718&lkgoc_dev=20260606T1012Z

Obs.: para forçar render do dev theme via terminal/browser sem cookie prévio, usar `_ab=0&_fd=0&_sc=1&preview_theme_id=155065450718`.

## Readback Shopify DEV

```json
{
  "theme_id": 155065450718,
  "theme_name": "lk-new-theme/dev",
  "theme_role": "unpublished",
  "asset_key": "sections/main-page.liquid",
  "after_sha256": "0cbfe9434e8dbd3543f9885de36494d22dbe77120c88c46a175bde6e8081ff8b",
  "readback_sha256": "0cbfe9434e8dbd3543f9885de36494d22dbe77120c88c46a175bde6e8081ff8b",
  "readback_matches": true,
  "has_nike_mind_branch": true,
  "has_lk_goc_guide": true,
  "has_parent_wrapper_fix": true,
  "candidate_branch_has_lk_204l": false,
  "faq_schema_count_in_branch": 1
}
```

## QA storefront DEV

```json
{
  "url": "https://lk-sneakerss.myshopify.com/pages/guia-nike-mind-001-002?_ab=0&_fd=0&_sc=1&preview_theme_id=155065450718&lkgoc_dev=20260606T1012Z",
  "status": 200,
  "theme_id_marker": true,
  "has_lk_goc_guide": true,
  "has_parent_wrapper_fix": true,
  "legacy_source_in_main": false,
  "legacy_source_total": 2,
  "faq_schema_total": 1,
  "details_count_main": 8,
  "product_card_count_main": 12,
  "external_card_count_main": 9,
  "liquid_error": false,
  "something_wrong": true,
  "h1s": [
    "Nike Mind 001/002: conforto sensorial, design e escolha certa"
  ],
  "cta_collection": true,
  "details_count_main_precise": 8,
  "product_card_count_main_precise": 8,
  "external_card_count_main_precise": 3,
  "something_wrong_in_main": false,
  "liquid_error_in_main": false
}
```

Notas QA:
- `legacy_source_total: 2` aparece fora do main por CSS/overrides globais no head; no main do guia novo está `false`.
- `something_wrong: true` vem de script/app global; no main do guia está `false`.

## Produção intocada

```json
{
  "url": "https://lksneakers.com.br/pages/guia-nike-mind-001-002?lkgoc_prod_check=20260606T1014Z",
  "status": 200,
  "production_has_new_lkgoc": false,
  "production_has_current_legacy": true,
  "h1s": [
    "Guia Nike Mind 001/002 | LK Sneakers",
    "Guia Nike Mind 001/002 | LK Sneakers"
  ]
}
```

## Evidência visual

- Desktop screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/nike-mind-guide-page-lkgoc-dev-20260606T100703Z/screenshots/desktop.png` (542403 bytes)
- Mobile screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/nike-mind-guide-page-lkgoc-dev-20260606T100703Z/screenshots/mobile.png` (280768 bytes)

## Rollback DEV

Restaurar:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/nike-mind-guide-page-lkgoc-dev-20260606T100703Z/before.sections__main-page.liquid`

para o asset DEV:

- `themes/155065450718/assets/sections/main-page.liquid`

## Próximo gate

Se Lucas aprovar visualmente o preview DEV: promover para produção com approval explícita, backup da página/tema, readback, validação pública e receipt.
