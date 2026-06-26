# Receipt — Production — Adidas Campus 00s guide/FAQ — 2026-06-25

Approval: Lucas Telegram current turn approved production publish.

## Executed

Production theme write limited to one asset:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Source:
- Dev theme preview `155065450718`, same asset.

The code is conditionally scoped to:
- `collection.handle == 'adidas-campus'`

## Content published

Guide/FAQ for Adidas Campus 00s covering:
- authenticity/originality;
- feminino/masculino/unissex;
- colors: preto, cinza, branco, verde, rosa;
- styling / “com o que vestir”;
- value/price nuance without operational promises.

## Not changed

- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock and ordering not changed.
- GMC, campaigns, Klaviyo and checkout not changed.

## Verification

Admin/theme readback:
- Production asset matched dev source after retry.
- Conditional marker present.
- FAQPage questions in asset: 5.

Public QA:
- `https://lksneakers.com.br/collections/adidas-campus?cache=false...`: new guide present, FAQPage count 1, no Liquid error.
- `view=seo-final` route: new guide present, FAQPage count 1, no Liquid error.
- Regression checks: Adidas SL 72 and New Balance 530 did not receive Campus guide; no Liquid error.
- `www.lksneakers.com.br` cache-busted route initially served old/no-guide HTML; treat as edge/cache propagation because canonical non-www and theme readback are OK.

Evidence files:
- `production-before.liquid`
- `dev-source.liquid`
- `production-after.liquid`
- `WRITE_READBACK.json`
- `PUBLIC_QA_INITIAL.json`
- `PUBLIC_REGRESSION_QA.json`
- `ROLLBACK.md`

## Impact review

Recommended D+7/D+14 GSC check for:
- `adidas campus 00s`
- `adidas campus 00s feminino`
- `adidas campus 00s preto`
- `adidas campus 00s cinza`
- `/collections/adidas-campus`
