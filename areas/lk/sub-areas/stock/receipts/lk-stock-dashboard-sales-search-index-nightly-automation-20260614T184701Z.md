# Receipt — LK Stock dashboard sales search index nightly automation

- Data/hora: 2026-06-14T18:47:15.298203+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock / Dashboard
- Responsável humano: Hermes lk-stock
- Pedido original: Automatizar atualização do índice da busca comercial/Product 360 no full sync noturno
- Classificação: local-write
- Fontes usadas:
- Cron LK Shopify Sales OS nightly full reconcile read-only; wrapper /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py; Shopify Sales OS DB local; smoke produção autenticado
- O que foi feito:
- Wrapper noturno atualizado para rodar export-search-index após export-summary, validar items > 0, registrar search_index no runtime report e hot-refresh via docker cp para lk-estoque-web:/app/src/data/shopify_sales_search_index.json sem restart
- Output/artefato:
- Smoke limitado exit 0/stdout vazio; runtime JSON status ok com search_index.items=1632; produção /api/vendas/search retornou 200/matches=3; Product 360 retornou 200/confirmado_stock_os; unauth 401 preservado
- Aprovação: Lucas pediu: Seguir, automatize por favor. Escopo local/read-only/dashboard; sem writes Shopify/Tiny e sem contato externo.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Primeiro run automático do cron às 05:40 UTC ainda será observado pelo próprio cron; hot-refresh usa docker cp no container atual e alerta em caso de falha. Produto 360 não autoriza promessa pública/reserva.
- Rollback/mitigação: Reverter /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py para versão anterior; o dashboard continua com último índice embutido; container não foi reiniciado nem recriado.
- Próximos passos: Aguardar primeiro run automático 05:40 UTC; próxima melhoria possível: montar volume read-only do Brain para evitar docker cp em deploy futuro.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/receipts/lk-stock-dashboard-sales-search-index-nightly-automation-20260614T184701Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
