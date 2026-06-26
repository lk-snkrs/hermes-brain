# Definição — Primeiro piloto Kanban controlado Hermes v0.16

Data: 2026-06-06
Card: `t_b1d4b9e4` — `[R2] Definir primeiro piloto Kanban controlado`
Status: planejamento local/documental; sem worker, sem assignee, sem dispatch, sem cron
Owner: Hermes Geral / Operações Hermes
Fonte: `areas/operacoes/prds/hermes-v016-kanban-pilot-controlled-prd-2026-06-06.md`

## Piloto escolhido

Piloto A0/A1 recomendado:

**“Receipt/handoff documental de Operating Layer”**

Motivo:

- já há board real e cards documentais;
- não envolve sistemas externos;
- não envolve produção, cliente, dinheiro, secrets, Docker, Traefik ou Shopify/Tiny;
- valida governança antes de worker automático;
- gera valor imediato para rastreabilidade.

## Escopo do piloto

Inclui:

- cards criados e encerrados manualmente;
- artefatos no Brain;
- receipt por card;
- comments Kanban apontando para artefatos;
- verificação de `running=0`, `by_assignee={}`, `diagnostics=[]`.

Não inclui:

- assignee real;
- worker automático;
- `dispatch`;
- cron;
- Telegram delivery automático;
- integração Dashboard;
- mudança de runtime/config.

## Owner e papéis

- Owner lógico: Hermes Geral.
- Executor nesta fase: Hermes Geral manual/local.
- Reviewer: Lucas por Telegram quando houver decisão.
- Especialistas: apenas destino documental/handoff, não execução.

## Campos obrigatórios para próximos cards do piloto

```yaml
title:
owner_profile: hermes-geral
company_area: operacoes/hermes
risk_level: A0/A1/A2/A3/A4
source_of_truth:
requested_by: Lucas Cimino / Hermes Geral
approval_required: true/false
external_writes_allowed: false
workers_allowed: false
next_step:
evidence_path:
receipt_path:
kill_criteria:
```

## Critérios de sucesso

- 100% dos cards Done têm artifact path e receipt path.
- 0 cards `running` sem approval.
- 0 cards com assignee sem approval para worker.
- 0 Telegram noise por movimentação interna.
- 0 writes externos.
- Board continua auditável por `stats`, `list`, `diagnostics`, `notify-list`.

## Kill criteria

Parar e pedir novo approval se qualquer condição ocorrer:

- necessidade de worker/assignee;
- necessidade de dispatch;
- necessidade de cron/daemon;
- necessidade de Telegram automático;
- necessidade de runtime/config/gateway;
- card tocar produção, Docker, Traefik, Dashboard, secrets, cliente, dinheiro ou write externo.

## Próximo piloto possível após este

Se o piloto documental ficar limpo, preparar novo approval para **um único worker local/read-only** com:

- um card A0/A1;
- profile escolhido;
- toolset mínimo;
- sem write externo;
- rollback por reclaim/reassign/park;
- dispatch dry-run antes;
- execução observada;
- receipt final.

## Resultado

Card `t_b1d4b9e4` pode ser considerado concluído no escopo aprovado: primeiro piloto definido e delimitado; nenhuma execução automática criada.
