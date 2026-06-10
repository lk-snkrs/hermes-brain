# LK POS pós-compra — backfill #147731/#147732 com limite diário por cliente

Data: 2026-06-09T18:31:57Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Evolution API / Hermes Cron
Aprovação: Lucas aprovou backfill dos pedidos POS `#147731` e `#147732` pela Evolution LK Flagship, com limite de 1 envio por execução e parada em erro. Lucas também determinou limitar a uma mensagem por cliente por dia.

## Guardrail implementado

Regra nova aplicada no código e no backfill:

- máximo de 1 WhatsApp pós-compra por telefone/cliente por dia BRT;
- quando houver múltiplos pedidos POS do mesmo cliente no mesmo dia, priorizar o pedido mais recente;
- marcar os demais como `skipped_daily_limit`;
- worker também revalida o limite antes de enviar, para evitar escape por backfill/webhook duplicado.

Arquivos alterados:

- `/opt/data/scripts/lk_store_sale_restock_alert.py`
- `/opt/data/scripts/lk_pos_postpurchase_auto_worker_once.py`

Backups:

- `/opt/data/scripts/lk_store_sale_restock_alert.py.bak-daily-limit-20260609T181418Z`
- `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-daily-limit-backfill-20260609T181418Z.json`

## Testes

Executado:

```text
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/lk_pos_postpurchase_auto_worker_once.py
```

Runner simulado com dois pedidos mesmo telefone/dia:

```json
{
  "r1": "scheduled",
  "r2": "skipped_daily_limit",
  "statuses": ["pending_delivery_confirmation", "skipped_daily_limit"],
  "sent_count": 1,
  "pending_delivery_confirmation": 1,
  "errors": 0
}
```

## Backfill executado

Ordem usada: mais recente primeiro.

```json
{
  "results": [
    {
      "order_name": "#147732",
      "enqueue_status": "scheduled",
      "job_id": "12b2d2ca888e7de7",
      "send_after": "2026-06-09T18:28:19+00:00",
      "customer_day": "2026-06-09",
      "phone_hash": "ed09dd312318",
      "eligible": true
    },
    {
      "order_name": "#147731",
      "enqueue_status": "skipped_daily_limit",
      "job_id": "3dc20dca21aa8836",
      "send_after": "2026-06-09T18:26:28+00:00",
      "customer_day": "2026-06-09",
      "phone_hash": "ed09dd312318",
      "eligible": true
    }
  ]
}
```

## Envio automático

O cron das `18:30Z` enviou o job elegível.

Estado final sanitizado:

```json
{
  "jobs": [
    {
      "order_name": "#147732",
      "status": "delivered",
      "send_after": "2026-06-09T18:28:19+00:00",
      "customer_day": "2026-06-09",
      "customer_phone_hash": "ed09dd312318",
      "customer_daily_limit": false,
      "send_executed": true,
      "external_write_executed": true,
      "live_send_attempted_at": "2026-06-09T18:30:53.933036+00:00",
      "evolution_message_id_hash": "19d9076a1d7c",
      "delivered_at": "2026-06-09T18:31:00.310253+00:00"
    },
    {
      "order_name": "#147731",
      "status": "skipped_daily_limit",
      "customer_day": "2026-06-09",
      "customer_phone_hash": "ed09dd312318",
      "customer_daily_limit": true,
      "daily_limit_existing_order_name": "#147732",
      "send_executed": false,
      "external_write_executed": false
    }
  ]
}
```

Gateway confirmou para o hash do envio:

```text
server_ack message_hash=19d9076a1d7c
 delivered message_hash=19d9076a1d7c
```

## Estado agregado final

```json
{
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 13,
    "send_error": 2,
    "read": 1,
    "skipped_daily_limit": 1
  }
}
```

## Pendência separada

Ainda existe incidente de ingressão: Shopify tem webhook `orders/paid` registrado para `hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`, mas os pedidos reais `#147731/#147732` não apareceram automaticamente nos logs Hermes. O backfill resolveu o atendimento destes pedidos, mas ainda é recomendável investigar/reparar a entrega Shopify→Vercel/Hermes ou criar reconciliação periódica read-only Shopify→fila.
