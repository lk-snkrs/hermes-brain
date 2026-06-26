# Gate B2 P2 — correction packet — tenis-new-balance-9060-olivine-verde

- title: `Tênis New Balance 9060 Olivine Verde`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `U9060EEC, U9060EEC, U9060EEC, U9060EEC, U9060EEC, U9060EEC, U9060EEC, U9060EEC, U9060EEC`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `4`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `U9060EEC` | shopify_duplicate_sku_blocked | Shopify SKU `U9060EEC` | Tiny `U9060EEC` id `1061050426` | saldo LK CONTROLE: 0.0
- `U9060EEC-1` | matched_exact_sku_stock_resolved | Shopify SKU `U9060EEC-1` | Tiny `U9060EEC-1` id `1061050434` | saldo LK CONTROLE: 0.0
- `U9060EEC-2` | matched_exact_sku_stock_resolved | Shopify SKU `U9060EEC-2` | Tiny `U9060EEC-2` id `1061050437` | saldo LK CONTROLE: 0.0
- `U9060EEC-3` | matched_exact_sku_stock_resolved | Shopify SKU `U9060EEC-3` | Tiny `U9060EEC-3` id `1061050440` | saldo LK CONTROLE: 0.0
- `U9060EEC-4` | matched_exact_sku_stock_resolved | Shopify SKU `U9060EEC-4` | Tiny `U9060EEC-4` id `1061050443` | saldo LK CONTROLE: 0.0
- `U9060EEC-5` | matched_exact_sku_stock_missing_deposit | Shopify SKU `U9060EEC-5` | Tiny `U9060EEC-5` id `1061050446`
- `U9060EEC-6` | shopify_variant_tiny_missing | Shopify SKU `U9060EEC-6` | Tiny `` id ``
- `U9060EEC-7` | shopify_variant_tiny_missing | Shopify SKU `U9060EEC-7` | Tiny `` id ``
- `U9060EEC-8` | shopify_variant_tiny_missing | Shopify SKU `U9060EEC-8` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
