# Rollback — Nike Mind production merge

Scope: production theme `lk-new-theme/production` / `155065417950` only.

1. Restore `layout/theme.liquid` from `production_layout.before.liquid`.
2. Restore/delete `snippets/lk-growth-nike-mind-seo-geo-preview.liquid` using `production_snippet.before.liquid`.
3. Fetch public storefront and verify block/schema absent.
