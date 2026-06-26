# Gate B2 P2 — correction packet — nike-sb-dunk-low-elephant

- title: `Tênis Nike SB Dunk Low Elephant Colorido`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `BQ6817009, BQ6817009`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `BQ6817009` | shopify_duplicate_sku_blocked | Shopify SKU `BQ6817009` | Tiny `` id ``
- `BQ6817009-35` | shopify_variant_tiny_missing | Shopify SKU `BQ6817009-35` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
