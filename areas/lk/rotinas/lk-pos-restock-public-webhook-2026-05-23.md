# LK POS Restock — Public Shopify Webhook Endpoint

Date: 2026-05-23

## Public endpoint

Use this URL in Shopify webhook settings:

```text
https://lk-recovery.lucascimino.com/webhooks/lk-shopify-pos-restock
```

Events:

- `orders/create`
- `orders/paid`

Content type: `application/json`

## Routing

Shopify calls `lk-recovery.lucascimino.com` (Vercel project `lk-recovery-os`).

`vercel.json` now has a first-match route:

```json
{
  "src": "/webhooks/lk-shopify-pos-restock",
  "dest": "https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-pos-restock"
}
```

That forwards to the Hermes webhook gateway route `lk-shopify-pos-restock` on the VPS.

## Verification

Verified after production deploy:

- `GET https://lk-recovery.lucascimino.com/healthz` → `200`, LK Recovery OS OK.
- `GET https://lk-recovery.lucascimino.com/webhooks/lk-shopify-pos-restock` → `405`, proving the route reaches Hermes webhook, which requires POST.
- signed safe `POST` with non-POS / unpaid payload → `200` with `status=ignored`, `reason=not_paid_active_pos_order`.

No real WhatsApp alert or Notion card was triggered during verification.

## Rollback

Remove the first route from `/opt/data/hermes_bruno_ingest/lk-recovery-os/vercel.json` and redeploy production.

DNS note: `crisp-hooks.lucascimino.com` A record was also created pointing to `72.60.150.124`, but the production Vercel route currently targets `crisp-hooks.srv1331756.hstgr.cloud`, which was already the active Traefik host for the Hermes webhook container.
