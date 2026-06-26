# PRD — Reminder OS v1

Data: 2026-06-12
Status: PRD v1 aprovado conceitualmente por Lucas para seguir com desenho/implementação local segura
Dono: Hermes Geral / Operações

## 1. Contexto

Lucas identificou um problema recorrente: várias frentes começam a ser construídas, a conversa muda de foco, e itens ficam em stand-by sem dono, próximo passo, prazo, gatilho de retomada ou fechamento.

O problema não é “falta de lembrete”. É perda de continuidade operacional.

Reminder OS nasce como uma camada transversal do Hermes para impedir abandono silencioso de loops abertos em qualquer agente, perfil, board, rotina ou conversa.

## 2. Objetivo

Criar um sistema operacional de reminders/loops abertos que:

1. esteja presente em todos os agentes;
2. capture pendências relevantes antes que se percam;
3. mantenha dono, próximo passo e gatilho de retomada;
4. revise a cada 2 horas;
5. alerte Lucas no Telegram apenas quando houver ação real;
6. integre com Kanban Hermes, Brain, Memory OS, Mesa COO, handoffs, receipts e agentes/profiles nativos do Hermes Agent;
7. não execute ações sensíveis automaticamente.

## 3. Não objetivos

Reminder OS não é:

- app genérico de tarefas;
- substituto de Kanban;
- substituto de Memory OS;
- executor autônomo de writes externos;
- approval bypass;
- sistema para spammar Lucas com status;
- fonte de verdade de dados vivos.

## 4. Usuários e stakeholders

- Lucas: recebe apenas lembretes acionáveis, decisões e riscos reais de abandono.
- Hermes Geral: orquestra o sistema, governa o contrato e mantém o Brain atualizado.
- Especialistas: LK Growth, LK Stock, LK Shopify, LK Ops, LK Trends, LKGOC, SPITI, Mordomo e demais profiles devem registrar loops quando deixam algo pendente.
- Crons/watchdogs: podem registrar loops e alertar apenas por exceção.
- Kanban: superfície operacional para cards rastreáveis.
- Brain: fonte documental e governança do contrato.

## 5. Princípio de produto

Todo trabalho relevante deve terminar em um dos três estados:

1. fechado;
2. explicitamente abandonado/expirado;
3. registrado como loop Reminder OS com dono, próximo passo e gatilho.

Nada importante deve ficar apenas “na conversa”.

## 6. Modelo mental

Fluxo canônico:

```text
sinal → loop aberto → dono → próximo passo → gatilho → revisão 2h → retomar / fechar / expirar / escalar
```

Exemplos de sinais:

- “seguir depois”;
- “vamos voltar nisso”;
- “falta validar”;
- “depende do Lucas”;
- “bloqueado por aprovação”;
- “quase pronto”;
- “precisa testar amanhã”;
- “especialista deve retomar”;
- card Kanban antigo em `ready`/`blocked`;
- cron reporta falha ou pendência;
- receipt/handoff com `next_action` não fechado.

## 7. Estados

- `open`: loop aberto sem bloqueio específico.
- `waiting_lucas`: precisa decisão/resposta de Lucas.
- `waiting_event`: depende de evento externo/sistema/cron/data.
- `scheduled_check`: tem data de revisão.
- `kanban_tracked`: acompanhamento primário no Kanban.
- `done`: fechado.
- `expired`: não faz mais sentido.

## 8. Schema mínimo do ledger

Fonte v1: `areas/operacoes/reminder-os/reminders.jsonl`

Campos mínimos:

- `id`: identificador estável.
- `title`: título curto.
- `owner`: dono lógico/agente/profile.
- `status`: estado atual.
- `next_action`: próxima ação concreta.

Campos recomendados:

- `source`: conversa, Mesa COO, Kanban, Memory OS, Brain, cron, especialista.
- `severity`: `low`, `medium`, `high`.
- `due_at`: prazo ISO UTC, se existir.
- `next_review_at`: revisão ISO UTC.
- `evidence`: caminho Brain/Kanban/sessão/relatório.
- `risk`: risco se esquecer.
- `created_at`, `updated_at`.

