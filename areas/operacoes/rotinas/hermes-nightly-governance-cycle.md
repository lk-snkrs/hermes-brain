# Rotina — Ciclo Noturno de Governança Hermes 01h/02h/02h15/02h30

Status: **ativo como arquitetura operacional de governança**
Atualizada em: 2026-06-02 UTC
Área: Operações / Hermes Brain / Grande Mente

## Objetivo

Fazer Hermes aprender diariamente com Lucas e com o próprio runtime, aumentando autonomia segura sem aumentar ruído ou risco produtivo.

O ciclo é composto por quatro camadas:

1. **01h — Fechamento + Handoff**: consolida o dia e gera pacote estruturado de aprendizado.
2. **02h — LC Hermes Daily Intelligence**: promove aprendizados, audita o ecossistema inteiro e aplica auto-melhorias A0/A1. A responsabilidade é do LC Hermes / Hermes Agent central, não do Mordomo isolado.
3. **02h15 — Higiene de Memória**: verifica memória e providers externos, mantendo silent-OK e receipt local.
4. **02h30 — Digest para Lucas**: relata o que aconteceu, o que Hermes fez, como Hermes se auto-melhorou e o que precisa de Lucas.

## Contrato de autonomia

### A0/A1 — permitido automaticamente

- Docs Brain, rotinas, índices, changelog e reports locais.
- Skills/referências quando o aprendizado é durável e procedimental.
- Prompts de crons existentes quando a mudança melhora relatório, aprendizagem, silent-OK ou verificação e não muda produção/entregas externas.
- Scripts locais/read-only/sanitizados, com validação e secret scan.
- Receipts locais e checks de integridade.
- Correção de drift documental, índice ausente, artefato faltando, wording obsoleto, relatório genérico ou watchdog ruidoso.

### A3/A4 — precisa aprovação atual e escopo/rollback

- Docker, VPS, gateway, deploy, restart, compose, containers, redes, Traefik ou host.
- Secrets, tokens, credenciais, providers externos de memória.
- Bancos, Shopify, Tiny, GMC, Klaviyo, Meta/Ads, Supabase ou fonte de verdade.
- WhatsApp/e-mail/envios externos, clientes, fornecedores, dinheiro, compra, campanha ou ação destrutiva.
- Criação de novos crons produtivos ou mudança de delivery externo sem aprovação explícita.

## Artefatos canônicos

- 01h:
  - `reports/daily-consolidation/YYYY-MM-DD.md`
  - `reports/daily-consolidation/YYYY-MM-DD-handoff.json`
  - `reports/daily-consolidation/latest-handoff.json`
- 02h:
  - `reports/hermes-continuous-improvement/YYYY-MM-DD.md`
  - `reports/hermes-learning-ledger/YYYY-MM-DD.md`
- 02h15:
  - `reports/memory-hygiene/YYYY-MM-DD.json`
  - `reports/memory-hygiene/latest.json`
- Validador local:
  - `/opt/data/scripts/hermes_nightly_governance_artifacts_check.py`
  - `reports/governance/nightly-governance-artifacts-latest.json`
- 02h30:
  - `reports/hermes-daily-digest/YYYY-MM-DD.md` quando o digest optar por salvar cópia local.

## Regra de aprendizagem

Quando Lucas aprova ou corrige algo:

1. O 01h captura no handoff com escopo, exclusões e padrão aprendido.
2. O 02h decide se é A0/A1 ou A3/A4.
3. Se A0/A1, promove no mesmo run para Brain/skill/memória/prompt/check.
4. Se A3/A4, cria decisão com escopo, benefício, risco, blast radius, exclusões e rollback.
5. O 02h30 explica em linguagem humana o que Hermes aprendeu e se algo depende de Lucas.

Correção sistêmica aprovada em 2026-06-06: quando o aprendizado afetar arquitetura, governança, contexto, memória, skills, crons ou subagentes, o Mordomo deve fazer handoff para o **LC Hermes / Hermes Agent central**. O LC Hermes é o owner de promoção sistêmica para o ecossistema inteiro; Mordomo não deve manter a melhoria apenas no próprio profile.

O handoff canônico desta decisão está em `reports/governance/handoff-lc-hermes-subagent-context-systemwide-2026-06-06.md`.

## Governança de contexto de subagentes

O ciclo noturno deve reforçar a regra aprovada de **contexto mínimo + busca sob demanda**.

Owner: **LC Hermes / Hermes Agent central**. Escopo: Hermes central, Brain versionado, crons de governança, LK, Zipper, SPITI, Mordomo, Mission Control e especialistas. Mordomo pode registrar o aprendizado, mas a promoção sistêmica e o relatório de melhoria pertencem ao LC Hermes.

Checks documentais esperados:

- subagentes recorrentes têm escopo, fontes e autonomia definidos no registry/PRD;
- novas rotinas ou crons de subagente apontam para índice/Brain/fonte viva, não para “carregar tudo”;
- handoffs sobem decisão, fonte, status, próximos passos e blockers, sem histórico bruto inteiro;
- aprendizados duráveis são promovidos seletivamente para memória, skill, rotina ou Brain;
- ausência de contexto vira lookup sob demanda (`session_search`, Brain, API/banco/fonte autorizada), não aumento indiscriminado de prompt.

Sinal de melhoria segura A0/A1: corrigir docs, índice, rotina ou skill para reduzir contexto carregado e melhorar recuperação sob demanda, sem alterar produção, cron externo ou fonte viva.

## Validação

O script `/opt/data/scripts/hermes_nightly_governance_artifacts_check.py` deve ser usado pelo 02h e/ou 02h30 para detectar:

- handoff ausente ou inválido;
- learning ledger ausente;
- relatório 02h ausente;
- receipt de memória ausente ou inválido;
- campos obrigatórios faltando;
- possíveis localizadores de segredo nos artefatos.

Se houver falha, o digest deve separar:

- falha do ciclo de governança;
- incidente no ecossistema descoberto pelo ciclo;
- melhoria segura aplicada;
- decisão que precisa de Lucas.

## Política de Telegram

- 01h, 02h e 02h15 ficam locais/silent-OK quando saudáveis.
- 02h30 entrega o resumo executivo esperado por Lucas.
- O resumo não deve conter wrapper, job ID, JSON bruto, logs, comandos ou ruído técnico.
- Se houver alerta, explicar gatilho, impacto, ação feita e próximo passo.
- O relatório/digest deve dizer quando uma melhoria foi promovida pelo LC Hermes para o sistema inteiro, diferenciando melhoria sistêmica de ajuste local do Mordomo.
