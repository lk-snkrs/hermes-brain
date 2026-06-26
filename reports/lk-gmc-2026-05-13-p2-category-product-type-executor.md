# LK GMC P2A Category/Product Type Executor — 2026-05-13

Status: `p2a_category_product_type_dry_run_ready`

## Escopo
- API: Merchant API v1 ProductInputs PATCH.
- Campos: `productAttributes.googleProductCategory` + `productAttributes.productTypes` somente.
- Data source: `accounts/*/dataSources/10636492695`
- Sem alterações de título, preço, disponibilidade ou produto Shopify.

## Resultado
- Candidatos totais: 2373
- Selecionados no piloto: 100
- Buckets selecionados: {'Apparel & Accessories > Shoes / Calçados': 100}
- Execution: {}
- Verify: {}
- Match esperado: 0/0

## Rollback privado
- Não criado no dry-run.

## Não executado
- title_update
- price_update
- availability_update
- merchant_delete
- shopify_write
- tiny_write
- database_write
- feed_fetch_or_upload
- message_or_campaign_send
