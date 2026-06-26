# Gate B2 — guia operacional da consulta atual estável — 2026-06-10

## Objetivo

Usar uma entrada estável para consultar o estado local atual do crosswalk LK Stock Gate B2 sem precisar lembrar timestamps de artefatos.

Esta superfície é **local/cache only**. Ela ajuda a saber “o que é o quê” entre Shopify↔Tiny↔estoque local, mas **não libera promessa de pronta entrega**.

## Comando padrão

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "<SKU-ou-handle-ou-texto>" --limit 10
```

Com histórico de estados antigos superseded:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "<SKU-ou-handle-ou-texto>" --history
```

Mostrar o pointer atual:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py --show-pointer
```

Saída JSON para automação local:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "CW1588601-4" --history --json
```

## Pointer estável

- `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`

O pointer aponta para os artefatos canônicos atuais:

- SQLite: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.csv`
- MD: `areas/lk/sub-areas/stock/approval-packets/gate-b2-canonical-current-index-20260610T130644Z.md`
- CLI canônico: `areas/lk/sub-areas/stock/scripts/gate_b2_lookup_canonical_current.py`

## Totais atuais

- Linhas canônicas atuais: `903`
- Linhas de input do lookup: `911`
- Estados antigos superseded preservados: `8`
- Handles: `558`
- SKUs únicos: `903`

Status:

- `CONSULTABLE_LOCAL_RESOLVED`: `6`
- `BLOCKED_TINY_MISSING`: `457`
- `BLOCKED_TINY_DUPLICATE`: `96`
- `BLOCKED_SHOPIFY_DUPLICATE`: `287`
- `BLOCKED_TINY_DEPOSIT_MISSING`: `57`

## Como interpretar

- `CONSULTABLE_LOCAL_RESOLVED`: match local resolvido para consulta interna, mas ainda exige Tiny/fonte viva antes de disponibilidade pública.
- `BLOCKED_*`: item permanece bloqueado para decisão operacional até saneamento/localização segura.
- `superseded_count > 0`: havia estado local antigo para o mesmo SKU+handle; a consulta atual prioriza a resolução canônica, mas mantém histórico.

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/bot/runtime novo: `0`
- `public_availability_safe`: `false`
- Disponibilidade/pronta entrega exige consulta Tiny ou fonte viva equivalente no momento.

## Procedimento para QA/sanidade da superfície atual

Use o checker local:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_current_surface_check.py
```

Ele valida:

- existência do pointer, DB, JSON/CSV/MD canônicos e wrapper estável;
- contagens do DB contra o pointer;
- status/prioridades do DB contra o pointer;
- guardrails zerados (`tiny_write`, `shopify_write`, `writes_externos`, `public_availability_safe`);
- amostra determinística por status/prioridade para QA manual.

Para gerar pacote de evidência:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_current_surface_check.py \
  --json-out areas/lk/sub-areas/stock/reports/<arquivo>.json \
  --csv-out areas/lk/sub-areas/stock/reports/<arquivo>.csv \
  --md-out areas/lk/sub-areas/stock/approval-packets/<arquivo>.md
```

## Procedimento para atualizar no futuro

1. Gerar novo índice canônico timestampado.
2. Validar consultas de SKU resolvido com histórico, SKU resolvido sem histórico e handle bloqueado.
3. Atualizar apenas `gate_b2_current_pointer.json` para apontar ao novo índice.
4. Rodar `lk_stock_current_surface_check.py`.
5. Rodar testes locais.
6. Criar receipt e atualizar PRD.

Não criar outro wrapper concorrente; manter `lk_stock_lookup_current.py` como entrada estável.
