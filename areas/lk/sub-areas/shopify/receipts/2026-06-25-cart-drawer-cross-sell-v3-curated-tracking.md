# Receipt — Cart drawer cross-sell v3 curated light tracking

- Data/hora: 2026-06-25T20:08:03.549518+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify cart drawer
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou: Aprovo DEV e merge Production cart drawer cross-sell v3 curated-light + tracking.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-25-cart-drawer-cross-sell-v3-curated-tracking.md; report areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-v3-quality-tracking.md; workdir /opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625.
- O que foi feito:
- Substituído mapa v2 public-filtered por v3 curated-light no cart drawer; v3 tem 22 handles e 37 regras após curadoria leve. Adicionados eventos sem PII lk_cart_cross_sell_view, lk_cart_cross_sell_click e lk_cart_cross_sell_add via window.dataLayer e CustomEvent. Mantido /collections/all ausente.
- Output/artefato:
- DEV readback OK em theme 155065450718. PR #102 merged: https://github.com/lk-snkrs/lk-new-theme/pull/102. Production ref final 58e0ac09e91a32207bc6edee3e19a96aee3fb338. GitHub readback bate target sha256 c970e05bcf664d824a173558513eb4c12b757ec7444ede21a9fe727d39f60ae2. Shopify Production readback bate target sha256 c970e05bcf664d824a173558513eb4c12b757ec7444ede21a9fe727d39f60ae2. Public HTML PDP status 200 contém v3 e os três eventos de tracking; /collections/all/products.json ausente. Runtime CDP de cart add ficou bloqueado por Shopify HTTP 429 no /cart/add.js, portanto dataLayer live event firing não foi confirmado nesta rodada.
- Aprovação: Aprovação explícita atual de Lucas para DEV e merge Production no escopo cart drawer cross-sell v3 curated-light + tracking.
- Envio/publicação: Telegram final com PR, readback, QA e caveat de 429.
- Writes externos: Shopify DEV asset PUT em theme 155065450718; GitHub PR #102 merge para production; Shopify Production atualizado por pipeline/sync e validado por readback. Sem produto, preço, estoque, checkout config, metafields, cron, GMC, ads, Klaviyo, WhatsApp ou e-mail.
- Riscos/bloqueios: Live event firing de dataLayer não confirmado por bloqueio 429 no cart add durante QA automatizado; source/readback confirmam código. Próxima validação deve ser reexecutada mais tarde ou via navegador humano para evitar rate-limit.
- Rollback/mitigação: Reverter PR #102 para voltar ao PR #101 / v2 public-filtered. Backup DEV antes do write em /opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/dev_before_cross_sell_v3_curated_tracking_snippets__lk-cart-drawer.liquid.
- Próximos passos: Revalidar runtime dataLayer view/click/add quando o rate-limit do cart API aliviar; depois decidir se liga captura no GTM/GA4.
- Onde foi documentado no Brain: Receipt criado via writer; report/approval packet já estavam no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
