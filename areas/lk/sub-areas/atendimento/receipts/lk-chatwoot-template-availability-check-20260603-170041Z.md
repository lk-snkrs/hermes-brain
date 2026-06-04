# LK Chatwoot — verificação template WhatsApp aprovado x Chatwoot

Data: 2026-06-03 17:00:41 UTC

## Pergunta

Lucas perguntou se o template aprovado pela Meta já estava "on" no Chatwoot.

## Verificações read-only

- Meta Graph API: template `lk_teste_chatwoot_builder_20260603` consta como `APPROVED`, categoria `MARKETING`, idioma `pt_BR`, rejected_reason `NONE`, ID `1930178777664845`.
- Chatwoot público `https://chat.lkskrs.online/api`: HTTP 200, versão `4.14.1`, `queue_services=ok`, `data_services=failing`.
- Chatwoot inboxes via Application API: conta tem apenas o inbox `1` / `Shopify Carrinho Abandonado` com `Channel::Api`.
- Não há inbox `whatsapp_cloud` listado na conta no momento da verificação.
- Endpoint customizado do template builder existe/respondendo: chamada em inbox não-WhatsApp retornou HTTP 400 com mensagem `WhatsApp template operations only available for WhatsApp Cloud inboxes`.

## Conclusão operacional

- A customização do template builder está ativa no Chatwoot em produção.
- O template aprovado ainda não está operacional/visível como template de um inbox WhatsApp Cloud dentro do Chatwoot, porque não há inbox WhatsApp Cloud conectado na conta.
- Nenhuma mensagem WhatsApp foi enviada e nenhuma campanha/importação foi ativada.

## Próximo gate

Para ficar realmente utilizável no Chatwoot: conectar/criar o inbox WhatsApp Cloud com Phone Number ID, WABA ID e token; depois sincronizar/listar templates pelo builder. Isso é alteração externa/produção e requer aprovação explícita de escopo.
