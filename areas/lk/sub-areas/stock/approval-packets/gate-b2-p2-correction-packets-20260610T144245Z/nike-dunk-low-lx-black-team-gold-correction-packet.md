# Gate B2 P2 — correction packet — nike-dunk-low-lx-black-team-gold

- title: `Tênis Nike Dunk Low LX Black Team Gold Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DV3054001, DV3054001, DV3054001, DV3054001`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `DV3054001` | shopify_duplicate_sku_blocked | Shopify SKU `DV3054001` | Tiny `` id ``
- `DV3054001-5` | shopify_variant_tiny_missing | Shopify SKU `DV3054001-5` | Tiny `` id ``
- `DV3054001-2` | shopify_variant_tiny_missing | Shopify SKU `DV3054001-2` | Tiny `` id ``
- `DV3054001-3` | shopify_variant_tiny_missing | Shopify SKU `DV3054001-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
