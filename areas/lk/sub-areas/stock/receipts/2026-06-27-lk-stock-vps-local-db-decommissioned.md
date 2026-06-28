# Receipt — LK Stock VPS/local stock DB decommissioned

- Data/hora: 2026-06-27T11:45:05Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Stock OS/Supabase
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou descontinuar e deletar a database local da VPS.
- Classificação: external-write
- Fontes usadas:
- filesystem checks; Supabase MCP readback; cronjob registry; Hub Stock OS lookup endpoint; script dry-run/live run
- O que foi feito:
- Backups criados; removidas DBs locais Stock OS/VPS ativas: Brain Stock OS local DBs, lk_tiny_stock_local.sqlite, stock_cache.sqlite e lk_stock_tiny_sync/runtime.db; removido snapshot contaminante local_sql_* do Supabase; ajustado pointer para Supabase read model; regravado cron script para não depender de SQLite local; cron c45da7bb0fcb rerodado e last_status=ok.
- Output/artefato:
- Arquivos locais alvo existem=False; Supabase local_sql snapshots/items=0; snapshot canônico 20260626T092006Z preservado com 12592 items; Hub /api/lk-stock/lookup voltou a source=Stock OS DB, result_count=12592,total_count=12592; cron c45da7bb0fcb last_run_at=2026-06-27T11:43:37Z last_status=ok.
- Aprovação: Aprovação explícita de Lucas no Telegram: 'A database local da VPs vai ser descontinuada ok? Pode deletar'.
- Envio/publicação: Telegram final report only
- Writes externos: Supabase delete/upsert limitado a lk_stock_snapshots/lk_stock_items para remover local_sql_* e recompor snapshot Stock OS DB; filesystem delete local com backup; Tiny write 0; Shopify write 0; public availability promise 0.
- Riscos/bloqueios: Cron usa endpoint Hub e PostgREST/Doppler fallback porque supabase CLI não estava disponível no wrapper; valores sensíveis não impressos. Outros bancos locais não relacionados a Stock OS não foram apagados.
- Rollback/mitigação: Backups: /opt/data/profiles/lk-stock/backups/decommission-local-stock-os-db-20260627T113518Z/local-stock-os-db-and-pointer.tar.gz e /opt/data/profiles/lk-stock/backups/decommission-vps-local-stock-db-20260627T114154Z/vps-local-stock-runtime-dbs.tar.gz; restaurar arquivos e reverter pointer/script se necessário.
- Próximos passos: Monitorar próxima execução do cron às 12:20 UTC; cron saudável fica silent-OK. Shopify Sales OS nightly segue frente separada em erro.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; pointer Stock OS marcado como supabase_read_model_sync_active_local_db_decommissioned.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
