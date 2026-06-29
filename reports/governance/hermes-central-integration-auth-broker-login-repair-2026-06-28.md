# Hermes Central Integration Auth Broker — login/instance repair — 2026-06-28

## Status

**Done:** a instância Hermes está saudável, Google Workspace foi reautenticado no broker central, Klaviyo foi corrigido no smoke, e as integrações principais passaram. Em decisão posterior do Lucas, Linear foi removido do inventário/smoke do broker central e não será usado como integração Hermes.

## Escopo executado

- Auditei runtime vivo: main/default + 12 especialistas, health API e cron.
- Corrigi o broker para Google Workspace (`gws`) usar auth central em `/opt/data/runtime/central-auth/gws`.
- Corrigi o smoke de Klaviyo para passar pelo broker e usar timeout adequado.
- Adicionei probe read-only real para Linear via GraphQL viewer, já que o CLI instalado não oferece `whoami` estável.
- Reautentiquei Google Workspace via OAuth humano com a conta `lucascimino@gmail.com`, sem salvar/registrar o OAuth code em artefatos.
- Atualizei a skill `google-workspace` com o procedimento central de auth broker.

## Runtime / instância

| Check | Resultado |
|---|---:|
| Main/default health | OK, Hermes `0.17.0` |
| Cron status | OK, 40 jobs ativos |
| Gateways especialistas | 12/12 vivos |
| API/webhook especialistas | fechados |
| Watchdog global | silent-OK |
| Restart extra | não necessário neste turno |

## Google Workspace central

| Item | Resultado |
|---|---:|
| Conta autorizada | `lucascimino@gmail.com` |
| Auth storage | central, encrypted gws config |
| Config dir | `/opt/data/runtime/central-auth/gws` |
| Directory mode | `0700` |
| Credential file modes | `0600` |
| Scope count | 10 |
| Smoke | OK |
| Values printed | false |

Observação: `gws` criou arquivos de credencial/cache no diretório central. Não copiei credenciais para profiles individuais e não rodei login por agente.

## Smokes finais

| Integração | Status |
|---|---:|
| Vercel | OK |
| GitHub | OK |
| Google Workspace | OK |
| Notion | OK |
| Sentry | OK |
| Shopify LK | OK |
| Supabase | OK |
| Cloudflare/Wrangler | OK |
| Klaviyo | OK |

Linear foi removido do inventário/smoke por decisão do Lucas em 2026-06-28.

## MCP

MCPs testados com conexão e tools discovery OK:

- `time`
- `fetch`
- `sequential_thinking`
- `metricool_readonly`
- `dataforseo`

## Arquivos alterados

- `/opt/data/scripts/hermes_cli_run.py`
- `/opt/data/scripts/hermes_cli_integrations.py`
- `/opt/data/skills/productivity/google-workspace/SKILL.md`
- `/opt/data/skills/productivity/google-workspace/references/central-gws-auth-broker-20260628.md`

## Backup

- `/opt/data/backups/auth-broker-login-fix-20260628T154052Z/`

## Verificação

| Gate | Resultado |
|---|---:|
| `py_compile` scripts | OK |
| unit tests broker | 5/5 OK |
| full CLI smoke | OK sem Linear |
| MCP tests | OK |
| secret literal scan scripts | 0 possible secret literals |
| values_printed | false |
| external writes | 0 |

## Linear decision

Lucas decidiu em 2026-06-28: “não vamos usar o LINEAR, pode deletar essa integração”. A integração Linear foi removida do inventário/smoke do broker central. Não há pendência de token Linear.

## Rollback

```bash
cp /opt/data/backups/auth-broker-login-fix-20260628T154052Z/hermes_cli_run.py.bak /opt/data/scripts/hermes_cli_run.py
cp /opt/data/backups/auth-broker-login-fix-20260628T154052Z/hermes_cli_integrations.py.bak /opt/data/scripts/hermes_cli_integrations.py
python3 -m py_compile /opt/data/scripts/hermes_cli_run.py /opt/data/scripts/hermes_cli_integrations.py
```

Para revogar/recriar Google Workspace central: usar `hermes-cli-run gws auth logout` e repetir reauth controlado no diretório central. Não apagar manualmente credenciais sem backup/approval.
