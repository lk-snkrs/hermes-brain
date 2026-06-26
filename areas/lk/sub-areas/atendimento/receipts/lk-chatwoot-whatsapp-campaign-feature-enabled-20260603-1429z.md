# LK Chatwoot — whatsapp_campaign feature enabled

Data: 2026-06-03 14:29 UTC
Status: `enabled_verified`

## Pedido

Lucas perguntou se já poderíamos deixar feito o item 2: habilitar a feature `whatsapp_campaign` no Chatwoot.

## Escopo executado

Alteração única na conta Chatwoot LK:

- account_id: `1`
- feature: `whatsapp_campaign`
- before: `false`
- after: `true`

Comando executado via Rails runner no Chatwoot self-hosted, sem expor secrets.

## Verificação pós-alteração

Rails runner confirmou:

```json
{
  "account_id": 1,
  "campaigns": true,
  "whatsapp_campaign": true,
  "inboxes": [
    {
      "id": 1,
      "name": "Shopify Carrinho Abandonado",
      "channel_type": "Channel::Api",
      "inbox_type": "API",
      "provider": null
    }
  ]
}
```

Health externo básico do Chatwoot:

```text
https://chat.lkskrs.online/api -> 200
```

## O que NÃO foi feito

- Nenhuma campanha criada.
- Nenhum contato criado/importado/alterado.
- Nenhum template WhatsApp criado ou enviado.
- Nenhuma inbox WhatsApp Cloud conectada.
- Nenhum envio externo/customer-visible.

## Observação operacional

A feature agora está habilitada, mas a LK ainda não consegue rodar campanha WhatsApp pelo Chatwoot até existir uma inbox `Whatsapp` com provider `whatsapp_cloud`, contatos com telefone E.164/labels e templates aprovados na Meta.
