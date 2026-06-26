# Receipt — NB 204L guide LKGOC

Date: 2026-06-02
Target: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk

## Writes executed
- Shopify Page `127336644830`
  - `title`: Guia New Balance 204L Original Brasil | LK Sneakers
  - `body_html`: full LKGOC guide body with black editorial hero, FAQ, media signals, product cards and FAQPage JSON-LD
  - `template_suffix`: `nb204l-guide`
- Production theme `155065417950` (`lk-new-theme/production`)
  - created `sections/lk-nb204l-guide-lkgoc.liquid`
  - created `templates/page.nb204l-guide.json`
  - also patched existing `sections/lk-geo-source-pages-v2.liquid` case for the same page handle as fallback

## Evidence
- Verified new page renders with `?view=nb204l-guide` and `?view=geo-source`.
- Default canonical route is still returning Shopify `PageDetailsController` stale cache with old `lk-auth-layout` body at time of verification.
- Default route cache headers show dynamic Shopify page cache ETag, not Cloudflare static HIT.

## Backups / rollback
- Page backup: `backup-page.json` and `backup-page-before-template-switch.json`
- Body backup: `backup-body.html`
- Section backup: `backup-section-lk-geo-source-pages-v2.liquid`
- New body source: `new-body.html`

Rollback:
1. Restore page body/title/template suffix from page backup.
2. Remove or leave unused `templates/page.nb204l-guide.json` and `sections/lk-nb204l-guide-lkgoc.liquid`.
3. Restore `sections/lk-geo-source-pages-v2.liquid` from backup section file.

## Notes
No price, stock, variants, images, campaigns, GMC, Klaviyo or checkout settings were touched.
