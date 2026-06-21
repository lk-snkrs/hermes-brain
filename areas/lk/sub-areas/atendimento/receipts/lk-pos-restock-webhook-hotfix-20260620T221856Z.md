# Receipt — LK POS restock WhatsApp webhook hotfix

- Data UTC: 2026-06-20T22:18:56Z
- Perfil executor: lk-ops
- Escopo aprovado por Lucas: hotfix limitado em produção para corrigir parada do fluxo Hermes de recompra/reposição de produtos vendidos na loja via WhatsApp.

## Sintoma

O Hermes parou de mandar mensagem/alerta de recomprar produtos vendidos na loja.

## Diagnóstico

A Shopify continuava chegando no Hermes, mas a rota `lk-shopify-pos-restock` respondia `401 Invalid signature` repetidamente.

Evidências sanitizadas:

- Logs antes do hotfix: `POST /webhooks/lk-shopify-pos-restock` com status `401` e erro `Invalid signature for route lk-shopify-pos-restock`.
- Outros webhooks Shopify do mesmo período passavam normalmente, isolando o problema na rota POS restock.
- A rota dinâmica correta existia em `/opt/data/webhook_subscriptions.json` com secret presente e compatível com `HERMES_WEBHOOK_SECRET` do Doppler (`values_printed=false`).
- Havia rota estática legada em `/opt/data/config.yaml` sob `platforms.webhook.extra.routes.lk-shopify-pos-restock`, com configuração antiga `secret_doppler: SHOPIFY_WEBHOOK_SECRET`, tomando precedência sobre a rota dinâmica.

## Ação executada

- Backup criado: `/opt/data/backups/lk-pos-restock-webhook-hotfix-20260620T221541Z/config.yaml.bak`.
- Removida somente a rota estática legada `lk-shopify-pos-restock` de `/opt/data/config.yaml`.
- Mantida a rota dinâmica correta em `/opt/data/webhook_subscriptions.json`.
- Reiniciado somente o container/gateway principal que expõe webhook/Telegram: `hermes-agent-5ajw-hermes-telegram-1`.

## Validação

- Gateway voltou a escutar:
  - porta `8644`: open
  - porta `8642`: open
  - `GET http://127.0.0.1:8644/health`: `{"status":"ok","platform":"webhook"}`
- Logs pós-restart:
  - `Starting Hermes Gateway...`
  - `Reloaded 14 dynamic route(s)` incluindo `lk-shopify-pos-restock`
  - `Listening on 0.0.0.0:8644`
- Teste local assinado com `HERMES_WEBHOOK_SECRET` via Doppler:
  - arquivo: `/opt/data/tmp/lk_pos_restock_hotfix_validation.json`
  - status: `200`
  - body: `{"status":"ignored", "event":"diagnostic/noop"}`

## Guardrails

- `values_printed=false`; nenhum secret foi impresso ou registrado.
- Não houve envio de WhatsApp durante o teste.
- Não houve alteração em Shopify, Tiny, estoque, preço, disponibilidade ou mapeamento.
- Não houve promise operacional de estoque/pronta entrega.

## Rollback

Se necessário, restaurar:

```bash
cp -a /opt/data/backups/lk-pos-restock-webhook-hotfix-20260620T221541Z/config.yaml.bak /opt/data/config.yaml
# reiniciar apenas o gateway principal depois do restore
```

## Pendência operacional

Confirmar no próximo pedido POS real se o alerta de recompra/reposição voltou a ser enviado pelo fluxo WhatsApp/Evolution. A validação técnica da rota passou; a validação funcional depende do próximo evento real `orders/paid` POS.
