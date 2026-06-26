---
title: LK Recovery OS abandoned checkout corrected diagnosis
created_at_utc: 2026-06-02T23:14:30Z
area: lk/atendimento
status: shopify_has_open_checkouts_supabase_unverifiable
---

# LK Recovery OS abandoned checkout corrected diagnosis

Lucas challenged the previous conclusion that there were no abandoned carts. Rechecked with broader Shopify sources.

## Corrected evidence

Shopify Admin REST `checkouts.json`, read-only, last 7 days:

- returned 31 checkouts.
- sample rows had `completed_at = null` and `closed_at = null`.
- examples included created_at from 2026-05-26 through 2026-06-01, values around R$ 1,199.99 to R$ 2,799.99+.
- Most sample rows had email contact available.

Shopify webhook subscriptions:

- Recovery OS has exactly one relevant webhook:
  - topic: `checkouts/create`
  - address: `https://recovery.lucascimino.com/shopify/checkouts/create`
  - created_at: 2026-05-24T08:17:45-03:00
- No Recovery OS webhook was found for `checkouts/update` or `orders/create`; those routes exist in Worker code but are not currently registered in Shopify.

Worker health:

- `https://recovery.lucascimino.com/healthz` returned HTTP 200 repeatedly.

Cloudflare Worker analytics, last 24h:

- script `lk-recovery` has traffic:
  - success: 26,101 requests
  - clientDisconnected: 20,277 requests
  - exceededResources: 135 requests/errors
- Not endpoint-specific; evidence of runtime traffic, not proof of specific checkout persistence.

Supabase:

- `raw_events`, `checkouts`, and `audit_log` still time out on read-only REST queries.
- Therefore Recovery OS DB persistence cannot be verified now.

## Corrected conclusion

Previous answer was too narrow because GraphQL `abandonedCheckouts` was not enough. Shopify REST shows open/non-completed checkout rows; there are abandoned/open checkout candidates.

Operationally:

- Shopify has abandoned/open checkout candidates: yes.
- Recovery OS ingress is configured for `checkouts/create`: yes.
- Worker is online and receiving traffic: yes.
- Recovery OS DB capture/persistence: not verifiable while Supabase times out.
- Risk: Worker responds 202 before async `persistCheckoutEvent`; if Supabase fails during `ctx.waitUntil`, Shopify may consider the webhook accepted while DB persistence failed.

## Recommended fixes

1. Restore Supabase availability and backfill from Shopify `checkouts.json` for the affected window.
2. Add durable fallback/buffer (Cloudflare Queue/KV/Durable Object) before Supabase writes.
3. Consider registering Recovery OS webhooks for `checkouts/update` and `orders/create` after approval, because Worker routes exist but Shopify currently only points `checkouts/create` at Recovery OS.
