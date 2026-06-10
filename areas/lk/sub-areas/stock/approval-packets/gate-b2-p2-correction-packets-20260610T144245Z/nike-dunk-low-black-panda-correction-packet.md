# Gate B2 P2 — correction packet — nike-dunk-low-black-panda

- title: `Tênis Nike Dunk Low Black Panda 2.0 Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `DJ6188002, DJ6188002`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DJ6188002` | shopify_duplicate_sku_blocked | Shopify SKU `DJ6188002` | Tiny `DJ6188002` id `1069536324` | saldo LK CONTROLE: 0.0
- `DJ6188002-34-1` | tiny_duplicate_exact_code_blocked | Shopify SKU `DJ6188002-34-1` | Tiny `DJ6188002-34-1` id `937680739`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
