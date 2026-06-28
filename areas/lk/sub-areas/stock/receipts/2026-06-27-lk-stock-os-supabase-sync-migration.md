# Receipt — LK Stock OS Supabase recurring sync migration

- Data/hora: 2026-06-27T11:14:50Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Supabase/Inventory Hub
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou seguir com a migração dos syncs Stock OS para Supabase.
- Classificação: external-write
- Fontes usadas:
- Supabase MCP execute_sql/list_tables; Hub Stock OS lookup endpoint; cronjob registry; script dry-run/live run; Doppler profile injection
- O que foi feito:
- Criado script /opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py; validado dry-run; executado sync live; removida duplicidade inicial de lk_stock_items importada em 2026-06-27; atualizado cron c45da7bb0fcb para LK Stock OS Supabase read-model sync hourly; forçado run do cron e verificado last_status=ok; Gate B reconcile também rerodado e ficou ok.
- Output/artefato:
- Source Hub retornou result_count=12592 e total_count=12592; Supabase MCP confirmou lk_stock_snapshots run_id=20260626T092006Z com snapshot_count=1, lk_stock_items item_count=12592, public_availability_sum=0, availability_claim_sum=0; cron c45da7bb0fcb last_run_at=2026-06-27T11:12:34Z last_status=ok; values_printed=false.
- Aprovação: Aprovação explícita de Lucas no Telegram: 'Seguir aprovado'. Escopo executado: migrar sync recorrente Stock OS para Supabase read-model tables e verificar; DB writes limitados a public.lk_stock_snapshots/public.lk_stock_items; nenhum Tiny/Shopify/customer-channel write.
- Envio/publicação: Telegram final report only
- Writes externos: Supabase writes: upsert/replace read model in lk_stock_snapshots and lk_stock_items; cron registry update local; Tiny write 0; Shopify write 0; public availability promise 0.
- Riscos/bloqueios: O sync usa Hub Stock OS lookup como fonte viva do read model; Tiny continua fonte de verdade de estoque upstream. Se a ordem da API mudar, o script substitui rows por snapshot_run_id antes de reinserir para evitar duplicidade.
- Rollback/mitigação: Restaurar backup /opt/data/profiles/lk-stock/backups/stock-os-supabase-sync-20260627T110623Z/lk_stock_tiny_full_sync_nightly.py.bak e reverter cron c45da7bb0fcb para script antigo se necessário; Supabase read model pode ser reexecutado a partir do Hub para recompor.
- Próximos passos: Monitorar próxima execução agendada às 11:20 UTC; healthy sync fica silent-OK. O cron Shopify Sales OS ainda aparece error e é frente separada.
- Onde foi documentado no Brain: Referência inventory-hub-vps-to-supabase-phases-2-4 atualizada; receipt via Memory OS writer; valores sensíveis impressos=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
