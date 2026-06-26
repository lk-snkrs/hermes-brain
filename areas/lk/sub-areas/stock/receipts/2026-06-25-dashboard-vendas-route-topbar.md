# Receipt — LK Stock dashboard Vendas em rota interna

- Data/hora: 2026-06-25T16:13:07.791057+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / Vendas
- Responsável humano: lk-stock
- Pedido original: Lucas corrigiu que a parte de vendas estava errada: busca comercial não podia ficar na lateral e Controle de Vendas precisava ter página interna em /vendas.
- Classificação: external-write
- Fontes usadas:
- Comentário e screenshot de Lucas; código src/public/index.html, src/index.js, test/app.test.js; npm test; Impeccable detect; smoke container lk-estoque-web /vendas e APIs vendas.
- O que foi feito:
- Criada rota /vendas; topbar Estoque/Vendas agora navega para / e /vendas; salesDashboard inicializa por pathname; sidebar/btnMenu/stockShell escondem em vendas; busca comercial movida para salesTopbarSearch; mantido único salesSearchInput; refresh e intervalo em vendas chamam carregarVendas, não /api/sync de estoque.
- Output/artefato:
- Commit 26590e6 em feat/stock-os-api-adapter; produção/container lk-estoque-web reiniciado; /vendas HTTP 200 no container com Controle de Vendas=true, salesTopbarSearch=true, Página interna /vendas=true, singleInput=1; /api/vendas/summary e /api/vendas/search HTTP 200 autorizado.
- Aprovação: Pedido direto de Lucas para mudar UI/rota de Vendas no dashboard Stock OS. Escopo: UI/route/read-only dashboard; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub branch feat/stock-os-api-adapter push/force-with-lease; container lk-estoque-web /app/src atualizado e reiniciado. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Restart curto do dashboard e ajuste de navegação; mitigado com backup, npm test 39/39, Impeccable [], smoke container e rollback path.
- Rollback/mitigação: Backups em .hermes/backups/sales-route-topbar-search-20260625T160407Z, /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-route-topbar-* e /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-refresh-fix-*; rollback via git revert 26590e6 e restauração dos backups no container.
- Próximos passos: Lucas revisar visualmente /vendas; se ainda estiver feio, próximo passe é redesenhar a hierarquia interna da página de vendas, não mexer em estoque.
- Onde foi documentado no Brain: Skill lk-stock atualizada com Sales route/topbar rule.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
