# Gate B2 P2 — correction packet — nike-sb-dunk-low-vx-1000-camcorder

- title: `Tênis Nike SB Dunk Low VX 1000 Camcorder Cinza`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `CV1659001, CV1659001, CV1659001`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `CV1659001` | shopify_duplicate_sku_blocked | Shopify SKU `CV1659001` | Tiny `` id ``
- `CV1659001-2` | shopify_variant_tiny_missing | Shopify SKU `CV1659001-2` | Tiny `` id ``
- `CV1659001-1` | shopify_variant_tiny_missing | Shopify SKU `CV1659001-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
