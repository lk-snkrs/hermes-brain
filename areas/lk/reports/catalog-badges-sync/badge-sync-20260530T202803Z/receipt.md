# LK catalog badges sync receipt

Data: 2026-05-30T20:28:26.482996+00:00

## Evidência
- Produtos atualizados: `8`
- Coleções alvo: `1`
- GA4: `{"available": true, "rows_total": 2425, "property": "348553567"}`

## Interpretação
- Tags padronizadas para `NEW` e `BEST SELLER` aplicadas com sucesso.

## Preview
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T202803Z/rollback-snapshot.json`
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T202803Z/receipt.json`

## Risco
- Mudança externa em Shopify foi aplicada; preservar snapshot para rollback.

## Rollback
- Usar `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T202803Z/rollback-snapshot.json` para restaurar `current_tags` por produto.