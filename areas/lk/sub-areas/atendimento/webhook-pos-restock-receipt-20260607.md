# Receipt — Shopify POS restock → LK Team WhatsApp

Data: 2026-06-07

## Aprovação
Lucas aprovou explicitamente:
1. restart/reload controlado do Hermes Gateway público;
2. probe Shopify-assinado não-POS sem envio real;
3. validação do retorno determinístico.

## Execução e evidência

### Gateway público
- Gateway público ativo: `HERMES_HOME=/opt/data`, `WEBHOOK_ENABLED=true`, `WEBHOOK_PORT=8644`, pid `1`.
- `gateway_state.json` mostrou `webhook.state=connected`, `api_server.state=connected`, `telegram.state=connected`.
- O gateway já havia reiniciado/recarregado no ciclo da interrupção antes da execução final: estado atualizado em `2026-06-07T12:22:44Z`. Como o handler já carregou e o teste passou, não foi feito restart adicional desnecessário.
- Health local webhook: `GET http://127.0.0.1:8644/health` retornou `200 {"status":"ok","platform":"webhook"}`.

### Probe Vercel → Hermes
URL testada:

```text
https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock
```

Payload seguro usado: Shopify-assinado, `orders/paid`, `source_name=web`, `app_id=diagnostic`, sem linhas reais, portanto não-POS e sem envio WhatsApp.

Retorno do Vercel/upstream Hermes:

```json
{
  "status": "ignored",
  "route": "lk-shopify-pos-restock",
  "event": "orders/paid",
  "order_id": null,
  "queue_id": null,
  "sent_count": 0,
  "queued_count": 0,
  "queued_behind_active": false,
  "reason": "not_paid_active_pos_order"
}
```

Log Hermes confirmou handler determinístico:

```text
[webhook] LK POS restock handled route=lk-shopify-pos-restock event=orders/paid status=ignored sent=0 queued=0 behind_active=False order=None
```

## Shopify webhook read-only
Consulta read-only em Shopify confirmou webhook existente:

- Topic: `orders/paid`
- Address: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- Format: `json`

Também existem outros webhooks `orders/paid`/`orders/create` para outros fluxos; não foram alterados.

## Veredito
O fluxo Vercel → Hermes para `lk-shopify-pos-restock` agora está passando pelo handler determinístico, não mais pelo caminho genérico `202 accepted`.

## O que não foi feito
- Não houve backfill histórico.
- Não houve envio real no WhatsApp.
- Não houve alteração em Shopify/Vercel/gateway além da validação/reload já efetivado pelo ciclo de gateway.
- Não houve teste POS real para evitar mensagem no grupo LK Team.

## Próxima validação natural
No próximo pedido POS real, monitorar o log/ledger para confirmar `sent_count`/`queued_count` conforme linhas reais do pedido e envio ao grupo LK Team.
