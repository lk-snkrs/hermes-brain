# Gate B2 P2 — correction packet — nike-dunk-low-polar-blue

- title: `Tênis Nike Dunk Low Polar Blue Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `DV0833400, DV0833400, DV0833400, DV0833400, DV0833400, DV0833400, DV0833400`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `2`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `DV0833400` | shopify_duplicate_sku_blocked | Shopify SKU `DV0833400` | Tiny `DV0833400` id `1054455147` | saldo LK CONTROLE: 0.0
- `DV0833400-1` | matched_exact_sku_stock_resolved | Shopify SKU `DV0833400-1` | Tiny `DV0833400-1` id `1054455263` | saldo LK CONTROLE: 0.0
- `DV0833400-7` | matched_exact_sku_stock_resolved | Shopify SKU `DV0833400-7` | Tiny `DV0833400-7` id `1055418152` | saldo LK CONTROLE: 0.0
- `DV0833400-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DV0833400-2` | Tiny `DV0833400-2` id `1054455266`
- `DV0833400-3` | shopify_variant_tiny_missing | Shopify SKU `DV0833400-3` | Tiny `` id ``
- `DV0833400-4` | shopify_variant_tiny_missing | Shopify SKU `DV0833400-4` | Tiny `` id ``
- `DV0833400-5` | shopify_variant_tiny_missing | Shopify SKU `DV0833400-5` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
