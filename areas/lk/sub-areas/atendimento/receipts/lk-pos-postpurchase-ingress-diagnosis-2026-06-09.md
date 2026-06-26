# LK POS pós-compra — diagnóstico de ingress Shopify/Vercel/Hermes

Data: 2026-06-09T15:58:39Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Evolution API
Modo: diagnóstico; sem envio WhatsApp; sem alteração Shopify/Vercel/Hermes/Doppler/cron; apenas um probe assinado não-POS que foi ignorado e não enfileirou job.

## Objetivo

Continuar a investigação do motivo pelo qual a mensagem de agradecimento pós-compra pela Evolution API LK Flagship não está sendo enviada.

Diagnóstico anterior: Evolution `connection_state=open`, worker live pausado, flag `LK_POS_POSTPURCHASE_LIVE_SEND` ausente, fila sem jobs novos desde 2026-06-06 apesar de pedidos POS elegíveis.

## Fontes verificadas

- Shopify Admin REST read-only: webhooks registrados.
- Gateway process env: processo público `HERMES_HOME=/opt/data`, `WEBHOOK_ENABLED=true`, porta `8644`.
- `/opt/data/webhook_subscriptions.json`, lido de forma sanitizada via terminal: rota `lk-shopify-pos-restock` existe com `kind=lk_shopify_pos_restock`, `events=['orders/paid']`, `script=/opt/data/scripts/lk_store_sale_restock_alert.py`, secret presente.
- Gateway logs `/opt/data/logs/gateway.log`.
- Proxy local `/opt/data/hermes-webhooks/api/webhooks/[route].js`.
- Vercel health e Vercel logs read-only.
- Probe assinado com `SHOPIFY_WEBHOOK_SECRET` Doppler e payload fake não-POS.
- Fila local `pos_thankyou_queue.json` antes/depois do probe.

## Achados

### 1. Shopify tem webhook cadastrado para o endpoint POS

Webhook relevante no Shopify:

- topic: `orders/paid`
- host: `hermes-webhooks.vercel.app`
- path: `/webhooks/lk-shopify-pos-restock`
- formato: `json`
- criado: `2026-05-23T17:52:30-03:00`

Observação: o Brain recomenda o custom domain `hermes-webhooks.lucascimino.com`, mas o alias técnico Vercel também é documentado como válido. O uso do alias não explica sozinho a falha.

### 2. Gateway público é o default/global, não o profile LK Ops

Processo público observado:

- `HERMES_HOME=/opt/data`
- `WEBHOOK_ENABLED=true`
- `WEBHOOK_PORT=8644`

Perfis especialistas, incluindo `lk-ops`, rodam com `WEBHOOK_ENABLED=false`. Isso é esperado pelo desenho atual: webhooks públicos entram no gateway global.

### 3. Rota global está configurada para handler determinístico

Rota sanitizada:

```json
"lk-shopify-pos-restock": {
  "kind": "lk_shopify_pos_restock",
  "events": ["orders/paid"],
  "deliver": "log",
  "script": "/opt/data/scripts/lk_store_sale_restock_alert.py",
  "secret": "present"
}
```

Código do gateway atual tem branch determinístico:

```python
if route_config.get("kind") == "lk_shopify_pos_restock":
    return await self._handle_lk_shopify_pos_restock_webhook(...)
```

### 4. Histórico mostra drift antigo: antes de 07/06 a rota caía no caminho genérico/LLM

Logs históricos mostraram POSTs `orders/paid` indo para `inbound message platform=webhook`, ou seja, caminho genérico.

Após correções em 07/06, logs passaram a mostrar:

```text
LK POS restock handled route=lk-shopify-pos-restock event=orders/paid status=ignored sent=0 queued=0 ...
```

Então o handler determinístico existe e já foi exercitado.

### 5. Vercel logs recentes mostram 401 no endpoint POS

Vercel logs read-only recentes mostraram várias entradas:

```text
POST /webhooks/lk-shopify-pos-restock 401
```

Isso significa que algumas chamadas chegaram no proxy Vercel, mas foram rejeitadas antes de chegar ao Hermes gateway. No código do proxy, para rota Shopify, 401 só deve ocorrer por:

