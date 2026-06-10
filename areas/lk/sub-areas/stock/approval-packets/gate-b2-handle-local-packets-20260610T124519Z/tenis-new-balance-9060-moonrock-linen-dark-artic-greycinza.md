# Gate B2 handle packet — tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza

- título: Tênis New Balance 9060 Moonrock Linen Dark Artic Grey Cinza
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `4`
- SKUs únicos: `3`
- priority_counts: `{'P1_saneamento': 4}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2, 'BLOCKED_SHOPIFY_DUPLICATE': 2}`
- issue_counts: `{'shopify_variant_tiny_missing': 2, 'shopify_duplicate_sku_blocked': 2}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `2` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `U9060EEB`
- `U9060EEB-7`
- `U9060EEB-8`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
