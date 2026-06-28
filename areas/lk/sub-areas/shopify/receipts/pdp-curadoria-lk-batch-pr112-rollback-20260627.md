# Receipt — Rollback PR112 Curadoria LK batch duplicated rails

- Data/hora: 2026-06-27T16:25:57.815319+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas apontou duplicação visual da Curadoria LK e aprovou rollback do PR #112.
- Classificação: external-write
- Fontes usadas:
- Screenshot de Lucas; probes públicos de duplicação; GitHub PR #114; Shopify Production Admin readback; delayed public cache watcher.
- O que foi feito:
- PR #114 criado e mergeado contra production removendo a render line do batch families 1-5 e deletando o snippet snippets/lk-variante-batch-families-1-5-20260627.liquid. Shopify Admin Production readback confirmou section match e snippet 404. Watcher público posterior confirmou cache limpo nos 2 PDPs remanescentes.
- Output/artefato:
- PR #114 MERGED; merge commit 3d9f9f2752518ad56d9851fbf9c5c1d6e1e51efc; GitHub production render_removed=true, snippet_deleted=true; Shopify Production Admin section SHA12 8243f12847bb match=true e snippet 404. Delayed watcher: tentativa 2 em 2026-06-27T16:22:10Z retornou bad=[]; NB9060 Sea Salt e Nike Vomero Black Volt HTTP 200, Liquid errors 0, count=1, markers top30-nb-9060/top30-vomero-premium, has_batch=false; values_printed=false.
- Aprovação: Aprovo rollback
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge + Shopify Production readback. Sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp/email.
- Riscos/bloqueios: Resolvido após cache público limpar. Aprendizado propagado para skill lk-shopify-theme-cro: probe público anti-duplicação no batch inteiro antes de merge, e cache pending só fecha após HTML público limpar.
- Rollback/mitigação: Rollback do rollback seria reverter PR #114, não recomendado porque PR #112 causou duplicação.
- Próximos passos: Para próximos batches, somente incluir handles com lk_variante_section_count=0 no HTML público ou fazer dedupe/substituição explícita aprovada.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/curadoria-batch-families-1-5-dev-20260627/rollback-pr112; skill lk-shopify-theme-cro atualizada; receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
