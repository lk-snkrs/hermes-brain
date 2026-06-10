# Gate B2 P1 — correction packet — camiseta-kaws-x-uniqlo-warhol-ut-graphic-branco

- title: `Camiseta KAWS x Uniqlo Warhol UT Graphic 471321 Branco`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `471321, 471321, 471321`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `471321` | shopify_variant_tiny_missing | Shopify SKU `471321` | Tiny `` id ``
- `471321-3` | matched_exact_sku_stock_resolved | Shopify SKU `471321-3` | Tiny `471321-3` id `1068923723` | saldo LK CONTROLE: 5.0
- `471321-4` | tiny_duplicate_exact_code_blocked | Shopify SKU `471321-4` | Tiny `471321-4` id `1060764459`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
