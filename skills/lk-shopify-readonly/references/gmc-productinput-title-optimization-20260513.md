# LK GMC ProductInput title optimization — 2026-05-13

Session learning from LK OS P2B/P2B-B Google Merchant title work.

## Core guardrail

Do **not** treat Shopify product titles as wrong just because Merchant titles are duplicated across variants or shorter than 150 chars. For LK, visible Shopify titles are usually intentionally human/commercial. GMC feed/ProductInput titles can be optimized separately.

When Lucas asks whether Shopify titles should change for SEO:

- First distinguish **Shopify visible title / SEO fields** from **GMC ProductInput title**.
- Do not recommend mass Shopify title rewrites for Google Shopping issues.
- For GMC-only title work, state explicitly: `não alterar Shopify`.

## P2B critical-title pattern

A true critical issue exists when the GMC title has degraded to only a variant attribute, e.g.:

- `39`, `37`, `42`
- `M/m`, `L/g`
- `Natural`

For these rows, the safe correction is usually:

`<Shopify public product title> - Tamanho <size>`

or for a color-only variant:

`<Shopify public product title> - Cor <color>`

Use public Shopify product JSON (`/products/<handle>.js`) when possible to source the product title and variants without Shopify Admin writes. If `.js` fails and only a handle-derived fallback is available, mark confidence as `média`, not `alta`.

## Pilot pattern for adding size to sneaker titles

For sneakers/shoes, adding size to **GMC ProductInput title** may improve long-tail Shopping matching and variant clarity, e.g.:

`Tênis Nike Shox TL Black Cave Stone Preto - Tamanho 37`

But do not scale blindly. Preferred sequence:

1. Fix only broken/critical titles first (P2B).
2. Generate a pilot preview of ~100 shoes:
   - category = shoes;
   - current title has no explicit size;
   - Shopify public variant maps by variant ID or SKU;
   - numeric size confirmed;
   - resulting title <= 150 chars;
   - exclude already-fixed critical rows and known blocked rows.
3. Ask for approval inline before applying.
4. Apply only via Merchant API v1 ProductInputs, not Shopify.
5. Snapshot rollback privately and verify via Merchant API product GET.
6. Monitor GMC acceptance/warnings before scaling beyond the pilot.

## Merchant API title patch shape

For LK dataSource `10636492695`, use Merchant API v1 ProductInputs PATCH, not Content API product update.

- `dataSource=accounts/<merchant_id>/dataSources/10636492695`
- `updateMask=productAttributes.title`
- Body includes:
  - `name`
  - `offerId`
  - `contentLanguage`
  - `feedLabel`
  - `productAttributes: { title: <new title> }`

Keep title under 150 chars.

## Verification and rollback

Before write:

- Snapshot current processed product/resource privately under local rollback snapshots.
- Do not print secrets or rollback content in Telegram.

After write:

- Merchant API product GET should show `productAttributes.title` exactly equal to expected title.
- Some rows may require more propagation time; retry before declaring failure.

## Known failure: multiple feeds

Merchant API PATCH can fail with:

`Validation failed: Item uploaded through multiple feeds`

When this happens:

- Do not retry blindly.
- Continue other rows if the batch can proceed safely.
- Mark the item blocked for separate data-source/feed ownership triage.
- Do not change Shopify to work around it.

## Reporting to Lucas

In Telegram approval/reporting, include the actual preview inline, not only file paths. Recommended wording:

- scope: `somente GMC/ProductInput title`
- explicit non-actions: `não alterar Shopify`, no price/stock/image/handle/description/campaign
- result counts: patched, verified, failed/blocked
- blocked reason if any
- rollback path as audit reference only
