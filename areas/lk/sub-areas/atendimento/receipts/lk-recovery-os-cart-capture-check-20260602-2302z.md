---
title: LK Recovery OS cart capture check
created_at_utc: 2026-06-02T23:02:49Z
area: lk/atendimento
status: not_verifiable_no_shopify_abandoned_rows_supabase_timeout
---

# LK Recovery OS cart capture check

Question: "Algum carrinho abandonado está sendo capturado?"

## Checks performed

- Supabase read-only REST queries against `cnjimxglpktznenpbail.supabase.co`:
  - `raw_events`
  - `checkouts`
  - `audit_log`
- Result: all timed out (`TimeoutError: The read operation timed out`). Therefore captured rows cannot be verified from the operational DB at this time.

- Shopify Admin GraphQL read-only, store `lk-sneakerss.myshopify.com`:
  - webhook subscriptions: found `CHECKOUTS_CREATE` webhook pointing to `https://recovery.lucascimino.com/shopify/checkouts/create`, created 2026-05-24T11:17:45Z.
  - `abandonedCheckouts(first:10, reverse:true)`: returned an empty node list at check time.

## Conclusion

- Capture plumbing exists: Shopify has a checkout-create webhook configured to the Cloudflare Worker.
- Worker health had previously returned HTTP 200 on `https://recovery.lucascimino.com/healthz`.
- No current abandoned-checkout rows were visible in Shopify's abandonedCheckouts query at this check time.
- Supabase is not queryable, so there is no DB evidence available now that any cart was captured.

Operational answer: no verifiable abandoned cart capture is visible right now. The system is wired, but current capture cannot be confirmed until Supabase responds and/or Shopify returns abandoned checkout rows.
