# Hermes follow-up 1-2-3 — 2026-06-25

- generated_at_utc: `2026-06-25T12:58:49.949755+00:00`
- status geral: **ok com 1 bloqueio externo (Linear token inválido)**
- values_printed: `false`

## Escopo aprovado

Lucas pediu `Fazer 1 e 2 e 3` após a auditoria:
1. migrar LK Stock para `secret_doppler` puro / runtime-safe;
2. corrigir/diagnosticar Linear;
3. tratar warnings de rede Telegram.

## 1 — LK Stock webhook secret_doppler

Resultado: **feito e verificado**.

- `lk-stock-shopify-order-paid`: `secret_present=false`, `secret_doppler=WEBHOOK_SECRET`.
- `lk-stock-shopify-product-update`: `secret_present=false`, `secret_doppler=WEBHOOK_SECRET`.
- `/opt/data/webhook_subscriptions.json`: modo `0600`.
- `WEBHOOK_SECRET` foi canonizado no Doppler `lc-keys/prd` como alias de compatibilidade, sem imprimir valor.
- `/opt/data/scripts/hermes_doppler.py` default `PROFILE_SECRET_MAP` agora inclui `WEBHOOK_SECRET`, `HERMES_WEBHOOK_SECRET` e `LK_STOCK_HERMES_ROUTE_SECRET` para futuras execuções helper-launched.

Certificação final:

- status: `pass`
- routes: `14`
- pass: `14`
- attention: `0`
- external_writes: `0`

Artefato:
- `/opt/data/tmp/hermes_webhooks_14_route_certification_final_after_123_20260625.json`

## 2 — Linear

Resultado: **não corrigível sem novo token válido**.

Evidência:
- `LINEAR_API_KEY`: presente no Doppler.
- `LINEAR_API_TOKEN`/`LINEAR_TOKEN`: ausentes.
- Smoke GraphQL Linear: HTTP `401`, `has_viewer=false`.
- Teste de variantes de Authorization: token cru = `401`, Bearer = `400`, stripped = `401`.

Conclusão: a integração Linear está configurada por nome, mas o valor atual de `LINEAR_API_KEY` é inválido/revogado/sem acesso. Nenhum valor foi impresso. Para corrigir de fato, Lucas precisa fornecer/rotacionar um token Linear válido ou autorizar outra fonte.

## 3 — Warnings Telegram network

Resultado: **classificado como watch, sem degradação atual**.

- Gateways vivos: `12`.
- Bot API `getMe`: `12/12 OK`.
- Falhas atuais de getMe: `0`.
- Logs têm warnings recorrentes de rede/fallback IP e conflitos antigos, mas com mensagens de retomada (`polling resumed`) e sem falha atual de identidade/token.

Ação tomada:
- Mantido como watchlist, sem restart e sem spam de round-trip.
- Registrada referência de skill para o caso LK Stock dynamic webhook secret alias.

## Verificação final

- Webhook no-op: `14/14 pass`, exit 0.
- Cron registry read-only: `nonok=0`.
- Secret scan dos artefatos: `possible_secret_hits=0` após investigar falso positivo em nome de variável (`DOPPLER_TOKEN`) no helper; nenhum valor sensível impresso.
- External sends/deploys/restarts: `0`.
