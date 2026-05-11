# Shopify image enrichment for CRM/Klaviyo previews — 2026-05-11

Use this when a local CRM/recompra queue needs customer-like product visuals, but no Shopify writes or Klaviyo objects should be created.

## Problem observed

A CRM queue row may carry a base SKU such as `1183C015101`, while Shopify variants/images are stored with size/variant suffixes such as `1183C015101-1`. A strict SKU lookup can therefore return no image even though the product exists in Shopify.

## Safe read-only resolution

1. Try exact variant/SKU lookup first.
2. If no image is found, derive a base SKU/product hint from the queue row.
3. Run a read-only Shopify GraphQL product search by likely product title, handle, vendor/family, or base SKU fragment.
4. Use the product-level featured image or first media image as preview enrichment only.
5. Record the fallback in the MD/JSON QA report so the HTML can stay clean and customer-like.
6. Do not infer stock from this lookup. Tiny remains stock truth.
7. Do not create Shopify/Klaviyo assets, lists, segments, campaigns, or customer sends from this step.

## Verification standard before saying preview is ready

- Count unique products/SKUs in the queue.
- Count how many received Shopify images.
- Open the generated HTML in a browser and visually verify no broken/missing images.
- Report the enrichment result as `images loaded X/Y` or equivalent.
- If any fallback was used, say it was a read-only fallback and that stock was still validated separately via Tiny if availability is part of the campaign gate.

## Reporting language for Lucas

Use: “Corrigi o enrichment de imagem: SKU exato primeiro, fallback por produto/handle quando o SKU base não bate com a variante Shopify. Continua read-only e sem mexer em Shopify/Klaviyo.”

Avoid implying this proves stock or authorizes campaign send.