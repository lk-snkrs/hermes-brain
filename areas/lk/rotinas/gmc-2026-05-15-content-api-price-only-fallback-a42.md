# LK GMC — Content API price-only fallback A42

Gerado em: `2026-05-15T21:27:42.249904+00:00`
Status: `completed_needs_review`

## Escopo
- Content API `products.insert`/upsert em 42 produtos `source=api`.
- Campo comercial alterado: `price` somente.
- `salePrice`/strikethrough fora do escopo.

## Resultado
- Execução: `{'content_api_upserted_price_only': 42}`
- Verificados com preço esperado: `1/42`
- Mismatches: `41`

## Rollback/progresso privado
- Rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-15-content-api-price-only-fallback-a42-rollback-20260515T212418Z.json`
- Progress: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-15-content-api-price-only-fallback-a42-progress-20260515T212418Z.jsonl`

## Artefatos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-content-api-price-only-fallback-a42.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-content-api-price-only-fallback-a42.csv`

## Não executado
- salePrice/strikethrough update
- Shopify write
- Tiny write
- feed fetch/upload/fetchNow
- campaign/message/WhatsApp/supplier/customer contact
