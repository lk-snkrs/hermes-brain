---
title: LK Recovery OS next live event monitor and verification runbook
created_at_utc: 2026-06-03T00:56:00Z
area: lk/atendimento
system: lk-recovery-os
mode: read_only_monitor
criterion: capture_and_persist_abandoned_checkouts_safely_without_customer_messages
status: awaiting_next_real_shopify_lifecycle_event
---

# LK Recovery OS — next live event monitor and verification runbook

## Scope

Lucas requested options 1 and 2 after the Superpowers audit:

1. Monitor read-only now for a few cycles.
2. Create a report/runbook for verifying the next real checkout event.

No writes were made to Shopify, Worker, DB, KV, Chatwoot or messaging systems.

## Current success criterion

The active criterion is:

```text
Capturar e persistir carrinhos abandonados com segurança, sem enviar mensagens.
```

This means the audit is successful when a Shopify checkout lifecycle event is observed as persisted in Recovery OS storage while customer-facing sends remain disabled.

## Monitor window

- Started: `2026-06-03T00:53:17Z`
- Finished: `2026-06-03T00:55:34Z`
- Cycles: 5
- Interval: ~30 seconds
- Mode: read-only

## Monitor evidence

Baseline at start:

- Shopify open checkouts in rolling 12h: `2`
- DB checkouts total: `31`

Across all 5 cycles:

- Shopify open checkouts in rolling 12h: stayed `2`
- New Shopify checkout since monitor start: `0`
- DB checkouts total: stayed `31`
- New DB checkout since monitor start: `0`
- Shopify open checkouts missing in DB: `0`
- `CHECKOUT_BUFFER_KV`: `0` keys / empty array
- `recovery_messages_total`: `0`

Recent Shopify lifecycle raw events in DB remained:

```text
checkout_started | shopify_checkouts_backfill | 31 | latest_received 2026-06-03 00:10:41.262555+00
```

## Interpretation

During the short monitor window, no new real Shopify checkout lifecycle event occurred.

The result is still healthy for the chosen criterion because:

- all current rolling-12h open Shopify checkouts were already persisted in DB;
- no Shopify open checkout was missing from DB;
- KV buffer was empty;
- no customer-facing recovery message was generated.

But final proof of **live webhook capture after lifecycle webhook completion** still requires the next real checkout lifecycle event.

## Exact proof needed for next real event

The next real Shopify checkout event is proven captured/persisted if all of these are true:

1. Shopify REST shows a new open checkout ID not present in the prior baseline.
2. Fallback DB `checkouts` contains the same checkout ID.
3. Fallback DB `raw_events` contains a recent lifecycle row for that checkout/event, ideally from webhook source rather than backfill.
4. `CHECKOUT_BUFFER_KV` is empty, or contains the event only temporarily and later drains.
5. `recovery_messages` remains unchanged at `0` unless Lucas separately approves internal/customer messaging scope.
6. Safety flags remain:
   - `LK_RECOVERY_DRY_RUN=true`
   - `LK_CHATWOOT_INTERNAL_ONLY=true`
   - `LK_LIVE_SEND_ENABLED=false`
   - `LK_WHATSAPP_SEND_ENABLED=false`
   - `LK_EMAIL_SEND_ENABLED=false`

## Read-only command pattern

### Shopify checkouts

Query rolling recent Shopify Admin REST checkouts and collect open IDs:

```text
GET /admin/api/2024-04/checkouts.json?status=any&created_at_min=<UTC_ISO>&limit=250
```

Open/uncompleted filter:

```text
completed_at IS NULL and closed_at IS NULL
```

Normalize to:

```text
gid://shopify/Checkout/<numeric_id>
```

### DB checks

On VPS `72.60.150.124`, path `/opt/lk-recovery-db`:

```sql
SELECT checkout_id, last_seen_at, completed_at IS NOT NULL AS completed,
       recovery_url IS NOT NULL AS has_recovery_url
FROM checkouts
ORDER BY last_seen_at DESC NULLS LAST
LIMIT 20;

SELECT event_type, source, count(*) n, max(received_at) latest_received
FROM raw_events
WHERE received_at > now() - interval '2 hours'
  AND (source ILIKE '%shopify%' OR event_type ILIKE '%checkout%' OR event_type ILIKE '%order%')
GROUP BY event_type, source
ORDER BY latest_received DESC NULLS LAST;

SELECT count(*) FROM recovery_messages;
```

### KV check

Using Wrangler from `/opt/data/lk-recovery-os/workers/recovery-os`:

```text
wrangler kv key list --binding CHECKOUT_BUFFER_KV
```

Expected steady state:

```text
[]
```

## Current verdict after monitor

```text
Operational for known/current abandoned checkouts.
No missing recent Shopify open checkout in DB.
No buffer backlog.
No customer sends.
Awaiting next real Shopify lifecycle event for live-webhook proof.
```

## Recommended next step

Run this monitor again during business/high-traffic window or while Lucas manually creates a real test checkout without completing payment. The manual real checkout is the cleanest proof of Shopify → webhook → Worker → DB without enabling messaging.
