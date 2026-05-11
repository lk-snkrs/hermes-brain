# Shopify SKU normalization to Tiny — 2026-05-11

## Session learning

Lucas explicitly approved a narrow Shopify write: standardize LK Shopify variant SKUs so they exactly match Tiny `codigo` values. This is an exception to the normal read-only posture and must remain tightly scoped.

## Proven workflow

1. Build a variant-level plan before writing:
   - product title;
   - Shopify handle;
   - Shopify variant ID/GID and numeric REST ID;
   - size / variant title;
   - current Shopify SKU;
   - target Tiny `codigo`;
   - Tiny product ID/name/situation;
   - rollback SKU.
2. Only include high-confidence rows:
   - Tiny `codigo` non-empty;
   - Shopify variant found by product + size and/or existing SKU;
   - target differs from current Shopify SKU;
   - no ambiguity across variants.
3. Skip, do not guess:
   - Tiny `codigo` blank;
   - variant not found with confidence;
   - current SKU already identical;
   - title/size mismatch.
4. Execute SKU-only writes via REST:
   - `PUT /admin/api/2024-01/variants/{numeric_variant_id}.json`
   - body: `{ "variant": { "id": <numeric_id>, "sku": "<Tiny codigo>" } }`
5. Verify every row immediately:
   - `GET /admin/api/2024-01/variants/{numeric_variant_id}.json`
   - compare live `variant.sku` exactly to Tiny `codigo`, preserving spaces/punctuation.
6. Write audit artifacts before claiming completion:
   - execution JSON with plan, skipped reasons, results, rollback data;
   - concise markdown summary in Brain;
   - update LK MAPA / routine index / control doc / changelog;
   - run health check and secret scan;
   - PR + merge when Brain docs changed.

## Tool/API pitfall observed

GraphQL `productVariantUpdate` returned no `userErrors`, but also did not provide a useful updated SKU and live verification still showed old values. REST `PUT /variants/{id}.json` returned HTTP 200 and live GET verification confirmed exact SKU updates. For this LK SKU-only mutation, prefer REST over GraphQL unless re-tested.

## Guardrail language for Lucas

Report clearly:

- how many variants were planned, written, verified, and skipped;
- which products/tamanhos changed as `old -> new`;
- what was not changed: price, stock, title, handle, images, collections, campaigns, Klaviyo/WhatsApp, suppliers, Tiny, DB, VPS/Docker, secrets;
- where rollback data lives.

## Rollback shape

For each written variant, rollback is the inverse REST call using the same variant ID and stored `rollback_sku`:

```json
{
  "variant": {
    "id": 45747573457118,
    "sku": "<rollback_sku>"
  }
}
```

Never roll back blindly; verify current live SKU first and confirm the intended rollback scope.
