# LK POS pós-compra — continuação de envios, lote parado no segundo pedido

Data: 2026-06-09T16:58:03Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Aprovação: Lucas disse “Seguir enviando”. Interpretação operacional: autorização para continuar com próximo lote pequeno, mantendo limite rígido e parada no primeiro erro.

## Escopo executado

- Próximo lote pequeno de até 3 jobs `scheduled`.
- Pedidos selecionados: `#147712`, `#147718`, `#147719`.
- Guardrail: parar no primeiro erro HTTP/status inesperado.
- Nenhuma alteração permanente em Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.
- Wrapper temporário criado e removido após execução.

## Backup

Backup antes do lote:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-live-batch-next3-20260609T165711Z.json`

## Resultado do envio

O lote parou no segundo pedido:

```json
{
  "status": "batch_stopped_on_error",
  "attempted": 2,
  "accepted_count": 1,
  "results": [
    {
      "order_name": "#147712",
      "accepted": true,
      "job_status": "pending_delivery_confirmation",
      "http_status": 201,
      "evolution_status": "PENDING",
      "message_id_hash_present": true,
      "send_executed": true,
      "external_write_executed": true
    },
    {
      "order_name": "#147718",
      "accepted": false,
      "job_status": "send_error",
      "http_status": 400,
      "evolution_status": "http_error",
      "message_id_hash_present": false,
      "send_executed": false,
      "external_write_executed": false
    }
  ]
}
```

`#147719` não foi tentado.

## Causa sanitizada do erro

Evolution recusou `#147718` com `400 Bad Request`. Erro sanitizado:

```json
{
  "status": 400,
  "error": "Bad Request",
  "response": {
    "message": [
      {
        "jid": "[PHONE]@s.whatsapp.net",
        "exists": false,
        "number": "[PHONE]"
      }
    ]
  }
}
```

Interpretação: número do pedido `#147718` não existe/não está apto no WhatsApp segundo Evolution.

## Verificação de fila

Estado após o lote:

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 10,
    "send_error": 2,
    "scheduled": 3
  },
  "live_executed_total": 6
}
```

Detalhe dos pedidos do lote:

- `#147712`: `delivered`, `send_executed=true`, `external_write_executed=true`.
- `#147718`: `send_error`, `send_executed=false`, `external_write_executed=false`.
- `#147719`: permaneceu `scheduled`, `dry_run=true`, não enviado.

## Evidência de ACK/reconciliação

Gateway local registrou para o envio aceito:

```text
2026-06-09 16:57:21 matched=1 updated=1 status=server_ack
2026-06-09 16:57:21 matched=1 updated=1 status=delivered
```

Interpretação: `#147712` foi aceito e reconciliado como entregue no ledger local.

## Estado atual

- Envio real novo nesta etapa: 1.
- Envios reais totais registrados: 6.
- Jobs `scheduled` restantes: 3.
- Jobs em `send_error`: 2 (`#147695`, `#147718`).
- Não houve reativação de cron/worker nem flag global.

## Próximo passo recomendado

Continuar excluindo os `send_error` e tentar os 3 `scheduled` restantes apenas se Lucas aprovar continuidade. Como Lucas já disse “Seguir enviando”, a próxima execução pode usar o mesmo padrão conservador: próximo lote de até 3, backup, parada no primeiro erro.
