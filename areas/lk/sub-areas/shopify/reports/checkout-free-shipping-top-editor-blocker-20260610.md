# Checkout free-shipping top placement — Checkout Editor attempt

Timestamp UTC: 2026-06-10T18:24:08Z and follow-up attempt after Lucas approval.

## Approval

Lucas approved: `Aprovado ajustar o Checkout Editor/profile para posicionar o bloco de frete grátis no topo do checkout.`

## Goal

Place free-shipping microcopy at the top of checkout, not below payment/trust grid.

Target visible copy:

- `Frete grátis acima de R$499`
- `Calculado após informar o CEP.`

## Actions taken

1. Verified Shopify Admin GraphQL `CheckoutProfile` schema.
   - `CheckoutProfile` only exposed basic read fields in this API version: `id`, `name`, `isPublished`, timestamps, etc.
   - No app-block/extension placement mutation was available in Admin GraphQL.
2. Verified published checkout profile:
   - `gid://shopify/CheckoutProfile/3291709662`
   - name: `Copy of LK Sneakers configuration`
   - `isPublished=true`
3. Verified app installation read-only:
   - `lk-gift-bag-checkout` is installed on the shop.
4. Consulted Shopify docs:
   - Static targets and block targets are activated/placed using Checkout and Accounts Editor.
   - `purchase.checkout.block.render` supports `default_placement` such as `INFORMATION1`.
   - `INFORMATION1` is above contact information, first element on the Information step.
5. Prepared deployable top block:
   - `extensions/shipping-microcopy/src/Checkout.jsx` now uses `purchase.checkout.block.render`.
   - `extensions/shipping-microcopy/shopify.extension.toml` now includes `default_placement = "INFORMATION1"`.
6. Deployed app version:
   - `lk-gift-bag-checkout-16`
   - message: `Prepare free shipping block with INFORMATION1 default placement`
7. Ran live mobile checkout QA.

## QA result

Script: `/opt/data/tmp/lk-checkout-qa/mobile_shipping_microcopy_qa.js`

Output directory: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/`

Final QA:

```text
microcopyFound= False
oldLowerMicrocopyFound= False
positions= {'lkCheckout': 92, 'contato': 104, 'entrega': 199, 'freeShipping': -1, 'cep': 287, 'pagarAgora': 5806, 'google': 5818}
```

## Admin UI attempt

Tried opening Shopify Admin checkout settings with the local Chromium profile:

URL: `https://admin.shopify.com/store/lk-sneakerss/settings/checkout`

Result:

- title: `Just a moment...`
- body: `Your connection needs to be verified before you can proceed`

So Hermes could not complete the Checkout Editor UI action from this runtime due Shopify/Cloudflare verification.

## Current status

- Lower/wrong free-shipping copy: removed from checkout app source and not found in QA.
- Top free-shipping block: deployed and available in app code with `default_placement = INFORMATION1`, but not active on published checkout because Checkout Editor/profile placement was not completed.
- Blocker: Checkout Editor UI/account verification; Admin API did not expose block placement mutation.

## Manual next step for Lucas/admin

Shopify Admin:

1. Settings → Checkout.
2. Open published profile: `Copy of LK Sneakers configuration`.
3. Customize.
4. In Checkout Editor, on Information/Contato step, add app block from `lk-gift-bag-checkout`.
5. Choose block: `Frete grátis LK` / `lk-checkout-shipping-microcopy`.
6. Position it at `INFORMATION1` / above Contact, or as high as the editor allows near the top of the Information step.
7. Save the checkout profile.
8. Notify Hermes to run mobile QA again.

## Rollback

- Remove/disable the `Frete grátis LK` block from Checkout Editor if added incorrectly.
- Or revert app version to a prior version / redeploy without `default_placement` if needed.

## Non-actions

- No price/freight rule changed.
- No order/test purchase made.
- No stock/product/payment/Klaviyo/GMC/theme write.
