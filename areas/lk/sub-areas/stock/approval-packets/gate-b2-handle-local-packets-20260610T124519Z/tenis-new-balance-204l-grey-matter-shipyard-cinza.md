# Gate B2 handle packet — tenis-new-balance-204l-grey-matter-shipyard-cinza

- título: Tênis New Balance 204L Grey Matter Shipyard Cinza
- prioridade: `P0_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `12`
- SKUs únicos: `12`
- priority_counts: `{'P0_saneamento': 12}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_SHOPIFY_DUPLICATE': 11}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `11` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `U204L86W`
- `U204L86W-1`
- `U204L86W-10`
- `U204L86W-11`
- `U204L86W-2`
- `U204L86W-3`
- `U204L86W-4`
- `U204L86W-5`
- `U204L86W-6`
- `U204L86W-7`
- `U204L86W-8`
- `U204L86W-9`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
