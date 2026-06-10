# Gate B2 P2 — correction packet — tenis-nike-dunk-sb-x-verdy-visty-azul

- title: `Tênis Nike Dunk Sb x Verdy Visty Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `FN6040, FN6040, FN6040, FN6040, FN6040, FN6040, FN6040, FN6040, FN6040`

## Status counts
- matched_exact_sku_stock_resolved: `4`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `FN6040` | shopify_variant_tiny_missing | Shopify SKU `FN6040` | Tiny `` id ``
- `FN6040-400` | shopify_duplicate_sku_blocked | Shopify SKU `FN6040-400` | Tiny `` id ``
- `FN6040-400-1` | shopify_variant_tiny_missing | Shopify SKU `FN6040-400-1` | Tiny `` id ``
- `FN6040-400-2` | shopify_variant_tiny_missing | Shopify SKU `FN6040-400-2` | Tiny `` id ``
- `FN6040-400-3` | shopify_variant_tiny_missing | Shopify SKU `FN6040-400-3` | Tiny `` id ``
- `FN6040-400-4` | matched_exact_sku_stock_resolved | Shopify SKU `FN6040-400-4` | Tiny `FN6040-400-4` id `1059540224` | saldo LK CONTROLE: 0.0
- `FN6040-400-5` | matched_exact_sku_stock_resolved | Shopify SKU `FN6040-400-5` | Tiny `FN6040-400-5` id `1059540227` | saldo LK CONTROLE: 1.0
- `FN6040-400-6` | matched_exact_sku_stock_resolved | Shopify SKU `FN6040-400-6` | Tiny `FN6040-400-6` id `1061226835` | saldo LK CONTROLE: 0.0
- `FN6040-400-7` | matched_exact_sku_stock_resolved | Shopify SKU `FN6040-400-7` | Tiny `FN6040-400-7` id `1061226838` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
