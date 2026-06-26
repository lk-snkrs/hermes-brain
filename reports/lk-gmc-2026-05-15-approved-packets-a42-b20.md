# LK GMC — Approved packets A42/B20 execution

Gerado em: `2026-05-15T20:51:39.954369+00:00`
Status: `applied_needs_review_or_delayed_propagation`

## Escopo aprovado
- Pacote A: 42 IDs `price-only`, campo `productAttributes.price` somente.
- Pacote B: 20 IDs Shopify DRAFT/404 para delete/suppress no Merchant.
- Aprovação: `aprovo todos` no Telegram.

## Resultado
- A execução: `{'patched_price_only_v1': 42}`
- A Merchant API v1 match: `0/42`
- A Content API match: `0/42`
- B execução: `{'deleted': 20}`
- B ausente em products.list: `20/20`
- B ausente em productstatuses.list: `20/20`

## Rollback/progresso privado
- Rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-15-approved-packets-a42-b20-rollback-20260515T204322Z.json`
- Progress: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-15-approved-packets-a42-b20-progress-20260515T204322Z.jsonl`

## Artefatos públicos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-approved-packets-a42-b20.json`
- CSV A: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-approved-packets-a42-b20-price-a42.csv`
- CSV B: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-approved-packets-a42-b20-draft404-b20.csv`

## Não executado
- salePrice/strikethrough update
- Shopify write/publish
- Tiny write
- feed fetch/upload/fetchNow
- campaign/message/WhatsApp/supplier/customer contact
