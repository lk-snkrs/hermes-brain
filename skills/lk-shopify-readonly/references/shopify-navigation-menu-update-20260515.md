# LK Shopify navigation/menu update — 2026-05-15

## Context

Lucas asked to add the collection `On Running x Loewe` to the LK menubar/menu:

- URL: `https://lksneakers.com.br/collections/loewe-x-on-running`
- Desired label: `On Running x Loewe`

This is a Shopify Admin navigation write. The user's direct request in chat acted as the narrow approval for this exact menu/link update only.

## What worked

1. Fetch Shopify credentials from Doppler without printing values. If Doppler CLI is unavailable, use Doppler HTTP API with the local token file and keep secrets in-process only.
2. Query all Shopify menus first, not just `main-menu`.
3. Relevant LK menus found:
   - `main-menu` / `Mega Menu` — older/non-live-ish menu; not enough for current storefront nav.
   - `mega-menu-c-pia-1` / `Mega Menu (PC)` — current desktop header menu.
   - `mega-menu-mobile` / `Mega Menu (MOBILE)` — current mobile drawer/header menu.
   - `rodape-sneakers` already had `Loewe x On Running` in the footer.
4. Use Admin GraphQL `menuUpdate` with full `items` tree from the existing menu, preserving all children.
5. Use the collection resource ID when available (`type: COLLECTION`, `resourceId`) instead of a raw HTTP link.
6. Update both `mega-menu-c-pia-1` and `mega-menu-mobile` under the top-level `Sneakers` item.
7. If mobile already contains a broader/incorrect label like `On Running` pointing to `/collections/loewe-x-on-running`, normalize it to `On Running x Loewe` rather than adding a duplicate.
8. Verify by re-querying the menus after mutation and checking the direct child under `Sneakers`.

## Pitfalls discovered

- Do **not** assume `main-menu` is the storefront header menu. Updating only `main-menu` can produce a verified Admin write that does not affect the current live PC/mobile header.
- The live homepage HTML may only show footer links for this collection, not header menu links, because header megamenu content may be rendered/loaded differently or cached. Admin menu readback is the primary verification for the navigation config; browser/HTML checks are secondary.
- Use relative URLs (`/collections/loewe-x-on-running`) or collection resource links for internal menu items; avoid leaving an external-looking full HTTP link when a collection resource exists.
- Always backup the full menu JSON before `menuUpdate`; rollback is re-applying the backed-up full `items` tree to the same menu ID/handle.

## Recommended future workflow

1. Confirm exact label + URL from Lucas's message.
2. Query all menus and identify PC/mobile live handles.
3. Save a timestamped JSON backup of targeted menus under a non-secret reports/audit directory.
4. Build full `MenuItemUpdateInput` trees from existing menu items, preserving nested children.
5. Apply only the narrow requested change to both PC and mobile menus.
6. Re-query and verify:
   - `mega-menu-c-pia-1` → `Sneakers` child has target label and URL.
   - `mega-menu-mobile` → `Sneakers` child has target label and URL.
   - No accidental duplicate top-level item in `main-menu` unless specifically requested.
7. Report concise completion and audit path.
