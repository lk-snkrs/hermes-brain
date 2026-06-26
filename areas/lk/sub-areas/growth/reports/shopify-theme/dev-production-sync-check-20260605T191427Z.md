# Shopify theme DEV vs Production sync check

- timestamp UTC: `2026-06-05T19:11:07.009679+00:00`
- operation: read-only Shopify Admin API + read-only Git fetch compare

## Verdict
- Full theme sync: `False`
- Shopify theme assets differ: `21` common text assets differ
- Shopify only DEV assets: `25`
- Shopify only Production assets: `7`
- Git branches are divergent; see Telegram summary for commit counts.

## Shopify themes
- DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished` / updated `2026-06-05T16:05:29-03:00`
- Production: `155065417950` / `lk-new-theme/production` / role `main` / updated `2026-06-05T15:51:18-03:00`

## Shopify asset counts
- DEV assets: `457`
- Production assets: `439`
- Common assets: `432`
- Checked common text assets: `420`
- Same common text assets: `399`
- Different common text assets: `21`
- Errors: `0`

## Critical assets
- `layout/theme.liquid`: dev `2c3e37d3bbd1` / prod `b084c5b1c83c` / same `False` / yeezy dev `False` / yeezy prod `False`
- `sections/lk-pdp.liquid`: dev `bf7c3ab32206` / prod `3698f5ec5745` / same `False` / yeezy dev `False` / yeezy prod `False`
- `snippets/lk-variante-top30-visited.liquid`: dev `493429e95ac5` / prod `089cc730d730` / same `False` / yeezy dev `True` / yeezy prod `False`
- `snippets/lk-variante-top30-visited-v2.liquid`: dev `MISSING` / prod `493429e95ac5` / same `n/a` / yeezy dev `n/a` / yeezy prod `True`
- `assets/lk-variante.css`: dev `703fdabbfa7c` / prod `703fdabbfa7c` / same `True` / yeezy dev `False` / yeezy prod `False`

## Sample differences
- `assets/lk-204l-hero-fix-20260527-1545.css`: dev `073bc159b902` len `85723` / prod `44e66ba9d49f` len `9082`
- `assets/lk-collection-v2.css`: dev `5d408e3a8dae` len `10646` / prod `a2d977e45748` len `11246`
- `assets/lk-footer.js`: dev `e5032b9a599b` len `4310` / prod `06a3bb965b9c` len `7533`
- `assets/lk-product-card.css`: dev `075ff53460eb` len `12522` / prod `a8f524ea2b47` len `27443`
- `layout/theme.liquid`: dev `2c3e37d3bbd1` len `149875` / prod `b084c5b1c83c` len `90054`
- `sections/lk-collection.liquid`: dev `744d60b85b2d` len `240743` / prod `c960bd0fd2b1` len `259568`
- `sections/lk-geo-source-pages-v2.liquid`: dev `8af1ac8d8fd9` len `48522` / prod `8a3dfb1ffe50` len `55492`
- `sections/lk-moon-shoe-source-page-v3.liquid`: dev `28d5d9a302b4` len `33657` / prod `a4d6abb7ef90` len `33620`
- `sections/lk-moon-shoe-source-page-v4.liquid`: dev `f659a39b07cb` len `34683` / prod `49e77bba442c` len `34646`
- `sections/lk-moon-shoe-source-page-v5.liquid`: dev `82f6e3195123` len `40457` / prod `9cf2855c2c8e` len `40420`
- `sections/lk-moon-shoe-source-page-v6.liquid`: dev `440e488fc3c1` len `41732` / prod `1477545a9a89` len `41695`
- `sections/lk-nb204l-guide-lkgoc.liquid`: dev `2106b816edfb` len `27472` / prod `983b1ca0ea39` len `22437`
- `sections/lk-pdp.liquid`: dev `bf7c3ab32206` len `130704` / prod `3698f5ec5745` len `131376`
- `sections/lk-search.liquid`: dev `70cb4f3df56b` len `37407` / prod `261b18011b56` len `25312`
- `sections/main-page.liquid`: dev `ec4115a49639` len `678` / prod `010147619eb0` len `477`
- `snippets/lk-goc-new-balance-9060-hero-204l-clone.liquid`: dev `fa9a050f009d` len `12122` / prod `3a3e6fa3bf56` len `11781`
- `snippets/lk-moon-shoe-source-preview.liquid`: dev `6c05ddb9a1d2` len `42747` / prod `7bab49db0954` len `42710`
- `snippets/lk-samba-jane-lkgoc-v2.liquid`: dev `eb433cde261c` len `2914` / prod `c61181384c09` len `3439`
- `snippets/lk-variante-top30-visited.liquid`: dev `493429e95ac5` len `206304` / prod `089cc730d730` len `178541`
- `templates/llms-full.txt.liquid`: dev `c7f2a6d8a3ae` len `121003` / prod `d447e96f334a` len `120059`
- `templates/llms.txt.liquid`: dev `8ef2c43c89cb` len `49693` / prod `5db8a51746ce` len `48558`

## Raw local artifacts
- `/opt/data/tmp/lk_theme_dev_prod_sync_check.json`
- Git working clone: `/opt/data/tmp/lk-new-theme-sync-check`
