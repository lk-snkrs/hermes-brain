# Production merge — Nike Mind LKGOC

## Status

- Merge no tema production/main: **feito e com readback OK**.
- Page body global: **atualizado via Page API e readback com conteúdo LKGOC**.
- QA por storefront público normal: **ainda retorna cache/versão antiga** no momento do teste.

## Production theme write

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`
- Asset: `sections/main-page.liquid`
- Source DEV SHA: `0cbfe9434e8dbd3543f9885de36494d22dbe77120c88c46a175bde6e8081ff8b`
- Production after SHA: `0cbfe9434e8dbd3543f9885de36494d22dbe77120c88c46a175bde6e8081ff8b`
- Readback matches source: `True`

## Page body write

- Page ID: `127519064286`
- Handle: `guia-nike-mind-001-002`
- Current Admin body contains `lk-goc-guide--guia-nike-mind-001-002` and no `lk-source-page--nike-mind-redo`.

## Public QA latest

```json
{
  "url": "https://lksneakers.com.br/pages/guia-nike-mind-001-002?final_prod_qa=20260606T1024Z_2",
  "status": 200,
  "has_lk_goc_main": false,
  "legacy_source_in_main": true,
  "lk_204l_in_main": true,
  "lk_lkgoc_in_main": false,
  "faq_schema_total": 1,
  "details_count_main_precise": 8,
  "product_card_count_main_precise": 0,
  "external_card_count_main_precise": 0,
  "liquid_error_in_main": false,
  "something_wrong_in_main": false,
  "h1s": [
    "Guia Nike Mind 001/002 | LK Sneakers",
    "Guia Nike Mind 001/002 | LK Sneakers"
  ],
  "html_has_touch": false,
  "main_sha256": "f307f892c45cb8090c2a7c1ab79e9e6d7dd3fe1cbcea9916cd69024cc605c425"
}
```

## Interpretation

Admin/API production state is updated, but normal storefront URL is still serving an old cached render. Preview/theme-forced routes show the production theme branch correctly; public normal route had not invalidated yet during polling.

## Rollback

- Theme rollback file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/nike-mind-guide-page-lkgoc-prod-merge-20260606T101421Z/production-before.sections__main-page.liquid`
- Page body rollback file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/nike-mind-guide-page-body-prod-publish-20260606T101740Z/page-before.body_html`
