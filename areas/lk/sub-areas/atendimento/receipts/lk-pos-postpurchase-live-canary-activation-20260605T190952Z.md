# Receipt — ativação canary live LK POS pós-venda WhatsApp 30min

Data UTC: 2026-06-05T19:09:52.693888+00:00

## Aprovação

Lucas aprovou explicitamente:

> Aprovo ativar canary live do pós-venda POS 30min via Evolution API / LK Flagship, usando o webhook Shopify orders/paid já existente, com limite inicial de 3 envios reais, kill switch, dedupe por pedido/telefone, sem n8n e sem alterar Shopify/Tiny/Chatwoot.

## Implementado

- Mantido o webhook Shopify existente `orders/paid` para `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Nenhum webhook Shopify novo foi criado nesta etapa.
- Adicionado worker live para consumir a fila local `pos_thankyou_queue.json` e enviar jobs vencidos via Evolution API / instância LK Flagship.
- Worker criado em `/opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py`.
- Cron local lk-ops criado/ativado em `/opt/data/profiles/lk-ops/cron/jobs.json`:
  - id: `lk-pos-postpurchase-canary`
  - schedule: `*/5 * * * *`
  - `no_agent: true`
  - entrega: `origin`
- Canary limit: 3 envios reais totais, contabilizando jobs já marcados com `send_executed` e `external_write_executed`.
- Kill switch operacional: pausar/desabilitar o cron `lk-pos-postpurchase-canary` ou setar `LIVE_SEND_ENABLED = False` no wrapper volta a bloquear envios live.

## Guardrails mantidos

- Sem n8n.
- Sem alteração Shopify/Tiny/Chatwoot.
- Sem alteração de webhook Shopify.
- Sem tocar `lucascimino.com/webhook/shopify`.
- Envio real apenas via Evolution API / LK Flagship, para jobs POS pagos/não cancelados com telefone e vencidos após 30min.
- Dedupe por `order_id` na fila e por status de job antes do envio.

## Verificação

Comandos executados:

```bash
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
python3 /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
```

Resultados:

- Test suite: `ok`.
- Py compile: exit 0.
- Worker manual: exit 0, sem jobs pendentes/due; resultado `sent=0`, `errors=0`, `would_send=0`.

## Estado no momento da ativação

Fila atual:

```json
{
  "jobs": [],
  "last_worker_result": {
    "status": "processed",
    "live": true,
    "canary_limit": 3,
    "would_send": 0,
    "sent": 0,
    "errors": 0,
    "prior_live_sends": 0
  }
}
```

## Observação operacional

O fluxo está ativado para próximas vendas POS reais. O primeiro pedido POS pago com telefone deve entrar pelo webhook Shopify já existente, gerar job local com `send_after +30min` e ser consumido pelo cron a cada 5 minutos, respeitando limite canary de 3 envios reais.
