# Packet pronto para aprovação — Envio/execução P0 (20260610TP0SENDREADY)

> SUPERSEDED_BY_20260610TP0NOTIONJULIO: Lucas corrigiu o fluxo em 2026-06-10T20:35:23Z. Compras LK entram no Notion para Júlio executar; não usar este packet para cotação/fornecedor.

- Data/hora UTC: 2026-06-10T20:16:58Z
- Status: `DRAFT_ONLY_NOT_SENT`
- Origem: execução local/Brain-only do preview P0 `20260610TP0EXECLOCAL`
- Interpretação segura do comando `SEGUIR`: preparar o próximo packet, **não enviar**, porque canal/destinatário/ação externa ainda não foram escopados.

## Itens P0

- `205759 610-8` — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 41 — qtd **4** — saldo Tiny LK observado **0.0**
- `FQ1180001-11` — Tênis Yuto Horigome x Nike SB Dunk Low Azul — tam. 44 — qtd **3** — saldo Tiny LK observado **0.0**
- `IH2612-1` — Tênis adidas Handball Spezial Sporty & Rich Brown Marrom — tam. 35 — qtd **3** — saldo Tiny LK observado **0.0**
- `205759 610-7` — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 40 — qtd **3** — saldo Tiny LK observado **0.0**

## Mensagem pronta — fornecedor/cotação

```text
Olá! Temos uma lista de reposição P0 para cotação/validação. Você consegue verificar disponibilidade e custo para os itens abaixo?

- Crocs Classic Clog x The Cars Lightning McQueen Vermelho — SKU 205759 610-8 — tamanho 41 — quantidade 4
- Tênis Yuto Horigome x Nike SB Dunk Low Azul — SKU FQ1180001-11 — tamanho 44 — quantidade 3
- Tênis adidas Handball Spezial Sporty & Rich Brown Marrom — SKU IH2612-1 — tamanho 35 — quantidade 3
- Crocs Classic Clog x The Cars Lightning McQueen Vermelho — SKU 205759 610-7 — tamanho 40 — quantidade 3

Obs.: isto é pedido de validação/cotação. Não reservar/confirmar compra sem aprovação final.
```

## Mensagem pronta — operador interno

```text
P0 Stock OS — itens aprovados no preview local para decisão de reposição/transferência. Favor validar canal/destino antes de qualquer execução:

- Crocs Classic Clog x The Cars Lightning McQueen Vermelho — SKU 205759 610-8 — tamanho 41 — quantidade 4 — saldo Tiny LK observado 0.0
- Tênis Yuto Horigome x Nike SB Dunk Low Azul — SKU FQ1180001-11 — tamanho 44 — quantidade 3 — saldo Tiny LK observado 0.0
- Tênis adidas Handball Spezial Sporty & Rich Brown Marrom — SKU IH2612-1 — tamanho 35 — quantidade 3 — saldo Tiny LK observado 0.0
- Crocs Classic Clog x The Cars Lightning McQueen Vermelho — SKU 205759 610-7 — tamanho 40 — quantidade 3 — saldo Tiny LK observado 0.0

Guardrail: não alterar Tiny/Shopify, não prometer pronta entrega, não enviar ao cliente sem aprovação final.
```

## Aprovações possíveis

- supplier_send: `Aprovo enviar para [fornecedor/canal/destinatário] a mensagem do packet 20260610TP0SENDREADY, com 4 SKUs e quantidades 4/3/3/3, sem write Tiny/Shopify, sem compra automática, e registrar receipt.`
- internal_operator_send: `Aprovo enviar para [operador/canal/destinatário] a mensagem interna do packet 20260610TP0SENDREADY, com 4 SKUs e quantidades 4/3/3/3, sem write Tiny/Shopify, sem compra/transferência automática, e registrar receipt.`
- execute_transfer_or_purchase: `Aprovo executar [compra/transferência] para os SKUs [listar] nas quantidades [listar], via [canal/destinatário], sem write Tiny/Shopify, com receipt e readback.`

## Guardrails

- tiny_write: 0
- shopify_write: 0
- writes_externos: 0
- external_send: 0
- purchase_executed: 0
- transfer_executed: 0
- availability_claim_allowed: 0
- public_availability_safe: 0
- cron_webhook_bot_runtime_new: 0

## Artefatos

- JSON: `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-send-ready-draft-20260610TP0SENDREADY.json`
- CSV itens: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-send-ready-draft-items-20260610TP0SENDREADY.csv`
