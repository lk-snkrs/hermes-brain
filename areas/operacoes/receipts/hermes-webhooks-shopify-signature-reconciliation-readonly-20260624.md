# Receipt — Hermes Webhooks Shopify signature reconciliation read-only

- Data/hora: 2026-06-24T23:17:51.110397+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas aprovou seguir do 1 ao 4: verificar Shopify webhook registry, comparar presença/status entre Shopify/Doppler/Vercel/Hermes, preparar packet se drift confirmado, e não mutar sem aprovação escopada.
- Classificação: read-only
- Fontes usadas:
- Shopify Admin REST read-only; Vercel/Hermes no-op probes; /opt/data/config.yaml; Doppler lc-keys/prd exists; live gateway process env booleans; no secret values printed
- O que foi feito:
- Confirmado que Shopify provider HMAC com SHOPIFY_WEBHOOK_SECRET passa na Vercel; falha real é Vercel -> Hermes: Vercel assina com HERMES_WEBHOOK_SECRET, enquanto rota static lk-shopify-pos-restock espera WEBHOOK_SECRET legado. Shopify registry tem 33 webhooks; POS restock aponta para hermes-webhooks.vercel.app. Approval packet criado para alinhar a rota para HERMES_WEBHOOK_SECRET.
- Output/artefato:
- areas/operacoes/reports/hermes-webhooks-shopify-signature-reconciliation-20260624.md; areas/operacoes/approval-packets/hermes-webhooks-shopify-route-secret-alignment-20260624.md
- Aprovação: Lucas: Seguir do 1 ao 4; mutação de gateway/config/secrets ainda não executada por exigir aprovação escopada operacional.
- Envio/publicação: Nenhum envio externo; probes no-op; sem WhatsApp/e-mail/campanha.
- Writes externos: nenhum
- Riscos/bloqueios: Shopify POS restock continua bloqueado até alinhar secret da rota Hermes; gateway restart/config change requer aprovação e rollback. POS restock usa alias vercel.app, não custom domain, mas isso não causou a falha.
- Rollback/mitigação: Não houve mutação externa nem restart. Artefatos locais podem ser removidos; estado produtivo não foi alterado.
- Próximos passos: Se Lucas aprovar o approval packet, fazer backup de config.yaml, trocar secret_doppler da rota lk-shopify-pos-restock para HERMES_WEBHOOK_SECRET, reiniciar/verificar gateway default com Doppler-first, e repetir probe até 200 ignored.
- Onde foi documentado no Brain: Brain report + approval packet + receipt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
