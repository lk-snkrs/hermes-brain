# LK P0 residual live lookup after Fila B prioritization — 2026-05-11

## When to use

Use after catalog-wide Shopify↔Tiny SKU normalization and residual prioritization when a small P0 set overlaps current sales/rupture queues. This is the safe bridge before deciding whether any residual item can move into Fila A sourcing/reposition.

## Session learning

A residual item with a Shopify SKU or a Tiny search hit is **not** automatically safe. Before a SKU-only write or commercial sourcing decision, verify the live Shopify variant and Tiny product details read-only.

Observed P0 live lookup on 2026-05-11:

- 15 P0 residual variants checked.
- 0 had a unique Tiny candidate with canonical `codigo` populated.
- 6 had Tiny size/color matches but code was missing or ambiguous.
- 9 had no Tiny size match in detailed candidate checks.

Conclusion: no P0 row was safe for automatic SKU-only correction or sourcing. The safe next step was manual/Tiny canonical-code resolution.

## Read-only workflow

1. Start from the prioritized residual report, usually `reports/lk-shopify-tiny-residual-fila-b-prioritized-review-YYYY-MM-DD.json`.
2. For each P0 row, read live Shopify state:
   - `GET /admin/api/2024-01/variants/{variant_id}.json`
   - `GET /admin/api/2024-01/products/{product_id}.json`
3. Search Tiny read-only with multiple queries:
   - current Shopify SKU when present;
   - full product title;
   - cleaned title without color words;
   - first few title tokens if needed.
4. For Tiny candidates, call detail read-only, e.g. `produto.obter`, and inspect variation/grade/size/color entries rather than trusting search result title alone.
5. Classify each row:
   - `candidate_unique_with_code_preview_possible`: exactly one size/color match and canonical Tiny `codigo` exists.
   - `candidate_size_match_but_code_missing_or_ambiguous`: Tiny likely has the product/variant, but code is missing or multiple candidates exist.
   - `no_tiny_size_match_found`: no safe Tiny variant match found in candidate details.
6. Only rows in `candidate_unique_with_code_preview_possible` may move to a SKU-only write preview. All others require manual/Tiny correction first.

## Guardrails

- Read-only only unless Lucas separately approves a narrow SKU-only write preview.
- Do not write Shopify/Tiny, change price/stock/title, contact supplier, or create sourcing/campaign/customer actions from P0 residual lookup alone.
- Tiny search hits with `[sem código]` or missing `codigo` are not sufficient for Shopify SKU correction.
- A Shopify SKU that follows an LK-looking pattern still does not prove Tiny truth.

## Reporting pattern

Report in Portuguese:

- Total P0 checked.
- Count with unique Tiny candidate + `codigo`.
- Count with Tiny match but missing/ambiguous code.
- Count with no Tiny detailed match.
- Clear next action: resolve Tiny canonical code/manual mapping before Fila A/sourcing.
- Explicitly state no writes/sourcing/campaigns were done.

## Artefacts from the session

- `areas/lk/rotinas/lk-p0-residual-live-lookup-enriched-2026-05-11.md`
- `reports/lk-p0-residual-live-lookup-2026-05-11.json`
- `reports/lk-p0-residual-live-lookup-enriched-2026-05-11.json`
