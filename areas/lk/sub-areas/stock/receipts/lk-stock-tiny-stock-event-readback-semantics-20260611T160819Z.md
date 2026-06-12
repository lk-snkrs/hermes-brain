# Receipt — Tiny/Olist stock event readback semantics

- Data/hora: 2026-06-11T16:08:19.574742+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Implementar regra: webhook de estoque é gatilho; quantidade final vem de readback Tiny API por idProduto no depósito oficial.
- Classificação: local-write
- Fontes usadas:
- Tiny/Olist webhook real, Tiny API read-only produto.obter.estoque, testes unitários locais, probe público hermes-webhooks
- O que foi feito:
- Atualizado processor para exigir readback Tiny API em eventos de estoque da rota /tiny/events; preservado webhook_quantity só para auditoria; adicionados testes TDD para quantidade do readback e bloqueio em falha.
- Output/artefato:
- PRD atualizado; scripts lk_stock_tiny_sync_processor.py e lk_stock_tiny_events_processor.py atualizados; suíte 25 tests OK; probe público HV8547-200-38 retornou quantity_source=tiny_api_readback e quantity=2.0 ignorando webhook_quantity=999.
- Aprovação: Aprovado por Lucas no Telegram: Fechado implementar.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Sem readback, webhook poderia ser interpretado como saldo/movimento errado; agora falha de readback bloqueia update local em vez de gravar quantidade ambígua.
- Rollback/mitigação: Reverter alterações nos scripts lk_stock_tiny_sync_processor.py e lk_stock_tiny_events_processor.py e no teste test_tiny_sync_runtime_processor.py; restaurar uso de payload bruto apenas se aprovado.
- Próximos passos: Monitorar próximos eventos reais de estoque para confirmar quantity_source=tiny_api_readback em produção; não prometer pronta entrega sem readback Tiny atual.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
