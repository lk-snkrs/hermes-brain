---
name: lk-shopify-readonly
description: Use when Lucas asks for LK Sneakers Shopify data, order/customer/product/catalog checks, or safe read-only Shopify analysis. Enforces Doppler-only secrets, GET/query-only access, Tiny-vs-Shopify stock boundaries, and approval rules before any Shopify write or customer-facing action.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [lk-sneakers, shopify, ecommerce, read-only, doppler, lucas-cimino]
    related_skills: [doppler-secrets-operations, multiempresa-routing-lucas, lucas-chief-of-staff]
---

# LK Shopify Read-only

## Overview

Use this skill for LK Sneakers Shopify work that is safe, analytical, and read-only: checking orders, customers, products, variants, SKUs, tags, collections, source URLs, and CRM/sales signals.

This skill deliberately does **not** authorize Shopify writes. Any mutation, theme/app/admin change, customer communication, product/price/stock update, tag write, webhook change, campaign send, or destructive/admin action requires a plan, preview/rollback where applicable, and explicit Lucas approval.

## Source-of-truth rules for LK

- Shopify is the source for sales, customers, orders, product catalog/source context, tags, and part of CRM context.
- Tiny / `LK | CONTROLE ESTOQUE` is the stock truth.
- Shopify stock is not reliable enough to be treated as final stock truth.
- Availability must be variant/size-level when the user asks about produto/tamanho/SKU.
- `encomenda BR/US` status is human-curated in the Shopify order context; do not infer it blindly.
- External campaigns/messages use preview + Lucas approval before any Klaviyo, WhatsApp/Evolution, Shopify email/SMS, or customer-facing send.

## Secrets and environment

Secrets live in Doppler `lc-keys/prd`. Never print values.

Expected names:

- `SHOPIFY_STORE_URL`
- `SHOPIFY_ACCESS_TOKEN`

Known historical detail: older docs mention `SHOPIFY_ACCESS_TOKEN` as the correct token name, not `SHOPIFY_API_TOKEN`. If both exist, prefer `SHOPIFY_ACCESS_TOKEN` unless Lucas/Brain says otherwise.

Before live API work, check only existence, not values. Preferred helper if available:

```bash
/opt/data/hermes_bruno_ingest/hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN
```

If using Doppler directly, do not echo token values. Keep tokens in environment variables inside one shell/Python process.

## Safe read-only workflow

1. Route the task to LK, not Zipper or SPITI.
2. Identify the object and objective:
   - order(s), customer(s), product(s), variant/SKU, campaign/source, time window, collection, or tag.
3. Confirm that the requested action is read-only.
4. Confirm Doppler secret existence without printing values.
5. Use only Shopify Admin REST `GET` endpoints or Admin GraphQL `query` operations.
6. Start with a small limit/window and expand only if necessary.
7. Minimize PII in outputs. Prefer IDs, counts, SKU, status, dates, totals and aggregated patterns.
8. Cross-check with Tiny/Supabase/GA4/Meta/Klaviyo only when needed and label each source clearly.
9. Separate:
   - fact observed;
   - interpretation;
   - recommended action;
   - confidence/risk;
   - approval required.
10. If the user asks for an action that would write to Shopify or contact customers, stop at preview/plan and ask for explicit approval before executing.

## REST examples — read-only only

Use the correct shop host shape. If `SHOPIFY_STORE_URL` already includes `.myshopify.com`, do not append it again.

```bash
STORE="$(doppler secrets get SHOPIFY_STORE_URL -p lc-keys -c prd --plain)"
TOKEN="$(doppler secrets get SHOPIFY_ACCESS_TOKEN -p lc-keys -c prd --plain)"
curl -sS "https://${STORE}/admin/api/2024-01/orders.json?status=any&limit=5" \
  -H "X-Shopify-Access-Token: ${TOKEN}"
```

Product by SKU usually needs searching variants/products and then reading product details. Keep limits small first.

```bash
curl -sS "https://${STORE}/admin/api/2024-01/products.json?limit=5" \
  -H "X-Shopify-Access-Token: ${TOKEN}"
```

## GraphQL examples — query only

Allowed operation type: `query`.

Blocked operation type: `mutation`.

```graphql
query OrdersPreview($first: Int!) {
  orders(first: $first, reverse: true) {
    nodes {
      id
      name
      createdAt
      displayFinancialStatus
      displayFulfillmentStatus
      totalPriceSet { shopMoney { amount currencyCode } }
      tags
    }
  }
}
```

## Approval boundaries

Free within scope:

- Read orders/customers/products/variants/tags/collections with minimal PII.
- Produce analysis, reports, QA, anomaly checks and previews.
- Create Hermes Brain documentation, templates, checklists, and read-only scripts.

Requires Lucas approval before execution:

- Any Shopify mutation: tags, notes, customer fields, products, variants, price, stock, fulfillment, cancellation, refunds, discounts, theme, apps, webhooks, metafields, admin settings.
- Any customer-facing or team-facing external send via Shopify/Klaviyo/Evolution/WhatsApp/email/SMS.
- Any bulk export with personal data.
- Any database write, campaign edit, product/price/stock purchase decision, or automation enabling.

Requires plan + rollback + explicit approval:

- Admin/destructive operations: theme, checkout, domains, billing, app permissions, webhook creation/deletion, access tokens, production integrations.

## Output format for Lucas

Use Portuguese. Be direct.

Recommended format:

- Veredito curto.
- Fonte(s) consultada(s).
- O que encontrei.
- Risco/incerteza.
- Ação recomendada.
- O que não fiz: writes, envios, campanha, estoque/preço/tema/admin.
- Aprovação necessária, if any.

## Verification checklist

Before saying “100%” or “funciona”:

- [ ] I verified the relevant file/API/source, not only memory.
- [ ] Secrets were not printed, stored, or committed.
- [ ] Only GET/query operations were used.
- [ ] No customer-facing send was made.
- [ ] No Shopify write/admin/destructive action was made.
- [ ] If stock was involved, I did not treat Shopify stock as final truth.
- [ ] If reporting product availability, I used variant/size-level language.
- [ ] If data is live/business-critical, I stated source and timestamp.
- [ ] If I wrote code/docs, I ran syntax/health/secret checks appropriate to the change.

## Common pitfalls

1. **Wrong token name.** Use `SHOPIFY_ACCESS_TOKEN`, not the historical mistaken `SHOPIFY_API_TOKEN` unless confirmed.
2. **Double `.myshopify.com`.** Some scripts expect `lk-sneakerss`; others expect `lk-sneakerss.myshopify.com`. Inspect the URL composition before calling.
3. **Skill ≠ automation.** Creating this skill does not create a cron or live sync. It only makes the safe procedure reusable.
4. **Shopify stock confusion.** Shopify stock is not LK stock truth; Tiny is.
5. **Platform attribution confusion.** Meta/Klaviyo platform signal is not the same as Shopify-confirmed revenue. Label ambiguity.
6. **PII over-sharing.** Do not put unnecessary customer personal data in Telegram, Brain, commits or reports.
7. **Silent success.** A script can return OK while inserting zero rows. Verify data freshness/counts when the task is about sync health.
