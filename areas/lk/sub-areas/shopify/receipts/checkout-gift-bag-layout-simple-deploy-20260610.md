# Receipt — Checkout gift bag layout simplification

Date: 2026-06-10
Agent/profile: lk-shopify
Surface: Shopify checkout app / Checkout UI Extension

## User issue

Lucas reported that the gift bag checkout block layout looked different from the native checkout pattern.

## Approved scope

Lucas approved: deploy of the simple layout version for `lk-gift-bag-checkout`.

## Change deployed

Updated local extension source:

- File: `/opt/data/projects/lk-gift-bag-checkout-app/extensions/gift-bag/src/Checkout.jsx`
- Removed helper/subdued text below the checkbox.
- Removed `BlockStack` wrapper and `Text` import.
- Kept attribute behavior unchanged:
  - key: `lk_gift_bag`
  - yes value: `yes`
  - no value: `no`
- Changed visible checkbox copy to: `Sacola de presente`

## Verification

Local build before deploy:

- Command: `npm run build`
- Result: success
- Output included: `lk-gift-bag-checkout built!`

Deploy:

- Command: `shopify app deploy --path /opt/data/projects/lk-gift-bag-checkout-app --no-color --allow-updates --message "Simplify gift bag checkout block layout"`
- Result: success
- Released version: `lk-gift-bag-checkout-3`
- Dashboard URL: `https://dev.shopify.com/dashboard/50805400/apps/380136325121/versions/1005752090625`

Readback:

- Command: `shopify app versions list --path /opt/data/projects/lk-gift-bag-checkout-app --no-color`
- Active version: `lk-gift-bag-checkout-3`

## Non-actions

- No product created.
- No price/stock/availability changed.
- No test order created.
- No checkout profile re-positioning performed after this deploy.

## Rollback

Rollback by releasing previous app version `lk-gift-bag-checkout-2` in the Partner Dashboard, or redeploying a source version with the previous helper text/layout.

## Follow-up QA

Lucas should refresh/reopen Checkout Editor or a real checkout session and verify the block now renders closer to native checkout style. The blue outline/label shown in Checkout Editor can be editor selection UI and may not appear in customer checkout.
