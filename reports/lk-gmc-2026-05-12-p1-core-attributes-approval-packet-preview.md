# LK GMC P1 Core Attributes Approval Packet Preview, 2026-05-12

Status: `gmc_p1_core_attributes_approval_packet_preview_ready_no_execution`

## Resumo executivo
- Candidatos exatos no packet preview: 1627
- Bloqueados no packet preview: 0
- Campos propostos: {'availability': 1627, 'imageLink': 1627, 'link': 1627, 'price': 1627, 'title': 1627}
- Linhas com availability proposta e caveat Tiny: 1627
- Writes executados: 0

## Veredito
- Packet preview pronto, mas ainda sem autorização de execução por este artefato. O pacote é tecnicamente estreito: exact online product IDs e core attrs calculados de evidência Shopify/Data Spine por SKU ativo exato.
- Caveat importante: `availability` é atributo obrigatório no Merchant, mas estoque verdadeiro da LK é Tiny. Recomendo escolher explicitamente entre executar todos os core attrs com availability do snapshot Shopify, ou partir em dois pacotes: title/link/imageLink/price primeiro e availability após validação Tiny.

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
- rollback_snapshot_creation
- pos_or_local_inventory_setting_change
- campaign_or_external_send

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attributes-approval-packet-preview.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attributes-approval-packet-preview.csv`
