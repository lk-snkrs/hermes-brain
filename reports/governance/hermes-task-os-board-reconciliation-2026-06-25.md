# Hermes Task OS — Reconciliação de boards Kanban existentes

- Data: 2026-06-25
- Execução: manual/read-only sobre boards; sem assignee, sem dispatch, sem worker
- Card Task OS executado manualmente: `t_9a93a4b9`
- generated_at_utc: `2026-06-25T14:23:27.582432+00:00`
- values_printed: `false`

## Sumário executivo

Foram reconciliados 6 boards Kanban nativos do Hermes. O sistema já tinha histórico útil (`lk-growth-ops`, `hermes-lk-improvements`, `reminder-os`, `hermes-operating-layer-v016`) e agora tem o board de governança `hermes-task-os`.

Achado principal: existem **14 itens abertos** sem execução ativa. Nenhum está `running`, não há diagnostics ativos e não há subscriptions de notificação nos boards auditados. O risco prático é menos técnico e mais governança: cards antigos `ready` podem ser confundidos com backlog atual se forem executados sem triagem.

## Placar por board

| Board | Total cards | Status | Assignees |
|---|---:|---|---|
| `default` | 0 | `{}` | `{}` |
| `hermes-lk-improvements` | 6 | `{'done': 3, 'ready': 3}` | `{'unassigned': 6}` |
| `hermes-operating-layer-v016` | 5 | `{'done': 5}` | `{'unassigned': 5}` |
| `lk-growth-ops` | 15 | `{'done': 9, 'ready': 6}` | `{'lk-analyst-readonly': 3, 'lk-content-reviewer': 1, 'unassigned': 6, 'hermes-ops-readonly': 3, 'brain-process': 2}` |
| `reminder-os` | 8 | `{'done': 8}` | `{'unassigned': 8}` |
| `hermes-task-os` | 5 | `{'ready': 5}` | `{'unassigned': 5}` |

## Itens abertos classificados

| Board | ID | Título | Status | Assignee | Idade dias | Recomendação |
|---|---|---|---|---|---:|---|
| `hermes-lk-improvements` | `t_01156a76` | [F2][PLUGIN][A2] Draft capability-status plugin mini-PRD | `ready` | `unassigned` | 21.9 | `keep_task_os_backlog` |
| `hermes-lk-improvements` | `t_fe598ba5` | [F2][DELIVERABLE][A2] Standardize deliverable mode and receipts | `ready` | `unassigned` | 21.9 | `keep_task_os_backlog` |
| `hermes-lk-improvements` | `t_45b92440` | [F2][PILOT][A1] Prepare first read-only Kanban worker approval packet | `ready` | `unassigned` | 21.9 | `keep_task_os_backlog` |
| `hermes-task-os` | `t_5e84b76c` | Task OS — definir convenção Lucas/Cimino de campos e statuses | `ready` | `unassigned` | 0.0 | `keep_current_seed` |
| `hermes-task-os` | `t_9a93a4b9` | Task OS — reconciliar boards existentes e cards stale | `ready` | `unassigned` | 0.0 | `keep_current_seed` |
| `hermes-task-os` | `t_1ed3d96d` | Task OS — integrar Mesa COO com Kanban sem spam | `ready` | `unassigned` | 0.0 | `keep_current_seed` |
| `hermes-task-os` | `t_6d7720a2` | Task OS — approval packet para primeiro worker read-only | `ready` | `unassigned` | 0.0 | `keep_current_seed` |
| `hermes-task-os` | `t_6d995d67` | Task OS — dashboard/Telegram UX de acompanhamento | `ready` | `unassigned` | 0.0 | `keep_current_seed` |
| `lk-growth-ops` | `t_90667bc2` | LK Stock/Sourcing — lead time canônico por SKU/tamanho | `ready` | `unassigned` | 45.5 | `review_stale` |
| `lk-growth-ops` | `t_e3121949` | LK Stock/Sourcing — investigar SKUs sem depósito oficial explícito | `ready` | `unassigned` | 45.5 | `review_stale` |
| `lk-growth-ops` | `t_2b69dfc8` | SEO/Google — Search Console/Search Central backlog | `ready` | `unassigned` | 45.6 | `review_stale` |
| `lk-growth-ops` | `t_305bf6e9` | LK Growth Ops — recheck data fechada 2026-05-10 | `ready` | `unassigned` | 45.6 | `review_stale` |
| `lk-growth-ops` | `t_389f0fbf` | LK Weekly Influencer Email — corrigir no-creatives/email-safe | `ready` | `unassigned` | 45.6 | `review_stale` |
| `lk-growth-ops` | `t_555772ac` | LK Weekly Influencer Email — validar preview Klaviyo real | `ready` | `unassigned` | 45.6 | `review_stale` |

## Classificação

### Manter como Task OS atual

- Os 5 cards do board `hermes-task-os` são seeds atuais, intencionalmente `unassigned`.
- Não devem ser atribuídos a worker até existir approval packet específico.

### Revisar como backlog/stale antes de qualquer worker

- Os 6 cards `ready` do board `lk-growth-ops` são antigos, criados no piloto LK Growth Ops.
- Eles têm valor como histórico/backlog, mas não devem ser executados automaticamente sem revalidação de fonte viva e histórico recente.
- Recomendação: transformar em cards Task OS revisados ou arquivar após impacto review.

### Migrar/referenciar backlog de melhorias

- Os 3 cards `ready` de `hermes-lk-improvements` são backlog de governança F2.
- Recomendação: manter como backlog, mas espelhar a decisão no `hermes-task-os` antes de executar.

### Sem ação

- `default`: vazio.
- `hermes-operating-layer-v016`: sem abertos.
- `reminder-os`: sem abertos.

## Regra operacional proposta

1. `hermes-task-os` vira board de governança central para novas pendências do Hermes/Linear interno.
2. Boards de domínio (`lk-growth-ops`, `reminder-os`) podem continuar existindo, mas qualquer execução real deve passar por card/pacote no Task OS se houver risco, stale ou necessidade Lucas.
3. Cards `ready` antigos (>30 dias) não entram em execução; primeiro viram `review_stale`.
4. Nenhum assignee em card `ready` sem approval, porque `kanban.dispatch_in_gateway=true`.

## Próximo passo recomendado

Executar o próximo card Task OS:

- `t_5e84b76c` — definir convenção Lucas/Cimino de campos e statuses.

Depois disso, fazer uma ação de higiene: comentar/arquivar ou migrar os 6 cards antigos de `lk-growth-ops`, mas somente após confirmar se Lucas quer manter LK Growth board histórico ou centralizar no Task OS.
