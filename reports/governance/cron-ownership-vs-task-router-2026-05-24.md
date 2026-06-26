# Fase 4B — Cron Ownership vs Task Router

Data: 2026-05-24  
Status: concluído em modo read-only  
Escopo: classificar ownership lógico dos crons existentes contra a matriz de roteamento, sem alterar scheduler, entrega, scripts, profiles, gateway ou produção.

## Resumo executivo

Foram classificados os cron registries ativos conhecidos:
- Main / Hermes Geral: 23 jobs (23 ativos, 0 pausados).
- LK Growth: 26 jobs (22 ativos, 4 pausados).
- Mordomo: 12 jobs (11 ativos, 1 pausados).
- SPITI: registry não encontrado / 0 jobs documentados.

Leitura principal:
- O profile `lk-growth` já concentra corretamente a maior parte dos crons Growth/SEO/CRO/GEO/GMC.
- O profile `mordomo` já concentra intake pessoal, agenda, Decision Inbox e parte operacional Zipper temporária.
- O profile `spiti` está ativo, mas ainda não tem cron registry próprio; qualquer rotina SPITI futura deve nascer nele, não no Main.
- O Main ainda concentra LK operacional, Zipper, watchdogs de profiles e superfícies executivas centrais; isso é aceitável para governança/watchdogs, mas deve ser explicitamente documentado para evitar “especialista por conveniência”.

## Contagem por ownership lógico

- Brain governance: 6
- Hermes ops/watchdog central: 5
- LK Growth: 27
- LK ops/comercial: 7
- Mordomo: 7
- Zipper: 2
- Zipper via Mordomo: 4
- central/COO: 2
- legado/revisar: 1

## Decisões de ownership propostas

### Manter no Hermes Geral / Main
- Mesa COO e superfícies de decisão central.
- Brain governance, sync, strict-runtime guard, runtime truth, self-heal e watchdogs técnicos.
- Watchdogs de saúde de profiles especialistas podem continuar no Main, desde que `deliver=local`/silent-OK e sem mutação de Docker/gateway.

### Migrar ou governar pelo LK Growth
- Todo job LK de Growth, SEO, GEO, CRO, GMC, blog, source pages, PDP/collection/menu/title-meta impact review.
- Duplicatas antigas no Main como GMC/Weekly review devem ser avaliadas em fase própria antes de qualquer pausa/migração.

### Manter no Mordomo
- WhatsApp pessoal, calendar watcher, CRM local sync, Decision Inbox, resumo pessoal, follow-ups conhecidos/verificados.
- Zipper via Mordomo é tolerado enquanto não existir profile Zipper, principalmente por e-mail/intake/drafts; ainda assim deve ser approval-gated.

### SPITI
- Não há crons SPITI próprios agora. Próximas rotinas SPITI devem ser criadas no profile `/opt/data/profiles/spiti`, com fonte verificada e silêncio > dado errado.

### Legado/revisar
- Jobs pausados one-shot antigos no LK Growth podem virar limpeza futura, mas não foram removidos.
- `Pixel AI Hub / Brainzinho daily learning scan` precisa decisão de ownership: Mordomo vs Brain governance vs legado.

## Inventário classificado

### Main / Hermes Geral — Lucas Brain daily intelligence loop
- ID: `f5a23dd6a1bd`
- Status/cadência: ativo; `0 5 * * *`
- Delivery/script: `local`; `agent`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### Main / Hermes Geral — Hermes runtime + cron watchdog no_agent
- ID: `edd06fe19397`
- Status/cadência: ativo; `*/30 * * * *`
- Delivery/script: `local`; `hermes_runtime_cron_watchdog.py`
- Owner lógico: Hermes ops/watchdog central
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Watchdog técnico centralizado; manter local/silent-OK.

