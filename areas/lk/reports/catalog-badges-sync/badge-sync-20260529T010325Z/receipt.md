# LK catalog badges sync receipt

Data: 2026-05-29T01:13:41.228973+00:00

## Evidência
- Produtos atualizados: `484`
- Coleções alvo: `48`
- GA4: `{"available": true, "rows_total": 2421, "property": "348553567"}`

## Interpretação
- Tags padronizadas para `NEW` e `BEST SELLER` aplicadas com sucesso.

## Preview
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T010325Z/rollback-snapshot.json`
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T010325Z/receipt.json`

## Risco
- Mudança externa em Shopify foi aplicada; preservar snapshot para rollback.

## Rollback
- Usar `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T010325Z/rollback-snapshot.json` para restaurar `current_tags` por produto.