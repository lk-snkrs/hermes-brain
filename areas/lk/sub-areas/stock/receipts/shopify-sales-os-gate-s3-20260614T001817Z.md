# Receipt — Shopify Sales OS Gate S3 local DB read-only

- Data/hora: 2026-06-14T00:33:31.357720+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Criar para vendas Shopify o mesmo padrão operacional do Stock OS/Tiny: database local, backfill, sync incremental/webhook preparado, endpoint/dashboard e guardrails read-only.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin API read-only via Doppler lc-keys/prd; DB local SQLite shopify_sales_os; summary local JSON; testes unitários e dashboard local.
- O que foi feito:
- Implementado script shopify_sales_os.py com schema SQLite, backfill read-only, ingestão por payload/fixture, ledger idempotente, export-summary e verificação HMAC; executado backfill real read-only desde 2026-01-01; criado PRD Gate S3 e approval packet de webhook sem ativar subscription; integrado endpoint /api/vendas/shopify-sales-os e painel Shopify Sales OS na aba Vendas.
- Output/artefato:
- DB local com 1956 pedidos e 3311 unidades; summary versionado shopify_sales_os_summary.json; dashboard commit 0d1a108 enviado para origin/feat/stock-os-api-adapter; Brain commit 1677e95 com script/testes/PRD/approval packet/summary.
- Aprovação: Lucas pediu seguir com o padrão DB local + sync + webhook para vendas Shopify; push GitHub foi parte do pedido atual; webhooks reais ainda NÃO ativados e exigem aprovação futura por approval packet.
- Envio/publicação: GitHub push do branch de dashboard e commit local Brain; nenhum contato com cliente/fornecedor; nenhum write Shopify/Tiny.
- Writes externos: GitHub push do branch de dashboard; Shopify write 0; Tiny write 0; webhook subscription 0.
- Riscos/bloqueios: Ativação real de webhooks Shopify permanece bloqueada até aprovação escopada; DB SQLite bruto não foi versionado por tamanho/operacional, apenas summary versionado.
- Rollback/mitigação: Reverter commits 0d1a108/1677e95 se necessário; manter ou apagar DB local se necessário; nenhuma alteração foi feita em Shopify/Tiny; webhooks não foram ativados.
- Próximos passos: Se aprovado: configurar rota pública hermes-webhooks com HMAC, ativar subscriptions Shopify orders/paid/create/updated, rodar smoke assinado e criar cron incremental/read-only.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/prds/shopify-sales-os-gate-s3-20260614T001817Z.md; areas/lk/sub-areas/stock/approval-packets/shopify-sales-os-webhook-activation-20260614T001817Z.md; areas/lk/sub-areas/stock/scripts/shopify_sales_os.py; areas/lk/sub-areas/stock/tests/test_shopify_sales_os.py
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
