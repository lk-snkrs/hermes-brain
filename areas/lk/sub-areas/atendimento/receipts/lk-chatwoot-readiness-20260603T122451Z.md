---
title: LK Chatwoot readiness check
created_at_utc: 2026-06-03T12:24:51Z
area: lk/atendimento
status: partially_connected_internal_only
---

# LK Chatwoot readiness check

Read-only verification performed for Lucas after asking to continue Chatwoot configuration.

## Verified live state

Chatwoot public health:

- URL: https://chat.lkskrs.online/api
- HTTP: 200
- version: 4.14.1
- queue_services: ok
- data_services: ok

Chatwoot account API:

- account_id: 1
- account name: LK Sneakers
- token source: Doppler `CHATWOOT_LK_API_TOKEN` (value not recorded)

Operational structure:

- labels: 13
- includes: pedido, estoque, troca, devolucao, prazo, reclamacao, vip, financeiro, humano, whatsapp-api, carrinho-abandonado, shopify, recuperacao
- teams: 2
- `atendimento whatsapp`: id 2, allow_auto_assign false

Inboxes:

- count: 1
- inbox id 1: Shopify Carrinho Abandonado
- channel_type: Channel::Api
- no WhatsApp Cloud inbox verified yet

Webhooks:

- count: 1
- subscription: message_created
- destination: Elle receiver URL present (secret path redacted)

Integrations list:

- Shopify appears in integration apps list
- Webhooks appears in integration apps list

Elle receiver:

- URL: https://elle.lkskrs.online/healthz
- HTTP: 200
- ok: true
- dry_run: true
- write_enabled: false
- kill_switch: true

## Conclusion

Chatwoot is healthy and internally configured for LK. Elle receiver is online but intentionally blocked/safe. There is no verified live WhatsApp Cloud inbox yet, so the stack is not end-to-end WhatsApp-ready.

## Not changed

- No WhatsApp inbox was created.
- No external/customer-visible message was sent.
- No Chatwoot writes were performed.
- No Shopify/Tiny/WhatsApp/Meta production setting was changed.

## Next safe step

Prepare/execute WhatsApp Cloud inbox setup only after scoped approval and required Meta credentials: phone number, Phone Number ID, WABA ID, and access token. Until then, continue internal-only Chatwoot/Shopify recovery context.
