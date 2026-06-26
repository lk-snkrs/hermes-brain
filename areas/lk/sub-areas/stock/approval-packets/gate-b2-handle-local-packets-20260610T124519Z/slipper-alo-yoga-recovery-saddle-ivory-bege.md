# Gate B2 handle packet — slipper-alo-yoga-recovery-saddle-ivory-bege

- título: Slipper Alo Yoga Recovery Saddle/Ivory Bege
- prioridade: `P0_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `12`
- SKUs únicos: `12`
- priority_counts: `{'P0_saneamento': 12}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_SHOPIFY_DUPLICATE': 11}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `11` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `a0827u`
- `a0827u-1`
- `a0827u-10`
- `a0827u-11`
- `a0827u-2`
- `a0827u-3`
- `a0827u-4`
- `a0827u-5`
- `a0827u-6`
- `a0827u-7`
- `a0827u-8`
- `a0827u-9`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
