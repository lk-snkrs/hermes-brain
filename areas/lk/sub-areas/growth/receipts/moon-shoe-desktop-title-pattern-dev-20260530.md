# Receipt — Moon Shoe desktop hero pattern correction on dev

Date: 2026-05-30
Theme: dev `155065450718`
Asset changed: `sections/lk-collection.liquid`
Collection: `nike-x-jacquemus-moon-shoe-sp`

## Issue from Lucas screenshot
Desktop H1 inherited the 204L short-title constraint and wrapped the final token `SP` alone on a second line. That increased the banner height and visually pushed the hero/collage/product-toolbar rhythm away from the approved premium/204L pattern.

## Change applied on dev
Added an aria-scoped desktop correction for the Moon Shoe collection title inside the existing 204L pattern block:

- desktop only `min-width:990px`;
- selector scoped to `.lk-204l-coll-preview[aria-label="Contexto editorial Nike x Jacquemus Moon Shoe"]`;
- H1 set to `font-size:46px`, `max-width:min(60vw,760px)`, `width:auto`, `display:inline-block`;
- mobile branch preserved.

No production publish was done in this step.

## Shopify admin readback
- PUT status: `200`
- GET status: `200`
- dev theme asset bytes: `230019`
- dev theme asset sha256: `d0c7ae300364b6890dd3c659a76f6a12ad1e62f5b4aaab6088a0fd192e21b845`
- desktop rule present: true

## Browser verification
URL checked:
`https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065450718&lkqa=moon-desktop-dev-fix-d0c7`

Rendered desktop checks at ~1265px viewport:

- H1 text: `Nike x Jacquemus Moon Shoe SP`
- H1 line count: `1`
- H1 font-size: `46px`
- H1 max-width: `760px`
- H1 height: `46.9px`
- Collage top: `170.3px`
- Toolbar top: `619.3px`
- after-grid guide present: true
- legacy `.coll-faq`: false
- `FAQPage` JSON-LD count: `1`

Visual check confirmed:

- no orphan `SP` line;
- hero/collage reads closer to the premium/204L desktop rhythm;
- filters/toolbar are clean, aligned and without broken gap.

## Screenshot evidence
`/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_2a483dfa0e864f51a5bf5c30139df206.png`

## Rollback
Revert only the Moon Shoe desktop title block in `sections/lk-collection.liquid` around the comment:
`LK Moon Shoe — desktop title parity with 204L, avoid orphan “SP” line`
