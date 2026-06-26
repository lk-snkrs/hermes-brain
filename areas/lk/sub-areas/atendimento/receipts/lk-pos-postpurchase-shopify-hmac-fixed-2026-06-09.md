# LK POS pós-compra — correção HMAC Shopify/Vercel aplicada

Data: 2026-06-09T19:01:14Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Webhooks / Vercel / Doppler

## Ação autorizada

Lucas forneceu o segredo Shopify correto e instruiu usar para corrigir o webhook.

## Guardrail de segredo

- Valor do segredo não registrado neste receipt.
- Relatório apenas por presença/shape/status.
- `values_printed=false` nas verificações finais.

## Mudanças realizadas

1. Atualizado `SHOPIFY_WEBHOOK_SECRET` no Doppler `lc-keys/prd`.
2. Atualizado `SHOPIFY_WEBHOOK_SECRET` no Vercel production env do projeto `hermes-webhooks`.
3. Redeploy production do Vercel executado.
4. Alias production atualizado:

```text
https://hermes-webhooks.vercel.app
```

## Verificações

Doppler shape/status:

```json
{
  "SHOPIFY_WEBHOOK_SECRET_exists": true,
  "shape_ok": true,
  "length": 38,
  "values_printed": false
}
```

Probe assinado com o novo secret para a rota Shopify:

```json
{
  "http_status": 200,
  "route": "lk-shopify-pos-restock",
  "event": "orders/paid",
  "status": "ignored",
  "reason": "not_paid_active_pos_order",
  "values_printed": false
}
```

Interpretação: a rota aceitou HMAC Shopify e encaminhou ao Hermes. O `ignored` é esperado porque o payload de teste não era pedido POS pago elegível.

Gateway Hermes confirmou recebimento:

```text
LK POS restock handled route=lk-shopify-pos-restock event=orders/paid status=ignored queued=0 reason not_paid_active_pos_order
```

Vercel logs recentes confirmaram o POST na rota com HTTP 200:

```text
POST /webhooks/lk-shopify-pos-restock 200
```

## Resultado

Causa raiz HMAC corrigida para o caminho atual:

```text
Shopify → Vercel hermes-webhooks → Hermes Gateway → handler lk-shopify-pos-restock
```

## Estado operacional recomendado

Manter os dois caminhos:

- Webhook Shopify: principal/event-driven.
- Reconciliador Shopify read-only: fallback/segurança operacional.

## Próxima confirmação de produção

A próxima compra POS real deve deixar de gerar `401` no Vercel e deve aparecer no Hermes como `queued` ou `duplicate` caso o reconciliador já tenha capturado antes.
