# Gate B2 handle packet — tenis-new-balance-1906l-silver-metallic-black-prata

- título: Tênis New Balance 1906L Silver Metallic Black Prateado
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_SHOPIFY_DUPLICATE`
- linhas: `7`
- SKUs únicos: `7`
- priority_counts: `{'P1_saneamento': 7}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_SHOPIFY_DUPLICATE': 6}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 6}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_SHOPIFY_DUPLICATE` — rows `6` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.

## SKUs amostra
- `U1906LOC`
- `U1906LOC-38`
- `U1906LOC-39`
- `U1906LOC-40`
- `U1906LOC-42`
- `U1906LOC-43`
- `U1906LOC-44`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
