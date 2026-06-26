# Receipt — LK Shopify webhook secret rotation and Vercel redeploy

- Data/hora: 2026-06-10T13:46:40.309448+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / atendimento / Shopify webhooks
- Responsável humano: Lucas Cimino
- Pedido original: Lucas autorizou atualizar SHOPIFY_WEBHOOK_SECRET no Doppler lc-keys/prd e Vercel production hermes-webhooks com a chave secreta da API Shopify enviada, fazer redeploy e validar com probe/logs.
- Classificação: external-write
- Fontes usadas:
- Autorização explícita de Lucas no Telegram; Shopify custom app LC Api/API credentials; Doppler lc-keys/prd; Vercel project hermes-webhooks production; Vercel production logs; local ledger lk_shopify_orders_ingest.
- O que foi feito:
- Atualizado SHOPIFY_WEBHOOK_SECRET em Doppler lc-keys/prd sem imprimir valor; atualizado env production SHOPIFY_WEBHOOK_SECRET no Vercel hermes-webhooks via stdin sem imprimir valor; redeploy production executado e alias hermes-webhooks.vercel.app ficou READY; probe assinado retornou HTTP 200 record_only; probe fake removido do ledger.
- Output/artefato:
- Após redeploy, logs Vercel mostram HTTP 200 no deployment novo dpl_4o3b3FTMQ6K5woBxPKJx17JWVhb2 para /webhooks/lk-shopify-orders-ingest. Ledger local ficou com 1 pedido real registrado (#147620) e sem o fake probe.
- Aprovação: Aprovado explicitamente por Lucas: atualizar Doppler, Vercel production, redeploy e validar com probe/logs.
- Envio/publicação: Sem envio externo para cliente; houve update autorizado de secrets/env e deploy production técnico.
- Writes externos: Doppler secret update; Vercel production env update; Vercel production deploy.
- Riscos/bloqueios: O secret foi colado no Telegram antes da atualização; recomendar rotação futura se Lucas quiser reduzir exposição. Monitorar próximos pedidos reais para garantir que POS/orders lifecycle sigam 200.
- Rollback/mitigação: Rollback possível: restaurar valor anterior do SHOPIFY_WEBHOOK_SECRET se documentado em Doppler/Vercel history e redeploy; não foi impresso nem salvo em receipt. Probe fake removido do ledger.
- Próximos passos: Monitorar logs das próximas vendas reais; se POS orders/paid ainda apresentar 401 após novo evento, validar se é a mesma app secret/subscription; decidir backfill/reconciliação dos pedidos perdidos se necessário.
- Onde foi documentado no Brain: areas/lk/sub-areas/atendimento/receipts/lk-shopify-webhook-secret-rotation-vercel-redeploy-20260610.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
