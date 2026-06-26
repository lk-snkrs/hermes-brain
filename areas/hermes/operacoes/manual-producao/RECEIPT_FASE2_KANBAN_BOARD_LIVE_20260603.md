# Receipt — Fase 2 Kanban board live setup

Data: 2026-06-03  
Executor: Hermes Geral  
Escopo: local/read-only + criação de board/cards Kanban locais sem assignee.

## O que foi feito

Criado board real Hermes Kanban:

- Slug: `hermes-lk-improvements`
- Nome: `Hermes/LK Improvements`
- Finalidade: Fase 2 — adoção controlada de features Hermes/LK, com backlog persistente, auditável e seguro.

Criados cards iniciais sem assignee real:

- `t_49098f9f` — `[F2][KANBAN][A1] Register live board setup receipt` — status `done`.
- `t_01156a76` — `[F2][PLUGIN][A2] Draft capability-status plugin mini-PRD` — status `ready`, assignee `null`.
- `t_fe598ba5` — `[F2][DELIVERABLE][A2] Standardize deliverable mode and receipts` — status `ready`, assignee `null`.
- `t_cd3dd451` — `[F2][COCKPIT][A1] Revalidate dashboard/API/webhook exposure classification` — status `ready`, assignee `null`.
- `t_45b92440` — `[F2][PILOT][A1] Prepare first read-only Kanban worker approval packet` — status `ready`, assignee `null`.

## Verificação Kanban

Comandos executados:

- `/opt/hermes/.venv/bin/hermes kanban boards list`
- `/opt/hermes/.venv/bin/hermes kanban --board hermes-lk-improvements stats`
- `/opt/hermes/.venv/bin/hermes kanban --board hermes-lk-improvements diagnostics`
- `/opt/hermes/.venv/bin/hermes kanban --board hermes-lk-improvements list --json`

Resultado após setup:

- `ready`: 4
- `done`: 1
- `running`: 0
- `blocked`: 0
- diagnósticos ativos: nenhum
- assignees dos cards ready: `null`

## Guardrails preservados

Não foi feito:

- nenhum card atribuído a worker real;
- nenhum dispatch produtivo;
- nenhum restart de gateway/profile;
- nenhuma alteração Docker/VPS/Traefik/SSH/secrets;
- nenhuma alteração de cron;
- nenhuma ativação de plugin/MCP/hook/goal;
- nenhum write Shopify/Tiny/GMC/Klaviyo/Meta/Crisp/WhatsApp/email;
- nenhum token/secret impresso.

## Próxima decisão

O próximo passo seguro é escolher **um** card para virar piloto real com approval packet separado.

Recomendação: `t_cd3dd451` — revalidar exposição Dashboard/API/webhook — porque é A1/read-only e deve preceder cockpit/plugin público.

Alternativa: `t_01156a76` — mini-PRD do plugin local/read-only — se a prioridade for produto/observabilidade antes de segurança de superfície.
