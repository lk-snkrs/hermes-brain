# LK POS pós-compra — verificação de confiança pós-ativação

Data: 2026-06-09T17:36:27Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Evolution API / Hermes Cron

## Pergunta

Lucas perguntou se há certeza de que a automação vai funcionar agora.

## Resposta técnica

Não há certeza absoluta até passar uma compra POS real end-to-end, mas os blocos críticos estão ativos e verificados com evidência viva.

## Evidências

### Cron Hermes

```text
✓ Gateway is running — cron jobs will fire automatically
30 active job(s)

6792657c0be7 [active]
Name:      LK POS pós-compra WhatsApp auto-worker
Schedule:  */5 * * * *
Next run:  2026-06-09T17:35:00+00:00
Deliver:   local
Script:    lk_pos_postpurchase_auto_worker_once.py
Mode:      no-agent
Workdir:   /opt/data
Last run:  2026-06-09T17:30:43.337679+00:00  ok
```

### Worker/script

```text
py_compile ok
script=/opt/data/scripts/lk_pos_postpurchase_auto_worker_once.py mode=750
manual run: worker_exit:0
```

### Fila

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
  "live_executed_total": 9,
  "last_worker_run_at": "2026-06-09T17:30:43.185357+00:00",
  "last_worker_result": {
    "status": "processed",
    "live": true,
    "would_send": 0,
    "errors": 0,
    "prior_live_sends": 9
  }
}
```

### Webhook público

Probe assinado, não-POS, recebido e ignorado corretamente:

```json
{
  "http_status": 200,
  "status": "ignored",
  "route": "lk-shopify-pos-restock",
  "event": "orders/paid",
  "queued_count": 0,
  "reason": "not_paid_active_pos_order"
}
```

Gateway confirmou:

```text
LK POS restock handled route=lk-shopify-pos-restock event=orders/paid status=ignored sent=0 queued=0
```

## Risco residual

Só será 100% comprovado depois de uma compra POS real elegível criar um job `scheduled` e o worker enviar após o delay.

Possíveis riscos residuais:

- Shopify mandar payload POS com campos diferentes do esperado;
- cliente sem WhatsApp/telefone inválido;
- Evolution instável no momento do envio;
- gateway/scheduler cair entre compra e envio.

## Conclusão

Confiança operacional: alta. Blocos críticos verificados. End-to-end real ainda pendente da próxima compra POS.
