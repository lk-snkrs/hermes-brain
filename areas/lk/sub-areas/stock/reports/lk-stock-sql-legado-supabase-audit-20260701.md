# Auditoria LK Stock — SQL legado vs Supabase

Data: 2026-07-01
Perfil: `lk-stock`
Escopo: scripts runtime LK Stock/POS, scripts do profile `lk-stock`, Brain `areas/lk/sub-areas/stock`, crons ativos e Inventory Hub (`/opt/data/worktrees/lk-stock/inventory-hub`).

## Resumo executivo

- O read model canônico de estoque para consulta operacional agora é Supabase: `public.lk_stock_snapshots` + `public.lk_stock_items`.
- O bug `U204LMMC-6` aconteceu porque um fluxo ainda dependia do ponteiro SQLite legado (`artifacts.sqlite_db`) mesmo com o Stock OS local decommissioned.
- Há SQL legado ainda em uso, mas em três classes diferentes:
  1. **perigoso/precisa migrar**: qualquer coisa que decide estoque/pronta entrega/POS a partir de SQLite local.
  2. **tolerado temporariamente**: cache/ledger local read-only ou fixture/teste sem promessa pública.
  3. **obsoleto/arquivo histórico**: backups e DBs antigos que não devem ser fonte viva.
- Supabase já cobre: Stock OS snapshot/items, Shopify Sales OS e Compras Hub.

## Evidência Supabase atual

Consulta live no Supabase:

| Tabela | Linhas |
|---|---:|
| `lk_stock_snapshots` | 1 |
| `lk_stock_items` | 8550 |
| `lk_shopify_sales_orders` | 2431 |
| `lk_shopify_sales_order_line_items` | 3536 |
| `lk_compras_pedidos` | 95 |
| `lk_compras_itens` | 120 |

Latest `lk_stock_snapshots`:

| Campo | Valor |
|---|---|
| `run_id` | `20260626T092006Z` |
| `status` | `confirmado` |
| `source` | `Stock OS DB` |
| `freshness` | `tiny_full_sync_nightly` |
| `source_observed_at` | `2026-06-26 09:20:06+00` |
| `imported_at` | `2026-07-01 14:20:37.507302+00` |
| items | 8550 |
| linhas com estoque positivo | 603 |
| unidades | 901.0 |
| `public_availability_safe` sum | 0 |
| `availability_claim_allowed` sum | 0 |

## Crons ativos

| Job | Script | Status atual | Classificação |
|---|---|---|---|
| LK Stock OS Supabase read-model sync hourly | `lk_stock_os_supabase_sync.py` | **error** no último run; readback-only OK | Supabase canônico, mas fonte upstream/sentinel precisa correção |
| LK Stock Gate B daily freshness reconcile | `lk_stock_gate_b_daily_reconcile.py` | OK/silent | SQLite local tolerado temporariamente; não deve decidir POS |
| LK Shopify Sales OS nightly full reconcile | `lk_shopify_sales_os_nightly_reconcile.py` | OK/silent | Supabase direto, sem SQLite |
| LK Supabase public exposure security gate | `lk_supabase_security_gate_daily.py` | error | não é SQL legado; é hardening/security gate |

Verificação executada:

- `hermes-cli-integrations smoke supabase`: OK, `values_printed=false`.
- `lk_stock_os_supabase_sync.py --readback-only --verbose`: OK, 8550 items, sentinel MR530SG OK, `supabase_write=0`.
- `lk_stock_os_supabase_sync.py --dry-run --verbose`: falhou em `source_mr530sg_sentinel_failed:rows=98:units=0`; não escreveu Supabase/Tiny/Shopify.

## Achados classificados

### P0 — precisa migrar/remover do caminho decisório de estoque

