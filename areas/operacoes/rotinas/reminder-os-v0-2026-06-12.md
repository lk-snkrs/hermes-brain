# Reminder OS v0 — loop de continuidade operacional

Data: 2026-06-12
Status: ativo em v0 local

## Objetivo

Evitar que trabalhos iniciados no Hermes fiquem em stand-by sem retomada. Reminder OS monitora loops abertos, Kanban e pendências explícitas, e chama Lucas apenas quando há ação necessária.

## Cadência aprovada

- Verificação: a cada 2 horas.
- Entrega: Telegram/origem apenas quando o watchdog encontrar reminder acionável.
- Silent OK: se nada estiver vencido/abandonado/bloqueado, stdout vazio e nenhuma mensagem.

## Fontes v0

1. Ledger canônico: `areas/operacoes/reminder-os/reminders.jsonl`.
2. Kanban canônico do Reminder OS: board `reminder-os` para governança/loops do próprio sistema.
3. Handoffs/receipts/rotinas — integração direta fica para v1, mas o contrato já existe.
4. Memory OS/Mesa COO — devem escrever loops no ledger quando detectarem stand-by.

Regra corrigida em 2026-06-13: backlog de Kanban especialista (`lk-growth-ops`, LK Stock, Mordomo, SPITI, Zipper etc.) **não** deve virar alerta central para Lucas via Hermes Geral. Quando o loop tem dono especialista, o reminder deve ser roteado para a superfície/profile do agente dono; Hermes Geral só recebe alertas de governança/sistema ou escalonamentos sem dono operacional.

## Regra cross-agent

Todo agente deve registrar um Reminder OS loop quando uma tarefa relevante:

- fica para depois;
- depende de Lucas;
- depende de evento externo;
- ficou parcialmente construída;
- tem review futuro;
- precisa de D+N;
- foi bloqueada por approval, dados ou especialista;
- gerou um “próximo passo” que não será executado agora.

## Formato recomendado do ledger

```json
{"id":"rem-20260612-001","title":"...","owner":"Hermes Geral","status":"open","severity":"medium","next_action":"...","due_at":"2026-06-12T17:00:00Z","evidence":"areas/...","risk":"..."}
```

Campos mínimos: `id`, `title`, `owner`, `status`, `next_action`.

Campos úteis: `due_at`, `next_review_at`, `severity`, `source`, `evidence`, `risk`, `created_at`, `updated_at`.

## Estados

- `open`: loop aberto sem bloqueio específico.
- `waiting_lucas`: precisa decisão/resposta do Lucas.
- `waiting_event`: depende de evento externo/sistema/cron/data.
- `scheduled_check`: tem data de revisão.
- `kanban_tracked`: acompanhamento primário no Kanban.
- `done`: fechado.
- `expired`: não faz mais sentido.

## Watchdog v0

Script: `/opt/data/scripts/reminder_os_watchdog.py`

Comportamento:

1. Lê ledger.
2. Lê apenas o board Kanban canônico `reminder-os` por padrão; outros boards só entram com allowlist escopada e plano de roteamento.
3. Detecta items vencidos, `waiting_lucas`, bloqueados antigos e cards `ready` parados dentro do escopo do Reminder OS.
4. Emite mensagem curta apenas se houver item acionável para Hermes Geral/Lucas.
5. Filtra loops com `owner` especialista (`LK Growth`, `LK Stock`, Mordomo, SPITI, Zipper etc.) para não paginar o canal central; esses loops ficam no ledger/health para cobertura, mas a entrega deve ocorrer pela superfície do agente dono quando ela existir.
6. Nunca imprime secrets, JSON bruto ou IDs de cron.

## Guardrail

Reminder OS **não executa** a tarefa lembrada. Ele só reabre o loop para decisão/retomada. Qualquer ação externa/prod/write segue a política normal de aprovação escopada.

## Próximas fases

- v1: adaptar Memory OS receipt/handoff hook para também registrar loop quando houver `next_action` não fechado.
- v2: patchar contratos profile-local dos especialistas para incluir Reminder OS.
- v3: integrar com Mesa COO para transformar stand-by crítico em decisão 1/N.
- v4: criar superfície nativa Hermes Agent para “Loops abertos por dono” usando Brain, Kanban, agents/profiles e relatórios locais; Mission Control fora do Reminder OS.
