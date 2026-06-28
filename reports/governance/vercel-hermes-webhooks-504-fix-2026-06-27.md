# Vercel hermes-webhooks 504 fix — 2026-06-27

Status: fixed/deployed/verified.
values_printed=false

## Incident
- Alert: Vercel/Sentry Medium Severity, 504 timeouts on `/api/webhooks/[route]`.
- Project: `lk-snkrs-projects` / `hermes-webhooks`.
- Started: 2026-06-27 13:40 UTC.
- Root cause confirmed by read-only logs: Vercel waited synchronously for upstream Hermes Gateway responses while Shopify webhook bursts hit slow Hermes agent-mode processing. Vercel serverless killed requests at 300s.

## Scoped approval
Lucas approved: “Fazer do 1 ao 6”.
Scope executed:
1. backup;
2. deterministic script adapter;
3. route change to script mode;
4. local/signed probe verification;
5. runtime hot-reload/reload verification;
6. Vercel proxy hardening + production deploy verification.

## Changes made

### 1) Backup
Backup directory:
- `/opt/data/backups/hermes-webhooks-504-fix-20260627T173304Z`

Backed up:
- `/opt/data/webhook_subscriptions.json`
- `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
- `/opt/data/hermes-webhooks/api/webhooks/[route].js`
- `/opt/data/hermes-webhooks/vercel.json`

### 2) Deterministic script adapter
File changed:
- `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`

Added `process_stdin_webhook()` + `--stdin-webhook` support:
- reads raw JSON from stdin as passed by Hermes `run_script` mode;
- uses `HERMES_WEBHOOK_EVENT_TYPE` and `HERMES_WEBHOOK_DELIVERY_ID`;
- returns compact JSON with `values_printed=false` and `write_executed=false`;
- keeps the processor deterministic/local-only, avoiding the slow LLM/agent route.

### 3) Route switched to deterministic script mode
File changed:
- `/opt/data/webhook_subscriptions.json`

Route changed:
- `lk-shopify-tiny-stock-sync`

New runtime mode:
- `kind: script`
- `run_script: true`
- `script: /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
- `script_timeout: 45`
- existing secret/events preserved.

The Gateway reloads dynamic subscriptions on each request, so no main/default restart was required for this route change.

### 4) Vercel proxy hardening
File changed:
- `/opt/data/hermes-webhooks/api/webhooks/[route].js`

Change:
- `forwardToHermes()` now uses `AbortController` with `HERMES_UPSTREAM_TIMEOUT_MS || 55000`.
- On abort, proxy returns controlled `502 { error: "upstream_timeout" }` instead of waiting until Vercel kills the function at 300s.

Production deployment:
- `https://hermes-webhooks-m3in2djwn-lk-snkrs-projects.vercel.app`
- Status: Ready
- Created: 2026-06-27 17:36 UTC
- Aliases remained healthy:
  - `https://hermes-webhooks.lucascimino.com/health`
  - `https://hermes-webhooks.vercel.app/health`

## Verification evidence

### Syntax/tests
- `python3 -m py_compile /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`: OK
- `node --check /opt/data/hermes-webhooks/api/webhooks/[route].js`: OK
- `python3 -m pytest /opt/data/scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py -q`: `7 passed in 0.55s`
- JSON validation:
  - `/opt/data/webhook_subscriptions.json`: OK
  - `/opt/data/hermes-webhooks/vercel.json`: OK
- `git diff --check` in `/opt/data/hermes-webhooks`: OK

### Local deterministic adapter
No-op unpaid Shopify payload through stdin adapter:
- exit code: `0`
- seconds: `0.102`
- status: `ignored`
- reason: `order_not_paid`
- write_executed: `false`
- values_printed: `false`

### Public signed probe after route change and deploy
Signed Shopify no-op probe to canonical public route:
- URL: `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`
- HTTP: `200`
- seconds: `1.057`
- status: `ignored`
- reason: `order_not_paid`
- transport: `hermes_run_script`
- write_executed: `false`
- values_printed: `false`

### Health checks
- `https://hermes-webhooks.lucascimino.com/health`: HTTP 200
- `https://hermes-webhooks.vercel.app/health`: HTTP 200
- local upstream before fix: `http://127.0.0.1:8644/health`: HTTP 200

### Vercel error check
After deploy/verification:
- `vercel logs --project hermes-webhooks --scope lk-snkrs-projects --environment production --since 15m --status-code 504 --json --limit 100`
- result: `0` 504 logs returned
- values_printed=false

## Safety
- Customer messages sent: 0
- Shopify writes: 0
- Tiny writes: 0
- Klaviyo writes: 0
- Secrets printed: 0
- values_printed=false

## Remaining observation
If future bursts still produce 5xx, the new proxy should fail fast with controlled `upstream_timeout` instead of Vercel runtime 300s. The route `lk-shopify-tiny-stock-sync` should no longer invoke the slow agent path; signed no-op proved `transport=hermes_run_script` in ~1s.
