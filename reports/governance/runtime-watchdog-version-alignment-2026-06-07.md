# Runtime watchdog version alignment — 2026-06-07

## Contexto

O watchdog `Hermes runtime + cron watchdog no_agent` alertou em 2026-06-07 04:30 UTC que esperava `v0.15.2`, mas o runtime local respondeu `Hermes Agent v0.16.0 (2026.6.5)`.

## Classificação

- Contexto: LC Hermes / Infra governança local.
- Risco: A1 local/read-only + alinhamento documental de watchdog.
- Produção: nenhum Docker, gateway, compose, Traefik, porta, secret, cron real ou sistema externo foi alterado.

## Ação aplicada

Atualizei apenas a expectativa de versão dos watchdogs/helpers locais e seus espelhos no Brain:

- `/opt/data/scripts/hermes_runtime_cron_watchdog.py`: `EXPECTED_VERSION_FRAGMENT = "v0.16.0"`.
- `areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`: espelho Brain alinhado.
- `/opt/data/scripts/hermes_host_docker_observability.py`: `EXPECTED_VERSION = "Hermes Agent v0.16.0 (2026.6.5)"`.
- `areas/operacoes/scripts/hermes_host_docker_observability.py`: espelho Brain alinhado.

## Verificação

- `date -Iseconds`: `2026-06-07T05:00:37+00:00`.
- `hermes --version`: `Hermes Agent v0.16.0 (2026.6.5)`.
- `py_compile`: OK para os dois scripts em `/opt/data/scripts/` e os dois espelhos do Brain.
- Execução manual de `/opt/data/scripts/hermes_runtime_cron_watchdog.py`: `rc=0` com stdout vazio; silent-OK restaurado.
- Host Docker observability recheck escreveu `reports/hermes-host-docker-observability-2026-06-07-watchdog-recheck.json` com containers esperados `running`, ambos reportando `Hermes Agent v0.16.0 (2026.6.5)`, cron/gateway vivo e `alerts: []`. Uma tentativa anterior expirou em 35s, mas a repetição read-only fechou a lacuna.

## Próxima regra

Depois de qualquer upgrade efetivo de runtime, alinhar no mesmo ciclo os watchdogs/helpers que validam versão esperada e verificar com `py_compile` + execução manual silent-OK. Se o helper host falhar por timeout, registrar recibo sanitizado e não transformar isso em restart/Docker mutation sem aprovação.
