# LK P0 blocked residual decision queue — 2026-05-11

## When to use

Use after approved Tiny `codigo` writes have resolved the safe subset of LK P0 residuals and a small set remains blocked by missing Shopify SKU, blank Tiny `codigo`, or duplicate Tiny variation rows.

## Session learning

After resolving 9/15 P0 residual Tiny `codigo` gaps, the final 6 were not safe for automatic writes even though all had at least one Tiny size/color match on live recheck.

Observed final blocked set:

- 5 rows had Shopify SKU blank and Tiny matched variation(s) with blank `codigo`:
  - Pace Cotton Code Branca G/L: 2 Tiny matches, both blank.
  - Aimé Leon Dore Musician Graphic Off White S/P: 4 Tiny matches, all blank, including color/family ambiguity.
  - Rhode Pocket Blush Sleepy Girl / Soft Mauve: 1 Tiny match, blank `codigo` (simplest manual code decision).
  - Pace Cotton Code Preta G/L: 2 Tiny matches, both blank.
  - Pace Sketch Yourself Off White P/S: 2 Tiny matches, both blank.
- 1 row had Shopify SKU present but Tiny duplicate ambiguity:
  - Pace Patavision Off White P/S: Shopify SKU `PAC-5857246-S`, two Tiny P/S matches with blank `codigo`; choose the correct Tiny ID before any write.

## Correct next artifact

Do **not** force a write preview for these rows. Create a decision queue for Lucas/Júlio:

- Markdown business-readable queue under `areas/lk/rotinas/`.
- JSON report under `reports/`.
- CSV manual-review queue under `reports/`.

Include fields:

- priority;
- classification;
- product title;
- Shopify product/handle/variant;
- size;
- live Shopify SKU or `[sem SKU]`;
- Tiny match count;
- Tiny candidate IDs and parent IDs;
- Tiny candidate codes;
- recommended next step;
- approval boundary.

## Classification rules

- `needs_canonical_code_decision_shopify_and_tiny_blank`: Shopify SKU is blank and Tiny match(es) are blank. Lucas/Júlio must define the SKU/code and choose the real Tiny ID if duplicates exist. No Tiny or Shopify write is safe yet.
- `ambiguous_tiny_duplicate_with_shopify_sku`: Shopify SKU exists, but more than one Tiny match could receive it. Lucas/Júlio must choose the exact Tiny ID first; then prepare a Tiny `codigo` preview using the Shopify SKU.
- `needs_cadastro_or_manual_search_no_tiny_size_match`: no reliable detailed Tiny size/color match; cadastro/manual search required before sourcing.

## Guardrails

- Read-only Shopify GET + Tiny `produtos.pesquisa`/`produto.obter` only while building the queue.
- No Shopify write, no Tiny write, no price/stock/title change, no supplier contact, no sourcing recommendation until SKU truth is resolved.
- A single Tiny match with blank `codigo` is still not executable if Shopify SKU is also blank; it is only a simpler human code decision.
- A Shopify SKU with duplicate blank Tiny matches is not enough; pick the exact Tiny child ID before writing.

## Reporting to Lucas

Use concise Portuguese:

- “A parte segura já foi feita; os 6 restantes viraram fila de decisão/cadastro.”
- Give counts by classification.
- List each item with Shopify SKU, Tiny candidate IDs, and next action.
- State explicitly that candidates safe for automatic write now = 0.
