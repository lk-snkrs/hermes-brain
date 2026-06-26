# LK GMC P1 Attribute Completion — Wave4 Timeout-Recovered Verify, 2026-05-13

Status: `gmc_p1_attribute_wave4_aggressive_nonprice_apply_timeout_recovered_verified`

## Resultado
- Planned records: 228
- Progress rows: 228
- Execution: {'updated_wave4_aggressive_nonprice_attrs': 228}
- Verify: {'verified_product_get': 228}
- Match esperado: 228/228
- Required rows after: 45
- Required instances after: 67
- Counts after: {'price': 35, 'size': 32}

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-executor-rollback-20260513T141552Z.json`

## Não executado na recuperação
- merchant_write_in_recovery_script
- merchant_price_update
- merchant_delete
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
