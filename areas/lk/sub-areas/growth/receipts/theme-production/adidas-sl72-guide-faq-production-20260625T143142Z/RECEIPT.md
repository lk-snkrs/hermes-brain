# Receipt — Production — Adidas SL 72 guide/FAQ/schema — 2026-06-25

Approval: Lucas Telegram current turn approved production publish.

## Executed

Production theme write limited to one asset:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Source:
- Dev theme preview `155065450718`, same asset.

New code is conditionally scoped to:
- `collection.handle == 'adidas-sl-72'`

Existing Adidas Campus 00s block was preserved:
- `collection.handle == 'adidas-campus'`

## Content published

Guide/FAQ/schema for Adidas SL 72 covering:
- OG vs RS;
- comfort;
- meaning/history of SL;
- feminino/styling;
- colors/use-case guidance.

## Not changed

- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock and ordering not changed.
- GMC, campaigns, Klaviyo and checkout not changed.

## Verification

Admin/theme readback:
- Production asset matched dev source after retry.
- SL72 conditional marker present.
- Campus block preserved.
- FAQPage questions in asset: 10 total across Campus + SL72.

Public QA:
- `/collections/adidas-sl-72?view=seo-final...`: new guide present, FAQPage count 1, no Liquid error.
- Canonical `/collections/adidas-sl-72?...`: initially served cached old HTML, then propagated and new guide present on retry; no Liquid error.
- Regression checks: Adidas Campus still has Campus guide; New Balance 530 did not receive SL72 guide.

Evidence files:
- `production-before.liquid`
- `dev-source.liquid`
- `production-after.liquid`
- `WRITE_READBACK.json`
- `PUBLIC_QA_FINAL.json`
- `PUBLIC_QA_PROPAGATION_RETRY.json`
- `PUBLIC_REGRESSION_QA.json` if present
- `ROLLBACK.md`

## Impact review

Recommended D+7/D+14 GSC check for:
- `adidas sl 72`
- `adidas sl 72 feminino`
- `adidas sl 72 og`
- `adidas sl 72 rs`
- `/collections/adidas-sl-72`
