# Gate B2 P2 — correction packet — air-jordan-1-mid-aqua-blue-tint

- title: `Tênis Nike Air Jordan 1 Mid Aqua Blue Tint Verde`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `BQ6472303, BQ6472303`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `BQ6472303` | shopify_duplicate_sku_blocked | Shopify SKU `BQ6472303` | Tiny `` id ``
- `BQ6472303-2` | matched_exact_sku_stock_resolved | Shopify SKU `BQ6472303-2` | Tiny `BQ6472303-2` id `1066244823` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
