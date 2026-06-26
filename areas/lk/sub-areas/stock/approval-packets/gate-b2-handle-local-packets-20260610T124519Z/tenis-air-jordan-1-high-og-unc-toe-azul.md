# Gate B2 handle packet — tenis-air-jordan-1-high-og-unc-toe-azul

- título: Tênis Nike Air Jordan 1 High OG UNC Toe Azul
- prioridade: `P1_saneamento`
- primary lane: `BLOCKED_TINY_MISSING`
- linhas: `2`
- SKUs únicos: `2`
- priority_counts: `{'P1_saneamento': 2}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 1, 'BLOCKED_TINY_DEPOSIT_MISSING': 1}`
- issue_counts: `{'shopify_variant_tiny_missing': 1, 'matched_exact_sku_stock_missing_deposit': 1}`

## Sequência local recomendada
- `BLOCKED_TINY_MISSING` — rows `1` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
- `BLOCKED_TINY_DEPOSIT_MISSING` — rows `1` — Reconfirmar/registrar lacuna do depósito oficial LK | CONTROLE ESTOQUE; manter bloqueado até fonte viva confirmar.

## SKUs amostra
- `DZ5485400-3`
- `DZ5485400-4`

## Guardrails
- local/cache only
- Tiny write: 0
- Shopify write: 0
- disponibilidade pública/pronta entrega: 0
