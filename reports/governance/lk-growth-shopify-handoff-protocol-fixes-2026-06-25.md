# LK Growth ↔ LK Shopify handoff protocol fixes — 2026-06-25

## Pedido

Lucas pediu executar os três follow-ups após o incidente `t_ae530570`:

1. LK Growth deve revalidar estado Kanban antes de reportar `blocked/gave_up`.
2. Worker/dispatcher deve ter readiness check para `kanban-worker`/profile antes de redespacho.
3. Evidência final de tasks com write externo não pode ficar apenas em scratch workspace.

## Implementado

### 1. Guard de status stale para LK Growth

Criado script local/read-only:

```text
/opt/data/scripts/hermes_kanban_task_status_guard.py
```

Função:

- localiza o task id no board;
- lê `tasks`, `task_runs`, `task_events`, comentários;
- retorna estado atual, última run, event tail e flag `stale_blocked_report_risk`;
- evita reportar `blocked/gave_up` antigo quando houve `unblocked/claimed/completed` depois.

Aplicado em:

```text
/opt/data/profiles/lk-growth/AGENTS.md
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/AGENTS.md
```

### 2. Readiness check de worker/profile

Criado script local/read-only:

```text
/opt/data/scripts/hermes_kanban_worker_readiness.py
```

Função:

- valida `HERMES_HOME` do profile;
- verifica skill exigida, por CLI e filesystem;
- verifica shape de `auth.json` sem imprimir segredo;
- retorna `ok`/`blocked_reason` e `values_printed=false`.

Verificação com `lk-shopify`:

```text
ok=true
required skill: kanban-worker
values_printed=false
```

### 3. Evidência final durável fora de scratch

Preservada evidência fresca do caso `t_ae530570` em Brain:

```text
areas/lk/sub-areas/shopify/evidence/adidas-samba-marrom-20260625T1917Z/admin-readback.json
areas/lk/sub-areas/shopify/evidence/adidas-samba-marrom-20260625T1917Z/public-readback.json
areas/lk/sub-areas/shopify/evidence/adidas-samba-marrom-20260625T1917Z/kanban-show.json
areas/lk/sub-areas/shopify/evidence/adidas-samba-marrom-20260625T1917Z/README.json
```

Aplicado em:

```text
/opt/data/profiles/lk-shopify/AGENTS.md
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/AGENTS.md
```

Também atualizada a skill global `shopify` com referência:

```text
references/lk-shopify-external-write-evidence-preservation-20260625.md
```

E atualizada a skill `kanban-orchestrator` com referência sobre status stale:

```text
references/lucas-kanban-stale-blocked-status-and-worker-retry-20260625.md
```

## Verificação

- `py_compile` OK para os dois novos scripts.
- `hermes_kanban_task_status_guard.py t_ae530570 --board lk-growth-ops` retornou:
  - `ok=true`
  - `status=done`
  - `latest_run.id=18`
  - `latest_run.outcome=completed`
  - `stale_blocked_report_risk=true`
- `hermes_kanban_worker_readiness.py lk-shopify --skills kanban-worker` retornou:
  - `ok=true`
  - `values_printed=false`
- JSONs duráveis de evidência parsearam OK.
- Brain health: `FAIL=0 WARN=0`.
- Secret scan escopado: `high_confidence_secret_hits=0`.

## Writes externos

Nenhum. Apenas arquivos locais/Brain/skills e scripts locais read-only.

## Backup

```text
/opt/data/backups/lk-handoff-protocol-fixes-20260625T192306Z/
```

## Próximo estado esperado

- LK Growth não deve mais responder a Lucas com status Kanban stale sem revalidar `show/runs`.
- Antes de redespachar worker, Hermes pode rodar readiness check do profile/skill.
- LK Shopify deve citar evidência durável no receipt quando uma task external-write roda em scratch workspace.
