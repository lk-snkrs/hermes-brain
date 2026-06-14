# Footer newsletter copy — GitHub dev receipt

Date: 2026-06-13 16:06 UTC
Profile: lk-shopify
Request: change footer phrase from `Less noise, more identity.` to `O que é raro, merece ser encontrado.`

## Change

- PR: https://github.com/lk-snkrs/lk-new-theme/pull/73
- Target branch: `dev`
- Merge commit: `3de4db1fa359ad2fb585c0a8aa3ae8f423995a5e`
- Files changed:
  - `sections/footer-group.json`
  - `sections/lk-footer.liquid`

## Summary

Updated the active footer newsletter title setting and the footer section defaults to:

`O que é raro, merece ser encontrado.`

## Verification

- `git diff --check` passed before PR.
- `sections/footer-group.json` parsed successfully after stripping Shopify's optional header comment.
- PR file list was scoped to the two active footer files.
- `origin/dev` readback:
  - `sections/footer-group.json`: new phrase count `1`, old phrase count `0`.
  - `sections/lk-footer.liquid`: new phrase count `2`, old phrase count `0`.

## Guardrails

- GitHub `dev` branch only.
- No Shopify theme upload, theme publication, or production branch merge was performed in this step.
- Production/live storefront promotion remains blocked until Lucas explicitly approves the scoped production step.

## Rollback

- Revert PR #73 / merge commit `3de4db1fa359ad2fb585c0a8aa3ae8f423995a5e` on `dev`, or restore the previous footer title in `sections/footer-group.json` and `sections/lk-footer.liquid`.
