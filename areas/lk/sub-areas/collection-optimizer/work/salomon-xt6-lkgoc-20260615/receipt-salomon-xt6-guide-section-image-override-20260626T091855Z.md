# Receipt — Salomon XT-6 guide section image override

Data UTC: 20260626T091855Z

Patch em `sections/lk-goc-guide-v1.liquid`: override específico para `page.handle == guia-salomon-xt-6`, garantindo imagens CDN HTTP 200 mesmo se Shopify servir settings antigos em cache.

Ações:
[
  {
    "theme_id": 155065417950,
    "status": 200,
    "changed": true
  },
  {
    "theme_id": 155065450718,
    "status": 200,
    "changed": true
  }
]

Rollback: `rollback-section-guide-image-override-*20260626T091855Z.liquid`.
values_printed=false
