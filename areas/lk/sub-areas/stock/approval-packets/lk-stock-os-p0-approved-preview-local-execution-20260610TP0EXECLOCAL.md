# Execução local — Preview P0 aprovado (20260610TP0EXECLOCAL)

- Data/hora UTC: 2026-06-10T20:06:12Z
- Área/profile: LK / Estoque Loja Física (`lk-stock`)
- Canal aprovado: Local/Brain apenas
- Pedido aprovado: executar preview P0 para os 4 SKUs, quantidades 4/3/3/3, sem write Tiny/Shopify, com receipt
- Fonte: preview B→A já reconfirmado live/read-only em Tiny/Shopify; depósito Tiny `LK | CONTROLE ESTOQUE`

## Resultado local registrado

- 205759 610-8 — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 41: qtd aprovada preview **4**; saldo Tiny LK **0.0**; status `APPROVED_PREVIEW_REGISTERED_LOCAL_ONLY`
- FQ1180001-11 — Tênis Yuto Horigome x Nike SB Dunk Low Azul — tam. 44: qtd aprovada preview **3**; saldo Tiny LK **0.0**; status `APPROVED_PREVIEW_REGISTERED_LOCAL_ONLY`
- IH2612-1 — Tênis adidas Handball Spezial Sporty & Rich Brown Marrom — tam. 35: qtd aprovada preview **3**; saldo Tiny LK **0.0**; status `APPROVED_PREVIEW_REGISTERED_LOCAL_ONLY`
- 205759 610-7 — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 40: qtd aprovada preview **3**; saldo Tiny LK **0.0**; status `APPROVED_PREVIEW_REGISTERED_LOCAL_ONLY`

## Totais

- SKUs: 4
- Quantidade total aprovada no preview local: 13

## Guardrails

- tiny_write: 0
- shopify_write: 0
- writes_externos: 0
- purchase_executed: 0
- transfer_executed: 0
- external_send: 0
- availability_claim_allowed: 0
- public_availability_safe: 0
- cron_webhook_bot_runtime_new: 0

## Próxima aprovação necessária para sair do local

Para envio a fornecedor, operador, compra ou transferência real, exigir aprovação nova com canal/destinatário/conteúdo/quantidade. Este artefato não enviou nada e não alterou Tiny/Shopify.

## Arquivos

- JSON: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-approved-preview-local-execution-20260610TP0EXECLOCAL.json`
- CSV: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-approved-preview-local-execution-20260610TP0EXECLOCAL.csv`
