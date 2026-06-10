# Gate B2 — camada local consultável ampliada — 20260610T121716Z

Objetivo: organizar todos os bloqueios Gate B2 para consulta futura segura, preservando Tiny/Shopify intactos.

## Guardrails
- Local/cache only.
- Tiny/Shopify sem write.
- Não libera pronta entrega pública; `public_availability_safe_rows=0`.
- Próximas ações recomendadas são locais/read-only por lane.

## Totais
- issue_rows: `905`
- handles: `558`
- priority_counts: `{'P0_saneamento': 9, 'P1_saneamento': 141, 'P2_saneamento': 408}`
- issue_counts: `{'matched_exact_sku_stock_missing_deposit': 57, 'shopify_duplicate_sku_blocked': 293, 'shopify_variant_tiny_missing': 459, 'tiny_duplicate_exact_code_blocked': 96}`
- lane_counts: `{'BLOCKED_TINY_DEPOSIT_MISSING': 57, 'BLOCKED_SHOPIFY_DUPLICATE': 293, 'BLOCKED_TINY_MISSING': 459, 'BLOCKED_TINY_DUPLICATE': 96}`
- public_availability_safe_rows: `0`
- writes_externos: `0`

## Top 20 handles por prioridade
- `P0_saneamento` `slipper-alo-yoga-recovery-saddle-ivory-bege` — issues `12`, SKUs `12`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `tenis-asics-gel-1130-black-pure-silver-prata` — issues `12`, SKUs `12`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `tenis-asics-gel-1130-white-black-silver-prata` — issues `12`, SKUs `12`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — issues `12`, SKUs `12`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `tenis-new-balance-204l-grey-matter-shipyard-cinza` — issues `12`, SKUs `12`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza` — issues `11`, SKUs `11`, principal `shopify_duplicate_sku_blocked`
- `P0_saneamento` `air-jordan-1-low-true-blue` — issues `5`, SKUs `5`, principal `tiny_duplicate_exact_code_blocked`
- `P0_saneamento` `nike-dunk-low-pink-red-white` — issues `4`, SKUs `4`, principal `tiny_duplicate_exact_code_blocked`
- `P0_saneamento` `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — issues `4`, SKUs `4`, principal `tiny_duplicate_exact_code_blocked`
- `P1_saneamento` `tenis-air-jordan-1-low-lucky-green-verde` — issues `7`, SKUs `7`, principal `shopify_duplicate_sku_blocked`
- `P1_saneamento` `tenis-new-balance-1906l-silver-metallic-black-prata` — issues `7`, SKUs `7`, principal `shopify_duplicate_sku_blocked`
- `P1_saneamento` `new-balance-530-white-natural-indigo-1` — issues `5`, SKUs `5`, principal `tiny_duplicate_exact_code_blocked`
- `P1_saneamento` `tenis-adidas-gazelle-indoor-collegiate-green-verde` — issues `5`, SKUs `5`, principal `tiny_duplicate_exact_code_blocked`
- `P1_saneamento` `camiseta-nude-project-global-soon-ash-cinza` — issues `5`, SKUs `5`, principal `shopify_duplicate_sku_blocked`
- `P1_saneamento` `tenis-new-balance-9060-grey-day-kids-td-cinza` — issues `7`, SKUs `7`, principal `shopify_variant_tiny_missing`
- `P1_saneamento` `air-jordan-1-low-vintage-grey` — issues `4`, SKUs `4`, principal `matched_exact_sku_stock_missing_deposit`
- `P1_saneamento` `air-jordan-4-se-black-canvas` — issues `4`, SKUs `4`, principal `matched_exact_sku_stock_missing_deposit`
- `P1_saneamento` `nike-dunk-low-se-australia` — issues `4`, SKUs `4`, principal `matched_exact_sku_stock_missing_deposit`
- `P1_saneamento` `air-jordan-1-low-panda-2023` — issues `3`, SKUs `3`, principal `tiny_duplicate_exact_code_blocked`
- `P1_saneamento` `air-jordan-1-low-se-mocha` — issues `3`, SKUs `3`, principal `tiny_duplicate_exact_code_blocked`

## Arquivos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-full-consultable-crosswalk-20260610T121716Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-full-consultable-crosswalk-20260610T121716Z.csv`
- SQLite: `areas/lk/sub-areas/stock/data/gate_b2_full_consultable_crosswalk_20260610T121716Z.db`
- Fonte issues: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-issues-20260610T104842Z.csv`
- Fonte fila: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-fila-p0p1-20260610T105900Z.csv`
