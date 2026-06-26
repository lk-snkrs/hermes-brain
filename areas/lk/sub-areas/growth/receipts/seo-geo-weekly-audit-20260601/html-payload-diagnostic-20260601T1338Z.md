# LK Sneakers — HTML payload diagnostic

Timestamp UTC: 2026-06-01T13:38Z
Scope: read-only public storefront + local theme inspection. No Shopify write, no app/theme change.

## Verdict

Yes, HTML can be reduced, but not by blindly editing theme code. The biggest raw payload source is not Product schema or page copy; it is app/embed payload injected into every page, especially Variant King / StarApps.

Recommended priority: P1 diagnostic/pilot, not emergency P0. The pages are large in decoded HTML, but Shopify is serving Brotli-compressed HTML around 116–130 KB over the wire and server processing is ~30–34 ms, so the urgent risk is browser parse/execute/third-party JS more than network transfer alone.

## URLs measured

- Home: https://lksneakers.com.br/
- PDP: https://lksneakers.com.br/products/nike-dunk-low-rose-whisper
- Collection: https://lksneakers.com.br/collections/air-jordan-1

## Raw HTML and transfer size

Home:
- Decoded HTML: 1,149,219 bytes
- Brotli content-length: 115,897 bytes
- Shopify processing: ~31 ms
- Mobile request median proxy: ~248 ms
- Head bytes: ~801 KB
- Body bytes: ~348 KB

PDP:
- Decoded HTML: 1,241,376 bytes
- Brotli content-length: 129,699 bytes
- Shopify processing: ~30 ms
- Mobile request median proxy: ~254 ms
- Head bytes: ~813 KB
- Body bytes: ~429 KB

Collection:
- Decoded HTML: 1,314,212 bytes
- Brotli content-length: 127,968 bytes
- Shopify processing: ~34 ms
- Mobile request median proxy: ~476 ms
- Head bytes: ~852 KB
- Body bytes: ~463 KB

Interpretation:
- Wire transfer is compressed well.
- Decoded DOM/head is heavy.
- The head is abnormally large because app embeds inject large inline JS/CSS.

## Largest contributors found

### 1. Variant King / StarApps combined listings — biggest source

Observed on all 3 URLs.

Per page approximate decoded payload:
- Inline `window.vkcl_data`: ~460 KB
- Inline/app CSS for `variant-king-combined-listing` / `swatch-preset`: ~188 KB
- External scripts also loaded from Shopify extension + `cdn.starapps.studio`.

Total rough decoded impact: ~648 KB per page before external JS execution.

Theme setting source:
- `config/settings_data.json`
- App embed: `shopify://apps/sa-variants/blocks/variant-king-combined-listing/...`
- Currently `disabled: false`.

Risk:
- High to disable without validation because it may control variant grouping/swatch behavior/combined listings.
- But it is the single best candidate for a dev-theme A/B payload test.

### 2. Rivo Loyalty app embed

Observed on all 3 URLs.

Approx decoded inline payload:
- ~95–100 KB per page.

Theme setting source:
- `config/settings_data.json`
- App embed: `shopify://apps/rivo-loyalty-rewards-referrals/blocks/app-embed/...`
- Currently `disabled: false`.

Risk:
- Medium. It may support rewards/loyalty UX, but likely not critical for first paint on collection/PDP.
- Candidate for delayed loading or route-limiting if app supports it.

### 3. Simprosys / Google Shopping Feed storefront block

Observed as large hidden inline script.

Approx decoded payload:
- ~48 KB per page.

Theme setting source:
- `config/settings_data.json`
- App embed: `shopify://apps/simprosys-google-shopping-feed/blocks/core_settings_block/...`
- Currently `disabled: false`.

Risk:
- Medium-high until confirmed. It may support dynamic remarketing/feed tracking, not just GMC feed.
- Needs app-purpose check before disabling.

### 4. Judge.me

Observed on all 3 URLs.

