# LK GMC residual approved executor — 2026-05-14

Status: `completed_with_errors`

## Summary
- planned_actions: `279`
- planned_by_kind: `{'price_saleprice_shopify_variant': 251, 'missing_attribute_completion': 14, 'image_link_repair': 5, 'landing_page_stale_delete': 9}`
- execution: `{'patched': 254, 'error': 16, 'deleted_or_absent': 9}`
- verify: `{'read': 270, 'absent_or_get_failed': 9}`
- target_issue_instances_after: `{'price_updated': 915, 'strikethrough_price_updated': 231, 'missing_item_attribute_for_product_type': 44, 'restricted_gtin': 100, 'reserved_gtin': 6, 'image_single_color': 8, 'landing_page_pending_crawl': 5, 'image_link_broken': 3}`
- target_issue_instances_after_on_acted_ids: `{'price_updated': 453, 'missing_item_attribute_for_product_type': 43, 'strikethrough_price_updated': 48, 'image_single_color': 8, 'landing_page_pending_crawl': 5, 'image_link_broken': 3}`
- productstatuses_read: `23259`

## Snapshots
- Rollback privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-executor-rollback-20260514T155630Z.json`
- Progress privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-executor-progress-20260514T155630Z.jsonl`

## Não executado
- Shopify write
- Tiny write
- campaign/message/send
- feed fetch/upload
- price policy invention; prices copied only from exact Shopify variant
