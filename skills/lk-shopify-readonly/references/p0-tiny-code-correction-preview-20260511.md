# LK P0 Tiny code correction preview — 2026-05-11

## When to use

Use after the P0 residual correction queue when a subset has Tiny size/color matches but blank `codigo` and/or ambiguous candidate rows.

## Session learning

Do not jump from “Tiny matched the size” to writing. Build a preview that separates:

- rows with a target `codigo` supported by live Shopify SKU and sibling SKU pattern;
- rows where Shopify is also missing SKU or the Tiny match is ambiguous, so the target `codigo` must be decided by Lucas/Júlio first.

Observed P0 preview:

- 6 rows had Tiny size/color matches.
- 2 rows were candidate Tiny `codigo` writes because Shopify had a consistent SKU and Tiny variation `codigo` was blank:
  - New Balance 204L Cortado Marrom size 39 → `NB-0254942-39`.
  - Nike x Skims Rift Mesh Archaeo Brown size 36 → `NKS-1065310-36`.
- 4 rows were not write-ready because Shopify also had no SKU and/or Tiny was ambiguous:
  - Pace Cotton Code Branca G/L.
  - Rhode Pocket Blush Sleepy Girl.
  - Pace Cotton Code Preta G/L.
  - Pace Sketch Yourself Off White P/S.

## Preview artifact fields

For each candidate include:

- Shopify variant ID;
- size;
- live Shopify SKU;
- Tiny item/variation ID;
- Tiny current `codigo`;
- proposed Tiny `codigo`;
- confidence;
- rollback;
- explicit approval wording.

## Guardrails

- Preview only is allowed.
- Tiny `codigo` write requires explicit scoped approval.
- Do not write Shopify during a Tiny-code preview.
- Do not change price, stock, product text/title, images, campaign, supplier, or customer communication.
- If the target `codigo` is blank or inferred weakly, do not include it as executable; route to human code decision first.

## Approval wording

Safe approval wording should be scoped, e.g.:

`aprovo preencher codigo Tiny dos 2 itens candidatos com os SKUs Shopify propostos, sem alterar Shopify, preço, estoque ou produto`

After approval, execute only those exact fields, then read back Tiny and document rollback.