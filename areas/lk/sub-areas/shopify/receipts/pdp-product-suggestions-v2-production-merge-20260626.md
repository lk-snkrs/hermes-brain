# Receipt — PDP Product Suggestions v2 Production merge

- Data/hora: 2026-06-26T14:32:09.197567+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou merge Production do Product Suggestions v2 do PDP.
- Classificação: external-write
- Fontes usadas:
- Approval DEV receipt areas/lk/sub-areas/shopify/receipts/pdp-product-suggestions-v2-dev-20260626.md; PR #110; GitHub production; Shopify Production readback; public QA.
- O que foi feito:
- PR #110 criado e mergeado contra production com diff mínimo em sections/lk-pdp.liquid. Product Suggestions v2 substitui Relacionados legado por Recommendations API filtrada + fallback Liquid, preservando Curadoria LK e Google Reviews.
- Output/artefato:
- PR #110 MERGED; merge commit 6a987f2514e3ccc953eb5e962b503c728bd4dccc; GitHub production SHA 869d257b3bf935ebab27cee232eaceba08bb7e23; Shopify Production Theme 155065417950 readback HTTP 200 SHA12 fe0864c6ca28; public QA HTTP 200/Liquid errors 0 nos PDPs Saint George, AJ1 Panda e Onitsuka Triple Black; JS node --check OK; NB9060 Bone Sparrow não aparece no filtro.
- Aprovação: Aprovo merge Production do Product Suggestions v2 do PDP.
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge + Shopify Production theme sync/readback. Asset sections/lk-pdp.liquid. Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp. values_printed=false.
- Riscos/bloqueios: Médio: JS client-side e API de recomendações; fallback filtrado reduz risco. Pode esconder bloco se menos de 2 candidatos coerentes.
- Rollback/mitigação: Reverter PR #110 / merge commit 6a987f2514e3ccc953eb5e962b503c728bd4dccc; ou restaurar /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v2-20260626/prod-merge/prod_before_sections__lk-pdp.liquid em sections/lk-pdp.liquid via PR.
- Próximos passos: Monitorar visualmente PDPs e, se Lucas apontar baixa qualidade residual, evoluir ranking com sinais de co-purchase/curadoria por família.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v2-20260626/prod-merge com prod before/target/diff/readback/QA.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
