# Intelligence Map — Hermes Brain / Cérebro Cimino

Atualizado em: 2026-05-22 14:22 UTC

## Objetivo

Unificar a visão de memória, cron, inteligência e proatividade do Hermes Brain para evitar duplicidade, ruído e decisões espalhadas.

Este mapa não cria runtime novo. Ele documenta a hierarquia aprovada para operar o que já existe.

## Princípio central

- **Brain versionado é fonte durável.**
- **Telegram é canal de decisão/exceção, não banco de memória.**
- **Mission Control é cockpit/preview, não fonte paralela.**
- **Especialistas são braços do Hermes Brain, não cérebros separados.**
- **Sucesso normal de watchdog técnico é silencioso.**

## Hierarquia operacional aprovada

### 1. Fechamento Ágil 23h BRT

- Job: `3fc45b0830c6` — Hermes Brain Fechamento Ágil 23h + Brain Sync.
- Cadência: diário, 23h BRT (`0 2 * * *` UTC).
- Delivery: `local`.
- Função: consolidar o dia, gerar artefatos locais e acionar Brain Sync seguro.
- Fonte: Brain, receipts, reports, dailies, decisões, outputs dos especialistas.
- Saída esperada: documentação local em `reports/daily-consolidation/` e artefatos correlatos.
- Regra anti-ruído: não mandar Telegram em sucesso normal; alertar só falha, risco, bloqueio ou decisão.

### 2. Meta-supervisor 02h BRT

- Job: `f5a23dd6a1bd` — Lucas Brain daily intelligence loop.
- Cadência: diário, 02h BRT (`0 5 * * *` UTC).
- Delivery: `local`.
- Função: analisar o Brain consolidado, identificar riscos, oportunidades e gaps.
- Fonte: Brain versionado, session search, crons, skills, memória Hermes, relatórios locais.
- Saída esperada: plano/diagnóstico local, não spam.
- Regra anti-duplicidade: não repetir relatório executivo se a Mesa COO já cobre a decisão do dia.

### 3. Relatório executivo curto 02h30 BRT

- Job: `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas.
- Cadência: diário, 02h30 BRT (`30 5 * * *` UTC).
- Delivery: `local` desde P2 2026-05-22.
- Função: consolidar localmente o 23h + 02h como insumo; não competir com a Mesa COO no Telegram.
- Fonte: 23h + 02h.
- Regra anti-ruído: Telegram fica reservado para Mesa COO e exceções; rollback documentado no cron control plane.
- Risco monitorado: se a Mesa COO não absorver decisões críticas, reavaliar delivery `origin` ou fundir prompts.

### 4. Mesa COO diária

- Job: `749ee30b51eb` — Mesa COO diária Telegram.
- Cadência: diário, 08h30 BRT (`30 11 * * *` UTC).
- Delivery: `origin`.
- Função: visão COO curta e acionável.
- Fonte: Brain, crons, handoffs, decisões pendentes.
- Saída esperada: até 5 itens priorizados.
- Regra anti-duplicidade: deve ser a fila executiva principal do dia; se já cobrir uma decisão, o 02h30 não deve repetir salvo risco novo.

### 5. Watchdogs técnicos silent-OK

Exemplos ativos:

- `edd06fe19397` — runtime + cron watchdog.
- `4bb4e2223fd3` — compression failure self-heal.
- `ac0b440e2643` — Mordomo Telegram gateway watchdog.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog.
- `663e3e6a148c` — SPITI Telegram gateway watchdog.
- `d03fa04e1188` — Brain Operating Layer structural watchdog.
- `d9badcd83411` — strict-runtime guard watchdog.
- `2404c0766d33` — Runtime Truth Reconciler.

Regra:

- Delivery preferencial: `local`.
- Output vazio em OK.
- Telegram apenas em restart, falha, regressão, perda de fonte ou risco material.

### 6. Relatórios de negócio aprovados

- LK Daily Sales Brief: Telegram/origin, relatório obrigatório.
- LK Weekly CEO Review: Telegram/origin.
- LK GMC Review: Telegram/origin.
- Zipper OS vendas 09h: local com delivery externo controlado pelo script aprovado.
- LK 09h e 19h30: local, scripts com delivery externo controlado.

Regra:

- Manter separação de empresa e fonte.
- Não misturar LK/Zipper/SPITI.
- External writes seguem guardrails e aprovações específicas já documentadas.

## Decision Queue única

A fila executiva recomendada para Lucas deve agrupar no máximo 5 itens/dia:

1. Decisão necessária.
2. Recomendação do Hermes.
3. Risco se não decidir.
4. Fonte/evidência.
5. Ação bloqueada ou próxima ação segura.

Categorias canônicas:

- `commercial_reply`
- `followup_due`
- `newsletter_noise`
- `price_availability_blocked`
- `customer_complaint`
- `supplier_or_internal`
- `calendar_or_logistics`
- `finance_or_bank`
- `ignore`

## Fontes por camada

### Memória quente

- `memories/hot.md`
- `memories/daily/YYYY-MM-DD.md`
- `empresa/decisoes/decisoes-permanentes.md`
- ledgers/approvals
- receipts recentes

### Runtime

- Registro vivo do Hermes cron.
- Scripts em `/opt/data/scripts/` e `scripts/` quando usados por jobs.
- Profiles em `/opt/data/profiles/*`.
- Gateway/bots somente por checagem read-only salvo aprovação explícita.

### Documentação operacional

- `areas/*/MAPA.md`
- `areas/*/rotinas/*.md`
- `areas/*/prds/*.md`
- `reports/governance/*.md`

## Guardrails

- Não usar `/root` como caminho operacional vivo em docs novos.
- Não usar `sshpass` como fluxo operacional.
- Não ressuscitar Mem0/OpenClaw como fonte de verdade paralela.
- Não documentar comando perigoso como instrução viva sem etiqueta `LEGACY`, `EXAMPLE`, `DO NOT RUN`, `DRY-RUN` ou gate de aprovação.
- Docker/VPS/Traefik/volumes/redes/deploys exigem plano, backup/rollback e aprovação explícita.
- Customer-facing/preço/disponibilidade/negociação/campanha exige fonte/aprovação conforme autonomia vigente.

## Critério de melhoria

Um novo cron, relatório, watchdog ou agente só deve ser criado se responder:

- Qual decisão/risco ele reduz?
- Qual fonte lê?
- Qual output grava?
- Quem recebe?
- Quando fica silencioso?
- Qual critério de remoção?
- Como evita duplicar 23h, 02h, 02h30 e Mesa COO?
