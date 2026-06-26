# Approval packet — Promote Yeezy Slide size-guide fix to Production

Date: 2026-06-16
Owner: LK Shopify
Scope requested: scoped Production promotion for one reviewed DEV theme change

## Current status

DEV/unpublished theme is fixed and QA'd.

- DEV theme: `lk-new-theme/dev`
- DEV theme ID: `155065450718`
- DEV role: `unpublished`
- DEV asset: `sections/lk-pdp.liquid`
- DEV before SHA-12: `578d423d3f13`
- DEV target/readback SHA-12: `834b18e897f9`
- DEV readback matched target: yes

Production remains unchanged.

- Production theme: `lk-new-theme/production`
- Production theme ID: `155065417950`
- Production role: `main`
- Production current SHA-12: `7d223086fbc0`
- Production has Yeezy Slide fix: no

## Proposed Production change

Promote only the reviewed scoped change from DEV to Production:

- File: `sections/lk-pdp.liquid`
- Add `lk_is_yeezy_slide` detection before generic Yeezy rendering.
- Render `Yeezy Slide` as its own size-guide label.
- Use whole-size-up recommendation for Yeezy Slide:
  - Copy: `Yeezy Slide costuma vestir pequeno. Recomendamos comprar um tamanho inteiro acima do seu tamanho habitual.`
  - Rows: habitual BR size maps to next whole BR size.
- Preserve generic Yeezy/Boost 350 half-size-up copy/table.
- Preserve Jordan 1 Mid and Vomero Premium controls.

## Execution path if approved

Because Production theme writes require explicit approval and normal LK theme governance avoids broad DEV-to-Production drift, the safe path is:

1. Create/reuse a scoped production branch from `origin/production`.
2. Apply only the reviewed `sections/lk-pdp.liquid` Yeezy Slide hunk.
3. Run local scope checks:
   - changed files limited to `sections/lk-pdp.liquid`
   - markers present: `lk_is_yeezy_slide`, `Yeezy Slide costuma vestir pequeno`, `Comprar no Yeezy Slide`
   - controls present: generic Yeezy 350 copy, Jordan Mid copy, Vomero Premium copy
4. Open/merge scoped PR into `production` if GitHub path is available.
5. Verify Shopify Production Asset API readback.
6. If Shopify GitHub sync does not update the live theme after merge, stop and ask before any direct live Asset API upload unless Lucas explicitly approves that fallback.
7. Public live QA without `preview_theme_id`:
   - `yeezy-slide-glow-green`: Slide copy +1 size, generic 350 copy absent
   - `yeezy-350-v2-salt`: generic 350 copy present, Slide copy absent
   - `air-jordan-1-mid-wolf-grey`: Jordan Mid copy preserved
   - `tenis-nike-vomero-premium-black-volt-preto`: Vomero Premium copy preserved
   - 0 Liquid errors, no horizontal overflow in mobile browser QA
8. Save Production receipt.

## Non-actions

This approval would not authorize:

- product edits
- price/stock/availability changes
- collection edits
- metafield writes
- GMC/Klaviyo/WhatsApp/email/campaign changes
- checkout/discount changes
- broad `dev → production` merge
- direct emergency live-theme upload unless separately stated

## Risk

Low functional risk: copy/table branch inside existing size-guide modal.

Main operational risk: Production theme governance. Avoid broad DEV drift; promote only the reviewed hunk.

## Rollback

Rollback if live QA fails:

1. Revert the scoped production commit/PR for `sections/lk-pdp.liquid`, or restore Production asset to previous SHA/state `7d223086fbc0`.
2. Verify Shopify Production readback.
3. Re-run live QA on the four PDPs.

## Explicit approval wording needed

To authorize the Production promotion, Lucas should reply exactly or clearly with:

`Aprovado subir a correção do guia de tamanhos do Yeezy Slide para Production, somente no arquivo sections/lk-pdp.liquid, sem mexer em produto/preço/estoque/campanhas.`

Short version acceptable if unambiguous:

`Aprovado Production Yeezy Slide size guide, escopo sections/lk-pdp.liquid.`
