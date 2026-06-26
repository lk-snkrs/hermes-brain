# Receipt — Deploy container /vendas — 5 rodadas analytics

- Data/hora: 2026-06-25T23:35:53.926104+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Vendas
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas aprovou aplicar em produção as 5 rodadas de melhorias no /vendas.
- Classificação: infra-sensitive
- Fontes usadas:
- Commit 5e81ccb; container lk-estoque-web; backup /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-five-rounds-20260625T233334Z; smoke interno e público autenticado.
- O que foi feito:
- Backup de /app/src criado; src do commit 5e81ccb copiado para /app/src; correção de cópia inicial que criou /app/src/src; nested removido; container lk-estoque-web reiniciado; smoke executado.
- Output/artefato:
- Produção /vendas HTTP 200 autenticado com salesTimeSummaryPanel e Projeção do mês; /api/vendas/time-summary HTTP 200 JSON; /estoque/acoes HTTP 200 interno; público sem auth /vendas HTTP 401 esperado. values_printed=false.
- Aprovação: Lucas: Aprovo.
- Envio/publicação: Deploy aplicado no container lk-estoque-web; sem contato externo/customer-facing além da superfície web autenticada.
- Writes externos: Docker/container restart: lk-estoque-web; Tiny write 0; Shopify write 0; Notion write 0; compra automática 0; contato externo 0.
- Riscos/bloqueios: Restart limitado a lk-estoque-web; lk-estoque-stock-api não reiniciado.
- Rollback/mitigação: Restaurar backup /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-five-rounds-20260625T233334Z/src para lk-estoque-web:/app/src e reiniciar lk-estoque-web.
- Próximos passos: Monitorar uso visual; se Lucas apontar ajuste, iterar em cima do commit 5e81ccb.
- Onde foi documentado no Brain: Receipt de implementação 2026-06-25-dashboard-vendas-five-rounds.md; skill lk-stock reference stock-sales-vendas-five-rounds-pattern-20260625.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
