# Gate B2 P2 — correction packet — air-jordan-1-high-dark-mocha

- title: `Tênis Nike Air Jordan 1 High Dark Mocha Marrom`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `555088105, 555088105, 555088105, 555088105`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `555088105` | shopify_duplicate_sku_blocked | Shopify SKU `555088105` | Tiny `` id ``
- `555088105-35` | matched_exact_sku_stock_resolved | Shopify SKU `555088105-35` | Tiny `555088105-35` id `924630284` | saldo LK CONTROLE: 0.0
- `555088105-39` | matched_exact_sku_stock_resolved | Shopify SKU `555088105-39` | Tiny `555088105-39` id `924630341` | saldo LK CONTROLE: 0.0
- `555088105-42` | matched_exact_sku_stock_resolved | Shopify SKU `555088105-42` | Tiny `555088105-42` id `924630365` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
