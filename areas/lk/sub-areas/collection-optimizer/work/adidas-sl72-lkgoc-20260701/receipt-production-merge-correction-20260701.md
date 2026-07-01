# Receipt — Production merge correction Adidas SL 72 duplicate editorial

UTC: 2026-07-01T17:09:32Z
Profile: lk-collection-optimizer / LKGOC

## Approval
Lucas requested: "Fazer o merge de correção" after confirming duplicate editorial blocks.

## Scope
- Store: lk-sneakerss.myshopify.com
- Collection: `/collections/adidas-sl-72` / gid://shopify/Collection/437668380894
- Write performed: Shopify Admin GraphQL `collectionUpdate(descriptionHtml)` via official Shopify CLI broker.
- No stock/Tiny/product/price/checkout/GMC/Klaviyo changes.

## Problem
Public collection had duplicate editorial blocks from previous competing theme/collection paths:
- old `LK_ADIDAS_SL72` / `coll-rich-content` content;
- `lk-guia-adidas-sl72-serp` block.

## Correction
Replaced collection `descriptionHtml` with a single LKGOC editorial payload:
- intro for banner;
- one post-grid guide: `Adidas SL 72: OG, RS, conforto e história`;
- OG vs RS comparison;
- styling/color guidance;
- single FAQ set;
- anti-inference note for size/stock/price/prazo;
- link to `/pages/adidas-sl-72-og-vs-rs-guia-lk`.

## Evidence
- Admin readback after mutation: collection updated at 2026-07-01T17:08:25Z, userErrors=[].
- Public readback with `sort_by=manual` showed:
  - `LK_ADIDAS_SL72`: 0
  - `lk-guia-adidas-sl72-serp`: 0
  - `Adidas SL 72 original no Brasil`: 0
  - `Abrir Guia Adidas SL 72 OG vs RS`: 1
  - `Liquid error`: 0
- Root URL may show short Shopify/CDN cache delay; cache-busted sorted URL showed corrected payload.

## Workdir
/opt/data/work/lkgoc-adidas-sl72-production-merge-20260701T170818Z

## Status
DONE_WITH_CACHE_PROPAGATION_NOTE
