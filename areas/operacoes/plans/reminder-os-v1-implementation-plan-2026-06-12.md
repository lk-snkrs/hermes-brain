# Reminder OS v1 Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task only for local/documental/code-safe work. Do not dispatch runtime/external workers without scoped approval.

**Goal:** Turn Reminder OS from v0 concept/watchdog into a reliable cross-agent continuity layer with schema validation, tests, profile rollout, and low-noise Telegram behavior.

**Architecture:** Brain remains the governance source; `reminders.jsonl` is the local ledger; Kanban is the operational visibility layer; `reminder_os_watchdog.py` is the 2h silent-OK monitor; profile/worker contracts enforce adoption. Reminder OS reminds and routes; it never executes sensitive actions.

**Tech Stack:** Python stdlib, JSONL, Hermes cron no_agent, Hermes Kanban CLI, Brain markdown docs, offline tests.

---

## Phase 1 — Make the current v0 reliable

### Task 1: Add schema constants to Reminder OS docs

**Objective:** Ensure the schema is clear enough for agents and scripts to follow.

**Files:**
- Modify: `areas/operacoes/reminder-os/LEDGER.md`
- Modify: `areas/operacoes/reminder-os/README.md`

**Steps:**
1. Add exact allowed values for `status` and `severity`.
2. Add one valid JSONL example.
3. Add one invalid example and why it fails.
4. Verify with `read_file` that examples are present.

**Acceptance:** Docs show required fields, allowed enums, and safe/no-secret rule.

### Task 2: Create `reminder_os_add.py`

**Objective:** Provide a safe helper to append validated reminders to the ledger.

**Files:**
- Create: `/opt/data/scripts/reminder_os_add.py`

**Implementation requirements:**
- Python stdlib only.
- CLI args: `--title`, `--owner`, `--status`, `--next-action`, optional `--severity`, `--source`, `--evidence`, `--risk`, `--due-at`, `--next-review-at`.
- Auto-generate `id` when omitted.
- Add `created_at` and `updated_at` in UTC.
- Reject missing required fields.
- Reject unknown `status` and `severity`.
- Reject strings containing obvious credential markers such as token assignment, API-key labels, password labels, or HTTP authorization header prefixes.
- Append one JSON object per line to `areas/operacoes/reminder-os/reminders.jsonl`.
- Print only `created <id>`; never print the full object.

**Verification:**
```bash
python3 /opt/data/scripts/reminder_os_add.py --help
python3 /opt/data/scripts/reminder_os_add.py --title "Reminder OS test" --owner "Hermes Geral" --status scheduled_check --next-action "Verificar helper" --next-review-at "2099-01-01T00:00:00Z"
tail -1 /opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/reminder-os/reminders.jsonl
```

**Acceptance:** Valid loop is appended; invalid enum fails nonzero; secret-like value fails nonzero.

### Task 3: Add offline tests for helper validation

**Objective:** Prevent schema regressions.

**Files:**
- Create: `/opt/data/scripts/test_reminder_os.py`

**Test cases:**
1. valid reminder returns rc 0 and appends JSONL;
2. missing title returns nonzero;
3. invalid status returns nonzero;
4. invalid severity returns nonzero;
5. secret-like text returns nonzero;
6. generated JSON has `id`, `created_at`, `updated_at`.

**Verification:**
```bash
python3 /opt/data/scripts/test_reminder_os.py
```

**Acceptance:** Tests pass without touching external systems.

### Task 4: Harden watchdog duplicate suppression

**Objective:** Ensure old Kanban backlogs do not page Lucas repeatedly.

**Files:**
- Modify: `/opt/data/scripts/reminder_os_watchdog.py`

**Checks:**
1. Run watchdog once with existing state.
2. Run immediately again.
3. Confirm second run prints nothing unless a forced `waiting_lucas` ledger item exists.
4. Confirm output contains no job IDs, raw JSON, or secrets.

**Verification:**
```bash
/opt/data/scripts/reminder_os_watchdog.py >/tmp/reminder1.out
/opt/data/scripts/reminder_os_watchdog.py >/tmp/reminder2.out
wc -c /tmp/reminder1.out /tmp/reminder2.out
```

**Acceptance:** Immediate second run is silent for non-forced stale backlog.

## Phase 2 — Cross-agent rollout

### Task 5: Patch profile AGENTS contracts

**Objective:** Make Reminder OS present in all major agents.

**Files:**
- Modify if exists: `/opt/data/profiles/*/AGENTS.md`

**Profiles to cover first:**
- `lk-growth`
- `lk-stock`
- `lk-shopify`
- `lk-ops`
- `lk-trends`
- `lk-content`
- `lk-finance`
- `lk-collection-optimizer`
- `spiti`
- `mordomo`

**Patch block:**

```markdown
## Reminder OS

If relevant work cannot be closed in the current turn, register or hand off a Reminder OS loop with owner, next action, evidence and review trigger. Do not execute the remembered task automatically. Telegram remains silent-OK unless Lucas action is needed.
```

**Verification:**
```bash
grep -R "## Reminder OS" /opt/data/profiles/*/AGENTS.md
```

**Acceptance:** Every listed profile has the Reminder OS block.

### Task 6: Patch Kanban worker/orchestrator guidance references if needed

**Objective:** Ensure Kanban workers treat stand-by as a Reminder OS loop, not just a stale card.

**Files:**
- Existing Kanban skills/references if appropriate.
- Do not patch Hermes runtime code unless a tested bug requires it and Lucas approves.

