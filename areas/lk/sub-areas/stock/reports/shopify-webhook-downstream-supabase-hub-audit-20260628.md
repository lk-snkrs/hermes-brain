# Audit — Downstream Shopify webhook → ledger → Supabase/Inventory Hub — 2026-06-28

## Veredito

O problema **não é ausência de webhook Shopify**. Os webhooks existem e o endpoint `lk-shopify-tiny-stock-sync` funciona.

O problema está no downstream: o fluxo de evento Shopify está parando em **dry-run/local ledger/local SQLite** e o cron Supabase atualmente só faz **readback/guardrail check** de um snapshot antigo. Ele **não está promovendo eventos/snapshots novos para `public.lk_stock_*`**.

Resultado prático: o Inventory Hub lê Supabase corretamente, mas lê um snapshot parado em `2026-06-26`, então não tem estoque real-time.

## Caminho auditado

```text
Shopify webhook
  → hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync
  → /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py
  → ledger.ndjson + local SQLite lk_tiny_stock_local.sqlite
  → NÃO promove para public.lk_stock_items/public.lk_stock_snapshots
  → Inventory Hub lê Supabase stale
```

## Evidências

### 1) Endpoint/webhook funciona

Audit anterior:

- `orders/paid`: HTTP `200`, `dry_run_recorded`, `write_executed=false`
- `orders/cancelled`: HTTP `200`, `dry_run_recorded`, `write_executed=false`
- assinatura inválida: HTTP `401`

### 2) Processor é explicitamente dry-run

Arquivo:

```text
/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py
```

Pontos observados:

- docstring: “dry-run processor”
- grava `LEDGER_FILE = /opt/data/hermes_bruno_ingest/local_sql/lk_shopify_tiny_stock_sync_dryrun/ledger.ndjson`
- atualiza local SQLite:
  - `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite`
- `would_update_record()` monta proposta de update Shopify, mas mantém `write_executed=false`
- só chama `update_local_stock_db_from_tiny_event()` em caso de Tiny match OK
- não há escrita para Supabase neste script

### 3) Ledger/local DB recebem eventos, mas isolados do Hub

Local audit:

| Artefato | Status |
|---|---|
| `ledger.ndjson` | existe, 63 linhas |
| `lk_tiny_stock_local.sqlite` | existe, 580 rows em `stock_by_sku`, 3 rows em `stock_events` |
| `refresh_queue` | 0 rows |

Resumo ledger:

| Status | Count |
|---|---:|
| `blocked` | 60 |
| `would_update_shopify_inventory` | 3 |

Principais motivos de bloqueio:

| Motivo | Count |
|---|---:|
| `tiny_match_not_high_confidence` | 42 |
| `tiny_no_match` | 6 |
| `missing_variant_id` | 11 |
| `missing_sku` | 1 |

Últimos eventos locais confirmados:

| SKU | Event | Status | Tiny read |
|---|---|---|---|
| `U9060ERA-7` | `orders/paid` | `updated_local` | `2026-06-28T18:02:52Z` |
| `1183A355.405-11` | `orders/paid` | `updated_local` | `2026-06-28T17:31:52Z` |
| `1183C015200-10` | `orders/paid` | `updated_local` | `2026-06-28T17:31:50Z` |

Esses eventos provam que o webhook chega e o Tiny é lido em alguns casos, mas ficam em base local separada.

### 4) Supabase Stock OS está stale

Supabase `public.lk_stock_snapshots`:

| Campo | Valor |
|---|---|
| latest `run_id` | `20260626T092006Z` |
| `total_count` / `result_count` | `8550 / 8550` |
| `source_observed_at` | `2026-06-26 09:20:06+00` |
| `imported_at` | `2026-06-26 17:08:56.055838+00` |
| `freshness` | `tiny_full_sync_nightly` |

Supabase `public.lk_stock_items`:

| Métrica | Valor |
|---|---:|
| rows | 8550 |
| snapshot_runs | 1 |
| positive_rows | 596 |
| units | 859 |

