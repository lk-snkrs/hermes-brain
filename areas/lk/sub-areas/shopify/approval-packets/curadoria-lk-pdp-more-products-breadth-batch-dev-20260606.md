# Approval Packet — Curadoria LK PDP — More products breadth batch — DEV — 2026-06-06

## Status

Prepared read-only. No Shopify/theme write executed in this step.

## Context

Lucas said: `Seguir em mais produtos` after the Air Jordan 3 + Vomero 5 Production merge.

Per LK Shopify guardrails and Curadoria workflow, this means continue autonomously with read-only candidate preparation and stop at a DEV approval packet. This does **not** authorize a DEV upload or Production merge.

## Current baseline inspected

- DEV theme: `155065450718`
- Production theme: `155065417950`
- Active asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Catalog products scanned: `2331`
- DEV covered handles detected: `587`
- Production covered handles detected: `583`
- Current marker count detected in both DEV/Production readbacks: `34`
- Read-only scan output: `/opt/data/tmp/lk_curadoria_more_products_readonly_20260606.json`

## Recommendation

Proceed with a breadth-first DEV batch of **4 small but clean groups**:

1. Adidas Superstar special/collab — 3 products
2. ASICS Gel-Kayano 14 special/collab — 3 products
3. Nike Air Max 95 x Levi's — 3 products
4. New Balance 550 regular/special — 3 products

Total new products covered in DEV: `12` handles.

Why these first:

- All candidates are currently uncovered in DEV and Production readbacks.
- All passed current public validation:
  - PDP HTML: `200`
  - `/products/<handle>.js`: `200`
  - CDN image: `200`
- Semantic grouping is cleaner than the mixed On Cloudtilt option.
- Each group is small, but adds broad coverage without mixing unrelated silhouettes.

## Caveat — small rails

Each proposed group has only `3` products today. Since the current PDP is excluded, the rail will show up to **2 alternative cards** on each PDP.

If Lucas wants denser rails, we should wait for groups with 5–6+ public-valid siblings. If Lucas wants more PDP coverage now, this batch is safe as breadth-first.

## Proposed group 1 — Adidas Superstar special/collab

Marker proposal: `top30-adidas-superstar-special`

Products:

1. `tenis-adidas-superstar-x-clot-chinese-new-year-preto`
   - Label: `CLOT CNY`
   - Title: `Tênis adidas Superstar x CLOT Chinese New Year Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-adidas-superstar-x-korn-30th-anniversary-preto`
   - Label: `Korn 30th`
   - Title: `Tênis adidas Superstar x Korn 30th Anniversary Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-adidas-superstar-x-wales-bonner-croc-wonder-white-branco`
   - Label: `Wales Bonner`
   - Title: `Tênis Adidas Superstar x Wales Bonner Croc Wonder White Branco`
   - HTML: 200
   - JS: 200
   - Image: 200

## Proposed group 2 — ASICS Gel-Kayano 14 special/collab

Marker proposal: `top30-asics-gel-kayano-14-special`

Products:

1. `tenis-asics-gel-kayano-14-x-senna-black-gold-preto`
   - Label: `Senna Black Gold`
   - Title: `Tênis Asics Gel-Kayano 14 x Senna Black Gold Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-asics-gel-kayano-14-x-senna-white-red-branco`
   - Label: `Senna White Red`
   - Title: `Tênis Asics Gel-Kayano 14 x Senna White Red Branco`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-asics-marvel-vs-capcom-x-kith-x-asics-gel-kayano-14-ryu-branco`
   - Label: `Kith Ryu`
   - Title: `Tênis ASICS Marvel vs. Bonécom x Kith x ASICS Gel Kayano 14 Ryu Branco`
   - HTML: 200
   - JS: 200
   - Image: 200

## Proposed group 3 — Nike Air Max 95 x Levi's

Marker proposal: `top30-nike-air-max-95-levis`

Products:

1. `tenis-levis-x-nike-air-max-95-og-black-anthracite-denim`
   - Label: `Black Denim`
   - Title: `Tênis Levi's x Nike Air Max 95 OG Black Anthracite Denim Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-levis-x-nike-air-max-95-og-light-orewood-brown-denim`
   - Label: `Orewood Denim`
   - Title: `Tênis Levi's x Nike Air Max 95 OG Light Orewood Brown Denim Branco`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-levis-x-nike-air-max-95-og-obsidian-denim-casual`
   - Label: `Obsidian Denim`
   - Title: `Tênis Levi's x Nike Air Max 95 OG Obsidian Denim Azul`
   - HTML: 200
   - JS: 200
   - Image: 200

## Proposed group 4 — New Balance 550 regular/special

Marker proposal: `top30-new-balance-550-regular-special`

Products:

1. `tenis-new-balance-550-sashiko-pack-pecan-marrom`
   - Label: `Sashiko Pecan`
   - Title: `Tênis New Balance 550 Sashiko Pack Pecan Marrom`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `new-balance-550-white-pine-green`
   - Label: `Pine Green`
   - Title: `Tênis New Balance 550 White Pine Green Branco/Verde`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-new-balance-550-x-aime-leon-dore-brown-marrom`
   - Label: `ALD Brown`
   - Title: `Tênis New Balance 550 x Aimé Leon Dore Brown Marrom`
   - HTML: 200
   - JS: 200
   - Image: 200

## Deferred option — On Cloudtilt

Read-only scan found 3 public-valid Cloudtilt candidates, but I recommend deferring for now because the set mixes regular Cloudtilt with Loewe variants:

- `tenis-on-running-cloudtilt-preto-e-branco`
- `tenis-on-running-cloudtilt-loewe-denim-blue-azul`
- `tenis-on-running-cloudtilt-loewe-denim-grey-cinza`

Safer future options:

- Create a separate `Cloudtilt Loewe` group if more Loewe siblings exist/pass.
- Or explicitly approve a mixed `Cloudtilt regular/special` group.

## Risk

Low/medium:

- DEV write would touch only `snippets/lk-variante-top30-visited-v2.liquid` in unpublished theme `155065450718`.
- Small rails may look sparse because each group has only 3 products.
- Static blocks must preserve all existing Curadoria groups and current CSS light typography behavior.

## QA plan if DEV approved

1. Backup DEV asset before write.
2. Apply scoped patch only to `snippets/lk-variante-top30-visited-v2.liquid`.
3. Read back DEV asset until all markers appear exactly once:
   - `top30-adidas-superstar-special`
   - `top30-asics-gel-kayano-14-special`
   - `top30-nike-air-max-95-levis`
   - `top30-new-balance-550-regular-special`
4. Static QA:
   - handles/labels/images/titles counts aligned per group;
   - duplicate handles: 0;
   - malformed image URLs: 0;
   - current product excluded from cards;
   - existing markers preserved.
5. Public DEV preview QA on at least one PDP per group.
6. Typography QA on visible block title and product labels:
   - `.lk-variante__title`: `font-weight: 300`
   - `.lk-variante__label`: `font-weight: 300`
   - `.lk-variante__label::after`: `font-weight: 300` or `content: none`
7. Record receipt in Brain.

## Rollback plan

Restore the pre-write DEV backup of `snippets/lk-variante-top30-visited-v2.liquid`.

## Requested approval

To apply this to DEV only, Lucas should approve explicitly:

`Aprovo DEV Curadoria breadth Adidas Superstar + ASICS Kayano 14 + Air Max 95 + NB550`
