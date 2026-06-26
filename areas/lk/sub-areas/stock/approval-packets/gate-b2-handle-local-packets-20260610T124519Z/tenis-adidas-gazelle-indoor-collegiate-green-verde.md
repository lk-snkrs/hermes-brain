# Gate B2 handle packet — tenis-adidas-gazelle-indoor-collegiate-green-verde

- título: Tênis adidas Gazelle Indoor Collegiate Green Verde
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `5`
- SKUs únicos: `5`
- priority_counts: `{'P1_saneamento': 5}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_SHOPIFY_DUPLICATE': 3, 'BLOCKED_TINY_DUPLICATE': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 3, 'tiny_duplicate_exact_code_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `3` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.
- `BLOCKED_TINY_DUPLICATE` — rows `1` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.

## SKUs amostra
- `IG5929`
- `IG5929-1`
- `IG5929-3`
- `IG5929-5`
- `IG5929-7`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
