# Shopify webhook canonical URL fix — lk-shopify-tiny-stock-sync — 2026-06-25

## Status

Done.

## Scope approved

Lucas approved the Shopify Admin write to fix the signature issue for `lk-shopify-tiny-stock-sync`.

## Changed resources

Only the `address` field of these Shopify webhook subscriptions was updated:

| Shopify webhook ID | Topic | New address |
|---|---|---|
| `1646886125790` | `orders/paid` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` |
| `1646886158558` | `orders/cancelled` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` |

## Diagnosis

Previous URL:

```text
https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync
```

That endpoint reached Hermes directly. Shopify sends `X-Shopify-Hmac-Sha256`; Hermes direct dynamic route expects Hermes `X-Webhook-Signature`. The canonical Vercel proxy validates Shopify HMAC, preserves/normalizes payload headers, and re-signs to Hermes with the route secret.

## Verification

- Shopify Admin update HTTP code: `200` for both webhook IDs.
- Shopify Admin readback: both IDs now point to `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`.
- Public Shopify-HMAC no-op probe after update: `HTTP 202 accepted`.
- Gateway log monitor after update/probe: `invalid_signature_count=0` for `lk-shopify-tiny-stock-sync` over the monitored window.
- `values_printed=false`.

## Backup / rollback

Sanitized backup/readback artifacts:

```text
/opt/data/backups/shopify-webhook-canonical-url-fix-20260625T233346Z/before_sanitized.json
/opt/data/backups/shopify-webhook-canonical-url-fix-20260625T233346Z/after_readback_sanitized.json
```

Rollback would set the same two webhook IDs back to the old URL. Not recommended unless the canonical Vercel proxy becomes unavailable.

## Non-actions

- No product writes.
- No stock writes.
- No Tiny writes.
- No theme writes.
- No price/availability changes.
- No Klaviyo/message/email writes.
- No secrets printed or persisted.
