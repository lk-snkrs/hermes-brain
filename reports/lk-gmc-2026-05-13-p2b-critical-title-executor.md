# LK GMC P2B Critical Title Executor — 2026-05-13

Status: `p2b_critical_title_apply_verified`

## Escopo
- API: Merchant API v1 ProductInputs PATCH.
- Campo: `productAttributes.title` somente.
- Data source: `accounts/*/dataSources/10636492695`
- Sem alteração de título visível da Shopify.

## Resultado
- Selecionados: 35
- Execution: {'patched_p2b_title_v1': 34, 'failed_patch_v1': 1}
- Verify: {'verified_merchant_product_get': 34, 'not_verified_due_to_execution_status': 1}
- Match esperado: 34/35

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2b-critical-title-executor-rollback-20260513T171717Z.json`

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
