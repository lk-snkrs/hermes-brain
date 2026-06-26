# Audit — Hermes Task OS / Kanban — 2026-06-26

Data UTC: 2026-06-26T12:20Z–12:33Z

## Veredito

Estado geral: **funcionou** para o caso NB740 e para o desenho Task OS, com **1 correção local de evidência aplicada** e **1 erro externo ao Task OS encontrado**.

O Task OS cumpriu o contrato principal:

- decisão Mesa COO virou trabalho rastreável;
- LK Shopify e LK Stock executaram em perfis donos;
- writes externos ficaram em `0`;
- tarefa Shopify ficou `blocked` em vez de executar write não aprovado;
- Stock fechou evidência read-only;
- orquestrador comentou o resultado final e a frente NB740 permaneceu bloqueada.

## Fontes auditadas

- Kanban CLI em `/opt/data/hermes-0.15.1-venv/bin/hermes`, `HERMES_HOME=/opt/data`.
- Board `lk-growth-ops`.
- Board `hermes-task-os`.
- Scripts guard:
  - `/opt/data/scripts/hermes_kanban_task_status_guard.py`
  - `/opt/data/scripts/hermes_kanban_worker_readiness.py`
  - `/opt/data/scripts/test_kanban_handoff_guards.py`
- Brain artifacts NB740 e receipts.
- Cron registry `/opt/data/cron/jobs.json`.

## Resultado dos boards

### `lk-growth-ops`

- Total: 23 cards.
- Status atuais: `done=15`, `blocked=2`.
- `ready=0`, `running=0`.
- Diagnostics: `[]`.
- Dispatch dry-run: `Spawned=0`, `Reclaimed=0`, `Auto-blocked=0`, `Promoted=0`.
- Notify subscriptions: nenhuma.

Blocked atuais:

1. `t_1f079009` — LK Shopify NB740: bloqueado corretamente por falta de estoque/publicação aprovada.
2. `t_5db8be73` — card anterior NB740 + ASICS Gel NYC: bloqueado corretamente no subescopo NB740; ASICS já havia avançado.

### `hermes-task-os`

- Total: 24 cards.
- Status atuais: `done=5`, `blocked=3`, `archived=16`.
- `ready=0`, `running=0`.
- Diagnostics: `[]`.
- Dispatch dry-run: `Spawned=0`, `Reclaimed=0`, `Auto-blocked=0`, `Promoted=0`.
- Notify subscriptions: nenhuma.

Blocked atuais são backlog seguro sem assignee:

- `t_8d2cea05` — revalidar LK Growth antigo antes de execução.
- `t_6e404c9e` — política deliverable mode e receipts.
- `t_6fbf8d6c` — capability-status plugin mini-PRD.

Todos estão bloqueados como **não-executáveis** até approval packet explícito; isso é estado correto, não falha.

## Caso NB740 — tarefas auditadas

### `t_0e4f7612` — LK Stock validação inicial

- Status: `done`.
- Assignee: `lk-stock`.
- Último run: `completed`.
- Duração: ~4m.
- Veredito: 8/8 SKUs `U740GP2-*` com match exato Shopify↔Tiny e saldo 0 no depósito Tiny `LK | CONTROLE ESTOQUE`.
- Resultado: `indisponível-sem venda` / não publicável por estoque.

### `t_1f079009` — LK Shopify publicabilidade/coleção NB740

- Status: `blocked`.
- Assignee: `lk-shopify`.
- Último run: `blocked`.
- Comentários: 2.
- Guard anti-stale: `stale_blocked_report_risk=false`.
- Estado atual é seguro de reportar: `safe_to_report_current_blocked=true`.
- Motivo: Shopify validou read-only produto `ARCHIVED`, sem `publishedAt`, sem `onlineStoreUrl`, sem `resourcePublications`, collection `new-balance-740` ausente; aguardar Stock/sem write.
- Comentário do orquestrador registrou que Stock confirmou saldo 0 e que o approval packet condicional não deve ser executado.

### `t_55c1f648` — LK Stock validação criada por Shopify

- Status: `done`.
- Assignee: `lk-stock`.
- Último run: `completed`.
- Duração: ~3m.
- Veredito: 8/8 SKUs `U740GP2-*` com match exato Shopify↔Tiny, saldo 0 em todos; não há correção SKU/Tiny necessária.

## Evidence/Brain artifacts

Confirmados existentes:

- `areas/lk/sub-areas/collection-optimizer/approval-packets/20260626T0905Z-new-balance-740-unblock-readonly-packet.md`
- `areas/lk/sub-areas/shopify/handoffs/2026-06-26-new-balance-740-publicability-collection-request.md`
- `areas/lk/sub-areas/shopify/handoffs/2026-06-26-new-balance-740-publicability-shopify-readonly-result.md`
- `areas/lk/sub-areas/shopify/approval-packets/2026-06-26-new-balance-740-publicability-write-preview-blocked-pending-stock.md`
- `areas/lk/sub-areas/shopify/snapshots/2026-06-26-new-balance-740-shopify-readonly-snapshot.json`
- `areas/lk/sub-areas/stock/handoffs/2026-06-26-new-balance-740-publicavel-stock-validation-request.md`
- `areas/lk/sub-areas/stock/handoffs/2026-06-26-new-balance-740-stock-validation-result.md`
- `areas/lk/sub-areas/stock/handoffs/2026-06-26-new-balance-740-publicability-stock-validation-t_55c1f648.md`
- `areas/lk/sub-areas/collection-optimizer/receipts/20260626T0919Z-new-balance-740-remains-blocked-readonly.md`

## Correção local aplicada durante audit

O snapshot Shopify read-only citado no receipt NB740 não estava no checkout operacional atual depois da troca do Brain para `main`, mas existia no backup pré-switch.

Restaurei de:

```text
/opt/data/hermes_bruno_ingest/hermes-brain.backup-pre-main-switch-20260626T102451Z/areas/lk/sub-areas/shopify/snapshots/2026-06-26-new-balance-740-shopify-readonly-snapshot.json
```

Para:

```text
areas/lk/sub-areas/shopify/snapshots/2026-06-26-new-balance-740-shopify-readonly-snapshot.json
```

Validação: JSON parse OK.

Observação: arquivos `.json` de snapshot/runtime podem ficar fora da allowlist do Brain Sync. O artefato local foi restaurado para consistência da evidência; versionamento de snapshots JSON deve seguir política/allowlist separada.

## Verificações

- `hermes kanban --board lk-growth-ops stats --json`: OK.
- `hermes kanban --board lk-growth-ops diagnostics --json`: `[]`.
- `hermes kanban --board hermes-task-os stats --json`: OK.
- `hermes kanban --board hermes-task-os diagnostics --json`: `[]`.
- `dispatch --dry-run --max 3` em `lk-growth-ops`: 0 spawn/reclaim/promote/auto-block.
- `dispatch --dry-run --max 3` em `hermes-task-os`: 0 spawn/reclaim/promote/auto-block.
- `hermes_kanban_task_status_guard.py` nos cards NB740: sem risco stale.
- `hermes_kanban_worker_readiness.py` para `lk-stock`, `lk-shopify`, `default`, `hermes-ops-readonly`: OK.
- `test_kanban_handoff_guards.py`: OK.
- `py_compile` scripts guard: OK.
- Brain health: OK.
- Strict-runtime guard: `fail_count=0`.

## Erros ou atenção

### 1. Task OS/Kanban atual: sem erro bloqueante

Não encontrei card running preso, claim ativo, diagnóstico ativo, notificação vazando, dispatch que spawnaria trabalho indevido, nem status NB740 stale.

### 2. Dívida histórica: runs antigos crashed/reclaimed existem

Existem runs antigos em `lk-growth-ops` e `hermes-task-os` com outcomes `crashed`, `reclaimed` ou `spawn_failed`, mas eles já foram absorvidos por correções/arquivamento/guardrails anteriores. Não aparecem como falha ativa:

- `lk-growth-ops`: failures atuais vazios.
- `hermes-task-os`: uma task arquivada (`t_c1d83f75`) preserva `consecutive_failures=2`, mas está `archived`; o guard indica que não deve ser reportada como bloqueio atual sem rechecagem.

### 3. Erro real fora do Task OS

O audit de crons encontrou 1 job ativo non-OK fora do Task OS:

```text
LK 09h previous-day sales report external delivery
last_status=error
causa sanitizada: generated payload missing message/html/email_meta
```

Impacto: não bloqueia Task OS/Kanban, mas é falha operacional separada de relatório externo LK e deve virar próxima correção se Lucas quiser.

## Veredito final

**Task OS funcionou.**

Para a decisão NB740, o fluxo correto aconteceu: decisão → cards rastreáveis → especialistas donos → evidência read-only → bloqueio seguro em vez de write indevido → receipt final.

O que não está “perfeito”: há dívida histórica arquivada e um erro separado no cron de relatório externo LK, mas não encontrei erro ativo no Task OS/Kanban em si.