Não há snapshot novo após `2026-06-26` apesar de eventos locais em `2026-06-28`.

### 5) Cron Supabase existe, mas só valida snapshot antigo

Cron:

| Campo | Valor |
|---|---|
| job_id | `c45da7bb0fcb` |
| nome | `LK Stock OS Supabase read-model sync hourly` |
| script | `lk_stock_os_supabase_sync.py` |
| último run | `2026-06-28T16:20:33Z` |
| status | `ok`, silent output |

Mas o script atual:

```text
/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py
```

é um **readback gate**:

- lê `public.lk_stock_snapshots`/`public.lk_stock_items`
- valida contagens e guardrails
- valida sentinela MR530SG
- não busca Hub `/api/lk-stock/lookup?q=all&limit=20000`
- não faz upsert/delete/insert em Supabase

Execução manual `--verbose` confirmou:

```json
{
  "status": "ok",
  "run_id": "20260626T092006Z",
  "items": 8550,
  "total_count": 8550,
  "result_count": 8550,
  "guardrails": {
    "tiny_write": 0,
    "shopify_write": 0,
    "supabase_write": 0,
    "public_availability_promise": 0
  }
}
```

Isso é “snapshot antigo consistente”, não sync ativo.

### 6) Inventory Hub lê Supabase corretamente, mas Supabase está stale

Código do Hub:

```text
/opt/data/worktrees/lk-stock/inventory-hub/src/stock-os.js
```

Comportamento observado:

- quando `SUPABASE_LK_URL` + `SUPABASE_LK_SERVICE_KEY` estão configurados, Hub usa Supabase como fonte primária;
- lê `lk_stock_snapshots` latest;
- depois lê `lk_stock_items` filtrando `snapshot_run_id` do latest;
- portanto, se Supabase está stale, o Hub também fica stale.

## MR530SG

Supabase atual contém MR530SG corretamente no snapshot antigo:

| Métrica MR530SG | Valor |
|---|---:|
| rows | 9 |
| units | 11 |
| positive_rows | 8 |

Então o bug histórico “aparecia só 2” já foi corrigido no read path. O problema atual é **freshness/real-time**, não esse SKU especificamente.

## Root cause provável

1. Webhooks existem.
2. Endpoint funciona.
3. Processor está em dry-run por design.
4. Eventos válidos atualizam somente local SQLite/ledger.
5. Cron Supabase foi degradado/alterado para readback-only gate.
6. Inventory Hub lê Supabase, mas Supabase só tem snapshot de `2026-06-26`.

Logo: **a sincronização real-time não fecha o ciclo até Supabase/Hub**.

## Correção necessária — requer aprovação separada

Restaurar/promover uma pipeline segura de sync para Supabase:

### Opção A — Snapshot recorrente do Hub/Stock OS para Supabase

Reimplementar o contrato documentado:

1. fetch server-side do Stock OS full feed (`q=all&limit=20000`) com auth correta;
2. validar `result_count == total_count == len(results)` e `truncated=false`;
3. criar novo `snapshot_run_id`;
4. inserir/upsert `lk_stock_snapshots`;
5. replace/insert `lk_stock_items` para o snapshot;
6. readback counts/guardrails;
7. Hub passa a ler latest fresco.

Risco: Supabase write. Exige aprovação.

### Opção B — Event delta bridge para Supabase

Promover `lk_shopify_tiny_stock_sync_dryrun.py` para, após Tiny match OK:

1. atualizar uma tabela de delta/eventos Supabase;
2. ou gerar novo snapshot parcial seguro;
3. Hub mescla latest snapshot + deltas.

Risco maior de consistência/merge. Exige desenho e aprovação.

## Recomendação

Escolher **Opção A primeiro**: restaurar snapshot Supabase recorrente, porque é mais simples e preserva o Hub como leitor de snapshot completo. Depois, se necessário, evoluir para deltas real-time.

## Guardrails preservados neste audit

- Shopify write: `0`
- Tiny write: `0`
- Supabase write: `0`
- Mensagens externas: `0`
- Secrets/tokens impressos: `0`
- `values_printed=false`
