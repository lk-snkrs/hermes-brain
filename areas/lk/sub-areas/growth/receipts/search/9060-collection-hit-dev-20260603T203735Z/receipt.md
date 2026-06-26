# Receipt — Dev preview: search collection hit for 9060

Date UTC: 20260603T203735Z

## Approval

Lucas approved: `aprovo aplicar no tema dev o módulo de coleção encontrada para busca 9060`.

## Scope executed

- Shopify Dev/unpublished theme only.
- Theme ID: `155065450718`
- Theme name: `lk-new-theme/dev`
- Theme role verified before upload: `unpublished`
- Asset: `sections/lk-search.liquid`
- Git branch: `fix/search-collection-hit-9060`
- Commit: `a1cd36a0bd59` (`feat(search): surface 9060 collection shortcut`)
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/21`

## Non-actions

- Production theme was not changed.
- No Shopify product, collection, price, stock, checkout, Search & Discovery settings, apps, campaigns or metafields were changed.

## Technical change

Added a curated collection-hit module for high-intent 9060 searches in `sections/lk-search.liquid`.

Mapped terms:

- `9060`
- `new balance 9060`
- `nb 9060`
- `newbalance 9060`

Rendered module:

- Eyebrow: `Coleção encontrada`
- Title: `New Balance 9060`
- Text: `Veja todos os modelos, cores e tamanhos disponíveis na curadoria LK.`
- CTA: `Ver coleção 9060`
- Link: `/collections/new-balance-9060`

The existing product search behavior was preserved:

- `type=product` hidden input remains in the search form.
- Product grid render remains via `lk-product-card`.
- Search filters/sort/load-more code remains present.

## Readback evidence

Precheck:

- Dev theme: `lk-new-theme/dev`, role `unpublished`
- Production theme: `lk-new-theme/production`, role `main`

Asset SHA-16:

- Dev before: `dcb60b4ab1cc6818`
- Target/local: `08a64a88375c3c4a`
- Dev after/readback: `08a64a88375c3c4a`
- Production before: `dcb60b4ab1cc6818`
- Production after: `dcb60b4ab1cc6818`

Results:

- `dev_readback_matches_target: true`
- `production_unchanged: true`
- `dev_has_module: true`

## QA

Static/local checks passed:

- Single collection module render block exists.
- `new-balance-9060` target link exists.
- `Ver coleção 9060` CTA exists.
- Product-only search form remains preserved.
- Product grid render remains preserved.
- Search filters remain present.

Public unauthenticated preview limitation:

- Fetching `https://lksneakers.com.br/search?q=9060&preview_theme_id=155065450718&cb=dev9060qa` returned live-like HTML without the dev module, matching the known Shopify preview-cookie/cache limitation for unpublished themes.
- Therefore, visual QA must be completed through an authenticated Shopify preview session or by Lucas opening the Dev preview link.

Suggested Dev preview URL:

`https://lksneakers.com.br/search?q=9060&preview_theme_id=155065450718`

Expected visual result in authenticated preview:

- A card/strip appears below the black search banner and before the toolbar.
- It says `Coleção encontrada` and `New Balance 9060`.
- CTA points to `/collections/new-balance-9060`.
- Products continue below.

## Rollback

Backup files:

- `dev_before.liquid`
- `production_before.liquid`
- `upload_summary.json`

Rollback Dev:

1. Re-upload `dev_before.liquid` to theme `155065450718`, key `sections/lk-search.liquid`.
2. Verify readback SHA returns to `dcb60b4ab1cc6818`.
3. Close/revert PR #21 if the preview is rejected.

## Next decision

Lucas should review the authenticated Dev preview. If approved visually, next step is either:

1. Merge PR #21 into `dev`; or
2. Request adjustments to copy/layout; or
3. Approve a separate production promotion after final Dev validation.
