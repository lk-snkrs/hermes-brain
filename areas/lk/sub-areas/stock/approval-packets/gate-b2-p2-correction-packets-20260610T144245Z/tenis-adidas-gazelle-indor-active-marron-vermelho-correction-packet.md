# Gate B2 P2 — correction packet — tenis-adidas-gazelle-indor-active-marron-vermelho

- title: `Tênis adidas Gazelle Indor "Active Maroon" Vermelho`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `12`
- prefixes: `IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734, IF9734`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `5`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `IF9734` | shopify_duplicate_sku_blocked | Shopify SKU `IF9734` | Tiny `IF9734` id `1058284942` | saldo LK CONTROLE: 0.0
- `IF9734-1` | matched_exact_sku_stock_resolved | Shopify SKU `IF9734-1` | Tiny `IF9734-1` id `1058284954` | saldo LK CONTROLE: 1.0
- `IF9734-2` | matched_exact_sku_stock_resolved | Shopify SKU `IF9734-2` | Tiny `IF9734-2` id `1058284957` | saldo LK CONTROLE: 1.0
- `IF9734-3` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IF9734-3` | Tiny `IF9734-3` id `1058284960`
- `IF9734-4` | shopify_variant_tiny_missing | Shopify SKU `IF9734-4` | Tiny `` id ``
- `IF9734-5` | shopify_variant_tiny_missing | Shopify SKU `IF9734-5` | Tiny `` id ``
- `IF9734-6` | shopify_variant_tiny_missing | Shopify SKU `IF9734-6` | Tiny `` id ``
- `IF9734-7` | shopify_variant_tiny_missing | Shopify SKU `IF9734-7` | Tiny `` id ``
- `IF9734-8` | shopify_variant_tiny_missing | Shopify SKU `IF9734-8` | Tiny `` id ``
- `IF9734-9` | matched_exact_sku_stock_resolved | Shopify SKU `IF9734-9` | Tiny `IF9734-9` id `1058284979` | saldo LK CONTROLE: 0.0
- `IF9734-10` | matched_exact_sku_stock_resolved | Shopify SKU `IF9734-10` | Tiny `IF9734-10` id `1058284982` | saldo LK CONTROLE: 0.0
- `IF9734-11` | matched_exact_sku_stock_resolved | Shopify SKU `IF9734-11` | Tiny `IF9734-11` id `1058284985` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
