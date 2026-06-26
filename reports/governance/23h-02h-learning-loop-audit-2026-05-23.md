# Audit — Crons 23h / 02h / 02h30 e aprendizado contínuo — 2026-05-23

## Veredito

Parcialmente bem configurado.

O desenho principal existe e está saudável: 23h consolida o dia no Brain, 02h executa o Daily Intelligence Loop com melhoria contínua/local, e 02h30 envia um resumo executivo para Lucas no Telegram. Os jobs rodaram OK na última execução e usam contexto encadeado.

A lacuna: o aprendizado contínuo ainda está mais forte no 02h do que no 23h. O 23h registra seção de aprendizados/promover para memória/skills/rotinas, mas não tem `memory` no toolset e não está explicitamente configurado como auto-fix/auto-learning; ele consolida e sincroniza. O 02h tem toolset `memory`, `skills`, `session_search`, `cronjob`, `file`, `terminal`, `web`, aplica melhorias low-risk e documenta relatório diário, mas precisa de linguagem mais dura para auto-fix de A0/A1 e para promover aprendizados do 23h automaticamente quando seguro.

## Estado vivo verificado

### 23h — Fechamento Ágil + Brain Sync

- Job: `3fc45b0830c6`
- Nome: Hermes Brain Fechamento Ágil 23h + Brain Sync
- Schedule: `0 2 * * *` UTC = 23h BRT
- Deliver: `local`
- Último run: 2026-05-23T02:08:40Z
- Status: ok
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Toolsets: terminal, file, cronjob, skills, session_search, messaging
- Função real: consolidar decisões, entregas, pendências, riscos, handoffs e aprendizados em `reports/daily-consolidation/YYYY-MM-DD.md`; rodar Brain Sync seguro allowlist.

### 02h — Daily Intelligence Loop

- Job: `f5a23dd6a1bd`
- Nome: Lucas Brain daily intelligence loop
- Schedule: `0 5 * * *` UTC = 02h BRT
- Deliver: `local`
- Último run: 2026-05-23T05:06:39Z
- Status: ok
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Contexto: `3fc45b0830c6`, `edd06fe19397`, `4bb4e2223fd3`
- Toolsets: web, terminal, file, skills, cronjob, session_search, memory, messaging
- Função real: saúde runtime, releases Hermes, prioridade viva, reconciliação Brain/runtime, melhoria de mecanismo, documentação, low-risk improvements, silent success.

### 02h30 — Resumo executivo Telegram

- Job: `98478b820720`
- Nome: Relatório Hermes diário 23h + 02h para Lucas
- Schedule: `30 5 * * *` UTC = 02h30 BRT
- Deliver atual: `origin`
- Último run: 2026-05-23T05:32:23Z
- Status: ok
- Contexto: `3fc45b0830c6`, `f5a23dd6a1bd`
- Função real: sintetizar o 23h + 02h para Lucas no Telegram.

## O que já cobre bem

- 23h documenta o dia e separa decisões, pendências, automações, handoffs, riscos, amanhã e aprendizados.
- 02h consulta 23h e watchdogs por `context_from`.
- 02h tem permissão de memória/skills e instrução de aplicar melhorias low-risk.
- 02h faz auditoria de runtime, releases, crons, Brain Health, Brain Sync dry-run e secret scan.
- Watchdogs específicos já fazem self-heal/local silent-OK em escopos estreitos, por exemplo compression failure self-heal.
- Aprendizados já são documentados em Brain: `empresa/gestao/hermes-learning-loop.md`, reports diários, changelog e micro-aulas em `reports/hermes-daily-digest/feature-lessons.md`.

## Lacunas

1. O 23h não tem `memory` no toolset; portanto ele pode listar aprendizados, mas não é o melhor lugar para salvar memória permanente do agente.
2. O prompt do 23h fala em promover para memória/skills/rotinas, mas é mais checklist do que execução automática.
3. O 02h aplica melhorias low-risk, mas não usa explicitamente termos como `auto-fix`/`corrigir automaticamente`; o comportamento existe por regra de skill, mas pode ficar mais forte no prompt.
4. Não há ainda um ledger único diário de “aprendizado promovido” ligando: aprendizado do 23h → decisão/lesson/skill/memory alterada → evidência de verificação.
5. O 02h30 é resumo, não executor; ele não deve corrigir nada, só reportar/decidir.

## Recomendação

Fazer um hardening leve, sem restart/deploy/Docker:

1. Atualizar prompt do 23h para dizer que aprendizados A0/A1 devem ser registrados em Brain/skills quando seguro, e que memória fica preferencialmente para o 02h quando exigida pelo toolset.
2. Atualizar prompt do 02h para ser explicitamente o `auto-learning / auto-improvement / safe auto-fix supervisor`.
3. Adicionar no 02h um ledger diário curto: `reports/hermes-learning-ledger/YYYY-MM-DD.md` com `aprendizado`, `destino`, `ação aplicada`, `verificação`, `bloqueio`.
4. Manter `deliver=local` para sucesso saudável e Telegram apenas para decisão/erro/oportunidade material.

## Ação aplicada após aprovação de Lucas

Lucas aprovou `Fazer` para hardening leve, sem restart/deploy/Docker/write externo.

Aplicado:

1. Prompt do 23h reforçado com `Hardening aprovado por Lucas — aprendizado contínuo e safe auto-fix`.
2. 23h agora deve gerar `Learning Ledger candidates` com aprendizado, destino, ação aplicada/bloqueio e verificação.
3. Toolset do 23h recebeu `memory`, além de terminal/file/cronjob/skills/session_search/messaging.
4. Prompt do 02h reforçado como `auto-learning / auto-improvement / safe auto-fix supervisor`.
5. 02h agora deve criar `reports/hermes-learning-ledger/YYYY-MM-DD.md` e promover aprendizados A0/A1 para Brain/memória/skills quando seguro.

Verificação pós-aplicação:

- `3fc45b0830c6`: `hardening=True`, `ledger=True`, `memory` presente no toolset, próximo run 2026-05-24T02:00:00Z.
- `f5a23dd6a1bd`: `hardening=True`, `ledger=True`, `context_from` preservado com 23h + watchdogs, próximo run 2026-05-24T05:00:00Z.
- `98478b820720`: `deliver=origin`, `context_from` preservado com 23h + 02h, próximo run 2026-05-24T05:30:00Z.

## Limites que devem permanecer

Não auto-corrigir sem aprovação: Docker/VPS/gateway/restart/deploy, banco, Shopify/Tiny/GMC/Klaviyo/Meta, envio externo, cliente/fornecedor, dinheiro, segredo, destrutivo.

