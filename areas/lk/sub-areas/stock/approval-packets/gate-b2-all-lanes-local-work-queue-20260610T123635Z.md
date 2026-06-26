# Gate B2 — execução sequencial local/cache de todas as lanes — 20260610T123635Z

Interpretação segura do pedido: processar todos os bloqueios em sequência como fila local/cache consultável. Tiny/Shopify permanecem intactos.

## Ordem executada
1. `BLOCKED_TINY_MISSING` — rows `459`, handles `346` — Criar candidato local de match Tiny por SKU/código; se não existir match exato, manter bloqueado e só registrar lacuna local.
2. `BLOCKED_SHOPIFY_DUPLICATE` — rows `293`, handles `207` — Agrupar SKUs duplicados por handle/variant; registrar duplicidade no cache e manter bloqueado sem alterar Shopify.
3. `BLOCKED_TINY_DUPLICATE` — rows `96`, handles `82` — Agrupar códigos duplicados Tiny; preparar escolha local de canônico provável, sem alterar Tiny.
4. `BLOCKED_TINY_DEPOSIT_MISSING` — rows `57`, handles `57` — Reconfirmar/registrar lacuna do depósito oficial LK | CONTROLE ESTOQUE; manter bloqueado até fonte viva confirmar.

## Totais
- queue_rows: `905`
- handles: `558`
- lane_counts: `{'BLOCKED_TINY_MISSING': 459, 'BLOCKED_SHOPIFY_DUPLICATE': 293, 'BLOCKED_TINY_DUPLICATE': 96, 'BLOCKED_TINY_DEPOSIT_MISSING': 57}`
- priority_counts_by_row: `{'P0_saneamento': 84, 'P1_saneamento': 319, 'P2_saneamento': 502}`
- public_availability_safe_rows: `0`
- tiny_write: `0`
- shopify_write: `0`
- writes_externos: `0`

## Arquivos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-all-lanes-local-work-queue-20260610T123635Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-all-lanes-local-work-queue-20260610T123635Z.csv`
- SQLite: `areas/lk/sub-areas/stock/data/gate_b2_all_lanes_local_work_queue_20260610T123635Z.db`
- Lane dir: `areas/lk/sub-areas/stock/approval-packets/gate-b2-all-lanes-local-work-queue-20260610T123635Z`

## Guardrails
- Tiny write: 0
- Shopify write: 0
- Disponibilidade pública/pronta entrega: 0
- Contato externo/fornecedor/cliente: 0
- Cron/runtime/webhook/bot/gateway novo: 0
