# Gate B2 — superfície estável de consulta atual — refresh 20260610T133814Z

## Decisão local implementada

A superfície estável de consulta atual foi revalidada e atualizada de forma idempotente para apontar ao índice canônico atual de Gate B2.

Não foi criado runtime novo. O objetivo é uso diário do comando estável sem depender de timestamp.

## Artefatos estáveis

- Pointer estável: `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`
- Wrapper estável: `areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py`
- Guia operacional: `areas/lk/sub-areas/stock/references/gate-b2-current-lookup-operational-guide-20260610.md`

## Artefatos canônicos apontados

- DB: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.csv`
- MD: `areas/lk/sub-areas/stock/approval-packets/gate-b2-canonical-current-index-20260610T130644Z.md`
- CLI canônico: `areas/lk/sub-areas/stock/scripts/gate_b2_lookup_canonical_current.py`

## Comando padrão

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "<SKU-ou-handle>" --limit 10
```

Com histórico superseded:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "<SKU-ou-handle>" --history
```

## Totais apontados

- Linhas canônicas atuais: `903`
- Linhas input lookup: `911`
- Estados superseded preservados: `8`
- Handles: `558`
- SKUs únicos: `903`
- Resolvidos locais atuais: `6`

## Guardrails

- Local/cache only.
- Tiny write: `0`.
- Shopify write: `0`.
- Writes externos: `0`.
- Cron/webhook/bot/runtime novo: `0`.
- Disponibilidade pública/pronta entrega: `0`.
- Tiny/fonte viva continua obrigatório para disponibilidade final.
