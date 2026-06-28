# CLI/MCP active cron fix — 2026-06-27

## Status

- status: done
- scope: active cron paths with raw API gaps after CLI-first audit
- values_printed: false
- external writes during fix: 0
- Telegram/WhatsApp/email sends: 0
- runtime/gateway/Docker/VPS restarts: 0

## Policy applied

1. CLI official / Hermes Doppler-first wrapper first.
2. MCP second when CLI/wrapper is not the better governed surface.
3. Raw API/HTTP only as documented exception; no active recurring cron path should depend on raw external API when a CLI/wrapper path exists.

## Changes

### 1. LK Stock OS Supabase read-model sync hourly

File: `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py`

Changed from:

- raw Hub lookup via `urllib.request`;
- raw Supabase PostgREST upsert/delete via `urllib.request`;
- recurring external DB write path.

Changed to:

- CLI-first Supabase readback gate using `hermes-cli-run supabase db query --linked`;
- no raw Hub/PostgREST path;
- no Supabase write in this cron gate;
- silent-OK when Supabase read model is present, count-consistent and guardrails are zero.

Readback evidence:

- snapshots_total: 1
- run_id: `20260626T092006Z`
- source: `Stock OS DB`
- total_count: 12592
- result_count: 12592
- items: 12592
- public availability sums: 0
- transport: `hermes_cli_run_supabase_db_query_linked`

### 2. LK Shopify Sales OS nightly full reconcile read-only

Files:

- `/opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/scripts/shopify_sales_os.py`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/scripts/shopify_sales_analytics_enrich.py`
- new wrapper: `/opt/data/scripts/shopify_admin_graphql_cli.py`
- symlink: `/opt/data/home/.local/bin/shopify-admin-graphql`

Changed from:

- raw Shopify Admin GraphQL via `urllib.request` inside active cron path.

Changed to:

- `hermes-cli-run shopify-admin-graphql` wrapper surface;
- Doppler/profile env injection; no token printing;
- mutations blocked by default;
- recurrent scripts no longer import/call `urllib`, `requests`, or `httpx`.

Note: official Shopify CLI `shopify store execute` exists, but read-only smoke showed no stored app authentication for `lk-sneakerss.myshopify.com` in this runtime. The Hermes CLI wrapper is therefore the governed CLI fallback for cron/runtime until Shopify CLI store auth is explicitly configured.

### 3. LK Stock agent rule corrected

Updated the LK Stock local skill and Brain AGENTS wording from Supabase-MCP-primary wording to the global policy:

- CLI/wrapper first;
- MCP second;
- raw API only exception.

## Verification

| Gate | Result |
|---|---:|
| `py_compile` touched Python files | OK |
| Supabase cron dry-run/readback | OK |
| Supabase cron silent run | exit 0, stdout 0, stderr 0 |
| Shopify wrapper smoke | OK |
| Nightly latest-order readback via wrapper | OK |
| Sales OS helper `shopify_graphql` via wrapper | OK |
| Analytics helper `shopify_graphql` via wrapper | OK |
| Cron JSON registries | 11/11 OK |
| Enabled external raw API gaps | 0 |
| Local loopback CLI callback exceptions | 1 (`wacli --webhook http://127.0.0.1:8787/wacli`) |
| Brain health | All checks passed |
| `git diff --check` | OK |

## Notes

- The remaining loopback URL is not an external raw API integration. It is the local callback URL required as an argument to the `wacli` CLI sync process.
- No full nightly Shopify reconcile was forced during this fix to avoid a heavy live backfill run; targeted read-only GraphQL paths were verified through the new wrapper.

## Backup

Backup directory:

`/opt/data/backups/cli-mcp-active-cron-fix-20260627T132053Z`
