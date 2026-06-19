# Approval Packet — LK GMC Shopify-first P1 Category + Identifier — 2026-06-18

Status: `PREVIEW_ONLY_NO_WRITE`.

## Decision requested

Approve or adjust the first Shopify-first correction packet for GMC product-data completeness.

This packet does **not** execute writes. It prepares the exact candidate list for review.

## Governance

- Source of truth for product data: Shopify.
- Mapping/submission layer: Simprosys.
- Readback/diagnostic: GMC.
- No direct GMC patch by default.
- No price, stock, availability, or customer-facing discount changes in this packet.
- Any execution requires explicit approval of scope and rollback.

## Scope prepared

Full active Shopify read-only crawl found:

- Active products: 1,838.
- Active variants: 13,347.
- Products with category empty/`Uncategorized`: 348.
- Products missing `mm-google-shopping.identifier_exists`: 112.

P1 preview candidate set:

- Total products in packet: 432.
- Category issue products: 348.
- Identifier_exists issue products: 112.
- Products with both issues: 28.
- Category suggestions with high-confidence rule: 320.
- Category requiring manual review: 28.
- `identifier_exists = no` suggestions: 111.
- Identifier mixed-GTIN manual review: 1.

## Proposed rules

### Category normalization

Only for products currently empty or `Uncategorized`.

Suggested mappings are rule-based from product_type/title/handle:

- sneakers/tênis terms → `Apparel & Accessories > Shoes > Sneakers`.
- camiseta/t-shirt → `Apparel & Accessories > Clothing > Clothing Tops > T-Shirts`.
- moletom/hoodie → `Apparel & Accessories > Clothing > Activewear > Activewear Sweatshirts & Hoodies`.
- boné/cap → `Apparel & Accessories > Clothing Accessories > Hats > Baseball Caps`.
- calça/pants → `Apparel & Accessories > Clothing > Pants`.
- shorts → `Apparel & Accessories > Clothing > Shorts`.
- bolsa/bag → `Apparel & Accessories > Handbags, Wallets & Cases > Handbags`.
- óculos/sunglasses → `Apparel & Accessories > Clothing Accessories > Sunglasses`.
- top → `Apparel & Accessories > Clothing > Activewear > Activewear Tops`.
- saia/skirt → `Apparel & Accessories > Clothing > Skirts`.

Rows marked `NEEDS_MANUAL_REVIEW` should not be auto-applied.

### Identifier policy

For products missing `mm-google-shopping.identifier_exists`:

- if all variants lack barcode/GTIN in Shopify, proposed value: `no`;
- if mixed barcode presence, proposed value: `manual_review_mixed_gtin`.

Important: this does not invent GTINs. If a real barcode/GTIN exists externally, it should be filled in Shopify variant barcode instead of forcing `identifier_exists=no`.

## First 20 candidates preview

- #1 `tenis-asics-gel-1130-black-pure-silver-prata` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #2 `tenis-asics-gel-1130-black-pure-silver-prata-1` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #3 `tenis-asics-gel-1130-white-black-silver-prata` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #4 `tenis-asics-gel-1130-white-black-silver-prata-1` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #5 `tenis-asics-gel-1130-white-clay-canyon-branco` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #6 `tenis-asics-gel-1130-white-pure-silver-prata` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #7 `tenis-asics-gel-nyc-graphite-grey-black-preto` — ASICS — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #8 `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco` — Air Jordan — Sneakers — category: `Uncategorized` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #9 `tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #10 `tenis-jordan-11-retro-low-university-blue-2026-azul` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #11 `tenis-jordan-4-retro-lakers-roxo` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #12 `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #13 `tenis-jordan-4-retro-toro-bravo-2026-vermelho-1` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #14 `tenis-jordan-5-retro-white-metallic-2026-metalizado` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #15 `tenis-jordan-5-retro-wolf-grey-2026-cinza` — Jordan — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #16 `tenis-new-balance-990v6-made-in-usa-cinza-castlerock` — New Balance — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #17 `tenis-nike-air-force-1-low-protro-kobe-bryant-siempre-hermanos-marrom` — Nike — Tênis — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #18 `tenis-nike-craft-general-purpose-shoe-tom-sachs` — Nike — Sneakers — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #19 `tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur` — Nike — Sneakers — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`
- #20 `tenis-nike-craft-general-purpose-shoe-tom-sachs-field-brown-marrom` — Nike — Sneakers — category: `<empty>` → `Apparel & Accessories > Shoes > Sneakers`; identifier_exists: `<empty>` → `no`

## Files

- CSV full preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/lk-gmc-shopify-p1-category-identifier-preview-2026-06-18.csv`
- Summary JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/lk-gmc-shopify-p1-category-identifier-preview-2026-06-18.summary.json`

## Rollback plan for execution phase

Before any write:

1. Export old values for every target product/metafield.
2. Save rollback JSON/CSV with product ID, field, old value, proposed new value.
3. Execute in a small pilot first, recommended 20–50 products.
4. Validate Shopify readback.
5. Trigger/wait Simprosys sync if applicable.
6. Validate GMC readback after processing.

Rollback:

- restore saved old Shopify category/metafield values via Admin API;
- re-read Shopify;
- wait Simprosys/GMC sync;
- confirm issue counts do not regress.

## Recommended approval unit

Approve a **pilot only**, not all 432 at once:

- P1A: first 50 high-confidence rows from this CSV.
- Exclude `NEEDS_MANUAL_REVIEW` rows.
- Exclude `manual_review_mixed_gtin` rows.
- No price/stock/availability writes.

Suggested approval phrase:

> Aprovo executar P1A Shopify-first nos primeiros 50 itens high-confidence do packet, excluindo manual review, apenas categoria Shopify e `mm-google-shopping.identifier_exists`, com rollback e readback.
