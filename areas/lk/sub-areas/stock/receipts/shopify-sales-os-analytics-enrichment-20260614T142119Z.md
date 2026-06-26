# Receipt — Shopify Sales OS analytics enrichment activated

- Data/hora: 2026-06-14T14:22:03.814306+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Melhorar a Sales OS DB para responder perguntas comerciais de categoria, canal, marca e modelo com filtros corretos.
- Classificação: local-write
- Fontes usadas:
- SQLite local shopify_sales_os.db; script local shopify_sales_analytics_enrich.py; wrapper cron lk_shopify_sales_os_nightly_reconcile.py; sem secrets impressos.
- O que foi feito:
- Criada dimensão local shopify_sales_product_dimension e views shopify_sales_line_items_enriched, shopify_sales_paid_line_items_enriched, shopify_sales_category_channel_summary e shopify_sales_brand_model_summary; criado report shopify_sales_analytics_readiness.json; wrapper noturno passou a rodar enrichment após backfill/export.
- Output/artefato:
- Analytics agora tem filtros padronizados para pedidos ativos + PAID, canal site/loja, categoria heurística, brand_group, model_family, audience e collab. Verificações finais: dimension_rows_processed=1892; dimension_table_rows=1864; null_categories=0; paid_totals orders=1808 units=2687 revenue=6242109.23; NB9060 last3 paid orders=110 units=135 revenue=337428.67; smoke cron rc=0.
- Aprovação: Aprovado por Lucas no Telegram: 'Melhore o que deve ser melhorado'. Escopo executado local/read-only; sem write Shopify/Tiny.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Categoria/modelo ainda são heurísticos por title/vendor/SKU até enriquecer product_type/tags oficiais Shopify; reportar como heurístico quando aplicável.
- Rollback/mitigação: Remover script/report e dropar views/tabela derivada shopify_sales_product_dimension; reverter commit Brain; wrapper noturno pode voltar a só backfill/export removendo chamada de enrichment.
- Próximos passos: Opcional: read-only Shopify product dimension com product_type/tags para transformar roupa/calçado/acessório em categoria canônica.
- Onde foi documentado no Brain: Receipt criado; skill lk-stock atualizada com regras de filtro PAID, canal e categorias heurísticas.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
