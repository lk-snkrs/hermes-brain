# Gate B2 handle packet — tenis-adidas-samba-og-maroon-cream-white-vinho

- título: Tênis adidas Samba Og Maroon Cream White Vinho
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P1_saneamento': 3}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2, 'BLOCKED_TINY_DUPLICATE': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 2, 'tiny_duplicate_exact_code_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `1` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `ID0477`
- `ID0477-3`
- `ID0477-7`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
