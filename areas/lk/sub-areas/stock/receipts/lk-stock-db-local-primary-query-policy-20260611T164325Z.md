# Receipt — DB local primary query policy for LK Stock

- Data/hora: 2026-06-11T16:43:26.007826+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Registrar decisão de Lucas: consultas normais devem usar DB local; Tiny fica para full sync madrugada, webhooks/readback de evento e reconciliação, não para query on-demand.
- Classificação: local-write
- Fontes usadas:
- Orientação de Lucas no Telegram; PRD lk-stock; estado runtime Tiny/Olist webhooks
- O que foi feito:
- Atualizado PRD com política: DB local é caminho primário de consulta operacional; Tiny é sincronizador/reconciliador; consultas normais não devem bater no Tiny a cada pergunta.
- Output/artefato:
- areas/lk/sub-areas/stock/PRD.md atualizado com decisão operacional de arquitetura DB-local-primary.
- Aprovação: Orientação direta de Lucas: full sync madrugada + webhooks durante o dia; não consultar Tiny a cada pergunta por lentidão.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: DB local só é confiável se full sync/webhooks estiverem saudáveis; se base quebrar ou faltar SKU, bloquear promessa de disponibilidade e sinalizar reconciliação.
- Rollback/mitigação: Reverter a entrada DB-local-primary no PRD se Lucas decidir voltar para Tiny on-demand.
- Próximos passos: Implementar/validar full sync madrugada e garantir que query paths leiam DB local primeiro.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
