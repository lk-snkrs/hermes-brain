# Receipt — Cart drawer stop same 4 upsell fallback

- Data/hora: 2026-06-25T18:41:58.144153+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify cart drawer
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou: Aprovo DEV e merge Production cart drawer stop same 4 upsell fallback.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-25-cart-drawer-upsell-stop-same-four.md; workdir /opt/data/profiles/lk-shopify/workdirs/cart-drawer-upsell-inner-fix-20260625; PR #99; DEV/GitHub/Shopify readbacks.
- O que foi feito:
- Aplicado em DEV e Production o patch que remove o fallback genérico /collections/all/products.json do cart drawer upsell, escondendo o bloco quando não há model match para evitar repetir sempre os mesmos 4 produtos. Também adicionados padrões de modelo para Salomon XT-6 e Autry Medalist.
- Output/artefato:
- DEV readback OK: target sha256 b4242155f39146e036a9fe687b8412878b2d237720d3c8fdde508e709eebde72, collections_all_count=0, hides_generic_fallback=true. PR #99 merged: https://github.com/lk-snkrs/lk-new-theme/pull/99; production ref a7dbf00250c756faf5eacd33f9fd3e9708b4252e. GitHub fresh readback and Shopify Production theme 155065417950 match target: collections_all_count=0, salomon/autry patterns=true. Public HTML QA hit HTTP 429 on PDP/home, so public visual QA remains blocked by storefront rate limit.
- Aprovação: Aprovação explícita atual de Lucas para DEV e merge Production no escopo cart drawer stop same 4 upsell fallback.
- Envio/publicação: Telegram final com PR/readback/QA caveat/rollback.
- Writes externos: Shopify DEV asset PUT em theme 155065450718; GitHub PR #99 merge para production; Shopify Production atualizado pelo pipeline/sync e validado por readback. Sem produto, preço, estoque, checkout config, metafields, cron, ads, Klaviyo, WhatsApp ou campanhas.
- Riscos/bloqueios: Produtos sem modelo mapeado deixam de exibir upsell em vez de cair nos mesmos 4 genéricos. A fase LK Stock prioridade segue pendente via handoff separado; public visual QA bloqueado por 429.
- Rollback/mitigação: Reverter PR #99 para restaurar fallback /collections/all; backup DEV antes em /opt/data/profiles/lk-shopify/workdirs/cart-drawer-upsell-inner-fix-20260625/dev_before_stop_same_four_snippets__lk-cart-drawer.liquid.
- Próximos passos: Aguardar LK Stock devolver regra/lista priorizada para implementar fallback inteligente por prioridade real de estoque/grade/giro.
- Onde foi documentado no Brain: Receipt criado via writer; handoff LK Stock já existente em areas/lk/sub-areas/stock/handoffs/cart-drawer-upsell-priority-logic-request-20260625.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
