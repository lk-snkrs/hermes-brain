# Gate B2 handle packet — camiseta-nude-project-global-soon-ash-cinza

- título: Camiseta Nude Project Global Soon Ash Cinza
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `5`
- SKUs únicos: `5`
- priority_counts: `{'P1_saneamento': 5}`
- lane_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 5}`
- issue_counts: `{'shopify_duplicate_sku_blocked': 5}`

## Sequência local recomendada
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `5` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `NDP006-1`
- `NDP006-2`
- `NDP006-3`
- `NDP006-4`
- `NDP006-5`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
