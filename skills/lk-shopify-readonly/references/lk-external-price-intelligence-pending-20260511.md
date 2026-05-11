# LK external price intelligence for sourcing — pending/later — 2026-05-11

## Trigger

Use this reference when Lucas reopens LK Fila A sourcing/reposição and asks for market price, cheapest source, Droper/StockX/GOAT comparison, or whether a product is worth importing.

## Status

Pending/later by Lucas decision. Do **not** run this automatically after building a Fila A preview, and do **not** contact suppliers or purchase. It is a future read-only price-intelligence layer that should happen before any supplier-contact quote.

## User correction captured

Lucas clarified that the useful feature is not merely preparing a supplier quote brief. The intended sourcing intelligence is:

1. Search Droper, StockX, and GOAT for the product and exact size.
2. Normalize sizes, especially StockX/GOAT US sizing.
3. Calculate estimated landed/import cost for international sources.
4. Return the cheapest viable option.
5. Keep everything pending/preview until explicit approval.

## Required source logic

- **Droper**: Brazil/local price and availability. Compare as local BRL price, with local lead time/risk.
- **StockX**: international price by size. Treat displayed size carefully: often US, and can be US Men or US Women.
- **GOAT**: international price by size and product reference. Same US Men/Women caution as StockX.

Do not compare sources unless product identity and size mapping are explicit. If mapping is uncertain, mark it as uncertain instead of choosing a winner.

## Size-normalization requirement

For each StockX/GOAT candidate record:

- Capture listing size exactly as displayed.
- Capture whether the sizing scale is US Men, US Women, GS/Y, EU, UK, or unknown.
- Convert to LK target size (BR/EU) only after identifying the scale.
- Women’s US sizing is not interchangeable with Men’s US sizing. A US W listing must not be treated as US M.
- If the product has women-specific or unisex sizing, document the assumption.

Output should show:

```text
LK target size: 38 BR/EU-equivalent
Source size: US W 8.5 (example)
Normalization confidence: medium/high/low
Reason: product/category sizing scale observed on source
```

## LK import cost formula

For StockX/GOAT USD pricing, apply the existing LK formula:

```text
preco_base = (preco_usd + custo_trazer_usd) × (dolar_atual × 1.05) × 2
preco_lk = arredondamento LK para final 49,99 ou 99,99 quando the task is pricing, not just sourcing cost
```

For sourcing comparison, call the result `estimated_landed_cost_brl` or `custo final estimado`, not final selling price unless Lucas asks for PDP/pricing.

## Cheapest viable option definition

Cheapest viable is not automatically the lowest sticker price. It should consider:

- exact product match;
- exact/normalized size match;
- estimated landed cost in BRL;
- lead time;
- source reliability/authenticity risk;
- local availability vs import delay;
- whether the item remains below the margin/cost cap from Fila A.

## Recommended output shape

For each SKU/tamanho:

- Product/SKU/size requested.
- Source candidates:
  - Droper local price/status.
  - StockX normalized size + USD price + landed BRL estimate.
  - GOAT normalized size + USD price + landed BRL estimate.
- Cheapest viable source.
- Confidence/risk.
- Recommendation: buy / do not buy / monitor / ask Lucas/Júlio / needs manual size confirmation.
- Explicit non-actions: no purchase, no supplier contact, no Shopify/Tiny write.

## Pitfalls

1. **Comparing US W and US M as if they are the same.** Always identify sizing scale before mapping.
2. **Choosing sticker price instead of landed cost.** International sources need import formula and FX buffer.
3. **Treating pending as approved.** Lucas intentionally parked this feature for later.
4. **Using marketplace data as product truth without SKU/size confidence.** Low-confidence matching must route to manual review.
