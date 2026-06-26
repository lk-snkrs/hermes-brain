# Gate B2 handle packet — air-jordan-1-low-multi-color-royal-toe

- título: Tênis Nike Air Jordan 1 Low Multi-Color Royal Toe Colorido
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `2`
- SKUs únicos: `2`
- priority_counts: `{'P1_saneamento': 2}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_TINY_DUPLICATE': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `1` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `CZ4776101`
- `CZ4776101-1`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
