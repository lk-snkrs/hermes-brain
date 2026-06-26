# Gate B2 P2 — correction packet — air-jordan-1-mid-se-french-blue

- title: `Tênis Nike Air Jordan 1 Mid SE French Blue Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DN3706401, DN3706401, DN3706401, DN3706401`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `DN3706401` | shopify_duplicate_sku_blocked | Shopify SKU `DN3706401` | Tiny `` id ``
- `DN3706401-4` | shopify_variant_tiny_missing | Shopify SKU `DN3706401-4` | Tiny `` id ``
- `DN3706401-1` | shopify_variant_tiny_missing | Shopify SKU `DN3706401-1` | Tiny `` id ``
- `DN3706401-2` | matched_exact_sku_stock_resolved | Shopify SKU `DN3706401-2` | Tiny `DN3706401-2` id `1000040400` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
