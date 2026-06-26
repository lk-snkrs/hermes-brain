---
title: LK Recovery OS audit after PostgREST fallback
generated_at_utc: 2026-06-03T00:24:00Z
area: lk/atendimento
system: lk-recovery-os
status: mostly_ok_with_webhook_gap
---

# LK Recovery OS audit — 2026-06-03 00:24Z

## Verdict

Recovery OS is operational for capture/persistence and historical checkout recovery, but not yet fully complete for all desired Shopify lifecycle events.

Current state:

- Worker ingress: OK.
- Fallback Postgres/PostgREST: OK.
- Backfill: 31/31 persisted.
- Current Shopify open checkouts in 7d: 30/30 represented in DB.
- KV checkout buffer: empty.
- Customer-facing sends: disabled.
- Backup: active and tested.
- Gap: Shopify only has `checkouts/create` webhook pointing to Recovery OS; `checkouts/update` and `orders/create` are not configured in Shopify based on read-only webhook audit.

## Evidence

### Health

- `https://recovery.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery","status":"ok"}`.
- `https://recovery-db.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery-db","status":"ok"}`.

### VPS / containers

VPS: `72.60.150.124`, host `lc`.

Containers:

- `lk-recovery-db-postgres`: up, healthy.
- `lk-recovery-db-postgrest`: up.
- `lk-recovery-db-rest-proxy`: up, `127.0.0.1:3030->8080`.

Capacity:

- Disk `/`: 387G total, 91G used, 296G free, 24% used.
- Memory: 31Gi total, 18Gi available.

### Backup

- Cron present: `/etc/cron.d/lk-recovery-db-backup`.
- Schedule: `17 3 * * *` UTC.
- Script: `/opt/lk-recovery-db/backup.sh`.
- Backup file exists: `/opt/lk-recovery-db/backups/lk_recovery_20260603T001604Z.dump.gz` plus SHA256 sidecar.

### DB counts

- `raw_events_total`: 1014.
- `raw_events_backfill`: 31.
- `raw_events_webhook`: 0.
- `checkouts_total`: 31.
- `open_checkouts_by_completed_null`: 31.
- `recovery_candidates`: 2, state `pending`.
- `recovery_messages`: 0.
- `audit_log`: 196.
- `smoke_rows`: 0.

Recent raw event freshness showed storefront/Klaviyo ingestion active around `2026-06-03 00:21Z`.

Recent checkout freshness:

- first `last_seen_at`: `2026-05-27 00:14:04+00`.
- latest `last_seen_at`: `2026-06-02 21:46:05+00`.

### Shopify read-only audit

Shopify webhooks total: 15.

Recovery OS webhook found:

- topic: `checkouts/create`.
- address: `https://recovery.lucascimino.com/shopify/checkouts/create`.
- created_at: `2026-05-24T08:17:45-03:00`.

No Recovery OS webhook was found for:

- `checkouts/update`.
- `orders/create`.

Shopify REST checkouts last 7 days:

- total checkouts returned: 30.
- open checkouts: 30.
- all open 7d checkout IDs are present in fallback DB.
- fallback DB has 1 additional checkout not in current 7d Shopify query: `gid://shopify/Checkout/39530128572638`, likely outside the exact rolling 7d window or no longer returned by that query.

### Cloudflare Worker / KV

Wrangler secret list succeeded with `CLOUDFLARE_API_TOKEN` and showed expected secret names, including:

- `SHOPIFY_WEBHOOK_SECRET`
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`
- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_STORE_URL`

`CHECKOUT_BUFFER_KV` key list returned empty array: no buffered checkout events pending.

Note: Cloudflare `/user/tokens/verify` returned 401 for some token candidates, but Wrangler operations succeeded with `CLOUDFLARE_API_TOKEN`; operational check should rely on Wrangler for this environment.

### Runtime safety flags

From `wrangler.toml`:

- `LK_RECOVERY_DRY_RUN=true`
- `LK_RECOVERY_PAUSE=false`
- `LK_SUPPORT_PROVIDER=chatwoot`
- `LK_CHATWOOT_INTERNAL_ONLY=true`
- `LK_LIVE_SEND_ENABLED=false`
- `LK_WHATSAPP_SEND_ENABLED=false`
- `LK_EMAIL_SEND_ENABLED=false`
- `LK_SCORING_ENABLED=true`

Interpretation: persistence/scoring can run, customer sends remain blocked.

### QA

Worker tests:

- 48 passed.

Repo Python QA:

- 161 passed.
- Ruff: all checks passed.
- `git diff --check`: passed as part of command.

## Risk / gaps

1. **Lifecycle webhook gap:** only `checkouts/create` is configured in Shopify. `checkouts/update` and `orders/create` routes exist in the Worker, but are not currently subscribed in Shopify. This means updates/completions may not be reflected unless reconciled/backfilled manually.
2. **No customer-facing recovery sends:** this is intentional/safe, but means the system is not actively recovering revenue via WhatsApp/e-mail yet.
3. **Fallback credentials long-term location:** fallback credentials are available operationally, but should be migrated/recorded in Doppler if this becomes permanent.
4. **Managed Supabase is still bypassed:** fallback is active. A reconciliation plan is needed if managed Supabase is restored and chosen as primary again.

## Recommended next actions

Approval packet needed before writes:

1. Create/validate missing Shopify webhooks:
   - `checkouts/update` -> `https://recovery.lucascimino.com/shopify/checkouts/update`
   - `orders/create` -> `https://recovery.lucascimino.com/shopify/orders/create`
2. Keep `dry_run`/internal-only until messaging templates, opt-in/cooldown and Chatwoot WhatsApp readiness are separately approved.
3. Move fallback DB secrets into Doppler as named secrets and document names only.
4. Add lightweight monitor for DB health and backup freshness.