Approx decoded inline/settings payload:
- ~19–23 KB pattern match plus ~34 KB `window.jdgmSettings` block.

Risk:
- Medium. Reviews/trust are important, especially PDP.
- Route gating might be possible: keep PDP, reduce collection/home if not needed above fold.

### 5. LK theme inline CSS/JS

Local theme file sizes:
- `sections/lk-collection.liquid`: 244,698 bytes / 3,185 lines
- `sections/lk-pdp.liquid`: 122,305 bytes / 2,540 lines
- `layout/theme.liquid`: 80,210 bytes / 1,330 lines
- `sections/lk-header.liquid`: 40,026 bytes / 982 lines
- `sections/lk-footer.liquid`: 25,312 bytes / 550 lines

Collection page has a large inline style block:
- Collection section inline style top segment: ~66.8 KB
- Product/filter CSS contributes to collection payload.

Risk:
- Lower than app embeds if handled carefully in dev theme.
- Moving stable inline CSS into theme assets would reduce HTML and improve caching, but needs theme dev preview/QA before production.

### 6. Footer payment SVG icons

Observed repeated SVGs in footer.

Approx decoded contribution:
- 18–30 KB depending page.

Risk:
- Low-medium. Can be optimized to simpler text/icon sprite or CSS background.
- Visual QA required.

## Low-risk / high-signal pilot plan

No changes made. Recommended next step is a dev-theme measurement pilot:

1. Dev theme snapshot.
2. Create a dev preview variant with only one change at a time.
3. Measure decoded HTML, Brotli size, Lighthouse mobile, and visual behavior.
4. Revert or keep depending evidence.

Suggested experiments, in order:

### Experiment A — Variant King route/disable test on dev

Goal:
- Quantify whether disabling/gating the embed saves ~600 KB decoded HTML without breaking variant selection.

Validation required:
- PDP variant selection and sizes still work.
- Combined listings/swatch behavior still works or has acceptable native fallback.
- Collections still show product cards correctly.
- No JS console breakage.

Expected impact:
- Largest potential reduction.

Approval required:
- Yes. Even dev theme upload/settings change is Shopify/theme write.

### Experiment B — Rivo delayed/route gating

Goal:
- Avoid loading loyalty app payload on pages where rewards are not immediately needed.

Validation required:
- Rewards page/account/launcher still works.
- No checkout/cart regression.

Expected impact:
- Medium.

Approval required:
- Yes.

### Experiment C — Simprosys storefront block purpose check

Goal:
- Confirm if storefront app embed is necessary for GMC/dynamic remarketing or just app boilerplate.

Validation required:
- No GMC/feed write.
- No conversion tracking assumption without checking app docs/admin behavior.

Expected impact:
- Medium.

Approval required before disabling:
- Yes.

### Experiment D — Move LK collection/PDP CSS to cached asset

Goal:
- Reduce repeated inline CSS in HTML, especially collection pages.

Validation required:
- Mobile collection layout, filter sheet, product grid, trust strips, badges, PDP CTA area.

Expected impact:
- Medium for HTML cleanliness, lower for total transfer if CSS remains same size but cacheable.

Approval required:
- Yes.

## What not to do now

- Do not remove Product/Organization schema; schema is not the payload problem.
- Do not remove reviews globally without PDP trust impact analysis.
- Do not disable Variant King in production without dev proof.
- Do not edit production theme directly.
- Do not treat lower decoded HTML alone as success; validate mobile visual and conversion-critical behavior.

## Recommendation for Lucas

Proceed with a P1 dev-theme payload pilot, starting with Variant King measurement, because it dominates the decoded HTML. Keep production untouched until a before/after packet proves:

- HTML reduction;
- Lighthouse/mobile improvement;
- no visible PDP/collection regression;
- rollback path.

If Lucas approves, exact approval scope should be:

`Aprovo criar um teste no tema dev da LK para medir redução de payload, começando por Variant King/StarApps, sem publicar produção e sem alterar preço/estoque/produtos/campanhas.`
