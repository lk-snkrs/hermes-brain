# Gate B2 handle packet — air-jordan-1-mid-wolf-grey

- título: Tênis Nike Air Jordan 1 Mid Wolf Grey Cinza
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `2`
- SKUs únicos: `2`
- priority_counts: `{'P2_saneamento': 2}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2}`
- issue_counts: `{'shopify_variant_tiny_missing': 2}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.

## SKUs amostra
- `BQ6472105-4`
- `BQ6472105-5`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
