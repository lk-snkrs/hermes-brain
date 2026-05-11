# LK Fila A validation + quote preview — 2026-05-11

## When to use

Use after the Fila A sourcing/reposição preview is built and Lucas approves moving forward with:

1. internal validation of supplier/lead time/margin; and
2. a quotation queue/brief for suppliers.

This is still a **read-only / preview** workflow until Lucas explicitly approves supplier contact, purchase, PO, Shopify/Tiny writes, pricing/stock changes, or campaign/customer actions.

## Session learning

Lucas approved both next safe options at once (“seguir 1 e 2”). The correct response was not to contact suppliers; it was to convert the Fila A Top 15 into a decision-ready internal validation and quote brief.

Key distinction:

- **Quote quantity** = reference quantity to ask availability/price from suppliers.
- **Purchase quantity** = not approved and must not be implied.

## Workflow

1. Load the existing Fila A sourcing preview JSON/MD.
2. Keep pending/stand-by residual SKU rows excluded.
3. For the Top 15, compute internal validation fields:
   - average sale price signal = `revenue / qty`;
   - cost ceiling for target gross margins, e.g. 45%, 50%, 55%;
   - Tiny stock signal;
   - priority/risk notes;
   - quote reference quantity.
4. Do not invent real costs, real suppliers, or real margins if not present in the Brain/source data. Label these as pending supplier/cost validation.
5. Apply lead-time gates:
   - P0: approve only if ready-stock or lead time <= 7 days;
   - 8–15 days: require Lucas/Júlio decision;
   - >15 days: not recommended without pre-sale or explicit decision;
   - P1: optional/bundle only, unless Lucas upgrades priority.
6. Group quotation items by model/family to make supplier requests legible.
7. Write both human-readable MD and machine-readable JSON/CSV reports.
8. Index the new routine in `empresa/rotinas/_index.md`.
9. Run `git diff --check` and `python3 scripts/brain_health_check.py`.
10. Version through PR/merge; do not push directly to protected main.

## Output shape

For Lucas, summarize:

- Top items validated count;
- P0/P1 split;
- quote groups by family/model;
- total reference quote quantity;
- explicit non-actions: no supplier contact, no purchase/PO, no Shopify/Tiny write, no price/stock/campaign/send;
- files written and PR/merge/check status.

## Guardrails / pitfalls

- Never call quote reference quantity a buying recommendation.
- Never infer supplier availability, cost or lead time from sales data.
- Never send the brief externally without explicit approval naming destination/scope.
- If costs are unavailable, use cost ceilings for margin targets rather than claiming actual margin.
- If an item is high ticket, include risk notes against overbuying without current demand and margin confirmation.
- Keep the six low-sales residual P0/pending items out of sourcing unless Lucas/Júlio reopens manual SKU/cadastro resolution.

## Artifact naming

Recommended names:

- `areas/lk/rotinas/lk-fila-a-sourcing-validation-and-quote-preview-YYYY-MM-DD.md`
- `reports/lk-fila-a-sourcing-validation-and-quote-preview-YYYY-MM-DD.json`
- `reports/lk-fila-a-sourcing-validation-and-quote-preview-YYYY-MM-DD.csv`
