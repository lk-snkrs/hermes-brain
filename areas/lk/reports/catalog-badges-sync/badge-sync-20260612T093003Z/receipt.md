# LK catalog badges sync receipt

Data: 2026-06-12T09:35:56.377139+00:00

## Evidência
- Produtos atualizados: `113`
- Coleções alvo: `141`
- GA4: `{"available": true, "rows_total": 2387, "property": "348553567"}`

## Interpretação
- Tags padronizadas para `NEW` e `BEST SELLER` aplicadas com sucesso.

## Preview
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260612T093003Z/rollback-snapshot.json`
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260612T093003Z/receipt.json`

## Risco
- Mudança externa em Shopify foi aplicada; preservar snapshot para rollback.

## Rollback
- Usar `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260612T093003Z/rollback-snapshot.json` para restaurar `current_tags` por produto.