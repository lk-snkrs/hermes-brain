# Receipt — Shopify Sales OS category fallback refinement

- Data/hora: 2026-06-14T15:12:47.201482+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Lucas pediu seguir após o upgrade de product_type/tags, então refinamos os unknown/ambiguous restantes.
- Classificação: local-write
- Fontes usadas:
- SQLite local shopify_sales_os.db; Shopify product metadata já sincronizada read-only; script shopify_sales_analytics_enrich.py; wrapper cron lk_shopify_sales_os_nightly_reconcile.py. values_printed=false.
- O que foi feito:
- Revisados unknown/ambiguous; ajustadas regras determinísticas: boné/meia/luva/espelho/pingente/colecionável/manutenção como acessório; dockside/moc toe/tokyo mj/Sézane x New Balance como calçado; pulôver/cueca/apparel como roupa; frete/crédito como service_non_product/outros; removido brush genérico para não confundir KITH Brush Tee.
- Output/artefato:
- Após refresh: requested_products=794 synced_products=794 missing_products=0; dimension_rows_processed=1894; dimension_table_rows=1866; ambiguous=0; unknown=1 apenas 'Motoca'; category_source shopify_product_type_tags_v1=1763, heuristic direct=100, service_non_product=2; paid_totals orders=1809 units=2688 revenue=6244609.22; by_category calcado=2005 units/R730436.39, roupa=504/R20203.65, acessorio=176/R2769.18, outros=3/R200.00; wrapper smoke rc=0.
- Aprovação: Aprovado por Lucas no Telegram: 'Seguir'. Escopo local/read-only, sem writes Shopify/Tiny.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Uma linha permanece unknown/outros ('Motoca') sem metadata Shopify, vendor ou SKU; não classifiquei sem evidência. Totais mudaram levemente por novo pedido/backfill antes do refresh; usar paid/enriched view como fonte.
- Rollback/mitigação: Reverter commit Brain ou remover regras novas; rodar shopify_sales_analytics_enrich.py refresh --with-shopify-products para recomputar estado anterior.
- Próximos passos: Se Lucas quiser precisão 100% visual/manual, definir categoria manual para 'Motoca' ou criar tabela manual overrides auditável.
- Onde foi documentado no Brain: Receipt criado; report shopify_sales_analytics_readiness.json atualizado; skill lk-stock atualizada com baseline de fallback refinado.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
