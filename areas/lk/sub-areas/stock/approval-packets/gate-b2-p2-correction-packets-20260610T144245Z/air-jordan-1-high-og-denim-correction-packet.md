# Gate B2 P2 — correction packet — air-jordan-1-high-og-denim

- title: `Tênis Nike Air Jordan 1 High OG Denim Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `FQ2947-100, FQ2947-100, FQ2947-100, FQ2947-100, FQ2947-100, FQ2947-100`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `FQ2947-100` | matched_exact_sku_stock_missing_deposit | Shopify SKU `FQ2947-100` | Tiny `FQ2947-100` id `1058666755`
- `FQ2947-100-1` | shopify_duplicate_sku_blocked | Shopify SKU `FQ2947-100-1` | Tiny `` id ``
- `FQ2947-100-3` | shopify_variant_tiny_missing | Shopify SKU `FQ2947-100-3` | Tiny `` id ``
- `FQ2947-100-4` | matched_exact_sku_stock_resolved | Shopify SKU `FQ2947-100-4` | Tiny `FQ2947-100-4` id `1058666774` | saldo LK CONTROLE: 0.0
- `FQ2947-100-6` | matched_exact_sku_stock_resolved | Shopify SKU `FQ2947-100-6` | Tiny `FQ2947-100-6` id `1058666780` | saldo LK CONTROLE: 0.0
- `FQ2947-100-7` | matched_exact_sku_stock_resolved | Shopify SKU `FQ2947-100-7` | Tiny `FQ2947-100-7` id `1058666783` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
