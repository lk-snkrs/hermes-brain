# NB 204L — normalize existing color-pattern receipt

Timestamp: 2026-06-03T18:35Z

## Approval captured

Lucas corrected the previous choice and approved: `normalizar também os 12 produtos que já tinham cor preenchida errada/genérica`.

## Scope executed

Shopify metafield writes executed only for the 12 NB 204L products that already had non-empty `shopify.color-pattern` values from before.

- Planned products: 12
- Products that needed write: 11
- Products already matching target: 1
- Mutation errors: 0

## Target field

- Namespace/key: `shopify.color-pattern`
- Type: `list.metaobject_reference`

## Readback after normalization

Admin readback for collection `new-balance-204l`:

- Products in collection: 32
- Category `Sneakers`: 32/32
- Missing category: 0
- Missing `shopify.color-pattern`: 0
- Inferred color mismatches after normalization: 0

Final color reference counts:

- Marrom: 4
- Bege: 4
- Gray/Cinza: 5
- Silver/Prateado: 7
- Rosa: 3
- Roxo: 1
- Branco: 1
- Jet Black/Preto: 2
- Orange/Laranja: 1
- Verde: 2
- Azul: 2

These final counts match the original inferred-color counts for the 32 products.

## Public storefront sample

Fetched public collection URL with cache-buster:

- URL: `https://lksneakers.com.br/collections/new-balance-204l?cb=nb204lnormalize1835`
- HTTP status: 200

Public HTML contained filter/color label signals including Marrom, Bege, Gray/Cinza, Silver/Prateado, Rosa, Roxo, Branco.

Note: production theme still shows singleton `Marca`/`Categoria` until the approved Dev theme change is promoted to Production.

## Artifacts

- Backup before writes: `backup_before.json`
- Mutation results: `apply_results.json`
- Readback after writes: `readback_after.json`

## Rollback

Rollback can be performed from `backup_before.json` by restoring the previous `shopify.color-pattern` value for each product.

## Non-actions

- No production theme upload.
- No theme publish.
- No product title, price, stock, availability, SKU, image or tag changes.
- No Tiny/GMC/Klaviyo/Meta/WhatsApp writes.
