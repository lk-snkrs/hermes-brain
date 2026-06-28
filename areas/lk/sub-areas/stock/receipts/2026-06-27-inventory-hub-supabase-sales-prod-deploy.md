# Receipt — Inventory Hub hub.lksnk.dev deployed with Supabase-first Sales OS

- Data/hora: 2026-06-27T14:50:49Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Inventory Hub/Supabase
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou deploy e reforçou: 'Lembra que tudo deve ser no github'. Escopo: hub.lksnk.dev usando Supabase como base confiável.
- Classificação: external-write
- Fontes usadas:
- GitHub repo lk-snkrs/inventory-hub; Vercel project inventory-hub; hub.lksnk.dev live APIs; Supabase read model lk_shopify_sales_* and Stock OS; npm test
- O que foi feito:
- Commitado e enviado ao GitHub em dev e production; deploy Vercel production executado; alias hub.lksnk.dev atualizado; endpoints de Vendas migrados para Supabase-first: summary, products, analytics, shopify-sales-os, search, product-360, queues, alerts, health e executive-summary; Stock OS e Compras verificados.
- Output/artefato:
- Commit production b55214d469be4aaac7525b42d47a02142ef94944; Vercel production URL https://inventory-oa29dy5yc-lk-snkrs-projects.vercel.app aliased para https://hub.lksnk.dev; npm test: 49/49 pass; live /api/vendas/summary source=supabase_lk_shopify_sales_os; /api/vendas/analytics source=supabase_lk_shopify_sales_os; /api/vendas/shopify-sales-os source=supabase_direct_shopify_sales_os totals orders=2075 revenue=6822723.07 units=2831; /api/vendas/search source=supabase_direct_shopify_sales_os_paid_active_line_items products=1709; /api/lk-stock/lookup total=12592; /compras/api/health store=supabase.
- Aprovação: Aprovação explícita atual de Lucas no Telegram: 'Aprovo deploy… Lembra que tudo deve ser no github'. Escopo: deploy produção do Hub hub.lksnk.dev com Supabase como base confiável.
- Envio/publicação: Telegram final report only
- Writes externos: GitHub push para dev/production; Vercel production deploy/alias hub.lksnk.dev; Supabase only read by Hub during verification; Shopify/Tiny/customer-facing write 0; secrets not printed.
- Riscos/bloqueios: Deploy executado via Vercel CLI após commit/push GitHub porque live alias continuava stale após push. O código fonte canônico está no GitHub; .vercel env local removido. Guardrails de disponibilidade pública continuam bloqueados.
- Rollback/mitigação: Rollback: reverter production para commit anterior cc3e8eb ou redeploy Vercel do deploy anterior; código atual em GitHub commit b55214d. Sem alterações Tiny/Shopify.
- Próximos passos: Monitorar próxima leitura normal; healthy fica silent-OK. Se Lucas pedir, fazer auditoria visual/browsed UI completa do dashboard.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
