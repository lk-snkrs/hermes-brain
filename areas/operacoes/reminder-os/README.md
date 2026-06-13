# Reminder OS

Status: v0 iniciado em 2026-06-12.

## Tese

Reminder OS é a camada de continuidade operacional do Hermes: impede que trabalhos em construção, aprovações, investigações e melhorias fiquem em stand-by sem dono, próximo passo ou gatilho de retomada.

Não é um app de tarefas genérico. É um sistema de **loops abertos** integrado a Brain, Kanban Hermes, Mesa COO, Memory OS, crons, handoffs e agentes/profiles especialistas nativos do Hermes Agent.

## Diferença para Memory OS

- Memory OS: garante contexto correto e higiene de memória.
- Reminder OS: garante retomada e fechamento de trabalho pendente.

Fórmula operacional:

`evento → loop aberto → dono → próximo passo → gatilho → revisão → fechar / retomar / expirar`

## Escopo v0

1. Criar ledger canônico de reminders/loops abertos.
2. Criar board Kanban `reminder-os` para desenvolvimento e governança do sistema.
3. Criar watchdog local a cada 2h.
4. Alertar Lucas no Telegram apenas quando houver item acionável; estado OK fica silencioso.
5. Preparar contrato para todos os agentes: todo agente deve transformar stand-by em loop rastreável.

## Contrato para todos os agentes

Quando um agente detectar qualquer item que não será resolvido no turno atual, ele deve registrar ou encaminhar um loop Reminder OS com:

- título curto;
- dono lógico;
- próximo passo concreto;
- gatilho de retomada ou data de revisão;
- evidência/link Brain/Kanban/sessão;
- risco de esquecimento;
- estado inicial.

Estados v0:

- `open`
- `waiting_lucas`
- `waiting_event`
- `scheduled_check`
- `kanban_tracked`
- `done`
- `expired`

## Políticas de alerta

- Cadência de verificação: a cada 2h.
- Telegram: só se houver decisão, risco de abandono, item vencido, bloqueio humano, ou loop importante parado.
- OK/silêncio: nenhum output.
- Sem job IDs, JSON bruto, wrappers técnicos ou segredos em mensagem ao Lucas.

## Guardrails

Reminder OS não autoriza execução. Ele só puxa a retomada do loop.

Bloqueado sem aprovação escopada:

- writes externos;
- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail;
- produção/runtime/Docker/VPS/Traefik;
- cron mutation além da cadência v0 aprovada;
- segredos;
- contato com clientes/fornecedores.

## Artefatos

- Ledger: `reminders.jsonl`
- Watchdog: `/opt/data/scripts/reminder_os_watchdog.py`
- Board: `reminder-os`
- Rotina: `../rotinas/reminder-os-v0-2026-06-12.md`
- Spec Memory OS: `memory-os-integration-v1.md`
- Spec Mesa COO: `mesa-coo-integration-v1.md`


## Superfície operacional

Reminder OS usa a estrutura nativa do Hermes Agent: agents/profiles, Brain, Kanban, cron/watchdog e ledger local. Mission Control fica fora do Reminder OS por decisão de Lucas.

## Fase 3 — Memory OS e Mesa COO

- Memory OS deve detectar `Próximos passos` abertos em handoff/receipt/daily/hot e criar ou encaminhar loop Reminder OS apenas quando houver continuidade real, com dedupe por owner + next action + evidence.
- Mesa COO só promove loops acionáveis: `waiting_lucas`, alta severidade, risco real de abandono ou decisão humana clara. Backlog baixo/stale fica local, resumido ou expirado.
- Telegram continua minimalista: uma decisão limpa por vez, sem JSON bruto, job ID, wrapper, stack trace ou secrets.