### Main / Hermes Geral — LK Daily Sales Brief read-only mandatory delivery
- ID: `7c688553e293`
- Status/cadência: ativo; `0 11 * * *`
- Delivery/script: `origin`; `lk_daily_sales_brief_watchdog.py`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A2/A3 potencial
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — LK Weekly CEO Review read-only mandatory delivery
- ID: `953b9055458e`
- Status/cadência: ativo; `0 12 * * 1`
- Delivery/script: `origin`; `lk_weekly_ceo_review_watchdog.py`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A2/A3 potencial
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — LK GMC Review read-only mandatory delivery
- ID: `d4c26da4cd48`
- Status/cadência: ativo; `0 12 * * 4`
- Delivery/script: `origin`; `lk_gmc_review_watchdog.py`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A2/A3 potencial
- Nota: Domínio Growth/SEO/CRO/GEO/GMC; deve morar/ser governado pelo profile LK Growth.

### Main / Hermes Geral — Zipper Gmail style learning refresh
- ID: `71b147362ec1`
- Status/cadência: ativo; `20 6 * * *`
- Delivery/script: `local`; `agent`
- Owner lógico: Zipper
- Runtime recomendado: Sem profile dedicado; hoje Main/Mordomo conforme fonte
- Risco: A0/A1
- Nota: Zipper ainda não tem profile próprio; manter read-only/approval-gated e evitar contato/preço sem aprovação.

### Main / Hermes Geral — Hermes compression failure self-heal watchdog
- ID: `4bb4e2223fd3`
- Status/cadência: ativo; `*/10 * * * *`
- Delivery/script: `local`; `hermes_compression_failure_self_heal.py`
- Owner lógico: Hermes ops/watchdog central
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Watchdog técnico centralizado; manter local/silent-OK.

### Main / Hermes Geral — LK WhatsApp Hermes responder watchdog
- ID: `71b2636add5d`
- Status/cadência: ativo; `every 1m`
- Delivery/script: `local`; `lk_hermes_whatsapp_watchdog.sh`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A0/A1
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — LK Pulso Comercial 16h read-only delivery
- ID: `c3bb587519d2`
- Status/cadência: ativo; `0 19 * * *`
- Delivery/script: `local`; `lk_financial_pulse_16h_watchdog.py`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A0/A1
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — LK 09h previous-day sales report external delivery
- ID: `e3279babbc4a`
- Status/cadência: ativo; `0 12 * * *`
- Delivery/script: `local`; `lk_previous_day_09h_sales_report_watchdog.py`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A2/A3 potencial
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — LK 19h30 physical store close external delivery
- ID: `a2ead305eab2`
- Status/cadência: ativo; `30 22 * * *`
- Delivery/script: `local`; `lk_store_close_1930_watchdog.py`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A2/A3 potencial
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — Mordomo Telegram gateway watchdog
- ID: `ac0b440e2643`
- Status/cadência: ativo; `every 1m`
- Delivery/script: `local`; `mordomo_gateway_watchdog.sh`
- Owner lógico: Hermes ops/watchdog central
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Watchdog técnico centralizado; manter local/silent-OK.

### Main / Hermes Geral — Zipper OS vendas 09h WhatsApp/email
- ID: `357d40a5863e`
- Status/cadência: ativo; `0 12 * * 1-5`
- Delivery/script: `local`; `zipper_weekday_sales_report_watchdog.py`
- Owner lógico: Zipper
- Runtime recomendado: Sem profile dedicado; hoje Main/Mordomo conforme fonte
- Risco: A2/A3 potencial
- Nota: Zipper ainda não tem profile próprio; manter read-only/approval-gated e evitar contato/preço sem aprovação.

### Main / Hermes Geral — LK Growth Telegram gateway watchdog
- ID: `876d54c62ccd`
- Status/cadência: ativo; `every 1m`
- Delivery/script: `local`; `lk_growth_gateway_watchdog.sh`
- Owner lógico: Hermes ops/watchdog central
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Watchdog técnico centralizado; manter local/silent-OK.

### Main / Hermes Geral — Mesa COO diária Telegram
- ID: `749ee30b51eb`
- Status/cadência: ativo; `0 9 * * *`
- Delivery/script: `origin`; `agent`
- Owner lógico: central/COO
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Superfície executiva central; Telegram deve ser limpo e acionável.

