# Shopify SALE tag + custom collection workflow (LK, 2026-05-15)

## Context

Lucas asked to mark all Adidas Samba products with tag `SALE` so they would appear at `https://lksneakers.com.br/collections/sale`.

The `sale` collection in LK was not a smart collection keyed only by tag; it resolved as a **custom collection** titled `LK Sale`. Therefore adding the product tag alone was insufficient to guarantee display in the collection.

## Safe execution pattern

1. Verify Shopify credentials via Doppler without printing values.
2. Resolve the collection handle first:
   - `GET /admin/api/2024-01/custom_collections.json?handle=sale&limit=5`
   - `GET /admin/api/2024-01/smart_collections.json?handle=sale&limit=5`
3. If `sale` is a custom collection, plan both:
   - product tag mutation: add `SALE` to matching products;
   - collection membership: create `collect` records for active/published products.
4. Prefer Admin GraphQL search for product candidates, because REST product pagination/search can miss non-active statuses or broad title contains:
   - Query: `products(first: 100, after: $after, query: "title:*samba*")`
   - Fields: `id`, `legacyResourceId`, `title`, `handle`, `vendor`, `productType`, `tags`, `status`, `publishedAt`.
5. Apply a conservative local match rule:
   - title contains `samba` (captures Samba/Sambae);
   - and Adidas appears in title/vendor/product type.
6. Back up current IDs/titles/tags before writing.
7. Add tag via GraphQL `tagsAdd(id: $id, tags: ["SALE"])`.
8. For custom collection membership, add only active/published products via REST:
   - `POST /admin/api/2024-01/collects.json`
   - body: `{ "collect": { "collection_id": <sale_collection_id>, "product_id": <legacyResourceId> } }`
9. Verify with GraphQL, not only REST collects pagination:
   - all candidates have tag `SALE`;
   - `collectionByHandle(handle:"sale") { products(...) { nodes { id legacyResourceId title tags status publishedAt } } }` contains every active/published candidate.
10. Public smoke check: fetch `/collections/sale` and confirm page HTML includes expected Samba/Sambae product text.

## Pitfalls observed

- `GET /products.json?limit=250&fields=...` only returned 250 products in this run and produced zero Samba matches, while GraphQL search returned the expected candidates. Do not rely on a simple REST full-catalog scan for this class of product discovery.
- Shopify search query syntax differs: `title:samba` returned zero; `title:*samba*` returned title contains matches.
- Broad query `adidas samba` returned irrelevant products (Campus, Gazelle, New Balance) due full-text matching. Always re-filter locally.
- A tag named `SALE` does not automatically place products in a manual/custom collection. Resolve collection type before writing.
- REST `collects` verification can be misleading if pagination is incomplete or ordered unexpectedly. Use GraphQL `collectionByHandle.products` full pagination for final membership verification.

## Audit artifact pattern

Store a JSON audit under:

`/opt/data/hermes_bruno_ingest/audits/shopify_sale_tag/`

Include:

- timestamp and store/API version;
- collection ID/title/handle/type;
- match rule;
- before tags;
- tag write results;
- collect write results;
- GraphQL final verification counts;
- rollback data: previous tag arrays and created collect IDs where available.
