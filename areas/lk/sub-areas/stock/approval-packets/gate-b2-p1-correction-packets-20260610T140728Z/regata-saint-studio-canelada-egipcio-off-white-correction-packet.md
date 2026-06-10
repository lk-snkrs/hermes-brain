# Gate B2 P1 — correction packet — regata-saint-studio-canelada-egipcio-off-white

- title: `Regata Saint Studio Canelada Egipcio Off White`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `ST27, ST27`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `ST27` | shopify_duplicate_sku_blocked | Shopify SKU `ST27` | Tiny `ST27` id `1061028449`
- `ST27-2` | tiny_duplicate_exact_code_blocked | Shopify SKU `ST27-2` | Tiny `ST27-2` id `1061480560`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
