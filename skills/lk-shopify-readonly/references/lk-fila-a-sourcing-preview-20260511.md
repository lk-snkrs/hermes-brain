# LK Fila A sourcing preview after SKU saneamento — 2026-05-11

## When to use

Use when LK Stock Intelligence has finished the safe part of Fila B SKU/Tiny saneamento and Lucas wants to move to the next LK OS stage: commercial sourcing/reposição prioritization.

## Session learning

After P0 SKU/Tiny cleanup, Lucas explicitly chose to leave the remaining low-sales/ambiguous products in stand-by instead of blocking the whole LK OS:

- Mark blocked residual rows as `pending_low_sales_manual_fix_later`.
- Treat them as pending/stand-by, not as failed sourcing candidates.
- Exclude them from Fila A sourcing/reposition recommendations until Lucas/Júlio reopen manual code resolution.

This allowed the LK OS to move from technical saneamento (Fila B) to a read-only commercial preview (Fila A) without unsafe writes.

## Correct sequence

1. Confirm Fila B status:
   - safe SKU/Tiny writes completed and verified;
   - remaining rows are either resolved or intentionally marked pending;
   - no ambiguous/no-code rows are accidentally entering commercial recommendations.
2. Build Fila A from the saneamento/sales/stock report, aggregating by real SKU + size/Tiny code where available.
3. Filter out rows marked `pending_low_sales_manual_fix_later` or equivalent manual-review hold.
4. Produce a sourcing preview only:
   - rank by rupture, repeated orders/sales, sell-through, and current stock;
   - aggregate by SKU/tamanho instead of influencer/ad-specific fragments;
   - include confidence and why the item is actionable.
5. Save both business-readable Markdown and machine-readable JSON/CSV reports in the Brain repo.
6. Keep all next actions as recommendations until Lucas approves supplier contact, purchase/cotação, or any write.

## Output shape

For Lucas, report:

- status of residual P0 items: how many completed, how many pending/stand-by;
- Fila A universe count and top executive shortlist;
- top SKUs with product, size, Tiny/Shopify SKU, stock, repeated demand, and recommended action;
- explicit non-actions: no Shopify write, no Tiny write, no supplier contact, no purchase, no campaign;
- next safe options: validate lead time/margem/fornecedor internally, or prepare a cotação brief for approval.

## Guardrails

- Fila A is read-only commercial intelligence unless Lucas approves execution.
- Do not contact suppliers or make purchases from a preview.
- Do not infer stock truth from Shopify alone; use Tiny/stock reports as the inventory source.
- If a high-demand item still lacks SKU truth, keep it out of sourcing and route back to Fila B/manual code resolution.
- Low-sales ambiguous products can be deliberately placed in stand-by by Lucas; document the decision and move on.
- Lucas explicitly marked the external price-source feature as **pending/later**: do not run it automatically now.

## Pending next feature — external price intelligence

Lucas liked the sourcing feature but corrected the direction: before any supplier-contact quote, a future version should query/compare external price sources and return the cheapest viable option. Detailed workflow lives in `references/lk-external-price-intelligence-pending-20260511.md`.

Required sources/order:

- Droper for Brazil/local availability and price.
- StockX for international market price.
- GOAT for international market price and sometimes better product/photo reference.

Required intelligence:

- Compare by exact product and size, not only model name.
- StockX and GOAT often expose sizes as US sizing, and may use US Men or US Women depending on product/category. Normalize size system before comparing to LK BR/EU size.
- Return the cheapest viable landed-cost option, not simply the cheapest sticker price.
- Apply LK international cost formula when using StockX/GOAT: `(preco_usd + custo_trazer_usd) × (dolar_atual × 1.05) × 2`, then compare with Droper/local alternatives.
- Keep output as preview/pending: no purchase, no supplier contact, no Shopify/Tiny write without explicit approval.

## Example labels

- Stand-by status: `pending_low_sales_manual_fix_later`.
- Report names: `lk-os-next-stage-fila-a-sourcing-preview-YYYY-MM-DD.md/json/csv`.
- Recommended action wording: “validar fornecedor/lead time/margem” or “preparar brief de cotação”, not “comprar” unless approved.
