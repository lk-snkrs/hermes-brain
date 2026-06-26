# Gate B2 handle packet — tenis-adidas-handball-spezial-sporty-rich-brown-marrom

- título: Tênis adidas Handball Spezial Sporty & Rich Brown Marrom
- prioridade: `P0_saneamento`
- primary lane: `BLOCKED_TINY_DUPLICATE`
- linhas: `4`
- SKUs únicos: `4`
- priority_counts: `{'P0_saneamento': 4}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_TINY_DUPLICATE': 3}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 3}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `3` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `IH2612`
- `IH2612-10`
- `IH2612-2`
- `IH2612-8`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
