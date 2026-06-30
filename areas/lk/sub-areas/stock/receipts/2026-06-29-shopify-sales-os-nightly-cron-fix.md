# Receipt — Shopify Sales OS nightly cron corrigido

- Data/hora: 2026-06-29T09:28:26.688450+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Lucas pediu corrigir o cron LK Shopify Sales OS nightly full reconcile read-only que estava em erro.
- Classificação: external-write
- Fontes usadas:
- Cron output 2fd03de2c8b8/2026-06-29_05-40-18.md; Integration Auth Broker smoke shopify_lk status ok; Shopify official CLI probe; Doppler-injected Admin token GraphQL read-only probe; Supabase MCP readback; runtime last report.
- O que foi feito:
- Corrigido script /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py: API_VERSION default 2025-07 em vez de 2024-01; parser robusto para JSON do Shopify CLI com linhas de progresso; fallback read-only Admin GraphQL token apenas quando official CLI retorna ACCESS_DENIED em orders, com bloqueio explícito de mutation. Backups criados em /opt/data/profiles/lk-stock/backups/shopify-sales-os-cron-fix-20260629T091840Z.
- Output/artefato:
- Execução manual do nightly reconcile passou silent-OK exit 0. Last report status=ok, mode=supabase_direct_no_sqlite, scanned=2412, orders table=2412, line_items=3508, paid_enriched=2830, dimensions=1959, metadata=823, search_items=1718, public_grants=0. Summary: orders=2086, revenue=6862554.74, units=2845.0. Guardrails: shopify_write=0, tiny_write=0, external_write=0, public_availability_promise=0, auto_purchase=0, values_printed=false.
- Aprovação: Aprovação escopada recebida no Telegram neste turno: Lucas respondeu "Corrigir" ao resumo que indicava que o cron LK Shopify Sales OS nightly full reconcile read-only seguia em erro; escopo executado: corrigir o cron/read-model, sem Shopify/Tiny/customer-facing writes.
- Envio/publicação: Sem envio externo/customer-facing. Cron deliver=local; Telegram apenas para receipt/resumo.
- Writes externos: 0 Shopify writes, 0 Tiny writes. 1 atualização server-side do Supabase read-model lk_shopify_sales_* pelo reconcile existente; public_grants=0.
- Riscos/bloqueios: Fallback raw Admin GraphQL é read-only e limitado a continuidade do Sales OS porque OAuth oficial do Shopify CLI autentica shop { id } mas retorna ACCESS_DENIED para orders; registrar necessidade futura de reparar escopo OAuth do broker para orders.
- Rollback/mitigação: Restaurar scripts a partir de /opt/data/profiles/lk-stock/backups/shopify-sales-os-cron-fix-20260629T091840Z e rerodar reconcile; não há rollback Shopify porque não houve Shopify write.
- Próximos passos: Manter cron agendado para 2026-06-30 05:40 UTC; se o broker OAuth ganhar read_orders, remover fallback raw e voltar a official CLI-only para orders.
- Onde foi documentado no Brain: Receipt canônico no Brain e skill lk-shopify-readonly atualizada com pitfall Sales OS API-version/scope.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
