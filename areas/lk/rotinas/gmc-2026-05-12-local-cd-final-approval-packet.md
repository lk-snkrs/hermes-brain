# LK GMC Local C/D Final Approval Packet, 2026-05-12

Status: `gmc_local_cd_final_approval_packet_ready_no_execution`

## Resumo executivo
- Candidatos exatos: 63
- Pacotes origem: {'C_local_identifier_fix': 62, 'D_local_stale_triage': 1}
- Títulos únicos: 14
- Replacement local presente: {'has_replacement': 63}
- Guard failures: 0
- Merchant/Shopify/Tiny/POS/DB writes: 0

## O que este pacote pediria se Lucas aprovar depois
- Deletar somente os 63 IDs antigos `local:pt:BR:LIA_<old_sku>` listados no JSON/CSV.
- Preservar todas as linhas replacement `local:pt:BR:LIA_<current_sku>`.
- Não mexer em online, Shopify, Tiny, feed, POS, banco, campanha ou local channel.

## Por que estes 63 entraram
- Shopify live encontrou produto ativo pelo título exato.
- O SKU antigo não está mais entre os SKUs atuais do produto.
- Já existe linha local replacement para o SKU atual do Shopify.
- Probe Tiny anterior não encontrou `codigo` exato para o SKU antigo.

## Exemplos
- Old: `local:pt:BR:LIA_ADI-3400542-34`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-35`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-36`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-37`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-38`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-39`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ADI-3400542-40`
  - Produto: Tênis Adidas Tokyo Crew White Floral Embroidery Branco
  - Current SKUs Shopify: JQ1687, JQ1687, JQ1687, JQ1687, JQ1687
  - Replacement local: local:pt:BR:LIA_JQ1687
- Old: `local:pt:BR:LIA_ALD-8631262-OS`
  - Produto: Boné 5 Panel Aimé Leon Dore Unisphere Azul
  - Current SKUs Shopify: AIME11
  - Replacement local: local:pt:BR:LIA_AIME11
- Old: `local:pt:BR:LIA_ONI-3740254-34`
  - Produto: Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege
  - Current SKUs Shopify: 1183C123.200, 1183C123.200, 1183C123.200, 1183C123.200, 1183C123.200
  - Replacement local: local:pt:BR:LIA_1183C123.200
- Old: `local:pt:BR:LIA_ONI-3740254-35`
  - Produto: Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege
  - Current SKUs Shopify: 1183C123.200, 1183C123.200, 1183C123.200, 1183C123.200, 1183C123.200
  - Replacement local: local:pt:BR:LIA_1183C123.200

## Rollback se aprovado/executado depois
- Snapshot privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-pos-source-validation-rollback-snapshot.json`
- Restaurar recurso Merchant exato se algum item válido for removido ou houver regressão.
- Verificar old gone + replacement present após delay de consistência da Content API.

## Arquivos
- JSON público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.json`
- CSV público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.csv`
- CSV privado/auditoria chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-local-cd-final-approval-packet.csv`

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

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: aprovar, ajustar ou bloquear a remoção dos 63 IDs antigos `local:pt:BR:LIA_<old_sku>` listados no JSON/CSV público deste packet.
- Ação proposta se aprovado: deletar somente esses 63 IDs antigos no Merchant/local, preservando todos os replacements atuais já presentes.

### Target / owner
- Target: Google Merchant Center / canal local da LK Sneakers, somente os 63 IDs exatos listados neste packet.
- Owner operacional: LK Growth / GMC, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: deletar os 63 IDs antigos listados, manter replacements `local:pt:BR:LIA_<current_sku>`, gerar/readback pós-delete e receipt.
- Pode fazer: usar o snapshot/CSV indicado, executar apenas a ação aprovada e validar old gone + replacement present após delay de consistência.

### Risco
- Risco principal: remoção indevida de item local válido caso identidade/SKU esteja incorreta.
- Blast radius limitado aos 63 IDs exatos; qualquer divergência de replacement ou readback deve bloquear a execução.

### Verificação / readback
- Verificação obrigatória: readback Merchant após delay, confirmar IDs antigos ausentes, replacements presentes e zero alterações em online/Shopify/Tiny/feed/POS/banco/campanhas.
- Registrar receipt com contagens de deletados, preservados, bloqueados e divergências.

### Secret hygiene
- Usar credenciais Google/Merchant somente via Doppler/wrapper seguro; não imprimir tokens, refresh tokens, passwords, service-account JSON ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
