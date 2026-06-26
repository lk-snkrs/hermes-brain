# Brain + GMC Governance Re-audit — 2026-05-22

Generated at: `2026-05-22T14:03Z`
Scope: read-only/local audit of Hermes Brain governance, cron control plane, operational docs guard, safe-sync dry-run, and LK GMC review queues.

## Verdict

Overall status: `mostly_correct_with_improvement_backlog`.

The core governance work is correct:

- Brain health check is clean: `FAIL=0`, `WARN=0`.
- Operational docs guard passes for its current configured scope: `scanned_files=180`, `fail_count=0`.
- Live cron registry matches the control-plane snapshot: `27` jobs total, `22` scheduled, `5` paused, no observed delivery error.
- Brain Sync dry-run remains safe: branch `consolidation/brain-filesystem-git-hygiene-20260516`, `allowed_files=74`, `skipped_files=301` after the refreshed local GMC queue report.
- LK GMC read-only queue refresh confirms the same blocker shape: `98` missing-color review rows and `12` GTIN products pending review; `writes_performed=0`.

## What is correct

1. `areas/operacoes/intelligence-map.md` correctly centralizes the runtime hierarchy and anti-duplication rules.
2. `areas/operacoes/rotinas/cron-control-plane.md` matches the live cron registry by count and status.
3. `areas/operacoes/rotinas/decision-inbox-taxonomy.md` fixes the earlier false-positive class and gives safe action categories.
4. `scripts/operational_docs_guard.py` blocks risky live operational docs in the intended docs scope.
5. GMC continuation remains safe/read-only and has not performed Merchant/Shopify/feed writes.

## Gaps / improvements found

### P1 — Guard coverage is too narrow

The current operational docs guard only scans:

- `areas/operacoes`
- `empresa`
- `memories`

It does not scan root docs, `skills/`, general `reports/`, or executable scripts by default. A broader custom scan over `1970` text/script files found legacy-risk references outside the protected scope, including:

- `monitor_daemon.py` with `/root/.hermes/...` paths.
- `alert_system.py` with `/root/.hermes/...` paths and remediator path.
- `scripts/hermes_consolidation_weekly.py` calling `/root/.hermes/scripts/...`.
- `scripts/session_end_summary.py` using legacy Mem0 API flow.
- `skills/lk-crosssell/SKILL.md` referencing `/root/lk-price/`.

These did not break the official guard because they are outside its current scan scope.

### P1 — Legacy executable scripts still exist

Even if not wired to live cron now, executable or importable legacy scripts with stale `/root` or Mem0 behavior remain a future-agent hazard. They should be converted to safe stubs or clearly marked `DEPRECATED / DO NOT RUN` at file top.

Priority candidates:

- `monitor_daemon.py`
- `alert_system.py`
- `scripts/hermes_consolidation_weekly.py`
- `scripts/session_end_summary.py`

### P2 — Too many untracked local artifacts

Current git/worktree state shows a large local backlog:

- modified files: `63`
- untracked files: `302`

This is not necessarily unsafe, but it increases cognitive load and makes future audits harder. The safe-sync allowlist skipped `301` files, which is expected, but those skipped reports/receipts should be classified as one of:

- durable docs to allowlist/version;
- local-only receipts;
- stale artifacts to archive/remove.

### P2 — 02h30 executive report vs Mesa COO overlap remains unresolved

The control plane correctly identifies possible duplication between:

- `98478b820720` — 02h30 executive report to Telegram.
- `749ee30b51eb` — 08h30 Mesa COO.

Recommendation: run a 7-day overlap audit and then either merge, suppress duplicates, or keep both with strict role separation.

### P2 — Paused cron backlog needs final decisions

The 5 paused jobs are correctly documented, but they remain pending. Recommended final action:

- remove expired one-shot SEO review if no longer needed;
- keep influencer email paused pending FHITS/Pareto/destinatários;
- migrate Mordomo jobs to Mordomo profile only if the active profile job is verified;
- keep main scheduler clean from specialist-operational loops.

### P3 — Guard false-positive/false-negative quality can improve

The broader scan shows some naive matches such as words containing `shutdown` or `passwd` in regex strings. The guard should become structured:

- scan docs and scripts with separate rules;
- ignore known safe regex definitions;
- detect only executable command contexts for host mutation;
- require top-of-file `DEPRECATED / DO NOT RUN` for executable legacy files, not just nearby prose.

## Recommended next package

Safe local/docs-only package:

1. Expand `operational_docs_guard.py` into two modes:
   - default docs mode;
   - `--strict-runtime` mode for root docs, skills, scripts and executable files.
2. Convert the four legacy scripts above into explicit safe stubs or mark them with hard `DEPRECATED / DO NOT RUN` banners.
3. Patch `skills/lk-crosssell/SKILL.md` to replace `/root/lk-price/` with current/source-verified path or mark it historical.
4. Create a skipped-artifact classification report for the `301` files skipped by Brain Sync.
5. Decide the 5 paused crons.
6. Audit 02h30 vs Mesa COO duplication after 7 days of outputs.

## Verification evidence

- Brain health: `FAIL=0`, `WARN=0` across secrets, links, required files, agent files, area maps, decisions index, routines index and skill references.
- Operational docs guard: `scanned_files=180`, `fail_count=0`.
- Brain Sync dry-run: branch `consolidation/brain-filesystem-git-hygiene-20260516`, `allowed_files=74`, `skipped_files=301`.
- Live cron registry: `27` jobs; `22` scheduled; `5` paused.
- LK GMC queue refresh: `98` missing-color pending rows; `12` GTIN products; `writes_performed=0`; Content API GET only.

## External side effects

None. No Docker/VPS/Traefik/container/cron mutation, no Shopify/Merchant/feed write, no WhatsApp/email/database write, no campaign or customer contact.
