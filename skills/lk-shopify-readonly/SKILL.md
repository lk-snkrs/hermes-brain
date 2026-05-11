---
name: lk-shopify-readonly
description: Use when Lucas asks for LK Sneakers Shopify data, order/customer/product/catalog checks, or safe read-only Shopify analysis. Enforces Doppler-only secrets, GET/query-only access, Tiny-vs-Shopify stock boundaries, and approval rules before any Shopify write or customer-facing action.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [lk-sneakers, shopify, ecommerce, read-only, doppler, lucas-cimino]
    related_skills: [doppler-secrets-operations, multiempresa-routing-lucas, lucas-chief-of-staff, lk-market-trends, lk-shopify-product-upload]
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

## Approved exception pattern — SKU-only Shopify normalization

Use only when Lucas explicitly approves a Shopify SKU write, e.g. “pode alterar”, after a preview/backup exists.

1. Limit scope to variant-level SKU fields; do not change price, inventory, titles, handles, products, images, collections, campaigns, customers, or Tiny.
2. Build a backup plan per variant with: product title, handle, Shopify variant ID, size/variant title, old Shopify SKU, target Tiny `codigo`, Tiny product ID/name, and rollback SKU.
3. Only write variants where:
   - Tiny `codigo` is non-empty;
   - Shopify variant is found with high confidence by product + size and/or old SKU;
   - target is truly different from the current Shopify SKU.
4. Prefer Shopify REST for this narrow mutation: `PUT /admin/api/2024-01/variants/{numeric_variant_id}.json` with body `{ "variant": { "id": <id>, "sku": "<Tiny codigo>" } }`.
5. Verify each write immediately with `GET /admin/api/2024-01/variants/{id}.json` and compare live `sku` exactly to the Tiny `codigo`, including spaces/punctuation.
6. Write an audit report with success/failure counts, skipped reasons, and rollback data before telling Lucas it is complete.

Pitfall: GraphQL `productVariantUpdate` may return no useful `productVariant.sku` in this environment even when no `userErrors` are present; for SKU-only updates, REST `PUT /variants/{id}.json` gave verifiable `200` responses and exact live SKU verification.

Detailed session reference: `references/shopify-sku-normalization-to-tiny-20260511.md`.

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

## Operationalization reference

For the stricter standard Lucas expects before calling this skill “100% installed/operational”, load `references/shopify-skill-operationalization-20260511.md`. In short: verify the runtime skill, Hermes Brain copy, Brain indexes/MAPAs, health check, secret scan, PR merge/sync, and any relevant watchdog cron state before giving a final verdict.

For LK OS Stock Intelligence work where Lucas asks to resolve SKU/mapping before sourcing, load `references/lk-stock-sku-saneamento-20260511.md`. It captures the B→A workflow: resolve `sem SKU no Shopify` / `mapear SKU no Tiny` first, use Shopify GraphQL query + Tiny read-only fallback searches, then prepare Fila A preview without writes or supplier contact.

For the approved SKU-only exception where Lucas explicitly authorizes Shopify SKU writes to match Tiny, load `references/shopify-sku-normalization-to-tiny-20260511.md`. It captures the plan/backup, REST update, exact live verification, skipped-row logic, and rollback shape.

For catalog-wide SKU normalization, load `references/catalog-wide-shopify-sku-normalization-20260511.md`. It captures full Shopify/Tiny catalog comparison, high-confidence match rules, idempotent timeout resume, large-audit secret-scan false positives, and how to report “safe divergences fixed” without implying ambiguous rows were changed.

For the post-normalization residual queue, load `references/residual-fila-b-prioritization-20260511.md`. It captures how to classify skipped variants into residual buckets, prioritize P0/P1/P2/P3 manual review, and avoid jumping to sourcing before ambiguous/no-match SKU rows are resolved.

For the P0 follow-up after live Shopify/Tiny lookup, load `references/p0-residual-correction-queue-20260511.md`. It captures the rule that Tiny size/color matches without populated `codigo` are still not safe for automatic SKU-only writes; convert the findings into a human correction queue (MD/JSON/CSV) before any Fila A/sourcing.

For the P0 Tiny code correction preview, load `references/p0-tiny-code-correction-preview-20260511.md`. It captures how to separate candidate Tiny `codigo` writes with target codes from rows that still need Lucas/Júlio to define the canonical code.

