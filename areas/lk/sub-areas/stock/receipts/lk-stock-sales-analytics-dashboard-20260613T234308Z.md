# Receipt — LK Stock dashboard: Vendas Analytics loja x site

- Data/hora: 2026-06-13T23:45:15.163066+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Estoque Web
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou evoluir a aba Vendas para analytics completo loja fisica x site, com historico local, distribuicao por categoria, marca e produto, mantendo topbar Estoque/Vendas e sem sidebar nova.
- Classificação: local-write
- Fontes usadas:
- Codigo LK-Estoque-Web-inicial; reports/lk-sales-reports 217 JSONs; container lk-estoque-web; smoke HTTPS autenticado; npm test.
- O que foi feito:
- Criado endpoint /api/vendas/analytics; read model historico multicanal; UI com Loja x Site, Categorias, Marcas e Produtos; corrigida selecao diaria para nao usar store_1930 como fonte principal; deploy Docker com labels Traefik restaurados.
- Output/artefato:
- Produção https://estoque.lkskrs.online validada: no-auth 401, auth 200, HTML contem analytics, /api/vendas/analytics 200, source local_sales_reports_history, periodo local 2026-05-15 a 2026-06-12, 28 dias, 335 pedidos, loja 40.78 por cento receita, online 59.22 por cento receita; guardrails todos 0.
- Aprovação: Lucas aprovou via Telegram: Aprovo; depois pediu seguir proximos passos.
- Envio/publicação: Dashboard interno atualizado; nenhum envio externo/customer-facing.
- Writes externos: 0
- Riscos/bloqueios: Historico anterior a fonte local ainda exige backfill read-only Shopify/Tiny/order-items; reports foram copiados para /sales-reports no container e devem virar rotina de refresh posterior.
- Rollback/mitigação: Imagem backup lk-estoque-web-web:pre-sales-analytics-final-20260613T234308Z; imagem nova lk-estoque-web-web:sales-analytics-final-20260613T234308Z; para rollback recriar container lk-estoque-web com imagem backup e labels Traefik lk-estoque.
- Próximos passos: Backfill read-only historico completo da LK e rotina/volume persistente para refresh dos reports no container; depois filtros de periodo D7/D30/MTD/YTD.
- Onde foi documentado no Brain: Commits 93d351e e 998c526 no branch feat/stock-os-api-adapter; receipt canônico areas/lk/sub-areas/stock/receipts/lk-stock-sales-analytics-dashboard-20260613T234308Z.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
