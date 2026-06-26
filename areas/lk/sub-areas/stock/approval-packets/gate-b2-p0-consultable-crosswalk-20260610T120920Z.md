# Gate B2 P0 — camada local consultável Shopify↔Tiny↔estoque — 20260610T120920Z

Objetivo: deixar organizado “o que é o quê” para consulta futura segura, sem alterar Shopify/Tiny.

## Regra
- Correção/organização padrão: local/cache.
- Tiny e Shopify usados como fonte viva read-only.
- Cache local ajuda consulta e decisão interna, mas não é promessa pública de pronta entrega.
- `public_availability_safe`: 0 para todas as linhas neste índice.
- `writes_externos`: 0.

## Totais
- rows: `74`
- handles: `9`
- status_counts: `{'shopify_variant_tiny_missing': 6, 'shopify_duplicate_sku_blocked': 58, 'matched_exact_sku_stock_resolved': 6, 'tiny_duplicate_exact_code_blocked': 4}`
- lane_counts: `{'BLOCKED_TINY_MISSING': 6, 'BLOCKED_SHOPIFY_DUPLICATE': 58, 'CONSULTABLE_LOCAL_RESOLVED': 6, 'BLOCKED_TINY_DUPLICATE': 4}`
- local_consult_safe_rows: `6`
- public_availability_safe_rows: `0`
- writes_externos: `0`

## Resumo por handle
- `air-jordan-1-low-true-blue` — rows `1`, resolvidos locais `0`, bloqueados `1`, lane `BLOCKED_TINY_DUPLICATE`, status `{'tiny_duplicate_exact_code_blocked': 1}`
- `nike-dunk-low-pink-red-white` — rows `1`, resolvidos locais `1`, bloqueados `0`, lane `CONSULTABLE_LOCAL_RESOLVED`, status `{'matched_exact_sku_stock_resolved': 1}`
- `slipper-alo-yoga-recovery-saddle-ivory-bege` — rows `12`, resolvidos locais `0`, bloqueados `12`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`
- `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — rows `7`, resolvidos locais `3`, bloqueados `4`, lane `BLOCKED_TINY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'matched_exact_sku_stock_resolved': 3, 'tiny_duplicate_exact_code_blocked': 3}`
- `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza` — rows `3`, resolvidos locais `0`, bloqueados `3`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_duplicate_sku_blocked': 3}`
- `tenis-asics-gel-1130-black-pure-silver-prata` — rows `12`, resolvidos locais `0`, bloqueados `12`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`
- `tenis-asics-gel-1130-white-black-silver-prata` — rows `12`, resolvidos locais `0`, bloqueados `12`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — rows `14`, resolvidos locais `2`, bloqueados `12`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11, 'matched_exact_sku_stock_resolved': 2}`
- `tenis-new-balance-204l-grey-matter-shipyard-cinza` — rows `12`, resolvidos locais `0`, bloqueados `12`, lane `BLOCKED_SHOPIFY_DUPLICATE`, status `{'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}`

## Arquivos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-p0-consultable-crosswalk-20260610T120920Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-p0-consultable-crosswalk-20260610T120920Z.csv`
- SQLite consulta: `areas/lk/sub-areas/stock/data/gate_b2_p0_consultable_crosswalk_20260610T120920Z.db`
- Fonte read-only: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
