# NB 204L — color-pattern + category apply receipt

Timestamp: 2026-06-03T18:28Z

## Approval captured

Lucas approved: `corrigir cores + categoria dos 20 produtos NB 204L`.

## Scope executed

Shopify product/metafield writes executed for the 20 NB 204L products that were missing:

- `shopify.color-pattern`
- product category/taxonomy

## Target category

- `gid://shopify/TaxonomyCategory/aa-8-8`
- `Apparel & Accessories > Shoes > Sneakers`

## Target color metaobjects used

- Marrom → `gid://shopify/Metaobject/77492814046`
- Bege → `gid://shopify/Metaobject/59566096606`
- Cinza → `gid://shopify/Metaobject/77492846814` (`Gray`)
- Prateado → `gid://shopify/Metaobject/55902240990` (`Silver`)
- Rosa → `gid://shopify/Metaobject/133736169694`
- Roxo → `gid://shopify/Metaobject/102441582814`
- Branco → `gid://shopify/Metaobject/94029906142`
- Laranja → `gid://shopify/Metaobject/57438994654` (`Orange`)
- Verde → `gid://shopify/Metaobject/59568619742`

## Apply result

- Planned products: 20
- Executed products: 20
- Mutation errors: 0

## Readback after apply

Admin readback for collection `new-balance-204l`:

- Products in collection: 32
- Category `Sneakers`: 32/32
- Missing category: 0
- Missing `shopify.color-pattern`: 0

Color reference counts after apply:

- Marrom: 2
- Bege: 4
- Gray: 16
- Silver: 4
- Rosa: 3
- Roxo: 1
- Jet Black: 10
- Branco: 2
- Orange: 1
- Vanilla: 1
- Verde: 1

## Public storefront sample

Fetched public collection URL with cache-buster:

- URL: `https://lksneakers.com.br/collections/new-balance-204l?cb=nb204lcolor1828`
- HTTP status: 200

Label hits in public HTML included: Marrom, Bege, Gray, Silver, Rosa, Roxo, Branco, Cinza, Prateado.

## Important caveat

This apply fixed the 20 products that had missing native data. It did not normalize the 12 products that already had a non-empty `shopify.color-pattern` value, even if their existing value may be too generic or wrong for the product's Portuguese color label.

Examples for a possible second pass:

- `tenis-new-balance-204l-cortado-marrom` currently has `Gray + Jet Black`, inferred primary color `Marrom`.
- `tenis-new-balance-204l-navy-salt-watre-azul` currently has `Gray + Jet Black`, inferred primary color `Azul`.
- `tenis-new-balance-204l-silver-metallic-double-bubble-prateado` currently has `Gray + Jet Black`, inferred primary color `Prateado`.

A separate approval is required before overwriting existing non-empty color-pattern values.

## Artifacts

- Backup before writes: `backup_before.json`
- Mutation results: `apply_results.json`
- Readback after writes: `readback_after.json`

## Rollback

Rollback can be done from `backup_before.json` by restoring each product's previous category and previous `shopify.color-pattern` value.

## Non-actions

- No production theme upload.
- No theme publish.
- No price/stock/availability changes.
- No Tiny/GMC/Klaviyo/Meta/WhatsApp writes.
