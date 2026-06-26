# Live validation — Chatwoot Sidebar Templates

Data UTC: 2026-06-03T19:18:21Z
Área: LK Sneakers / Atendimento / Chatwoot / WhatsApp Templates

## Resultado

Lucas confirmou visualmente que a rota/tela `Templates` carregou no Chatwoot live.

URL esperada:

`https://chat.lkskrs.online/app/accounts/1/templates`

## Estado observado

A tela mostra:

`No WhatsApp Cloud API inbox found. Connect a WhatsApp Cloud inbox before listing or creating Meta templates.`

Isso é consistente com o estado atual da conta: read-only Rails runner listou apenas um inbox:

- id: 1
- name: `Shopify Carrinho Abandonado`
- channel_type: `Channel::Api`
- provider: null
- message_templates_count: null

Não existe ainda inbox `Channel::Whatsapp` com provider `whatsapp_cloud` na conta LK.

## Interpretação

- A sidebar/rota estão funcionando em produção.
- O botão/fluxo de criação não aparece porque a página exige um WhatsApp Cloud API inbox real para saber WABA/phone_number_id/provider_config.
- Sem esse inbox, sincronizar/listar/criar templates Meta por Chatwoot não tem o canal/WABA de origem.

## Guardrails

Não foram feitos:

- criação de template Meta;
- envio WhatsApp;
- campanha;
- conexão de WhatsApp Cloud API;
- alteração Shopify/Tiny.

Próximo passo, se aprovado separadamente: conectar/criar o WhatsApp Cloud API inbox no Chatwoot com phone number, phone number ID, WABA ID e token Meta; depois reabrir Templates e sincronizar/listar templates.
