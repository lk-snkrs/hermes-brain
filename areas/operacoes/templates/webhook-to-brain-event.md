# Template — Webhook/Event → Brain

Use para eventos recebidos por webhook, API, email, WhatsApp, Shopify, GitHub, Vercel, Klaviyo, GMC, GSC, Notion ou outros sistemas.

```md
# Event Receipt — <origem> — <YYYY-MM-DDTHHMMSSZ>

- Origem/evento:
- Payload armazenado? sim/não/local privado
- PII/secrets removidos:
- Empresa/área roteada:
- Classificação: informativo | precisa decisão | precisa ação | falha | risco
- Evidência:
- Ação tomada pelo Hermes:
- Writes externos:
- Próximo responsável:
- Próximo passo:
- Onde foi salvo no Brain:
```

## Regra

Começar webhooks como read-only/receipt-first. Qualquer write externo, envio, gasto, alteração de campanha ou alteração de produção exige aprovação explícita e rollback.
