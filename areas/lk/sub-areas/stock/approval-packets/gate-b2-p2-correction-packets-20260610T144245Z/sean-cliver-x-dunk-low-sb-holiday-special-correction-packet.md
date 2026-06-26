# Gate B2 P2 — correction packet — sean-cliver-x-dunk-low-sb-holiday-special

- title: `Tênis Sean Cliver x Dunk Low SB Holiday Special Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `DC9936100, DC9936100, DC9936100`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `DC9936100` | shopify_duplicate_sku_blocked | Shopify SKU `DC9936100` | Tiny `` id ``
- `DC9936100-34.5` | shopify_variant_tiny_missing | Shopify SKU `DC9936100-34.5` | Tiny `` id ``
- `DC9936-100-2` | shopify_variant_tiny_missing | Shopify SKU `DC9936-100-2` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