| Superfície | Arquivo | SQL legado | Risco | Recomendação |
|---|---|---|---|---|
| POS restock preflight | `/opt/data/scripts/lk_store_sale_restock_alert.py` | `current_stock_db_path()`, `run_stock_os_prefix_repair()`, `artifacts.sqlite_db` | Alto: tenta reparar/validar POS via SQLite local que foi decommissioned | Migrar preflight para Supabase/Hub sync; quando missing, abrir alerta `lk-stock`/sync, não crosswalk SQLite |
| POS/WhatsApp responder fallback | `/opt/data/scripts/lk_hermes_whatsapp_responder.py` | `lk_stock_os_local_lookup()`, `current_local_stock`, `stock_cache.sqlite`, `lk_tiny_stock_local.sqlite` | Médio/alto: Supabase já está primário, mas fallback local pode mascarar falha do read model | Manter só como fallback diagnóstico por curto prazo; remover do alerta POS depois que Supabase sync estiver estável |
| Stock OS API adapter legado | `areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py` | `artifacts.sqlite_db`, `current_local_stock` | Alto se usado por algum endpoint/runtime | Decommissionar ou trocar internamente para Supabase (`lk_stock_items`) |
| Full sync nightly antigo | `/opt/data/profiles/lk-stock/scripts/lk_stock_tiny_full_sync_nightly.py` | lê ponteiro SQLite e `current_local_stock` para shard | Alto se reativado; hoje conflita com pointer decommissioned | Substituir por sync Supabase direto / remover do runtime |

### P1 — migrar para Supabase ou arquivar formalmente

| Superfície | Arquivo/DB | Uso atual | Recomendação |
|---|---|---|---|
| Gate B local cache | `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite` + `lk_stock_gate_b_daily_reconcile.py` | SQLite local com 12 tabelas, 13 ledger events, 3 scores, 3 receipts | Migrar ledger/receipts/scores para Supabase ou Brain; manter somente até fim da transição |
| Gate B schema/modules | `stock_local_db.py`, `stock_score.py`, `stock_webhook_ingest.py` | SQLite local para eventos, variants, scores | Migrar se ainda houver pipeline ativo; senão arquivar como legado Gate B |
| Tiny sync runtime | `areas/lk/sub-areas/stock/scripts/lk_stock_tiny_sync_processor.py` + `/opt/data/hermes_bruno_ingest/local_sql/lk_stock_tiny_sync/runtime.db` | ledger local (`tiny_stock_event_ledger`, `tiny_stock_latest`) | Se eventos Tiny continuarem, sink deve ser Supabase; local só idempotência temporária |
| Tiny events processor | `lk_stock_tiny_events_processor.py` | runtime SQLite event ledger | Mesma recomendação: Supabase/ledger central ou arquivo |
| Internal consult overlay | `lk_stock_os_internal_consult_overlay.py` | lê/escreve overlay em DB local apontado | Migrar overlay/decisões para Supabase ou Brain; não usar como fonte POS |

### P2 — legado tolerado/cache, sem urgência se não decidir disponibilidade

| Superfície | Arquivo/DB | Evidência | Guardrail |
|---|---|---|---|
| WhatsApp/Tiny local cache | `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite` | 1211 linhas `stock_by_sku` | Só cache interno; não usar para alerta POS como base correta |
| WhatsApp stock cache | `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/stock_cache.sqlite` | 1211 linhas `stock_cache` | Cache; TTL/fonte viva antes de promessa |
| `/opt/data/scripts/lk_tiny_stock_local_db.py` | SQLite wrapper local Tiny | útil para fallback/diagnóstico | Não promover a fonte primária |
| `/opt/data/scripts/lk_tiny_stock_fullsync.py` | lê `lk_os_phase5.sqlite` e grava local Tiny cache | pipeline histórico/atendimento | Migrar quando precisar de fonte oficial; bloquear para POS |
| Testes POS | `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py` | SQLite fixtures | OK: fixture/regressão, não runtime |

### P3 — obsoleto/histórico; não migrar, arquivar

| Artefato | Estado |
|---|---|
| `/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups/*.sqlite` | backups históricos |
| `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite` | DB grande legado com clientes/pedidos/produtos/stock; não usar como fonte LK Stock atual |
| `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260626T102006Z.db` | arquivo 0 bytes; forte candidato a remover/arquivar após backup |
| receipts/reports antigos apontando DB local | histórico documental; manter como evidência, não runtime |

### Já migrado / Supabase-first

