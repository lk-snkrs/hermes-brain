# Gate B2 P2 — correction packet — tenis-new-balance-9060-nori-verde

- title: `Tênis New Balance 9060 Nori Verde`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `U9060VNG, U9060VNG, U9060VNG, U9060VNG, U9060VNG, U9060VNG, U9060VNG, U9060VNG`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `U9060VNG` | shopify_duplicate_sku_blocked | Shopify SKU `U9060VNG` | Tiny `U9060VNG` id `1057764823`
- `U9060VNG-7` | shopify_variant_tiny_missing | Shopify SKU `U9060VNG-7` | Tiny `` id ``
- `U9060VNG-1` | shopify_variant_tiny_missing | Shopify SKU `U9060VNG-1` | Tiny `` id ``
- `U9060VNG-2` | shopify_variant_tiny_missing | Shopify SKU `U9060VNG-2` | Tiny `` id ``
- `U9060VNG-3` | shopify_variant_tiny_missing | Shopify SKU `U9060VNG-3` | Tiny `` id ``
- `U9060VNG-4` | matched_exact_sku_stock_resolved | Shopify SKU `U9060VNG-4` | Tiny `U9060VNG-4` id `1057764839` | saldo LK CONTROLE: 0.0
- `U9060VNG-5` | matched_exact_sku_stock_resolved | Shopify SKU `U9060VNG-5` | Tiny `U9060VNG-5` id `1057764842` | saldo LK CONTROLE: 0.0
- `U9060VNG-6` | matched_exact_sku_stock_resolved | Shopify SKU `U9060VNG-6` | Tiny `U9060VNG-6` id `1057764845` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
