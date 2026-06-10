# LK POS pós-compra — lote real aprovado `#147697` a `#147699`

Data: 2026-06-09T16:38:29Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Aprovação: Lucas respondeu “Aprovo” após pedido explícito para enviar 3 mensagens reais dos pedidos `#147697`, `#147698` e `#147699`.

## Escopo executado

- Lote real limitado a exatamente 3 pedidos aprovados.
- Pedidos: `#147697`, `#147698`, `#147699`.
- Guardrail: parar no primeiro erro HTTP/status inesperado.
- Resultado: não houve erro; 3 tentativas, 3 aceites.
- Wrapper temporário criado e removido após execução.
- Nenhuma alteração permanente em Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.

## Backup

Backup antes do lote:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-live-batch-147697-147699-20260609T163746Z.json`

## Resultado do envio

Saída sanitizada:

```json
{
  "status": "batch_live_processed",
  "attempted": 3,
  "accepted_count": 3,
  "results": [
    {
      "order_name": "#147697",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    },
    {
      "order_name": "#147698",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    },
    {
      "order_name": "#147699",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    }
  ]
}
```

## Verificação de fila

Verificação independente logo após a reconciliação:

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 9,
    "send_error": 1,
    "scheduled": 5
  },
  "live_executed_total": 5,
  "batch_items": [
    {
      "order_name": "#147697",
      "status": "delivered",
      "dry_run": false,
      "send_executed": true,
      "external_write_executed": true,
      "has_hash": true
    },
    {
      "order_name": "#147698",
      "status": "delivered",
      "dry_run": false,
      "send_executed": true,
      "external_write_executed": true,
      "has_hash": true
    },
    {
      "order_name": "#147699",
      "status": "delivered",
      "dry_run": false,
      "send_executed": true,
      "external_write_executed": true,
      "has_hash": true
    }
  ]
}
```

## Evidência de ACK/reconciliação

Gateway local registrou eventos sanitizados da rota `lk-evolution-delivery-reconciliation`:

```text
2026-06-09 16:37:53 matched=1 updated=1 status=server_ack
2026-06-09 16:37:56 matched=1 updated=1 status=server_ack
2026-06-09 16:37:57 matched=1 updated=1 status=delivered
2026-06-09 16:37:57 matched=1 updated=1 status=delivered
2026-06-09 16:37:58 matched=1 updated=1 status=server_ack
2026-06-09 16:37:59 matched=1 updated=1 status=delivered
```

Interpretação: os 3 envios foram aceitos e reconciliados como `delivered` no ledger local.

## Estado atual

- Mensagens reais enviadas nesta etapa: 3.
- Total de jobs com `send_executed=true` e `external_write_executed=true`: 5.
- Jobs ainda `scheduled`: 5.
- Job em `send_error`: 1 (`#147695`, telefone não apto segundo Evolution).
- Não houve liberação permanente de worker/cron nem flag global de envio.

## Próximo passo recomendado

Continuar apenas com aprovação explícita, em lote pequeno:

- preparar próximos 3 candidatos dentre os 5 `scheduled` restantes; ou
- parar e trabalhar a correção do ingresso Shopify/Vercel para evitar reconciliação manual recorrente; ou
- revisar o caso `#147695` manualmente antes de nova tentativa.
