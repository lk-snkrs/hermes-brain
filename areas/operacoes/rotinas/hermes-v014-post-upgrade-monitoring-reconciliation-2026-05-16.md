# Hermes v0.14 — Reconciliação pós-upgrade e monitoramento

Data: 2026-05-16 08:31 BRT  
Contexto: alerta do watchdog `edd06fe19397` após produção passar de v0.13 para v0.14.  
Ação: inspeção read-only + ajuste de expectativas dos watchdogs/helpers; nenhuma mutação Docker/compose/gateway/host executada nesta reconciliação.

## Situação observada

O watchdog `Hermes runtime + cron watchdog no_agent` alertou:

- Esperado: `v0.13.0`.
- Obtido: `Hermes Agent v0.14.0 (2026.5.16)`.

Após inspeção read-only:

- `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes --version` retornou `Hermes Agent v0.14.0 (2026.5.16)`.
- `hermes cron status` retornou gateway/scheduler rodando, PID `7`, 14 jobs ativos.
- API local `/health` retornou `200` / `ok`.
- Helper Hostinger/Docker confirmou containers `running`:
  - `hermes-agent-5ajw-hermes-agent-1` — `hermes-agent-custom:v0.14.0-20260516`.
  - `hermes-agent-5ajw-hermes-telegram-1` — `hermes-agent-custom:v0.14.0-20260516`.

Conclusão: Hermes voltou/está rodando em v0.14. O alerta era drift de expectativa dos monitores, não evidência de gateway fora.

## Correção aplicada

Atualizados em modo local/read-only operacional:

- `/opt/data/scripts/hermes_runtime_cron_watchdog.py`
  - `EXPECTED_VERSION_FRAGMENT = "v0.14.0"`.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`
  - cópia fonte no Brain atualizada.
- `/opt/data/scripts/hermes_host_docker_observability.py`
  - `EXPECTED_VERSION = "Hermes Agent v0.14.0 (2026.5.16)"`.
  - `EXPECTED_IMAGE_FRAGMENT = "hermes-agent-custom:v0.14.0-20260516"`.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_host_docker_observability.py`
  - cópia fonte no Brain atualizada.
- Cron `f5a23dd6a1bd` atualizado para tratar v0.14 como produção esperada.
- Skill `lucas-hermes-continuous-improvement` atualizada com nota runtime v0.14.

## Verificação pós-correção

- `python3 /opt/data/scripts/hermes_runtime_cron_watchdog.py`: `rc=0`, stdout vazio.
- Helper Hostinger/Docker pós-ajuste salvou:
  - `reports/hermes-host-docker-observability-2026-05-16-post-v014-fixed.json`.
- `alerts`: `[]`.
- Containers seguem `running` com imagem `hermes-agent-custom:v0.14.0-20260516`.

## Guardrails

Não foi executado nesta reconciliação:

- restart de gateway/container;
- alteração de Docker/compose/Traefik/host/root/SSH;
- alteração de secrets;
- escrita em banco/Shopify/campanhas;
- envio externo.

## Próximo passo

Monitorar o próximo run automático do watchdog às 12:00 UTC. Com as expectativas corrigidas para v0.14, ele deve voltar ao contrato silencioso: `rc=0` + stdout vazio = sem Telegram.
