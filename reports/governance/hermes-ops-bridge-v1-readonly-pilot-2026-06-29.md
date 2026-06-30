# Hermes Ops Bridge v1 — piloto local read-only

Data: 2026-06-29

## Resultado

Implementado script local read-only:

`/opt/data/scripts/hermes_ops_bridge_readonly.py`

Sem runtime novo, sem cron, sem dashboard/API, sem restart, sem Docker/VPS/Traefik e sem writes externos.

## Subcomandos v1

| Subcomando | Função | Mutação |
|---|---|---:|
| `status` | resumo executivo de default + profiles | não |
| `profile-map` | configs, Skill Diet, PIDs e gateway_state | não |
| `cron-inventory` | leitura de cron registries locais | não |
| `health` | Brain health + Skill Diet latest | não |
| `logs` | últimos erros/warnings sanitizados | não |
| `smoke` | smoke read-only via broker central | não |
| `packet` | template local de approval packet | stdout somente |
| `receipt` | template local de receipt | stdout somente |

Comandos bloqueados/inexistentes: restart, deploy, Docker, cron mutation, webhook creation, login/reauth, writes externos.

## Piloto executado

Relatórios JSON do piloto gerados por redirecionamento externo ao bridge; o script não possui flag de escrita:

- `reports/governance/ops-bridge/status-2026-06-29.json`
- `reports/governance/ops-bridge/profile-map-2026-06-29.json`
- `reports/governance/ops-bridge/cron-inventory-2026-06-29.json`
- `reports/governance/ops-bridge/health-2026-06-29.json`
- `reports/governance/ops-bridge/logs-2026-06-29.json`
- `reports/governance/ops-bridge/smoke-github-2026-06-29.json`

## Leituras executivas do piloto

- Profiles configurados: `16`.
- Gateways rodando: `13` incluindo default.
- Profiles fora de config v30: `0`.
- Cron inventory: `108` jobs, `90` enabled, `18` paused, `0` enabled non-ok.
- Brain health: return code `0`.
- Smoke GitHub via broker: return code `0`.
- Finding esperado: default PID 1 expõe API/health local; especialistas seguem API/webhook off conforme política anterior.

## Verificação TDD

Teste criado antes do script:

`/opt/data/scripts/tests/test_hermes_ops_bridge_readonly.py`

RED observado: `4 failed` por script inexistente.

GREEN observado: `4 passed` após implementação.

## Guardrails

- `values_printed=false`.
- Sanitização de token/API key/secret/password em stdout/report.
- Nenhum secret value preservado nos artefatos.
- Não altera cron registry; apenas lê JSON local.
- Não altera profile config; apenas lê config/gateway_state/proc/logs.
- `smoke` usa broker central `/opt/data/home/.local/bin/hermes-cli-integrations`.
