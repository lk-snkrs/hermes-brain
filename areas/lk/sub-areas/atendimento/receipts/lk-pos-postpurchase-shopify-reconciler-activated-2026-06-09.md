# LK POS pós-compra — ativação reconciliador Shopify read-only → fila local

Data: 2026-06-09T18:51:06Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Hermes Cron
Aprovação: Lucas aprovou "opção B, ativar" após investigação do webhook Shopify 401 HMAC.

## Objetivo

Mitigar falhas do webhook Shopify `orders/paid` para POS pós-compra, usando polling read-only no Shopify para alimentar a fila local do WhatsApp pós-compra.

## Guardrails

- Sem escrita em Shopify.
- Sem Tiny/estoque; estoque/pronta entrega continua fora do escopo e pertence ao `lk-stock`.
- Sem Chatwoot/n8n/Klaviyo.
- O reconciliador só lê Shopify Admin API e grava fila/ledger local.
- Mensagens reais continuam sendo enviadas pelo worker existente.
- Limite diário obrigatório: no máximo 1 WhatsApp por cliente/telefone por dia BRT.

## Artefatos criados

Script principal:

```text
/opt/data/scripts/lk_pos_postpurchase_shopify_reconciler.py
```

Wrapper cron Doppler-first:

```text
/opt/data/scripts/lk_pos_postpurchase_shopify_reconciler_cron.sh
```

Cron Hermes:

```text
id: e2f169cc046a
name: LK POS Shopify→fila reconciliador
schedule: */5 * * * *
deliver: local
mode: no-agent
script: lk_pos_postpurchase_shopify_reconciler_cron.sh
```

## Comportamento

A cada 5 minutos:

1. carrega credenciais via Doppler `lc-keys/prd`;
2. consulta Shopify `orders.json` read-only para pedidos pagos recentes;
3. filtra POS (`source_name=pos`), pago, não cancelado, com cliente e telefone;
4. chama `enqueue_pos_thankyou_dry_run()` para usar a mesma fila do webhook/backfill;
5. respeita idempotência por `order_id`;
6. respeita limite diário por telefone/cliente;
7. stdout vazio quando OK/no-op, portanto sem ruído Telegram.

## Verificações executadas

Sintaxe:

```text
python3 -m py_compile ok
```

Dry-run com Shopify real:

```json
{
  "orders_seen": 2,
  "eligible_seen": 2,
  "duplicates": 2,
  "queued": 0,
  "status": "ok"
}
```

Run live idempotente:

```json
{
  "orders_seen": 2,
  "eligible_seen": 2,
  "duplicates": 2,
  "queued": 0,
  "status": "ok"
}
```

Wrapper cron manual silencioso:

```text
stdout bytes: 0
```

Cron Hermes executou:

```text
Last run: 2026-06-09T18:48:48.272871+00:00 ok
Next run: 2026-06-09T18:55:00+00:00
```

Nenhum artifact de output foi gerado em `/opt/data/profiles/lk-ops/cron/output/` para esse job, consistente com silent-OK/no-op.

## Estado dos pedidos investigados após ativação

```json
{
  "#147732": {
    "status": "delivered",
    "send_executed": true,
    "external_write_executed": true
  },
  "#147731": {
    "status": "skipped_daily_limit",
    "send_executed": false,
    "external_write_executed": false,
    "daily_limit_existing_order_name": "#147732"
  }
}
```

## Pendência separada

A causa raiz do webhook segue sendo provável HMAC/secret Shopify incorreto no Vercel (`POST /webhooks/lk-shopify-pos-restock 401`). O reconciliador mitiga a operação, mas a correção canônica ainda é alinhar o `SHOPIFY_WEBHOOK_SECRET` real do app Shopify no Doppler/Vercel.
