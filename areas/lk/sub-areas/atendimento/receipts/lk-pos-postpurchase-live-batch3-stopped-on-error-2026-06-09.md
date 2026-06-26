# LK POS pós-compra — lote real de 3 aprovado, parado no primeiro erro

Data: 2026-06-09T16:28:05Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Aprovação: Lucas respondeu “Aprovo” após pedido explícito para enviar 3 mensagens reais dos pedidos `#147695`, `#147697` e `#147698`.

## Escopo executado

- Tentativa de lote real limitado a 3 pedidos aprovados.
- Guardrail aplicado: parar no primeiro erro HTTP/status inesperado.
- Wrapper temporário criado e removido após execução.
- Nenhuma alteração permanente em Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.

## Backup

Backup antes da tentativa:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-live-batch3-20260609T162722Z.json`

## Resultado

O lote parou no primeiro pedido:

```json
{
  "status": "batch3_stopped_on_error",
  "attempted": 1,
  "accepted_count": 0,
  "results": [
    {
      "order_name": "#147695",
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

Os pedidos `#147697` e `#147698` não foram tentados.

## Causa sanitizada

A Evolution recusou o envio para `#147695` com `400 Bad Request`. Erro sanitizado:

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

Interpretação: o número associado ao pedido `#147695` não existe/ não está apto no WhatsApp, segundo a Evolution API. Por isso não houve `message_id_hash` nem ACK de entrega para esse pedido.

## Verificação de fila

Estado após a tentativa:

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 6,
    "send_error": 1,
    "scheduled": 8
  },
  "live_executed_total": 2
}
```

Detalhe dos pedidos aprovados:

- `#147695`: `send_error`, `send_executed=false`, `external_write_executed=false`, `http_status=400`.
- `#147697`: permanece `scheduled`, `dry_run=true`, não enviado.
- `#147698`: permanece `scheduled`, `dry_run=true`, não enviado.

## Verificação de ACK

Não houve ACK/delivery para esse lote porque a tentativa foi recusada antes de gerar mensagem. O último ACK material com `matched=1 updated=1` permanece relacionado ao canário anterior `#147694`.

## Próximo passo recomendado

Opções seguras:

1. tratar `#147695` como telefone inválido/não contatável via WhatsApp e seguir com novo lote pequeno excluindo esse pedido;
2. revisar/validar manualmente o telefone do pedido `#147695` antes de qualquer nova tentativa;
3. executar próximo lote limitado com `#147697`, `#147698` e próximo `scheduled`, sob nova aprovação explícita.

Não executar novos envios sem aprovação explícita.
