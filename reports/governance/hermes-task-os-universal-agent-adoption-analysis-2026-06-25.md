# Análise — adoção universal da lógica de tarefas no Hermes

- Data: 2026-06-25
- Pedido Lucas: “todos os nossos agentes vão começar a seguir essa lógica de tarefa para toda a tarefa que tiver no Hermes”.
- generated_at_utc: `2026-06-25T16:45:56.048151+00:00`
- values_printed: `false`

## Veredito

Sim, a lógica deve virar padrão de sistema. Mas não deve ser aplicada como “todo prompt vira card”. O padrão correto é:

```text
Todo trabalho operacional não-trivial vira tarefa rastreável; tarefa simples continua resposta direta.
```

A regra universal deve ser uma **política de funil**, não burocracia.

## Inventário lido agora

- Perfis/configs encontrados: 19 entradas de profile/home, incluindo duplicatas sem config em `home/.hermes`.
- Gateways vivos: 13 processos com `hermes gateway run`.
- Perfis ativos principais: default, mordomo, lk-growth, spiti, spiti-atendimento, lk-ops, lk-shopify, lk-trends, lk-collection-optimizer, lk-stock, lk-finance, lk-content.
- `dispatch_in_gateway=true` aparece em vários profiles/configs; portanto assignee em card pode executar.
- `AGENTS.md` existe em vários especialistas, mas não em todos.
- Skills profile-local são inconsistentes: alguns têm `kanban-orchestrator`, outros não; alguns têm `mesa`, outros não.

## Implicação

Para “todos os agentes seguirem”, precisamos de 3 camadas:

1. **Política canônica Brain** — já criada em `areas/operacoes/rotinas/hermes-task-os-universal-agent-policy-20260625.md`.
2. **Propagação documental profile-local** — patch em `AGENTS.md` de cada profile relevante, com backup.
3. **Ativação runtime** — só se quisermos que gateways já vivos leiam a mudança imediatamente; exige restart controlado por profile, não feito agora.

## Como cada agente deve agir

### Hermes Geral/default

- Orquestra o Task OS.
- Cria policy, board, receipts, approval packets.
- Decide se um pedido vira card, handoff ou resposta direta.

### Especialistas de domínio

Ex.: LK Growth, LK Shopify, LK Ops, LK Stock, LK Trends, LK Finance, LK Content, LKGOC, SPITI, Mordomo.

- Não devem despejar tudo no `hermes-task-os` sem filtro.
- Devem registrar/handoff quando a tarefa é operacional, recorrente, multi-step, aprovada, bloqueada ou precisa voltar depois.
- Devem manter sua fonte canônica de domínio: Brain/Tiny/Shopify/Hub conforme o caso.

### Workers Kanban

- Só executam quando card tiver escopo claro.
- Devem fechar com `kanban_complete` ou `kanban_block`.
- Devem preservar guardrails: sem external write não aprovado.

## O que não fazer

- Não criar card para cada pergunta simples.
- Não transformar Telegram em backlog.
- Não usar `--triage` para backlog passivo.
- Não atribuir assignee sem entender se o dispatcher vai executar.
- Não reiniciar todos gateways sem plano.
- Não tratar “seguir” como autorização ampla para produção.

## Rollout recomendado

### Fase 1 — documental/local, baixo risco

Patchar `AGENTS.md` dos profiles existentes com bloco curto “Task OS universal”.

Sem restart. Sem runtime mutation. Efeito imediato apenas para novas sessões/processos que leem esses arquivos; gateways vivos podem precisar restart para ativar.

### Fase 2 — skill sync seletivo

Atualizar profile-local `kanban-orchestrator` quando existir. Não instalar skill em todos por padrão; muitos especialistas não precisam ser orquestradores.

### Fase 3 — runtime activation opcional

Reiniciar apenas profiles escolhidos, um a um, com backup/rollback/verificação. Não reiniciar tudo de uma vez.

## Recomendação

Aprovar Fase 1 agora: patch documental em `AGENTS.md` dos profiles relevantes + receipt + secret scan. Não reiniciar gateways ainda.

Depois de 24–48h de uso, decidir se algum profile precisa Fase 2/3.
