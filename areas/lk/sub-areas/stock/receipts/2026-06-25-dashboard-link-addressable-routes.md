# Receipt — Dashboard Stock OS com rotas endereçáveis

- Data/hora: 2026-06-25T16:48:02.446167+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas pediu aplicar a regra de que toda tela alterada precisa ser acessível por link no dashboard.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas; skill lk-stock link-addressable page rule; código src/index.js, src/public/index.html, test/app.test.js; npm test; Impeccable detect; smoke container; screenshot headless local.
- O que foi feito:
- Atualizado dashboard para usar rotas diretas: /estoque/hoje, /estoque/consulta, /estoque/acoes, /estoque/grades, /estoque/ruptura, /estoque/demanda, /estoque/base, /estoque/disponiveis, /estoque/baixo-estoque, /reposicao e /vendas. Nav/topbar/filtros/abas viraram links href; JS usa STOCK_ROUTE_STATE e popstate; server tem DASHBOARD_PAGE_ROUTES explícito.
- Output/artefato:
- Commit 64422da em feat/stock-os-api-adapter; produção/container lk-estoque-web reiniciado; todas as rotas diretas deram HTTP 200 no container com STOCK_ROUTE_STATE e links diretos; /api/vendas/summary HTTP 200 autorizado; npm test 39/39; Impeccable [].
- Aprovação: Pedido direto de Lucas para atualizar o Dashboard e usar a regra acima. Escopo: UI/rotas/read-only dashboard; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub branch feat/stock-os-api-adapter push; container lk-estoque-web /app/src atualizado e reiniciado. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Restart curto do dashboard e mudança de navegação; mitigado com backup, testes, detector, HTTP smoke e screenshot local.
- Rollback/mitigação: Backups em .hermes/backups/link-addressable-dashboard-routes-20260625T164447Z e /opt/data/profiles/lk-stock/backups/lk-estoque-web-link-addressable-routes-20260625T164649Z; rollback via git revert 64422da e restauração dos arquivos no container.
- Próximos passos: Nas próximas mudanças UI, adicionar qualquer nova superfície ao DASHBOARD_PAGE_ROUTES e STOCK_ROUTE_STATE antes de reportar como pronta.
- Onde foi documentado no Brain: Skill lk-stock atualizada com route registry implementado.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