- `missing_shopify_signature`; ou
- `invalid_shopify_signature`.

### 6. Probe assinado com o secret Doppler foi aceito e ignorado corretamente

Probe seguro executado:

- endpoint: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- assinatura: `X-Shopify-Hmac-Sha256` calculada com `SHOPIFY_WEBHOOK_SECRET` do Doppler
- tópico: `orders/paid`
- payload: fake, `source_name=web`, não-POS, sem cliente real

Resposta:

```json
{
  "http_status": 200,
  "status": "ignored",
  "route": "lk-shopify-pos-restock",
  "event": "orders/paid",
  "order_id": null,
  "sent_count": 0,
  "queued_count": 0,
  "reason": "not_paid_active_pos_order"
}
```

Fila depois do probe permaneceu:

- `jobs_total=11`
- `last_updated_at=2026-06-06T14:52:16.643248+00:00`
- statuses: `delivered=5`, `pending_delivery_confirmation=6`

Conclusão do probe: o proxy Vercel consegue validar uma assinatura calculada com o secret Doppler atual e consegue encaminhar para o handler determinístico. O probe não gerou job.

## Interpretação

O caminho técnico Vercel → Hermes → handler está funcional agora para payload Shopify assinado corretamente.

Mas os pedidos POS reais recentes não apareceram na fila. Possíveis explicações restantes:

1. O webhook real de Shopify para `orders/paid` falhou antes/na hora dos pedidos POS recentes, possivelmente por assinatura rejeitada no proxy naquele momento.
2. As entradas `401` no Vercel podem ser chamadas não-Shopify/sem assinatura, mas a ausência de logs determinísticos para o pedido `#147727` continua indicando que o pedido real não chegou ao handler.
3. Pode ter havido janela de drift/redeploy/env entre 06/06 e hoje: rota ou secret parcialmente corrigidos depois, mas os pedidos ocorridos antes não foram reconciliados/enfileirados.
4. A automação não possui reconciliador/poller de pedidos POS recentes; depende do webhook `orders/paid`. Se o evento se perde ou é rejeitado, o agradecimento não entra na fila.

## Veredito complementar

A falha atual não é na Evolution e não parece ser no código do proxy/handler no estado atual. O buraco operacional é:

- pedidos POS recentes não foram capturados/enfileirados;
- há evidência de `401` no Vercel para a rota POS;
- não há reconciliação automática de POS pagos perdidos;
- e mesmo com fila populada, envio real continuaria pausado por `LIVE_SEND_ENABLED=False` e ausência de `LK_POS_POSTPURCHASE_LIVE_SEND=1`.

## Próximo passo com aprovação necessária

Para recuperar e validar sem enviar cliente ainda:

1. **Reconciliar pedidos POS recentes para a fila em modo dry-run local**
   - Escopo: pedidos POS pagos desde `2026-06-06T14:52:16Z` que não estejam na fila.
   - Write: local apenas em `pos_thankyou_queue.json`.
   - Sem WhatsApp, sem Shopify/Tiny/Vercel/Doppler write.
   - Esperado: jobs `scheduled` ou `missing_phone` aparecem na fila com `dry_run=true`, `send_executed=false`, `external_write_executed=false`.

2. **Criar/rodar verificador read-only periódico de lacuna**
   - Comparar POS pagos recentes Shopify vs fila local.
   - Alertar se POS elegível não estiver enfileirado.
   - Não enviar cliente.

3. **Somente depois reativar canário de envio real**
   - Requer aprovação separada para setar `LK_POS_POSTPURCHASE_LIVE_SEND=1` e/ou `LIVE_SEND_ENABLED=True`.
   - Iniciar com limite baixo e mensagem aprovada.
   - Tratar Evolution `201/PENDING` como aceitação de API, não entrega; exigir ACK forte.

## O que não foi feito

- Não enviei WhatsApp.
- Não alterei Shopify, Vercel, Hermes, Doppler, cron ou Evolution.
- Não rodei replay de pedido real, pois isso escreveria fila local operacional.
- Não expus telefone, cliente, token ou payload real.
