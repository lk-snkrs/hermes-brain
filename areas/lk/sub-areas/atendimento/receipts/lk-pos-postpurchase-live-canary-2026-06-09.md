# LK POS pós-compra — canário real único via Evolution LK Flagship

Data: 2026-06-09T16:09:28Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Aprovação: Lucas respondeu “Aprovo” após proposta de canário real limitado.

## Escopo executado

- Canário real conservador: exatamente 1 tentativa de envio externo.
- Instância: Evolution API LK Flagship.
- Pedido usado: `#147694`.
- Sem alteração permanente em Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.
- Escrita local: atualização do job correspondente em `pos_thankyou_queue.json`.

## Segurança operacional

Para evitar disparo em lote, não foi usado o worker genérico em loop. Foi usado um wrapper temporário que:

1. criou backup da fila;
2. selecionou apenas o primeiro job `scheduled` vencido;
3. chamou `evolution_send_lk_flagship_text(...)` uma única vez;
4. atualizou somente o job selecionado;
5. removeu o script temporário ao final.

Nenhum telefone, texto completo ou token foi registrado neste receipt.

## Backup

Backup antes do canário:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-live-canary-20260609T160752Z.json`

## Resultado do envio

Saída sanitizada do canário:

```json
{
  "status": "single_live_canary_processed",
  "attempted": 1,
  "accepted": true,
  "order_name": "#147694",
  "job_status": "pending_delivery_confirmation",
  "http_status": 201,
  "evolution_status": "PENDING",
  "message_id_hash_present": true,
  "send_executed": true,
  "external_write_executed": true
}
```

Interpretação inicial: Evolution aceitou o envio (`201/PENDING`).

## Verificação posterior da fila

Verificação independente logo depois:

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 6,
    "scheduled": 9
  },
  "live_executed_total": 2,
  "canary_jobs": [
    {
      "order_name": "#147694",
      "status": "delivered",
      "send_executed": true,
      "external_write_executed": true,
      "has_response": true,
      "has_hash": true
    }
  ]
}
```

Interpretação: o job `#147694` evoluiu de `scheduled` para `delivered`. Os outros 9 jobs reconciliados permaneceram `scheduled`.

## Evidência de ACK/reconciliação

Gateway local registrou eventos sanitizados da rota:

```text
2026-06-09 16:07:59 LK Evolution reconciled route=lk-evolution-delivery-reconciliation event=messages.update matched=1 updated=1 status=server_ack
2026-06-09 16:07:59 LK Evolution reconciled route=lk-evolution-delivery-reconciliation event=messages.update matched=1 updated=1 status=delivered
2026-06-09 16:08:52 LK Evolution reconciled route=lk-evolution-delivery-reconciliation event=messages.update matched=1 updated=1 status=server_ack
```

O `matched=1 updated=1 status=delivered` é a confirmação material de que o webhook de reconciliação casou o ACK com o ledger local.

## Estado atual

- 1 mensagem real de agradecimento enviada e reconciliada como `delivered`.
- 9 jobs novos continuam `scheduled`, não enviados.
- A fila total tem 21 jobs.
- Não houve liberação permanente do cron nem flag global `LK_POS_POSTPURCHASE_LIVE_SEND=1` no Doppler.

## Observação fora do escopo

Durante a checagem de logs apareceu `401 Invalid signature` para rota `lk-shopify-tiny-stock-sync`. Isso é de estoque/sync Shopify→Tiny e deve ser roteado ao dono `lk-stock`; não foi investigado nem alterado neste atendimento.

## Próximo passo recomendado

Se Lucas aprovar, próximo passo seguro:

- enviar mais um lote pequeno, por exemplo 2 ou 3 mensagens, usando o mesmo wrapper de limite rígido;
- só depois considerar reativação controlada do worker/cron;
- corrigir em paralelo o ingresso Shopify POS para evitar depender de reconciliação manual.
