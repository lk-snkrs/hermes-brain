# Gate B2 P2 — correction packet — camiseta-boxy-saint-studio-supima-preto

- title: `Camiseta Boxy Saint Studio Supima Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `1`
- prefixes: `ST33`

## Status counts
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `ST33` | shopify_duplicate_sku_blocked | Shopify SKU `ST33` | Tiny `ST33` id `1061480011`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
