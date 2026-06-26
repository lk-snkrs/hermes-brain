---
title: LK Recovery OS Superpowers read-only audit — capture and persistence
created_at_utc: 2026-06-03T00:51:00Z
area: lk/atendimento
system: lk-recovery-os
mode: read_only
criterion: capture_and_persist_abandoned_checkouts_safely_without_customer_messages
status: operational_with_live-event-caveat
---

# LK Recovery OS Superpowers read-only audit

## User-selected success criterion

Lucas selected option 1:

> Capturar e persistir carrinhos abandonados com segurança, sem enviar mensagens.

This audit intentionally does **not** evaluate revenue recovery or customer sends.

## Mental model verified

Expected flow:

```text
Shopify checkout lifecycle event
→ Shopify webhook
→ Cloudflare Worker `https://recovery.lucascimino.com`
→ Shopify HMAC validation
→ normalized raw event + checkout row
→ Postgres/PostgREST fallback at `https://recovery-db.lucascimino.com/rest/v1`
→ KV buffer if DB persistence fails
→ customer-facing sends remain disabled
```

## Evidence collected

### Shopify webhooks

Shopify has 17 total webhooks. Recovery OS lifecycle webhooks present:

- `checkouts/create`: ID `1641293316318`, `https://recovery.lucascimino.com/shopify/checkouts/create`
- `checkouts/update`: ID `1648382181598`, `https://recovery.lucascimino.com/shopify/checkouts/update`
- `orders/create`: ID `1648382247134`, `https://recovery.lucascimino.com/shopify/orders/create`

Legacy lifecycle webhook left untouched:

- `orders/create`: ID `1643681644766`, `https://lucascimino.com/webhook/shopify`

### Shopify checkouts

Shopify REST Admin, rolling 72h:

- total checkouts returned: 16
- open/uncompleted checkouts: 16
- all 16 have recovery URL

### DB fallback consistency

Fallback DB checkouts:

- `checkouts_total`: 31
- first `last_seen_at`: `2026-05-27 00:14:04+00`
- latest `last_seen_at`: `2026-06-02 21:46:05+00`
- open by `completed_at IS NULL`: 31
- with recovery URL: 31

Exact set comparison:

- Shopify open checkouts in rolling 72h: 16
- Missing in DB: 0
- DB has 15 additional checkouts outside the rolling Shopify 72h query window.

### Raw events by checkout/order source

Current checkout lifecycle raw-event evidence:

- `checkout_started` / `shopify_checkouts_backfill`: 31
- latest occurred_at: `2026-06-02 21:46:05+00`
- latest received_at: `2026-06-03 00:10:41.262555+00`

Important caveat:

- No real Shopify webhook-created checkout event is visible yet in `raw_events`; current checkout rows are from the controlled backfill.
- This means configuration + persistence are verified and all current open Shopify rows are persisted, but live production webhook capture remains awaiting the next real checkout lifecycle event.

### Worker / DB health

- `https://recovery.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery","status":"ok"}`
- `https://recovery-db.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery-db","status":"ok"}`

### KV buffer

`CHECKOUT_BUFFER_KV` returned empty array:

```text
[]
```

No checkout events are stuck in the buffer.

### Worker secrets presence

Wrangler listed expected secret names including:

- `SHOPIFY_WEBHOOK_SECRET`
- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_STORE_URL`
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`

No secret values were recorded.

### Safety flags

From `wrangler.toml`:

- `LK_RECOVERY_DRY_RUN=true`
- `LK_RECOVERY_PAUSE=false`
- `LK_SUPPORT_PROVIDER=chatwoot`
- `LK_CHATWOOT_INTERNAL_ONLY=true`
- `LK_LIVE_SEND_ENABLED=false`
- `LK_WHATSAPP_SEND_ENABLED=false`
- `LK_EMAIL_SEND_ENABLED=false`
- `LK_SCORING_ENABLED=true`

Interpretation: capture/persistence/scoring may operate, but customer-facing sends remain blocked.

## Verdict

For Lucas's selected criterion — capture and persist abandoned carts safely, without sending messages — current state is:

```text
Operational for current known abandoned checkouts.
Configured for live lifecycle capture.
No customer sends enabled.
Live webhook capture awaits next real Shopify event for final proof.
```

Classification:

```text
A-/B+: OK for capture/persistence state, with live-event caveat.
```

Why not full A:

- Current checkout persistence evidence is from backfill, not from a new real Shopify webhook after lifecycle webhooks were completed.
- The next real checkout/update/order event should produce the final live proof.

## Recommended next read-only step

Monitor the next real Shopify checkout lifecycle event and verify that `raw_events.source`/`event_type` reflects webhook ingestion, not only backfill.

Do not enable customer-facing sends until Lucas separately approves Chatwoot/WhatsApp template, opt-in/cooldown and live-send flags.
