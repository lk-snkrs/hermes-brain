# LK GMC residual approved resume/verify — 2026-05-14

Status: `completed_with_verify_mismatches`

## Summary
- source_progress_lines: `182`
- source_execution_counts: `{'patched': 180, 'error': 2}`
- source_kind_counts: `{'price_saleprice_shopify_variant': 160, 'missing_attribute_completion': 17, 'image_link_repair': 5}`
- local_repairs: `{'local_content_upsert_patched': 2}`
- verify_counts: `{'read': 182}`
- verify_matches: `30`
- verify_mismatches: `152`
- productstatuses_read: `23277`
- target_issue_instances_after: `{'price_updated': 915, 'strikethrough_price_updated': 228, 'missing_item_attribute_for_product_type': 44, 'image_single_color': 8, 'image_link_broken': 3, 'landing_page_error': 3}`
- target_issue_instances_after_on_acted_ids: `{'price_updated': 450, 'strikethrough_price_updated': 48, 'image_single_color': 8, 'image_link_broken': 3}`
- acted_ids_with_target_issue_after: `157`

## Paths
- Progress fonte: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-executor-progress-20260514T190600Z.jsonl`
- Rollback fonte: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-executor-rollback-20260514T190600Z.json`
- Local repair progress: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-resume-verify-local-repair-20260514T191747Z.jsonl`

## Não executado
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
- bulk reapply after timeout
