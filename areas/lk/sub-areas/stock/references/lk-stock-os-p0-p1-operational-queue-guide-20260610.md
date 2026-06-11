# Guia — LK Stock OS fila P0/P1 operacional

Criado em: 2026-06-10T19:23:28Z

## Fonte

Usar a DB apontada por `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`, atualmente `areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db`.

## Interpretação

- **P0**: candidato forte a decisão porque tem demanda local, estoque observado zero na DB e identidade local resolvida. Ainda exige reconfirmação Tiny/fonte viva antes de ação externa ou disponibilidade.
- **P1**: demanda com identidade bloqueada. Resolver SKU/Tiny/Shopify local/read-only antes de estoque/reposição.

## Artefatos atuais

- JSON: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.csv`
- Markdown: `areas/lk/sub-areas/stock/reports/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.md`
- Packet: `areas/lk/sub-areas/stock/approval-packets/lk-stock-os-p0-p1-operational-queue-20260610T192328Z.md`
- Workers: `areas/lk/sub-areas/stock/reports/gate-b3-p0p1-operational-queue-workers-20260610T_P0P1_QUEUE_WORKERS`

## Guardrails

Tiny write 0; Shopify write 0; writes externos 0; runtime novo 0; pronta entrega pública 0.
