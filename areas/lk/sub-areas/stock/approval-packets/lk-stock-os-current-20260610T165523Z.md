# Gate B3 — LK Stock OS current local DB — 20260610T165523Z

## Veredito

Foi criada uma DB unificada local/read-only para consulta interna do Stock OS. Ela materializa a visão atual por SKU+handle, junta status canônico, master register, observações de estoque lidas nos batches Gate B2 e guardrails.

Esta DB **não** é autorização para pronta entrega pública: toda disponibilidade final continua exigindo Tiny/fonte viva no momento.

## Totais

- Linhas `current_local_stock`: `903`
- Observações detalhadas de estoque/proposta: `8333`
- Linhas master register: `558`
- Handles únicos: `558`
- Linhas current com alguma observação de estoque: `316`
- Linhas current com estoque positivo observado: `18`
- Linhas current com estoque zero observado: `298`
- Identidade resolvida segura localmente: `6`
- Bloqueadas/não resolvidas: `897`
- Disponibilidade pública segura: `0`

## Status canônico

- `BLOCKED_SHOPIFY_DUPLICATE`: 287
- `BLOCKED_TINY_DEPOSIT_MISSING`: 57
- `BLOCKED_TINY_DUPLICATE`: 96
- `BLOCKED_TINY_MISSING`: 457
- `CONSULTABLE_LOCAL_RESOLVED`: 6

## Gaps da database

- `BLOCKED_SHOPIFY_DUPLICATE_BLOCKS_PUBLIC_AVAILABILITY`: 285
- `BLOCKED_TINY_DEPOSIT_MISSING_BLOCKS_PUBLIC_AVAILABILITY`: 57
- `BLOCKED_TINY_DUPLICATE_BLOCKS_PUBLIC_AVAILABILITY`: 93
- `BLOCKED_TINY_MISSING_BLOCKS_PUBLIC_AVAILABILITY`: 359
- `NO_STOCK_OBSERVATION_IN_MASTER_REGISTER`: 103
- `OK_LOCAL_RESOLVED_STILL_RECONFIRM_LIVE_TINY`: 6

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Runtime novo: `0`
- Pronta entrega pública: `0`

## Artefatos

- sqlite_db: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db`
- json: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-os-current-20260610T165523Z.json`
- csv: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-os-current-20260610T165523Z.csv`
- packet_md: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/approval-packets/lk-stock-os-current-20260610T165523Z.md`
- guide: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/references/lk-stock-os-current-db-guide-20260610.md`
- pointer: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- script: `areas/lk/sub-areas/stock/scripts/gate_b3_build_unified_local_stock_db.py`
