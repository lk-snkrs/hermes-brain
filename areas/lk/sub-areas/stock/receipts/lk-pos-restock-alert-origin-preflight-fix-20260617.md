# Receipt — LK POS restock alert origin preflight fix

- Data/hora: 2026-06-17T16:01:06.373352+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / POS restock alert
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas apontou que o erro recorrente de alerta POS com estoque não encontrado precisava ser corrigido na origem, não por SKU quase todo dia.
- Classificação: local-write
- Fontes usadas:
- /opt/data/scripts/lk_store_sale_restock_alert.py; /opt/data/scripts/lk_hermes_whatsapp_responder.py; /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py; skill lk-stock
- O que foi feito:
- Adicionado preflight antes de enviar/encadear alerta POS: consulta todos os itens, detecta miss do LK Stock OS, deriva prefixo pai, roda reparo read-only Shopify↔Tiny via Doppler lk-stock, promove current_local_stock e re-renderiza com current_stock_line; responder também respeita current_stock_line em itens enfileirados.
- Output/artefato:
- Regressão nova test_webhook_runs_stock_os_preflight_before_sending_restock_alert; suíte /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py com 18 passed; simulação #147843 retornou Estoque atual 3 un. e não perguntou reposição.
- Aprovação: Sem aprovação externa necessária: correção local/read-only/documental. Nenhum Tiny/Shopify write, envio WhatsApp adicional, deploy, gateway restart ou public availability promise.
- Envio/publicação: Telegram: resumo para Lucas nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Se crosswalk/preflight falhar em produção, o alerta preserva o comportamento seguro de validar com lk-stock; não promete disponibilidade pública.
- Rollback/mitigação: Reverter patches em /opt/data/scripts/lk_store_sale_restock_alert.py, /opt/data/scripts/lk_hermes_whatsapp_responder.py e teste; skill lk-stock pode ser revertida removendo a regra de preflight POS.
- Próximos passos: Monitorar próximos alertas POS: se ainda aparecer não encontrado, investigar retorno stock_os_preflight no evento antes de tratar SKU individual.
- Onde foi documentado no Brain: Skill lk-stock atualizada com regra: alerta POS não pode enviar não encontrado antes de curar origem por pedido inteiro.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
