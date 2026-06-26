# Approval packet — DEV Curadoria LK PDP Nike Cortez + Puma Speedcat

Date: 2026-06-07

## Scope

Read-only packet for the next LK Thumbnail PDP / Curadoria LK batch after AJ1 layout and group-guard hotfixes.

No Shopify write executed in this packet.

## Safety gates for this next batch

To avoid repeating the AJ1 errors, the DEV apply must pass these gates before any report:

1. Use canonical Curadoria classes only:
   - `lk-variante__head`
   - `lk-variante__rail`
   - `lk-variante__media`
   - no `lk-variante__grid`
   - no `lk-variante__image-wrap`
2. If using a split snippet with more than one group, wrap every group section with current-product membership guard:
   - `{%- if lk_handles contains product.handle -%}`
3. Representative PDP QA per group:
   - current product excluded from cards;
   - exactly 1 expected `data-lk-variante` marker on that PDP;
   - wrong sibling marker absent;
   - `lk-variante.css` present;
   - `lk-variante__rail` present;
   - legacy grid classes absent.
4. Static QA:
   - markers count = 1;
   - handles/labels/images/titles aligned;
   - image URLs valid;
   - no placeholders;
   - no malformed URL patterns.
5. Stop at DEV/unpublished after approval; no Production merge without separate approval.

## Current read-only baseline

Catalog scan:

- Products scanned via Shopify Admin read-only: 2,331
- Covered handles parsed from current DEV/Production Curadoria assets: 694

Production active assets checked:

- `snippets/lk-variante-top30-visited-v2.liquid`
  - SHA: `c64dafba4777418ac7be08c0dafa6224d6fab8dafe3b0aa61029ba7b63f9da8d`
  - sections: 45
  - bad `lk-variante__grid`: 0
  - bad `lk-variante__image-wrap`: 0
  - render call: `lk-variante-aj1-low-high-20260606`
- `snippets/lk-variante-aj1-low-high-20260606.liquid`
  - SHA: `96d936e1a2dddd14f419f3388cb46e1454031bfd95183f9c0aa762bac90e7b7a`
  - sections: 2
  - group guards: 2
  - bad `lk-variante__grid`: 0
  - bad `lk-variante__image-wrap`: 0

DEV assets checked:

- `snippets/lk-variante-top30-visited-v2.liquid`
  - SHA: `e5df3582f2e9f5e17485deee2b8c9b29a055ca8da6b215c48b8c35d4c19a240e`
  - sections: 45
  - bad `lk-variante__grid`: 0
  - bad `lk-variante__image-wrap`: 0
- `snippets/lk-variante-aj1-low-high-20260606.liquid`
  - SHA: `96d936e1a2dddd14f419f3388cb46e1454031bfd95183f9c0aa762bac90e7b7a`
  - sections: 2
  - group guards: 2

## Recommended DEV batch

### 1. Nike Cortez

Marker proposal:

- `top30-nike-cortez-breadth`

Why:

- Clean model/silhouette cluster.
- 7 uncovered active/public products.
- 6/6 sampled products passed public HTML 200 + product `.js` 200 + image 200 in validation.
- Good density: after excluding current product, each PDP can render up to 5 alternatives.

Products:

- `tenis-nike-cortez-sl-white-gym-red-branco` — Tênis Nike Cortez SL White Gym Red Branco
- `tenis-nike-cortez-textile-beyond-pink-rosa` — Tênis Nike Cortez Textile Beyond Pink Rosa
- `tenis-nike-cortez-valentines-day-2025` — Tênis Nike Cortez Valentine's Day (2025) Off White
- `tenis-nike-cortez-valentines-day-branco` — Tênis Nike Cortez Valentine's Day Branco
- `tenis-nike-cortez-vintage-muslin-black-bege` — Tênis Nike Cortez Vintage Muslin Black Bege
- `tenis-nike-cortez-white-black-branco` — Tênis Nike Cortez White Black Branco
- `tenis-nike-cortez-white-laser-fuchsia-branco` — Tênis Nike Cortez White Laser Fuchsia Branco

Suggested short labels:

- White Gym Red
- Beyond Pink
- Valentine 2025
- Valentine Branco
- Vintage Muslin
- White Black
- Laser Fuchsia

### 2. Puma Speedcat

Marker proposal:

- `top30-puma-speedcat-breadth`

Why:

- Clean model/silhouette cluster.
- 5 uncovered active/public products.
- 5/5 products passed public HTML 200 + product `.js` 200 + image 200 in validation.
- Medium density: after excluding current product, each PDP renders 4 alternatives.

Products:

- `tenis-puma-speedcat-og-pele-yellow-black-amarelo` — Tênis Puma Speedcat OG Pelé Yellow Black Amarelo
- `tenis-puma-speedcat-og-pink-white-rosa` — Tênis Puma Speedcat OG Pink White Rosa
- `tenis-puma-speedcat-og-red-white-vermelho` — Tênis Puma Speedcat Og Red White Vermelho
- `tenis-puma-speedcat-og-team-royal-white-azul` — Tênis Puma Speedcat OG Team Royal White Azul
- `tenis-puma-speedcat-silk-chocotart-warm-white-marrom` — Tênis Puma Speedcat Silk Chocotart Warm White Marrom

Suggested short labels:

- Pelé Yellow
- Pink White
- Red White
- Team Royal
- Chocotart

## Deferred / not recommended in this batch

### Adidas Campus

Found 6 uncovered, but not clean enough for the next safe batch:

- includes kids/J sizing and collab capsules;
- Bad Bunny, Korn and Campus 00s should likely be separated, not mixed into one generic Campus rail.

Recommendation: defer and split later by capsule/adult/kids if needed.

### NB 550, Adidas Superstar, ASICS Gel-Kayano 14, Air Max 95, Yeezy Slide, Yeezy Foam Runner

Current scan found 0 uncovered with this simple coverage parser/ruleset. Not prioritized now.

## Approval needed for DEV write

If approved, exact next action should be DEV/unpublished only:

> Aprovo DEV Curadoria Cortez + Speedcat

That approval would authorize only:

- backup DEV asset(s);
- add these two groups to DEV/unpublished theme;
- readback polling;
- static QA;
- public/preview QA;
- receipt.

It would not authorize Production merge, product writes, price/stock, collections, ads, Klaviyo, GMC, or campaigns.

## Audit artifact

Raw audit JSON:

- `/opt/data/tmp/lk_curadoria_next_safe_audit_20260607.json`
