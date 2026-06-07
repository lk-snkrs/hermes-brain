# Receipt — LK Evolution delivery reconciliation

- Data UTC: 2026-06-06T17:18:16Z
- Escopo: LK Ops / Atendimento / Evolution API delivery ACK reconciliation
- Instância Evolution: LK Flagship
- Endpoint público: `https://hermes-webhooks.vercel.app/webhooks/lk-evolution-delivery-reconciliation?secret=[REDACTED]`
- Rota Hermes: `lk-evolution-delivery-reconciliation`
- n8n: não usado

## Correção aplicada

A causa do `matched=0` era divergência entre IDs da Evolution:

- `key.id`: ID WhatsApp retornado em `sendText`.
- `id`: ID interno do registro Evolution, frequentemente usado em `messages.update`.

O reconciler foi ajustado para extrair e comparar múltiplos aliases sanitizados de ID:

- `key.id`
- `id`
- `messageId`
- `keyId`
- `evolution_message_id_hash`
- `evolution_key_message_id_hash`
- `evolution_record_id_hash`
- `evolution_message_id_alias_hashes`

Também foi ajustado para aceitar histórico `MessageUpdate` com status `SERVER_ACK` e `DELIVERY_ACK`.

## Evidência — teste original destravado

Job: `evo-webhook-live-20260606164900`

Comparação sanitizada:

- hash salvo no job via `sendText`: `30815f3e5f82`
- hash `key.id` no registro Evolution: `30815f3e5f82`
- hash `id` interno Evolution: `3ea4ccf965f5`
- statuses no registro Evolution: `SERVER_ACK`, `DELIVERY_ACK`, `SERVER_ACK`

Reprocessamento pela rota pública Vercel → Hermes:

```json
{
  "http": 200,
  "status": "reconciled",
  "route": "lk-evolution-delivery-reconciliation",
  "event": "messages.update",
  "matched": 1,
  "updated": 1,
  "ledger_status": "delivered",
  "statuses": ["SERVER_ACK", "DELIVERY_ACK"],
  "reason": null
}
```

Ledger após reprocessamento:

```json
{
  "job_id": "evo-webhook-live-20260606164900",
  "status": "delivered",
  "updates_count": 3,
  "last_update": {
    "source": "evolution_webhook_reconciler",
    "event": "messages.update",
    "message_id_hash": "30815f3e5f82",
    "remote_jid_hash": "8336409b2321",
    "statuses": ["SERVER_ACK", "DELIVERY_ACK"],
    "ledger_status": "delivered"
  }
}
```

## Evidência — novo teste interno

Job: `evo-webhook-unlock-20260606171433`

Envio interno controlado para número final `3361`:

```json
{
  "send_http": 201,
  "send_status": "PENDING",
  "message_id_hash": "8d09d951963c",
  "key_message_id_hash": "8d09d951963c",
  "resolved_record_id_hash": "5ebfb3784050"
}
```

Reprocessamento pela rota pública Vercel → Hermes:

```json
{
  "http": 200,
  "status": "reconciled",
  "route": "lk-evolution-delivery-reconciliation",
  "event": "messages.update",
  "matched": 1,
  "updated": 1,
  "ledger_status": "delivered",
  "statuses": ["SERVER_ACK", "DELIVERY_ACK"],
  "reason": null
}
```

Ledger final do novo teste:

```json
{
  "job_id": "evo-webhook-unlock-20260606171433",
  "status": "delivered",
  "updates_count": 1,
  "last_update": {
    "source": "evolution_webhook_reconciler",
    "event": "messages.update",
    "message_id_hash": "8d09d951963c",
    "remote_jid_hash": "8336409b2321",
    "statuses": ["SERVER_ACK", "DELIVERY_ACK"],
    "ledger_status": "delivered"
  }
}
```

## Ativação pós-aprovação — auto-delivered confirmado

Após aprovação de Lucas, o Vercel foi ajustado para estabilizar o fluxo sem n8n e sem restart arriscado do gateway principal:

- normaliza `messages.update` para espelhar o ID interno Evolution em `data.key.id` quando o payload não traz `key.id`;
- aplica atraso curto em ACKs (`EVOLUTION_WEBHOOK_ACK_DELAY_MS`, default 5000ms) para dar tempo do ledger local persistir aliases de ID;
- o sender local salva o hash do ID interno Evolution também como `evolution_message_id_hash` para compatibilidade com o gateway já carregado.

Novo teste interno controlado:

- job: `evo-webhook-finalauto-20260606173057`
- envio Evolution: `HTTP 201`, `PENDING`
- key hash: `5c0dd9fdaf71`
- record hash: `5d139b0581d6`
- record hash salvo no ledger: `2026-06-06T17:31:00.970162+00:00`

Vercel → Hermes automático:

```json
{
  "event": "messages.update",
  "message_id_hash": "5d139b0581d6",
  "upstream_status": 200,
  "upstream": {
    "status": "reconciled",
    "matched": 1,
    "updated": 1,
    "ledger_status": "delivered",
    "statuses": ["DELIVERY_ACK"],
    "reason": null
  }
}
```

Ledger final automático:

```json
{
  "job_id": "evo-webhook-finalauto-20260606173057",
  "auto": true,
  "seconds": 6,
  "status": "delivered",
  "updates_count": 2,
  "last_update": {
    "source": "evolution_webhook_reconciler",
    "event": "messages.update",
    "message_id_hash": "5d139b0581d6",
    "statuses": ["DELIVERY_ACK"],
    "ledger_status": "delivered"
  }
}
```

## Observação operacional

Os webhooks reais da Evolution chegam muito rápido após `sendText`. O fluxo foi estabilizado com persistência imediata de aliases, normalização no Vercel e atraso curto só para ACKs. Para jobs operacionais, manter o job persistido antes do envio e salvar os aliases retornados/consultados imediatamente após o envio.

## Rollback seguro

Se necessário, remover a rota/handler `lk-evolution-delivery-reconciliation` do Hermes Gateway e manter a Evolution apontando para o Vercel apenas com secret desativado/rotacionado. Nenhum secret foi registrado neste receipt.
