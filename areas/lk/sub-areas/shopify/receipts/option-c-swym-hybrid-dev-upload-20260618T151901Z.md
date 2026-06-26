# Receipt — Opção C SWYM híbrido DEV — 20260618T151901Z

- values_printed: false
- alvo: Shopify theme DEV `155065450718` (`lk-new-theme/dev`, role `unpublished`)
- produção: `155065417950` (`lk-new-theme/production`, role `main`)
- ação: upload DEV-only de `assets/lk-swym-hybrid-v1.js` e patch em `layout/theme.liquid`
- rollback snapshot: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_dev_upload/rollback-before-option-c-dev-upload-20260618T151901Z.json`
- receipt JSON: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_dev_upload/option-c-dev-upload-receipt-20260618T151901Z.json`

## Readback

- JS hash match: `True`
- layout hash match: `True`
- marker count: `1`
- asset reference count: `1`
- Production layout unchanged: `True`
- Production settings unchanged: `True`
- Dev SWYM enabled app blocks: `0`

## QA CDP mobile DEV

- QA JSON: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_dev_upload/option-c-dev-qa-cdp-20260618T152019Z.json`
- screenshot: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_dev_upload/option-c-dev-pdp-mobile-20260618T152019Z.png`
- before click: hybrid asset present, `window.LKSwymHybrid=true`, SWYM SDK scripts `0`, `_swat=false`, wishlist button found.
- after click: SWYM SDK scripts `1`, `_swat=true`, queue length `0`, loaded `true`.

## Rollback

Restore the DEV assets from the rollback JSON. Do not touch Production unless separately approved.
