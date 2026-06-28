# Receipt — LK Shopify Sales OS SQLite decommissioned; Supabase direct active

- Data/hora: 2026-06-27T13:38:28Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Sales OS/Supabase
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas determinou: 'Quero que descontínuas e migrar tudo pro supabase'.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin GraphQL read-only; Supabase psql/MCP readback; filesystem checks; cron runtime report; script search; receipt writer
- O que foi feito:
- Criado /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py com ingest direto Shopify read-only -> Supabase; reescrito cron lk_shopify_sales_os_nightly_reconcile.py para modo supabase_direct_no_sqlite; webhook wrapper /opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py não chama mais SQLite e aciona refresh Supabase; removido script legado lk_shopify_sales_os_supabase_sync.py; backup e delete do shopify_sales_os.db; skill lk-shopify-readonly atualizada para não reintroduzir SQLite.
- Output/artefato:
- Supabase readback: orders=2395, line_items=3483, paid_enriched=2813, search_items=1706, snapshots=1, public_grants=0. Runtime report: mode=supabase_direct_no_sqlite; source=shopify_admin_graphql_readonly; latest_order=gid://shopify/Order/7440594796766; summary orders=2073 revenue=6817938.08 units=2828.0. Filesystem: shopify_sales_os.db/db-wal/db-shm absent; old sync script absent.
- Aprovação: Aprovação explícita atual de Lucas no Telegram: 'Quero que descontínuas e migrar tudo pro supabase'. Escopo: descontinuar SQLite Sales OS e migrar fluxo ativo para Supabase, sem Shopify/Tiny write e sem envio externo.
- Envio/publicação: Telegram final report only
- Writes externos: Supabase DDL/DML em public.lk_shopify_sales_*; Shopify Admin GraphQL read-only; Shopify write 0; Tiny write 0; customer-facing send 0; secrets not printed.
- Riscos/bloqueios: Artefatos históricos/PRDs/testes no Brain ainda mencionam SQLite como histórico; fluxo ativo de cron/webhook não usa mais shopify_sales_os.db. O cronjob registry mostrou last_status ok anterior, mas o runtime report e execução direta pós-delete confirmaram sucesso; próxima execução agendada permanece 2026-06-28T05:40Z.
- Rollback/mitigação: Backup: /opt/data/profiles/lk-stock/backups/decommission-sales-os-sqlite-20260627T133527Z/shopify_sales_os.db.bak sha256 bad15a254c0b2316e34b2d8daacba87942fd028febc31cfbf0f01ecfffcb5ee5; script legado backup sha256 4392a61caf882fd7fc9da982ca10e3a97ccc4d0b463273964d2aa1f73801752b. Rollback: restaurar DB/script e reverter cron/webhook se necessário.
- Próximos passos: Monitorar próxima execução automática; healthy fica silent-OK. Se dashboard/API tiver código lendo SQLite diretamente fora destes wrappers, migrar esse consumidor para lk_shopify_sales_* Supabase.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer e skill lk-shopify-readonly atualizada.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
