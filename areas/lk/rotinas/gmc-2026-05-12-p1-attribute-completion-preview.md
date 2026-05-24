# LK GMC P1 Attribute Completion Preview, 2026-05-12

Status: `gmc_p1_attribute_completion_preview_ready_no_execution`

## Resumo executivo
- Produtos online com required-attribute issues revisados: 2100
- Instâncias required-attribute: 10162
- Candidatos para approval packet futuro: 1583
- Bloqueados/sem evidência suficiente: 469
- Estados: {'ambiguous_missing_source_value': 48, 'blocked_no_shopify_exact_sku_match': 469, 'candidate_high_confidence_attr_preview': 60, 'candidate_medium_confidence_attr_preview_needs_review': 1523}
- Atributos faltantes por produto: {'color': 524, 'size': 1585, 'age group': 1510, 'gender': 1510, 'price': 10}
- Writes executados: 0

## Veredito
- Preview P1 pronto sem execução. A maior parte dos problemas é core attr ausente em produtos online; pode virar pacote de aprovação separado, mas ainda não deve ser aplicado automaticamente.

## Não executado
- merchant_product_delete
- merchant_product_insert
- merchant_product_update
- content_api_custombatch
- supplemental_feed_upload
- datafeed_fetchNow
- feed_update
- shopify_write
- tiny_write
- database_write
- pos_or_local_inventory_setting_change
- campaign_or_external_send

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-attribute-completion-preview.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-attribute-completion-preview.csv`
