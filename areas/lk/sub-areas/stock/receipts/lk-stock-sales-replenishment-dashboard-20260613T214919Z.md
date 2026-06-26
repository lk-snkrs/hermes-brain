# Receipt — LK Stock dashboard: fila Estoque x Vendas

- Data/hora: 2026-06-13T21:50:45.033238+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK/stock
- Responsável humano: lk-stock
- Pedido original: Seguir: dentro de Vendas, adicionar cruzamento Estoque x Vendas para compra/reposicao, sem sidebar e sem writes externos.
- Classificação: local-write
- Fontes usadas:
- Stock OS API read-only; relatorios JSON locais de vendas; testes node --test; validacao no container lk-estoque-web
- O que foi feito:
- Adicionado read model buildReplenishmentQueue; endpoint /api/estoque-vendas/replenishment; painel Compra / reposicao na aba Vendas; testes cobrindo P0/P1/P2 e guardrails.
- Output/artefato:
- https://estoque.lkskrs.online/ com topbar Estoque/Vendas e painel Vendas contendo Compra / reposicao; commit 11c876a; imagem lk-estoque-web-web:replenishment-20260613T214919Z.
- Aprovação: Aprovacao do Lucas via Telegram: Seguir; escopo limitado a dashboard interno/read-only.
- Envio/publicação: Dashboard interno atualizado; sem contato externo.
- Writes externos: 0
- Riscos/bloqueios: V1 usa top products agregados dos relatorios locais; quantidade de compra final exige D30/D90/D180 e decisao humana.
- Rollback/mitigação: Imagem backup lk-estoque-web-web:pre-replenishment-20260613T214919Z; reverter container para backup se necessario.
- Próximos passos: Automatizar refresh dos relatorios de venda no container e evoluir para D30/D90/D180 antes de sugestao quantitativa de compra.
- Onde foi documentado no Brain: Commit 11c876a no repo LK-Estoque-Web-inicial; PRD/plano existentes em areas/lk/sub-areas/stock/prds/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
