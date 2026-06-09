# Receipt — LK POS restock backfill final — 2026-06-08

## Escopo

Finalização operacional do fluxo de alerta de recompra/reposição para vendas POS da LK Loja Física em 2026-06-08.

## Correção de rota realizada

- Rota pública Shopify → Vercel → Hermes: `lk-shopify-pos-restock`.
- Ajuste realizado em produção no Vercel `hermes-webhooks`:
  - `SHOPIFY_WEBHOOK_SECRET` alinhado para validação HMAC Shopify.
  - `HERMES_WEBHOOK_SECRET` alinhado com o segredo específico da rota Hermes local.
- Secrets não registrados neste receipt.
- Validação end-to-end segura registrada durante a execução: payload assinado non-POS retornou HTTP 200 com `status=ignored`, `reason=not_paid_active_pos_order`, `sent_count=0`, `queued_count=0`.

## Backfill POS de hoje

Pedidos POS pagos processados:

- `#147712` — 1 item.
- `#147718` — 2 itens.
- `#147719` — 2 itens.
- `#147720` — 3 itens.

Total: 8 itens.

Queue/backfill inicial:

- `queue_id`: `7c56e207525a333b`.
- `queued_count`: 8.
- Primeiro envio: item `1/8`, pedido `#147712`, SKU/modelo `1183C015-202-3`, tamanho `36`.

## Verificação final no WhatsApp

Verificação via `wacli` com ambiente correto da conta `hermes`:

- `HOME=/opt/data/home`
- `XDG_STATE_HOME=/opt/data/home/.local/state`
- `XDG_CONFIG_HOME=/opt/data/home/.config`

Mensagens encontradas no grupo `[LK] Team` (`120363367222855384@g.us`):

- Item `1/8` — 2026-06-08T20:13:01Z — pedido `#147712`.
- Item `2/8` — 2026-06-08T20:18:42Z — pedido `#147718`.
- Item `3/8` — 2026-06-08T20:19:39Z — pedido `#147718`.
- Item `4/8` — 2026-06-08T20:20:33Z — pedido `#147719`.
- Item `5/8` — 2026-06-08T20:22:11Z — pedido `#147719`.
- Item `6/8` — 2026-06-08T20:23:06Z — pedido `#147720`.
- Item `7/8` — 2026-06-08T20:24:01Z — pedido `#147720`.
- Item `8/8` — 2026-06-08T20:24:55Z — pedido `#147720`.

Todas as mensagens usam o layout final:

- `🚨 ALERTA DE REPOSIÇÃO — LK Loja`
- `📦 Item X/8`
- `📦 Estoque atual: ...`
- `Responda: ✅ #sim | ❌ #não`

## Estado final local

Verificação em `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/state.json`:

- `pending_sale_restock`: lista vazia `[]`.
- Não há item ativo/pending no responder para esse lote.

Processos ativos no momento da verificação:

- Responder: `/opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.
- Sync WhatsApp: `/opt/data/bin/wacli --account hermes sync --follow ...`.

## Observações

- Alguns itens tiveram `Estoque atual: não encontrado pelo SKU — validar manualmente`; isso é intencional/seguro e não promete disponibilidade.
- Para itens aprovados com `#sim`, o robô anotou reposição no Notion quando aplicável.
- Este receipt não contém secrets, tokens ou valores sensíveis.
