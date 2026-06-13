# Handoff LK Stock → LC Hermes Central

Data/hora: 2026-06-11T20:04:20Z
Agente/profile: [LK] Estoque Loja Física (`lk-stock`)
Empresa/área: LK Sneakers / Estoque Loja Física / Stock OS
Responsável humano: Lucas Cimino

## Pedido original

Lucas pediu: "Preciso que avise o agente LC Hermes que está tudo funcionando na nossa database".

## Aviso para LC Hermes

A base local do LK Stock OS está operacional como superfície primária de consulta de estoque. A regra vigente é:

- consulta normal de estoque/disponibilidade interna usa **DB local primeiro**;
- Tiny/Olist não fica no caminho quente de cada pergunta;
- Tiny/Olist mantém a base fresca por **webhooks durante o dia** e **full sync noturno**;
- se a DB local estiver sem SKU, stale ou inconsistente, o agente deve sinalizar reconciliação em vez de prometer disponibilidade.

## Evidência verificada antes do handoff

- Suíte Stock OS: `29 tests OK`.
- DB local atual: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260611T023437Z.db`.
- Linhas em `current_local_stock`: `5191`.
- Linhas `local_consult_safe`: `4539`.
- Linhas `identity_resolved_safe`: `4539`.
- Runtime de webhooks Tiny/Olist existe: `/opt/data/hermes_bruno_ingest/local_sql/lk_stock_tiny_sync/runtime.db`.
- Eventos já processados no runtime:
  - `tiny_order_event_ledger`: `16` eventos.
  - `tiny_stock_event_ledger`: `39` eventos.
  - `tiny_stock_latest`: `30` SKUs.
- Full sync noturno ativo no cron:
  - job: `c45da7bb0fcb`.
  - nome: `LK Stock Tiny full sync nightly read-only`.
  - schedule: `20 6 * * *` UTC = `03:20 BRT`.
  - script: `lk_stock_tiny_full_sync_nightly.py`.
  - `no_agent=true`, profile `lk-stock`.
- Smoke do full sync: `full_sync_smoke_rc=0`.
- Probe público sem secret em `/webhooks/lk-stock/tiny/events`: `401`, esperado.
- Consulta real por DB local testada:
  - SKU `MR530EMA-3` retornou quantidade local `1.0`.
  - fonte: `stock_observations exact Shopify↔Tiny evidence / LK | CONTROLE ESTOQUE`.
  - freshness: `cached_observation_promoted_after_full_live_gap`.
  - `public_availability_safe=0` e `availability_claim_allowed=0`.

## Artefatos principais

- PRD atualizado: `areas/lk/sub-areas/stock/PRD.md`.
- Receipt final: `areas/lk/sub-areas/stock/receipts/lk-stock-db-local-primary-hot-path-finalized-20260611T170607Z.md`.
- Política/skill: `lk-stock/references/db-local-primary-tiny-sync-policy-20260611.md`.
- Script de consulta local: `areas/lk/sub-areas/stock/scripts/lk_stock_os_query.py`.
- Teste adicionado: `areas/lk/sub-areas/stock/evaluation/test_lk_stock_os_query.py`.

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Writes externos: `0`.
- Cliente/fornecedor/campanha: `0`.
- Pronta entrega pública: `0`.
- `public_availability_safe=0` e `availability_claim_allowed=0` continuam bloqueados por padrão.

## Próximo acompanhamento recomendado

LC Hermes deve tratar o Stock OS como **base local operacional funcionando** para consultas internas, mas considerar o full sync noturno 100% comprovado somente após a primeira execução completa automática às `03:20 BRT`. Até lá: configurado, ativo, com smoke OK e webhooks reais processando.

## Onde foi documentado no Brain

`areas/operacoes/handoffs/handoff-lk-stock-to-lc-hermes-stock-db-operational-20260611T200420Z.md`

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/operacoes/handoffs/handoff-lk-stock-to-lc-hermes-stock-db-operational-20260611T200420Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/operacoes/handoffs/handoff-lk-stock-to-lc-hermes-stock-db-operational-20260611T200420Z.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
