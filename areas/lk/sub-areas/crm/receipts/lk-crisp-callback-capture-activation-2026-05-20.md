# Receipt — ativação de captura Callback Crisp WhatsApp

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Pedido

Lucas pediu continuar corrigindo o fluxo de carrinho/checkout abandonado da Shopify, focando apenas no problema de o envio não aparecer na Inbox Crisp.

## Diagnóstico

- Workflow de envio ativo já estava com o shape híbrido recomendado no nó `Crisp Send lk_checkout_abandonado_30min_v4`:
  - `crisp_options.as = text`
  - `crisp_options.type = text`
  - `crisp_options.new_session = false`
  - `BODY.text` presente
- O ponto ainda descoberto sem correção operacional era a ausência de endpoint produtivo ativo para receber callbacks do plugin WhatsApp da Crisp.
- Workflow antigo `LK - Crisp WhatsApp Callback Debug` estava arquivado (`isArchived=true`), então não podia ser ativado via API apesar de o CLI permitir alterar estado no banco.

## Correção aplicada

Criado e ativado novo workflow n8n apenas para captura de callbacks:

- Nome: `LK - Crisp WhatsApp Callback Capture (ATIVO)`
- Workflow ID: `8heG4ZyRp85p0MQj`
- Método: `POST`
- Path: `lk-crisp-whatsapp-callback`
- URL produtiva esperada: `https://n8n.lucascimino.com/webhook/lk-crisp-whatsapp-callback`
- Resposta: `200`, respond immediately

## Verificação

Probe local no n8n via VPS:

- Endpoint: `POST http://127.0.0.1:32769/webhook/lk-crisp-whatsapp-callback`
- HTTP: `200`
- Resposta: `{"message":"Workflow was started"}`

Isso confirma que o webhook produtivo está registrado no runtime n8n.

## Segurança

- Nenhuma mensagem foi enviada para cliente ou número interno nesta correção.
- Nenhum template Meta/Crisp foi alterado.
- Nenhum segredo foi registrado neste receipt.
- O workflow antigo arquivado não foi apagado.

## Observação operacional

A captura de callback não faz mensagens antigas aparecerem retroativamente na Inbox. Ela corrige a falta de evidência assíncrona para os próximos envios e permite correlacionar `request_id`, eventual `session_id`, `whatsapp_message_id` e erros do provider quando a Crisp chamar o callback configurado.

Se a URL ainda não estiver configurada no painel/plugin da Crisp, configurar como Callback URL produtivo:

`https://n8n.lucascimino.com/webhook/lk-crisp-whatsapp-callback`
