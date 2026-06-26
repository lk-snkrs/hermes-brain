# Receipt — Deploy /vendas performance — painéis pesados sob demanda

- Data/hora: 2026-06-26T00:20:07.897865+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Vendas
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas perguntou se o load do Dashboard demorar é normal e aprovou aplicar a melhoria em produção.
- Classificação: infra-sensitive
- Fontes usadas:
- Commit 87cbbcf; backup /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-load-performance-20260626T001919Z; smoke interno e público autenticado.
- O que foi feito:
- Aplicado no container lk-estoque-web com docker cp src/. para /app/src; verificado que /app/src/src não existe; restart limitado ao lk-estoque-web; smoke executado.
- Output/artefato:
- Interno: /vendas 200 82ms, summary 200 52ms, time-summary 200 7ms, analytics 200 8ms, shopify-sales-os 200 8ms. Produção autenticada /vendas 200 com botões sob demanda; auto_loads_julio=false, auto_loads_alerts=false, auto_loads_sanitation=false. Público sem auth 401 esperado. values_printed=false.
- Aprovação: Lucas escolheu: Aprovar deploy agora.
- Envio/publicação: Deploy aplicado na superfície web autenticada estoque.lkskrs.online; sem contato externo.
- Writes externos: Docker/container restart: lk-estoque-web; GitHub já sincronizado no commit 87cbbcf; Tiny write 0; Shopify write 0; Notion write 0; compra automática 0; contato externo 0.
- Riscos/bloqueios: Restart limitado a lk-estoque-web; lk-estoque-stock-api preservado.
- Rollback/mitigação: Restaurar /opt/data/profiles/lk-stock/backups/lk-estoque-web-vendas-load-performance-20260626T001919Z/src para lk-estoque-web:/app/src e reiniciar lk-estoque-web.
- Próximos passos: Se ainda houver lentidão percebida, otimizar/cachar /api/vendas/executive-summary, que mediu cerca de 3983ms antes da mudança.
- Onde foi documentado no Brain: Receipt de código 2026-06-25-dashboard-vendas-load-performance-defer-heavy-panels.md; skill lk-stock reference stock-sales-vendas-five-rounds-pattern-20260625.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
