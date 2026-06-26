# Hermes Task OS — consolidação prioridades 1, 2, 3 e 4

- Data: 2026-06-25
- Pedido Lucas: Fazer 1, 2, 3 e 4.
- generated_at_utc: `2026-06-25T16:01:03.283468+00:00`
- values_printed: `false`

## 1. Rotina de uso consolidada

Criada rotina operacional canônica:

- `areas/operacoes/rotinas/hermes-task-os-operating-routine-20260625.md`

Decisão: `hermes-task-os` é o board canônico do Linear interno; Kanban é backoffice, Mesa COO é superfície de decisão no Telegram.

## 2. Boards antigos revisados

Open tasks encontrados antes da limpeza:

- `hermes-lk-improvements`: 3 cards `ready`, todos `unassigned`.
- `lk-growth-ops`: 6 cards `ready`, todos `unassigned`.
- `hermes-task-os`: 0 cards abertos naquele momento.

Ação executada:

- migrado `hermes-lk-improvements/t_01156a76` para backlog seguro `hermes-task-os/t_6fbf8d6c` (`blocked`, unassigned);
- migrado `hermes-lk-improvements/t_fe598ba5` para backlog seguro `hermes-task-os/t_6e404c9e` (`blocked`, unassigned);
- `hermes-lk-improvements/t_45b92440` arquivado como duplicado concluído pelo piloto worker read-only;
- os 6 cards antigos de `lk-growth-ops` foram consolidados no backlog seguro `hermes-task-os/t_8d2cea05` (`blocked`, unassigned), com regra de revalidar fonte viva/histórico antes de qualquer execução.

Durante a primeira migração, `--triage` disparou especificação/decomposição automática e criou child tasks. Contenção executada no mesmo turno: reclaim/archive dos child tasks acidentais, archive dos cards migrados inseguros e recriação de 3 cards seguros `blocked`/unassigned. Estado final sem running e sem diagnostics.

## 3. Consulta sob demanda local criada

Script local/read-only:

- `/opt/data/scripts/hermes_task_os_summary.py`

Modos testados:

```bash
agora
 decisoes
 bloqueios
```

Resultado de teste:

- `agora`: 3 cards abertos seguros (`blocked`/unassigned);
- `decisoes`: nenhuma decisão acionável;
- `bloqueios`: 3 backlogs bloqueados por guardrail, sem assignee.

Não houve integração Telegram automática, cron mutation ou gateway change.

## 4. Linear externo formalizado como opcional

Decisão operacional: não depender do Linear externo para operação Hermes. O token Linear atual permanece diagnosticado como inválido/revogado/sem acesso; reabrir apenas se Lucas quiser integração externa.

## Guardrails preservados

- Sem Docker/VPS/Traefik/gateway/restart.
- Sem cron mutation.
- Sem Telegram automático.
- Sem write externo.
- Sem Shopify/Tiny/Klaviyo/GSC/GA4/API externa.
- Sem secrets impressos.

## Estado esperado após consolidação

- `hermes-task-os`: 5 done + 3 blocked/unassigned safe backlog.
- Boards antigos sem cards `ready` abertos.
- Nenhum card running.
- Nenhum diagnostics ativo.