## 9. Kanban

Board canônico: `reminder-os`.

Função do board:

- governar evolução do próprio Reminder OS;
- registrar frentes de implantação;
- auditar cards antigos/stale em outros boards;
- dar visibilidade de próximos passos sem iniciar execução automática.

Regra crítica: atribuir card a profile real pode disparar execução dependendo do dispatcher. Portanto, cards Reminder OS começam `unassigned` por padrão até haver aprovação explícita de execução.

## 10. Watchdog 2h

Cron v1:

- script: `/opt/data/scripts/reminder_os_watchdog.py`;
- frequência: a cada 2h;
- modo: `no_agent=true`;
- entrega: origem/Telegram;
- contrato silent-OK:
  - stdout vazio + rc 0 = sem mensagem;
  - stdout não vazio + rc 0 = alerta acionável;
  - rc != 0 = falha do watchdog.

O watchdog deve:

1. ler ledger;
2. ler boards Kanban;
3. detectar loops vencidos, `waiting_lucas`, bloqueados antigos e cards ready sem dono;
4. suprimir repetição por janela de ruído;
5. nunca imprimir segredos, JSON bruto, job IDs ou wrappers técnicos;
6. nunca executar a tarefa lembrada.

## 11. Política de Telegram

Telegram só deve receber:

- decisão necessária;
- risco real de abandono;
- loop vencido/importante;
- bloqueio humano;
- falha de watchdog;
- resumo explicitamente pedido por Lucas.

Telegram não deve receber:

- OK/status saudável;
- ruído histórico;
- fallback benigno/recuperado;
- dumps de cards;
- paths internos sem necessidade;
- job IDs;
- JSON bruto.

## 12. Contrato cross-agent

Todo agente/worker deve aplicar esta regra:

> Se algo relevante não será resolvido agora, registrar ou encaminhar um loop Reminder OS com dono, próximo passo, evidência e gatilho.

Aplicável a:

- Hermes Geral;
- profiles especialistas;
- workers Kanban;
- crons no_agent;
- subagentes;
- rotinas Brain;
- Mesa COO;
- Memory OS;
- handoffs/receipts.

## 13. Integrações por fase

### Fase 0 — já iniciada

- Brain docs v0.
- Ledger v0.
- Board `reminder-os`.
- Watchdog 2h.
- Regra global no `AGENTS.md` do Brain.

### Fase 1 — agora

- PRD v1.
- Implementation plan.
- Helper CLI/script para adicionar loop com validação de schema.
- Testes offline do watchdog e schema.
- Seeds iniciais para loops reais importantes, sem spam.

### Fase 2 — todos os agentes

- Patch nos `AGENTS.md` dos profiles especialistas.
- Patch em skills centrais de operação para citar Reminder OS.
- Handoff/receipt template passa a incluir campo `reminder_loop` quando houver pendência.

### Fase 3 — Memory OS / Mesa COO

Status 2026-06-12: executada em escopo local/documental.

- Memory OS detecta `next_action`/`Próximo passo` aberto e registra ou encaminha loop com dedupe por owner + next action + evidence.
- Mesa COO promove loops críticos como decisões 1/N apenas quando houver `waiting_lucas`, alta severidade, risco real de abandono ou decisão humana clara.
- Daily/weekly governance mede loops abertos, fechados e expirados sem enviar Telegram em estado saudável.
- Specs canônicas: `areas/operacoes/reminder-os/memory-os-integration-v1.md` e `areas/operacoes/reminder-os/mesa-coo-integration-v1.md`.

### Fase 4 — Hermes Agent nativo read-only

Status 2026-06-12: executada em escopo local/read-only.

- Superfície “Loops abertos” por dono/status/severidade criada via `/opt/data/scripts/reminder_os_report.py`.
- Reports gerados em `reports/reminder-os/open-loops-readonly-2026-06-12.md` e `.json`.
- Sem write externo.
- Sem runtime/cron/gateway mutation.
- Ações continuam apenas como preview/approval packet.

