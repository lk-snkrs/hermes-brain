# LK Chatwoot — WhatsApp campaign capability check

Data: 2026-06-03 14:21 UTC
Status: `capability_exists_but_lk_not_ready_enabled`

## Pergunta

Lucas perguntou se o Chatwoot tem opção de fazer campanha para contatos usando WhatsApp Business API.

## Fontes consultadas

- Skill Chatwoot LK.
- Código do Chatwoot self-hosted em `/opt/chatwoot` via Rails/container, read-only:
  - `app/models/campaign.rb`
  - `app/services/whatsapp/oneoff_campaign_service.rb`
  - `app/controllers/api/v1/accounts/campaigns_controller.rb`
- Estado live da conta Chatwoot LK via Rails runner read-only.

## Resultado geral

O Chatwoot suporta campanhas one-off para inbox tipo `Whatsapp`, desde que:

- a inbox seja `Whatsapp`;
- o provider seja `whatsapp_cloud`;
- a feature flag da conta `whatsapp_campaign` esteja habilitada;
- os contatos estejam no Chatwoot e segmentáveis por labels;
- a campanha tenha `template_params` de template WhatsApp aprovado.

O serviço observado é `Whatsapp::OneoffCampaignService`, que processa contatos por labels e envia template via `channel.send_template`.

## Estado LK atual observado

```text
account_id: 1
campaigns_feature: true
whatsapp_campaign_feature: false
inboxes: somente Shopify Carrinho Abandonado / Channel::Api / inbox_type API
```

Logo, na LK agora:

- existe infraestrutura de campanhas genérica no Chatwoot;
- mas WhatsApp campaign não está habilitado;
- não há inbox WhatsApp Cloud conectada;
- a inbox atual de Shopify é API/internal context, não WhatsApp Business API.

## Guardrails

Nenhuma campanha criada, nenhum contato alterado, nenhum envio feito. Para ativar campanha real seria necessário approval separado: conectar inbox WhatsApp Cloud, habilitar feature, templates Meta aprovados, segmentação/consentimento/LGPD, dry-run e kill-switch.
