# Gate B2 handle packet — yeezy-500-blush

- título: Tênis Yeezy 500 Blush Bege
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `3`
- SKUs únicos: `3`
- priority_counts: `{'P1_saneamento': 3}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 2, 'BLOCKED_TINY_DEPOSIT_MISSING': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 2, 'matched_exact_sku_stock_missing_deposit': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `2` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DEPOSIT_MISSING` — rows `1` — Reconfirmar/registrar lacuna do depósito oficial LK | CONTROLE ESTOQUE; manter bloqueado até fonte viva confirmar.

## SKUs amostra
- `DB2908`
- `DB2908-39`
- `DB2908-40`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
