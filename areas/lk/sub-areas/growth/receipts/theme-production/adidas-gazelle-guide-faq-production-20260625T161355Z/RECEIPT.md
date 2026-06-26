# Receipt — Production — Adidas Gazelle guide/FAQ/schema — 2026-06-25

Approval: Lucas Telegram current turn approved production publish with scoped context from prior message (`Aprovo publicar`).

## Executed

Production theme write limited to one asset:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Source:
- Dev theme preview `155065450718`, same asset.

New code is conditionally scoped to:
- `collection.handle == 'adidas-gazelle'`

Existing blocks preserved:
- `collection.handle == 'adidas-campus'`
- `collection.handle == 'adidas-sl-72'`

## Content published in asset

Guide/FAQ/schema for Adidas Gazelle covering:
- Adidas Gazelle feminino;
- Gazelle Indoor / OG / Bold;
- Gazelle vs Samba;
- colors: branco, prata, rosa, verde, bege/marrom;
- comfort/fit;
- authenticity.

## Not changed

- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock and ordering not changed.
- GMC, campaigns, Klaviyo and checkout not changed.

## Verification

Admin/theme readback:
- Production asset matched dev source after retry.
- Gazelle conditional marker present.
- Campus and SL72 blocks preserved.
- FAQPage questions in asset: 15 total across Campus + SL72 + Gazelle.

Public QA:
- `/collections/adidas-gazelle?view=seo-final...`: new guide present, FAQPage count 1, no Liquid error.
- `/collections/adidas-gazelle-feminino?view=seo-final...`: new guide present, FAQPage count 1, no Liquid error.
- Canonical `/collections/adidas-gazelle?...`: still served old/no-guide HTML during repeated QA attempts; likely cache/route/template propagation issue. Do not report canonical final OK until later recheck confirms.
- Regression checks: Campus and SL72 still show their own guides; New Balance 530 did not receive Gazelle guide.

Evidence files:
- `production-before.liquid`
- `dev-source.liquid`
- `production-after.liquid`
- `WRITE_READBACK.json`
- `PUBLIC_QA_FINAL.json`
- `PUBLIC_QA_PROPAGATION_RETRY.json`
- `PUBLIC_QA_LATE_RETRY.json`
- `ROLLBACK.md`

## Required follow-up

Recheck canonical route later:
- `/collections/adidas-gazelle`
- `/collections/adidas-gazelle-feminino`

If canonical remains old while `view=seo-final` and Admin readback are OK, investigate template/cache behavior before any further Gazelle write.

## Impact review

Recommended D+7/D+14 GSC check only after canonical public route confirms the block is visible:
- `adidas gazelle feminino`
- `adidas gazelle feminino branco`
- `adidas gazelle feminino prata`
- `adidas gazelle indoor feminino`
- `/collections/adidas-gazelle`
