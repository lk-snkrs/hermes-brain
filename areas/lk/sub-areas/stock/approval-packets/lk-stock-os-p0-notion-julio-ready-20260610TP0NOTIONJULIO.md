# Packet corrigido — Compras P0 para Notion/Júlio (20260610TP0NOTIONJULIO)

- Data/hora UTC: 2026-06-10T20:35:23Z
- Status: `NOTION_READY_LOCAL_DRAFT_NOT_WRITTEN`
- Correção do Lucas: compras da LK entram no **Notion**; **Júlio** realiza as compras. Não precisamos fazer cotação de fornecedor pelo agente.
- Packet anterior de fornecedor/cotação: `SUPERSEDED` por este fluxo.
- Notion write executado: `0` — falta database/page alvo e aprovação escopada de write Notion.

## Itens prontos para Notion

- `205759 610-8` — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 41 — qtd **4** — responsável **Júlio** — status **Aguardando Júlio**
- `FQ1180001-11` — Tênis Yuto Horigome x Nike SB Dunk Low Azul — tam. 44 — qtd **3** — responsável **Júlio** — status **Aguardando Júlio**
- `IH2612-1` — Tênis adidas Handball Spezial Sporty & Rich Brown Marrom — tam. 35 — qtd **3** — responsável **Júlio** — status **Aguardando Júlio**
- `205759 610-7` — Crocs Classic Clog x The Cars Lightning McQueen Vermelho — tam. 40 — qtd **3** — responsável **Júlio** — status **Aguardando Júlio**

## Campos sugeridos para a database Notion

- Name
- SKU
- Produto
- Tamanho
- Quantidade sugerida
- Prioridade
- Responsável
- Área
- Status
- Fonte
- Saldo Tiny LK observado
- Demanda sinalizada
- Score operacional
- Tiny ID
- Shopify Variant ID
- Handle
- Observações

## Aprovação necessária para escrever no Notion

`Aprovo adicionar no Notion de compras da LK para o Júlio os 4 itens do packet 20260610TP0NOTIONJULIO, quantidades 4/3/3/3, sem write Tiny/Shopify, e registrar receipt.`

## Guardrails

- notion_write: 0
- tiny_write: 0
- shopify_write: 0
- supplier_contact: 0
- external_send: 0
- purchase_executed: 0
- transfer_executed: 0
- public_availability_safe: 0
- cron_webhook_bot_runtime_new: 0

## Artefatos

- JSON: `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-notion-julio-ready-20260610TP0NOTIONJULIO.json`
- CSV import Notion: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-notion-julio-import-20260610TP0NOTIONJULIO.csv`
