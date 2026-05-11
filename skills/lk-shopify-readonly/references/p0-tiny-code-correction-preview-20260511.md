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

## Tiny write execution note — variation child records

Observed during approved execution (`reports/lk-p0-tiny-code-correction-execution-2026-05-11.json`):

- `produto.alterar` with a bare `{ "id": ..., "codigo": ... }` object can return `OK` but leave `codigo` unchanged. Do not trust status alone; read back the product/variation.
- The effective API layout was the official root wrapper: `{ "produtos": [{ "produto": { ... } }] }`.
- For a variation child record, update the child Tiny ID directly with required existing fields (`sequencia`, `id`, `codigo`, `nome`, `unidade`, `preco`, `preco_promocional`, `origem`, `situacao`, `tipo`, and `grade` when present). Then verify before/after non-code fields.
- Updating the parent via `variacoes` failed when sibling variations had blank codes: Tiny returned `É necessário informar o código para um produto variação.` Do not fill sibling codes unless separately approved.
- Success criteria: Tiny write status `OK` plus live `produto.obter` shows target `codigo` exactly and non-code fields unchanged.
- For apparel sizes, match normalized grade/size exactly; do not use substring matching because `S/P` can falsely match `XS/PP`, and `L/G` can falsely match `XL/GG`.