For live P0 residual follow-up, load `references/lk-p0-residual-live-lookup-20260511.md`. It captures the Shopify GET + Tiny search/detail workflow, the requirement for a unique Tiny candidate with populated canonical `codigo`, and the rule that Tiny matches without code or ambiguous size/color matches cannot move to automatic SKU-only write or sourcing.

## Verification checklist

Before saying “100%” or “funciona”:

- [ ] I verified the relevant file/API/source, not only memory.
- [ ] If the claim is that the skill is installed/operational, I verified both the local skill path and any Hermes Brain copy/index entries that should exist.
- [ ] If the claim is about a merged Brain change, I verified health check, secret scan, PR/merge state and local sync to `origin/main`.
- [ ] Secrets were not printed, stored, or committed.
- [ ] Only GET/query operations were used.
- [ ] No customer-facing send was made.
- [ ] No Shopify write/admin/destructive action was made, **unless** Lucas explicitly approved a narrow SKU-only write and I created backup/rollback + live verification.
- [ ] If stock was involved, I did not treat Shopify stock as final truth.
- [ ] If reporting product availability, I used variant/size-level language.
- [ ] If data is live/business-critical, I stated source and timestamp.
- [ ] If I wrote code/docs, I ran syntax/health/secret checks appropriate to the change.

## Common pitfalls

0. **Product upload has its own skill.** If Lucas asks to `subir produto`, cadastrar produto, use GOAT photos/order, create product SKUs, or draft Shopify product descriptions, load `lk-shopify-product-upload`. Keep this read-only skill focused on catalog/sales/order validation unless a separately approved narrow write flow applies.

0. **Market Trends/WhatsApp intake belongs elsewhere.** If Lucas mentions LC WhatsApp `!subir`, hype, drops, sourcing trends, or “market trends”, load/use `lk-market-trends`; keep this Shopify skill focused on catalog/sales/order validation. Shopify can be a read-only validation source for Market Trends, but `!subir` is intake, not Shopify-write approval.

1. **Wrong token name.** Use `SHOPIFY_ACCESS_TOKEN`, not the historical mistaken `SHOPIFY_API_TOKEN` unless confirmed.
2. **Double `.myshopify.com`.** Some scripts expect `lk-sneakerss`; others expect `lk-sneakerss.myshopify.com`. Inspect the URL composition before calling.
3. **Skill ≠ automation.** Creating this skill does not create a cron or live sync. It only makes the safe procedure reusable.
4. **Shopify stock confusion.** Shopify stock is not LK stock truth; Tiny is.
5. **Platform attribution confusion.** Meta/Klaviyo platform signal is not the same as Shopify-confirmed revenue. Label ambiguity.
6. **PII over-sharing.** Do not put unnecessary customer personal data in Telegram, Brain, commits or reports.
7. **Silent success.** A script can return OK while inserting zero rows. Verify data freshness/counts when the task is about sync health.
8. **Jumping to Fila A before B.** For LK Stock Intelligence, Lucas wants B first: resolve `sem SKU no Shopify` and `mapear SKU no Tiny` before commercial sourcing/reposition previews.
9. **Tiny search false negatives.** Tiny SKU lookup may miss variants because Tiny stores spaces/punctuation differently (e.g. Shopify `1183C102751-3` vs Tiny `1183C102 751-3`) or variants have blank `codigo`. Retry with normalized/spaced SKU and product-title+size searches before declaring “not in Tiny”.
10. **Treating Tiny match as enough.** A Tiny size/color match with blank `codigo` or duplicate candidate IDs is not a safe write target. Produce a correction queue and require human/Tiny `codigo` confirmation before Shopify SKU-only preview or sourcing.
10. **Tiny candidate without `codigo` is not actionable.** In residual/P0 cleanup, a Tiny search or detail match that returns the right product/size but no canonical `codigo` still blocks automatic Shopify SKU writes and sourcing. Require a unique candidate with populated Tiny `codigo`, otherwise route to manual/Tiny canonical-code resolution first.
11. **P0 residual ≠ Fila A.** Even when a residual row overlaps sales/rupture, do a live read-only Shopify + Tiny detail lookup before commercial recommendations; no sourcing/reposition until SKU truth is confirmed.
