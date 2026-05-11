# LK stock SKU saneamento — session learning 2026-05-11

Use this reference when Lucas asks to continue LK OS Stock Intelligence, resolve Fila B before Fila A, or reconcile missing Shopify SKUs with Tiny stock mapping.

## Workflow correction from Lucas

Lucas explicitly asked for sequence: **B first, then A, then the other things**.

For stock decision work this means:

1. Resolve/saneamento for Fila B (`sem SKU no Shopify`, `mapear SKU no Tiny`) before making commercial sourcing/reposition recommendations.
2. Only after B is classified, prepare Fila A preview for P0/P1 sourcing/reposition.
3. Then do secondary items: velocity vs lead time, Mission Control cards, Data Spine follow-up.

Do not jump directly to purchasing/sourcing just because a queue has ruptures.

## Read-only technique used

For orders/line-items with `[sem SKU no Shopify]`:

- Query Shopify Admin GraphQL with operation type `query`, not mutation.
- Search product by title and inspect variants.
- Match the requested size/variant using `selectedOptions` and variant title.
- If a variant has an SKU, treat it as a **candidate**, not an automatic correction.
- Then search Tiny read-only by the candidate SKU and/or product name.

Safe GraphQL shape:

```graphql
query ProductSkuLookup($query: String!) {
  products(first: 10, query: $query) {
    nodes {
      id
      title
      handle
      status
      variants(first: 100) {
        nodes {
          id
          title
          sku
          selectedOptions { name value }
        }
      }
    }
  }
}
```

## Tiny SKU search pitfall

Tiny search can fail when Shopify SKU omits spaces or punctuation that Tiny stores. Example patterns observed:

- Shopify `1183C102751-3` matched Tiny `1183C102 751-3`.
- Shopify `1183B566021-4` matched Tiny `1183B566 021-4`.
- Some Tiny variants have blank `codigo` but clear product name + size, so they are candidates for mapping, not proof of absence.

Search strategy:

1. Search exact Shopify SKU.
2. If no result, try a spaced normalized form for Onitsuka-style SKUs: `^[A-Z0-9]{7}[A-Z0-9]{3}-.+$` → insert a space before the 3-digit color block.
3. Search product title/name and select by size suffix (`" - 39"`, `" - 42.5"`, etc.).
4. Deduplicate candidates by Tiny id/codigo/name.
5. Mark confidence and action as mapping/alias preview; do not write Tiny automatically.

## Output classification from the 2026-05-11 run

Fila B result categories worth reusing:

- `sku_candidate_found`: Shopify variant SKU found by product + size; validate with Tiny before moving to Fila A.
- `tiny_candidate_found`: Tiny candidate found for a Shopify SKU that previous lookup missed; propose alias/mapping review.
- `needs_manual_shopify_sku`: no confident current Shopify SKU candidate; manual catalog review before commercial action.
- `needs_manual_tiny_mapping`: no confident Tiny candidate after fallback searches; manual Tiny mapping.

## Approval boundary

Even when B is resolved and A is prepared:

- Free: read-only lookup, docs, queue, preview, Mission Control unassigned cards.
- Requires Lucas approval: any write to Shopify/Tiny, purchase/reposition, supplier contact, campaign/send, or external/team-facing execution.

## Files created in the successful run

- `areas/lk/rotinas/stock-sku-saneamento-b-e-preview-a-2026-05-11.md`
- `reports/lk-stock-sku-saneamento-b-e-preview-a-2026-05-11.json`

These are examples, not permanent source of truth; future runs should use current data and timestamped outputs.
