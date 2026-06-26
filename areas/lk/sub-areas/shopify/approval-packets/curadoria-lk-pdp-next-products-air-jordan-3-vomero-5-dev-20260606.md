# Approval Packet — Curadoria LK PDP — Next products DEV batch — 2026-06-06

## Status

Prepared read-only. No Shopify write executed in this step.

## Context

Lucas asked to continue adding Curadoria LK / `Outras variações` to more products after the typography hotfix was merged to Production.

Per workflow, this step is read-only and stops at a DEV approval packet. A DEV/unpublished theme upload still requires explicit approval.

## Current DEV baseline

- Theme DEV: `155065450718`
- Active asset inspected: `snippets/lk-variante-top30-visited-v2.liquid`
- Product catalog scan: `2331` products
- Covered handles detected in DEV snippet: `950`
- Existing Curadoria groups detected: `60`
- Prior DEV-only expansion already included in baseline: Adidas Tokyo Mary Jane expansion.

## Proposed next safe DEV batch

Add two new static Curadoria groups to the DEV theme:

1. `top30-air-jordan-3-regular-special`
2. `top30-nike-zoom-vomero-5-regular-special`

Total new products getting a Curadoria block: `8` handles.

Why these first:

- Both clusters are currently uncovered in DEV scan.
- Each has `4/4` public-valid PDPs checked.
- Same silhouette/model grouping is clean enough for a small batch.
- All candidates passed public HTML, public `.js`, and CDN image checks.
- No Production write is included in this approval.

## Group 1 — Air Jordan 3

Marker proposal: `top30-air-jordan-3-regular-special`

Products:

1. `tenis-nike-air-jordan-3-og-rare-air-preto`
   - Label: `Rare Air`
   - Title: `Tênis Nike Air Jordan 3 OG Rare Air Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-air-jordan-3-retro-black-cat-preto`
   - Label: `Black Cat`
   - Title: `Tênis Nike Air Jordan 3 Retro Black Cat Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-air-jordan-3-retro-x-j-balvin-rio-preto`
   - Label: `J Balvin Rio`
   - Title: `Tênis Nike Air Jordan 3 Retro x J Balvin "Rio" Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

4. `tenis-air-jordan-3-retro-x-wnba-desert-camo-bege`
   - Label: `WNBA Camo`
   - Title: `Tênis Nike Air Jordan 3 Retro x WNBA Desert Camo Bege`
   - HTML: 200
   - JS: 200
   - Image: 200

## Group 2 — Nike Zoom Vomero 5

Marker proposal: `top30-nike-zoom-vomero-5-regular-special`

Products:

1. `tenis-nike-air-zoom-vomero-5-doernbecher-2023-laranja`
   - Label: `Doernbecher`
   - Title: `Tênis Nike Air Zoom Vomero 5 Doernbecher 2023 Laranja`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-nike-zoom-vomero-5-metallic-silver-blue-tint-prateado-azul`
   - Label: `Silver Blue`
   - Title: `Tênis Nike Zoom Vomero 5 Metallic Silver & Blue Tint Prateado/Azul`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta`
   - Label: `Platinum Violet`
   - Title: `Tênis Nike Zoom Vomero 5 Metallic Silver Platinum Violet Prateado/Violeta`
   - HTML: 200
   - JS: 200
   - Image: 200

4. `tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza`
   - Label: `Photon Dust`
   - Title: `Tênis Nike Zoom Vomero 5 Photon Dust Metallic Silver Cinza`
   - HTML: 200
   - JS: 200
   - Image: 200

## Caveats

- Each group has only 4 public-valid items today. On a current PDP, this means up to 3 alternative cards render after excluding the current product, not 5.
- Group names include `regular-special` because both groups mix regular and special/collab executions; there are not enough public-valid clean regular-only items to split them safely now.
- On Running Cloudtilt was not selected because one candidate returned `.js` 429 during validation and the group mixes regular Cloudtilt with Loewe variants.
- Adidas Superstar / ASICS Kayano 14 / Air Max 95 / NB 550 are valid but only 3 items each; they are better as a later smaller batch unless Lucas wants breadth over density.

## Risk

Low/medium:

- DEV write would touch only `snippets/lk-variante-top30-visited-v2.liquid` in unpublished theme `155065450718`.
- Static group patch must preserve all existing Curadoria blocks and the current DEV Adidas Tokyo Mary Jane expansion.
- Public preview can be affected by Shopify preview/caching behavior; readback/static QA is required after write.

## QA plan if DEV approved

1. Backup DEV asset before write.
2. Apply scoped patch only to `snippets/lk-variante-top30-visited-v2.liquid`.
3. Read back DEV asset until markers appear exactly once:
   - `top30-air-jordan-3-regular-special`
   - `top30-nike-zoom-vomero-5-regular-special`
4. Static QA:
   - handles/labels/images/titles counts aligned per group;
   - duplicate handles: 0;
   - malformed image URLs: 0;
   - current product excluded from cards.
5. Public DEV preview QA on at least one PDP per group.
6. Record receipt in Brain.

## Rollback plan

Restore the pre-write DEV backup of `snippets/lk-variante-top30-visited-v2.liquid`.

## Requested approval

To apply this to DEV only, Lucas should approve explicitly:

`Aprovo DEV Curadoria Air Jordan 3 + Vomero 5`
