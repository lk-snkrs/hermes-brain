# LK GMC P1 Core Attributes Root-Cause Probe, 2026-05-12

Status: `gmc_p1_core_attributes_root_cause_probe_readonly_ready`

## Resumo executivo
- Linhas core-attr P1 rechecadas: 0
- Candidatas a approval packet futuro: 0
- Recheck/no-write por possível inconsistência productstatus vs product resource: 0
- Fonte incompleta/manual: 0
- Buckets: {}
- Core attrs faltantes no payload Merchant segundo status/payload: {}
- Core attrs que Shopify local consegue suprir: {}
- Writes executados: 0

## Veredito
- Probe read-only concluído. O próximo passo seguro é gerar um approval packet menor somente para linhas onde Merchant está sem core attrs e Shopify/Data Spine tem evidência de SKU ativo exato para todos os campos faltantes.

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
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attributes-root-cause-probe.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attributes-root-cause-probe.csv`
