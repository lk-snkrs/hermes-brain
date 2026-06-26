# Gate B2 P1 — correction packet — tenis-new-balance-9060-black-castlerock-grey-preto

- title: `Tênis New Balance 9060 Black Castlerock Grey Preto`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `U9060BLK, U9060BLK, U9060BLK, U9060BLK, U9060BLK, U9060BLK, U9060BLK`

## Status counts
- matched_exact_sku_stock_resolved: `2`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `U9060BLK` | shopify_duplicate_sku_blocked | Shopify SKU `U9060BLK` | Tiny `` id ``
- `U9060BLK-7` | shopify_variant_tiny_missing | Shopify SKU `U9060BLK-7` | Tiny `` id ``
- `U9060BLK-2` | shopify_variant_tiny_missing | Shopify SKU `U9060BLK-2` | Tiny `` id ``
- `U9060BLK-4` | shopify_variant_tiny_missing | Shopify SKU `U9060BLK-4` | Tiny `` id ``
- `U9060BLK-1` | matched_exact_sku_stock_resolved | Shopify SKU `U9060BLK-1` | Tiny `U9060BLK-1` id `1061142702` | saldo LK CONTROLE: 0.0
- `U9060BLK-5` | matched_exact_sku_stock_resolved | Shopify SKU `U9060BLK-5` | Tiny `U9060BLK-5` id `1064963180` | saldo LK CONTROLE: 0.0
- `U9060BLK-6` | tiny_duplicate_exact_code_blocked | Shopify SKU `U9060BLK-6` | Tiny `U9060BLK-6` id `1061142700`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
