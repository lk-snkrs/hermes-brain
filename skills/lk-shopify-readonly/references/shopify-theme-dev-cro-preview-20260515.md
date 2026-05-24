# Shopify theme dev CRO preview workflow — LK Sneakers (2026-05-15)

Use this reference when Lucas approves a narrowly scoped LK theme/CRO preview on Shopify, especially collection/PDP tests that must stay off production.

## Scope pattern learned

Example approved scope: Adidas Samba Jane CRO Preview Pack v0, limited to:

- collection route: `/collections/adidas-samba-jane`
- PDP route: `/products/tenis-adidas-samba-jane-black-white-gum-preto`
- popup delayed/removed only on pilot routes
- compact trust strip
- collection size shortcuts
- no production publish, no product/price/stock/campaign writes

## Safe sequence

1. Confirm repository and base branch first.
   - For LK theme work, observed repo: `lk-snkrs/lk-new-theme`.
   - Start from `origin/dev`, never from production/main for preview work.
2. Clone/fetch with Doppler-stored GitHub PAT using temporary `GIT_ASKPASS`; keep remote clean (`https://github.com/lk-snkrs/lk-new-theme.git`).
3. Create a feature branch from `origin/dev`, e.g. `cro/<pilot>-preview-v0`.
4. Make Liquid/CSS/JS changes scoped by explicit handles/routes:
   - collection: `{% if collection.handle == '<handle>' %}`
   - PDP: `{% if product.handle == '<handle>' %}`
   - global layout changes should render a pilot-only snippet that self-disables outside target routes.
5. Validate locally:
   - `git diff --check`
   - basic secret scan of the diff
   - `shopify theme check` when possible, but distinguish pre-existing repo/theme warnings from new issues.
6. Commit and push branch; open PR to `dev` and record the PR URL.
7. Before uploading assets to Shopify dev theme, list themes via Admin API and verify the exact target:
   - name: `lk-new-theme/dev`
   - role: `unpublished`
   - observed dev theme ID: `155065450718`
   Refuse upload if name/role do not match.
8. Snapshot remote copies of every asset to be uploaded under a timestamped backup directory before each upload.
9. Upload only changed assets to the dev/unpublished theme via Shopify Asset API.
10. Validate with preview URLs and screenshots:
   - `https://<domain>/collections/<handle>?preview_theme_id=<theme_id>`
   - `https://<domain>/products/<handle>?preview_theme_id=<theme_id>`
   - For Lucas's PDP/CRO iterations, validate **mobile first**: open the preview, take/inspect a mobile screenshot, and self-correct if it looks cramped/ugly before reporting. Desktop review can come later unless explicitly requested.
   - Check both desktop and mobile behavior for trust bars/size shortcuts; Lucas may explicitly ask "Todos no móbile ok?" and expects the answer to be backed by preview validation, not assumption.
11. Report clearly:
   - PR URL/commit
   - theme name/id/role
   - backup path
   - preview URLs
   - what was not done: no publish, no production, no product/price/stock/campaign/customer send.

## Production promotion sequence

Use this only after Lucas explicitly approves publishing a validated dev-theme change to production (e.g. “pode jogar para o tema production”).

1. Re-confirm the exact production theme via Shopify Admin API before any write:
   - name: `lk-new-theme/production`
   - role: `main`
   - observed production theme ID: `155065417950`
   Refuse upload if name or role differs.
2. Backup the current production asset(s) under `backups/theme-production/<timestamp>/` before upload.
3. Upload only the validated asset(s) from the reviewed dev work. Do **not** publish/create themes, touch apps, products, prices, stock, checkout, campaigns, or customer sends.
4. Read the production asset back and verify by exact hash where possible. If exact-string checks fail, inspect/readback around the target block before assuming the upload failed; brittle substring checks can produce false negatives when CSS values are split across lines or are scoped differently.
5. Open the live production URL (no `preview_theme_id`) and visually validate:
   - target component appears in production;
   - dev-only preview query is not required;
   - no overlay/popup is blocking the evidence (close it before screenshot/vision if needed);
   - no obvious layout break/overflow in the affected block.
6. Git hygiene: if the production branch already contains the asset contents, do not force a redundant commit. If syncing code is needed, use a separate worktree/branch from `origin/production` and copy only the approved asset(s); avoid merging a CRO branch wholesale if it contains unrelated/big diffs.
7. Report production theme ID/name/role, backup path, live URL, validation result, and explicit non-actions.

