# Hermes Webhooks — custom domain correction and signed probes — 2026-06-07

## Scope

Lucas asked to correct the remaining Vercel Hermes Webhook items:

1. Custom domain `hermes-webhooks.lucascimino.com`.
2. Provider-signed end-to-end probes.

No secrets were printed or stored in this receipt.

## Custom domain correction

Before correction:

- Vercel project domains listed only `hermes-webhooks.vercel.app`.
- `hermes-webhooks.lucascimino.com` had Cloudflare DNS record:
  - type: `A`
  - target: Hostinger IP
  - proxied: `true`
  - comment indicated old Traefik/Hostinger ingress.
- Vercel domain config reported `misconfigured: true`.

Actions taken:

- Added `hermes-webhooks.lucascimino.com` to Vercel project `hermes-webhooks` under team scope `lk-snkrs-projects`.
- Updated Cloudflare DNS record to:
  - type: `CNAME`
  - target: Vercel recommended CNAME
  - proxied: `false` / DNS-only
  - TTL: Auto
- Rollback reference retained in Cloudflare record comment: previous A record target and proxied state.

Verification:

- Vercel domain config after update:
  - `configuredBy: CNAME`
  - `misconfigured: false`
  - `ipStatus: no-change`
- Public DoH resolvers returned CNAME to the Vercel DNS target.
- Direct Vercel-edge probe with SNI/Host `hermes-webhooks.lucascimino.com` returned `200 OK`, `Server: Vercel`, and `/health` JSON.

Note: the local system resolver still temporarily returned old Cloudflare proxied IPs during cache propagation, causing `403/1010` for ordinary local requests. Public DNS was already corrected.

## Signed provider probes

### Canonical Vercel URL

Tested `https://hermes-webhooks.vercel.app` with signed, safe payloads:

- Shopify route: `POST /webhooks/lk-shopify-pos-restock`
  - Valid Shopify HMAC over raw body.
  - Fake non-POS paid order payload, intentionally expected to be ignored.
  - Result: `200 OK`, `status: ignored`, `reason: not_paid_active_pos_order`, `sent_count: 0`, `queued_count: 0`.

- Evolution route: `POST /webhooks/lk-evolution-delivery-reconciliation`
  - Valid Evolution proxy secret.
  - Fake inbound/fromMe=false message update, intentionally expected not to update ledgers.
  - Result: `200 OK`, `status: reconciled`, `matched: 0`, `updated: 0`, `reason: not_outbound_from_me`.

### Custom domain via corrected Vercel edge

Because local resolver still cached old Cloudflare IPs, direct edge probes used the corrected Vercel IP with SNI/Host `hermes-webhooks.lucascimino.com`.

- Shopify signed probe: `200 OK`, `Server: Vercel`, same safe ignored result.
- Evolution signed probe: `200 OK`, `Server: Vercel`, same safe no-update result.

## GitHub assessment

A GitHub repository is not required for the webhook runtime to work. Vercel can run this project from CLI/source state as currently deployed.

It is operationally important if the project is treated as canonical infrastructure because GitHub provides:

- version history and diff review;
- rollback by commit;
- reproducible deployments;
- safer collaboration between agents;
- disaster recovery if `/opt/data/hermes-webhooks` or the Vercel project state drifts.

Recommendation: create or identify a canonical Git repository before the next functional change to the proxy. It is not a blocker for today’s corrected runtime.
