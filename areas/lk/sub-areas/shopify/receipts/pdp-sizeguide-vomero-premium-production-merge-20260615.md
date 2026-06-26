# Receipt — PDP Size Guide Nike Vomero Premium Production promotion

Date: 2026-06-15
Agent/profile: lk-shopify
Scope: Production promotion for `sections/lk-pdp.liquid`

## Approval
Lucas approved Production promotion in Telegram: `aprovado`.

## PR / GitHub
Repo: `lk-snkrs/lk-new-theme`
Base: `production`
Branch: `fix/vomero-premium-sizeguide-production-20260615`
PR: https://github.com/lk-snkrs/lk-new-theme/pull/79
PR state: merged
Merge time: `2026-06-15T20:02:01Z`
Merge commit: `0bab7d98ffcada298f87ee8549f58bb0e1f08c8c`

PR scoped files:
- `sections/lk-pdp.liquid` — 32 additions, 1 deletion

Checks:
- `git diff --check`: passed
- Static checks: passed
- GitHub PR mergeability: `MERGEABLE` / `CLEAN`
- GitHub checks: no checks reported

## Shopify readback
Production theme:
- ID: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`

DEV theme:
- ID: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`

Asset: `sections/lk-pdp.liquid`

Readback SHA12:
- Local target: `8444d3aede2f`
- Production: `8444d3aede2f`
- DEV: `8444d3aede2f`

Production readback checks passed:
- Vomero flag present.
- Vomero copy present.
- Full table header present: `BR / US M / US W / EU / CM`.
- Row `38 / 7 / 8.5 / 40 / 24.5` present.
- Row `45 / 12.5 / 14 / 47 / 29.2` present.
- Jordan 1 Mid/High rule preserved.

Backup/readback directory:
`/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/backups/shopify-production-sizeguide-vomero-premium-20260615`

## Live Production QA
Mode: mobile user-agent, live storefront, no `preview_theme_id`, 2 rounds.

Handles tested:
- `tenis-nike-vomero-premium-black-volt-preto`
- `tenis-nike-vomero-premium-sail-coconut-milk-branco`
- `tenis-nike-vomero-premium-hyper-pink-rosa`
- Control: `air-jordan-1-mid-wolf-grey`

Results:
- HTTP 200.
- Production theme seen.
- Size guide modal present.
- No Liquid errors.
- Vomero label present.
- Vomero normal-size/TTS copy present.
- Full columns present: BR, US M, US W, EU, CM.
- Rows `38 / 7 / 8.5 / 40 / 24.5` and `45 / 12.5 / 14 / 47 / 29.2` present.
- Jordan 1 Mid control preserved.

Final QA status: passed.

## Non-actions
- No product write.
- No price write.
- No stock/availability write or claim.
- No collection/GMC/Klaviyo/ads/WhatsApp/email/campaign changes.

## Rollback
Preferred rollback:
- Revert PR #79 in GitHub and let Production sync/readback, then QA live.

Asset-level rollback reference:
- Previous Production readback/backup directory: `/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/backups/shopify-production-sizeguide-vomero-premium-20260615`
