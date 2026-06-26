# LK Collection Filters — New Balance 204L read-only packet

Timestamp: 2026-06-03T18:04:53Z
URL: https://lksneakers.com.br/collections/new-balance-204l
Scope: read-only investigation only. No Shopify writes.

## Verdict

Lucas is right: the color filter is incomplete, and on this specific collection the Brand and Product Category filters add no decision value because all visible products are New Balance and sneaker/shoe category.

## Current storefront evidence

Public sidebar groups parsed from the live collection HTML:

- Preço: numeric range
- Categoria: 1 value — `Tênis (12)`
- Tamanho: 12 values — 34, 35, 36, 37, 37.5, 38, 39, 40, 41, 42, 43, 44
- Disponibilidade: 2 values — Em estoque, Fora de estoque
- Cor: 2 values only
  - `Grisalho (3)` using `filter.v.t.shopify.color-pattern=gid://shopify/TaxonomyValue/8`
  - `Preto (2)` using `filter.v.t.shopify.color-pattern=gid://shopify/TaxonomyValue/1`
- Marca: 1 meaningful value — `New Balance (12)`

Theme role rechecked via Shopify Admin API before analysis:

- `155065417950` — `lk-new-theme/production` — `role=main`
- `155065450718` — `lk-new-theme/dev` — `role=unpublished`

Caveat: the public HTML still included a stale `Shopify.theme` JSON block saying `lk-new-theme/dev` / `role=main`, likely storefront/edge cache residue. Admin role is the source of truth for writes.

## Product data evidence

Collection products show color intent in titles/handles/tags, but many products do not have Shopify taxonomy category and color-pattern populated.

Examples:

- `tenis-new-balance-204l-mushroom-arid-stone-marrom`
  - title color: Marrom
  - category: `Uncategorized`
  - `shopify.color-pattern`: empty
- `tenis-new-balance-204l-timberwolf-bege`
  - title color: Bege
  - category: `Uncategorized`
  - `shopify.color-pattern`: empty
- `tenis-new-balance-204l-pastel-pink-rosa`
  - title color: Rosa
  - category: `Uncategorized`
  - `shopify.color-pattern`: empty
- `tenis-new-balance-204l-natural-roxo`
  - title color: Roxo
  - category: `Uncategorized`
  - `shopify.color-pattern`: empty
- `tenis-new-balance-204l-grey-matter-shipyard-cinza`
  - category: `Sneakers`
  - `shopify.color-pattern`: populated
- `tenis-new-balance-204l-black-magnet-preto`
  - category: `Sneakers`
  - `shopify.color-pattern`: populated

Expected color set inferred from current collection titles/tags includes more than the two storefront chips, e.g. Bege, Marrom, Cinza/Grisalho, Prateado, Rosa, Roxo, Branco, Preto, Laranja and possibly Verde/Sage depending on taxonomy/color naming decision.

## Root cause hypothesis

The native Shopify color filter is reading `filter.v.t.shopify.color-pattern`, not regular color tags or title text. Therefore only products with Shopify taxonomy/category/color-pattern populated contribute to the color chips. Tags like `Bege`, `Marrom`, `Rosa`, etc. are not enough for this particular native filter.

## Agreement on UX

For a collection where a filter has only one non-active value, it should usually be hidden:

- Hide `Marca` when the only value is New Balance.
- Hide `Categoria`/`Tipo` when the only meaningful value is Tênis/Sneakers.
- Keep the filter visible if the user has an active value selected and needs to remove it, or provide active-filter chips/clear-all elsewhere.

## Safe correction options

### Option A — Product data/taxonomy fix (best native filtering)

Populate Shopify product category and `shopify.color-pattern` for all products in the collection.

Pros:
- Native filter URLs work correctly.
- Benefits this collection and other collection/search contexts.
- More semantically correct for Shopify/Search & Discovery.

Cons:
- Requires Shopify product/metafield writes.
- Needs exact mapping to Shopify taxonomy/metaobject IDs per color.
- Must backup current product category/metafields and read back after writes.

### Option B — Theme-only UX cleanup + synthetic color fallback (lower data-risk, less canonical)

On `lk-new-theme/dev` only, hide one-value `Marca`/`Categoria` filters for this collection and render a pilot color filter derived from product title/tags/handles.

Pros:
- Can preview without product data changes.
- Faster visual fix for this collection.

Cons:
- Theme write still needs approval.
- Synthetic filtering may require custom JS/query behavior and will be less canonical than native Search & Discovery filters.
- Does not repair underlying product taxonomy.

## Recommended path

Start with a narrow pilot on `/collections/new-balance-204l`:

1. Read-only full color mapping for every product in this collection.
2. Approval packet with before/after product taxonomy/color-pattern values.
3. If Lucas approves product data writes: backup all product category + `shopify.color-pattern`, update only these fields, read back, then QA native color chips.
4. Separately, prepare a dev-theme preview to hide one-value `Marca` and `Categoria` groups on this collection; no production upload without explicit approval.

## Non-actions

- No Shopify product writes.
- No theme upload.
- No Search & Discovery config write.
- No price, stock, Tiny, GMC, checkout, app, campaign or collection membership changes.
