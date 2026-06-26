# Rollback — Nike Mind dev preview

Scope: unpublished theme `lk-new-theme/dev` / `155065450718` only.

To rollback:
1. Restore `layout/theme.liquid` from `layout__theme.before.liquid`.
2. Restore or delete `snippets/lk-growth-nike-mind-seo-geo-preview.liquid` using `snippet.before.liquid`.
3. Re-run readback and verify marker absent.

Production was not touched.
