# Receipt — Shopify Sales OS product_type tags enrichment activated

- Data/hora: 2026-06-14T14:34:53.569294+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Ativar o upgrade sugerido para enriquecer categorias da Sales OS com product_type/tags oficiais do Shopify em modo read-only.
- Classificação: local-write
- Fontes usadas:
- Shopify Admin GraphQL read-only via hermes-cli-run/Doppler; SQLite local shopify_sales_os.db; script shopify_sales_analytics_enrich.py; wrapper cron lk_shopify_sales_os_nightly_reconcile.py. values_printed=false.
- O que foi feito:
- Adicionada tabela local shopify_sales_product_metadata; sincronização read-only de product_type/tags/handle/status/updatedAt; dimensão e views passam a usar Shopify product_type/tags quando disponíveis e heurística local como fallback; reconcile noturno chama enrichment com --with-shopify-products.
- Output/artefato:
- Sincronização verificada: requested_products=794, synced_products=794, missing_products=0; metadata_rows=794; with_product_type=772; coverage products_in_sales=794/794; category_source shopify_product_type_tags_v1=1727 linhas, heuristic fallback=137 linhas; paid_totals orders=1808 units=2687 revenue=6242109.23; NB9060 last3 paid orders=110 units=135 revenue=337428.67; wrapper smoke rc=0.
- Aprovação: Aprovado por Lucas no Telegram: 'Fazer gostei da sugestão do upgrade'. Escopo read-only Shopify + writes locais derivados; sem write Shopify/Tiny.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: 772/794 produtos têm product_type oficial; produtos sem product_type ou casos não mapeados continuam usando fallback heurístico identificado por category_source. Categoria ainda não usa cost/margem.
- Rollback/mitigação: Reverter commit Brain; remover chamada --with-shopify-products do wrapper; dropar tabela shopify_sales_product_metadata e colunas/relatório derivado se necessário; rodar refresh heurístico anterior.
- Próximos passos: Opcional: revisar os 24 unknown e 5 ambiguous por regra manual/categoria canônica se Lucas quiser máxima precisão.
- Onde foi documentado no Brain: Receipt criado; report shopify_sales_analytics_readiness.json atualizado; skill lk-stock atualizada para usar product_type/tags oficiais quando disponíveis.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
