# Checkout free-shipping microcopy top correction — execution/blocker

Timestamp UTC: 2026-06-10T18:24:08Z

## Approval

Lucas approved in Telegram: "Aprovado subir correção do frete grátis para o topo do checkout."

## Intended change

Move free-shipping copy away from the lower payment/trust-grid area and into the top checkout/delivery area.

Target copy:

- `Frete grátis acima de R$499`
- `Calculado após informar o CEP.`

## Local changes prepared

Project: `/opt/data/projects/lk-gift-bag-checkout-app`

Changed files:

- `extensions/social-proof/src/Checkout.jsx`
  - removed lower free-shipping microcopy from the active trust/social-proof block
  - removed the `FRETE GRÁTIS` cell from the lower trust grid to avoid duplication in the wrong area
- `extensions/shipping-microcopy/src/Checkout.jsx`
  - tried top static targets for the microcopy
- `extensions/shipping-microcopy/shopify.extension.toml`
  - tried `purchase.checkout.delivery-address.render-before`, then `purchase.checkout.contact.render-after`
- `extensions/social-proof/src/ShippingTop.jsx`
  - added a top copy module under the already-active social-proof extension
- `extensions/social-proof/shopify.extension.toml`
  - added second target `purchase.checkout.contact.render-after` pointing at `ShippingTop.jsx`

## Deploys

All builds/deploys succeeded technically:

1. `lk-gift-bag-checkout-13`
   - message: `Move free shipping microcopy to top delivery area`
   - target: `purchase.checkout.delivery-address.render-before`
2. `lk-gift-bag-checkout-14`
   - message: `Move free shipping microcopy after contact at top`
   - target: `purchase.checkout.contact.render-after`
3. `lk-gift-bag-checkout-15`
   - message: `Attach top free shipping copy to active social proof extension`
   - added top target under active social-proof extension

## QA evidence

Script: `/opt/data/tmp/lk-checkout-qa/mobile_shipping_microcopy_qa.js`

Output directory: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/`

Final QA result after version `lk-gift-bag-checkout-15`:

```text
microcopyFound= False
oldLowerMicrocopyFound= False
positions= {'lkCheckout': 92, 'contato': 104, 'entrega': 199, 'freeShipping': -1, 'cep': 287, 'pagarAgora': 5806, 'google': 5818}
```

Interpretation:

- The lower/wrong free-shipping copy was removed.
- The new top free-shipping target did not render in the live checkout.
- The checkout still shows the active lower Google/social-proof block, proving checkout app rendering is working, but the new top/static targets are not active in the published checkout profile.

## Blocker

Shopify Checkout UI Extension deploy does not guarantee visibility. For this checkout profile, the top static target did not render from deploy alone. The remaining step is likely Checkout Editor/profile activation/placement of the new app block/target, or a Shopify Checkout profile configuration layer that is not available via the current CLI deploy path.

This is an external/admin checkout write. It should not be done silently without explicit scope.

## Rollback

If Lucas wants the prior lower free-shipping mention back immediately, rollback options:

1. Re-add the `FRETE GRÁTIS` cell to `extensions/social-proof/src/Checkout.jsx`; or
2. Re-add the small lower microcopy above the trust grid; then build/deploy a new version.

If Lucas wants the correct top placement, next action is Checkout Editor/Profile placement approval and/or manual UI action.

## Non-actions

- No price/freight rule was changed.
- No product, stock, order, payment, discount, Klaviyo, GMC, or theme change was made.
- No test order was placed.
