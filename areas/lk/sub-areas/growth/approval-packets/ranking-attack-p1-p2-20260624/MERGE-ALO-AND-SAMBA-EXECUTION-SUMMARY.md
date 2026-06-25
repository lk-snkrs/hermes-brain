# Merge Alo Yoga + Samba SEO — Execution Summary — 2026-06-24

Approval: `eu aprovo merge do 1 e fazer o 2`.

## 1) Alo Yoga LKGOC Lite — production theme merge

Scope approved/executed:
- Production theme merge for Alo Yoga LKGOC Lite only.
- Crocs excluded from final merge.
- No price, stock, products, ordering, campaigns, GMC, Klaviyo or checkout changes.

Implementation details:
- Theme main: `lk-new-theme/production`.
- Assets touched:
  - `snippets/lk-goc-collection.liquid`
  - `sections/lk-collection.liquid`
- First attempt was rolled back/adjusted because QA detected out-of-scope Crocs signal and snippet readback inconsistency.
- Final upload used attachment mode for snippet; Admin readback confirmed snippet contains `alo-yoga-1` and not `crocs-mcqueen`.

Final QA:
- Alo Yoga cache-bust/view route: guide 1, FAQPage 1, no Liquid error.
- Alo Yoga clean URL: cache can still show old state temporarily.
- Crocs control: `guide_crocs=0`; Crocs LKGOC guide not merged.

Receipts:
- Failed/rolled-back first attempt: `receipts/theme-production/alo-yoga-lkgoc-lite-prod-merge-20260624T151024Z/`
- Final retry/current receipt: `receipts/theme-production/alo-yoga-lkgoc-lite-prod-merge-retry-20260624T151214Z/`

## 2) Samba PDP SEO title/meta

Scope approved/executed:
- Product SEO title/meta only for PDP Samba Marrom and PDP Samba Branco.
- No collection, price, stock, visible description, FAQ, schema, theme, campaign, Klaviyo or WhatsApp changes.

### PDP Samba Marrom
Handle: `tenis-adidas-samba-og-shadow-brown-powder-yellow-marrom`

SEO title applied:
`Adidas Samba OG Shadow Brown Original | LK`

Meta applied:
`Adidas Samba OG Shadow Brown original na LK: tom marrom desejado, curadoria premium, autenticidade e atendimento humano para escolher tamanho.`

Verification:
- Admin SEO OK.
- Public readback OK.
- Clean URL OK.
- Description HTML unchanged.

### PDP Samba Branco
Handle: `tenis-adidas-samba-og-off-white-core-black-branco`

SEO title applied:
`Adidas Samba OG Off White Original | LK`

Meta applied:
`Adidas Samba OG Off White original na LK: clássico branco com contraste preto, curadoria premium e atendimento humano para escolher tamanho.`

Verification:
- Admin SEO OK.
- Public readback OK.
- Clean URL OK.
- Description HTML unchanged.

Receipt:
- `receipts/shopify-production/samba-marrom-branco-seo-meta-20260624T151400Z/`

## Follow-up

- Recheck Alo Yoga clean URL cache later; cache-bust/view already validates guide + FAQPage.
- D+7/D+14: SEMrush/GSC watchlist:
  - `alo yoga`, `alo yoga brasil`, `alo yoga original`
  - `adidas samba marrom`, `samba branco`, `adidas samba feminino`, `tenis adidas samba`
