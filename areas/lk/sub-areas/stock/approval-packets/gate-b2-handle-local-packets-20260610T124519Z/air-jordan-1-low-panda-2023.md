# Gate B2 handle packet — air-jordan-1-low-panda-2023

- título: Tênis Nike Air Jordan 1 Low Panda (2023) Preto
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_DUPLICATE`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P1_saneamento': 3}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_TINY_DUPLICATE': 2}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 2}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `2` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `DC0774101`
- `DC0774101-14`
- `DC0774101-15`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
