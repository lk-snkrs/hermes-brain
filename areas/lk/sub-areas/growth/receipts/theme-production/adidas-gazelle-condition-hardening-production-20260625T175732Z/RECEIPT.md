# Receipt — Production — Adidas Gazelle condition hardening — 2026-06-25

Approval: Lucas approved scoped production publish in current turn.

## Executed

Production write limited to one asset:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Source:
- Dev theme preview `155065450718`, same asset.

Changed only Gazelle condition from handle-only to hardened condition:
- handle `adidas-gazelle`
- handle `adidas-gazelle-feminino`
- collection ID `428761874654`
- title contains `adidas gazelle`

Existing blocks preserved:
- Adidas Campus
- Adidas SL 72

## Not changed

- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock and ordering not changed.
- GMC, campaigns, Klaviyo and checkout not changed.

## Verification

Admin/theme readback:
- Production asset matched dev source after retry.
- Hardened Gazelle markers present.
- Campus and SL72 blocks preserved.

Public QA:
- First canonical checks still served old HTML briefly.
- Retry confirmed `/collections/adidas-gazelle` canonical rendered the Gazelle guide, FAQPage 1, no Liquid error.
- `/collections/adidas-gazelle-feminino` redirects to canonical; first fetch served old HTML briefly, retry confirmed Gazelle guide present, FAQPage 1, no Liquid error.
- `/collections/adidas-gazelle?view=seo-final` remains OK.
- Regression: Campus, SL72 and NB530 checked OK; no Liquid error.

Evidence:
- `WRITE_READBACK.json`
- `PUBLIC_QA_RETRY.json`
- `PUBLIC_QA_FINAL.json`
- `PUBLIC_QA_FEM_RETRY.json`
- `production-before.liquid`
- `production-after.liquid`
- `dev-source-hardened.liquid`
- `ROLLBACK.md`

## Impact review

Recommended D+7/D+14 GSC check after propagation:
- `/collections/adidas-gazelle`
- queries around `adidas gazelle feminino`, `adidas gazelle branco feminino`, `adidas gazelle prata feminino`, `gazelle indoor feminino`, `adidas gazelle original`.
