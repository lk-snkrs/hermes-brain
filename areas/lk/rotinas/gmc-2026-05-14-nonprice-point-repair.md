# LK GMC non-price point repair — 2026-05-14

Generated: `2026-05-14T20:31:41.277722+00:00`

## Resultado
- Status: `completed`
- triage_nonprice_products: `28`
- planned_actions: `27`
- planned_by_kind: `{'clear_bad_additional_image_links': 5, 'online_color_completion': 22}`
- pending_records: `1`
- pending_by_reason: `{'landing_page_error_but_shopify_product_active_or_unknown_public_probe_needed': 1}`
- execution_counts: `{'patched_content_api': 2, 'patched_productinputs_v1': 25}`
- verify_counts: `{'match': 18, 'mismatch': 9}`
- final_target_issue_counts_on_acted_ids: `{}`
- acted_rows_with_target_issue_after: `0`

## Auditoria privada
- Rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-nonprice-point-repair-rollback-20260514T202719Z.json`
- Progress: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-nonprice-point-repair-progress-20260514T202719Z.jsonl`

## Bloqueados/pending
- `online:pt:BR:GW3773-39` — landing_page_error_but_shopify_product_active_or_unknown_public_probe_needed

## Não executado
- price/salePrice write
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
- bulk reapply
- new image asset generation or product-photo invention
