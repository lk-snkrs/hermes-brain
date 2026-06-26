# Gate B2 P2 — correction packet — tenis-air-jordan-1-high-og-sp-x-travis-scott-mocha

- title: `Tênis Nike Air Jordan 1 High Og Sp x Travis Scott Mocha`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `CD4487, CD4487, CD4487`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `CD4487` | shopify_variant_tiny_missing | Shopify SKU `CD4487` | Tiny `` id ``
- `CD4487-100` | shopify_duplicate_sku_blocked | Shopify SKU `CD4487-100` | Tiny `CD4487-100` id `1059843736` | saldo LK CONTROLE: 0.0
- `CD4487-100-1` | matched_exact_sku_stock_resolved | Shopify SKU `CD4487-100-1` | Tiny `CD4487-100-1` id `1060974639` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
