# Gate B2 P1 — correction packet — tenis-adidas-gazelle-x-bad-bunny-core-white-bege

- title: `Tênis adidas Gazelle x Bad Bunny Core White Bege`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `10`
- prefixes: `IF9735, IF9735, IF9735, IF9735, IF9735, IF9735, IF9735, IF9735, IF9735, IF9735`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `5`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `IF9735` | shopify_variant_tiny_missing | Shopify SKU `IF9735` | Tiny `` id ``
- `IF9735-9` | tiny_duplicate_exact_code_blocked | Shopify SKU `IF9735-9` | Tiny `IF9735-9` id `1058875484`
- `IF9735-1` | matched_exact_sku_stock_resolved | Shopify SKU `IF9735-1` | Tiny `IF9735-1` id `1058875493` | saldo LK CONTROLE: 0.0
- `IF9735-2` | matched_exact_sku_stock_resolved | Shopify SKU `IF9735-2` | Tiny `IF9735-2` id `1058875496` | saldo LK CONTROLE: 0.0
- `IF9735-3` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IF9735-3` | Tiny `IF9735-3` id `1058875499`
- `IF9735-4` | shopify_variant_tiny_missing | Shopify SKU `IF9735-4` | Tiny `` id ``
- `IF9735-5` | shopify_variant_tiny_missing | Shopify SKU `IF9735-5` | Tiny `` id ``
- `IF9735-6` | shopify_variant_tiny_missing | Shopify SKU `IF9735-6` | Tiny `` id ``
- `IF9735-7` | shopify_variant_tiny_missing | Shopify SKU `IF9735-7` | Tiny `` id ``
- `IF9735-8` | matched_exact_sku_stock_resolved | Shopify SKU `IF9735-8` | Tiny `IF9735-8` id `1058875514` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
