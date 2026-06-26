# Gate B2 P2 — correction packet — bolsa-minimal-saint-studio-cacto-caramelo

- title: `Bolsa Minimal Saint Studio Cacto Caramelo`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `35`
- prefixes: `ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4, ST4`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `17`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `16`

## Linhas principais
- `ST4` | shopify_variant_tiny_missing | Shopify SKU `ST4` | Tiny `` id ``
- `ST44-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST44-1` | Tiny `ST44-1` id `1063679628` | saldo LK CONTROLE: 0.0
- `ST45-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST45-1` | Tiny `ST45-1` id `1063679800` | saldo LK CONTROLE: 0.0
- `ST46-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST46-1` | Tiny `ST46-1` id `1063680110` | saldo LK CONTROLE: 0.0
- `ST47-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST47-1` | Tiny `ST47-1` id `1063680228` | saldo LK CONTROLE: 0.0
- `ST44-2` | matched_exact_sku_stock_resolved | Shopify SKU `ST44-2` | Tiny `ST44-2` id `1063679631` | saldo LK CONTROLE: 0.0
- `ST45-2` | matched_exact_sku_stock_resolved | Shopify SKU `ST45-2` | Tiny `ST45-2` id `1063679803` | saldo LK CONTROLE: 0.0
- `ST46-2` | shopify_variant_tiny_missing | Shopify SKU `ST46-2` | Tiny `` id ``
- `ST47-2` | shopify_variant_tiny_missing | Shopify SKU `ST47-2` | Tiny `` id ``
- `ST44-3` | shopify_variant_tiny_missing | Shopify SKU `ST44-3` | Tiny `` id ``
- `ST45-3` | shopify_variant_tiny_missing | Shopify SKU `ST45-3` | Tiny `` id ``
- `ST46-3` | shopify_variant_tiny_missing | Shopify SKU `ST46-3` | Tiny `` id ``
- `ST47-3` | shopify_variant_tiny_missing | Shopify SKU `ST47-3` | Tiny `` id ``
- `ST44-4` | matched_exact_sku_stock_resolved | Shopify SKU `ST44-4` | Tiny `ST44-4` id `1063679637` | saldo LK CONTROLE: 0.0
- `ST45-4` | matched_exact_sku_stock_resolved | Shopify SKU `ST45-4` | Tiny `ST45-4` id `1063679809` | saldo LK CONTROLE: 0.0
- `ST46-4` | matched_exact_sku_stock_resolved | Shopify SKU `ST46-4` | Tiny `ST46-4` id `1063680119` | saldo LK CONTROLE: 1.0
- `ST47-4` | matched_exact_sku_stock_resolved | Shopify SKU `ST47-4` | Tiny `ST47-4` id `1063680237` | saldo LK CONTROLE: 0.0
- `ST44-5` | matched_exact_sku_stock_resolved | Shopify SKU `ST44-5` | Tiny `ST44-5` id `1063679640` | saldo LK CONTROLE: 0.0
- `ST45-5` | matched_exact_sku_stock_resolved | Shopify SKU `ST45-5` | Tiny `ST45-5` id `1063679812` | saldo LK CONTROLE: -1.0
- `ST46-5` | shopify_variant_tiny_missing | Shopify SKU `ST46-5` | Tiny `` id ``
- `ST47-5` | shopify_variant_tiny_missing | Shopify SKU `ST47-5` | Tiny `` id ``
- `ST44-6` | shopify_variant_tiny_missing | Shopify SKU `ST44-6` | Tiny `` id ``
- `ST45-6` | shopify_variant_tiny_missing | Shopify SKU `ST45-6` | Tiny `` id ``
- `ST4-1` | shopify_duplicate_sku_blocked | Shopify SKU `ST4-1` | Tiny `` id ``
- `ST40` | shopify_variant_tiny_missing | Shopify SKU `ST40` | Tiny `` id ``
- `ST42-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST42-1` | Tiny `ST42-1` id `1063781322` | saldo LK CONTROLE: 0.0
- `ST42-2` | matched_exact_sku_stock_resolved | Shopify SKU `ST42-2` | Tiny `ST42-2` id `1063781325` | saldo LK CONTROLE: 0.0
- `ST43-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST43-1` | Tiny `ST43-1` id `1062538583` | saldo LK CONTROLE: 0.0
- `ST43-2` | matched_exact_sku_stock_resolved | Shopify SKU `ST43-2` | Tiny `ST43-2` id `1062538586` | saldo LK CONTROLE: 0.0
- `ST43-3` | matched_exact_sku_stock_resolved | Shopify SKU `ST43-3` | Tiny `ST43-3` id `1062538589` | saldo LK CONTROLE: 0.0
- `ST43-4` | matched_exact_sku_stock_missing_deposit | Shopify SKU `ST43-4` | Tiny `ST43-4` id `1062538592`
- `ST43-5` | shopify_variant_tiny_missing | Shopify SKU `ST43-5` | Tiny `` id ``
- `ST43-6` | shopify_variant_tiny_missing | Shopify SKU `ST43-6` | Tiny `` id ``
- `ST48` | shopify_variant_tiny_missing | Shopify SKU `ST48` | Tiny `` id ``
- `ST49` | shopify_variant_tiny_missing | Shopify SKU `ST49` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
