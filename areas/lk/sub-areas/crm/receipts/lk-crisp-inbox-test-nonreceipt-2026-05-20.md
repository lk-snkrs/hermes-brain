# Receipt — non-receipt after Crisp Inbox visibility test

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / Zoppy / Meta

## Input

Lucas informou que não recebeu no WhatsApp a mensagem de teste enviada via Crisp Template API com o payload documentado para aparecer no Inbox.

## Teste afetado

- Canal: Crisp WhatsApp Plugin `/template/send`
- Template: `lk_checkout_abandonado_30min_v3`
- `crisp_options`: `{ "type": "text", "new_session": true }`
- BODY incluiu `text` e `parameters`, conforme documentação Crisp
- Resultado síncrono: HTTP 200 / `request_accepted`
- `request_id`: `6ea55176-5cd6-48a5-9c41-84be37f27a8a`

## Documentação confirmada

Crisp docs de configuração dizem que `request_accepted` não é entrega final. Após aceitar a requisição, o plugin tenta enviar a mensagem e envia um webhook para o Callback URL configurado com o `request_id`.

- Sucesso inclui: `crisp_fingerprint`, `whatsapp_message_id`, `session_id`
- Falha inclui mensagem descrevendo por que o template não foi enviado

## Auditoria read-only após non-receipt

Meta Phone ID audit:

- Phone ID: `1220780761111140`
- Display: `+55 11 94956-5000`
- Verified name: `LK Sneakers & Apparels`
- Platform: `CLOUD_API`
- Quality: `GREEN`
- Code verification: `VERIFIED`
- Webhook atual: `https://api-partners.zoppy.com.br/whatsapp-account/.../webhook`

Conclusão: o webhook operacional do número continua apontando para Zoppy, não para Crisp.

## Diagnóstico

O teste provou apenas que o Crisp aceitou a requisição (`request_accepted`), não que a mensagem foi enviada/entregue. Como Lucas não recebeu e o webhook do número está em Zoppy, os receipts finais provavelmente não estão disponíveis no Crisp/Hermes sem acessar:

1. Callback URL configurado no plugin WhatsApp da Crisp; ou
2. painel/logs da Zoppy; ou
3. credencial REST/API adequada do Crisp para buscar a conversa por `session_id` após callback.

## Decisão operacional

Não reenviar em loop. Próxima ação segura: obter/validar Callback URL do plugin WhatsApp da Crisp ou configurar temporariamente um callback controlado para capturar payloads de sucesso/falha por `request_id`, sem ativar produção.
