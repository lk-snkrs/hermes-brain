# Receipt — Google Customer Reviews opt-in approval attempt

- timestamp UTC: `2026-06-05T19:??:??Z`
- context: Lucas approved option 1 from prior packet: Simprosys + controlled test order for Merchant ID `5297679409`.
- scope approved: configure Google Customer Reviews in Simprosys and QA with a controlled test order; no price, stock, feed, production theme, campaigns or other app changes.

## Actions attempted

1. Re-read PRD:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/prds/2026-06-05-google-customer-reviews-opt-in.md`
2. Rechecked Simprosys documentation:
   - app integration requires app-provided GCR setup/checkouts script flow;
   - verification requires test order and confirmation page popup.
3. Read-only Shopify Admin API probe:
   - shop: `lk-sneakerss.myshopify.com`
   - production theme: `lk-new-theme/production` / role `main` / id `155065417950`
   - no `snippets/gts.liquid` in production theme;
   - `layout/theme.liquid` does not contain `surveyoptin`, `apis.google.com/js/platform.js`, or GCR copy.
4. Attempted to open Shopify Admin embedded app URL for Simprosys:
   - `https://admin.shopify.com/store/lk-sneakerss/apps/google-shopping-feed`
   - result: redirected to Shopify login with `errorHint=no_cookie_session`.

## Result

No external write was executed.

The available Shopify Admin API token is not enough to access/configure the Simprosys embedded app UI or Shopify checkout Additional Scripts/thank-you configuration. The Simprosys configuration requires an authenticated Shopify Admin browser session or app-specific credentials/session.

## Blocker

- No Shopify Admin browser cookie/session for the Simprosys embedded app.
- No Simprosys-specific API credential found in Doppler.
- Controlled test order also needs an approved operational method/payment/test-order path before completing checkout.

## Rollback

No rollback needed because no write occurred.

## Next decision

Use one of these paths:

1. Lucas/Renan configures inside Shopify Admin > Apps > Simprosys using the PRD checklist, then Hermes does read-only QA from available confirmation evidence/screenshots.
2. Provide an authenticated browser/admin path/session for Hermes to operate the Simprosys UI.
3. If app UI is unavailable, open Simprosys support ticket with Merchant ID `5297679409` and the PRD evidence.
