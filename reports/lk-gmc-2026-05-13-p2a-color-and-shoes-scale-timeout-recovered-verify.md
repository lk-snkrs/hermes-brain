# LK GMC P2A — Color + Shoes scale timeout-recovered verify, 2026-05-13

Status: `timeout_recovered_with_mismatches`

## Resultado
- Progress rows: 1418
- Execution: {'patched_color_v1': 1, 'patched_p2a_shoes_v1': 1417}
- Verify: {'verified_merchant_product_get': 1418}
- Match esperado: 1407/1418
- Productstatuses after: 23253
- Required attr rows after: 11
- Required attr counts after: {'color': 11}
- Top issues after: {'price_updated': 1029, 'strikethrough_price_updated': 507, 'restricted_gtin': 102, 'landing_page_error': 63, 'missing_item_attribute_for_product_type': 22, 'availability_updated': 9, 'image_single_color': 8, 'image_link_broken': 8, 'reserved_gtin': 6, 'condition_updated_from_detected': 4, 'restricted_nfs_policy_violation': 4, 'coupon_gtin': 3, 'multiple_sizes': 2, 'pause_expired': 2, 'image_too_small_for_high_resolution': 2}

## Recuperação
- Processo original falhou na sondagem final por ACCESS_TOKEN_EXPIRED; este verificador usou token novo e não reaplicou nada.

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2a-color-and-shoes-scale-rollback-20260513T171051Z.json`

## Não executado
- no_writes
- no_reapply
- no_delete
- no_shopify_tiny_db_campaign_message_changes
