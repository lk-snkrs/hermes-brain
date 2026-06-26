# LK GMC Local C/D POS/Source Validation, 2026-05-12

Status: `gmc_local_cd_pos_source_validation_readonly`

## Resumo executivo
- Residuais locais avaliados: 63
- Títulos únicos checados no Shopify live: 14
- Estados: {'old_lia_sku_replaced_by_active_shopify_product_with_replacement_local_present': 63}
- Candidatos para approval packet residual: 63
- Bloqueados para revisão manual: 0
- Merchant/Shopify/Tiny/POS/DB writes: 0

## Veredito
- O bloco POS/source reduziu a investigação a um pacote residual exato, mas não executa nada.
- Candidatos só podem virar delete/update após aprovação explícita, por product ID exato, com rollback privado.
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-pos-source-validation-rollback-snapshot.json`

## Arquivos
- JSON público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-pos-source-validation.json`
- CSV público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-pos-source-validation.csv`
- CSV privado/auditoria chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-local-cd-pos-source-validation.csv`

## Não executado
- merchant_product_delete
- merchant_product_update
- content_api_custombatch
- feed_update
- shopify_write
- tiny_write
- database_write
- local_inventory_disable
- pos_inventory_write
- campaign_or_external_send
