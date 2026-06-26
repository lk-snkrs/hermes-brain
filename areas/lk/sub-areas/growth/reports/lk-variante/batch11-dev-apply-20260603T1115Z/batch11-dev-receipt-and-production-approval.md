# Curadoria LK — Batch 11 Dev receipt / Production approval packet

Timestamp UTC: 2026-06-03T11:12:56Z

## Scope approved by Lucas

Apply Batch 11 to Dev only, without touching Production, products, price, stock, apps, GMC, Tiny, Klaviyo, Meta or checkout.

## Important correction during execution

The initial read-only packet named Onitsuka Mexico 66 regular, Onitsuka Mexico 66 SD and New Balance 9060 as if they were fully new groups. During source inspection, current Production already had those group markers:

- `top30-mexico66-regular`
- `top30-mexico66-sd`
- `top30-nb-9060`

So the safe Batch 11 action was **not to duplicate groups**. Instead, I expanded the existing high-demand groups with additional active/available handles.

## Dev write executed

- Asset: `snippets/lk-variante-top30-visited.liquid`
- Dev theme: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Production theme: `155065417950` / `lk-new-theme/production` / role `main`

## Readback

- Dev before SHA12: `3ddbc92afb29`
- Production before SHA12: `6e36b5761ff3`
- Candidate SHA12: `13133993edf5`
- Dev after/readback SHA12: `13133993edf5`
- Production after SHA12: `6e36b5761ff3`
- Dev readback matches candidate: `true`
- Production unchanged: `true`

## Handles added in Dev

### `top30-mexico66-regular`

- `tenis-onitsuka-tiger-mexico-66-white-blue-branco` → `White Blue`
- `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` → `Black White`
- `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` → `Birch Rust`

Result: 10 handles / 10 labels / 10 images.

### `top30-mexico66-sd`

- `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` → `Cream Peacoat`
- `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` → `Licorice Champagne`

Result: 12 handles / 12 labels / 12 images.

### `top30-nb-9060`

- `tenis-new-balance-9060-sea-salt-concrete-branco` → `Sea Salt Concrete`
- `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` → `Rose Sugar`

Result: 11 handles / 11 labels / 11 images.

## QA Dev static/readback

Pass: `true`

Checks:

- malformed image URLs: `0`
- Liquid `for/endfor` balance: OK
- Liquid `if/endif` balance: OK
- every added handle simulates 5 cards after current-product exclusion: OK
- current product excluded from cards: OK
- labels short: max 18 chars in affected groups
- public `.js` sample for all 7 added handles: 7/7 OK and available

## Preview limitation

Public unauthenticated Dev preview may drop `preview_theme_id`, so Asset API readback + static simulation are the authoritative Dev validation here. Production remained unchanged.

## Risk for Production

Low/moderate. The change is scoped to existing Curadoria groups and only expands arrays. It does not alter product data, price, stock, cart, checkout, apps, or visible product titles. Main risk is Shopify storefront render/cache propagation after Production upload, which must be verified with live QA and rollback ready.

## Rollback

- Dev rollback: restore `dev-before.liquid` from this folder to `snippets/lk-variante-top30-visited.liquid` on theme `155065450718`.
- Production rollback, if promoted and needed: restore current Production backup `production-before.liquid` from this folder to the same asset on theme `155065417950`, then run live QA.

## Approval needed for Production

Exact approval wording:

`Aprovo promover o Batch 11 Curadoria LK para Production, expandindo Mexico 66 regular, Mexico 66 SD e New Balance 9060 com os 7 handles validados no Dev, com backup/readback/live QA e rollback.`

## Non-actions

- No Production write was executed in the Dev apply step.
- No product, price, stock, app, GMC, Tiny, Klaviyo, Meta or checkout write was executed.