### Main / Hermes Geral — SPITI Telegram gateway watchdog
- ID: `663e3e6a148c`
- Status/cadência: ativo; `every 1m`
- Delivery/script: `local`; `spiti_gateway_watchdog.py`
- Owner lógico: Hermes ops/watchdog central
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Watchdog técnico centralizado; manter local/silent-OK.

### Main / Hermes Geral — Hermes Brain Fechamento Ágil 23h + Brain Sync
- ID: `3fc45b0830c6`
- Status/cadência: ativo; `0 2 * * *`
- Delivery/script: `local`; `agent`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### Main / Hermes Geral — Lucas Brain weekly Learning Loop report
- ID: `f4c499e85eac`
- Status/cadência: ativo; `15 12 * * 1`
- Delivery/script: `origin`; `agent`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### Main / Hermes Geral — Hermes Brain Operating Layer structural watchdog
- ID: `d03fa04e1188`
- Status/cadência: ativo; `10 11 * * *`
- Delivery/script: `local`; `brain_operating_layer_audit.py`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### Main / Hermes Geral — Hermes Brain Runtime Truth Reconciler
- ID: `2404c0766d33`
- Status/cadência: ativo; `20 11 * * *`
- Delivery/script: `local`; `agent`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### Main / Hermes Geral — LK WhatsApp Hermes responder regression watchdog
- ID: `a5d7a392eed9`
- Status/cadência: ativo; `*/30 * * * *`
- Delivery/script: `local`; `lk_hermes_whatsapp_responder_selftest.sh`
- Owner lógico: LK ops/comercial
- Runtime recomendado: Main hoje; futuro owner a definir
- Risco: A0/A1
- Nota: Operação/comercial LK; sensível a cliente/estoque/relatório externo.

### Main / Hermes Geral — Relatório Hermes diário 23h + 02h para Lucas
- ID: `98478b820720`
- Status/cadência: ativo; `30 5 * * *`
- Delivery/script: `origin`; `agent`
- Owner lógico: central/COO
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Superfície executiva central; Telegram deve ser limpo e acionável.

### Main / Hermes Geral — Hermes Brain strict-runtime guard watchdog
- ID: `d9badcd83411`
- Status/cadência: ativo; `0 10 * * *`
- Delivery/script: `local`; `hermes_brain_strict_runtime_guard_watchdog.py`
- Owner lógico: Brain governance
- Runtime recomendado: Main / Hermes Geral
- Risco: A0/A1
- Nota: Governança/saúde do Brain/runtime; silent-OK preferencial.

