# Recibo — LK Content gateway reativado e incluído na recuperação global

Data: 2026-06-07
Escopo: perfil Hermes `lk-content` / bot Telegram `@hermes_lk_producaodeconteudo_bot`

## Motivo

Lucas informou que o agente LK Content caiu e pediu:

- reiniciar o agente;
- adicionar o perfil ao processo de recuperação após restart do gateway.

## Pré-estado observado

- Perfil `/opt/data/profiles/lk-content` existia.
- `hermes profile list` mostrava `lk-content` como `stopped`.
- Não havia processo vivo com `HERMES_HOME=/opt/data/profiles/lk-content`.
- Logs indicavam shutdown por `SIGTERM` às 2026-06-07 11:37 UTC.

## Ações executadas

1. Reiniciado somente o gateway do perfil `lk-content`.
2. API Server e Webhook foram forçados fechados no runtime:
   - `API_SERVER_ENABLED=false`
   - `API_SERVER_KEY` vazio
   - `API_SERVER_PORT` vazio
   - `API_SERVER_HOST` vazio
   - `WEBHOOK_ENABLED=false`
   - `WEBHOOK_PORT` vazio
   - `WEBHOOK_SECRET` vazio
3. `lk-content` foi adicionado ao watchdog global/local de recuperação pós-restart:
   - script: `/opt/data/scripts/hermes_all_gateway_watchdog.py`
   - modo: `managed`
   - home: `/opt/data/profiles/lk-content`
   - max_iterations esperado: `60`
4. Backup antes da alteração no watchdog:
   - `/opt/data/scripts/hermes_all_gateway_watchdog.py.bak-lk-content-20260607T115624Z`

## Pós-estado verificado

- Processo vivo único para `lk-content`:
  - PID observado: `2487`
  - binário: `/opt/hermes/.venv/bin/hermes`
  - `HERMES_HOME=/opt/data/profiles/lk-content`
- `gateway_state.json`:
  - `gateway_state=running`
  - `telegram=connected`
- Logs frescos:
  - `Active profile: lk-content`
  - `Agent budget: max_iterations=60`
  - `[Telegram] Connected to Telegram (polling mode)`
  - `✓ telegram connected`
  - `Gateway running with 1 platform(s)`
- Watchdog global:
  - `python3 -m py_compile /opt/data/scripts/hermes_all_gateway_watchdog.py`: OK
  - `/opt/data/scripts/hermes_all_gateway_watchdog.py`: `rc=0`, stdout vazio

## Limites preservados

- Não mexeu em Docker, VPS, Traefik, Hermes principal, Shopify, Tiny, Klaviyo, WhatsApp, e-mail, ads ou crons externos.
- Nenhum token/secret foi registrado neste recibo.
- Alteração foi local ao script de recuperação e ao processo do perfil `lk-content`.

## Status

Concluído. `lk-content` voltou a rodar e passou a fazer parte da recuperação automática local depois de restart do gateway/Main.
