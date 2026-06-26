# Theme trustbar link production hotfix — LK Sneakers (2026-05-15)

Use this reference when Lucas asks for a tiny production theme behavior fix on LK trust/benefit bars, especially turning an existing card into a link without changing layout.

## Context

Task: make the trustbar item `Loja Física / Jardins, SP` navigate to `https://lksneakers.com.br/pages/loja-fisica` on both collection pages and PDP.

Production theme verified before write:

- Theme name: `lk-new-theme/production`
- Role: `main`
- Observed ID: `155065417950`

Assets touched:

- `sections/lk-collection.liquid`
- `sections/lk-pdp.liquid`

## Safe pattern used

1. Route to LK Shopify/theme scope and inspect local repo state.
2. Create a local backup of the current repo files, but do not assume local files are safe to upload.
3. Use Doppler `lc-keys/prd` to fetch Shopify credentials inside a short-lived process; never print values.
4. Query Shopify themes and verify the exact production theme name/role before writes.
5. Fetch the live production assets with Shopify Admin Asset API and save a live rollback backup under:
   - `backups/theme-production/<timestamp>/trustbar-loja-fisica-link-live-before/sections__lk-collection.liquid`
   - `backups/theme-production/<timestamp>/trustbar-loja-fisica-link-live-before/sections__lk-pdp.liquid`
6. Patch the fetched live strings in a temporary directory, not the whole local working tree, because the repo may contain unrelated uncommitted diffs or a branch that differs from production.
7. Narrow changes only:
   - Collection: convert the final `.lk-cro-trust-strip__item` from `<span>` to `<a href="/pages/loja-fisica">` and add `text-decoration: none` to the existing item class.
   - PDP: convert the final `.lk-tg__item` from `<div>` to `<a href="/pages/loja-fisica">`.
   - Add an accessibility label like `aria-label="Ver loja física LK Sneakers em Jardins, SP"`.
8. Upload only those two patched live asset strings to the verified production theme.
9. Read back both assets and verify exact distinctive substrings:
   - `href="/pages/loja-fisica"` appears once in each asset.
   - The `aria-label` exists.
10. Validate storefront behavior:
   - Open a collection URL with a cachebuster query (e.g. `/collections/adidas-samba-jane?cachebust=<timestamp>`) because old theme HTML can be cached.
   - Confirm the accessibility snapshot exposes the trustbar item as a link.
   - Click/trigger the link and verify navigation reaches `/pages/loja-fisica`.
   - Repeat for a PDP URL with a cachebuster query.

## Verification snippets

DOM check after storefront load:

```js
(() => {
  const a = document.querySelector('a.lk-cro-trust-strip__item[href="/pages/loja-fisica"], a.lk-tg__item[href="/pages/loja-fisica"]');
  return {
    found: !!a,
    href: a && a.href,
    text: a && a.innerText,
    display: a && getComputedStyle(a).display,
    pointerEvents: a && getComputedStyle(a).pointerEvents,
    rect: a && a.getBoundingClientRect().toJSON()
  };
})()
```

Admin readback check should not print tokens; report only counts/booleans, e.g. `href_count=1`, `anchor_label=True`.

## Pitfalls

- **Do not upload local `sections/lk-collection.liquid` wholesale.** In this session the local repo already had unrelated collection sort/trustbar diffs, while the live production asset had only some of them. Uploading local would have promoted unrelated changes.
- **Shopify/theme cache can make the first plain URL look stale.** Use a cachebuster query for validation when a recent Asset API write does not immediately appear in the storefront snapshot.
- **Browser click snapshots can lag.** If `browser_click` returns success but the snapshot still shows the old page, check `location.href` or trigger `element.click()` in the browser console and then snapshot again.
- **Relative href is acceptable.** `href="/pages/loja-fisica"` resolves to the requested canonical URL on `lksneakers.com.br` while avoiding hardcoding environment hosts.

## Rollback

Rollback by uploading the backed-up live asset files from `trustbar-loja-fisica-link-live-before` to the same verified production theme, then read back by substring/hash and validate the storefront.

## Non-actions to state to Lucas

No product, price, stock, collection membership, campaign, app, checkout, customer, or theme publish action was performed beyond the narrow section asset hotfix.