# Hermes Task OS — Kanban nativo como Linear interno

- Data: 2026-06-25
- Status: board local criado, **sem execução automática**
- Board: `hermes-task-os`
- Fonte runtime: Hermes Kanban nativo (`/opt/hermes/.venv/bin/hermes kanban`)
- DB: `/opt/data/kanban/boards/hermes-task-os/kanban.db`
- generated_at_utc: `2026-06-25T13:57:49.520449+00:00`
- values_printed: `false`

## Decisão operacional

O Hermes já possui um sistema nativo equivalente a um Linear interno: **Hermes Kanban**. Para Lucas/Cimino, o papel do Kanban será:

- registrar tarefas duráveis;
- separar pendências, bloqueios e aprovações;
- preservar handoff entre profiles;
- permitir auditoria por runs/logs/comments;
- servir como fila operacional para Mesa COO e especialistas.

Não estamos criando um clone novo do Linear. Estamos criando uma camada de governança sobre o Kanban nativo, conectada ao Brain, Mesa COO e Telegram silent-OK.

## Board criado

`hermes-task-os` foi criado sem `--switch`, então o board atual permaneceu `lk-growth-ops`. Nenhum card foi atribuído a worker, nenhum dispatch foi chamado e não há notificações.

Verificações:

- current board preservado: `lk-growth-ops`.
- `hermes-task-os`: 5 cards `ready`.
- running: 0.
- assigned: 0.
- notify subscriptions: 0.
- diagnostics: 0.

## Cards seed

| ID | Card | Status | Assignee |
|---|---|---|---|
| `t_5e84b76c` | Task OS — definir convenção Lucas/Cimino de campos e statuses | `ready` | `unassigned` |
| `t_9a93a4b9` | Task OS — reconciliar boards existentes e cards stale | `ready` | `unassigned` |
| `t_1ed3d96d` | Task OS — integrar Mesa COO com Kanban sem spam | `ready` | `unassigned` |
| `t_6d7720a2` | Task OS — approval packet para primeiro worker read-only | `ready` | `unassigned` |
| `t_6d995d67` | Task OS — dashboard/Telegram UX de acompanhamento | `ready` | `unassigned` |

## Convenção proposta v0

Cada card operacional deve ter no corpo:

```text
Empresa/área:
Dono lógico:
Profile executor candidato:
Risco: A0-A4
Precisa Lucas: sim/não
Fonte:
Evidência/receipt/report:
Próxima ação:
Bloqueio:
Writes externos: permitido? não, salvo aprovação escopada
```

Status Kanban nativo:

- `triage`: entrada ainda ambígua.
- `todo`: especificado, mas aguardando dependências.
- `ready`: pronto para decisão/roteamento, mas **não necessariamente autorizado para worker**.
- `running`: worker ativo.
- `blocked`: precisa Lucas, fonte, approval, credencial, ativo externo ou evento.
- `done`: encerrado com evidência/receipt.
- `archived`: fora de operação ativa.

## Guardrails Lucas/Cimino

1. Em produção atual, `kanban.dispatch_in_gateway=true`; portanto, **atribuir assignee a um card ready pode virar execução real**.
2. Cards novos de governança ficam `unassigned` até approval packet específico.
3. Mesa COO deve ler Kanban como fonte de pendências, mas só mandar Telegram quando houver decisão real, bloqueio ou risco acionável.
4. Writes externos/prod/Docker/VPS/secrets continuam exigindo aprovação escopada, backup/rollback e verificação.
5. Brain continua sendo fonte de verdade para receipts/reports; Kanban é fila/estado operacional.

## Próximo passo recomendado

Executar primeiro o card `Task OS — reconciliar boards existentes e cards stale` de forma **manual/local/read-only**, sem assignee/dispatch, para limpar o estado antigo antes de permitir worker real.