## Implementation notes from the session

- `gh` may be absent in the runtime. Use GitHub REST API for PR creation/comments and temporary `GIT_ASKPASS` for git push.
- Doppler CLI may also be absent. If Lucas has authorized the local Doppler token file, fetch `lc-keys/prd` through the Doppler HTTP API inside the same Python process and never print token values.
- Shopify store observed through API: `lk-sneakerss.myshopify.com`; public domain observed: `lksneakers.com.br`.
- Shopify theme preview/readback may prove the asset uploaded, but visual validation still needs a mobile viewport. In a desktop browser snapshot, `getComputedStyle` can still show desktop values (e.g. trust strip `display:grid`) even when the mobile CSS is present; do not treat desktop computed styles as mobile validation.
- When using Admin Asset API readback, verify snippets by searching robust distinctive substrings; whitespace/serialization can make exact string checks falsely fail. If a check fails, inspect the readback around the target CSS before assuming upload failed.
- If a browser iframe is cross-origin or preview-bar constrained, `contentDocument` may be null; fall back to asset readback + direct mobile screenshots/browser tooling rather than guessing.
- Theme check in this repo may emit large numbers of pre-existing warnings/errors from backups or missing snippets (e.g. `lk-whatsapp-widget`). Do not claim the whole theme is clean unless those are resolved; say whether the new files/snippets introduced obvious errors.

## CRO component conventions learned

For LK collection/PDP trust bars in this visual system:

- Keep copy short, premium and operationally concrete. In the Samba Jane pilot, Lucas preferred a 4-column collection trust bar:
  1. `Originalidade garantida`
  2. `10x sem juros`
  3. `Frete Grátis acima de 499`
  4. `Loja Física Jardins SP`
- Center text robustly inside each column (`text-align: center` plus flex `align-items: center; justify-content: center`) so labels stay centered when columns wrap or heights differ.
- On mobile, Lucas may prefer **no horizontal scroll** once the first pass is visually acceptable. If he asks for "sem scroll" and then "4 em uma linha só", use a compact four-column single-row grid: `grid-template-columns: repeat(4, minmax(0, 1fr))`, small gap (≈5px), compact cards (≈58px min-height, 8px/4px padding), 14px icons, and ≈7.2px labels. Hide extra cards after the first four. Use 2×2 only if the single row becomes illegible or Lucas prefers it.
- **Do not implement a no-scroll mobile trust strip as CSS grid with wide repeated columns** (`grid-template-columns: repeat(4, minmax(116px, 1fr))` or similar); this can create page-level horizontal overflow and make CTA/description look cut off on iPhone. For no-scroll, use `repeat(4, minmax(0, 1fr))` and shrink inner spacing/copy. For scrollable, safer pattern: `.lk-trust-grid { display:flex; width:100%; max-width:100%; overflow-x:auto; overflow-y:hidden; }` plus `.lk-tg__item { flex:0 0 <card-width>; max-width:<card-width>; box-sizing:border-box; }`.
- For PDP mobile overflow fixes, add containment at the mobile breakpoint: `html, body { overflow-x:hidden; }`, `.pdp { width:100%; max-width:100vw; overflow-x:hidden; }`, `.pdp-gallery { width:100%; max-width:100vw; overflow-x:hidden; }`, `.pdp-info { width:100%; max-width:100%; box-sizing:border-box; }`, and ensure CTAs/description blocks have `width/max-width:100%` with description `overflow-wrap:anywhere`.
- If the PDP also has a trust strip, keep product-page copy consistent unless Lucas explicitly says the correction is collection-only.
- **PDP trustbar is conversion-critical.** Do not remove it as a fallback for ugly layout. If it feels awkward, fix height, spacing, order, and density instead.
- PDP mobile decision area: keep `ADICIONAR AO CARRINHO` as the dominant CTA; hide Shopify dynamic checkout / `COMPRE JÁ` on mobile if it competes with ATC; make selected size unmistakable with a filled/badged state; mark unavailable sizes with muted tile + strike-through + `Esgotado`; keep the trust signals visible, then stack the decision helpers as `Provador Virtual` → compact trustbar → `Sujeito a encomenda` → `Detalhes do produto`; align trustbar/encomenda height and spacing to the Provador Virtual card (≈52px, off-white, 1px light border, tight 4px vertical rhythm) so the trustbar does not look squeezed between taller cards; and offset floating WhatsApp/chat widgets above sticky ATC. Full session details: `references/pdp-mobile-decision-area-cro-20260515.md`.
- **Do not remove PDP trust bars just because the current layout looks ugly.** Lucas explicitly corrected this on 2026-05-15: the trust bar is conversion-critical. If it feels visually wrong, redesign it in-place (e.g. compact off-white bordered grid, first 4 signals on mobile, no horizontal overflow), preserving the trust signal rather than deleting it.

