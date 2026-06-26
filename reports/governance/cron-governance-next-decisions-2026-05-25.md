# Pacote de decisão — próximos passos de governança dos crons

Data: 2026-05-25 11:40 UTC  
Owner: Hermes Geral / COO  
Escopo: decisões futuras a partir da reauditoria `cron-owner-final-reaudit-2026-05-25.md`  
Writes externos/runtime: não

## Contexto

A reauditoria confirmou que a matriz atual está consistente após a migração de donos inequívocos:

- Main: 20 crons, 19 `local`, 1 `origin`.
- LK Growth: 23 crons, com 19 `origin`, 3 `telegram`, 1 `local`.
- Mordomo: 13 crons, 8 `origin`, 5 `local`.
- SPITI: sem `cron/jobs.json` local.
- Duplicidades entre profiles auditados: nenhuma.

A lacuna principal não é mais ownership incorreto. É governança de ruído, maturidade de profiles e clareza de boundaries.

## Decisão 1 — Consolidar reviews D+7 da LK Growth

### Opção recomendada

Criar primeiro um desenho local de digest/ledger para os 19 reviews D+7 da LK Growth, sem alterar cron ainda.

### Por quê

Hoje os reviews D+7 parecem corretos como dono, mas entregam separadamente em `origin`, aumentando risco de ruído no Telegram. Um digest/ledger preserva rastreabilidade e reduz interrupções.

### Escopo seguro inicial

- Criar rotina documental `areas/lk/sub-areas/growth/rotinas/growth-d7-review-digest-ledger.md`.
- Criar template de relatório consolidado.
- Definir critério: o que vira Telegram, o que fica local, o que vira decisão 1/N.
- Não editar crons nesta etapa.

### Exige aprovação posterior

- Alterar `deliver`, pausar/remover crons existentes, criar cron de digest ou mudar schedule.

## Decisão 2 — Zipper: manter no Mordomo ou criar profile próprio

### Opção recomendada

Manter por enquanto dentro do Mordomo, mas criar critério explícito de promoção para profile próprio.

### Por quê

Zipper está documental/read-only/approval-gated e ainda não justifica custo operacional de outro runtime, a menos que volume, risco ou autonomia aumentem.

### Escopo seguro inicial

- Criar seção de critérios em `areas/operacoes/rotinas/cron-owner-reaudit-semanal.md` ou rotina Zipper existente.
- Não criar profile, bot, cron ou gateway.

### Exige aprovação posterior

- Criar profile `zipper`, mover crons, criar bot/canal, alterar gateway ou scripts.

## Decisão 3 — SPITI registry baseline

### Opção recomendada

Documentar explicitamente “SPITI sem crons locais” por enquanto; criar skeleton registry apenas se auditorias futuras precisarem diferenciar ausência intencional de erro.

### Por quê

Criar arquivo `cron/jobs.json` vazio pode melhorar auditoria, mas também pode sugerir runtime scheduler ativo onde não há. O estado atual é aceitável se estiver documentado.

### Escopo seguro inicial

- Patch documental em SPITI/Operações dizendo que o profile não tem registry local de cron.
- Não criar arquivo runtime em `/opt/data/profiles/spiti/cron/jobs.json` nesta etapa.

### Exige aprovação posterior

- Criar registry runtime, ativar scheduler, mover/criar crons SPITI.

## Decisão 4 — LK Comercial/Ops no Main

### Opção recomendada

Manter no Main/COO por enquanto.

### Por quê

Relatórios de venda, pulso e fechamento são operação comercial, não necessariamente Growth. Sem profile operacional LK próprio, Main/COO é o lugar mais seguro.

### Escopo seguro inicial

- Marcar a distinção LK Growth vs LK Comercial/Ops na rotina de reauditoria.
- Não mover crons.

### Exige aprovação posterior

- Criar profile operacional LK, migrar crons comerciais ou alterar destinos.

## Recomendação de sequência

1. Fazer Decisão 1 em modo local/documental: desenhar digest/ledger D+7 LK Growth.
2. Fazer Decisão 2 em modo local/documental: critério de promoção Zipper.
3. Fazer Decisão 3 em modo documental: registrar SPITI sem crons locais.
4. Manter Decisão 4 sem ação runtime.

## Não realizar sem aprovação explícita

- Criar, pausar, remover ou editar cron.
- Alterar `deliver`.
- Criar profile runtime.
- Reiniciar gateway/Docker/VPS.
- Enviar mensagens externas.
- Publicar qualquer coisa fora do Brain local.

## Próximo passo operacional sugerido

Se Lucas aprovar seguir com a opção recomendada, executar apenas a parte documental da Decisão 1: desenho do digest/ledger LK Growth D+7, sem mexer em crons.
