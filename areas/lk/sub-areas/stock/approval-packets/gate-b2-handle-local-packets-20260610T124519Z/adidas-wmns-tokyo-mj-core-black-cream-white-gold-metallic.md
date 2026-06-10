# Gate B2 handle packet — adidas-wmns-tokyo-mj-core-black-cream-white-gold-metallic

- título: adidas Wmns Tokyo MJ 'Core Black Cream White Gold Metallic'
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P1_saneamento': 3}`
- lane_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 3}`
- issue_counts: `{'shopify_duplicate_sku_blocked': 3}`

## Sequência local recomendada
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `3` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `JR4790-37`
- `JR4790-39`
- `JR4790-40`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
