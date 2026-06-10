# Receipt — LK checkout social proof block deploy

Date: 2026-06-10
Agent/profile: lk-shopify
Surface: Shopify checkout app / Checkout UI Extension

## User request

Lucas selected the exact social proof copy for checkout:

```text
Compra segura na LK Sneakers
4,9/5 no Google com 411 avaliações
Loja física em São Paulo, produtos originais e atendimento humano.
```

## Approved scope

Lucas approved deploying a new checkout UI extension block named `Compra segura LK` inside the existing controlled app `lk-gift-bag-checkout`.

## Implementation

New extension added locally:

- Directory: `/opt/data/projects/lk-gift-bag-checkout-app/extensions/social-proof/`
- Extension handle: `lk-checkout-social-proof`
- Extension name: `Compra segura LK`
- Target: `purchase.checkout.block.render`
- API version: `2025-07`
- Capabilities: `api_access=false`, `network_access=false`

Code file:

- `/opt/data/projects/lk-gift-bag-checkout-app/extensions/social-proof/src/Checkout.jsx`

## Verification

Local build:

- Command: `npm run build`
- Result: success
- Build output included both:
  - `lk-gift-bag-checkout successfully built`
  - `lk-checkout-social-proof successfully built`

Deploy:

- Command: `shopify app deploy --path /opt/data/projects/lk-gift-bag-checkout-app --no-color --allow-updates --message "Add LK checkout social proof block"`
- Result: success
- Released version: `lk-gift-bag-checkout-5`
- Dashboard URL: `https://dev.shopify.com/dashboard/50805400/apps/380136325121/versions/1005773062145`

## Non-actions

- Did not remove the old `LK Social Proof` block from the Checkout Editor.
- Did not reposition checkout blocks.
- Did not create/change products, prices, stock, discounts, orders, Google reviews data, or checkout profile content beyond extension availability.

## Next manual/live step

In Checkout Editor, add app block `Compra segura LK` from the app `lk-gift-bag-checkout`, then remove/disable the old `LK Social Proof` block if replacing it. Save the published checkout profile.

## Rollback

- Remove the `Compra segura LK` block from Checkout Editor; or
- Release previous app version `lk-gift-bag-checkout-4` in Partner Dashboard if needed.
