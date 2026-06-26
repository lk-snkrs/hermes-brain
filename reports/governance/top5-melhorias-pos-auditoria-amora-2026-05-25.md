# Execução — Top 5 melhorias pós-auditoria Hermes vs Amora

Data: 2026-05-25  
Owner: Hermes Geral / COO  
Escopo: documentação local/read-only e governança operacional.  
Writes externos: não.  
Runtime mutation: não.  
Cron novo: não.

## Pedido

Executar as 5 melhorias priorizadas na auditoria crítica, com item 2 em cadência semanal.

## Status

Concluído em modo seguro/local.

## 1. Validar a próxima Mesa COO real no Telegram

Implementado como rotina local:

- `areas/operacoes/rotinas/mesa-coo-telegram-quality-audit.md`

O que ficou definido:

- checklist de UX limpa;
- classificação `validada`, `limpa_mas_fraca`, `suja`, `não_observada`;
- template de receipt;
- regra de não reiniciar gateway/scheduler sem packet aprovado.

Limite: a próxima entrega real ainda precisa ocorrer para ser classificada.

## 2. Criar scorecard de orquestração semanal

Implementado como rotina semanal:

- `areas/operacoes/rotinas/orquestracao-scorecard-semanal.md`

O que mede:

- roteamento correto;
- handoff/receipt;
- approval gates;
- UX Telegram;
- aprendizado/skills.

Entrega padrão:

- salvar no Brain/local;
- Telegram apenas se houver decisão, exceção, falha ou approval necessário.

## 3. Rodar auditoria local de handoff completeness

Implementado como rotina local:

- `areas/operacoes/rotinas/handoff-completeness-audit-local.md`

O que faz:

- varre outputs materiais;
- classifica gaps;
- corrige automaticamente apenas gaps documentais com fatos suficientes;
- bloqueia runtime/infra e produção.

## 4. Refinar guardrails de leitura administrativa

Implementado como packet/proposta, sem patch de código:

- `reports/governance/guardrails-readonly-admin-inspection-packet-2026-05-25.md`

Achado base:

- `cronjob list` foi bloqueado em auditoria local/read-only;
- o fallback seguro foi terminal/CLI read-only;
- a melhoria proposta é separar verbos read-only (`list/status`) de verbos mutáveis (`create/update/run/remove`).

Limite: código/runtime só deve ser alterado em rodada própria com testes e aprovação se necessário.

## 5. Revisar skills por efetividade

Implementado como rotina documental:

- `areas/operacoes/rotinas/skills-effectiveness-review.md`

O que mede:

- se skill patch evitou erro;
- erro repetido após correção;
- skills inchadas/desatualizadas;
- quando mover aprendizado para Brain/rotina.

## Indexação

Arquivos adicionados ao MAPA de Operações:

- Mesa COO quality audit;
- scorecard semanal;
- handoff completeness local;
- revisão de efetividade de skills;
- packet de guardrails read-only admin.

## Não executado deliberadamente

- cron novo;
- restart de gateway;
- Docker/VPS/Traefik/volumes/networks;
- alteração de scheduler;
- mudança de delivery;
- envio externo;
- produção.

## Próxima ação operacional

Depois da próxima Mesa COO real, executar `mesa-coo-telegram-quality-audit.md` e registrar o receipt. Se vier limpa, marcar a Mesa COO v2 como validada; se vier suja, abrir packet técnico de correção com testes e rollback.
