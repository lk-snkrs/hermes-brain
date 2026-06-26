# Gate B2 handle packet — tenis-asics-gel-1130-white-black-silver-prata

- título: Tênis ASICS Gel-1130 White Black Silver Prata
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
- `1201A933-100`
- `1201A933-100-34`
- `1201A933-100-35`
- `1201A933-100-36`
- `1201A933-100-37`
- `1201A933-100-38`
- `1201A933-100-39`
- `1201A933-100-40`
- `1201A933-100-41`
- `1201A933-100-42`
- `1201A933-100-43`
- `1201A933-100-44`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
