# LK GMC P1 Attribute Completion — Wave5 Timeout-Recovered Verify, 2026-05-13

Status: `gmc_p1_attribute_wave5_final_size_apply_timeout_recovered_verified`

- Planned records: 32
- Progress rows: 32
- Execution: {'updated_wave5_final_size_default': 32}
- Verify: {'verified_product_get': 32}
- Match esperado: 32/32
- Required rows after: 35
- Required instances after: 35
- Counts after: {'price': 35}

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave5-final-size-default-executor-rollback-20260513T143903Z.json`

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
