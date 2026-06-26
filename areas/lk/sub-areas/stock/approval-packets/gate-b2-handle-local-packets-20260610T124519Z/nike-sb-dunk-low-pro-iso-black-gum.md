# Gate B2 handle packet — nike-sb-dunk-low-pro-iso-black-gum

- título: Tênis Nike SB Dunk Low Pro ISO Black Gum Preto
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
- `CD2563006`
- `CD2563006-6`
- `CD2563006-7`
- `CD2563006-9`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
