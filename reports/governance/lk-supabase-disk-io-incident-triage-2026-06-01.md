# LK Supabase Disk IO incident triage — 2026-06-01

## Context

Supabase project `cnjimxglpktznenpbail` (`LK Sneakers Db`) emitted a Disk IO Budget warning. The investigation was kept read-only and secret-safe.

## Read-only checks executed

- Supabase REST `/rest/v1/` OpenAPI probe: HTTP 522 / timeout.
- Lightweight REST `limit=1` probes against known LK tables (`orders`, `customers`, `order_items`, `customer_rfm`, `lk_crm_event_log`, `pos_whatsapp_log`, `product_announcements`): all timed out.
- Supabase Management `/database/query` with `SELECT 1`: timed out / Cloudflare 1010 depending on User-Agent.
- Direct DB via Supavisor pooler from stored `DATABASE_URL`: failed with `EAUTHQUERY authentication query failed: connection to database not available`.
- Direct DB via IPv4 hostaddr and stored LK Postgres password: same `EAUTHQUERY authentication query failed: connection to database not available`.
- n8n API read-only inventory: 46 workflows total, 8 active. Active LK workflows touching the LK Supabase REST API:
  - `q8ZU4s8H50m7tFnP` — `LK - Envio de Email Novo Produto`; webhook; POST `/rest/v1/product_announcements`.
  - `VLOygUcX6xbQYQif` — `LK POS → WhatsApp Thank You`; webhook; POST `/rest/v1/pos_whatsapp_log`.
  - `QNze6mFEVt27P1E4` — `GMC Health Check + Shopify Sync`; weekly cron; PostgreSQL insert into `gmc_health_snapshots`; scheduled Monday 02:00 UTC.
- Hermes cron audit: enabled script jobs in the default scheduler did not directly match LK Supabase patterns.
- 2026-06-01 LK 09h external report cron failed only at WhatsApp auth (`wacli hermes not authenticated`); not a Supabase cause.

## Assessment

The LK database is not merely slow; it is currently unreachable/unavailable from multiple independent paths. Because `SELECT 1` cannot complete, live SQL stats (`pg_stat_activity`, `pg_stat_statements`, table bloat, relation sizes) could not be collected from this environment.

Most likely operational state: Disk IO budget exhaustion/throttling or database health issue severe enough to block REST, pooler auth queries, and management query execution.

n8n read-only inventory found only small webhook log writers into LK Supabase plus a weekly GMC/Postgres insert. These may add pressure if retries loop, but the observed state is too degraded to prove root cause without Supabase Dashboard/Observability.

## Recommended next action

1. Open Supabase Dashboard → LK Sneakers Db → Observability / Database Health.
2. Check if the project is currently marked degraded/unresponsive and inspect Disk IO, CPU, wait events, active queries, and logs.
3. If the DB is still unavailable and business operations depend on it, approve one of:
   - temporary compute upgrade/restart from Supabase dashboard; or
   - targeted pause of LK n8n workflows that write to LK Supabase while the DB recovers.
4. After recovery, immediately run SQL read-only stats to identify root cause before any DDL/cleanup.

## Guardrails

No secrets printed. No n8n workflow paused. No Supabase write, restart, upgrade, index, cleanup, or destructive action executed.
