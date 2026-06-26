# Receipt — Production cache-touch — sections/lk-collection.liquid — Adidas Gazelle canonical follow-up — 2026-06-25

Approval: Lucas approved current turn.

## Executed

Production cache-touch only:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `sections/lk-collection.liquid`

Action:
- Rewrote identical content to force recompilation/propagation.

## Readback

- Readback matched before exactly.
- `{% render 'lk-goc-guide-contract' %}` is present in the section.
- No functional change was made.

## Public QA

Canonical Gazelle remains unresolved:
- `/collections/adidas-gazelle`: no Gazelle guide, FAQPage 0, no Liquid error.
- `/collections/adidas-gazelle-feminino`: redirects to `/collections/adidas-gazelle`, no Gazelle guide, FAQPage 0, no Liquid error.

View route remains OK:
- `/collections/adidas-gazelle?view=seo-final`: Gazelle guide present, FAQPage 1, no Liquid error.

Regressions:
- Adidas Campus: guide present, FAQPage 1, no Liquid error.
- Adidas SL72: guide present, FAQPage 1, no Liquid error.
- NB530: guide present, FAQPage 1, no Liquid error.

## Interpretation

The cache-touch did not solve canonical Gazelle. Since Campus and SL72 render through the same snippet on canonical routes, the issue is specific to the Gazelle canonical route/condition/template behavior, not a sitewide snippet or section failure.

Do not make further production writes without scoped approval. Next safest investigation is to prepare a dev-only condition hardening for Gazelle using collection ID/title in addition to handle, then QA canonical preview before production.

Evidence:
- `WRITE_READBACK.json`
- `PUBLIC_QA_FINAL.json`
- `sections__lk-collection.before.liquid`
- `sections__lk-collection.after.liquid`
- `ROLLBACK.md`
