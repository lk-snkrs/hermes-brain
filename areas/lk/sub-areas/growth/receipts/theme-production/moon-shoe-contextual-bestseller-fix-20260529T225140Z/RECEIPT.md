# Moon Shoe contextual best-seller fix

Generated: 20260529T225140Z

## Scope
- Collection: `nike-x-jacquemus-moon-shoe-sp`
- Target tag: `best-seller--nike-x-jacquemus-moon-shoe-sp`
- Shopify product tag write: approved by Lucas in current turn.
- Theme production/dev hotfix: approved by Lucas in current turn.

## Results
- Products missing tag before: `6`
- Products updated: `6`
- Tag violations after readback: `0`

## Theme assets
- production `snippets/lk-product-card.liquid` changed=True readback_ok=True before=94be67348649 after=077e6737ee97
- production `sections/lk-collection.liquid` changed=True readback_ok=True before=adb00572edcc after=a8d401b75ac8
- dev `snippets/lk-product-card.liquid` changed=False readback_ok=True before=20fbeebfec2f after=20fbeebfec2f
- dev `sections/lk-collection.liquid` changed=True readback_ok=True before=631ade42e7ee after=9b5e52a50ea2

## Public QA
- Production URL tested: `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065417950&lkqa=bestseller-prod-theme-2255`
- DOM `.pc__badge--bestseller` count: `6`
- First 6 product badge HTML: all contain `Best Seller`.

## Broader audit
- Collections flagged in bounded audit: `71`
- Important checked handles:
  - `nike-x-jacquemus-moon-shoe-sp`: exact contextual tags `6/6` after fix.
  - `new-balance-204l`: exact contextual tags `0/20` in first 20; products have broader `best-seller--sneakers` only.
  - `onitsuka-tiger-todos-os-modelos`: exact contextual tags `0/20` in first 20; one product has broader `best-seller--sneakers` only.
  - `adidas-samba-jane`: exact contextual tags `0/12`; some products have broader `best-seller--ballet-core` only.
  - `lululemon`: exact contextual tags `8/20` in first 20; appears OK for contextual badge scope.
- See `broader-contextual-badge-audit.json` for samples.

## Rollback
- Product tags: use `products-tags-before.json` to restore prior tags for the 6 Moon Shoe products.
- Theme: re-upload files under `backup/production/` and/or `backup/dev/`.