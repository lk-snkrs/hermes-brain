# Gate B2 handle packet — tenis-onitsuka-tiger-mexico-66-white-blue-branco

- título: Tênis Onitsuka Tiger Mexico 66 White Blue Branco
- prioridade: `P2_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `2`
- SKUs únicos: `1`
- priority_counts: `{'P2_saneamento': 2}`
- lane_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 2}`
- issue_counts: `{'shopify_duplicate_sku_blocked': 2}`

## Sequência local recomendada
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `2` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `1183C102100`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
