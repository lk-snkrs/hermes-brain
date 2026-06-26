# Gate B2 P2 — correction packet — tenis-nike-cortez-white-laser-fuchsia-branco

- title: `Tênis Nike Cortez White Laser Fuchsia Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `DM0950, DM0950, DM0950, DM0950, DM0950`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `DM0950` | shopify_variant_tiny_missing | Shopify SKU `DM0950` | Tiny `` id ``
- `DM0950-104` | shopify_duplicate_sku_blocked | Shopify SKU `DM0950-104` | Tiny `DM0950-104` id `1059489712`
- `DM0950-104-1` | matched_exact_sku_stock_resolved | Shopify SKU `DM0950-104-1` | Tiny `DM0950-104-1` id `1059489717` | saldo LK CONTROLE: 0.0
- `DM0950-104-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DM0950-104-2` | Tiny `DM0950-104-2` id `1059489720`
- `DM0950-104-3` | shopify_variant_tiny_missing | Shopify SKU `DM0950-104-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
