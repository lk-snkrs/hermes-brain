# LK POS pós-compra — ativação automática para próximas compras na loja

Data: 2026-06-09T17:28:51Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Evolution API LK Flagship / Hermes Cron
Aprovação: Lucas pediu “seguir, vamos deixar tudo ativado para o próximo cliente que comprar na loja, enviar a mensagem automaticamente?”

## Resultado

Automação ativada via Hermes cron interno.

- Job ID: `6792657c0be7`
- Nome: `LK POS pós-compra WhatsApp auto-worker`
- Schedule: `*/5 * * * *`
- Script: `lk_pos_postpurchase_auto_worker_once.py`
- Mode: `no-agent`
- Deliver: `local`
- Workdir: `/opt/data`

## Como funciona

1. Shopify `orders/paid` chama Vercel/Hermes em:
   - `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
2. Rota Hermes já ativa:
   - route: `lk-shopify-pos-restock`
   - kind: `lk_shopify_pos_restock`
   - script: `/opt/data/scripts/lk_store_sale_restock_alert.py`
3. Se for pedido POS pago/ativo/elegível, o handler cria job local `scheduled` com envio para 30 minutos depois.
4. O cron roda a cada 5 minutos.
5. O wrapper processa no máximo 1 envio real por execução, usando limite dinâmico `prior_live_sends + 1`.
6. Evolution delivery webhooks reconciliam `server_ack`/`delivered`/`read` no ledger local.

## Guardrails ativos

- Máximo de 1 envio real por execução do worker.
- Fila antiga não tem `scheduled`; nada pendente será disparado retroativamente.
- `deliver=local`, para não poluir Telegram em sucesso rotineiro.
- Script fica silencioso quando não há trabalho.
- Não houve alteração em Shopify, Tiny, Chatwoot, Vercel ou secrets Doppler.
- Reconciliador já foi corrigido para não rebaixar `delivered/read` para `server_ack`.

## Verificações executadas

### Worker manual antes do cron

Com fila sem `scheduled`, o worker rodou e ficou silencioso:

```text
EXIT:0
```

### Hermes cron

```text
6792657c0be7 [active]
Name:      LK POS pós-compra WhatsApp auto-worker
Schedule:  */5 * * * *
Repeat:    ∞
Next run:  2026-06-09T17:30:00+00:00
Deliver:   local
Script:    lk_pos_postpurchase_auto_worker_once.py
Mode:      no-agent
Workdir:   /opt/data
Last run:  2026-06-09T17:27:43.045237+00:00  ok
```

### Estado da fila após ativação

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 12,
    "send_error": 2,
    "read": 1
  },
  "scheduled_remaining": 0,
  "probe_present": false,
  "last_worker_run_at": "2026-06-09T17:27:42.971489+00:00"
}
```

### Probe público Shopify/Vercel/Hermes

Payload falso, não-POS, assinado com `SHOPIFY_WEBHOOK_SECRET`, aceito e ignorado corretamente:

```json
{
  "http_status": 200,
  "body": {
    "status": "ignored",
    "route": "lk-shopify-pos-restock",
    "event": "orders/paid",
    "queued_count": 0,
    "reason": "not_paid_active_pos_order"
  }
}
```

O probe não criou job.

## Arquivos criados/alterados

Criado:

`/opt/data/scripts/lk_pos_postpurchase_auto_worker_once.py`

Cron interno Hermes criado:

`6792657c0be7`

Tentativa de `crontab` Linux não foi usada porque o host/container não tem `crontab` instalado; a automação válida é o Hermes cron interno.

## Rollback

Pausar automação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron pause 6792657c0be7
```

Remover automação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron remove 6792657c0be7
```

Desabilitar sem mexer no cron:

```bash
chmod 000 /opt/data/scripts/lk_pos_postpurchase_auto_worker_once.py
```

## Próxima validação recomendada

Após a próxima venda POS real:

1. confirmar que novo job entrou como `scheduled`;
2. aguardar 30 minutos + próximo tick de até 5 minutos;
3. confirmar Evolution `server_ack`/`delivered`;
4. registrar receipt do primeiro envio automático real.
