# Gate B2 handle packet — adi2000-triple-black

- título: Tênis ADI2000 Triple Black Preto
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
- `GX4634`
- `GX4634-43`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
