---
title: LK Recovery OS checkout buffer and Shopify backfill hardening
created_at_utc: 2026-06-02T23:45:00Z
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
pr: 24
status: deployed_buffer_backfill_pending_supabase
---

# LK Recovery OS checkout buffer and Shopify backfill hardening

## Context

Lucas approved fixing abandoned checkout capture without moving immediately to a self-hosted Supabase on Hostinger. The safe route chosen was:

1. Protect new Shopify checkout webhooks with a durable Cloudflare KV buffer when Supabase/PostgREST is unavailable.
2. Add a dry-run-first backfill script for Shopify open checkouts.
3. Keep customer-facing sends disabled.

## Delivered

PR #24 merged:

- `fix: buffer checkout webhooks during Supabase outages (#24)`
- merge commit: `af6c55d9259214f12cf21ee0df5f9bcb444b2652`

Worker deployed:

- Worker: `lk-recovery`
- route: `https://recovery.lucascimino.com`
- version id: `c9925b69-253a-4cb3-9991-94f78295a0a6`
- schedule: `*/10 * * * *`

Cloudflare KV namespace created/bound:

- title: `lk_recovery_checkout_buffer`
- binding: `CHECKOUT_BUFFER_KV`
- id: `09053375df944f61ad1f05e05201f238`

## Behavior now

For Shopify checkout webhooks:

```text
Shopify checkouts/create
→ Worker validates/normalizes
→ tries Supabase persistence
→ if Supabase fails, writes event to CHECKOUT_BUFFER_KV
→ existing */10 cron drains buffered events
→ KV item is deleted only after successful Supabase replay
```

This protects new checkout events from being lost while Supabase is timing out.

## Backfill status

Script added:

```text
scripts/lk_recovery_os_shopify_checkout_backfill.py
```

Dry-run live result:

```json
{
  "fetched": 31,
  "eligible": 31,
  "skipped_completed": 0,
  "skipped_closed": 0,
  "skipped_no_recovery_url": 0,
  "written": 0,
  "errors": 0
}
```

Real execution attempted but blocked by Supabase:

```text
Supabase REST POST raw_events timed out after 4 attempts
method=POST
path=raw_events
retryable=true
exit_code=75
```

Therefore historical backfill remains pending until Supabase REST/PostgREST accepts writes again.

## Validation

Local QA before PR:

```text
uv run pytest -q -> 161 passed, 1 warning
uv run ruff check . -> All checks passed
npm test -> 48 passed
npx tsc --noEmit -> passed
git diff --check -> passed
```

GitHub Actions for PR #24:

```text
CI success
```

Post-deploy checks:

```text
https://recovery.lucascimino.com/healthz -> HTTP 200
CHECKOUT_BUFFER_KV list -> success true, key_count 0
```

## Safety

- No Shopify webhook writes were made in this change.
- No customer-facing WhatsApp/e-mail/Chatwoot send was enabled.
- `LK_RECOVERY_DRY_RUN=true`, `LK_CHATWOOT_INTERNAL_ONLY=true`, `LK_LIVE_SEND_ENABLED=false`, `LK_WHATSAPP_SEND_ENABLED=false`, `LK_EMAIL_SEND_ENABLED=false` remain active.
- Secrets were fetched through Doppler/API process env and not printed.

## Remaining action

When Supabase recovers, run:

```bash
uv run python scripts/lk_recovery_os_shopify_checkout_backfill.py --days 7 --limit 50 --execute
```

Then verify `raw_events`, `checkouts`, and `audit_log`.
