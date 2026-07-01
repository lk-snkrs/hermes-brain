# LK Stock SQL legado → Supabase — implementação fases 1/2/3

Data: 2026-07-01
Perfil executor: `lk-stock`
Escopo aprovado no Telegram: “Fazer fase 1/2 e 3 Sequencialmente”.

## Resultado executivo

Fases 1, 2 e 3 executadas no escopo local/read-only governado. Não houve write em Tiny, Shopify, WhatsApp/customer, campanha ou Supabase.

## Fase 1 — decisão POS/Stock OS sem SQLite legado

### 1. POS restock preflight

Arquivo: `/opt/data/scripts/lk_store_sale_restock_alert.py`

Mudanças:

- Removida dependência decisória de:
  - `current_stock_db_path()`;
  - `run_stock_os_prefix_repair()`;
  - `LK_STOCK_CROSSWALK`;
  - `LK_STOCK_PROMOTE`;
  - `artifacts.sqlite_db` / promoção de SQLite local.
- `ensure_stock_os_ready_for_candidates()` agora usa o responder/lookup Supabase e, quando não resolve, retorna:
  - `status=needs_lk_stock_validation`;
  - `legacy_sqlite_repair=0`;
  - `tiny_write=0`, `shopify_write=0`, `writes_externos=0`.
- `restock_current_stock_line()` não congela mais preflight line antiga `não encontrado`.
- Prompt de ação reconhece `Stock OS` genérico, inclusive `Stock OS Supabase`, não só `Stock OS local`.

### 2. Stock OS API adapter legado

Arquivo: `areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py`

Mudanças:

- Reescrito como adapter Supabase-first.
- Removeu leitura runtime de `sqlite3`, `artifacts.sqlite_db` e `current_local_stock`.
- Consulta `public.lk_stock_snapshots` latest + `public.lk_stock_items` via Supabase REST com env governado.
- Mantém CLI/HTTP contract `/lookup` e `/api/lk-stock/lookup`.
- `--pointer` permanece só como argumento legado ignorado para compatibilidade.
- Health agora expõe `legacy_sqlite=0` e `values_printed=false`.

Verificação real do adapter:

```json
{
  "status": "confirmado",
  "result_count": 2,
  "total_count": 2,
  "first_sku": "U204LMMC-6",
  "first_size": "39",
  "first_qty": 2.0,
  "values_printed": false
}
```

### 3. Cron Supabase sync

Arquivo: `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py`

Mudança:

- Se a fonte upstream/Hub vier ruim ou decommissioned, o script não sobrescreve/poison Supabase.
- Ele valida o readback atual do Supabase + sentinel MR530SG e cai em modo:
  - `source_unavailable_readback_only`;
  - `supabase_write=0`.

Verificação manual:

```json
{
  "status": "ok",
  "run_id": "20260626T092006Z",
  "items": 8550,
  "mode": "source_unavailable_readback_only",
  "source_error": "source_mr530sg_sentinel_failed:rows=98:units=0",
  "supabase_write": 0,
  "values_printed": false
}
```

Observação: isso evita erro/poison de dados, mas ainda deixa uma pendência real: o endpoint/fonte Hub que alimenta snapshot fresco precisa ser corrigido/deployado em escopo próprio.

## Fase 2 — despromover SQLite local para diagnóstico

Arquivo: `/opt/data/profiles/lk-stock/scripts/lk_stock_gate_b_daily_reconcile.py`

Mudanças:

- Header/documentação runtime atualizado: Gate B SQLite é `legacy diagnostic` temporário.
- Alerta/receipt local passa a dizer explicitamente que Gate B/SQLite não é fonte POS/pronta entrega.
- Contrato de freshness atualizado para orientar Supabase Stock OS read model como base.
- Mantidos guardrails: local SQLite write apenas, Supabase/Tiny/Shopify/customer write 0.

## Fase 3 — limpeza/arquivo

### 1. Artefato DB obsoleto 0 bytes

Movido de:

`areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260626T102006Z.db`

Para:

`areas/lk/sub-areas/stock/archive/sqlite-decommissioned-20260701/lk_stock_os_current_tiny_full_sync_20260626T102006Z.db`

### 2. Skill/doc ambígua renomeada

Skill `lk-stock`:

- criado `references/pos-restock-alert-supabase-readmodel-20260701.md`;
- removido arquivo antigo ambíguo `pos-restock-alert-supabase-pointer-tiny-readback-fallback-20260701.md`;
- índice da skill atualizado para não mencionar `tiny-readback-fallback`.

## Verificações

```bash
python3 -m py_compile \
  /opt/data/scripts/lk_store_sale_restock_alert.py \
  /opt/data/scripts/lk_hermes_whatsapp_responder.py \
  /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py \
  /opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py \
  /opt/data/profiles/lk-stock/scripts/lk_stock_gate_b_daily_reconcile.py \
  /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py
```

Resultado: `py_compile_ok`.

```bash
python3 -m pytest /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py -q
```

Resultado: `26 passed in 4.40s`.

Buscas de regressão:

- `/opt/data/scripts/lk_store_sale_restock_alert.py`: `run_stock_os_prefix_repair`, `current_stock_db_path`, `LK_STOCK_CROSSWALK`, `LK_STOCK_PROMOTE`, `artifacts.sqlite_db`, `current_local_stock` → 0 matches.
- `areas/lk/sub-areas/stock/data/*.db` → 0 files.
- Skill `lk-stock` não referencia mais o arquivo ambíguo antigo; referencia o novo readmodel.

## Guardrails preservados

- Tiny write: 0
- Shopify write: 0
- Supabase write nesta execução: 0
- WhatsApp/customer send: 0
- Deploy/prod change: 0
- Secrets printed: false / `values_printed=false`

## Pendência consciente

Não fiz deploy/Vercel nem migração DDL Supabase nova. Esses são external/prod writes e exigem aprovação escopada com rollback/readback.

Pendência técnica restante: corrigir/deployar a fonte Hub/protected endpoint que hoje causa `source_mr530sg_sentinel_failed:rows=98:units=0`. O readback Supabase está íntegro, mas o refresh upstream ainda precisa de correção em produção.
