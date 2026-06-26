# Receipt — Shopify Sales OS audited category overrides

- Data/hora: 2026-06-14T15:24:28.510613+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Lucas pediu seguir após o refinamento; criar camada auditável para resolver o último unknown sem chute.
- Classificação: local-write
- Fontes usadas:
- SQLite local shopify_sales_os.db; report de unknown/ambiguous; arquivo local shopify_sales_category_overrides.json; script shopify_sales_analytics_enrich.py; wrapper reconcile. values_printed=false.
- O que foi feito:
- Criada tabela shopify_sales_category_overrides e arquivo JSON versionado de overrides auditáveis; aplicado override estreito para product_key title:Motoca|sku: como category=outros/source=manual_review_no_product_metadata_v1, mantendo motivo e aprovação; refresh usa overrides antes de regras automáticas.
- Output/artefato:
- Motoca investigado: 1 linha POS paga #146210 em 2026-02-12, sem product_id, variant_id, sku, vendor, product_type ou tags; classificado como outros/manual-review, não como produto específico. Após refresh: requested_products=794 synced=794 missing=0; dimension_rows_processed=1894; dimension_table_rows=1866; unknown=0; ambiguous=0; paid_totals orders=1809 units=2688 revenue=6244609.22; wrapper smoke rc=0.
- Aprovação: Aprovado por Lucas no Telegram: 'Seguir'. Escopo local/read-only; sem writes Shopify/Tiny.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Override manual é propositalmente estreito e auditável; se aparecer metadata real para Motoca no futuro, revisar override. Totais pagos atuais refletem a base após último backfill.
- Rollback/mitigação: Remover entrada do JSON de overrides ou reverter commit; rodar refresh --with-shopify-products para recomputar classificação automática.
- Próximos passos: Opcional: criar CLI/listagem periódica para overrides quando surgirem novos unknowns; por ora unknown/ambiguous estão zerados.
- Onde foi documentado no Brain: Receipt criado; shopify_sales_category_overrides.json versionado; skill lk-stock atualizada com padrão de manual overrides.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
