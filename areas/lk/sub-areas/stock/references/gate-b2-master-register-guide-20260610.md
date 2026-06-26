# Gate B2 — guia do Master Register P0+P1+P2 — 2026-06-10

## Objetivo

Consolidar todos os packets P0/P1/P2 do Gate B2 em uma única superfície operacional local/read-only por `priority + lane + handle`, preservando as 8.333 linhas detalhadas de proposta SKU/Tiny/Shopify.

## Artefatos

- JSON master: `areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.json`
- CSV master por handle/lane: `areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.csv`
- CSV detalhe/propostas: `areas/lk/sub-areas/stock/reports/gate-b2-master-register-proposals-20260610T162241Z.csv`
- SQLite consulta local: `areas/lk/sub-areas/stock/data/gate_b2_master_register_20260610T162241Z.db`
- Packet MD: `areas/lk/sub-areas/stock/approval-packets/gate-b2-master-register-20260610T162241Z.md`
- Gerador reutilizável: `areas/lk/sub-areas/stock/scripts/gate_b2_master_register.py`

## Totais

- Linhas master: `558`
- Handles únicos: `558`
- Propostas detalhadas: `8.333`
- P0: `9`
- P1: `141`
- P2: `408`

## Lanes

- `SHOPIFY_DUPLICATE_PACKET`: `225`
- `TINY_CODE_INVESTIGATION_PACKET`: `165`
- `TINY_DEPOSIT_PACKET`: `105`
- `TINY_DUPLICATE_PACKET`: `54`
- `LOCAL_RESOLVED_REFERENCE_PACKET`: `9`

## Uso operacional

1. Abrir o CSV master e filtrar por `priority`, depois `lane`.
2. Abrir o `packet_md` da linha escolhida para ver a decisão por handle.
3. Para detalhe SKU/tamanho, consultar o CSV de propostas ou o SQLite.
4. Se alguma decisão virar possível alteração Tiny/Shopify, criar novo packet com diff, rollback e readback; não executar por inferência.

## Consulta SQLite rápida

```bash
sqlite3 areas/lk/sub-areas/stock/data/gate_b2_master_register_20260610T162241Z.db \
  "select priority,lane,count(*) from master_register group by priority,lane order by priority,lane;"
```

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Runtime novo: `0`
- Disponibilidade pública/pronta entrega: `0`
- Disponibilidade final exige Tiny/fonte viva consultada no momento.
