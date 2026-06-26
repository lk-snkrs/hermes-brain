# Receipt — LK specialist gateways pós-restart

Data: 2026-05-30 15:49 UTC

## Pedido Lucas

Lucas corrigiu que os agentes abaixo ficam de fora após restart do Main Hermes e devem ser tratados como superfícies obrigatórias:

- LK Ops/Atendimento — `/opt/data/profiles/lk-ops`
- LK Shopify — `/opt/data/profiles/lk-shopify`
- LK Trends — `/opt/data/profiles/lk-trends`

## Implementado

- Criado script silent-OK: `/opt/data/scripts/lk_specialist_gateways_watchdog.py`
- Criado cron no-agent: `955dc769b5a6` — `LK specialist Telegram gateway watchdog`
- Schedule: `every 1m`
- Deliver: `origin`, mas o script fica em stdout vazio quando está OK ou quando a autocorreção local foi bem-sucedida; stdout só aparece para falha acionável.

## Guardrails

- Não toca Docker, VPS, Traefik, Main Hermes, volumes, rede ou compose.
- Não faz writes em Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/CRM.
- Não imprime tokens.
- Força `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` nos gateways iniciados.
- Remove `API_SERVER_KEY/API_SERVER_PORT/API_SERVER_HOST/WEBHOOK_PORT/WEBHOOK_SECRET/WEBHOOK_HOST` do ambiente herdado.

## Verificação em 2026-05-30 15:49 UTC

- `lk-ops`: processo vivo, `gateway_state=running`, Telegram `connected`, `HERMES_MAX_ITERATIONS=40`, API/webhook off.
- `lk-shopify`: processo vivo, `gateway_state=running`, Telegram `connected`, `HERMES_MAX_ITERATIONS=50`, API/webhook off.
- `lk-trends`: processo vivo, `gateway_state=running`, Telegram `connected`, `HERMES_MAX_ITERATIONS=45`, API/webhook off.
- Cron `955dc769b5a6`: `Last run ... ok`.
- Execução manual do script: stdout vazio (`silent-OK`).

## Atualizações de memória/skill

- User profile compactado com regra pós-restart: validar todos bots, incluindo LK Ops/Shopify/Trends.
- Skill `hermes-agent` atualizada em `references/specialist-gateways-after-main-restart-20260527.md` para registrar o watchdog e a correção de Lucas.
