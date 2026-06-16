# Receipt — Salomon XT-6 collection final guide fix

Status: production/dev patched; Shopify default URL page-cache still alternates old/new in public curl checks.

Changes applied:
- `sections/lk-collection.liquid`: inserted scoped LKGOC Salomon final guide bridge after product grid.
- `templates/collection.salomon-xt6-lkgoc.json`: created from `collection.lkgoc.json` in DEV and production.
- Collection `salomon-xt-6`: template_suffix changed to `salomon-xt6-lkgoc`.
- `assets/lk-footer.js`: added scoped runtime bridge for `/collections/salomon-xt-6` as fallback once asset cache updates.
- `config/settings_data.json`: non-visual cache-bust key added.

Verification:
- `?view=salomon-xt6-lkgoc`: returns marker `lk-goc-salomon-final-guide` and guide URL `/pages/guia-salomon-xt-6`.
- Default URL: Shopify page-cache shards still alternate between old HTML and patched HTML; not 100% decision-grade yet.

Rollback assets saved in this folder with prefixes:
- `rollback-before-salomon-final-guide-*`
- `rollback-lk-footer-before-salomon-guide-*`
- `rollback-settings-data-before-cachebust-*`
- `rollback-collection-salomon-template-suffix-*`
