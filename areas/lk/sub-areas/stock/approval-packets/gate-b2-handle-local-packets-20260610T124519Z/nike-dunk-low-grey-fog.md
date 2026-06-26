# Gate B2 handle packet — nike-dunk-low-grey-fog

- título: Tênis Nike Dunk Low Grey Fog Cinza
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `1`
- SKUs únicos: `1`
- priority_counts: `{'P2_saneamento': 1}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.

## SKUs amostra
- `DD1391103-3`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
