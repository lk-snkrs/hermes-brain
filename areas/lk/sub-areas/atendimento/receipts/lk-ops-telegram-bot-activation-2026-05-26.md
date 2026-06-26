# Receipt — LK Ops Hermes Bot activation

Data/hora: 2026-05-26  
Bot: `@LKOps_HermesBot`  
Profile: `/opt/data/profiles/lk-ops`  
Status: gateway ativo em polling mode  
API server: disabled  
Webhook: disabled  
Token: recebido de Lucas, validado e armazenado localmente; valor não documentado.

## O que foi feito

1. Token validado via Telegram `getMe` com username esperado `LKOps_HermesBot`.
2. Profile `lk-ops` criado em `/opt/data/profiles/lk-ops` a partir do profile default.
3. `.env` do profile atualizado com token do bot e permissões `0600`.
4. `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` aplicados no runtime.
5. Webhook herdado do default foi desativado no `config.yaml` do profile para evitar tentativa de bind/rota indevida.
6. `SOUL.md` do profile ajustado para LK Ops/Atendimento.
7. Gateway iniciado somente para o profile `lk-ops`.
8. Verificação por processo confirmou `HERMES_HOME=/opt/data/profiles/lk-ops`, API server off e webhook off.
9. Log confirmou `Connected to Telegram (polling mode)` e `Gateway running with 1 platform(s)`.

## Não ações

- Nenhuma alteração em Docker/VPS/Traefik.
- Nenhum API/webhook público ativado.
- Nenhum cron criado.
- Nenhum write em Shopify, Tiny, CRM, WhatsApp, Klaviyo, n8n ou produção.
- Token não foi salvo no Brain.

## Round-trip Telegram

Validado em 2026-05-26 16:56 UTC.

Evidência sanitizada:
- Gateway do profile `lk-ops` ativo com `HERMES_HOME=/opt/data/profiles/lk-ops`.
- Log registrou inbound Telegram de Lucas no chat do bot às 16:53 UTC.
- Log registrou resposta enviada pelo bot para o mesmo chat.
- Nenhum token foi documentado no Brain.

## Observação de segurança

Como o token foi colado no chat, depois que o bot estiver validado em round-trip, Lucas pode opcionalmente rotacionar o token no BotFather e repetir a ativação com o novo valor.
