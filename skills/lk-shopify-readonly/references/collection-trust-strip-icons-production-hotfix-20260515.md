# Collection trust strip icons production hotfix — LK Sneakers (2026-05-15)

Use this as a concrete reference when Lucas asks for a small visual hotfix on LK collection pages, especially adding/refining icons in the collection benefits/trust strip.

## Context

Task: add icons to the collection-page trust strip under the collection banner on production.

Asset touched: `sections/lk-collection.liquid`.

Target theme verified before write:

- Shopify theme name: `lk-new-theme/production`
- role: `main`
- observed ID: `155065417950`

## Safe production pattern used

1. Inspect local repo state and current section shape.
2. Patch local `sections/lk-collection.liquid` for code-sync only:
   - add inline SVG icon wrappers inside `.lk-cro-trust-strip__item`;
   - add compact CSS classes `.lk-cro-trust-strip__icon` and `.lk-cro-trust-strip__label`;
   - preserve 4-column mobile no-scroll grid with small icons/text.
3. Verify diff locally:
   - `git diff --check -- sections/lk-collection.liquid`
   - scan diff for secret-looking strings.
4. For production upload, do **not** upload the full local file blindly.
   - Fetch the live production asset from Shopify Admin Asset API.
   - Backup it under `backups/theme-production/<timestamp>/sections__lk-collection.liquid`.
   - Narrowly replace only the trust-strip CSS blocks and HTML block in the live string.
   - Upload the patched live string back to the verified production theme.
5. Read back the asset and verify:
   - exact SHA-256 equals target patched string;
   - `lk-cro-trust-strip__icon` exists;
   - all distinctive SVG substrings exist;
   - compact mobile CSS exists (`height: 58px`, small font/icon sizing).
6. Validate storefront visually with browser tooling on a real collection URL, e.g. `/collections/adidas-samba-jane`.

## Asset API quirk observed

A first Shopify Asset API `PUT` to `2024-10` returned HTTP 200 but immediate readback still showed the old asset (`icon_class_count: 0`). A subsequent retry using the same Admin API version and the same narrow patch returned exact readback (`icon_class_count: 7`, SHA matched target).

Treat `200` as insufficient for theme asset writes. Always read back and compare target hash/distinctive substrings. If readback is stale, retry once with the same API version and verify again before reporting success.

## Visual validation notes

Browser accessibility snapshot may not list SVGs as separate visible nodes. Use DOM inspection and/or vision:

```js
(() => {
  const strip = document.querySelector('.lk-cro-trust-strip');
  const icons = [...document.querySelectorAll('.lk-cro-trust-strip__icon')];
  return {
    icons: icons.length,
    stripText: strip?.innerText,
    stripHeight: strip?.getBoundingClientRect().height,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
  };
})()
```

Then ask vision whether the trust strip has four visible icons aligned above the labels.

## Rollback

Rollback is the backed-up live asset from `backups/theme-production/<timestamp>/sections__lk-collection.liquid`; re-upload it to the same verified production theme and read back by hash.

## Non-actions to state to Lucas

No product, price, stock, campaign, app, checkout, customer, or theme publish action was performed beyond the narrow section asset hotfix.