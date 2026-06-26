# Hermes Task OS — auditoria final: todo agente sabe usar?

- Data: 2026-06-25
- Pedido Lucas: “faça mais uma vez, pense, se todo agente vai saber usar o Task OS”
- values_printed: `false`

## Veredito

**Sim para os profiles Hermes existentes e para os gateways ativos, agora com cobertura também para cron agents.**

A primeira propagação em `AGENTS.md` ensinava os agentes interativos/contexts. A auditoria adicional encontrou uma lacuna importante: crons agent-driven sem `workdir` carregam `SOUL.md` (`load_soul_identity=True`) e não necessariamente `AGENTS.md` (`skip_context_files=True`).

Correção executada: propagar o bloco Task OS universal também para os `SOUL.md` dos 17 profiles.

## Cobertura verificada

| Superfície | Resultado |
|---|---:|
| Profiles com `AGENTS.md` Task OS | 17/17 |
| Profiles com `SOUL.md` Task OS | 17/17 |
| Gateways vivos | 12 |
| Gateways vivos apontando para AGENTS+SOUL com marcador | 12/12 |
| AGENTS nonconforming | 0 |
| SOUL nonconforming | 0 |
| Secret scan AGENTS+SOUL | 0 hits |
| Watchdog global | silent-OK |
| Kanban diagnostics | limpo |

## O que cada agente agora sabe

- Trabalho operacional não-trivial vira tarefa rastreável, handoff ou receipt.
- Resposta simples/factual/trivial continua direta.
- Antes de sugerir melhoria em superfície já trabalhada, verificar histórico/fonte canônica.
- Criar/usar card quando houver continuidade, múltiplos passos, multiagente, risco A2+, approval, bloqueio, rotina, auditoria ou retomada futura.
- Fechar com evidência: `done` + receipt/handoff/report, ou `blocked` com pergunta/owner claro, ou `archived/stale` com motivo.
- Mesa COO/Telegram só recebe decisão real, bloqueio concreto, falha atual, aprovação necessária ou alerta acionável.
- Com `dispatch_in_gateway=true`, `ready` + `assignee` pode executar.
- Não usar `kanban create --triage` para backlog passivo em produção.
- A3/A4 e writes sensíveis exigem aprovação escopada, backup/rollback e verificação.

## Limites honestos

- **Agentes existentes:** cobertos.
- **Gateways vivos:** cobertos e reiniciados anteriormente; arquivos atuais também têm AGENTS+SOUL.
- **Crons agent-driven:** agora cobertos via SOUL.md no próximo run.
- **No-agent scripts:** não são LLM agents; só seguem Task OS se script/cron wrapper for desenhado para isso.
- **Futuros profiles:** precisam copiar o template AGENTS+SOUL ou passar pelo checklist de criação.
- **Agentes externos/CLI como Codex/Claude chamados manualmente:** precisam receber contexto Task OS no prompt ou carregar skill/AGENTS do profile; não herdam automaticamente se rodados fora do Hermes profile.

## Backups

- AGENTS.md: `/opt/data/backups/task-os-universal-agents-20260625T165853Z`
- SOUL.md: `/opt/data/backups/task-os-universal-soul-20260625T174502Z`

## Aprendizado registrado

Atualizada a skill `runtime-profile-map` com a referência:

`references/task-os-soul-cron-propagation-20260625.md`
