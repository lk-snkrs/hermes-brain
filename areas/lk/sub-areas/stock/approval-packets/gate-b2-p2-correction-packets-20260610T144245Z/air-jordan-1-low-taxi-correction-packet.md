# Gate B2 P2 — correction packet — air-jordan-1-low-taxi

- title: `Tênis Nike Air Jordan 1 Low Taxi Amarelo`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `553558701, 553558701, 553558701`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `553558701` | shopify_duplicate_sku_blocked | Shopify SKU `553558701` | Tiny `` id ``
- `553558701-1` | shopify_variant_tiny_missing | Shopify SKU `553558701-1` | Tiny `` id ``
- `553558701-2` | matched_exact_sku_stock_resolved | Shopify SKU `553558701-2` | Tiny `553558701-2` id `926167208` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
