# Gate B2 handle packet — tenis-jordan-4-retro-toro-bravo-2026-vermelho

- título: Tênis Jordan 4 Retro Toro Bravo 2026 Vermelho
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
- `FQ8138-600`
- `FQ8138-600-34`
- `FQ8138-600-35`
- `FQ8138-600-36`
- `FQ8138-600-37`
- `FQ8138-600-38`
- `FQ8138-600-39`
- `FQ8138-600-40`
- `FQ8138-600-41`
- `FQ8138-600-42`
- `FQ8138-600-43`
- `FQ8138-600-44`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
