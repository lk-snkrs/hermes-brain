# Gate B2 P2 — correction packet — moletom-represent-clo-masking-tape-initial-cedar-marrom

- title: `Moletom Represent Clo Masking Tape Initial Cedar Marrom`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `1`
- prefixes: `Rep01`

## Status counts
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `Rep01` | shopify_duplicate_sku_blocked | Shopify SKU `Rep01` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
