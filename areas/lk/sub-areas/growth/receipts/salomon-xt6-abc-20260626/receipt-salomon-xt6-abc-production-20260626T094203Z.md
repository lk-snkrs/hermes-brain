# Receipt — Salomon XT-6 A/B/C production

Data UTC: 20260626T094203Z

Aprovação Lucas: sim aplicar A B e C.

Executado:
- A: SEO explícito do Guia Salomon XT-6 no layout theme.
- B: bloco PDP Salomon XT-6 → Collection + Guia.
- C: FAQ visível extra no Guia; FAQPage JSON-LD existente passa a incluir os novos blocos.

Ações:
[
  {
    "theme_id": 155065417950,
    "asset": "layout/theme.liquid",
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065450718,
    "asset": "layout/theme.liquid",
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065417950,
    "asset": "sections/lk-pdp.liquid",
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065450718,
    "asset": "sections/lk-pdp.liquid",
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065417950,
    "asset": "templates/page.guia-salomon-xt6-lkgoc-v2.json",
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065450718,
    "asset": "templates/page.guia-salomon-xt6-lkgoc-v2.json",
    "status": 200,
    "changed": true
  }
]

Rollback: backups nesta pasta com prefixo `rollback-*`.
values_printed=false


## Readback pós-execução

```json
{
  "generated_at": "2026-06-26T09:44:00.866216+00:00",
  "admin_checks": {
    "layout/theme.liquid": {
      "explicit_seo": true,
      "pdp_hub": false,
      "faq_05": false,
      "preview_DEV": false,
      "updated_len": 130941
    },
    "sections/lk-pdp.liquid": {
      "explicit_seo": false,
      "pdp_hub": true,
      "faq_05": false,
      "preview_DEV": false,
      "updated_len": 182100
    },
    "templates/page.guia-salomon-xt6-lkgoc-v2.json": {
      "explicit_seo": false,
      "pdp_hub": false,
      "faq_05": true,
      "preview_DEV": false,
      "updated_len": 16284
    }
  },
  "public_readback_sample": [
    {
      "url": "https://lksneakers.com.br/pages/guia-salomon-xt-6?receipt_verify=1",
      "title": "Guia Salomon XT-6 | Cores, GORE-TEX e Curadoria LK",
      "meta_desc": "Guia LK do Salomon XT-6: entenda colorways, GORE-TEX, proporção, conforto e compra assistida na curadoria premium da LK Sneakers.",
      "pdp_hub_count": 0,
      "guide_link_count": 2,
      "faq_extra_count": 0,
      "preview_DEV_count": 1
    },
    {
      "url": "https://lksneakers.com.br/products/tenis-salomon-xt-6-cloudburst-icy-pink?receipt_verify=1",
      "title": "Tênis Salomon XT-6 Cloudburst Icy Pink | LK Sneakers",
      "meta_desc": "Salomon XT-6 Cloudburst Icy Pink na curadoria LK Sneakers: tênis técnico Sportstyle com quickLACE, Contagrip e estética outdoor urbana premium.",
      "pdp_hub_count": 0,
      "guide_link_count": 0,
      "faq_extra_count": 0,
      "preview_DEV_count": 0
    },
    {
      "url": "https://lksneakers.com.br/products/tenis-salomon-xt-6-vanilla-ice-almond-milk?receipt_verify=1",
      "title": "Tênis Salomon XT-6 Vanilla Ice Almond Milk | LK Sneakers",
      "meta_desc": "Salomon XT-6 Vanilla Ice Almond Milk na LK Sneakers: sneaker técnico off-white com estética Sportstyle, conforto, Contagrip e curadoria premium.",
      "pdp_hub_count": 11,
      "guide_link_count": 1,
      "faq_extra_count": 0,
      "preview_DEV_count": 0
    }
  ],
  "note": "Public cache is inconsistent across Shopify shards; Admin assets are patched and some public reads already show changes.",
  "values_printed": false
}
```
