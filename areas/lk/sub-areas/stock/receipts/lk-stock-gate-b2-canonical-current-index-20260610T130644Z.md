# Receipt — LK Stock Gate B2 visao canonica local atual

- Data/hora: 20260610T130644Z
- Agente/profile/cron: [LK] Estoque Loja Fisica
- Empresa/área: LK/stock
- Responsável humano: lk-stock
- Pedido original: Lucas pediu seguir; criada visao canonica local para consulta futura sem conflito entre historico bloqueado e match resolvido.
- Classificação: local-write
- Fontes usadas:
- Lookup local Gate B2 20260610T125335Z.
- O que foi feito:
- Criada visao canonica por SKU+handle com 903 linhas atuais, 8 estados antigos superseded preservados, script de consulta canonica e guardrails sem writes externos.
- Output/artefato:
- areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db; areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json; areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.csv; areas/lk/sub-areas/stock/approval-packets/gate-b2-canonical-current-index-20260610T130644Z.md; areas/lk/sub-areas/stock/scripts/gate_b2_lookup_canonical_current.py
- Aprovação: Escopo local/cache; sem aprovacao para write Tiny/Shopify.
- Envio/publicação: Telegram somente resumo; nenhum contato externo.
- Writes externos: 0
- Riscos/bloqueios: Visao canonica local nao afirma pronta entrega; disponibilidade exige fonte viva Tiny.
- Rollback/mitigação: Remover artefatos e script deste timestamp; artefatos historicos preservados; Tiny/Shopify intactos.
- Próximos passos: Usar consulta canonica como default para perguntas futuras de SKU/handle; histórico lookup antigo segue auditavel.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
