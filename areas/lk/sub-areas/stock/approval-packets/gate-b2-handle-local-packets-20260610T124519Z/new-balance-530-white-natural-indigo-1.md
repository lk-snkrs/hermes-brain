# Gate B2 handle packet — new-balance-530-white-natural-indigo-1

- título: Tênis New Balance 530 White Natural Indigo Branco
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `5`
- SKUs únicos: `5`
- priority_counts: `{'P1_saneamento': 5}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 3, 'BLOCKED_TINY_DUPLICATE': 2}`
- issue_counts: `{'shopify_variant_tiny_missing': 3, 'tiny_duplicate_exact_code_blocked': 2}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `3` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `2` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `MR530SG`
- `MR530SG-40`
- `MR530SG-41`
- `MR530SG-7`
- `MR530SG-8`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
