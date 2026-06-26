# LK GMC Orphan Ranking, 2026-05-12

Status: `gmc_orphan_risk_ranker_ready_readonly`

## Resumo executivo
- Produtos Merchant lidos: 25578
- Fila P0/P1 total: 4671
- P0: 2383
- P1: 2288
- Canais na fila: {'online': 3369, 'local': 1302}

## Buckets principais
- valid_online_listing: 10571
- valid_local_listing: 10336
- online_unmatched_possible_stale: 2415
- online_identifier_mismatch: 954
- local_identifier_mismatch: 847
- local_unmatched_after_normalization: 455

## Interpretação
- `valid_local_listing`: local preservado; bateu com Shopify depois de normalizar `LIA_`.
- `identifier_mismatch`: parece produto real, mas ID/SKU/GTIN precisa saneamento antes de ação.
- `unmatched_possible_stale` / `unmatched_after_normalization`: maior risco de item antigo, errado ou fonte inconsistente.
- Nada foi escrito ou removido; isso é ranking de investigação/aprovação.

## Próximo bloco seguro recomendado
- Abrir amostras P0/P1 por bucket, cruzar com Shopify/Tiny e gerar pacote de correção ou limpeza com rollback.

## Não executado
- merchant_product_delete
- merchant_product_update
- feed_update
- shopify_write
- database_write
- campaign_or_external_send
- local_inventory_disable
