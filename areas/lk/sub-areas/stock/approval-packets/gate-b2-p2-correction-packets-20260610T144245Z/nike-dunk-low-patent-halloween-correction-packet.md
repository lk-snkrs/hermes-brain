# Gate B2 P2 — correction packet — nike-dunk-low-patent-halloween

- title: `Tênis Nike Dunk Low Patent Halloween Laranja`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `DJ9955800, DJ9955800`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `DJ9955800` | shopify_duplicate_sku_blocked | Shopify SKU `DJ9955800` | Tiny `` id ``
- `DJ9955800-1` | shopify_variant_tiny_missing | Shopify SKU `DJ9955800-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
