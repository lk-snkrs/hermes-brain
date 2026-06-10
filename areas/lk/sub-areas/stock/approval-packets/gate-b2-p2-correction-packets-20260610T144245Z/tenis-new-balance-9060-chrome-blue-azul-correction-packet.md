# Gate B2 P2 — correction packet — tenis-new-balance-9060-chrome-blue-azul

- title: `Tênis New Balance 9060 Chrome Blue Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `U9060EED, U9060EED, U9060EED, U9060EED, U9060EED, U9060EED`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `U9060EED` | shopify_duplicate_sku_blocked | Shopify SKU `U9060EED` | Tiny `U9060EED` id `1058347323` | saldo LK CONTROLE: 0.0
- `U9060EED-1` | matched_exact_sku_stock_missing_deposit | Shopify SKU `U9060EED-1` | Tiny `U9060EED-1` id `1058347329`
- `U9060EED-2` | shopify_variant_tiny_missing | Shopify SKU `U9060EED-2` | Tiny `` id ``
- `U9060EED-3` | shopify_variant_tiny_missing | Shopify SKU `U9060EED-3` | Tiny `` id ``
- `U9060EED-5` | shopify_variant_tiny_missing | Shopify SKU `U9060EED-5` | Tiny `` id ``
- `U9060EED-4` | shopify_variant_tiny_missing | Shopify SKU `U9060EED-4` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
