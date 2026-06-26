# Hermes Task OS — restart Main/default e ativação final

- Data: 2026-06-25
- Aprovação Lucas: “pode dar restart e ativar”
- values_printed: `false`

## Resultado

O Main/default foi reiniciado por processo detached externo ao gateway atual. O restart inicialmente registrou race/guardrail de PID 1 ainda vivo, mas a validação posterior confirmou novo start time do Main/default.

## Evidência Main/default

| Campo | Antes | Depois |
|---|---:|---:|
| PID | `1` | `1` |
| start_utc | `2026-06-24T23:44:38Z` | `2026-06-25T17:30:49Z` |
| API health | OK | OK |
| Webhook health | OK | OK |
| Telegram state | connected | connected |

Observação: PID continua `1` porque é o processo principal do container, mas o start time mudou, confirmando restart.

## Especialistas pós-restart

O restart do Main/default derrubou temporariamente os especialistas; o watchdog global os reativou em seguida.

Especialistas vivos pós-validação:

- `mordomo`
- `lk-growth`
- `spiti`
- `spiti-atendimento`
- `lk-ops`
- `lk-shopify`
- `lk-trends`
- `lk-collection-optimizer`
- `lk-stock`
- `lk-finance`
- `lk-content`

Todos os especialistas ficaram com API/webhook surfaces fechadas.

## Task OS

A política Task OS universal está presente nos `AGENTS.md` e agora carregada em runtime pelo Main/default reiniciado e pelos especialistas reativados.

## Verificações finais

- Gateways reais vivos: 12.
- Main/default start time pós-restart: `2026-06-25T17:30:49Z`.
- Especialistas vivos: 11.
- Especialistas com API/webhook unsafe surfaces: 0.
- Global gateway watchdog: silent-OK.
- API health: 200.
- Webhook health: 200.
- `hermes-task-os`: running=0; diagnostics limpo.

## Não executado

- Nenhum write externo.
- Nenhuma alteração em secrets/.env/auth.
- Nenhuma alteração de cron schedule/delivery.
- Nenhum deploy/DNS/Traefik.

## Rollback

- AGENTS.md: restaurar backups de `/opt/data/backups/task-os-universal-agents-20260625T165853Z`.
- Watchdog scrub pós-Doppler: reverter patch em `/opt/data/scripts/hermes_all_gateway_watchdog.py`, se necessário.
- Runtime: reexecutar watchdog global para reativar especialistas gerenciados.