| Superfície | Arquivo | Status |
|---|---|---|
| Inventory Hub Stock OS client | `/opt/data/worktrees/lk-stock/inventory-hub/src/stock-os.js` | Supabase-first quando `SUPABASE_LK_URL` + service key configurados; upstream só diagnóstico |
| Stock snapshot sync | `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py` | escreve/readback Supabase `lk_stock_snapshots`/`lk_stock_items` |
| Shopify Sales OS nightly | `lk_shopify_sales_os_nightly_reconcile.py` | modo `supabase_direct_no_sqlite` |
| Shopify Sales OS direct | `lk_shopify_sales_os_supabase_direct.py` | cria/escreve tabelas Supabase `lk_shopify_sales_*`; Shopify via broker CLI |
| Compras Hub | `inventory-hub/src/compras/supabase-store.cjs` | Supabase-only; DB local `lk-compras.db` está vazio |

## DBs locais encontrados

| Caminho | Tamanho | Tabelas/linhas relevantes | Classificação |
|---|---:|---|---|
| `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite` | 135 KB | `event_ledger=13`, `scores=3`, `receipts=3` | P1 transição |
| `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite` | 89.7 MB | clientes/pedidos/produtos/stock legado | P3 histórico/legado |
| `/opt/data/hermes_bruno_ingest/local_sql/lk_stock_tiny_sync/runtime.db` | 40 KB | `tiny_stock_event_ledger=6`, `tiny_stock_latest=3` | P1 se ativo |
| `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite` | 446 KB | `stock_by_sku=1211`, `stock_events=59` | P2 cache |
| `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/stock_cache.sqlite` | 204 KB | `stock_cache=1211` | P2 cache |
| `/opt/data/worktrees/lk-stock/inventory-hub/src/compras/lk-compras.db` | 73 KB | tabelas vazias | P3 obsoleto/teste/local dev |

## Resposta direta: temos que migrar para Supabase?

Sim, mas não tudo com a mesma urgência.

Migrar/agora:
1. qualquer decisão de estoque/POS/pronta entrega que ainda dependa de `current_local_stock`, `artifacts.sqlite_db` ou `lk_tiny_stock_local.sqlite`;
2. `lk_store_sale_restock_alert.py` preflight/repair;
3. `lk_stock_api_adapter.py`, se ainda estiver exposto/consumido;
4. o fallback local do responder depois que o sync Supabase estiver estável.

Manter temporariamente:
1. caches locais de WhatsApp/atendimento;
2. Gate B local se for só ledger/diagnóstico;
3. testes/fixtures SQLite.

Não migrar; arquivar:
1. backups SQLite;
2. DBs vazios/obsoletos;
3. relatórios antigos que citam local DB.

## Plano recomendado

### Fase 0 — já aplicado no bug U204LMMC
- POS restock consulta Supabase primeiro.
- Tiny local cache deixou de ser fonte primária do alerta.

### Fase 1 — P0, imediata
- Trocar `lk_store_sale_restock_alert.py` preflight local repair por fluxo Supabase:
  - consultar `lk_stock_items` por SKU/tamanho;
  - se missing, disparar sync/alerta de fonte Stock OS/Hub;
  - nunca tentar promover ponteiro SQLite quando `sqlite_db=null`.
- Desativar/retirar `lk_stock_api_adapter.py` legado se não houver consumidor real; se houver, portar para Supabase.
- Corrigir o cron `LK Stock OS Supabase read-model sync hourly`: readback está OK, mas `--dry-run` da fonte falha no sentinel MR530SG (`rows=98`, `units=0`).

### Fase 2 — P1, transição controlada
- Migrar Gate B ledger/scores/receipts para Supabase ou Brain.
- Migrar Tiny event ledgers (`lk_stock_tiny_sync_processor.py`, `lk_stock_tiny_events_processor.py`) para Supabase se esses eventos continuarem úteis.

### Fase 3 — limpeza
- Arquivar/remover DB 0 bytes e backups locais fora do runtime.
- Renomear documentação ambígua que ainda contém `tiny-readback-fallback` no nome.
- Adicionar teste global: se pointer tiver `sqlite_db=null`, nenhum alerta POS pode retornar `não encontrado` sem tentar Supabase.

## Guardrails

- Não foi executado write em Tiny, Shopify, WhatsApp, cliente, supplier ou campanha.
- Supabase writes nesta auditoria: 0.
- Consultas foram read-only; `values_printed=false`.
- Secrets não foram impressos.
