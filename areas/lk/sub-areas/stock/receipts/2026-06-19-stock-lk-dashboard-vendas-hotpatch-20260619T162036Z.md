# Receipt — Stock.LK Dashboard Vendas hot-patch

- Data/hora: 2026-06-19T16:20:37.069485+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock.LK dashboard
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas informou que a parte de Vendas do dashboard Stock.LK estava vazia e precisava puxar da tabela/read model de vendas.
- Classificação: infra-sensitive
- Fontes usadas:
- Container lk-estoque-web; repo /opt/data/worktrees/lk-stock/LK-Estoque-Web-inicial; artefatos /app/data/live/shopify_sales_os_summary.json e shopify_sales_search_index.json; smoke público https://estoque.lkskrs.online/api/vendas/summary.
- O que foi feito:
- Reproduzido container antigo sem /api/vendas/*; criado rollback image lk-estoque-web:rollback-before-vendas-20260619T161434Z; copiado src testado; reiniciado lk-estoque-web; implementado fallback /api/vendas/summary e /api/vendas/products para Shopify Sales OS DB quando local_sales_reports está vazio; retestado e reaplicado no container.
- Output/artefato:
- Aba Vendas passou a ter summary source=shopify_sales_os_db_fallback com orders=1999, revenue=6585484.91, top_products=20; /api/vendas/products com 50 produtos; /api/vendas/search ok; rota pública retornou HTTP 200 autenticado.
- Aprovação: Aprovação explícita de Lucas no Telegram: 'Aprovo o hot-patch Docker agora'.
- Envio/publicação: Sem contato externo/customer-facing; somente hot-patch local do dashboard interno protegido por senha.
- Writes externos: Docker local write: container lk-estoque-web e imagem local lk-estoque-web-web:latest atualizados; Tiny write 0; Shopify write 0; Notion write 0; public availability promise 0.
- Riscos/bloqueios: Hot-patch em container é mudança operacional; mitigado com backup de /app/src e rollback image antes do patch. Imagem original do container em execução permanece no inspect até recriação; tag lk-estoque-web-web:latest foi atualizada para futuro recreate simples.
- Rollback/mitigação: docker stop lk-estoque-web && recriar usando lk-estoque-web:rollback-before-vendas-20260619T161434Z ou restaurar backup /opt/data/profiles/lk-stock/backups/lk-estoque-web-hotpatch-20260619T161434Z/src-before para /app/src e reiniciar.
- Próximos passos: Se a aba ainda parecer vazia no navegador, forçar refresh/cache; depois considerar formalizar em Git/CI em vez de manter apenas hot-patch.
- Onde foi documentado no Brain: Receipt gerado por hermes_memory_os_receipt_writer.py no Brain canônico com HERMES_HOME=/opt/data; teste local npm test 36/36 OK; smoke container e público OK.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
