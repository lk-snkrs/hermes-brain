# Receipt — LK IA Bot context follow-up fix

- Data/hora: 2026-06-26T09:43:57.650589+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK/Atendimento
- Responsável humano: lk-ops
- Pedido original: Corrigir responder WhatsApp para usar contexto da lista anterior e não cair em help quando Lucas pede whatsapp dele
- Classificação: local-write
- Fontes usadas:
- screenshot de Lucas, logs do responder, testes locais, dry-run Shopify read-only
- O que foi feito:
- Persistência de contexto customers, follow-up de contato/whatsapp, desambiguação quando há múltiplos clientes, testes e restart local responder/wacli
- Output/artefato:
- Responder agora entende follow-up de lista anterior; pergunta qual cliente quando ambíguo; 23 tests passed; runtime 8787 ativo
- Aprovação: Lucas solicitou correção/feature no Telegram em 2026-06-26
- Envio/publicação: Sem envio proativo; responde apenas @Hermes/reply em grupo allowlistado
- Writes externos: nenhum
- Riscos/bloqueios: Contato de cliente é sensível; fluxo desambigua e limita a contexto de busca anterior; sem mensagem para cliente
- Rollback/mitigação: Restaurar /opt/data/backups/lk-ia-bot-context-followup-20260626T093819Z/lk_hermes_whatsapp_responder.py e reiniciar responder/wacli
- Próximos passos: Projetar camada LLM/router para perguntas não previstas sem perder guardrails e fontes vivas
- Onde foi documentado no Brain: Este receipt; testes em /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
