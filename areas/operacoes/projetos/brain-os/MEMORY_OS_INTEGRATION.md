# Brain OS ↔ Memory OS Integration

**Status:** canonical governance contract.
**Mode:** local/documental; no runtime mutation by this file.
**Updated:** 2026-06-11.

## Contract

Brain OS, Memory OS, skills, and receipts have different jobs. They must not collapse into the same layer.

- **Brain OS:** stores rich business/project intelligence, canonical project hubs, executive status, source-of-truth rules, current state, decisions, timelines, and artifact indexes.
- **Memory OS:** routes compact context into future agent turns and keeps only durable facts/preferences that reduce repeated steering. It must not absorb rich project archives or stale operational receipts.
- **Skills:** store reusable procedures and operating playbooks: how to run audits, create reports, use APIs safely, debug recurrent systems, and verify before completion.
- **Receipts/reports:** store evidence of what happened: command outputs, audit results, generated reports, approvals, execution traces, and snapshots. They are evidence, not live state.

## Routing rules

1. If the information is rich, project-specific, or needs curation: put it in **Brain OS**.
2. If it is a compact durable preference/fact that should affect future behavior: put it in **Memory OS**.
3. If it is a repeatable workflow or command pattern: put it in a **skill**.
4. If it proves that something happened: put it in a **receipt/report**.
5. If the question depends on current external state, consult the **live source** before answering or acting.

## Non-goals

- Brain OS must not become a live database replacement for Tiny, Shopify, GMC, Meta, Klaviyo, Chatwoot, Supabase, GitHub, or runtime state.
- Memory OS must not become a dump of PR numbers, receipts, report bodies, or temporary task state.
- Skills must not contain raw secrets, one-off receipts, or stale execution logs.
- Receipts must not be treated as authorization for future writes.

## Handoff protocol

When updating a hub:

1. Update Brain OS hub docs first: `CURRENT_STATE.md`, `DECISIONS_AND_GUARDRAILS.md`, `NEXT_STEPS.md`, and `ARTIFACT_INDEX.md` as applicable.
2. Add or update Memory OS only if there is a compact durable fact/preference.
3. Add or patch a skill only if the procedure will recur.
4. Save receipts/reports for evidence, with secret values redacted.
5. Re-run Brain OS scanner/health if the change affects hub status or governance reports.

## Telegram/noise policy

Telegram receives only actionable alerts or explicitly requested summaries. Routine Brain OS and Memory OS jobs should be silent/local when healthy.

## Current implementation evidence

- Brain OS scanner: `scripts/brain_os_scanner_v2.py`.
- Brain OS health: `scripts/brain_os_health.py`.
- Brain OS executive status: `scripts/brain_os_executive_status.py`.
- Source-of-truth matrix: `scripts/brain_os_source_truth_matrix.py`.
- Strict docs/runtime guard: `scripts/brain_os_docs_runtime_guard.py`.
- Silent-OK script: `scripts/brain_os_silent_ok_check.py`.
- Cron wrapper: default profile script `brain_os_silent_ok_watchdog.py`.

## Guardrails

- No secrets in Brain, Memory, skills, reports, receipts, cron output, or Telegram.
- No external writes from Brain OS scores or reports.
- No runtime/Docker/VPS/cron changes without scoped approval and verification.
- Health/scanner OK stays silent; only real degradation should alert Telegram.
