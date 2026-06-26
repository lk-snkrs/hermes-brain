# Elle / Chatwoot — diagnóstico read-only da inbox WhatsApp

Data: 2026-06-09T14:31:33Z
Área: LK / Atendimento / Elle / Chatwoot / WhatsApp
Modo: read-only, metadata-only

## Escopo

Lucas pediu “seguir” após a ativação da Elle e watches sem inbound real. Foi feita auditoria read-only para entender se a falta de inbound era por ausência de inbox WhatsApp ou por falta de evento recebido do provider.

## Inboxes Chatwoot

Rails read-only confirmou `2` inboxes na conta `1`:

- Inbox `1`: `Shopify Carrinho Abandonado`, `Channel::Api`.
- Inbox `2`: `LK WhatsApp`, `Channel::Whatsapp`.

Times:

- `suporte`.
- `atendimento whatsapp`.

## Canal WhatsApp

`Channel::Whatsapp.first` confirmou:

- `id=1`
- `account_id=1`
- `phone_number_present=true`
- `provider=whatsapp_cloud`
- `provider_config_keys` presentes:
  - `api_key`
  - `phone_number_id`
  - `business_account_id`
  - `webhook_verify_token`

Nenhum valor de token/config foi impresso.

## Segregação de secrets Doppler

Doppler `lc-keys/prd` confirmou presença dos secrets separados:

- `CHATWOOT_WHATSAPP_WEBHOOK_URL`: presente, host `chat.lkskrs.online`, path `/webhooks/whatsapp/...`.
- `CHATWOOT_WHATSAPP_WEBHOOK_SECRET`: presente, length `32`.
- `ELLE_CHATWOOT_WEBHOOK_URL`: presente, host `elle.lkskrs.online`, path `/webhooks/chatwoot/...`.
- `ELLE_CHATWOOT_WEBHOOK_SECRET`: presente, length `32`.

Conclusão: não há mistura aparente entre webhook Meta/WhatsApp → Chatwoot e webhook Chatwoot → Elle.

## Contagens de mensagens/conversas

Postgres read-only:

- total conversas: `331`
- total mensagens: `661`
- inbox `1`: `661` mensagens, `0` incoming public.
- inbox `2`/WhatsApp: sem mensagens/conversas observadas na consulta agrupada.

## Logs Rails filtrados

Desde `2026-06-09T12:50:00Z`:

- `GET /webhooks/whatsapp/[PHONE_REDACTED]`: `1`
- `POST /webhooks/shopify`: `77`
- `GET /api/v1/accounts/1/webhooks`: `3`
- `GET /api/v1/accounts/1/conversations/meta`: `11`

Detalhe do GET WhatsApp:

- `Webhooks::WhatsappController#verify`
- parâmetros logados só com `phone_number` sanitizado
- resultado: `401 Unauthorized`

Não foram encontrados `POST /webhooks/whatsapp/...` na janela consultada.

## Interpretação operacional

- A inbox WhatsApp existe no Chatwoot e está configurada como WhatsApp Cloud.
- Os secrets relevantes existem e estão separados corretamente.
- O Chatwoot recebeu ao menos uma tentativa GET de verificação/abertura do endpoint, mas ela retornou `401` e não houve POST inbound Meta/WhatsApp observado.
- A ausência de reação da Elle é coerente: não houve mensagem inbound pública no Chatwoot WhatsApp para ela processar.

## Próximo passo seguro

Validar no painel Meta/WhatsApp Cloud se o callback URL e verify token estão configurados exatamente com os dados do Chatwoot. Essa validação/alteração no Meta é externa e exige aprovação explícita se for feita por Hermes.

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhum WhatsApp enviado.
- Nenhum endpoint/webhook alterado.
- Nenhum container/Chatwoot/Meta/Shopify/Tiny alterado.
- Nenhum segredo impresso.

`values_printed=false`.
