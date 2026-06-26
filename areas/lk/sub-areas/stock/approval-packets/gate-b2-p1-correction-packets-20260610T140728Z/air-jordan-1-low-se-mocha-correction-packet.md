# Gate B2 P1 — correction packet — air-jordan-1-low-se-mocha

- title: `Tênis Nike Air Jordan 1 Low SE Mocha Marrom`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `11`
- prefixes: `DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200, DC6991200`

## Status counts
- matched_exact_sku_stock_resolved: `4`
- shopify_variant_tiny_missing: `6`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DC6991200` | shopify_variant_tiny_missing | Shopify SKU `DC6991200` | Tiny `` id ``
- `DC6991200-16` | matched_exact_sku_stock_resolved | Shopify SKU `DC6991200-16` | Tiny `DC6991200-16` id `1055988779` | saldo LK CONTROLE: 0.0
- `DC6991200-15` | tiny_duplicate_exact_code_blocked | Shopify SKU `DC6991200-15` | Tiny `DC6991200-15` id `925682194`
- `DC6991200-1` | shopify_variant_tiny_missing | Shopify SKU `DC6991200-1` | Tiny `` id ``
- `DC6991200-38` | shopify_variant_tiny_missing | Shopify SKU `DC6991200-38` | Tiny `` id ``
- `DC6991200-3` | shopify_variant_tiny_missing | Shopify SKU `DC6991200-3` | Tiny `` id ``
- `DC6991200-4` | shopify_variant_tiny_missing | Shopify SKU `DC6991200-4` | Tiny `` id ``
- `DC6991200-5` | shopify_variant_tiny_missing | Shopify SKU `DC6991200-5` | Tiny `` id ``
- `DC6991200-42` | matched_exact_sku_stock_resolved | Shopify SKU `DC6991200-42` | Tiny `DC6991200-42` id `925682131` | saldo LK CONTROLE: 1.0
- `DC6991200-43` | matched_exact_sku_stock_resolved | Shopify SKU `DC6991200-43` | Tiny `DC6991200-43` id `925682138` | saldo LK CONTROLE: 1.0
- `DC6991200-44` | matched_exact_sku_stock_resolved | Shopify SKU `DC6991200-44` | Tiny `DC6991200-44` id `925682144` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
