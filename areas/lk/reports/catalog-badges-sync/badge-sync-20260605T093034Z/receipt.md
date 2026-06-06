# LK catalog badges sync receipt

Data: 2026-06-05T09:36:38.987475+00:00

## Evidência
- Produtos atualizados: `80`
- Coleções alvo: `140`
- GA4: `{"available": true, "rows_total": 2413, "property": "348553567"}`

## Interpretação
- Tags padronizadas para `NEW` e `BEST SELLER` aplicadas com sucesso.

## Preview
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260605T093034Z/rollback-snapshot.json`
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260605T093034Z/receipt.json`

## Risco
- Mudança externa em Shopify foi aplicada; preservar snapshot para rollback.

## Rollback
- Usar `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260605T093034Z/rollback-snapshot.json` para restaurar `current_tags` por produto.