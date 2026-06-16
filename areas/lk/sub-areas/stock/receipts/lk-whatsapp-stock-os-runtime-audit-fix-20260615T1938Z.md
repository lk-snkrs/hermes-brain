# Receipt — LK WhatsApp responder now uses LK Stock OS for stock answers

- Data/hora: 2026-06-15T19:36:27.181523+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque / WhatsApp atendimento
- Responsável humano: Hermes lk-stock
- Pedido original: Auditar e corrigir Hermes WhatsApp não usando LK Stock OS para responder estoque de produtos.
- Classificação: external-write
- Fontes usadas:
- Script /opt/data/scripts/lk_hermes_whatsapp_responder.py; selftest /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py; Stock OS pointer areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json; process list; wacli auth status sanitized.
- O que foi feito:
- Detectado que o processo vivo estava carregado desde 2026-06-08, antes do patch de Stock OS; corrigido parser de termos Stock OS para prompts 'tem <SKU>'; criado stock_os_search_rows como hot path; answer_stock, assisted-sale e reposição WhatsApp passaram a consultar LK Stock OS local DB em vez de Tiny direto; reiniciado responder via watchdog mantendo wacli sync; testes e CLI ask verificados.
- Output/artefato:
- WhatsApp responder ativo no PID novo; wacli hermes authenticated=true; --ask stock/assist usa LK Stock OS local DB e não menciona Tiny direto; selftest passou.
- Aprovação: Lucas pediu explicitamente CORRIGIR; escopo limitado a script local/runtime WhatsApp Hermes, sem envio manual de mensagem, sem Tiny/Shopify write, sem secret print.
- Envio/publicação: Nenhuma mensagem externa/manual enviada; apenas responder runtime reiniciado.
- Writes externos: Processo local produtivo reiniciado; scripts locais alterados; nenhum Tiny/Shopify/Notion/WhatsApp send manual executado.
- Riscos/bloqueios: Funções legadas Tiny read-only permanecem no arquivo para outros fluxos, mas caminhos de stock/assist/ops WhatsApp agora usam Stock OS; U204L2SZ tamanho 35 segue não confirmado no Stock OS atual porque DB não tem saldo/linha segura para esse tamanho.
- Rollback/mitigação: Restaurar backups /opt/data/scripts/lk_hermes_whatsapp_responder.py.bak-20260615Twhatsapp-stockos-audit e /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py.bak-20260615Twhatsapp-stockos-audit; reiniciar /opt/data/scripts/lk_hermes_whatsapp_watchdog.sh.
- Próximos passos: Monitorar próximos eventos replied; se Lucas quiser, remover funções Tiny legadas/dead code em PR separado com testes ampliados.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/receipts/lk-whatsapp-stock-os-runtime-audit-fix-20260615T1938Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
