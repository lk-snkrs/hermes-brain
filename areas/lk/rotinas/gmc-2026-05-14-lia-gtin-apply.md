# LK GMC Local/LIA GTIN Apply — 2026-05-14

Gerado em: `2026-05-14T18:30:24.440607+00:00`

## Resultado
- Status: `completed_with_readback_mismatch`
- Aprovados: `34`
- Piloto: `5`; escala: `29`
- Execução: `{'skipped_already_matching': 5, 'patched': 29}`
- Readback piloto: `{'match': 5}`
- Readback escala: `{'match': 27, 'mismatch': 2}`
- Productstatuses finais com issue alvo GTIN: `4`; códigos `{'reserved_gtin': 4}`

## Escopo executado
- Content API `products.insert`/upsert em product IDs exatos `local:pt:BR:LIA_*`.
- Recurso atual preservado; campo alterado: somente `gtin`.
- Piloto 5 verificado antes de aplicar os 29 restantes.

## Auditoria privada
- Rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-lia-gtin-rollback-20260514T182410Z.json`
- Progresso: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-lia-gtin-progress-20260514T182410Z.jsonl`

## Não executado
- Shopify write
- Tiny write
- POS/local inventory config change
- feed fetch/upload
- price update
- availability update
- title/category/image update
- campaign/message/send
- supplier/contact/purchase