### Fase 5 — Kanban hygiene

Status 2026-06-12: executada em escopo local/Kanban-safe.

- Os 5 cards `ready` do board `reminder-os` foram classificados como **fechar**.
- Motivo: todos eram cards de governança já cobertos por Fases 1–4 concluídas e documentadas.
- Pós-higiene: `done=8`, `ready=0`, `running=0`, sem assignee.
- Sem dispatch automático.
- Sem write externo.
- Sem runtime/cron/gateway mutation.

### Fase 6 — Adoption audit

Status 2026-06-12: executada em escopo local/read-only.

- 10 profiles nativos auditados.
- 10/10 têm `AGENTS.md` com bloco `## Reminder OS`.
- 10/10 preservam política silent-OK.
- 10/10 preservam regra de não executar automaticamente tarefa lembrada.
- Nenhuma lacuna operacional bloqueante.
- Relatório: `reports/reminder-os/adoption-audit-2026-06-12.md`.
- Sem write externo.
- Sem runtime/cron/gateway mutation.

### Fase 7 — Ingress audit read-only

Status 2026-06-12: executada em escopo local/read-only.

- Criado `/opt/data/scripts/reminder_os_ingress_audit.py` para auditar handoffs/receipts/approval-packets/reports com marcador explícito `Reminder OS loop needed`.
- Relatórios gerados em `reports/reminder-os/ingress-audit-2026-06-12.md` e `.json`.
- Resultado atual: `open_needed_count=0`; nenhum artefato recente pede loop sem cobertura ativa no ledger.
- Sem criar loop automaticamente.
- Sem executar card.
- Sem write externo.
- Sem runtime/cron/gateway mutation.

### Fase 8 — Watchdog ingress integration

Status 2026-06-12: executada em escopo local/code-safe.

- O watchdog 2h existente agora consulta a auditoria de ingress.
- Marcadores `Reminder OS loop needed: yes` sem ledger ativo viram candidatos Telegram-safe.
- Marcadores cobertos por ledger ativo ou `loop needed: no` continuam silent-OK.
- Nenhum cron novo foi criado.
- Nenhum loop é criado automaticamente.
- Nenhum card é executado/dispatchado.
- Sem write externo.
- Sem Mission Control.

### Fase 9 — Template coverage audit

Status 2026-06-12: executada em escopo local/documental + script read-only.

- Criado `/opt/data/scripts/reminder_os_template_audit.py` para verificar cobertura dos campos Reminder OS em templates canônicos de handoff/receipt.
- Template central `empresa/contexto/handoff-ledger.md` atualizado com campos explícitos Reminder OS.
- Template executivo `template-receipt-executivo-telegram-safe-v016.md` normalizado para os mesmos nomes de campo.
- Relatórios gerados em `reports/reminder-os/template-audit-2026-06-12.md` e `.json`.
- Resultado atual: `gap_count=0`; 4/4 templates canônicos cobertos.
- Sem cron novo.
- Sem write externo.
- Sem Mission Control.

### Fase 10 — Health gate agregado

Status 2026-06-12: executada em escopo local/code-safe + read-only.

- Criado `/opt/data/scripts/reminder_os_health_gate.py` para consolidar ledger, ingress audit, template audit e Kanban `reminder-os` em um único gate `PASS|FAIL`.
- Relatórios gerados em `reports/reminder-os/health-gate-2026-06-12.md` e `.json`.
- Resultado atual: `status=PASS`, `blocker_count=0`, `warning_count=0`.
- Ledger: `active_count=0`, `due_count=0`, `schema_error_count=0`.
- Ingress: `open_needed_count=0`.
- Templates: `gap_count=0`.
- Kanban: `running_count=0`, `ready sem assignee=0`.
- Sem cron novo.
- Sem loop automático.
- Sem dispatch Kanban.
- Sem write externo.
- Sem Mission Control.

### Fase 11 — Watchdog health/status/index hardening