**Acceptance:** Kanban docs mention Reminder OS as continuity layer while preserving “assignment can execute” guardrail.

## Phase 3 — Brain/Memory/Mesa integration

### Task 7: Extend handoff/receipt templates with Reminder OS field

**Objective:** Make future handoffs expose unresolved next actions.

**Files:**
- Relevant Brain templates under `areas/operacoes/rotinas/`.

**Field:**

```markdown
Reminder OS loop needed: yes/no
Owner:
Next action:
Review trigger:
Evidence:
```

**Acceptance:** New material outputs can explicitly say whether a reminder loop is needed.

### Task 8: Create Memory OS integration spec, not code yet

**Objective:** Define how Memory OS writes Reminder OS loops without duplicate noise.

**Files:**
- Create: `areas/operacoes/reminder-os/memory-os-integration-v1.md`

**Content:**
- trigger rules;
- dedupe key;
- silence rules;
- failure behavior;
- tests needed before hook activation.

**Acceptance:** Spec exists before any Memory OS hook mutation.

### Task 9: Create Mesa COO integration spec

**Objective:** Define when a loop becomes a Mesa COO decision.

**Files:**
- Create: `areas/operacoes/reminder-os/mesa-coo-integration-v1.md`

**Rules:**
- high-severity `waiting_lucas` loops can become Decisão 1/N;
- stale low-priority loops should be summarized or expired, not paged individually;
- Mesa must not expose job IDs/JSON.

**Acceptance:** Mesa promotion criteria are documented.

## Phase 4 — Verification and hygiene

### Task 10: Run Brain health

**Objective:** Verify Brain docs/indexes are consistent.

**Command:**
```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain && python3 /opt/data/hermes_brain_wave14_publish/scripts/brain_health_check.py --json reports/brain-health-check-2026-06-12-reminder-os-v1.json
```

**Acceptance:** `FAIL=0 WARN=0`.

### Task 11: Verify cron status

**Objective:** Confirm Reminder OS cron exists and is scheduled every 2h.

**Method:** Use `cronjob list` or Hermes CLI read-only cron list.

**Acceptance:** Job named `Reminder OS — 2h open-loop watchdog` is enabled and scheduled every 120m.

### Task 12: Telegram-safe final report

**Objective:** Report to Lucas concisely.

**Report should include:**
- PRD path;
- implementation plan path;
- cron cadence;
- whether tests passed;
- Brain health result;
- writes externos = 0;
- next decision if needed.

**Do not include:**
- job ID;
- raw JSON;
- full script output;
- internal wrappers;
- secret previews.

## Execution status — 2026-06-12

- Phase 1: executed locally; helper and offline tests pass.
- Phase 2: executed locally/documentally across native Hermes Agent profiles in `/opt/data/profiles/*/AGENTS.md`.
- Product correction from Lucas: Reminder OS will not use Mission Control. Operational surface is native Hermes Agent: agents/profiles, Brain, Kanban, cron/watchdog and local ledger.
- Phase 3: executed locally/documentally. Memory OS integration spec and Mesa COO integration spec created; receipt/handoff templates now include Reminder OS loop fields; Memory OS and Mesa COO routines point to the new specs.
- Phase 4: executed locally/read-only. Created `/opt/data/scripts/reminder_os_report.py` and generated open-loop reports by owner/status/severity under `reports/reminder-os/`; no runtime/cron/gateway mutation.
- Phase 5: executed locally. Classified the 5 stale `ready` cards on Kanban board `reminder-os` as fechar/completed after reconciling them against completed Phase 1–4 artifacts; no assignee, no dispatch, no external writes.
- Phase 6: executed locally/read-only. Audited adoption across 10 native profiles: 10/10 `AGENTS.md` files include Reminder OS, silent-OK, and no-auto-execution guardrails; no blocking gaps found.
- Phase 7: executed locally/read-only. Created `/opt/data/scripts/reminder_os_ingress_audit.py` to scan Brain handoffs/receipts/approval-packets/reports for explicit Reminder OS loop markers and identify `loop needed: yes` artifacts not covered by active ledger evidence. Generated `reports/reminder-os/ingress-audit-2026-06-12.md` and `.json`; current result: `open_needed_count=0`.
- Phase 8: executed locally/code-safe. Integrated ingress gaps into the existing 2h watchdog: uncovered `Reminder OS loop needed: yes` markers now become Telegram-safe candidates; covered/closed markers remain silent. No new cron, no loop auto-creation, no card dispatch, no Mission Control surface.
- Phase 9: executed locally/documentally plus read-only audit. Created `/opt/data/scripts/reminder_os_template_audit.py`; patched central handoff/receipt templates so canonical Reminder OS fields are explicit; generated `reports/reminder-os/template-audit-2026-06-12.md` and `.json`; current result: `gap_count=0`, 4/4 templates covered.
- Phase 10: executed locally/code-safe. Created `/opt/data/scripts/reminder_os_health_gate.py` to aggregate ledger, ingress, templates and Kanban into a single PASS/FAIL contract. Generated `reports/reminder-os/health-gate-2026-06-12.md` and `.json`; current result: `status=PASS`, `blocker_count=0`, `warning_count=0`.
- Phase 11: executed locally/code-safe/documentally. Integrated the health gate into the existing 2h watchdog, created `/opt/data/scripts/reminder_os_status.py` for compact on-demand status, indexed Reminder OS in `areas/operacoes/MAPA.md`, and added regressions for watchdog health blockers and the status command. No new cron, no loop auto-creation, no card dispatch, no Mission Control surface.
- External writes: 0.

