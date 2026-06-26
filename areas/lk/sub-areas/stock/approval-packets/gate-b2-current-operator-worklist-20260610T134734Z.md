# Gate B2 — worklist operacional local da consulta atual — 20260610T134734Z

Objetivo: transformar a superfície canônica de consulta em uma fila humana/local de próximos passos por handle/lane/prioridade, sem write Tiny/Shopify e sem afirmar pronta entrega.

## Totais
- worklist_rows: `694`
- blocked_cleanup_rows: `691`
- resolved_reference_rows: `3`
- source_canonical_sku_rows: `903`
- blocked_source_sku_rows: `897`
- resolved_source_sku_rows: `6`
- unique_handles: `558`
- priority_handle_lane_counts: `{'P0_saneamento': 18, 'P1_saneamento': 251, 'P2_saneamento': 425}`
- status_handle_lane_counts: `{'BLOCKED_TINY_MISSING': 345, 'BLOCKED_SHOPIFY_DUPLICATE': 207, 'BLOCKED_TINY_DUPLICATE': 82, 'CONSULTABLE_LOCAL_RESOLVED': 3, 'BLOCKED_TINY_DEPOSIT_MISSING': 57}`
- status_sku_counts: `{'BLOCKED_SHOPIFY_DUPLICATE': 287, 'BLOCKED_TINY_DUPLICATE': 96, 'BLOCKED_TINY_MISSING': 457, 'CONSULTABLE_LOCAL_RESOLVED': 6, 'BLOCKED_TINY_DEPOSIT_MISSING': 57}`

## Ações recomendadas por tipo
- READONLY_TINY_CODE_INVESTIGATION: `345` handles/lane
- SHOPIFY_DUPLICATE_PROPOSAL: `207` handles/lane
- TINY_DUPLICATE_PROPOSAL: `82` handles/lane
- NO_WRITE_RESOLVED_CACHE: `3` handles/lane
- TINY_DEPOSIT_MAPPING_CHECK: `57` handles/lane

## Primeiros itens bloqueados P0
- `1` `BLOCKED_TINY_MISSING` `slipper-alo-yoga-recovery-saddle-ivory-bege` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `2` `BLOCKED_TINY_MISSING` `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `3` `BLOCKED_TINY_MISSING` `tenis-asics-gel-1130-black-pure-silver-prata` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `4` `BLOCKED_TINY_MISSING` `tenis-asics-gel-1130-white-black-silver-prata` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `5` `BLOCKED_TINY_MISSING` `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `6` `BLOCKED_TINY_MISSING` `tenis-new-balance-204l-grey-matter-shipyard-cinza` — SKUs `1` — READONLY_TINY_CODE_INVESTIGATION
- `7` `BLOCKED_SHOPIFY_DUPLICATE` `slipper-alo-yoga-recovery-saddle-ivory-bege` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `8` `BLOCKED_SHOPIFY_DUPLICATE` `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `9` `BLOCKED_SHOPIFY_DUPLICATE` `tenis-asics-gel-1130-black-pure-silver-prata` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `10` `BLOCKED_SHOPIFY_DUPLICATE` `tenis-asics-gel-1130-white-black-silver-prata` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `11` `BLOCKED_SHOPIFY_DUPLICATE` `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `12` `BLOCKED_SHOPIFY_DUPLICATE` `tenis-new-balance-204l-grey-matter-shipyard-cinza` — SKUs `11` — SHOPIFY_DUPLICATE_PROPOSAL
- `13` `BLOCKED_TINY_DUPLICATE` `air-jordan-1-low-true-blue` — SKUs `5` — TINY_DUPLICATE_PROPOSAL
- `14` `BLOCKED_TINY_DUPLICATE` `nike-dunk-low-pink-red-white` — SKUs `3` — TINY_DUPLICATE_PROPOSAL
- `15` `BLOCKED_TINY_DUPLICATE` `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — SKUs `3` — TINY_DUPLICATE_PROPOSAL

## Arquivos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.csv`
- Fonte DB: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Runtime/cron/webhook/bot novo: `0`
- Disponibilidade pública/pronta entrega: `0`; exige Tiny/fonte viva no momento.
