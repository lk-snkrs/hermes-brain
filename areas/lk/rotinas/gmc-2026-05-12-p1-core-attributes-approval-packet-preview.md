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

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: escolher entre executar todos os core attrs com `availability` do snapshot Shopify, dividir em dois pacotes, ajustar o escopo ou bloquear a execução.
- Ação proposta se aprovado: atualizar somente os campos core indicados (`title`, `link`, `imageLink`, `price`, `availability`) para os 1627 IDs exatos do preview, respeitando o caveat Tiny.

### Target / owner
- Target: Google Merchant Center / produtos online LK Sneakers nos 1627 product IDs exatos do preview.
- Owner operacional: LK Growth / GMC, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: aplicar os core attrs calculados a partir de evidência Shopify/Data Spine por SKU ativo exato.
- Pode fazer: criar snapshot/rollback, executar batch estreito nos campos aprovados, fazer readback/status e salvar receipt.

### Risco
- Risco principal: `availability` divergir da fonte oficial Tiny; preço/link/imagem/título incorretos podem afetar Merchant e anúncios orgânicos/pagos.
- Blast radius alto pela quantidade de 1627 IDs; recomenda-se pacote menor ou separação de availability caso a aprovação não seja explícita.

### Verificação / readback
- Verificação obrigatória: Product API/statuses após delay, amostragem por campo alterado, contagem de aprovados/reprovados/bloqueados e comparação contra CSV/JSON do preview.
- Se availability não tiver fonte validada no escopo aprovado, bloquear esse campo e registrar exceção.

### Opções de aprovação
- Aprovar todos os core attrs incluindo availability do snapshot Shopify.
- Aprovar primeiro apenas `title`, `link`, `imageLink` e `price`, deixando availability para validação Tiny separada.
- Aprovar micro-piloto com subconjunto de IDs.
- Bloquear e pedir novo preview.

### Secret hygiene
- Usar credenciais Google/Merchant/Shopify somente via Doppler/wrapper seguro; não imprimir tokens, refresh tokens, passwords, service-account JSON ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
