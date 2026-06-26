# Gate B2 P2 — correction packet — jersey-off-white-x-nike-allover-print-kelly-green-verde

- title: `Jersey Off White x Nike "Allover Print Kelly Green" Verde`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `FQ0997, FQ0997, FQ0997, FQ0997-389, FQ0997-389`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `2`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `FQ0997` | shopify_variant_tiny_missing | Shopify SKU `FQ0997` | Tiny `` id ``
- `FQ0997-389` | shopify_duplicate_sku_blocked | Shopify SKU `FQ0997-389` | Tiny `FQ0997-389` id `1056164335`
- `FQ0997-389-1` | matched_exact_sku_stock_resolved | Shopify SKU `FQ0997-389-1` | Tiny `FQ0997-389-1` id `1056164401` | saldo LK CONTROLE: 0.0
- `FQ0997-389` | shopify_duplicate_sku_blocked | Shopify SKU `FQ0997-389` | Tiny `` id ``
- `FQ0997-389-1` | shopify_variant_tiny_missing | Shopify SKU `FQ0997-389-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
