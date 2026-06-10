# LK Shopify all-orders ingest — HMAC fix e verificação

Data: 2026-06-09
Perfil executor: lk-ops
Escopo aprovado: receber todos os pedidos Shopify via `orders/create`, mantendo automação pós-compra POS filtrada/separada.

## Decisão operacional

- `orders/create` deve ir para uma rota record-only de ingestão geral: `lk-shopify-orders-ingest`.
- `orders/paid` POS continua na rota de automação existente: `lk-shopify-pos-restock`.
- A automação atual de WhatsApp pós-compra permanece filtrando apenas POS pago/ativo.

## Mudanças aplicadas

1. Rota dinâmica Hermes `lk-shopify-orders-ingest` alinhada com o HMAC Vercel→Hermes:
   - `kind: script`
   - `run_script: true`
   - `events: [orders/create]`
   - script: `/opt/data/scripts/lk_shopify_orders_ingest.py`
   - segredo gravado no credential store de subscriptions a partir do Doppler sem impressão de valor.

2. `config.yaml` limpo para manter a rota POS apenas com:
   - `events: [orders/paid]`

3. Shopify webhook readback confirmado:
   - `orders/paid` → `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
   - `orders/create` → `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-orders-ingest`

## Evidência de verificação

Probe assinado Shopify → Vercel → Hermes:

- `orders/create` / `lk-shopify-orders-ingest`:
  - HTTP: `200`
  - status: `recorded`
  - action: `record_only`
  - `values_printed: false`

- `orders/paid` / `lk-shopify-pos-restock`:
  - HTTP: `200`
  - status: `ignored`
  - reason: `not_paid_active_pos_order`
  - esperado para payload de teste web/não elegível.

Ledger local:

- O probe `orders/create` foi confirmado como gravado no ledger sanitizado.
- Entrada fake `#HERMES_*` removida depois da verificação para não poluir o ledger operacional.

## Backups relevantes

- `/opt/data/webhook_subscriptions.json.bak-lk-orders-ingest-secret-20260609T200818Z`
- `/opt/data/config.yaml.bak-lk-orders-ingest-clean-<timestamp>`
- backup anterior de subscriptions da criação da rota: `/opt/data/webhook_subscriptions.json.bak-lk-orders-ingest-20260609T200244Z`

## Guardrails preservados

- Nenhum secret foi impresso.
- Nenhum envio WhatsApp foi disparado.
- Nenhuma alteração de estoque, Tiny, reserva ou Shopify order data foi feita além da configuração do webhook previamente autorizada.
- Pedidos web/site agora podem ser recebidos por ingestão record-only, mas não entram na automação POS.

## Estado final

Operacional:

- Todos os novos pedidos Shopify devem chegar via `orders/create` na rota `lk-shopify-orders-ingest`.
- A automação POS permanece limitada à rota `orders/paid` + filtro POS do script `lk_store_sale_restock_alert.py`.

Pendente apenas de observação natural:

- Validar próximo pedido real Shopify chegando no ledger de ingestão geral.
- Validar próxima venda POS real completando o fluxo POS pós-compra já existente.
