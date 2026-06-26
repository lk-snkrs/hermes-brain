# PRD — Piloto Kanban controlado no Hermes v0.16

Data: 2026-06-06T16:40:25Z
Status: PRD/documental — nenhum board, worker, daemon, cron ou execução automática criado nesta fase
Owner: Hermes Geral / Operações Hermes

## Problema

O Hermes já opera com múltiplos agentes e rotinas. Sem um board operacional controlado, iniciativas ficam dispersas entre Telegram, Brain, crons e perfis especialistas. Porém Kanban mal ativado pode virar swarm barulhento com execução automática sem governança.

## Objetivo

Criar um piloto Kanban pequeno, auditável e sem execução automática por padrão, para transformar demandas recorrentes em cards com owner, fonte, risco, próximo passo e receipt.

## Princípios

- Kanban organiza trabalho; não autoriza writes.
- Cards começam `unassigned` por padrão.
- Nenhum worker automático sem approval packet.
- Cada card tem risco A0-A4 e owner lógico.
- Done exige evidência/receipt.
- Telegram só recebe decisão/exceção, não movimentação de card.

## Board piloto recomendado

Nome sugerido: `hermes-operating-layer-v016`

Por que esse board:

- cobre os 4 pacotes aprovados por Lucas;
- é horizontal e governamental;
- evita escolher uma empresa como cobaia prematura;
- pode depois gerar boards especialistas para LK Shopify/Growth/SPITI.

## Colunas

- Backlog — demanda capturada, ainda não triada.
- Triaged — owner, risco e fonte definidos.
- Doing — execução ativa por humano/agente.
- Waiting Lucas — precisa decisão/aprovação.
- Waiting External — depende de fonte/equipe/sistema externo.
- QA/Verify — precisa validação/secret scan/readback.
- Done — fechado com receipt.
- Parked — não fazer agora, razão documentada.

## Campos obrigatórios do card

```yaml
title:
owner_profile:
company_area:
risk_level: A0/A1/A2/A3/A4
source_of_truth:
requested_by:
approval_required: true/false
external_writes_allowed: false
workers_allowed: false
next_step:
evidence_path:
receipt_path:
kill_criteria:
```

## Cards iniciais sugeridos

1. Receipts/handoff padrão entre agentes — owner Hermes Geral — A1.
2. Fast lane/model routing por perfil — owner Hermes Geral — A2/A3 para ativação.
3. Kanban piloto controlado — owner Hermes Geral — A2 para board local, A3 se workers.
4. Dashboard OIDC/security upgrade — owner Hermes Geral/Infra — A3/A4.
5. Telegram Decision Hygiene Pack — owner Hermes Geral — A2/A3 dependendo de cron delivery changes.

## Critério para ativar board real

A ativação local de board sem workers pode ser A2 se:

- não cria cron;
- não ativa worker;
- não mexe em gateway;
- não executa ações externas;
- fica local;
- tem rollback por remoção/export do board.

Qualquer uma das condições abaixo sobe para A3/A4:

- worker automático;
- cron/daemon;
- Telegram delivery automático;
- integração Dashboard pública;
- execução por profile especialista;
- writes externos;
- Docker/gateway changes.

## Métricas de sucesso do piloto

- 100% dos cards Done têm receipt.
- 0 cards `running` sem owner e approval quando exigido.
- 0 Telegram noise por movimentação interna.
- 0 writes externos sem approval.
- Lucas consegue saber “o que está pendente” sem procurar em chat.

## Verificação antes de chamar ativo

Quando aprovado para criar board real:

1. listar boards antes;
2. criar board local;
3. criar cards iniciais unassigned;
4. verificar board stats;
5. provar `running=0`;
6. registrar receipt;
7. secret scan em artefatos Brain.

## Recomendação

Próximo passo seguro: pedir approval específico para criar o board local `hermes-operating-layer-v016` **sem workers e sem Telegram delivery**. Não ativar worker/daemon nesta etapa.
