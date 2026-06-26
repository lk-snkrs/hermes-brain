# Receipt — LK Chatwoot order lifecycle WEB-only guard

- Data/hora UTC: 2026-06-15T14:56Z
- Área: LK / Atendimento / Chatwoot / WABA lifecycle
- Pedido humano: corrigir urgente para que mensagens de pedido feito, pagamento aprovado e demais lifecycle sejam enviadas apenas para clientes WEB, nunca loja física/POS.
- Classificação: produção aprovada pelo pedido urgente do responsável; customer-send guard/fail-closed; sem disparo de mensagem de teste para cliente.

## O que foi alterado

- Arquivo fonte remoto: `/opt/data/lk-chatwoot-v2/app/services/shopify/order_notification_service.rb`.
- Serviço afetado: `Shopify::OrderNotificationService`.
- Novo guard: `web_order?` roda antes de inbox/telefone, antes do dedupe e antes do dispatcher que envia WABA.
- Regra implementada:
  - permite pedidos WEB/online quando `source_name` é `web`, `online` ou `shopify`;
  - permite payloads WEB legados quando há `checkout_id`, `checkout_token` ou `order_status_url` sem sinais POS;
  - bloqueia `pos`, `shopify_pos`, `point_of_sale`, `retail`, `draft_order`, `shopify_draft_order`;
  - bloqueia qualquer payload com `location_id`/`location`;
  - fail-closed para payload ambíguo sem fonte WEB suficiente.
- Observabilidade: log sanitizado para bloqueio não-WEB/ambíguo com `kind`, `order_name` sanitizado e `source_name`, sem PII, telefone, e-mail, URL ou token.

## Deploy

- Imagem criada: `lk-chatwoot:v2-recovery26-web-only-lifecycle-20260615`.
- Compose ativo atualizado: `/opt/chatwoot/docker-compose.yaml`.
- Serviços recriados: `chatwoot-rails-1` e `chatwoot-sidekiq-1`.
- Rollbacks/backup:
  - arquivo de serviço anterior salvo em `/root/chatwoot-rollbacks/web-only-order-lifecycle-20260615T144643Z/`;
  - backup de compose criado em `/root/chatwoot-rollbacks/web-only-order-lifecycle-compose-20260615T145027Z.yaml`.

## Verificação

- Ruby syntax no container: `Syntax OK`.
- Readback do código dentro da imagem confirmou strings:
  - `Customer-facing order lifecycle WABA is online-only`;
  - `WEB_SOURCE_NAMES`;
  - `NON_WEB_SOURCE_NAMES`.
- Containers ativos com imagem nova:
  - `chatwoot-rails-1 lk-chatwoot:v2-recovery26-web-only-lifecycle-20260615`;
  - `chatwoot-sidekiq-1 lk-chatwoot:v2-recovery26-web-only-lifecycle-20260615`.
- Health local: HTTP `200`.
- Smoke sem envio real:
  - WEB por `source_name=web`: permitido;
  - WEB por `checkout_id`: permitido;
  - POS por `source_name=pos` + `location_id`: bloqueado;
  - loja física por `location_id`: bloqueado;
  - payload ambíguo sem fonte: bloqueado;
  - resultado: `pass=true`, `values_printed=false`.

## Observações

- Nenhuma URL de pedido/status, telefone, e-mail, token ou credencial foi registrada neste receipt.
- A regra vale para os templates lifecycle enviados por esse serviço: pedido feito/criado, pagamento aprovado, enviado, entregue e follow-up associado.
- POS/loja física deve continuar em sua própria esteira operacional, separada da WABA online lifecycle.
