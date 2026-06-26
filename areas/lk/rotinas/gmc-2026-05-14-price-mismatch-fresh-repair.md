# LK GMC price mismatch fresh repair — 2026-05-14

Status: `completed_with_review`

## Summary
- input_mismatches: `152`
- triage_counts: `{'needs_patch_price': 62, 'no_action_current_matches_shopify': 42, 'needs_patch_sale': 43, 'review_clear_salePrice_no_shopify_sale': 5}`
- actions_count: `105`
- execution_counts: `{'patched': 105}`
- verify_counts: `{'read': 105}`
- verify_matches: `0`
- verify_mismatches: `105`

## Paths
- Rollback privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-price-mismatch-fresh-repair-rollback-20260514T195302Z.json`
- Progresso privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-price-mismatch-fresh-repair-progress-20260514T195302Z.jsonl`

## Não executado
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
- bulk reapply
- salePrice clearing for no-Shopify-sale rows
