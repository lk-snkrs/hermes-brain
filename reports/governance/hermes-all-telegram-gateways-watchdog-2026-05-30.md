# Receipt — watchdog global de gateways Telegram Hermes

Data: 2026-05-30 15:56 UTC

## Correção de Lucas

Lucas corrigiu que a solução não deveria ser um watchdog/hotdog só para LK Ops/Atendimento, LK Shopify e LK Trends. A lógica correta é verificar se já existem watchdogs para os outros agentes e, se a cobertura estiver fragmentada, criar um watchdog global para todos os gateways Telegram esperados.

## Inventário encontrado

Profiles/bots runtime esperados:

- Main Hermes — `/opt/data` — check-only por ser foreground/container-sensitive.
- Mordomo — `/opt/data/profiles/mordomo`.
- LK Growth — `/opt/data/profiles/lk-growth`.
- SPITI — `/opt/data/profiles/spiti`.
- LK Ops/Atendimento — `/opt/data/profiles/lk-ops`.
- LK Shopify — `/opt/data/profiles/lk-shopify`.
- LK Trends — `/opt/data/profiles/lk-trends`.

Também existem profiles com token mas sem gateway runtime esperado agora (`brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`). Eles não foram colocados no auto-start global para não ativar agentes read-only/preparados por engano.

## Implementado

- Script global: `/opt/data/scripts/hermes_all_gateway_watchdog.py`
- Cron global: `b78ae7ac81d0` — `Hermes all Telegram gateways watchdog`
- Schedule: `every 1m`
- Modo: `no_agent`, silent-OK
- Delivery: `origin` apenas para alertas acionáveis; stdout vazio = OK/self-heal silencioso.

## Watchdogs antigos pausados para evitar fragmentação/race

- `ac0b440e2643` — Mordomo Telegram gateway watchdog
- `876d54c62ccd` — LK Growth Telegram gateway watchdog
- `663e3e6a148c` — SPITI Telegram gateway watchdog
- `955dc769b5a6` — LK specialist Telegram gateway watchdog

Scripts antigos foram preservados para rollback manual, mas a cobertura canônica agora é o watchdog global.

## Guardrails do watchdog global

- Não mexe em Docker/VPS/Traefik/Main/container/volumes/networks.
- Main Hermes é apenas verificado; não é iniciado pelo script.
- Secondary profiles são iniciados apenas localmente se ausentes.
- API/webhook forçados off nos secondary profiles.
- Remove env herdada de `API_SERVER_KEY/API_SERVER_PORT/API_SERVER_HOST/WEBHOOK_PORT/WEBHOOK_SECRET/WEBHOOK_HOST`.
- Não imprime tokens.
- Não faz writes externos.
- Usa lock em `/tmp/hermes_all_gateway_watchdog.lock` para evitar corrida entre ticks.
- Conta processos reais por `/proc/<pid>/cmdline` argv + `/proc/<pid>/environ` `HERMES_HOME`, evitando falso positivo de shell wrapper.

## Verificação

Cron global `b78ae7ac81d0` rodou com status `ok` em 2026-05-30 15:54 UTC.

Execução manual do script: stdout vazio (`silent-OK`).

Estado verificado:

- Main: processo vivo, `gateway_state=running`, Telegram `connected`.
- Mordomo: processo vivo, `gateway_state=running`, Telegram `connected`.
- LK Growth: processo vivo, `gateway_state=running`, Telegram `connected`.
- SPITI: processo vivo, `gateway_state=running`, Telegram `connected`.
- LK Ops/Atendimento: processo vivo, `gateway_state=running`, Telegram `connected`.
- LK Shopify: processo vivo, `gateway_state=running`, Telegram `connected`.
- LK Trends: processo vivo, `gateway_state=running`, Telegram `connected`.

## Atualizações de memória/skill

- User memory compactada: `Pós-restart: watchdog global p/ todos gateways Telegram.`
- Skill `hermes-agent` atualizada em `references/specialist-gateways-after-main-restart-20260527.md` com o cron global e a desativação dos watchdogs fragmentados.
