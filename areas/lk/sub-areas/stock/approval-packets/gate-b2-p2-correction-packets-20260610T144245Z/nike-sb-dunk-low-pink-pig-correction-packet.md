# Gate B2 P2 — correction packet — nike-sb-dunk-low-pink-pig

- title: `Tênis Nike SB Dunk Low Pink Pig Rosa`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `CV1655600, CV1655600, CV1655600, CV1655600, CV1655600`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `CV1655600` | shopify_duplicate_sku_blocked | Shopify SKU `CV1655600` | Tiny `CV1655600` id `957827003` | saldo LK CONTROLE: 0.0
- `CV1655600-1` | matched_exact_sku_stock_resolved | Shopify SKU `CV1655600-1` | Tiny `CV1655600-1` id `957827036` | saldo LK CONTROLE: 0.0
- `CV1655600-4` | matched_exact_sku_stock_missing_deposit | Shopify SKU `CV1655600-4` | Tiny `CV1655600-4` id `957827069`
- `CV1655600-2` | shopify_variant_tiny_missing | Shopify SKU `CV1655600-2` | Tiny `` id ``
- `CV1655600-3` | shopify_variant_tiny_missing | Shopify SKU `CV1655600-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
