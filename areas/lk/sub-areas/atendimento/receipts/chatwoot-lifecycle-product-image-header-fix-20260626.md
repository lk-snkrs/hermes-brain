# Receipt — Chatwoot lifecycle — header image produto em pedido/pagamento

- Data/hora: 2026-06-26T16:24:59.948131+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Chatwoot lifecycle WhatsApp
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas reportou que as mensagens de pedido feito e pagamento aprovado estavam enviando o logo LK em vez da foto do produto comprado.
- Classificação: infra-sensitive
- Fontes usadas:
- Screenshot de Lucas; runtime chatwoot-rails-1/chatwoot-sidekiq-1; Shopify read-only via integração Chatwoot; mensagem/order #147940 usada somente como smoke sanitizado; values_printed=false.
- O que foi feito:
- Backup criado; patch em Shopify::OrderNotificationService para resolver first_product_image_url via payload/line item e, se ausente, lookup Shopify read-only por product_id/variant_id; copiado para Rails e Sidekiq; reiniciado somente chatwoot-rails-1 e chatwoot-sidekiq-1.
- Output/artefato:
- Smoke pós-restart: lk_online_pedido_realizado_v1 e lk_online_pagamento_aprovado_v1 renderizam HEADER IMAGE com host cdn.shopify.com, header_is_logo=false; ruby -c OK nos dois containers; external_send_executed=false; db_updates_executed=false.
- Aprovação: Pedido direto de Lucas no Telegram para corrigir imagem em pedido feito e pagamento aprovado; escopo limitado a lifecycle header image.
- Envio/publicação: Nenhum reenvio histórico, nenhum teste customer-facing; só smoke no-save/no-send e próximo evento real usará o patch.
- Writes externos: 0 customer sends; runtime code patch + restart seletivo de Rails/Sidekiq do Chatwoot; Shopify somente GET/read-only.
- Riscos/bloqueios: Final proof depende do próximo pedido/pagamento real enviado após o patch; se Shopify product lookup falhar, fallback institucional ainda existe para evitar template quebrado.
- Rollback/mitigação: Restaurar /app/app/services/shopify/order_notification_service.rb a partir de /opt/data/backups/chatwoot-lifecycle-product-image/20260626T162155Z/ em Rails e Sidekiq e reiniciar chatwoot-rails-1/chatwoot-sidekiq-1.
- Próximos passos: Monitorar próximo pedido realizado/pagamento aprovado real para confirmar delivery/read com header de produto; não reenviar mensagens antigas sem aprovação.
- Onde foi documentado no Brain: Receipt canônico; skill customer-chat-operations atualizada em lk-chatwoot-online-lifecycle-approved-layout-20260618.md; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
