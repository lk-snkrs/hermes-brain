# Receipt — LK Stock dashboard: universo Vendas na topbar

- Data/hora: 2026-06-13T21:27:47.834619+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Estoque Web
- Responsável humano: Hermes lk-stock
- Pedido original: Adicionar no estoque.lkskrs.online uma escolha TOPBAR entre ESTOQUE e VENDAS, sem sidebar nova para vendas.
- Classificação: local-write
- Fontes usadas:
- Código local LK-Estoque-Web-inicial; reports/lk-sales-reports JSON; Docker container lk-estoque-web; smoke produção https://estoque.lkskrs.online/
- O que foi feito:
- Criado read model de vendas local/read-only; endpoints /api/vendas/summary e /api/vendas/products; topbar com opções Estoque/Vendas; seção Vendas sem sidebar; deploy no container com dados locais de vendas copiados para /app/data/sales-reports.
- Output/artefato:
- Produção validada: noauth 401, HTML 200 com topbarUniverseToggle e salesDashboard, vendas 200 status ok com 159 pedidos e 10 top products, estoque summary 200, Tiny write 0, Shopify write 0.
- Aprovação: Lucas aprovou escopo via Telegram: topbar com ESTOQUE/VENDAS e sem adicionar sidebar no momento.
- Envio/publicação: Nenhum envio externo/customer-facing.
- Writes externos: 0
- Riscos/bloqueios: Vendas V1 usa snapshot JSON local copiado no container; atualização live de vendas ainda depende de rotina posterior para sincronizar reports no container/read model.
- Rollback/mitigação: Docker backup image lk-estoque-web-web:pre-sales-universe-20260613T212239Z; git commit anterior disponível; restaurar imagem anterior e reconectar network lk-estoque-web_default.
- Próximos passos: Fase 2: cruzamento estoque x vendas para fila de compra/reposição e rotina de atualização do read model de vendas.
- Onde foi documentado no Brain: PRD e plano existentes em areas/lk/sub-areas/stock/prds/; commit d2af4f8.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