Status 2026-06-12: executada em escopo local/code-safe/documental.

- O watchdog 2h existente passou a consultar o health gate agregado e alertar apenas se houver blocker real (`status=FAIL`).
- Criado `/opt/data/scripts/reminder_os_status.py` para snapshot on-demand Telegram-safe/read-only.
- `areas/operacoes/MAPA.md` passou a apontar para PRD, plano, hub Reminder OS, health gate e status snapshot.
- Regressões cobrem health gate, watchdog com blocker, status command, ingress e templates.
- Nenhum cron novo foi criado.
- Nenhum loop é criado automaticamente.
- Nenhum card é executado/dispatchado.
- Sem write externo.
- Sem Mission Control.

## 14. Requisitos funcionais

R1. Criar loop Reminder OS via arquivo/CLI/helper local.
R2. Validar schema mínimo antes de aceitar loop.
R3. Rodar watchdog a cada 2h.
R4. Alertar apenas para loops acionáveis.
R5. Suprimir repetição de alertas não resolvidos por janela configurável.
R6. Ler Kanban sem executar cards.
R7. Permitir fechar/expirar loops por edição local/rotina segura.
R8. Documentar contrato em Brain e profile docs.
R9. Não vazar segredos ou dados sensíveis.
R10. Verificar Brain health e testes antes de declarar pronto.

## 15. Requisitos não funcionais

- Silent-OK por padrão.
- Sem dependência de APIs externas para funcionar.
- Read-only para Kanban e dados vivos no watchdog.
- Determinístico e testável offline.
- Telegram-safe.
- Fail-safe: em erro, reportar falha sanitizada; nunca executar ação lembrada.

## 16. Guardrails

Reminder OS não autoriza:

- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail writes;
- contato cliente/fornecedor;
- deploy;
- Docker/VPS/Traefik;
- secrets;
- database migrations/writes;
- runtime profile restart;
- execução automática de card Kanban.

Qualquer uma dessas ações continua exigindo aprovação escopada, backup/rollback e verificação.

## 17. Critérios de aceite

A versão v1 está aceita quando:

1. PRD salvo no Brain.
2. Implementation plan salvo no Brain.
3. Ledger e schema documentados.
4. Watchdog 2h existente e testado.
5. Cron ativo e silent-OK testado.
6. Board `reminder-os` existe com cards governança v1.
7. Contrato global cross-agent documentado.
8. Brain health passa sem FAIL/WARN.
9. Não houve write externo.
10. Lucas recebe próximos passos claros sem ruído técnico.

## 18. Métricas de sucesso

- Loops importantes sem dono: cai ao longo do tempo.
- Pendências reabertas antes de ficarem velhas: aumenta.
- Alertas Telegram por dia: baixos e acionáveis.
- % de loops fechados/expirados: aumenta.
- Cards antigos em `ready`/`blocked`: reduzidos por higiene.
- Menos “quase pronto esquecido”.

## 19. Riscos

- Virar mais um backlog esquecido.
- Spammar Telegram com cards antigos.
- Misturar reminder com autorização de execução.
- Duplicar Memory OS/Kanban.
- Registrar contexto demais no ledger.
- Especialistas não adotarem o contrato.

Mitigações:

- watchdog 2h silent-OK;
- suppressão de repetição;
- contrato cross-agent curto;
- Kanban como superfície, Brain como governança;
- execução sempre separada de lembrança;
- rollout por fases.

## 20. Próximo passo recomendado

Reminder OS v1 está operacional e sem cards `ready` antigos após Fase 5.

Próximo passo recomendado: observar o watchdog 2h e só abrir nova fase quando houver loop real (`waiting_lucas`, risco alto, falha do watchdog ou adoção incompleta por algum perfil). Não criar mais cron, Mission Control surface ou dispatch automático sem aprovação específica.


## Superfície operacional

Reminder OS usa a estrutura nativa do Hermes Agent: agents/profiles, Brain, Kanban, cron/watchdog e ledger local. Mission Control fica fora do Reminder OS por decisão de Lucas.
