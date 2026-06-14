# Receipt — LK Stock dashboard vendas fases 1-7 decisão reposição

- Data/hora: 2026-06-14T22:30:08.103768+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock
- Responsável humano: Hermes lk-stock
- Pedido original: Fazer melhorias 1 a 7 na aba de vendas/Produto 360 do dashboard de estoque
- Classificação: local-write
- Fontes usadas:
- Stock OS API local; Shopify Sales OS DB/index local; produção estoque.lkskrs.online; npm test
- O que foi feito:
- Score D7/D30/D90; filas comprar/repor/investigar/ignorar; cobertura por tamanho; alertas silenciosos; Lista para Julio CSV; últimas vendas; saneamento identidade por impacto financeiro; deploy produção read-only
- Output/artefato:
- Dashboard commit 253507d; Brain commit f791fd2; imagem lk-estoque-web-web:sales-decision-1-7-20260614T222328Z; endpoints /api/vendas/decision-queues, /lista-julio, /alerts, /saneamento-identidade
- Aprovação: Autonomia local/read-only; sem write Tiny/Shopify/externo
- Envio/publicação: Telegram final summary
- Writes externos: Nenhum
- Riscos/bloqueios: Fila é recomendação conservadora, não promessa pública nem compra automática
- Rollback/mitigação: Rollback Docker tag lk-estoque-web-rollback-sales-decision-1-7-20260614t222328z e git revert dos commits 253507d/f791fd2 se necessário
- Próximos passos: Usar a Lista para Julio como fila de compra humana; calibrar thresholds após feedback
- Onde foi documentado no Brain: Receipt criado via Memory OS writer
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
