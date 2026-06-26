# Receipt — Shopify webhook canonical URL fix — lk-shopify-tiny-stock-sync

- Data/hora: 2026-06-25T23:36:33.151777+00:00
- Agente/profile/cron: default
- Empresa/área: LK Sneakers / Hermes Webhooks / Shopify
- Responsável humano: Hermes default
- Pedido original: Lucas aprovou write para corrigir assinatura da rota lk-shopify-tiny-stock-sync.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin REST read-only/readback; Hermes gateway logs; public Shopify-HMAC no-op probe; Doppler presence checks without values.
- O que foi feito:
- Atualizados os webhook IDs 1646886125790 orders/paid e 1646886158558 orders/cancelled para https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync; preservado backup sanitizado; criada referência de skill webhook-subscriptions.
- Output/artefato:
- Shopify Admin PUT HTTP 200 para ambos; readback address_ok=true para ambos; probe público HTTP 202 accepted; monitor de logs pós-update invalid_signature_count=0.
- Aprovação: Lucas: Aprovo write.
- Envio/publicação: Sem mensagem externa; apenas resposta Telegram ao Lucas.
- Writes externos: Shopify Admin webhook subscription address update para 2 IDs; nenhum produto, pedido, estoque, Tiny, tema, preço, Klaviyo, WhatsApp ou e-mail.
- Riscos/bloqueios: Baixo/médio: alteração de endpoint de webhook. Mitigado por readback, probe público e rollback simples pelo address antigo.
- Rollback/mitigação: Reverter os IDs 1646886125790 e 1646886158558 para https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync usando backup sanitizado em /opt/data/backups/shopify-webhook-canonical-url-fix-20260625T233346Z/.
- Próximos passos: Monitorar se novos Invalid signature voltam a aparecer; se sim, procurar outro webhook/upstream antigo.
- Onde foi documentado no Brain: Report: reports/governance/shopify-webhook-canonical-url-fix-lk-shopify-tiny-stock-sync-2026-06-25.md; backup: /opt/data/backups/shopify-webhook-canonical-url-fix-20260625T233346Z/; skill reference: webhook-subscriptions/references/shopify-admin-webhooks-direct-hermes-invalid-signature-20260625.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
