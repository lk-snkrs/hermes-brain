# LK POS pós-compra — pedidos POS novos não entraram na fila automática

Data: 2026-06-09T18:07:22Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Evolution API / Hermes Cron

## Achado

Shopify read-only mostrou pedidos POS novos elegíveis após a ativação, mas a fila local de pós-compra não recebeu novos jobs.

Pedidos observados no Shopify, sem PII:

- `#147731`
  - created_at: `2026-06-09T14:56:29-03:00`
  - financial_status: `paid`
  - cancelled: `false`
  - source_name: `pos`
  - app_id: `129785`
  - customer_present: `true`
  - phone_present: `true`
  - line_items: `2`, com SKU e variant_id presentes
- `#147732`
  - created_at: `2026-06-09T14:58:19-03:00`
  - financial_status: `paid`
  - cancelled: `false`
  - source_name: `pos`
  - app_id: `129785`
  - customer_present: `true`
  - phone_present: `true`
  - line_items: `2`, com SKU e variant_id presentes

## Fila local no momento da checagem

```json
{
  "jobs_total": 21,
  "scheduled_remaining": 0,
  "last_worker_run_at": "2026-06-09T18:00:44.660772+00:00",
  "last_worker_result": {
    "status": "processed",
    "live": true,
    "would_send": 0,
    "errors": 0,
    "prior_live_sends": 9
  }
}
```

## Gateway/logs

Logs recentes do gateway tinham apenas probes/ignores para `lk-shopify-pos-restock`:

```text
2026-06-09 17:28:28 LK POS restock handled ... status=ignored queued=0
2026-06-09 17:36:08 LK POS restock handled ... status=ignored queued=0
```

Não havia evento `queued` para `#147731` ou `#147732`.

## Shopify webhook registry

Shopify read-only confirmou webhook registrado:

```json
{
  "topic": "orders/paid",
  "address_host_path": "hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock",
  "format": "json"
}
```

## Interpretação

Os pedidos são elegíveis para pós-compra POS, mas o delivery real Shopify → Vercel/Hermes não apareceu nos logs locais para estes pedidos. A automação de worker/cron está rodando, mas não tem job para enviar.

## Ações pendentes

1. Backfill local controlado de `#147731` e `#147732` para a fila, com envio automático respeitando delay/guardrail, se Lucas aprovar.
2. Investigar por que o webhook Shopify registrado não entregou esses pedidos ao endpoint Hermes/Vercel.
3. Se necessário, criar rota de reconciliação read-only periódica Shopify → fila para cobrir perdas de webhook.

## O que não foi feito

- Não houve envio WhatsApp para `#147731`/`#147732`.
- Não houve write Shopify/Tiny/Chatwoot/Vercel.
- Não houve alteração em webhook remoto.
