# LK GMC GTIN relaxed same-product repair — 2026-05-14

Status: `completed`

## Summary
- gtin_issue_rows_seen: `44`
- planned_online_patches: `6`
- execution: `{'patched': 6}`
- verify: `{'mismatch': 6}`
- skipped_by_reason: `{'local_lia_not_patched_in_this_wave': 30, 'no_safe_style_sku': 8}`

## Rule
- Same product/style SKU is sufficient; exact size GTIN match is not required per Lucas voice approval.
- GTINs starting with 2/02/04 or failing check digit were rejected.

## Snapshots
- Rollback privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-gtin-relaxed-same-product-repair-rollback-20260514T172829Z.json`
- Progress privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-gtin-relaxed-same-product-repair-progress-20260514T172829Z.jsonl`

## Não executado
- local/LIA GTIN patch (avoided POS/local inventory data-source overlay)
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
- price/title/image/availability changes
