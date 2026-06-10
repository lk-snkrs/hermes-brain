# Mensagem para Klaviyo Support — habilitação Advanced KDP / System Webhooks

Assunto sugerido: Enable Advanced KDP / System Webhooks API for LK Sneakers account

Olá, time Klaviyo.

Somos da LK Sneakers e estamos configurando uma integração interna read-only para monitoramento operacional de campanhas e eventos de email no Klaviyo.

Já temos:

- private API key com escopos de webhook configurada;
- endpoint HTTPS público para receber eventos;
- validação HMAC implementada;
- fallback read-only via Campaigns/Reporting API;
- nenhum envio, alteração de campanha ou ativação de flow por webhook.

Ao tentar consultar/criar System Webhooks via API, recebemos o erro:

`You must have Advanced KDP enabled to use this endpoint.`

Pedido:

Podem habilitar Advanced KDP ou o acesso necessário à System Webhooks API para a conta da LK Sneakers?

Objetivo técnico:

- receber eventos de campanhas/email como sent/delivered/opened/clicked quando disponíveis;
- acionar rotinas internas de leitura, métricas e pós-mortem;
- manter o fluxo read-only e auditável.

Endpoint preparado:

`https://hermes-webhooks.lucascimino.com/webhooks/lk-content-klaviyo-events`

Observação de segurança:

- o secret HMAC não será enviado por email/chat;
- será configurado apenas em ambiente seguro;
- não solicitamos acesso a dados sensíveis fora do necessário para webhooks operacionais.

Obrigado.
