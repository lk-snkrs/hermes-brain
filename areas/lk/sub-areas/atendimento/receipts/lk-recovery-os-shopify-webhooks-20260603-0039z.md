---
title: LK Recovery OS Shopify lifecycle webhooks completed
created_at_utc: 2026-06-03T00:39:00Z
area: lk/atendimento
system: lk-recovery-os
status: completed
approval_surface: Lucas Telegram "Seguir" after audit recommendation
---

# LK Recovery OS — Shopify lifecycle webhooks completed

## Scope

Approved small packet executed after audit identified that Recovery OS had only `checkouts/create` subscribed in Shopify.

Created only the missing Recovery OS Shopify webhook subscriptions:

- `checkouts/update` -> `https://recovery.lucascimino.com/shopify/checkouts/update`
- `orders/create` -> `https://recovery.lucascimino.com/shopify/orders/create`

No customer-facing sends were enabled.

## Pre-read

Shopify read-only audit before write:

- Recovery OS already had:
  - `checkouts/create` -> `https://recovery.lucascimino.com/shopify/checkouts/create`
- No Recovery OS subscription existed for:
  - `checkouts/update`
  - `orders/create`
- A legacy/non-Recovery `orders/create` webhook existed at `https://lucascimino.com/webhook/shopify`; it was left untouched.

## Created webhooks

### checkouts/update

- Shopify webhook ID: `1648382181598`
- topic: `checkouts/update`
- address: `https://recovery.lucascimino.com/shopify/checkouts/update`
- format: `json`
- created_at: `2026-06-02T21:38:34-03:00`

### orders/create

- Shopify webhook ID: `1648382247134`
- topic: `orders/create`
- address: `https://recovery.lucascimino.com/shopify/orders/create`
- format: `json`
- created_at: `2026-06-02T21:38:35-03:00`

## Post-read verification

Shopify now has exactly 3 Recovery OS webhooks for the intended lifecycle topics:

- `checkouts/create`: ID `1641293316318`, `https://recovery.lucascimino.com/shopify/checkouts/create`
- `checkouts/update`: ID `1648382181598`, `https://recovery.lucascimino.com/shopify/checkouts/update`
- `orders/create`: ID `1648382247134`, `https://recovery.lucascimino.com/shopify/orders/create`

## Health verification

At `2026-06-03T00:39:01Z`:

- `https://recovery.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery","status":"ok"}`
- `https://recovery-db.lucascimino.com/healthz`: HTTP 200, `{"service":"lk-recovery-db","status":"ok"}`
- `CHECKOUT_BUFFER_KV`: empty array `[]`

Fallback DB quick counts after creation:

- `raw_events_total`: 1534
- `checkouts_total`: 31
- `recovery_messages`: 0
- `pending_candidates`: 9

## Safety flags still disabled

From `wrangler.toml`:

- `LK_RECOVERY_DRY_RUN=true`
- `LK_RECOVERY_PAUSE=false`
- `LK_SUPPORT_PROVIDER=chatwoot`
- `LK_CHATWOOT_INTERNAL_ONLY=true`
- `LK_LIVE_SEND_ENABLED=false`
- `LK_WHATSAPP_SEND_ENABLED=false`
- `LK_EMAIL_SEND_ENABLED=false`

Interpretation: lifecycle capture/persistence is enabled; customer-facing sends remain blocked.

## Rollback

If these subscriptions need to be removed, delete only these Shopify webhook IDs:

- `1648382181598` (`checkouts/update`, Recovery OS)
- `1648382247134` (`orders/create`, Recovery OS)

Do not delete existing `checkouts/create` ID `1641293316318` unless explicitly rolling back all Recovery OS webhook ingress.

Do not touch legacy `orders/create` webhook at `https://lucascimino.com/webhook/shopify` unless separately approved.

## Remaining note

Next real Shopify lifecycle event should validate production path naturally. Customer-facing recovery is still intentionally off until Lucas approves Chatwoot/WhatsApp template, opt-in/cooldown and send enablement.
