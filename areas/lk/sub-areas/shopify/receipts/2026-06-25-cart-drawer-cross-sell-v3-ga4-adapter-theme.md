# Receipt — Cart drawer cross-sell v3 GA4 theme adapter

- Data/hora: 2026-06-26T00:15:21.743329+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify cart drawer analytics
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou: Aprovo DEV e merge Production adapter GA4 para eventos cart drawer cross-sell v3.
- Classificação: external-write
- Fontes usadas:
- Approval in Telegram current turn; prior GA4 Admin 403 receipt; production source snippets/lk-cart-drawer.liquid; workdir /opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625.
- O que foi feito:
- Adicionado adapter GA4 no cart drawer v3: mantém dataLayer object events e CustomEvents existentes e também envia window.gtag('event', eventName, params) com parâmetros normalizados sem PII. Adapter version 2026-06-25-ga4-adapter-v1. Scope exclusivo snippets/lk-cart-drawer.liquid.
- Output/artefato:
- DEV readback OK em theme lk-new-theme/dev 155065450718. PR #103 merged: https://github.com/lk-snkrs/lk-new-theme/pull/103. Production ref 2b41c4ff59a30a99fd6b7c92f00254a0e6836365. GitHub and Shopify Production readback sha256 ad6da891fc299ffee27e3662348727d075a5d97b41e349088b041124af33daa9 matched target. Public HTML 200 contained v3, adapter marker, adapter event, gtag event call, and three cross-sell events; /collections/all count 0. Runtime CDP first pass: /cart/add.js 200, drawer opened, one card rendered, dataLayer object view event present, gtag view command present, adapter CustomEvent present, no adapter errors. A later retry hit Shopify 429, so click/add runtime confirmation remains pending.
- Aprovação: Aprovação explícita atual de Lucas for DEV and Production merge of GA4 adapter for cart drawer cross-sell v3.
- Envio/publicação: Telegram final with PR/readbacks/QA caveat.
- Writes externos: Shopify DEV asset PUT; GitHub PR #103 merge to production; Shopify Production updated by normal theme pipeline and verified by Admin readback. No product, price, stock, checkout config, GA4 Admin, GTM, GMC, ads, Klaviyo, WhatsApp or email writes.
- Riscos/bloqueios: GA4 Admin custom definitions remain blocked by prior 403; adapter sends gtag/dataLayer commands but GA4 reporting dimensions still need Editor/Admin or later setup. Runtime view event confirmed; click/add runtime confirmation pending due later 429.
- Rollback/mitigação: Revert PR #103 to remove only the GA4 adapter and keep v3 curated-light dataLayer/CustomEvent tracking. Backup DEV before write: /opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/dev_before_ga4_adapter_v3_snippets__lk-cart-drawer.liquid.
- Próximos passos: Revalidate click/add gtag events when Shopify 429 clears; obtain GA4 Editor/Admin permission if custom dimensions/metrics need to be created.
- Onde foi documentado no Brain: Receipt via writer; local evidence JSONs in workdir: ga4_adapter_v3_github_readback.json, ga4_adapter_v3_shopify_production_readback.json, ga4_adapter_v3_public_html_check.json, ga4_adapter_v3_runtime_cdp_qa_view_success_observed.json.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
