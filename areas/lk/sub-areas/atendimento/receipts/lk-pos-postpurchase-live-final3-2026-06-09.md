# LK POS pós-compra — lote final dos scheduled

Data: 2026-06-09T17:05:24Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Aprovação: continuidade do escopo “seguir enviando”, mantendo lote pequeno, backup e parada no primeiro erro.

## Escopo executado

- Pedidos restantes em `scheduled`: `#147719`, `#147720`, `#147727`.
- Lote real limitado a 3.
- Guardrail: parar no primeiro erro.
- Resultado: 3 tentativas, 3 aceites pela Evolution.
- Nenhuma alteração permanente em Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.
- Wrapper temporário criado e removido após execução.

## Backup

Backup antes do lote:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-live-batch-final3-20260609T170339Z.json`

## Resultado de envio

```json
{
  "status": "batch_live_processed",
  "attempted": 3,
  "accepted_count": 3,
  "results": [
    {
      "order_name": "#147719",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    },
    {
      "order_name": "#147720",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    },
    {
      "order_name": "#147727",
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

## Evidência de ACK/reconciliação

Gateway registrou eventos `matched=1 updated=1` para os 3 hashes do lote:

```text
#147719 hash=4a4a75f42431
2026-06-09 17:03:47 status=server_ack matched=1 updated=1
2026-06-09 17:03:48 status=delivered matched=1 updated=1

#147720 hash=96fe2e00750f
2026-06-09 17:03:51 status=server_ack matched=1 updated=1
2026-06-09 17:03:52 status=delivered matched=1 updated=1

#147727 hash=877a876bf118
2026-06-09 17:03:55 status=server_ack matched=1 updated=1
2026-06-09 17:03:56 status=delivered matched=1 updated=1
```

## Estado final da fila

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 11,
    "send_error": 2,
    "read": 1,
    "server_ack": 1
  },
  "scheduled_remaining": 0,
  "live_executed_total": 9
}
```

## Observação importante — bug de ledger

O pedido `#147719` teve evento `delivered` confirmado pelo gateway, mas o status local ficou `server_ack` depois, indicando provável downgrade por ACK duplicado/fora de ordem na reconciliação. Não foi corrigido manualmente neste passo.

A correção recomendada é ajustar a reconciliação para não rebaixar status terminal/mais forte:

- `read` >= `delivered` >= `server_ack` >= `pending_delivery_confirmation`
- evento `server_ack` posterior não deve rebaixar `delivered`/`read`

## Resultado operacional

- Scheduled restantes: 0.
- Novos envios aceitos nesta etapa: 3.
- Envios reais totais registrados: 9.
- Erros finais de telefone não apto: 2 (`#147695`, `#147718`).
- Não houve ativação automática de worker/cron.

## Próximo passo recomendado

1. Corrigir bug de downgrade no reconciliador local antes de reativar worker automático.
2. Tratar `#147695` e `#147718` como telefone inválido/não apto no WhatsApp, ou revisar manualmente no Shopify/WhatsApp.
3. Corrigir o ingresso Shopify/Vercel que causou a necessidade de reconciliação manual inicial.
