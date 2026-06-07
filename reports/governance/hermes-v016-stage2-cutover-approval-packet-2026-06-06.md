# Hermes v0.16 Stage 2 — Controlled Cutover Approval Packet

- Date: 2026-06-06T13:59:39+00:00
- Prepared by: Hermes default profile
- Trigger: Lucas replied “aprovo” after Stage 1 validation. Interpreted conservatively as approval to prepare this Stage 2 packet, **not** approval to execute production cutover.
- Current live runtime: Hermes Agent `v0.15.2 (2026.5.29.2)`
- Target candidate: Hermes Agent `v0.16.0 (2026.6.5)`
- Candidate path: `/opt/data/hermes-v016-candidate-20260606/src`
- Live config: `/opt/data/config.yaml`

## Executive decision needed

Approve or block a controlled production cutover from Hermes v0.15.2 to Hermes v0.16.0 using the already validated candidate runtime.

This packet is **not** itself a cutover. It defines the exact scope, prechecks, backup, rollback, execution plan, and postchecks required before touching production.

## Stage 1 evidence summary

Stage 1 report:

- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-v016-stage1-candidate-runtime-validation-2026-06-06.md`

Stage 1 receipt:

- `/opt/data/hermes_bruno_ingest/hermes-brain/receipts/hermes-v016-stage1-candidate-runtime-validation-receipt-2026-06-06.md`

Validated in the isolated candidate:

- Candidate version: PASS — `Hermes Agent v0.16.0 (2026.6.5)`
- Candidate config check: PASS — exit 0; config version `24 → 27` noted
- Migration preview on copied config: PASS — exit 0; live config SHA unchanged
- Critical imports: PASS — `critical_imports_ok 9`
- Py compile: PASS — `py_compile_ok`
- Inline-button clean delivery smoke: PASS — `inline_marker_clean_delivery_ok`
- Selected pytest matrix: PASS — `395 passed in 19.24s`
- Secret scan: PASS — `secret_scan_hits []`
- Brain Health: PASS — `All checks passed`

## Important candidate patch requirement

The candidate tree contains a local patch required to preserve Lucas-facing Mesa COO / Telegram decision-card UX.

Patched candidate files:

- `/opt/data/hermes-v016-candidate-20260606/src/cron/scheduler.py`
- `/opt/data/hermes-v016-candidate-20260606/src/gateway/platforms/telegram.py`
- `/opt/data/hermes-v016-candidate-20260606/src/tools/send_message_tool.py`

Patch behavior:

- strips trailing hidden `<!-- HERMES_INLINE_BUTTONS:{...} -->` markers before delivery;
- converts marker payload into structured `inline_buttons` metadata;
- passes metadata through runtime adapter and standalone send paths;
- renders Telegram native inline buttons via `reply_markup`;
- uses compact callback data `cj:<context>:<value>`;
- prevents hidden scheduler/marker text from appearing in Telegram.

Decision: do **not** deploy a vanilla v0.16 artifact unless this patch is carried forward or an upstream-equivalent fix is confirmed.

## Proposed Stage 2 scope

If Lucas explicitly approves execution of Stage 2, perform only the following:

1. Create a timestamped backup bundle:
   - `/opt/data/config.yaml`
   - `/opt/data/.env` if present, copied with permissions preserved and never printed
   - default profile cron registry/state relevant to gateway operation
   - current `/opt/hermes` launcher/runtime metadata sufficient for rollback
   - current Hermes version/config check outputs, sanitized
2. Preserve candidate-local inline-button patch in the production-bound artifact.
3. Run a final preflight on the candidate:
   - version check;
   - config check;
   - critical imports;
   - py_compile;
   - inline-button smoke;
   - selected pytest matrix or narrower emergency matrix if timeboxed.
4. Stop or drain the affected gateway/runtime only in the maintenance window.
5. Switch the production launcher/runtime pointer to the v0.16 candidate or equivalent prepared artifact.
6. Run `hermes config migrate` against the live config **only after backup**.
7. Start/restart the affected gateway/runtime.
8. Validate post-cutover runtime and platform health:
   - `hermes --version` reports v0.16.0 from the production path;
   - `hermes config check` reports version 27/current;
   - exact gateway process has expected `HERMES_HOME=/opt/data`;
   - API health responds locally if enabled;
   - webhook health responds locally if enabled;
   - Telegram adapter connects;
   - cron scheduler starts;
   - Mesa COO inline-button delivery path is validated with a safe/local or Lucas-approved Telegram test;
   - no secret leakage in logs/artifacts.
9. Write a post-cutover receipt and Brain report.
10. If any critical validation fails, rollback immediately.

## Explicitly out of scope unless separately approved

- Docker image rebuild or container recreation beyond what is explicitly required for this runtime cutover.
- Hostinger/VPS package changes.
- Traefik/public routing changes.
- Dashboard/API public exposure changes.
- New webhooks or external integrations.
- Shopify/Tiny/GMC/GitHub/source-of-truth writes.
- Secrets rotation or new credentials.
- Starting/stopping unrelated specialist gateways.
- Broad cron redesign.

## Pre-cutover backup plan

Create backup root:

- `/opt/data/backups/hermes-v016-cutover-20260606-HHMMSS/`

Minimum backup contents:

- `config.yaml.before-v016`
- `.env.before-v016` if present, mode `0600`, never printed
- `hermes-version-before.txt`
- `config-check-before.txt` sanitized
- `process-inventory-before.txt` sanitized
- `candidate-diff-before.patch` sanitized
- `rollback-instructions.md`

If Docker/launcher metadata is required, capture read-only metadata first and include it in the backup bundle without mutating containers.

## Rollback plan

Rollback trigger examples:

- production `hermes --version` is not v0.16.0 after cutover;
- config migration fails;
- gateway does not start;
- Telegram cannot connect/send;
- API/webhook health fails unexpectedly;
- Mesa COO buttons leak raw markers/wrappers or are not native buttons;
- cron scheduler fails to start;
- provider/model startup fails in a way not recovered by existing fallback;
- secret leakage appears in logs/artifacts.

Rollback actions:

1. Restore launcher/runtime pointer to the previous live v0.15.2 runtime.
2. Restore `/opt/data/config.yaml` from the pre-cutover backup.
3. Restart only the affected gateway/runtime.
4. Verify `hermes --version` reports v0.15.2.
5. Verify config check returns version 24/current for the restored runtime.
6. Verify Telegram/API/webhook/cron health as applicable.
7. Write rollback receipt with failure trigger and evidence.

## Proposed final verification checklist for execution

Before declaring Stage 2 complete, run and record:

- production version check;
- production config check;
- process inventory by exact `HERMES_HOME`;
- local API health if enabled;
- webhook health if enabled;
- gateway log startup markers;
- Telegram connectivity evidence;
- cron scheduler status;
- safe inline-button delivery test or approved real Telegram probe;
- targeted secret scan over new reports/receipts/log excerpts;
- Brain Health.

## Approval options

Recommended option: **Approve Stage 2 execution with patch + backup + rollback**, during a controlled maintenance window.

Alternative options:

1. **Preview only** — keep candidate prepared, no production cutover.
2. **Block for upstream** — wait until an upstream release confirms equivalent inline-button behavior.
3. **Execute Stage 2 now** — only if Lucas explicitly approves production cutover under this packet’s scope.
4. **Revise packet** — adjust scope, timing, tests, or rollback before execution.

## Exact approval wording needed for execution

To avoid ambiguity, Stage 2 execution should require a fresh explicit approval like:

> Aprovo executar Stage 2 Hermes v0.16: backup, carregar patch de inline buttons, migrar config 24→27, swap/restart controlado do runtime Hermes default, validar Telegram/API/webhook/cron, e rollback se falhar. Não aprovo Docker/Traefik/VPS/dashboard/externos fora desse escopo.

Without that explicit production-cutover approval, no swap/restart/migration will be executed.
