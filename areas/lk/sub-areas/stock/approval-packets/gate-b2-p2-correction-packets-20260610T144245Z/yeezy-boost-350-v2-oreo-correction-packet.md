# Gate B2 P2 — correction packet — yeezy-boost-350-v2-oreo

- title: `Tênis Yeezy Boost 350 V2 Oreo Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `BY1604, BY1604, BY1604, BY1604, BY1604, BY1604`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `BY1604` | shopify_duplicate_sku_blocked | Shopify SKU `BY1604` | Tiny `` id ``
- `BY1604-1` | shopify_variant_tiny_missing | Shopify SKU `BY1604-1` | Tiny `` id ``
- `BY1604-2` | shopify_variant_tiny_missing | Shopify SKU `BY1604-2` | Tiny `` id ``
- `BY1604-3` | matched_exact_sku_stock_resolved | Shopify SKU `BY1604-3` | Tiny `BY1604-3` id `1056209477` | saldo LK CONTROLE: 0.0
- `BY1604-4` | matched_exact_sku_stock_resolved | Shopify SKU `BY1604-4` | Tiny `BY1604-4` id `1056209480` | saldo LK CONTROLE: 0.0
- `BY1604-5` | matched_exact_sku_stock_resolved | Shopify SKU `BY1604-5` | Tiny `BY1604-5` id `1056209483` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
