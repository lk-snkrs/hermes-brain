---
title: LK Recovery OS Postgres/PostgREST fallback deployed
created_at_utc: 2026-06-03T00:20:00Z
area: lk/atendimento
system: lk-recovery-os
status: active_fallback
owner: lk-ops
---

# LK Recovery OS — Postgres/PostgREST fallback

## Summary

Lucas approved option B: self-host a minimal Postgres + PostgREST fallback on the Hostinger VPS instead of installing full Supabase.

Goal: restore durable persistence for LK Recovery OS after managed Supabase REST/Auth returned repeated HTTP 522/timeouts and prevented checkout backfill.

## Production endpoints

- Recovery Worker: `https://recovery.lucascimino.com`
- Fallback DB REST: `https://recovery-db.lucascimino.com/rest/v1`
- Fallback DB health: `https://recovery-db.lucascimino.com/healthz`
- VPS: `72.60.150.124`
- VPS path: `/opt/lk-recovery-db`

`lkskrs.online` DNS/API was not usable from this runtime due Hostinger/Cloudflare API blocking and Cloudflare token not owning that zone. The fallback hostname was therefore created under the Cloudflare-owned `lucascimino.com` zone.

## Stack deployed

Path on VPS: `/opt/lk-recovery-db`

Containers:

- `lk-recovery-db-postgres` — `postgres:16-alpine`
- `lk-recovery-db-postgrest` — `postgrest/postgrest:v12.2.8`
- `lk-recovery-db-rest-proxy` — `nginx:1.27-alpine`

Routing:

- Cloudflare DNS `recovery-db.lucascimino.com` -> `72.60.150.124`, proxied.
- Traefik route host: `recovery-db.lucascimino.com`.
- Nginx maps `/rest/v1/*` to PostgREST so existing Supabase-style clients work.

## Secrets and safety

Generated new local fallback credentials:

- Postgres password
- PostgREST JWT secret
- PostgREST `service_role` JWT

Secrets were not printed in chat/receipts.

Cloudflare Worker `lk-recovery` secrets updated:

- `SUPABASE_LK_URL` -> `https://recovery-db.lucascimino.com`
- `SUPABASE_LK_SERVICE_KEY` -> fallback `service_role` JWT
- `SHOPIFY_WEBHOOK_SECRET` was re-uploaded from Doppler after smoke HMAC failed with the previous Worker value.

Doppler remains the source of truth for business secrets. The fallback credential cache is currently local under the Hermes secret area for operational continuity and should be migrated/recorded in Doppler if long-term use continues.

Customer-facing sends remain disabled:

```text
LK_RECOVERY_DRY_RUN=true
LK_CHATWOOT_INTERNAL_ONLY=true
LK_LIVE_SEND_ENABLED=false
LK_WHATSAPP_SEND_ENABLED=false
LK_EMAIL_SEND_ENABLED=false
```

## Schema created

Core tables provisioned:

- `raw_events`
- `checkouts`
- `audit_log`
- `identity_clusters`
- `identity_links`
- `identity_events`
- `suppression_list`
- `recovery_candidates`
- `recovery_sequences`
- `recovery_messages`
- `cart_recovery_links`
- `provider_callbacks`
- `recovery_cooldowns`

Grants:

- `web_anon`: read-only
- `service_role`: read/write/delete on public tables and sequences

## Backfill result

Shopify checkout backfill executed against fallback DB.

Result:

```json
{
  "fetched": 31,
  "eligible": 31,
  "skipped_completed": 0,
  "skipped_closed": 0,
  "skipped_no_recovery_url": 0,
  "written": 31,
  "errors": 0
}
```

Validation:

- `raw_events` where `source='shopify_checkouts_backfill'`: `31`
- `checkouts`: `31`
- smoke rows removed after validation; `smoke_checkouts`: `0`

## Worker smoke test

Initial fake Shopify webhook failed with `invalid_hmac`, revealing divergence between the Worker `SHOPIFY_WEBHOOK_SECRET` and Doppler's `SHOPIFY_WEBHOOK_SECRET`.

Action:

- Re-uploaded Worker `SHOPIFY_WEBHOOK_SECRET` from Doppler.

Then smoke webhook returned:

```json
{
  "accepted": true,
  "source": "checkouts/create",
  "checkout_id": "gid://shopify/Checkout/999000111222336",
  "event_id": "shopify_checkout_started:gid://shopify/Checkout/999000111222336:2026-06-03T00:30:00Z"
}
```

HTTP status: `202`.

The smoke checkout was confirmed in fallback DB and then removed to keep data clean.

## Backup

Daily backup configured on VPS:

- Script: `/opt/lk-recovery-db/backup.sh`
- Cron: `/etc/cron.d/lk-recovery-db-backup`
- Schedule: `03:17 UTC` daily
- Output dir: `/opt/lk-recovery-db/backups`
- Format: compressed custom `pg_dump` (`.dump.gz`) + SHA256 file
- Retention: 14 days

Manual backup test succeeded:

- Example file: `/opt/lk-recovery-db/backups/lk_recovery_20260603T001604Z.dump.gz`

## Rollback

To stop fallback writes from Worker:

1. Restore previous managed Supabase values into Worker secrets:
   - `SUPABASE_LK_URL`
   - `SUPABASE_LK_SERVICE_KEY`
2. Deploy or let Worker secret update propagate.
3. Keep fallback running read-only until data is reconciled/exported.

To stop fallback stack:

```bash
cd /opt/lk-recovery-db
docker compose down
```

Do not delete volume until export/reconciliation is complete:

```text
lk-recovery-db_lk_recovery_pgdata
```

## Remaining recommendations

- Move fallback credentials into Doppler if this fallback remains active beyond incident recovery.
- Decide whether managed Supabase should be recovered and reconciled from fallback via export/import.
- Add a lightweight operational monitor for `https://recovery-db.lucascimino.com/healthz` and backup freshness.
- Optionally create `recovery-db.lkskrs.online` once Hostinger DNS API/manual hPanel is available.
