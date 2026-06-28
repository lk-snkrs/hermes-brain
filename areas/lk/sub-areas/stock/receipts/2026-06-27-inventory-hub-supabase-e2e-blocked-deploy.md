# Receipt — Inventory Hub Supabase E2E verified; public Sales OS deploy pending

- Data/hora: 2026-06-27T14:02:16Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Inventory Hub/Supabase
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu linha final/E2E em todo o sistema e dashboard Inventory Hub para usar Supabase como base confiável.
- Classificação: local-write
- Fontes usadas:
- Supabase readback via MCP/Doppler; hub.lksnk.dev public smoke; local inventory-hub tests; local app smoke; cron registry; Docker read-only inspect
- O que foi feito:
- Verificado Stock OS, Sales OS, Compras e Hub público; identificado que Hub público Vendas ainda lê fonte legada shopify_sales_os_db; preparada correção local no repo inventory-hub para endpoints de Vendas lerem lk_shopify_sales_* via Supabase server-side; testes locais passaram.
- Output/artefato:
- Stock public OK total=12592; Compras public OK store=supabase; Sales OS Supabase direct OK orders=2074 search_items=1709; Hub público Vendas stale: summary source=shopify_sales_os_db generated_at=2026-06-22, search source=shopify_sales_os_db_paid_active_line_items generated_at=2026-06-14. Local patched app OK source=supabase_direct_shopify_sales_os. npm test: 49 pass, 0 fail.
- Aprovação: Pendente: deploy produção/hub.lksnk.dev exige aprovação escopada de Lucas.
- Envio/publicação: Telegram report/approval request
- Writes externos: 0
- Riscos/bloqueios: Sem deploy, hub.lksnk.dev continua mostrando Vendas stale/legado apesar de Supabase estar correto. Deploy deve ser limitado a src/sales-read-model.js e src/index.js e verificado por smoke público.
- Rollback/mitigação: Rollback de código: git restore src/sales-read-model.js src/index.js no worktree inventory-hub antes de deploy; se deploy aprovado e falhar, reverter commit/deploy anterior do inventory-hub.
- Próximos passos: Lucas aprovar deploy do patch inventory-hub para produção; depois executar smoke público e receipt final done.
- Onde foi documentado no Brain: Report: areas/lk/sub-areas/stock/reports/2026-06-27-inventory-hub-supabase-e2e-line-check.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
