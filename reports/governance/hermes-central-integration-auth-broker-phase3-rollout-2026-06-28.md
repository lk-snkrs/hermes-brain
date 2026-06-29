# Hermes Central Integration Auth Broker — Fase 3 rollout/runtime — 2026-06-28

## Status

**Done com ressalva controlada:** política propagada, especialistas recarregados, smokes críticos OK. O restart do main/default foi tentado com aprovação escopada, mas o processo PID 1 permaneceu vivo e o CLI retornou `rc=1` por corrida/auto-proteção. Estado final do main/default está saudável por health/status/cron; não forcei Docker/VPS/Traefik.

## Escopo executado

- Propagação documental/canônica do Central Integration Auth Broker para skills, referência CLI/MCP-first e blocos AGENTS com política Shopify CLI oficial.
- Reload de gateways especialistas gerenciados via watchdog central.
- Tentativa aprovada de restart main/default via runner destacado, seguida de validação real.
- Smokes pós-rollout: unit tests, Shopify read-only, mutation block e watchdog silent-OK.

## Alterações locais/documentais

| Superfície | Resultado |
|---|---:|
| AGENTS com bloco Shopify policy encontrados | 29 |
| AGENTS faltando linha do broker | 0 |
| Skills/reference com frase stale de fallback legado | 0 |
| Backup AGENTS | `/opt/data/backups/central-auth-broker-phase3-agents-20260628T152055Z` |

Atualizações principais:

- `areas/operacoes/rotinas/cli-mcp-first-integration-policy.md`
- `skills/productivity/shopify/SKILL.md`
- `skills/productivity/lk-shopify-readonly/SKILL.md`
- `skills/productivity/lk-shopify-product-upload/SKILL.md`
- `skills/productivity/lk-seo-weekly-improvement/SKILL.md`
- `skills/productivity/shopify/references/*`
- `skills/devops/doppler-secrets-operations/SKILL.md`
- 29 arquivos `AGENTS.md` com complemento do broker central

## Runtime reload

### Especialistas gerenciados

Comando controlado: `/opt/data/scripts/reload_managed_gateways_for_auth_broker_policy_20260628.py`.

| Check | Resultado |
|---|---:|
| Watchdog rc | 0 |
| Watchdog stdout nonempty | False |
| Watchdog stderr nonempty | False |
| Managed missing/duplicate | 0 |
| Bad API/webhook surfaces | 0 |

Contagem pós-reload:

```json
{
  "mordomo": 1,
  "lk-growth": 1,
  "spiti": 1,
  "spiti-atendimento": 1,
  "lk-ops": 1,
  "lk-shopify": 1,
  "lk-trends": 1,
  "lk-collection-optimizer": 1,
  "lk-stock": 1,
  "lk-finance": 1,
  "lk-content": 1,
  "lc-claude-cli": 1
}
```

### Main/default

Runner destacado: `/opt/data/scripts/default_gateway_restart_auth_broker_phase3_runner_20260628.py`.

| Check | Resultado |
|---|---:|
| Restart command rc | 1 |
| Health rc | 0 |
| Gateway status rc | 0 |
| Cron status rc | 0 |
| Watchdog rc | 0 |
| Shopify smoke rc | 0 |

Interpretação: `hermes gateway restart` tentou parar PID 1, mas o processo permaneceu vivo e o start detectou "Another gateway instance is already running". Como health/status/cron/watchdog/smoke estão OK, classifiquei como **restart não efetivado/sem necessidade de escalation**. Não executei `--replace`, Docker, VPS, Traefik ou SIGKILL manual adicional.

## Verificações finais

| Gate | Resultado |
|---|---:|
| Unit tests broker | 5/5 OK |
| `py_compile` broker + runner | OK |
| Shopify LK smoke | OK |
| Mutation Shopify sem approval | bloqueada, `rc=64` |
| Managed specialist roster | 12/12 OK |
| Specialist API/webhook surfaces | fechadas |
| Main health | OK, version `0.17.0` |
| Cron status | OK, 40 jobs ativos |
| Watchdog global | silent-OK |
| Secrets impressos | `values_printed=false` |
| Writes externos | 0 |

## Evidência

- Managed reload JSON: `reports/governance/hermes-central-integration-auth-broker-phase3-managed-reload-2026-06-28.json`
- Default restart run dir: `reports/governance/default-gateway-restart-auth-broker-phase3-2026-06-28/`
- Broker tests: `/opt/data/scripts/tests/test_hermes_cli_run.py`
- Broker patch: `/opt/data/scripts/hermes_cli_run.py`
- Backup broker Fase 2: `/opt/data/backups/hermes-cli-run-pre-auth-broker-20260628T145647Z.py`
- Backup AGENTS Fase 3: `/opt/data/backups/central-auth-broker-phase3-agents-20260628T152055Z`

## Rollback

Broker:

```bash
cp /opt/data/backups/hermes-cli-run-pre-auth-broker-20260628T145647Z.py /opt/data/scripts/hermes_cli_run.py
python3 -m py_compile /opt/data/scripts/hermes_cli_run.py
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
```

AGENTS/policy docs: restaurar arquivos do backup `/opt/data/backups/central-auth-broker-phase3-agents-20260628T152055Z` conforme path correspondente.

Runtime: se algum especialista divergir, rodar somente o watchdog global e validar PID/HERMES_HOME/API/webhook; não usar Docker/VPS/Traefik sem nova aprovação.

## Próximos itens

- Não há blocker no caminho crítico Shopify/Auth Broker.
- Health separado já conhecido: Google Workspace `rc=2` e Klaviyo timeout transitório devem ser tratados fora deste PRD.
- Curadoria futura opcional: revisar os 209 matches do drift report para separar histórico/governança de instrução ativa.