### LK Growth — LK Growth OS Weekly Growth Review
- ID: `738d3deabaeb`
- Status/cadência: ativo; `0 13 * * 1`
- Delivery/script: `telegram`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Growth OS GMC Review read-only
- ID: `1240644c5f3f`
- Status/cadência: ativo; `0 12 * * 4`
- Delivery/script: `telegram`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Growth OS SEO/CRO impact review — SEO title/meta P1 packets
- ID: `c45cda5fe2df`
- Status/cadência: ativo; `once at 2026-05-25 14:34`
- Delivery/script: `telegram`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK CRO dev preview impact review — Onitsuka/NB/Kill Bill
- ID: `3526b59ca052`
- Status/cadência: ativo; `once at 2026-05-26 12:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK D+7 review — botão Compre Já branco PDP
- ID: `61717aaf7c61`
- Status/cadência: ativo; `once at 2026-05-26 15:30`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK D+7 review — PDP CRO production promotion 2026-05-19
- ID: `9834f69e3541`
- Status/cadência: ativo; `once at 2026-05-26 15:30`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK PDP CRO hotfix D+7 review — trustbar/reviews/tryon
- ID: `d34a61f3bcd9`
- Status/cadência: ativo; `once at 2026-05-26 15:45`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK PDP preorder compact hotfix D+7 review
- ID: `3c6547609c35`
- Status/cadência: ativo; `once at 2026-05-26 16:05`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK n8n checkout abandonado hardening impact review
- ID: `20affa4dcba6`
- Status/cadência: ativo; `once at 2026-05-27 17:50`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK cart intent phase 2 — monitor 90min
- ID: `350be0e438c7`
- Status/cadência: pausado; `once in 30m`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1 — pausado
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK cart intent v2.2 cache/event monitor
- ID: `015cb75e8e91`
- Status/cadência: pausado; `once in 15m`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1 — pausado
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK cart intent Crisp REST identity review D+7
- ID: `2fd730af8433`
- Status/cadência: ativo; `once at 2026-05-27 12:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Recovery OS T1 go-live D+7 impact review
- ID: `a215814309a2`
- Status/cadência: ativo; `once at 2026-05-28 12:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Recovery OS production tracker propagation monitor
- ID: `36694eae598e`
- Status/cadência: pausado; `once in 15m`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1 — pausado
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Recovery OS cart intent controlled LIVE runner
- ID: `fdc9ad165daa`
- Status/cadência: pausado; `every 30m`
- Delivery/script: `origin`; `lk_recovery_os_cart_intent_live_cron.sh`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A2/A3 potencial — pausado
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Recovery OS checkout_started webhook D+7 impact review
- ID: `644f8a37e250`
- Status/cadência: ativo; `once in 7d`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK GEO llms.txt root D+7 impact review
- ID: `e87932cda969`
- Status/cadência: ativo; `once at 2026-05-29 13:45`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK SEO/GEO Experiment Ledger — weekly impact review
- ID: `de3a45d36040`
- Status/cadência: ativo; `30 13 * * 5`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK collection GEO FAQ production D+7 impact review
- ID: `cd5f548bfe49`
- Status/cadência: ativo; `once at 2026-05-29 18:45`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Auth Hub D+7 impact review
- ID: `b58683155a65`
- Status/cadência: ativo; `once at 2026-05-29 19:11`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK blog boutique premium D+7 impact review
- ID: `e0f45429a4f7`
- Status/cadência: ativo; `once in 7d`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK NB blog rewrite D+7 impact review
- ID: `c90e2186b0a0`
- Status/cadência: ativo; `once in 7d`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK GEO Source Pages D+7 Impact Review
- ID: `e0088791bb3b`
- Status/cadência: ativo; `once at 2026-05-30 10:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK D+7 impact review — Adidas SL 72 OG vs RS GEO page table
- ID: `0ab9cd485d15`
- Status/cadência: ativo; `once in 7d`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK D+7 impact review — Packet D GEO Source Pages
- ID: `31b40105c4e5`
- Status/cadência: ativo; `once at 2026-05-30 10:30`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### LK Growth — LK Menu Drawer Production D+7 Review
- ID: `f81883cce339`
- Status/cadência: ativo; `once at 2026-05-30 13:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: LK Growth
- Runtime recomendado: /opt/data/profiles/lk-growth
- Risco: A0/A1
- Nota: Já está no profile correto; revisar ruído/one-shots stale em fase separada.

### Mordomo — Mordomo global WhatsApp watcher — Lucas pessoal
- ID: `6f4c913082db`
- Status/cadência: ativo; `every 5m`
- Delivery/script: `origin`; `mordomo_whatsapp_global_watch.py`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

### Mordomo — Zipper Gmail draft engine — safe draft-only
- ID: `5bbe5169fe62`
- Status/cadência: ativo; `every 15m`
- Delivery/script: `local`; `agent`
- Owner lógico: Zipper via Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo até existir profile Zipper
- Risco: A0/A1
- Nota: Aceitável temporariamente por e-mail/WhatsApp/intake; futuro Zipper profile pode absorver.

### Mordomo — Mordomo global Calendar watcher
- ID: `fe5cf7f1b228`
- Status/cadência: ativo; `every 15m`
- Delivery/script: `origin`; `mordomo_calendar_global_watch.py`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

### Mordomo — Mordomo CRM local sync
- ID: `daf97feec481`
- Status/cadência: ativo; `every 10m`
- Delivery/script: `local`; `mordomo_crm_sync_local.py`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

### Mordomo — Mordomo Decision Inbox digest
- ID: `e46ea230f0cf`
- Status/cadência: ativo; `0 9 * * *`
- Delivery/script: `origin`; `mordomo_decision_digest.py`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

### Mordomo — Mordomo A2 executor scaffold
- ID: `058df00bf941`
- Status/cadência: pausado; `every 30m`
- Delivery/script: `origin`; `mordomo_a2_executor.py`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A2/A3 potencial — pausado
- Nota: Já está no profile correto.

### Mordomo — Pixel AI Hub / Brainzinho daily learning scan
- ID: `c358f8f56a26`
- Status/cadência: ativo; `30 23 * * *`
- Delivery/script: `origin`; `agent`
- Owner lógico: legado/revisar
- Runtime recomendado: Revisar se pertence ao Mordomo ou Brain governance
- Risco: A0/A1
- Nota: Nome indica possível rotina fora do domínio Mordomo; precisa decisão.

### Mordomo — Zipper direct main e-mail monitor — zipper@zippergaleria.com.br
- ID: `20972b3c7595`
- Status/cadência: ativo; `every 60m`
- Delivery/script: `origin`; `zipper_main_email_monitor.py`
- Owner lógico: Zipper via Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo até existir profile Zipper
- Risco: A0/A1
- Nota: Aceitável temporariamente por e-mail/WhatsApp/intake; futuro Zipper profile pode absorver.

### Mordomo — Mordomo WhatsApp pessoal resumo 17h BRT
- ID: `3bcbf3be9b73`
- Status/cadência: ativo; `0 20 * * *`
- Delivery/script: `origin`; `mordomo_whatsapp_summary_17.sh`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

### Mordomo — Zipper artist PDFs local-only known-answer ingest
- ID: `f537bb9c505b`
- Status/cadência: ativo; `every 30m`
- Delivery/script: `local`; `zpr_artist_pdf_local_ingest.py`
- Owner lógico: Zipper via Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo até existir profile Zipper
- Risco: A0/A1
- Nota: Aceitável temporariamente por e-mail/WhatsApp/intake; futuro Zipper profile pode absorver.

### Mordomo — ZPR Enquiry Form watcher — approval-gated
- ID: `871b9bc5617a`
- Status/cadência: ativo; `every 5m`
- Delivery/script: `origin`; `zipper_zpr_enquiry_watcher.py`
- Owner lógico: Zipper via Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo até existir profile Zipper
- Risco: A0/A1
- Nota: Aceitável temporariamente por e-mail/WhatsApp/intake; futuro Zipper profile pode absorver.

### Mordomo — Follow-up Leticia Albuquerque — importação/Portugal
- ID: `1f734765abc4`
- Status/cadência: ativo; `once at 2026-05-28 12:00`
- Delivery/script: `origin`; `agent`
- Owner lógico: Mordomo
- Runtime recomendado: /opt/data/profiles/mordomo
- Risco: A0/A1
- Nota: Já está no profile correto.

## Backlog recomendado — sem execução automática

1. Fase 4C — corrigir UX do `Mesa COO diária Telegram`: sem wrapper, sem job_id visível, sem marker JSON/HTML, com botões nativos reais.
2. Fase 4D — plano de deduplicação/migração LK: comparar jobs Main vs LK Growth e propor pausas/migrações com rollback, sem executar ainda.
3. Fase 4E — decidir futuro Zipper: manter via Mordomo/Main ou criar profile Zipper quando houver volume/risco suficiente.
4. Fase 4F — SPITI cron baseline: se necessário, criar apenas após PRD/rotina e aprovação, dentro do profile SPITI.
5. Fase 4G — limpeza de one-shots pausados/stale: somente com aprovação explícita e backup da registry.

## Guardrails preservados

- Nenhum cron foi criado, pausado, removido, editado ou executado.
- Nenhum `deliver`, schedule, script ou profile foi alterado.
- Nenhum gateway, Docker, VPS, Traefik, volume ou network foi alterado.
- Nenhum write externo foi executado.
- Nenhum `.env` ou secret foi lido em valor ou copiado para este relatório.
