# Gate B2 handle packet — tenis-air-jordan-1-low-lucky-green-verde

- título: Tênis Nike Air Jordan 1 Low Lucky Green Verde
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `7`
- SKUs únicos: `7`
- priority_counts: `{'P1_saneamento': 7}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_SHOPIFY_DUPLICATE': 6}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 6}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `6` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `553558065-1`
- `DC0774304-10`
- `DC0774304-2`
- `DC0774304-3`
- `DC0774304-5`
- `DC0774304-6`
- `DC0774304-8`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
