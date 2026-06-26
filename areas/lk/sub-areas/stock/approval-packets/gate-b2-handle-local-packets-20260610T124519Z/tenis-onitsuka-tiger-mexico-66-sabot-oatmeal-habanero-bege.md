# Gate B2 handle packet — tenis-onitsuka-tiger-mexico-66-sabot-oatmeal-habanero-bege

- título: Tênis Onitsuka Tiger Mexico 66 Sabot Oatmeal Habanero Bege
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
- `1183C123.251`
- `1183C123.251-1`
- `1183C123.251-2`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
