# Gate B2 handle packet — nike-sb-dunk-low-pro-classic-green

- título: Tênis Nike SB Dunk Low Pro Classic Green Verde
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P2_saneamento': 3}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2, 'BLOCKED_SHOPIFY_DUPLICATE': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 2, 'shopify_duplicate_sku_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `1` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `BQ6817302`
- `BQ6817302-3`
- `BQ6817302-4`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
