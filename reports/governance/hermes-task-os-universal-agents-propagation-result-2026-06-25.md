# Hermes Task OS — propagação universal nos agentes

- Data: 2026-06-25
- Pedido/aprovação Lucas: aprovada Opção A — patch documental sem restart.
- generated_at_utc: `2026-06-25T17:01:31.060811+00:00`
- values_printed: `false`

## Resultado

A política Task OS universal foi propagada para os `AGENTS.md` dos profiles existentes e para o `AGENTS.md` raiz do Brain.

## Escopo executado

- Profiles/runtime documentais alvo: 17
- Documento Brain alvo: 1
- Backups criados: 18
- Backup root: `/opt/data/backups/task-os-universal-agents-20260625T165853Z`

## Arquivos atualizados

- `default`
- `profiles/lk-collection-optimizer`
- `profiles/lk-content`
- `profiles/lk-finance`
- `profiles/lk-growth`
- `profiles/lk-ops`
- `profiles/lk-shopify`
- `profiles/lk-stock`
- `profiles/lk-trends`
- `profiles/mordomo`
- `profiles/spiti`
- `profiles/spiti-atendimento`
- `brain-root`

## Arquivos criados

- `profiles/brain-process`
- `profiles/hermes-ops-readonly`
- `profiles/lc-claude-cli`
- `profiles/lk-analyst-readonly`
- `profiles/lk-content-reviewer`

## Regra propagada

Todos os agentes passam a ter instrução local/documental de que:

- trabalho operacional não-trivial vira tarefa rastreável, handoff ou receipt;
- resposta simples continua direta;
- Telegram/Mesa COO só recebe decisão, bloqueio, falha ou aprovação acionável;
- `ready` + `assignee` pode executar quando `dispatch_in_gateway=true`;
- backlog passivo não deve usar `--triage`; usar `blocked`/unassigned ou `ready`/unassigned quando seguro;
- A3/A4 e writes sensíveis exigem aprovação escopada, backup/rollback e verificação.

## Não executado

- Nenhum gateway restart.
- Nenhum Docker/VPS/Traefik.
- Nenhuma alteração em `.env`, `auth.json`, secrets ou provider credentials.
- Nenhum cron mutation.
- Nenhum card Kanban criado/atribuído/despachado.
- Nenhum external write.

## Verificações

- Cobertura: 18/18 arquivos com marcador exatamente uma vez.
- Secret scan scoped: 0 hits.
- Brain health: FAIL=0, WARN=0.
- Kanban `hermes-task-os`: running=0, diagnostics limpo.
- Gateway process count após patch: 13; sem restart intencional.

## Ativação

Isto é **configurado/documentado**, não necessariamente **ativo em processos gateway já vivos**.

Para ativação imediata em runtimes vivos, seria necessária Fase 3: restart controlado profile por profile, com approval separado.

## Rollback

Restaurar os backups em `/opt/data/backups/task-os-universal-agents-20260625T165853Z` para os respectivos `AGENTS.md`.
