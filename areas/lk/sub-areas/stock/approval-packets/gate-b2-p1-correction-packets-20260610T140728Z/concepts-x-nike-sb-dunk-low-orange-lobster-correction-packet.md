# Gate B2 P1 — correction packet — concepts-x-nike-sb-dunk-low-orange-lobster

- title: `Tênis Concepts x Nike SB Dunk Low Orange Lobster Laranja`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `FD8776800, FD8776800, FD8776800, FD8776800, FD8776800, FD8776800, FD8776800, FD8776800, FD8776800`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `5`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `FD8776800` | shopify_variant_tiny_missing | Shopify SKU `FD8776800` | Tiny `` id ``
- `FD8776800-34` | shopify_variant_tiny_missing | Shopify SKU `FD8776800-34` | Tiny `` id ``
- `FD8776800-35` | shopify_variant_tiny_missing | Shopify SKU `FD8776800-35` | Tiny `` id ``
- `FD8776800-36` | shopify_variant_tiny_missing | Shopify SKU `FD8776800-36` | Tiny `` id ``
- `FD8776800-37` | shopify_variant_tiny_missing | Shopify SKU `FD8776800-37` | Tiny `` id ``
- `FD8776800-38` | matched_exact_sku_stock_resolved | Shopify SKU `FD8776800-38` | Tiny `FD8776800-38` id `924562806` | saldo LK CONTROLE: 0.0
- `FD8776800-39` | matched_exact_sku_stock_resolved | Shopify SKU `FD8776800-39` | Tiny `FD8776800-39` id `924562814` | saldo LK CONTROLE: 0.0
- `FD8776800-8` | tiny_duplicate_exact_code_blocked | Shopify SKU `FD8776800-8` | Tiny `FD8776800-8` id `962647589`
- `FD8776800-41` | matched_exact_sku_stock_resolved | Shopify SKU `FD8776800-41` | Tiny `FD8776800-41` id `924562834` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
