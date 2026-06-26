# Gate B2 P2 — correction packet — nike-dunk-low-team-red

- title: `Tênis Nike Dunk Low Team Red Vermelho`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `DD1391601, DD1391601`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `DD1391601` | shopify_duplicate_sku_blocked | Shopify SKU `DD1391601` | Tiny `` id ``
- `DD1391601-1` | shopify_variant_tiny_missing | Shopify SKU `DD1391601-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
