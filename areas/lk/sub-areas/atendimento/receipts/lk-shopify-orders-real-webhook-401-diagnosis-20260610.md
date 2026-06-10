# Receipt — LK Shopify orders real webhook 401 diagnosis

- Data/hora: 2026-06-10T11:35:16.190824+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / atendimento / Shopify webhooks
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas perguntou se novas vendas LK chegaram via webhook e pediu seguir no diagnóstico seguro.
- Classificação: read-only
- Fontes usadas:
- Shopify Admin REST read-only, Shopify webhook registry readback, Vercel production logs hermes-webhooks, Hermes gateway logs, local ingest ledger, Doppler presence checks values_printed=false.
- O que foi feito:
- Verificado que Shopify tem pedidos novos #147739-#147741 pagos/web em 2026-06-10; webhooks orders/create/updated/cancelled e POS orders/paid estão registrados para hermes-webhooks; Vercel logs das últimas horas mostram 76 respostas 401 para /webhooks/lk-shopify-orders-ingest e 13 para /webhooks/lk-shopify-pos-restock; probe seguro assinado com Doppler SHOPIFY_WEBHOOK_SECRET retornou HTTP 200 e gravou ledger; fake ledger removido após teste.
- Output/artefato:
- Causa provável confirmada por evidência: Shopify real chega ao Vercel, mas é rejeitado no primeiro HMAC layer com 401 antes do Hermes/ledger. Como probe assinado com Doppler passa 200, Doppler/Vercel/Hermes estão coerentes entre si; o segredo atual não corresponde ao client secret/API secret key real do app Shopify que assina as entregas.
- Aprovação: Nenhuma correção externa executada. Seguir com update de secret/Vercel/deploy requer aprovação escopada e o client secret correto do app Shopify.
- Envio/publicação: Sem mensagem externa para cliente/fornecedor.
- Writes externos: nenhum
- Riscos/bloqueios: Enquanto não corrigir, vendas reais continuam sem entrar no ledger webhook; POS postpurchase webhook também recebe 401. Reconciliadores/polling podem mitigar, mas não substituem ingress canônico.
- Rollback/mitigação: Fake order 991810999999 removido do ledger local; ledger ficou com remaining_count=0. Sem rollback externo necessário.
- Próximos passos: Obter client secret/API secret key correto do app/custom app Shopify; atualizar SHOPIFY_WEBHOOK_SECRET no Doppler lc-keys/prd e Vercel production hermes-webhooks; redeploy; repetir probe seguro e aguardar/forçar retry real Shopify; só depois tratar backfill/reconciliação se aprovado.
- Onde foi documentado no Brain: Receipt criado via hermes_memory_os_receipt_writer.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
