# Gate B2 P2 — correction packet — tenis-adidas-campus-00s-grey-three-cinza

- title: `Tênis Adidas Campus 00s Grey Three Cinza`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `HQ8707, HQ8707, HQ8707, HQ8707, HQ8707`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `HQ8707` | shopify_duplicate_sku_blocked | Shopify SKU `HQ8707` | Tiny `` id ``
- `HQ8707-4` | shopify_variant_tiny_missing | Shopify SKU `HQ8707-4` | Tiny `` id ``
- `HQ8707-1` | matched_exact_sku_stock_resolved | Shopify SKU `HQ8707-1` | Tiny `HQ8707-1` id `1056109406` | saldo LK CONTROLE: 0.0
- `HQ8707-2` | matched_exact_sku_stock_resolved | Shopify SKU `HQ8707-2` | Tiny `HQ8707-2` id `1056109409` | saldo LK CONTROLE: 0.0
- `HQ8707-3` | matched_exact_sku_stock_resolved | Shopify SKU `HQ8707-3` | Tiny `HQ8707-3` id `1056109412` | saldo LK CONTROLE: 2.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
