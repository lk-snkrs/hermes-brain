# Gate B2 P2 — correction packet — nike-sb-dunk-low-prm-paisley-brown

- title: `Tênis Nike SB Dunk Low PRM Paisley Brown Marrom`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `DH7534200, DH7534200`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `DH7534200` | shopify_duplicate_sku_blocked | Shopify SKU `DH7534200` | Tiny `` id ``
- `DH7534200-35-1` | shopify_variant_tiny_missing | Shopify SKU `DH7534200-35-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
