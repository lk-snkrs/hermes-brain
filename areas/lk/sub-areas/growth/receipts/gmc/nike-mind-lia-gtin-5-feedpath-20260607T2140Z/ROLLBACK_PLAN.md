# Rollback plan — Nike Mind LIA GTIN 5

Source snapshot:
`../nike-mind-lia-gtin-5-20260607T2133Z/before_snapshots.json`

Rollback action:
- Re-insert each original product resource from `before_snapshots.json` via Content API `products.insert`, removing output-only fields (`kind`, `id`, `source`, `creationDate`, `expirationDate`, `googleExpirationDate`, `destinationStatuses`, `itemLevelIssues`, `productStatus`).
- Original snapshots had no `gtin` field for these 5 Local/LIA items.
- Readback each `productId` and confirm `gtin` absent/null.

Important:
- Do not touch Shopify.
- Do not delete products.
- Do not alter price, availability, title, link or MPN beyond restoring original snapshot.
