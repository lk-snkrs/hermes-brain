# Chatwoot lifecycle oficial via Chatwoot/MessageBuilder — 2026-06-18

## Pedido do Lucas
Prioridade única: próximos disparos de carrinho abandonado, pedido criado/aprovado/enviado/entregue/follow-up devem sair pelo caminho oficial do Chatwoot, não por sender paralelo, e aparecer no histórico público da conversa.

## Estado aplicado
- Runtime Chatwoot Rails/Sidekiq está em imagem imutável `lk-chatwoot:v2-lifecycle-public-content-20260618152919`.
- Patch ativo: `Messages::MessageBuilder` preenche `content` renderizado quando recebe templates LK lifecycle conhecidos com `content` vazio.
- O envio continua sendo template WABA do Chatwoot: `MessageBuilder` cria mensagem pública, `SendReplyJob` envia via `Whatsapp::SendOnWhatsappService` usando `additional_attributes.template_params`.
- Não há reenvio histórico neste patch.

## Evidência read-only
- `SHOPIFY_RECOVERY_INBOX_ID` aponta para inbox `Channel::Whatsapp`.
- `SHOPIFY_NOTIFY_ENABLED=true`.
- Templates configurados presentes:
  - `SHOPIFY_RECOVERY_TEMPLATE_1/2/3`
  - `SHOPIFY_CREATED_TEMPLATE`
  - `SHOPIFY_APPROVED_TEMPLATE`
  - `SHOPIFY_SHIPPING_TEMPLATE`
  - `SHOPIFY_DELIVERED_TEMPLATE`
  - `SHOPIFY_FOLLOWUP_TEMPLATE`
- `Shopify::AbandonedCheckoutJob` chama `Recovery::ConversationDispatcher`.
- `Shopify::OrderNotificationService` chama `Recovery::ConversationDispatcher`.
- `Recovery::ConversationDispatcher#send_template` usa `Messages::MessageBuilder`.
- Renderer carregado em Rails runtime.
- Smoke no-save/no-send via `Messages::MessageBuilder#rendered_content` passou.

## Segurança
- `db_updates_executed=false` na verificação.
- `external_send_executed=false` na verificação.
- Nenhum valor de template, telefone, e-mail, token ou PII impresso no Telegram.

## Arquivos locais
- Verificação sanitizada: `/opt/data/tmp/chatwoot_official_api_lifecycle_20260618T154019Z/official_lifecycle_verify.json`
- Preview backfill histórico, se algum dia for aprovado separadamente: `/opt/data/tmp/lifecycle_visibility_fix_20260618T152120Z/backfill_preview_full_restricted.json`

## Observação operacional
O caminho interno do Chatwoot usa `Messages::MessageBuilder`, que é o mesmo construtor chamado pelo endpoint oficial `POST /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages`. Como o sender roda dentro do próprio Rails do Chatwoot, não precisa fazer HTTP contra si mesmo para estar no caminho oficial; o importante é não chamar Meta direto fora do Chatwoot e manter a mensagem pública no histórico.
