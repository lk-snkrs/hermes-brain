# Receipt — LK Shopify Sales OS migrated to Supabase read model

- Data/hora: 2026-06-27T13:23:49Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Sales OS/Supabase
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas determinou: 'Você deve migrar' o Sales OS para Supabase.
- Classificação: external-write
- Fontes usadas:
- SQLite Sales OS local; Shopify Sales OS summary/search/analytics artifacts; Supabase psql write/readback via Doppler; Supabase MCP read-only verification; Hermes cron registry
- O que foi feito:
- Criado script /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_sync.py; criadas 8 tabelas Supabase prefixadas lk_shopify_sales_; RLS habilitado e grants anon/authenticated removidos; dados atuais migrados; cron lk_shopify_sales_os_nightly_reconcile.py passou a executar sync Supabase em toda rodada; cron 2fd03de2c8b8 rerodado com last_status=ok.
- Output/artefato:
- Supabase readback: orders=2396, line_items=3485, paid_enriched=2815, product_dimensions=1949, product_metadata=823, search_items=1706, event_ledger=2559, snapshots=1, public_grants=0. Last report supabase_sync status=ok em 2026-06-27T13:21:44Z. Cron Sales OS last_run_at=2026-06-27T13:23:09Z last_status=ok.
- Aprovação: Aprovação explícita atual de Lucas no Telegram: 'Você deve migrar'. Escopo: migrar Sales OS para Supabase read model, sem Shopify/Tiny write e sem envio externo.
- Envio/publicação: Telegram final report only
- Writes externos: Supabase DDL/DML em public.lk_shopify_sales_*; Shopify write 0; Tiny write 0; customer-facing send 0; secrets not printed.
- Riscos/bloqueios: Local SQLite shopify_sales_os.db permanece como staging/cache do backfill read-only e geração de artefatos; o read model operacional agora existe no Supabase e é atualizado pelo cron. Remover totalmente SQLite exigiria reescrever o ingestor/backfill, não apenas migrar o read model.
- Rollback/mitigação: Tabelas Supabase são prefixadas lk_shopify_sales_; rollback seguro é pausar sync e dropar/truncar apenas essas tabelas, preservando SQLite local e artefatos existentes. Script novo pode ser removido e chamada supabase_sync retirada do nightly.
- Próximos passos: Se Lucas quiser descontinuar também o SQLite staging do Sales OS, próxima etapa é reescrever ingest/backfill para gravar diretamente em Supabase e só então remover shopify_sales_os.db.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; cron e Supabase verificados em runtime.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
