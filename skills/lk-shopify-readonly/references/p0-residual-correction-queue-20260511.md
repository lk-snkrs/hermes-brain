# LK P0 residual correction queue after live Shopify/Tiny lookup — 2026-05-11

## When to use

Use after the residual Fila B prioritization identifies P0 rows that overlap with current sales/rupture signals and a read-only live Shopify/Tiny lookup has been run.

## Session learning

A live lookup can find Tiny products/variations but still **not** make a Shopify SKU write safe. In the observed P0 run:

- 15 P0 residual variants were checked read-only against Shopify variant/product GET endpoints and Tiny `produtos.pesquisa` + `produto.obter`.
- 0/15 had a unique Tiny candidate with canonical `codigo` populated.
- 6/15 had Tiny size/color matches but the matched Tiny variation/product had blank `codigo` or ambiguous duplicate matches.
- 9/15 had no reliable detailed Tiny size match.

Therefore the correct next artifact is not a write plan and not Fila A/sourcing. It is a **P0 correction queue** for human/Tiny SKU decisions.

## Correct output artifacts

Create three artifacts:

- Markdown routine for Lucas/business reading: `areas/lk/rotinas/lk-p0-residual-correction-queue-YYYY-MM-DD.md`.
- JSON report for machine reuse: `reports/lk-p0-residual-correction-queue-YYYY-MM-DD.json`.
- CSV queue for manual review: `reports/lk-p0-residual-correction-queue-YYYY-MM-DD.csv`.

Index the routine in `empresa/rotinas/_index.md` and run Brain checks before versioning.

## Queue fields

For each P0 row include:

- priority (`P0`);
- classification:
  - `A_match_tiny_sem_codigo_ou_ambiguo`;
  - `B_sem_match_tiny_detalhado`;
- product title;
- Shopify product ID / handle;
- Shopify variant ID;
- size/variant title;
- live Shopify SKU or `[sem SKU]`;
- orders/revenue signal;
- Tiny size match count;
- Tiny candidate details where available;
- recommended next step;
- approval boundary for any Tiny/Shopify write.

## Decision logic

- If Tiny has a size/color match but `codigo` is blank or duplicate/ambiguous, recommend defining/correcting the canonical Tiny `codigo` first, then revalidating Shopify.
- If Shopify has a SKU but Tiny has no detailed match, use the Shopify SKU only as a search clue; do not assume it is canonical Tiny truth.
- If Shopify has no SKU and Tiny has no detailed match, block sourcing/repositioning until Tiny cadastro/código is resolved.
- If no row has a unique Tiny candidate with populated `codigo`, explicitly state that **no SKU-only automatic write is safe**.

## Guardrails

- Read-only lookup and queue creation are allowed.
- No Shopify/Tiny write, product publish, price/stock change, sourcing order, supplier contact, campaign, or customer send.
- Any later correction must be a preview with product, Shopify variant ID, current SKU, target Tiny `codigo`, decision source/confidence, and rollback.

## Reporting pattern to Lucas

Say:

- “Transformei o diagnóstico P0 em fila acionável.”
- Give counts by classification.
- Say whether any item is safe for SKU-only preview; if 0, say none.
- State the next safe path: fix/confirm Tiny `codigo` for A rows, investigate alias/cadastro for B rows.
