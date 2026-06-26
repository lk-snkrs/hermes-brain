# Gate B2 — P0 live read-only completo — 20260610T135530Z

Escopo: investigar todos os P0 atuais da worklist com workers locais paralelos, usando Shopify/Tiny read-only. Nenhuma correção externa foi executada.

## Totais
- workers solicitados: `3`
- workers concluídos: `3`
- linhas P0 da worklist cobertas: `18`
- handles P0 investigados: `9`
- prefixes P0 investigados: `13`
- linhas crosswalk live/read-only: `150`

## Status live/read-only
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `27`
- shopify_duplicate_sku_blocked: `99`
- shopify_variant_tiny_missing: `12`
- tiny_duplicate_exact_code_blocked: `11`

## Por handle
- `air-jordan-1-low-true-blue` — matched_exact_sku_stock_resolved: 1, tiny_duplicate_exact_code_blocked: 5
- `nike-dunk-low-pink-red-white` — matched_exact_sku_stock_resolved: 4, tiny_duplicate_exact_code_blocked: 3
- `slipper-alo-yoga-recovery-saddle-ivory-bege` — shopify_duplicate_sku_blocked: 11, shopify_variant_tiny_missing: 1
- `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — matched_exact_sku_stock_resolved: 3, shopify_variant_tiny_missing: 1, tiny_duplicate_exact_code_blocked: 3
- `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza` — matched_exact_sku_stock_resolved: 1, shopify_duplicate_sku_blocked: 11
- `tenis-asics-gel-1130-black-pure-silver-prata` — shopify_duplicate_sku_blocked: 22, shopify_variant_tiny_missing: 2
- `tenis-asics-gel-1130-white-black-silver-prata` — shopify_duplicate_sku_blocked: 22, shopify_variant_tiny_missing: 2
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho` — matched_exact_sku_stock_missing_deposit: 1, matched_exact_sku_stock_resolved: 18, shopify_duplicate_sku_blocked: 22, shopify_variant_tiny_missing: 5
- `tenis-new-balance-204l-grey-matter-shipyard-cinza` — shopify_duplicate_sku_blocked: 11, shopify_variant_tiny_missing: 1

## Artefatos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-all-20260610T135530Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-all-20260610T135530Z.csv`
- diretório workers: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-workers-20260610T135530Z`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública/pronta entrega: `0`
- Saldos Tiny lidos são evidência interna e precisam de reconfirmação/fonte viva antes de atendimento.

## Próximo gate recomendado
Gerar packets de correção P0 por handle/lane com diff/rollback/readback proposto. Não executar writes sem aprovação escopada.
