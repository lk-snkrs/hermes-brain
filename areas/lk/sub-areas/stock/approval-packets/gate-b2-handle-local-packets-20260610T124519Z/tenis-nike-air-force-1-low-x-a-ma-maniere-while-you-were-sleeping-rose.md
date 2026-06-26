# Gate B2 handle packet — tenis-nike-air-force-1-low-x-a-ma-maniere-while-you-were-sleeping-rose

- título: Tênis Nike Air Force 1 Low x A Ma Maniére While You Were Sleeping Rose
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
- `HF4084-200`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
