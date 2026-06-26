# Gate B2 handle packet — air-jordan-1-mid-aqua-blue-tint

- título: Tênis Nike Air Jordan 1 Mid Aqua Blue Tint Verde
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `1`
- SKUs únicos: `1`
- priority_counts: `{'P2_saneamento': 1}`
- lane_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 1}`
- issue_counts: `{'shopify_duplicate_sku_blocked': 1}`

## Sequência local recomendada
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `1` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `BQ6472303`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
