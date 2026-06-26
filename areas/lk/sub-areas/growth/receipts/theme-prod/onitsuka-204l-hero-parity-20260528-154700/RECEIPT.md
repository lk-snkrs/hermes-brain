# Receipt — Onitsuka 204L hero parity production hotfix

Date: 2026-05-28
Theme: production `155065417950`
Asset: `layout/theme.liquid`
Scope: Onitsuka Tiger Mexico 66 collection hero/collage parity with New Balance 204L.

## Approved by Lucas
Lucas approved production theme write in the current turn.

## Change
Added a scoped desktop-only rule inside `#lk-204l-final-desktop-override`:

```css
html body:has(.lk-next-coll-preview--onitsuka-tiger-mexico-66) .lk-next-coll-preview--onitsuka-tiger-mexico-66{padding-top:2px!important;}
```

Purpose: normalize Onitsuka pre-transform section geometry so the existing `translateY(-123px)` starts from the same effective baseline as the 204L mold.

## Backup / rollback
- Backup before write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/onitsuka-204l-hero-parity-20260528-154700/theme.liquid.before`
- After snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/onitsuka-204l-hero-parity-20260528-154700/theme.liquid.after`
- JSON receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-prod/onitsuka-204l-hero-parity-20260528-154700/receipt.json`

Rollback: restore `theme.liquid.before` to production theme asset `layout/theme.liquid`.

## Verification
Browser/public storefront after cache-busted JS navigation:

- Rule present in rendered HTML: yes.
- H1 font: `52px`.
- H1 display: `inline-block`.
- H1 background: transparent.
- Breadcrumb top: `140px`.
- Collage top: `140.03px`.
- Delta collage vs breadcrumb: `0.03px`.
- Collage transform: `matrix(..., -123)` / `translateY(-123px)`.
- Preview padding-top: `2px`.
- Inner grid top: `263.03px`.
- Collage height: `390px`.
- After-grid guide card columns: `438.844px 558.531px`.
- FAQ grid-column: `2 / 3`.
- FAQ grid-row: `1 / span 2`.
- FAQ align-self: `start`.
- FAQ delta vs left title: `0px`.

Screenshot captured:
`/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_9c533d46d5964f3391febc144aa0b308.png`

## Documentation updates completed
- `PADRAO-GUIAS-EDITORIAIS-LK.md`: separated 204L collection mold from Moon Shoe guide/source mold.
- `templates/brief-guia-editorial-colecao-lk.md`: added 204L collection checklist.
- Skill `lk-collection-patterns`: patched 204L hero parity reference to require rendered pre-transform geometry checks, not only `translateY`.
