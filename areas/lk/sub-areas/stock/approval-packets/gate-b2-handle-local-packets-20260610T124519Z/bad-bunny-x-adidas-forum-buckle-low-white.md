# Gate B2 handle packet — bad-bunny-x-adidas-forum-buckle-low-white

- título: Tênis Bad Bunny x adidas Forum Buckle Low White Branco
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P2_saneamento': 3}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 3}`
- issue_counts: `{'shopify_variant_tiny_missing': 3}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `3` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.

## SKUs amostra
- `HQ2153`
- `HQ2153-40`
- `HQ2153-40.5`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
