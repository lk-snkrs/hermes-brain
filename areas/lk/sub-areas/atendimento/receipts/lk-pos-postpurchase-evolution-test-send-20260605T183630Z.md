# Receipt — LK POS pós-venda teste real Evolution API / LK Flagship

Data UTC: 2026-06-05T18:36:30Z

## Aprovação

Lucas aprovou no Telegram: enviar teste real para `5511991203361` usando a instância LK Flagship da Evolution API.

## Mensagem enviada

```text
Oi, tudo bem? Aqui é a equipe da LK Sneakers.

Este é um teste interno do novo fluxo de pós-venda POS 30min via Evolution API / LK Flagship.

Nenhuma automação de cliente está ativa ainda.
```

## Execução

- Provider: Evolution API.
- Instância: `LK Flagship`.
- Endpoint usado: `/message/sendText/{instance}`.
- Credenciais: buscadas em Doppler `lc-keys/prd`, sem imprimir valores.
- Número destinatário: registrado aqui porque foi explicitamente informado para teste pelo Lucas; não expandir para listas sem nova aprovação.

## Resultado sanitizado

```json
{
  "mode": "EXECUTE_SEND_APPROVED_TEST",
  "instance": "LK Flagship",
  "phone_hash": "a6ceac695ca3",
  "message_chars": 194,
  "send_status": "sent",
  "http_status": "201",
  "status": "PENDING",
  "fromMe": true,
  "id_present": true
}
```

## Guardrails

- Foi um único envio de teste aprovado.
- Nenhum webhook Shopify foi alterado.
- Nenhum envio automático para clientes foi ativado.
- Nenhum write em Shopify/Tiny/Chatwoot/n8n.
- Próximos envios reais/canary precisam de novo approval packet.
