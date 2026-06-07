# Receipt — Host Docker observability triage — 2026-06-06

Trigger: Lucas respondeu `Fazer` à Mesa COO 2026-06-06 Decisão 2/4.

Escopo aprovado: diagnóstico read-only/sanitizado do timeout de observabilidade Host Docker/SSH; sem Docker restart, sem root fix, sem gateway, sem mudança de rede.

## Ação executada

Rodei o helper read-only:

- `/opt/data/scripts/hermes_host_docker_observability.py`

Relatórios sanitizados gerados:

- `reports/hermes-host-docker-observability-triage-2026-06-06T1006Z.json`
- `reports/hermes-host-docker-observability-triage-2026-06-06T1008Z.json`

## Resultado

O timeout anterior não se repetiu na triagem.

Evidência:

- Host respondeu via SSH read-only.
- Containers esperados encontrados e `running`:
  - `hermes-agent-5ajw-hermes-agent-1`
  - `hermes-agent-5ajw-hermes-telegram-1`
- Runtime em ambos: `Hermes Agent v0.15.2 (2026.5.29.2)`.
- Cron status no host: `Gateway is running`, 27 active jobs.
- `alerts: []` nos relatórios de triagem.

## Achado secundário

Logs recentes do Telegram no host mostram erro recorrente:

- `Field "message_id" must be a valid number`

Classificação: provável bug/ressaca do fluxo de reply/callback/inline button, não incidente de Docker/SSH. Requer investigação read-only de logs/código antes de qualquer gateway restart ou patch ativo.

## Não executado

- Nenhum Docker/container/compose/image swap.
- Nenhum gateway restart/reload.
- Nenhum root/SSH fix.
- Nenhuma alteração de rede.
- Nenhuma alteração de cron.
- Nenhum secret impresso.
- Nenhum write externo/produção.

## Próxima decisão recomendada

Investigar o erro Telegram `message_id` em modo read-only e preparar correção local/testes se confirmado, sem ativar no gateway sem aprovação escopada.
