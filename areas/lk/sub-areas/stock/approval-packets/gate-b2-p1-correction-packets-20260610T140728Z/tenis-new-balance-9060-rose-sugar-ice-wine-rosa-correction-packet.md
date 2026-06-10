# Gate B2 P1 — correction packet — tenis-new-balance-9060-rose-sugar-ice-wine-rosa

- title: `Tênis New Balance 9060 Rose Sugar Angora Rosa`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `U9060LBC, U9060LBC, U9060LBC, U9060LBC, U9060LBC, U9060LBC, U9060LBC, U9060LBC`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `3`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `U9060LBC` | shopify_variant_tiny_missing | Shopify SKU `U9060LBC` | Tiny `` id ``
- `U9060LBC-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `U9060LBC-2` | Tiny `U9060LBC-2` id `1066075274`
- `U9060LBC-3` | shopify_variant_tiny_missing | Shopify SKU `U9060LBC-3` | Tiny `` id ``
- `U9060LBC-4` | shopify_variant_tiny_missing | Shopify SKU `U9060LBC-4` | Tiny `` id ``
- `U9060LBC-5` | matched_exact_sku_stock_resolved | Shopify SKU `U9060LBC-5` | Tiny `U9060LBC-5` id `1066075283` | saldo LK CONTROLE: 1.0
- `U9060LBC-6` | matched_exact_sku_stock_resolved | Shopify SKU `U9060LBC-6` | Tiny `U9060LBC-6` id `1066075286` | saldo LK CONTROLE: 1.0
- `U9060LBC-7` | tiny_duplicate_exact_code_blocked | Shopify SKU `U9060LBC-7` | Tiny `U9060LBC-7` id `1066075151`
- `U9060LBC-8` | matched_exact_sku_stock_resolved | Shopify SKU `U9060LBC-8` | Tiny `U9060LBC-8` id `1066075292` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
