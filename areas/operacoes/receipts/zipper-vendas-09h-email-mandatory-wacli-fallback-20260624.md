# Receipt — Zipper vendas 09h email mandatory + WACLI fallback

- Data/hora: 2026-06-24T09:34:52.442609+00:00
- Agente/profile/cron: default / Mesa COO follow-through
- Empresa/área: Zipper OS / Operações Hermes
- Responsável humano: Hermes Geral
- Pedido original: Lucas esclareceu que no report interno Zipper 09h o e-mail é obrigatório; WhatsApp deve tentar WACLI hermes e depois WACLI pessoal como fallback.
- Classificação: local-write
- Fontes usadas:
- Mensagem de Lucas no Telegram; script /opt/data/scripts/zipper_sales_report_external_delivery.py; tests /opt/data/tests/test_zipper_sales_report_delivery.py; skill customer-messaging-automation reference wacli-zipper-sales-cron-nosend-idempotency-packet-20260624.md.
- O que foi feito:
- Aplicado patch local: send_whatsapp já tenta hermes e depois pessoal; main agora não deixa WACLI bloquear e-mail obrigatório; delivery_status explicita partial_sent_email_only_whatsapp_failed; estado marca whatsapp=failed quando e-mail sai sem WhatsApp; skill reference atualizada.
- Output/artefato:
- /opt/data/scripts/zipper_sales_report_external_delivery.py; /opt/data/tests/test_zipper_sales_report_delivery.py; /opt/data/skills/productivity/customer-messaging-automation/references/wacli-zipper-sales-cron-nosend-idempotency-packet-20260624.md; decision ledger 2026-06-24.
- Aprovação: Aprovação/clarificação atual de Lucas: e-mail obrigatório; WhatsApp WACLI hermes primeiro, WACLI pessoal fallback; se ambos falharem, e-mail-only OK com status parcial. Não autoriza --force, reenvio duplicado, pairing/reconnect WACLI, cron mutation ou contato externo.
- Envio/publicação: Nenhum WhatsApp/e-mail enviado por este patch; apenas dry-run/no-send.
- Writes externos: 0
- Riscos/bloqueios: Próximo run pode enviar e-mail interno real conforme contrato aprovado; se WhatsApp falhar, status parcial deve registrar pendência. WACLI reconnect/pairing continua separado.
- Rollback/mitigação: Reverter /opt/data/scripts/zipper_sales_report_external_delivery.py pelo backup local /opt/data/backups/zipper-sales-report-20260624T093216Z/ ou VCS; remover teste se rollback total.
- Próximos passos: Monitorar próximo run; se e-mail falhar, alertar; se apenas WhatsApp falhar e e-mail sair, tratar como parcial acionável conforme política de ruído.
- Onde foi documentado no Brain: Brain receipt + skill reference + decision-sequence ledger
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
