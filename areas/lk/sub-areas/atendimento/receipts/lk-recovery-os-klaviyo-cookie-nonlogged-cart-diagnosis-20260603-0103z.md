---
title: LK Recovery OS Klaviyo cookie diagnosis for non-logged abandoned carts
created_at_utc: 2026-06-03T01:03:00Z
area: lk/atendimento
system: lk-recovery-os
mode: local_patch_predeploy
status: awaiting_deploy_approval
---

# LK Recovery OS — Klaviyo cookie for non-logged abandoned carts

## Lucas direction

Lucas clarified the goal:

> Capturar pessoas que têm carrinho abandonado mas não estão logadas utilizando o cookie do Klaviyo.

Customer-facing sends remain out of scope unless separately approved.

## Operational idea

For non-logged visitors, Shopify checkout/webhook often lacks customer identity. The Recovery OS must therefore rely on the storefront beacon:

```text
Browser/theme JS
→ reads Klaviyo cookie `__kla_id`
→ sends it to `/events/storefront`
→ Worker decodes cookie / resolves Klaviyo profile
→ stores hashed email/phone/profile links in identity graph
→ stitches cart_token/session/anonymous_id to identity
→ later checkout/cart intent can be captured even when Shopify customer is null
```

## Evidence inspected

### Backend already has the intended architecture

Worker has:

- `POST /events/storefront`
- `extractKlaviyoSignals()` in `src/klaviyo.ts`
- `decodeKlaviyoCookie()` for base64/url/plain JSON `__kla_id`
- `klaviyoGetProfile()` lookup by Klaviyo profile ID
- identity graph linking via `identity_links.key_type='klaviyo_profile_id'`
- scoring/candidate flow downstream

### Production traffic exists

Fallback DB, last 24h storefront events:

- `storefront_24h`: 1502
- `klaviyo_mentions_24h`: 1502
- `kla_cookie_mentions_24h`: 1502
- `email_hash_24h`: 3
- `phone_hash_24h`: 0
- `cart_token_24h`: 401

Live theme sends Klaviyo cookie fields:

- `identity_hints.kla_cookie`: 1267 events in 24h
- `identity_hints.__kla_id`: 1267 events in 24h
- `identity_hints.klaviyo_kx`: 12 events in 24h
- `identity_hints.klaviyo_profile_id`: 0 events in 24h

Identity graph already has historical Klaviyo links:

- `identity_links.key_type='klaviyo_profile_id'`: 249

### Bug found

The live Shopify theme sends the cookie under:

```text
payload.identity_hints.kla_cookie
payload.identity_hints.__kla_id
```

But Worker `extractKlaviyoSignals()` only decoded:

```text
payload.klaviyo_kla_id
payload.kla_cookie
payload.identities.klaviyo.kla_cookie
```

It did **not** read `payload.identity_hints.kla_cookie`.

Effect: production events contained the Klaviyo cookie, but the Worker often failed to decode/use it for non-logged visitors.

## Local patch applied

Files changed locally:

- `workers/recovery-os/src/klaviyo.ts`
- `workers/recovery-os/tests/klaviyo.test.ts`

Patch behavior:

- `extractKlaviyoSignals()` now reads cookie/profile/kx/email/phone from `identity_hints` as well as top-level and `identities.klaviyo`.
- Added regression test for the exact live-theme shape: `identity_hints.kla_cookie` containing a base64 JSON Klaviyo cookie.

## Verification

RED:

- New test failed before patch:
  - expected profile ID `01JPROFILE`
  - received `null`

GREEN:

- Specific test passed:
  - `tests/klaviyo.test.ts`: 1/1 passed

Full Worker suite:

```text
Test Files: 8 passed
Tests: 49 passed
```

## Current status

```text
Local code is fixed and tested.
Production is not deployed yet.
No external writes performed.
Customer-facing sends remain disabled.
```

## Approval packet for deploy

Proposed external action if Lucas approves:

1. Deploy Cloudflare Worker `recovery-os` with the local Klaviyo extraction fix.
2. Keep all safety flags unchanged:
   - `LK_RECOVERY_DRY_RUN=true`
   - `LK_CHATWOOT_INTERNAL_ONLY=true`
   - `LK_LIVE_SEND_ENABLED=false`
   - `LK_WHATSAPP_SEND_ENABLED=false`
   - `LK_EMAIL_SEND_ENABLED=false`
3. Monitor next 10–30 minutes of storefront events:
   - increased `identity_links.key_type='klaviyo_profile_id'`
   - increased `email_hash`/possibly `phone_hash` on storefront events where Klaviyo profile resolves
   - no increase in `recovery_messages`
4. Do not change Shopify theme unless post-deploy evidence shows the current theme cookie payload is insufficient.

## Risk

Low technical risk: parser reads more shapes from already received payload. Main production risk is deploy operation itself, not customer messaging. No live send flags need to change.
