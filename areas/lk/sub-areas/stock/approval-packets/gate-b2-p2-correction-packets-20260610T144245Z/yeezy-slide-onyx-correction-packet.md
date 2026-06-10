# Gate B2 P2 — correction packet — yeezy-slide-onyx

- title: `Tênis Yeezy Slide Onyx Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `1`
- prefixes: `HQ6448`

## Status counts
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `HQ6448` | shopify_duplicate_sku_blocked | Shopify SKU `HQ6448` | Tiny `HQ6448` id `924625411`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