## Rollback shape

If Lucas rejects a dev preview or a change breaks the dev theme:

1. Use the timestamped backup directory created before upload.
2. Re-upload each backed-up asset to the same verified `lk-new-theme/dev` unpublished theme.
3. Delete newly introduced remote snippets/assets only if they did not exist in the backup manifest.
4. Push a reverting commit to the PR branch or close the PR if the experiment is abandoned.
5. Verify preview URLs again after rollback.

## Pitfalls

- Do not create or publish a new live theme without explicit approval.
- Do not merge the PR into `dev` if Lucas only approved a dev-theme preview and still wants to review suggestions.
- Do not treat a Shopify theme asset upload to `lk-new-theme/dev` as a production publish; but still treat it as a Shopify write requiring approval and backup.
- Do not let global layout snippets affect non-pilot pages. Gate by `request.page_type` + exact collection/product handles.
- Do not combine CRO preview with product data changes, price/stock changes, campaigns, or popup-platform configuration changes unless separately approved.
- When Lucas sends iterative visual corrections, update the same PR branch and the dev/unpublished theme, make a new backup for each upload, and add a PR comment summarizing the revision.
- Do not merge a feature/CRO branch wholesale into `production` just to publish a validated asset. In this repo, branch diffs can include unrelated generated/cache deletions and other theme changes. For production promotion, copy/upload the approved asset only and verify production readback/live URL.
- **Ugly trust bar ≠ removable trust bar.** For LK PDP/mobile CRO, if Lucas says the trust bar is ugly/awkward, first compress/reposition/redesign it while preserving the trust signal. Removal is only acceptable if Lucas explicitly says to remove the trust bar despite being told what conversion signal would be lost.
- If Shopify Asset API `PUT` returns 200 but immediate readback hash still shows the previous asset, retry with the same Admin API version used by the successful `PUT`/theme workflow (2026-05-15 session: `2024-10` produced exact readback where an earlier mixed readback appeared stale). Always verify with exact SHA-256 and a distinctive CSS substring before reporting.
- **Do not upload local `layout/theme.liquid` wholesale during production hotfixes.** The live production layout can contain app/tracker snippets or marketplace edits absent from the repo/worktree (e.g. `et-tracker`). For production, fetch the live asset, create a backup, patch the live string narrowly, upload that patched live asset, then read back and verify. Local repo patches are useful for code sync, but live hotfix upload should preserve remote-only blocks.
- **When Lucas asks to “reverter” a visual detail, restore the literal previous visual, not a new interpretation.** Example learned on PDP dynamic checkout (`COMPRE JÁ`): previous/correct style is `background: var(--white)`, `border: 1px solid var(--light-gray)`, and no added inset `box-shadow`/double-stroke. Do not keep off-white/warm-gray “premium” styling when the correction says “como era antes”. Verify with Admin asset readback, browser computed styles, and a visual check.
- **Storefront cache can be per-route/per-collection after asset upload.** Asset API readback may show the new section/layout while one collection URL still serves cached old HTML and another already serves new HTML. Verify the actual rendered HTML contains the guard/snippet on each representative handle, use cache-busting query params and a short wait, and do not report a global collection fix until at least the high-traffic handles render the updated HTML.
- **Full-page mobile screenshots can create false positives for hidden drawers.** A transformed off-canvas/bottom sheet may appear later in a full-page screenshot even when `aria-expanded=false` and the viewport is clean. For filters/drawers, validate the initial viewport screenshot plus DOM state (`aria-expanded`, overlay opacity/pointer-events, sheet transform/top) before calling it “open by default”.
- **WhatsApp/chat tooltip fixes may need a page-level guard, not only snippet CSS.** If a snippet readback is updated but storefront HTML for collections still contains the old widget CSS/JS, add a narrow guard in the rendered collection/PDP section or layout and verify the final HTML includes the guard before relying on visual QA.