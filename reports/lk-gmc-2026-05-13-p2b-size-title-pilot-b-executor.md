# LK GMC P2B/B Size-in-title Pilot Executor — 2026-05-13

Status: `p2b_size_title_pilot_b_apply_verified`

## Escopo
- API: Merchant API v1 ProductInputs PATCH.
- Campo: `productAttributes.title` somente.
- Data source: `accounts/*/dataSources/10636492695`
- Sem alteração de título visível da Shopify.

## Resultado
- Selecionados: 100
- Execution: {'patched_p2b_size_title_pilot_b_v1': 100}
- Verify: {'verified_merchant_product_get': 100}
- Match esperado: 100/100

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2b-size-title-pilot-b-executor-rollback-20260513T172833Z.json`

## Não executado
- shopify_write
- shopify_title_update
- handle_update
- description_update
- price_update
- availability_update
- googleProductCategory_update
- productTypes_update
- merchant_delete
- tiny_write
- database_write
- feed_fetch_or_upload
- message_or_campaign_send
