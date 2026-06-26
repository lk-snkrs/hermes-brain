# LK GMC price regular micro-pilot — 2026-05-14

Status: `pilot_completed_needs_review`

## Scope
- Até 5 IDs online `regular_price_stale`.
- Campo alterado: `productAttributes.price` somente.
- Excluído: `salePrice`, settings, feeds, Shopify, Tiny, campanhas.
- DataSource: `10636492695`

## Result
- selected_count: `5`
- execution_counts: `{'patched_price_only': 5}`
- verify_content_matches: `0`
- verify_merchant_v1_matches: `0`
- status_issue_counts_after: `{'price_updated': 15}`

## IDs
- `online:pt:BR:01424-002-2`: `5999.90` → `8999.99`
- `online:pt:BR:553558140-7`: `1499.99` → `1799.99`
- `online:pt:BR:AQ9129-170-5`: `2599.99` → `2749.99`
- `online:pt:BR:AQ9129-170-7`: `2599.99` → `3349.99`
- `online:pt:BR:AQ9129-170-9`: `2599.99` → `3349.99`

## Rollback/progress privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-price-regular-micro-pilot-rollback-20260514T212618Z.json`
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-price-regular-micro-pilot-progress-20260514T212618Z.jsonl`

## Not performed
- salePrice write
- automatic item update settings change
- feed fetch/upload
- Shopify write
- Tiny write
- campaign/message/send
- bulk price write
