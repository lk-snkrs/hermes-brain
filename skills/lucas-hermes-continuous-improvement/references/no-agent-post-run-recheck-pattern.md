# Lucas Hermes continuous improvement — post-run watchdog pattern

## Trigger
Use when a scheduled Hermes cron/watchdog is newly created or changed, but the next meaningful validation can only happen after its first scheduled run.

## Pattern
Prefer a one-shot `no_agent` post-check rather than restarting gateway/Docker or waiting manually in chat.

1. Identify the target job ID and expected first run time.
2. Write a tiny script under `/opt/data/scripts/` that:
   - reads `/opt/data/cron/jobs.json` read-only;
   - checks `last_run_at`/`last_status` only after the expected run window;
   - exits `0` always;
   - prints nothing when healthy or when run before the expected window;
   - prints a concise alert only when the job is missing, disabled, stale, or failed.
3. Validate the script before the expected window: stdout must be empty and rc=0.
4. Create a one-shot cron with `no_agent=True` shortly after the expected run.
5. Document the job ID and script path in Brain/report.

## Observed example
After validating Hermes v0.13 ops, cron `f5a23dd6a1bd` had not yet reached its next daily run (`2026-05-11T05:00Z`). A one-shot read-only recheck was created:

- job: `635d6bceab80`
- schedule: `2026-05-11T05:30Z`
- script: `/opt/data/scripts/hermes_daily_ci_recheck_after_first_run.py`
- behavior: silent if healthy; alert only if `f5a23dd6a1bd` has no fresh run/status is bad.

## Guardrails
- Do not change the target cron while creating the post-check unless explicitly approved.
- Do not touch Docker/gateway/Hostinger for a missing first-run observation; first gather post-run evidence.
- Keep stdout empty on OK to preserve Lucas's no-noise operating model.
