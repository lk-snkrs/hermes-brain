# Receipt — Hermes Webhooks Vercel signed no-op probes

- Data/hora: 2026-06-24T22:41:43.477558+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas pediu seguir após auditoria read-only do Vercel hermes-webhooks; executar probes assinados no-op por provider crítico.
- Classificação: read-only
- Fontes usadas:
- Doppler lc-keys/prd injected secrets without printing values; hermes-webhooks custom domain; Hermes gateway logs; no-op signed payloads for Shopify, Evolution and Klaviyo
- O que foi feito:
- Executados probes assinados no-op: Evolution aceito 202 e chegou ao Hermes; Klaviyo aceito 202 e logou no-op; Shopify POS restock rejeitou assinatura com 401 Invalid signature usando secret canônico Doppler. Relatório salvo no Brain.
- Output/artefato:
- areas/operacoes/reports/hermes-webhooks-signed-noop-probes-20260624.md
- Aprovação: Lucas: Seguir
- Envio/publicação: Nenhum envio externo; payloads no-op; sem WhatsApp/e-mail/campanha.
- Writes externos: nenhum
- Riscos/bloqueios: Shopify webhook ingress não está provado; provável drift de SHOPIFY_WEBHOOK_SECRET entre Doppler/Vercel/Shopify ou secret ativo diferente. Evolution/Klaviyo aceitam assinatura mas usam processamento assíncrono 202, não resposta determinística 200.
- Rollback/mitigação: Não houve mutação externa. Artefatos locais/report/receipt podem ser removidos; probes não alteraram Vercel, Shopify, Klaviyo, Evolution, gateway ou secrets.
- Próximos passos: P0 preparar reconciliação read-only do Shopify webhook secret e registry; se drift confirmado, pedir aprovação escopada para corrigir/rotacionar Vercel/Shopify secret e repetir probe até 200 ignored.
- Onde foi documentado no Brain: Brain report + receipt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
