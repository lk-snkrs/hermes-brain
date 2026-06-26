# Gate B2 — superfície estável de consulta atual — 20260610T132630Z

## Decisão local implementada

Promovida a visão canônica timestampada para uma superfície estável de consulta diária, sem precisar lembrar o timestamp do último índice.

## Artefatos

- Pointer estável: `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`
- Wrapper estável: `areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py`
- Guia operacional: `areas/lk/sub-areas/stock/references/gate-b2-current-lookup-operational-guide-20260610.md`
- DB canônico apontado: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- JSON canônico apontado: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json`

## Comando padrão

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py <query> --limit 10
```

## Totais apontados

- Linhas canônicas atuais: `903`
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
