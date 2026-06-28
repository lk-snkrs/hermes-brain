# Shopify official OAuth — 2026-06-27

## Status

- status: done
- store: `lk-sneakerss.myshopify.com`
- method: official `shopify store auth`
- scopes: `read_orders`, `read_products`
- values_printed: false
- Shopify writes/mutations: 0

## Verification

| Gate | Result |
|---|---:|
| OAuth callback | HTTP 200 |
| `shopify store auth list --json` | 1 session |
| Official `shopify store execute` read-only query | OK |
| Store readback | `lk-sneakerss.myshopify.com` |
| Config file mode | `0600` |

## Notes

- The official Shopify CLI now has stored store auth for LK Sneakers on this runtime.
- The token value was not printed in chat, logs, report, or receipt.
- Existing Hermes Doppler-first wrapper remains available as a governed fallback for cron/runtime.
