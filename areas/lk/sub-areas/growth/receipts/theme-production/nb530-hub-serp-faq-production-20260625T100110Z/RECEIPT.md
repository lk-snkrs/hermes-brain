# Receipt — Production — NB530 hub SERP FAQ — 2026-06-25

Approval: Lucas Telegram current turn: `Aprovo` after dev preview.

## Executed

Production theme write limited to one asset:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `snippets/lk-goc-new-balance-530-guide-panel.liquid`

Source:
- Dev theme preview `155065450718`, same asset.

## Content updated

Guide/FAQ now covers SERP intent captured via DataForSEO:
- `new balance 530 feminino`
- `new balance 530 branco/prata/cinza/bege`
- “O New Balance 530 é de corrida ou casual?”
- “O New Balance 530 feminino é casual?”
- “Qual é melhor: New Balance 530, 9060 ou 740?”
- autenticidade/originalidade

## Not changed

- No collection SEO/title/meta change.
- No visible collection description write.
- No product/price/stock/order changes.
- No GMC, campaigns, Klaviyo or checkout changes.

## Verification

Admin/theme readback:
- Production asset readback matched updated dev source after retry.
- New H2 present: `New Balance 530: running retrô, leveza e escolha assistida`.
- Old H2 absent in asset.
- FAQ schema question count: 6.

Public QA:
- Cache-busted production collection URL: OK.
- `Liquid error`: false.
- New H2/FAQ present.
- FAQPage count: 1.
- Plain URL via fetch initially returned cached old copy; cache-busted route confirmed update. Treat as cache propagation, not failed write.

Evidence files:
- `production-before.liquid`
- `dev-source.liquid`
- `production-after-final.liquid`
- `WRITE_READBACK.json`
- `READBACK_RETRY.json`
- `PUBLIC_QA_INITIAL.json`
- `ROLLBACK.md`

## Impact review

Recommended D+7/D+14 check in GSC for:
- `new balance 530`
- `new balance 530 feminino`
- `tenis new balance 530`
- `new balance 530 branco`
- page `/collections/new-balance-530`
