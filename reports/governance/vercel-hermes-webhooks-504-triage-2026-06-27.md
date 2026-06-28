# Vercel hermes-webhooks 504 triage — 2026-06-27

Status: read-only triage completed; no production deploy/restart/config mutation executed.
values_printed=false

## Alert
- Source: Vercel email / Sentry anomaly
- Project: `lk-snkrs-projects` / `hermes-webhooks`
- Route family: `/api/webhooks/[route]` (public rewrite: `/webhooks/<route>`)
- Started: 2026-06-27 13:40 UTC
- Alert sample: 59 failed requests in last 5 minutes; previous 24h avg 0.

## Read-only evidence
- Current UTC checked: 2026-06-27T17:01:39Z.
- Vercel auth smoke: OK via Hermes CLI wrapper; values not printed.
- Public health:
  - `https://hermes-webhooks.lucascimino.com/health` => HTTP 200, ~1.06s.
  - `https://hermes-webhooks.vercel.app/health` => HTTP 200, ~0.33s.
- Upstream local gateway health: `http://127.0.0.1:8644/health` => HTTP 200, ~0.006s.
- Vercel deployment inspected: `dpl_2gr5yZk77XFT6FY95c6EMDoMgfjH`, status Ready, created 2026-06-24, build contains `api/webhooks/[route]` serverless function.
- Vercel logs, status 504, since 4h, parsed 1000 records. Returned window was 2026-06-27T14:31:08Z–14:38:32Z, all with `Vercel Runtime Timeout Error: Task timed out after 300 seconds`.
- Top 504 paths in sampled Vercel logs:
  - `/webhooks/lk-online-waba-dryrun`: 400/1000
  - `/webhooks/lk-stock-shopify-sales-os`: 300/1000
  - `/webhooks/lk-shopify-orders-ingest`: 160/1000
  - `/webhooks/lk-shopify-birthday-klaviyo-sync`: 60/1000
  - `/webhooks/lk-shopify-tiny-stock-sync`: 60/1000
  - `/webhooks/lk-shopify-pos-restock`: 20/1000
- Vercel 504s in last 30 minutes at triage time: 0.
- Negative auth probes to key routes returned HTTP 401 `missing_shopify_signature` quickly (~0.18–0.20s), proving public Vercel function is currently responsive.

## Local gateway correlation
- Local gateway logs around 13:20–14:45 UTC show slow webhook processing for `lk-shopify-tiny-stock-sync` only.
- Slow local response examples:
  - 13:37:58 POST → response ready 13:49:27, 689.1s.
  - 13:39:21 POST → response ready 13:51:36, 386.6s.
  - 13:41:29 POST → response ready 13:55:07, 597.3s.
  - 14:33:20 POST → response ready 14:56:07, 1324.2s.
  - 14:40/14:44/14:46/14:49 POSTs → responses ~344–560s.
- The route `lk-shopify-tiny-stock-sync` is configured in `webhook_subscriptions.json` as `kind: lk_shopify_tiny_stock_sync_dryrun` with `script` present but without `run_script: true`; therefore Hermes executes the generic/agent path instead of deterministic script mode.
- The target script `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py` currently has a CLI main that returns `webhook_only_dry_run` when no `--sample-file` is supplied; if switched to script mode it needs stdin/env adapter support first.

## Root-cause hypothesis
Most likely root cause: Vercel proxy waits synchronously for the upstream Hermes Gateway response. During Shopify webhook bursts, at least one route (`lk-shopify-tiny-stock-sync`) fell into LLM/agent processing and took 300–1324s. This exceeds Vercel's 300s serverless runtime limit and can also saturate/queue the upstream webhook path, causing Vercel 504s across multiple Shopify webhook routes in the same burst.

This is not currently a DNS/health outage: health endpoints pass and 504 count was 0 in the last 30m during triage.

## Recommended scoped fix
Approval-gated because it changes production webhook behavior and likely requires gateway reload/restart:
1. Backup `/opt/data/webhook_subscriptions.json` and `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`.
2. Add stdin/env webhook adapter to `lk_shopify_tiny_stock_sync_dryrun.py` so it can process raw JSON from Hermes script mode using `HERMES_WEBHOOK_EVENT_TYPE` and `HERMES_WEBHOOK_DELIVERY_ID`.
3. Change only route `lk-shopify-tiny-stock-sync` to deterministic `run_script: true`, `kind: script`, `script_timeout: 30–60` while preserving secret and events.
4. Run local script tests/py_compile and a signed no-op probe; verify response <30s and `write_executed=false`.
5. Restart/reload only the required webhook runtime if necessary; no Vercel deploy unless proxy timeout behavior is also changed.
6. Optional hardening after this: deploy Vercel proxy timeout guard (`AbortSignal` < 300s + controlled 202/502) so Vercel does not hang for 300s on upstream saturation.

## Safety
- External writes during triage: 0.
- Messages sent: 0.
- Secrets printed: 0.
- values_printed=false.
