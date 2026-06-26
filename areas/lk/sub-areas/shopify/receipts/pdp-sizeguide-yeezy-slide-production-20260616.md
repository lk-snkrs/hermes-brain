# Receipt — PDP size guide Yeezy Slide Production

Date: 2026-06-16
Owner: LK Shopify
Scope: approved Production promotion for one scoped theme file

## Approval

Lucas approved in chat:

> Aprovado subir a correção do guia de tamanhos do Yeezy Slide para Production, somente no arquivo sections/lk-pdp.liquid, sem mexer em produto/preço/estoque/campanhas.

## Scope executed

- Repo: `lk-snkrs/lk-new-theme`
- Base branch: `production`
- Feature branch: `fix/yeezy-slide-sizeguide-production-20260616`
- File changed: `sections/lk-pdp.liquid`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/81
- Feature commit: `41ef376d8afb`
- Merge commit: `3ec4a6314ccf`
- Production branch after merge: `3ec4a6314ccf`

## Change

Added a Yeezy Slide-specific size-guide exception:

- Declared `lk_is_yeezy_slide`.
- Detected `yeezy-slide` / `yeezy slide` before generic Yeezy rendering.
- Displayed modal brand label `Yeezy Slide`.
- Rendered copy: `Yeezy Slide costuma vestir pequeno. Recomendamos comprar um tamanho inteiro acima do seu tamanho habitual.`
- Rendered whole-BR-size-up table under `Comprar no Yeezy Slide`.

Controls preserved:

- Generic Yeezy/Boost 350 copy/table still recommends half-size up.
- Jordan 1 Mid copy/table still recommends one whole size up.
- Vomero Premium copy/table still recommends habitual size.

## Production readback

Before:

- GitHub Production SHA-12: `7d223086fbc0`
- Shopify Production SHA-12: `7d223086fbc0`
- GitHub matched Shopify before: yes
- Production had Slide fix before: no

After:

- GitHub Production SHA-12: `a3cd7e5c20a5`
- Shopify Production readback SHA-12: `a3cd7e5c20a5`
- Shopify Production matched target: yes
- Shopify Production has `lk_is_yeezy_slide`: yes
- Shopify Production has Slide copy: yes
- `values_printed=false`

## Live QA

Mobile Chromium/CDP QA, viewport `390x844`, public live URLs without `preview_theme_id`:

- `yeezy-slide-glow-green`
  - Modal opened.
  - Label/copy `Yeezy Slide` + one whole size up present.
  - Generic Boost 350 copy absent.
  - 0 Liquid errors.
  - No horizontal overflow.
- `yeezy-350-v2-salt`
  - Generic Yeezy/Boost 350 half-size-up copy present.
  - Slide copy absent.
  - 0 Liquid errors.
  - No horizontal overflow.
- `air-jordan-1-mid-wolf-grey`
  - Jordan 1 Mid copy present.
  - Slide copy absent.
  - 0 Liquid errors.
  - No horizontal overflow.
- `tenis-nike-vomero-premium-black-volt-preto`
  - Vomero Premium copy present.
  - Slide copy absent.
  - 0 Liquid errors.
  - No horizontal overflow.

## Artifacts

- Production before from GitHub: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/github_production_before_sections__lk-pdp.liquid`
- Production before from Shopify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/shopify_production_before_sections__lk-pdp.liquid`
- Production target: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/github_production_target_sections__lk-pdp.liquid`
- Scoped diff: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/production_scoped.diff`
- GitHub PR/merge result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/github_pr_merge_result.json`
- Shopify readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/shopify_production_readback_sections__lk-pdp.liquid`
- QA JSON/screenshots: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-production-20260616/assets/`

## Non-actions

No product edits, price changes, stock/availability changes, collection edits, metafield writes, GMC, Klaviyo, WhatsApp, email, campaign, checkout, discount, or broad `dev -> production` merge.

## Rollback

Recommended rollback if Lucas wants to revert:

1. Revert PR #81 / merge commit `3ec4a6314ccf` on branch `production` with a scoped PR.
2. Verify GitHub Production file returns to pre-change state/previous SHA `7d223086fbc0` for this asset.
3. Verify Shopify Production Asset API readback.
4. Re-run live QA on the same four PDPs.

## Status final

Production corrigido e validado. DEV permanece corrigido. Controls live passaram.
