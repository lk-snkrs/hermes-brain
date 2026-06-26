# Gate B2 handle packet — yeezy-350-v2-carbon-beluga

- título: Tênis Yeezy 350 V2 Carbon Beluga Cinza
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `4`
- SKUs únicos: `4`
- priority_counts: `{'P1_saneamento': 4}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 3, 'BLOCKED_TINY_DUPLICATE': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 3, 'tiny_duplicate_exact_code_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `3` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `1` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `HQ7045`
- `HQ7045-1`
- `HQ7045-8`
- `HQ7045-9`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
