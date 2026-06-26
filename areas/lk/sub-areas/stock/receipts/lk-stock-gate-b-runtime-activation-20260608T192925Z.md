# Receipt — LK Stock Gate B runtime activation

Data UTC: 2026-06-08T19:29:25Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **ativado com guardrails read-only**

## Aprovação

Lucas respondeu `1`, interpretado conforme o decision packet como aprovação para ativar o runtime real do Gate B do `lk-stock` com:

- `hermes-webhooks` no Vercel;
- eventos listados;
- cron diário read-only;
- HMAC/resign;
- idempotência;
- kill criteria/rollback preservados;
- Telegram silent-OK;
- zero writes em Tiny/Shopify/fornecedor/cliente/campanha.

## O que foi ativado

### Webhook ingress

Rotas públicas via `hermes-webhooks`:

```text
https://hermes-webhooks.vercel.app/webhooks/lk-stock-shopify-order-paid
https://hermes-webhooks.vercel.app/webhooks/lk-stock-shopify-product-update
https://hermes-webhooks.vercel.app/webhooks/lk-stock-tiny-stock-snapshot
```

A rota custom domain também responde no mesmo projeto:

```text
https://hermes-webhooks.lucascimino.com/webhooks/<route>
```

Alteração aplicada em `/opt/data/hermes-webhooks`:

- `api/webhooks/[route].js`: adiciona validação genérica HMAC para rota `lk-stock-tiny-*` e resign específico `LK_STOCK_HERMES_ROUTE_SECRET` para rotas `lk-stock-*`.
- `README.md`: documenta endpoints Gate B.
- Commit local: `6460bc5 Add LK stock Gate B webhook routing`.
- Observação: commit local está `ahead 1`; não foi feito push GitHub.

### Hermes subscriptions

Subscriptions já registradas no gateway público `HERMES_HOME=/opt/data`:

- `lk-stock-shopify-order-paid` — evento `orders/paid` — script `/opt/data/scripts/lk_stock_gate_b_webhook_ingest.py` — deliver `log`.
- `lk-stock-shopify-product-update` — eventos `products/update`, `products/create` — mesmo script — deliver `log`.
- `lk-stock-tiny-stock-snapshot` — evento `tiny_stock_snapshot` — mesmo script — deliver `log`.

### Cron diário

Criado cron no profile `lk-stock`:

- Job ID: `e8b35e20751b`
- Nome: `LK Stock Gate B daily freshness reconcile read-only`
- Schedule: `15 11 * * *` UTC
- Próximo run verificado: `2026-06-09T11:15:00+00:00`
- Modo: `no_agent`
- Deliver: `origin`
- Script: `lk_stock_gate_b_daily_reconcile.py`
- Profile: `lk-stock`

Script criado:

```text
/opt/data/profiles/lk-stock/scripts/lk_stock_gate_b_daily_reconcile.py
```

Comportamento: stdout vazio em OK; stdout só para exceção acionável (`sem_snapshot_tiny_no_cache` ou `tiny_snapshot_stale`). Writes externos permanecem `0`.

### Base local

```text
/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite
```

Uso: cache/ledger/score local. Não é fonte final de disponibilidade; Tiny / `LK | CONTROLE ESTOQUE` continua fonte de verdade.

## Probes e evidência

### Vercel deploy

Deploy produção concluído:

```text
Production: https://hermes-webhooks-ov1148we4-lk-snkrs-projects.vercel.app
Aliased: https://hermes-webhooks.vercel.app
Ready in 9s
```

### Health

```text
curl https://hermes-webhooks.vercel.app/health
{"status": "ok", "platform": "webhook"}
```

### Negative HMAC probe

POST sem assinatura em `lk-stock-tiny-stock-snapshot` retornou:

```text
HTTP/2 401
{"error":"missing_generic_signature"}
```

### Tiny signed probe

POST assinado para `lk-stock-tiny-stock-snapshot` retornou:

```json
{
  "status": "processed",
  "event_type": "tiny_stock_snapshot",
  "entities_updated": 1,
  "scores_recalculated": 2,
  "freshness_contract": "local_cache_not_stock_truth",
  "writes_externos": 0,
  "route": "lk-stock-tiny-stock-snapshot",
  "event": "tiny_stock_snapshot"
}
```

Readback SQLite:

```text
latest_event: tiny_stock_snapshot / processed
latest_snapshot: GATEB-PROBE-006 / quantity 0 / freshness live
```

### Shopify signed probe

POST Shopify-assinado para `lk-stock-shopify-order-paid` retornou:

```json
{
  "status": "processed",
  "event_type": "shopify_order_paid",
  "entities_updated": 1,
  "scores_recalculated": 2,
  "freshness_contract": "local_cache_not_stock_truth",
  "writes_externos": 0,
  "route": "lk-stock-shopify-order-paid",
  "event": "orders/paid"
}
```

### Cron script probe

Após haver snapshot live, execução manual do cron script retornou stdout vazio e exit `0`:

```text
exit=0
```

### Testes locais Gate B

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 2.115s

OK
```

### Cron registry

```text
e8b35e20751b [active]
Name: LK Stock Gate B daily freshness reconcile read-only
Schedule: 15 11 * * *
Next run: 2026-06-09T11:15:00+00:00
Deliver: origin
Mode: no-agent
Profile: lk-stock
```

### SQLite resumo

```json
{
  "events": [
    {"event_type": "shopify_order_paid", "status": "processed", "count": 2},
    {"event_type": "tiny_stock_snapshot", "status": "processed", "count": 1}
  ],
  "freshness": [
    {"freshness": "live", "count": 1}
  ],
  "writes_external_in_receipts": 0
}
```

## Guardrails preservados

- Tiny write: `0`
- Shopify write: `0`
- Fornecedor/cliente/campanha/WhatsApp/Klaviyo: `0`
- Secrets impressos: `0`
- Telegram OK: silencioso
- Disponibilidade final: **não afirmar sem Tiny/fonte viva equivalente**
- Base local: cache/ledger, não fonte final de pronta entrega

## Kill switch / rollback

Se necessário:

1. Pausar cron `e8b35e20751b`.
2. Remover/pausar subscriptions `lk-stock-*` no gateway público.
3. Manter SQLite como evidência read-only.
4. Marcar snapshots como `stale`.
5. Voltar para Gate A/manual read-only com consulta Tiny sob demanda.

## Próximo passo recomendado

Gate C: transformar sinais do Gate B em fila operacional de decisão segura — P0/P1, divergência SKU/Tiny/Shopify, e resposta A1 — mantendo bloqueio de promessa de disponibilidade sem Tiny/fonte viva.
