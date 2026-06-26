# Moon Shoe mobile title size fix — dev theme

Date UTC: 20260529T223653Z
Theme: lk-new-theme/dev `155065450718`
Asset: `sections/lk-collection.liquid`
Scope: CSS-only, conditional for collection handle `nike-x-jacquemus-moon-shoe-sp`.

Problem: mobile H1 was clipping/vanishing on Safari because the 204L mobile title size (`44px`) is too large for the longer Moon Shoe title.

Change:
- Add collection-scoped mobile override.
- H1 uses `clamp(31px, 8.8vw, 36px)` on mobile.
- Preserve `class="coll-banner"` and `class="lk-204l-coll-preview"`.
- No production write.

Hashes:
- before: `7af3195e061bec897d674110f9bf87229cbf800ecf909db73d685cddcd83503b`
- after/readback: `631ade42e7ee741b53115e1888deda728c7614a106d9ecd15af328afb2f68cec`

Rollback: re-upload `sections__lk-collection.before.liquid` to the same dev theme asset.
