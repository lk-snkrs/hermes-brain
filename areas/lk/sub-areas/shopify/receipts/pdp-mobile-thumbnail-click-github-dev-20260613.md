# PDP mobile thumbnail click — GitHub dev receipt

Date: 2026-06-13 11:15 UTC
Profile: lk-shopify
Scope approved by Lucas: subir no GitHub dev

## Change

- File: `sections/lk-pdp.liquid`
- Branch: `fix/pdp-mobile-thumbnail-click`
- Base: `origin/dev`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/69
- Merge target: `dev`
- Merge commit: `fc02a9269dabbadf9606d9b1aa2c2bac501f2426`

## Summary

PDP mobile thumbnail clicks now sync the mobile swipe track (`#pdp-track`) in addition to the desktop main image. The 360 thumbnail path also scrolls the mobile gallery to the 360 slide.

## Verification

- `git diff --check origin/dev...HEAD` passed before push.
- PR file list contained only `sections/lk-pdp.liquid`.
- PR state readback: `MERGED`.
- `origin/dev` readback includes `syncMobileGallery` markers in `sections/lk-pdp.liquid`.

## Guardrails

- GitHub dev only.
- No Shopify theme upload, publication, production merge, or external storefront write was performed in this step.
- Production promotion remains blocked until Lucas gives explicit scoped approval.

## Rollback

- Revert PR #69 / merge commit `fc02a9269dabbadf9606d9b1aa2c2bac501f2426` on `dev`, or apply the reverse patch for the `syncMobileGallery` change in `sections/lk-pdp.liquid`.
