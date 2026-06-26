# Gate B2 handle packet — nike-dunk-low-se-australia

- título: Tênis Nike Dunk Low SE Australia Marrom
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `4`
- SKUs únicos: `4`
- priority_counts: `{'P1_saneamento': 4}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2, 'BLOCKED_TINY_DUPLICATE': 1, 'BLOCKED_TINY_DEPOSIT_MISSING': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 2, 'tiny_duplicate_exact_code_blocked': 1, 'matched_exact_sku_stock_missing_deposit': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DUPLICATE` — rows `1` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.
- `BLOCKED_TINY_DEPOSIT_MISSING` — rows `1` — Reconfirmar/registrar lacuna do depósito oficial LK | CONTROLE ESTOQUE; manter bloqueado até fonte viva confirmar.

## SKUs amostra
- `FN7645133`
- `FN7645133-7`
- `FN7645133-8`
- `FN7645133-9`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
