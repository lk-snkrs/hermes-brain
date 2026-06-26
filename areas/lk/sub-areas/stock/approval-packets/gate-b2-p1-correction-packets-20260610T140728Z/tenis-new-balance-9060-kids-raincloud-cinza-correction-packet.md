# Gate B2 P1 — correction packet — tenis-new-balance-9060-kids-raincloud-cinza

- title: `Tênis New Balance 9060 Kids Raincloud Cinza (Infantil)`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `PC9060GY, PC9060GY, PC9060GY`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `PC9060GY` | shopify_duplicate_sku_blocked | Shopify SKU `PC9060GY` | Tiny `` id ``
- `PC9060GY-1` | shopify_variant_tiny_missing | Shopify SKU `PC9060GY-1` | Tiny `` id ``
- `PC9060GY-2` | tiny_duplicate_exact_code_blocked | Shopify SKU `PC9060GY-2` | Tiny `PC9060GY-2` id `1064258188`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
