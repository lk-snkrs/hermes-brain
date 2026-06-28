# Receipt — CLI-first API migration active paths — 2026-06-27

Status: active scheduled raw-API execution paths eliminated or converted.

## Policy

1. CLI official / Hermes-Doppler-first wrapper first.
2. MCP second.
3. Raw direct API/HTTP only as justified exception with approval + rollback/readback.
4. External writes remain approval-gated; values_printed=false.

## Converted active/root paths

- `/opt/data/scripts/hermes_doppler.py`: Doppler helper now uses `doppler secrets download --no-file --format=json` via CLI instead of direct Doppler API.
- `/opt/data/scripts/hermes_cli_integrations.py`: smokes moved to CLIs where available (`ntn`, `wrangler`, `gh`, `shopify store execute`, `klaviyo get flows`, `gws`, `sentry-cli`); Linear is blocked as `lin` has no read-only smoke.
- `/opt/data/scripts/hermes_daily_intelligence_preflight.py`: GitHub release probe now uses `gh api`.
- `/opt/data/scripts/brain_sync_safe.py`: token lookup delegates to `hermes_doppler.py run` instead of direct Doppler API.
- `/opt/data/scripts/zipper_gmail_style_learner.py`: Gmail reads now route through `hermes-cli-run gws`.
- Honcho watchdog/auditors: local health checks moved from raw HTTP `/health` to Docker/SDK/process checks.
- `/opt/data/scripts/watchdog_claude_proxy.sh`: local HTTP health probe replaced by process check.

## Converted active profile cron scripts

- `lk-content/scripts/klaviyo_sent_watchdog.py`: campaign listing now uses `hermes-cli-run klaviyo get campaigns --stdout`.
- `lk-ops/scripts/lk_pos_restock_exception_monitor.py`: Shopify recent POS read now uses `hermes-cli-run shopify store execute`; local raw diagnostic POST disabled.
- `lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py`: GitHub token lookup uses Doppler helper; product readback uses `hermes-cli-run shopify store execute`.
- `lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py`: live latest order readback uses `hermes-cli-run shopify store execute`.
- `mordomo/scripts/mordomo_wacli_pessoal_audio_watchdog.py`: raw local `/healthz` call replaced by process-based health.

## Disabled pending CLI/MCP implementation

- `LK Stock OS Supabase read-model sync hourly` was disabled in `/opt/data/profiles/lk-stock/cron/jobs.json` because it still uses raw Hub/Supabase REST writes and needs a proper Supabase CLI/MCP-backed rewrite before it can run under the new policy.
- Backup: `/opt/data/backups/cli-mcp-raw-api-migration-20260627/lk-stock-cron-jobs.before-disable-raw-supabase.json`.

## Verification

- Active enabled cron jobs referencing raw `requests/httpx/urllib.request/curl`: `0`.
- Cron registries scanned: `11`.
- Enabled jobs scanned: `84`.
- `py_compile` for touched Python scripts: OK.
- `lk-stock/cron/jobs.json`: JSON OK.
- Doppler helper doctor: OK via Doppler CLI, `values_printed=false`.
- Hermes CLI inventory: OK, `values_printed=false`.
- Brain health: All checks passed.

## Known remaining static raw files

There are still inactive/manual legacy scripts and third-party/profile skill files with direct HTTP/API code. They are not referenced by enabled cron jobs after this migration. They should be converted opportunistically when revived, or blocked/deleted after owner review, because blind mass rewrites could break stale one-off operational scripts without improving live behavior.

values_printed=false
