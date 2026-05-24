# LK WhatsApp / Crisp Inbox — hybrid payload confirmed

Date UTC: 2026-05-20T11:53:38Z

## Context

Internal Lucas-only test for LK abandoned-checkout WhatsApp automation via Crisp Template API / n8n route.

## Confirmed by Lucas

- WhatsApp delivery: confirmed — message arrived on Lucas's WhatsApp.
- Crisp Inbox visibility: confirmed — message appeared in Crisp Inbox.

## Payload behavior confirmed

Hybrid Crisp options:

```json
{
  "crisp_options": {
    "as": "text",
    "type": "text",
    "new_session": false
  },
  "BODY": {
    "text": "<unique marker>"
  }
}
```

## Test identifiers

- Unique marker: `INBOX114811`
- Request ID: `cf9d38a4-7099-4706-bada-88f7590216f9`
- Template: `lk_checkout_abandonado_30min_v2`
- Media: none / text template
- Crisp result: HTTP 200 / `request_accepted`

## Decision

For LK text-template sends where both WhatsApp delivery and Crisp Inbox logging are required, the current confirmed route is the hybrid payload retaining legacy `as:text` while adding documented text semantics.

Do not treat media/image header variants as confirmed for production until separately tested and visually verified in both WhatsApp and Crisp Inbox.

## Rollback / caution

- Workflow should remain inactive until Lucas explicitly approves activation.
- If future edits remove `as:text`, re-test delivery and Inbox visibility before rollout.
- Do not expose Crisp/Meta/n8n tokens in receipts or reports.
