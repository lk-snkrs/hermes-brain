# Receipt — LK Shopify Sales OS nightly reconcile fixed

- Data/hora: 2026-06-27T12:55:29Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Sales OS/Shopify
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu corrigir o Sales OS depois da correção do Stock OS/Supabase.
- Classificação: local-write
- Fontes usadas:
- cronjob registry; runtime script execution; Shopify read-only Admin GraphQL through Doppler env; SQLite Sales OS local readback; generated summary/search/analytics files
- O que foi feito:
- Corrigido cron script lk_shopify_sales_os_nightly_reconcile.py: analytics enrichment agora roda antes do export-search-index para criar a view shopify_sales_paid_line_items_enriched; live latest-order readback usa Admin GraphQL read-only com token via Doppler; script rodou com stdout silencioso e exit 0; cron 2fd03de2c8b8 rerodado com last_status=ok; skill lk-shopify-readonly atualizada com pitfall/ordem correta.
- Output/artefato:
- Last report status=ok em 2026-06-27T12:54:06Z; backfill scanned=2395 ignored=2395; summary orders=2074 revenue=6821898.08 units=3504; search index items=1706; analytics requested_products=823 synced_products=823 missing=0; latest_order=#147950 gid://shopify/Order/7440594796766; cron last_run_at=2026-06-27T12:54:06Z last_status=ok.
- Aprovação: Lucas autorizou no Telegram: Então corrigir tbm o Sales OS. Escopo executado: correção local/read-only do cron Sales OS, sem mutation Shopify/Tiny e sem envio externo.
- Envio/publicação: Telegram final report only
- Writes externos: nenhum
- Riscos/bloqueios: Sales OS ainda usa SQLite local como datastore analítico local; diferente do Stock OS Supabase read model. Isso foi mantido porque Sales OS cron/artefatos ainda são locais e read-only.
- Rollback/mitigação: Reverter /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py: voltar export-search-index para antes do analytics enrich e voltar live_latest_order ao Shopify CLI store execute se necessário; reverter pitfall adicionado na skill lk-shopify-readonly. Como a correção é read-only/local, rollback não exige Shopify/Tiny write.
- Próximos passos: Próxima execução automática em 2026-06-28T05:40:00Z; healthy cron fica silent-OK.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer e pitfall registrado na skill lk-shopify-readonly.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
