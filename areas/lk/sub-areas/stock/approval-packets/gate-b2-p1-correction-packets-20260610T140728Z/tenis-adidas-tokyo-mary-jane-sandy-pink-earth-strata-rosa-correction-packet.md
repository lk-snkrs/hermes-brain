# Gate B2 P1 — correction packet — tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa

- title: `Tênis Adidas Tokyo Mary Jane Sandy Pink Earth Strata Rosa`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `IH4000, IH4000, IH4000, IH4000, IH4000, IH4000`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `2`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `IH4000` | shopify_variant_tiny_missing | Shopify SKU `IH4000` | Tiny `` id ``
- `IH4000-35` | shopify_duplicate_sku_blocked | Shopify SKU `IH4000-35` | Tiny `` id ``
- `IH4000-36` | shopify_duplicate_sku_blocked | Shopify SKU `IH4000-36` | Tiny `` id ``
- `IH4000-37` | shopify_variant_tiny_missing | Shopify SKU `IH4000-37` | Tiny `` id ``
- `IH4000-38` | shopify_variant_tiny_missing | Shopify SKU `IH4000-38` | Tiny `` id ``
- `IH4000-39` | matched_exact_sku_stock_resolved | Shopify SKU `IH4000-39` | Tiny `IH4000-39` id `1070120463` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
