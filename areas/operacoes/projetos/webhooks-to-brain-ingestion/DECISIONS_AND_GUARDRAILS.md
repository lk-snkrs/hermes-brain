# Decisions and Guardrails — Webhooks to Brain Ingestion

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 9 prioriza governança operacional Hermes onde estado documental pode ser confundido com runtime vivo.

## Guardrails

- Não expor endpoint, secret ou assinatura; Doppler-first para credenciais.
- Webhook externo não deve executar write sensível sem validação, approval e roteamento.
- `Shopify/webhooks exigem HMAC/raw body quando aplicável e proxy canônico aprovado.`
- `Eventos recebidos devem virar evidência/preview/receipt antes de ação produtiva.`
