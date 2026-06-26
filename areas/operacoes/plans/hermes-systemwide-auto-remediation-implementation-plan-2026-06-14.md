# Hermes Systemwide Auto-Remediation Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task when moving beyond local/documental Fase 1.

**Goal:** Make every Hermes agent/process that detects a problem either correct it automatically within safe scope or produce a specific approval packet.

**Architecture:** Brain policy + skills establish the behavioral contract; local audit script detects scripts/crons/docs that lack the contract; future runtime enforcement starts observe-only and remains approval-gated.

**Tech Stack:** Hermes Brain markdown, Hermes skills, Python local audit script, Brain health/docs guard.

---

## Task 1: Canonical PRD and routine

**Objective:** Save the product contract in Brain.

**Files:**
- Create: `areas/operacoes/prds/hermes-systemwide-auto-remediation-prd-2026-06-14.md`
- Create: `areas/operacoes/rotinas/hermes-auto-remediation-contract.md`

**Verification:** files exist and Brain health passes.

## Task 2: Update autonomy policy and indexes

**Objective:** Make the contract discoverable by future agents.

**Files:**
- Modify: `empresa/contexto/politica-autonomia-aprovacao-hermes.md`
- Modify: `areas/operacoes/MAPA.md`
- Modify: `empresa/rotinas/_index.md`

**Verification:** targeted grep finds `Auto-Remediation Contract`; docs guard passes.

## Task 3: Update central skills

**Objective:** Ensure runtime/Brain/Hermes skills tell agents to correct safe failures automatically.

**Files:**
- Modify skill: `hermes-agent`
- Modify skill: `hermes-brain-governance`
- Modify skill: `lucas-runtime-operations`

**Verification:** `skill_view` or filesystem readback shows the rule.

## Task 4: Add local audit script

**Objective:** Detect scripts/crons/docs likely to diagnose without correction contract.

**Files:**
- Create: `scripts/auto_remediation_contract_audit.py`

**Verification:**

```bash
python3 -m py_compile scripts/auto_remediation_contract_audit.py
python3 scripts/auto_remediation_contract_audit.py
```

Expected: JSON with `status=ok` and candidate lists. Candidate count is not failure; it is backlog.

## Task 5: Future waves for scripts/crons

**Objective:** Patch concrete scripts only after reviewing the audit output.

**Rules:**
- No cron schedule/delivery mutation without approval.
- No runtime/gateway restart without approval.
- Patch only local allowlisted script behavior with tests/simulation.
- Preserve silent-OK.

**Verification:** per-script simulation, cron dry-run/readback, secret scan, receipt.
