# Receipt — Chatwoot online lifecycle approved layout fix

- Data/hora: 2026-06-18T17:32:42.821821+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK/Atendimento
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir lifecycle online para usar os layouts aprovados, não templates simples/técnicos
- Classificação: infra-sensitive
- Fontes usadas:
- Chatwoot Rails runtime; templates WABA aprovados; final smoke no-send pós-deploy; recovery_settings readback
- O que foi feito:
- Patch no Recovery::ConversationDispatcher para mapping por template lk_online_*, HEADER IMAGE, botão URL e fallback institucional; patch no Shopify::OrderNotificationService para product_list e first_product_image_url; build/deploy da imagem lk-chatwoot:v2-online-layout-templates-20260618172845; settings de pedido criado/aprovado/enviado/entregue trocadas para templates lk_online_* aprovados
- Output/artefato:
- Runtime ativo usa imagem nova; pedido criado=lk_online_pedido_realizado_v1; pagamento aprovado=lk_online_pagamento_aprovado_v1; pedido enviado=lk_online_pedido_enviado_v1; pedido entregue=lk_online_pedido_entregue_v1; carrinho abandonado preservado em lk_checkout_abandonado_*
- Aprovação: Aprovado explicitamente por Lucas no Telegram: corrigir o uso do layout/template aprovado após ele apontar que o teste anterior usou template errado; escopo limitado ao Chatwoot lifecycle online
- Envio/publicação: Nenhum WhatsApp novo enviado nesta correção; apenas smoke no-send/read-only após deploy
- Writes externos: Recreate dos containers Chatwoot Rails/Sidekiq e update de recovery_settings no Chatwoot DB; nenhum Shopify/Tiny/Meta template write; nenhum envio WhatsApp novo
- Riscos/bloqueios: Se payload real não trouxer imagem de produto, HEADER IMAGE usa fallback institucional público da LK; saída bruta de Rails pode conter PII e ficou restrita/local
- Rollback/mitigação: Rollback por renomear/remover containers novos e restaurar containers pre-online-layout; backup de recovery_settings salvo no workdir /opt/data/tmp/online_layout_fix_20260618T172016Z
- Próximos passos: Observar o primeiro envio real de pedido/carrinho e confirmar status WABA, content público e layout visual no Chatwoot; enviar teste real com template aprovado somente se Lucas pedir
- Onde foi documentado no Brain: Receipt criado via hermes_memory_os_receipt_writer.py; final verification em /opt/data/tmp/online_layout_fix_20260618T172016Z/final_verification_after_fallback.txt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
