# Gate B2 handle packet — travis-scott-x-air-jordan-1-low-og-reverse-mocha

- título: Tênis Nike Travis Scott x Air Jordan 1 Low OG Reverse Mocha Bege
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `2`
- SKUs únicos: `2`
- priority_counts: `{'P1_saneamento': 2}`
- lane_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 1, 'BLOCKED_TINY_DEPOSIT_MISSING': 1}`
- issue_counts: `{'shopify_duplicate_sku_blocked': 1, 'matched_exact_sku_stock_missing_deposit': 1}`

## Sequência local recomendada
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `1` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.
- `BLOCKED_TINY_DEPOSIT_MISSING` — rows `1` — Reconfirmar/registrar lacuna do depósito oficial LK | CONTROLE ESTOQUE; manter bloqueado até fonte viva confirmar.

## SKUs amostra
- `DM7866162`
- `DM7866162-41`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
