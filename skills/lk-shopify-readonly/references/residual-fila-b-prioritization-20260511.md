# LK residual Fila B prioritization after Shopify SKU normalization — 2026-05-11

## When to use

Use after catalog-wide Shopify SKU normalization to Tiny when there is a skipped/residual set that was not safe to mutate automatically. This is the bridge between SKU hygiene and a new commercial Fila A sourcing/reposition preview.

## Session learning

After fixing all high-confidence divergences, do **not** jump straight to sourcing. Classify the skipped variants and prioritize manual review first.

Observed residual after the 2026-05-11 catalog run:

- 1,282 variants skipped by safety.
- 857 had a Shopify SKU but no safe Tiny match.
- 374 had no Shopify SKU and no safe Tiny match.
- 40 had no Shopify SKU and ambiguous title+size match.
- 11 had Shopify SKU and ambiguous title+size match.

## Recommended residual buckets

For each skipped row, derive a `residual_bucket`:

- `ambiguous_title_size_com_sku`: Shopify SKU exists, but product+size maps to 2–3 Tiny candidates.
- `ambiguous_title_size_sem_sku`: Shopify SKU blank, product+size maps to 2–3 Tiny candidates.
- `no_safe_tiny_match_com_sku`: Shopify SKU exists, but no safe Tiny code match.
- `no_safe_tiny_match_sem_sku`: Shopify SKU blank and no safe Tiny code match.

## Priority sequence before new Fila A

1. **P0**: residual rows that also appear in current stock/sales/rupture queues. Resolve before any sourcing or reposition recommendation.
2. **P1**: all ambiguous title+size rows. Volume is usually small and needs human decision among candidates.
3. **P2**: Shopify variants with no SKU and no safe Tiny match. These require canonical SKU before commercial action.
4. **P3**: Shopify variants with a SKU but no safe Tiny match. Separate temporary LK SKUs, products outside Tiny, apparel/accessories not stocked the same way, and Tiny spacing/punctuation false negatives.

## Reporting pattern for Lucas

Say:

- “Corrigi todos os divergentes seguros; agora classifiquei/priorizei os residuais.”
- Give counts by bucket and priority.
- State clearly that residual rows are not safe for automatic sourcing/reposition until Tiny SKU/source is confirmed.
- Do not imply “all products fixed”; say “all safe/high-confidence divergences fixed; ambiguous/no-match rows queued.”

## Guardrails

- This residual prioritization is read-only unless Lucas explicitly approves a new narrow SKU-only write.
- No Shopify/Tiny write, price/stock/title change, supplier contact, sourcing order, campaign/send, customer action, DB/infra change.
- Any proposed correction must be a preview with product name + Shopify variant ID + size + old SKU + target Tiny `codigo` + confidence + rollback SKU.

## Artefact examples from the session

- `areas/lk/rotinas/shopify-tiny-fila-b-residual-pos-saneamento-2026-05-11.md`
- `reports/lk-shopify-tiny-residual-fila-b-2026-05-11.json`
- `areas/lk/rotinas/shopify-tiny-fila-b-residual-priorizada-2026-05-11.md`
- `reports/lk-shopify-tiny-residual-fila-b-prioritized-review-2026-05-11.json`
