# Amora-style agent orchestration hardening — 2026-05-24

## Scope

Docs-only hardening of Lucas Cimino's Hermes Brain agent organogram after the Mesa COO UX fix and before technical Task Router enforcement.

No runtime, cron, Docker, gateway, Shopify, GMC, Klaviyo, Meta, Supabase, WhatsApp, email, or external writes were changed.

## Verdict

The orchestration model is directionally correct and now closer to the Amora/OpenClaw maturity pattern:

```text
Lucas / Telegram
  ↓
Hermes Geral — COO / Orquestrador Central
  ↓
Task Router / Approval Gate
  ↓
Especialistas / profiles / bots / rotinas
  ↓
Hermes Brain — fonte de verdade, handoff, memória e evidência
```

Canonical rule preserved:

> Hermes Geral coordena. Especialistas executam. Brain registra. Produção/externo exige aprovação.

## What was audited

Canonical routing/orchestration files checked:

- `AGENTS.md`
- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `templates/handoff-especialista.md`

Agent document packages checked under `agentes/`:

- `hermes-geral`
- `lk`
- `mordomo`
- `spiti`
- `zipper`

## Amora pattern applied

Amora/OpenClaw maturity pattern adapted, not copied 1:1:

- `SOUL.md` — how the agent thinks/talks.
- `IDENTITY.md` — role, scope, runtime, boundaries.
- `USER.md` — served user/business context.
- `AGENTS.md` — operational contract, permissions, red lines.
- `MAPA.md` — navigation and output paths.
- `HEARTBEAT.md` — proactivity and silence rules.
- `TOOLS.md` — available/allowed tools and sources.
- `MEMORY.md` — local durable notes.

## Changes made

Created missing minimum package files:

- `agentes/hermes-geral/MAPA.md`
- `agentes/lk/IDENTITY.md`
- `agentes/lk/MAPA.md`
- `agentes/mordomo/IDENTITY.md`
- `agentes/mordomo/MAPA.md`
- `agentes/spiti/IDENTITY.md`
- `agentes/spiti/MAPA.md`
- `agentes/zipper/IDENTITY.md`
- `agentes/zipper/MAPA.md`

Updated:

- `AGENTS.md` — added references to `MAPA.md` and specialist `IDENTITY`/`MAPA` files.
- `empresa/contexto/organograma-agentes-hermes.md` — replaced stale gaps. Mordomo/LK/Zipper/SPITI now have minimum Amora/Hermes packages; remaining gaps are consistency/runtime enforcement, not file absence.

## Current status by agent

### Hermes Geral

- Package: now complete enough for Amora-style navigation.
- Runtime: `/opt/data`.
- Role: COO/router, central governance, approval gate, Brain consolidation.
- Remaining gap: technical enforcement of Task Router, not documentation.

### LK / LK Growth

- LK package: now includes `IDENTITY.md` and `MAPA.md`.
- Growth specialist remains canonical under `areas/lk/sub-areas/growth/` with runtime `/opt/data/profiles/lk-growth`.
- Rule preserved: LK content/blog/source pages/SEO/GEO/CRO must route to LK Growth; Hermes Geral should not draft final content by convenience.
- Remaining gap: runtime router should automatically choose `lk-growth` and require handoff.

### Mordomo

- Package: now includes `IDENTITY.md` and `MAPA.md`.
- Runtime: `/opt/data/profiles/mordomo`.
- Rule preserved: personal intake/follow-ups allowed only within guardrails; blocked for price, availability, reservation, negotiation, complaints, suppliers, bulk/campaigns, and material promises without source/approval.
- Remaining gap: ensure Mordomo cron/jobs live under Mordomo profile and handoffs are visible centrally.

### SPITI

- Package: now includes `IDENTITY.md` and `MAPA.md`.
- Runtime: `/opt/data/profiles/spiti`.
- Rule preserved: silence is better than wrong data; no lote/lance/finance/deploy/customer claim without source/approval.
- Remaining gap: future SPITI routines should be created under the SPITI profile after PRD/approval, not Main.

### Zipper

- Package: now includes `IDENTITY.md` and `MAPA.md`.
- Runtime: no dedicated profile yet; documented as read-only/documental.
- Rule preserved: no collector/artist/client contact, price, availability, proposal, or logistics-sensitive claim without approval/source.
- Remaining gap: decide later whether Zipper volume justifies dedicated profile/bot.

## Remaining gaps before Amora-level operational maturity

1. **Runtime enforcement** — the Task Router is documented but not yet a hard runtime classifier.
2. **Cron ownership reconciliation** — cron jobs still need read-only classification against the routing matrix before any migration/noise changes.
3. **Handoff enforcement** — template exists, but the system must require specialist outputs to return to Brain/Central.
4. **Legacy language cleanup** — some older LK/Zipper files still contain maintained legacy references; they are marked but not fully normalized.
5. **Zipper runtime decision** — current status is intentionally read-only/documental.

## Recommended next phase — Fase 5

Build technical Task Router enforcement without external writes:

1. Add a router/classifier layer for context + task type + risk.
2. Use the matrix to return one of:
   - `executar_aqui`
   - `delegar_especialista`
   - `preparar_approval_packet`
   - `bloquear_por_aprovacao`
   - `perguntar_clarificacao`
   - `registrar_handoff`
3. For `lk-growth-content`, block main-Hermes final content generation and route to LK Growth.
4. For Mordomo/SPITI/Zipper, enforce source and approval boundaries.
5. Add tests/regression cases for common Lucas prompts.
6. Keep all writes external/production blocked until explicit approval.

## Verification evidence

Fresh verification run after doc updates:

- Agent package check: `hermes-geral`, `lk`, `mordomo`, `spiti`, `zipper` all have `SOUL.md`, `IDENTITY.md`, `USER.md`, `AGENTS.md`, `MAPA.md`, `HEARTBEAT.md`, `TOOLS.md`, `MEMORY.md`.
- Canonical docs existence: all key routing/orchestration/handoff files exist.
- Focused secret scan over 12 changed/new files: `findings=0`.
- Git status: Brain repo already contains many pre-existing modified/untracked files outside this scope; this pass changed only the listed orchestration docs/files and did not commit/sync.
