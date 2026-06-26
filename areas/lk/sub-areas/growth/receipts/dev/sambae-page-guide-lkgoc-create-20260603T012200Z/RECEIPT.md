# Receipt — Create Adidas Sambae page guide using LKGOC

Data UTC: 2026-06-03T00:55:14Z
Pedido: criar link page do guia Sambae usando LKGOC no dev.

## Ação
- Shopify page `guia-adidas-sambae`: `created`
- Page title: `Guia Adidas Sambae: plataforma gum, proporção fashion e como escolher`
- Page published_at: `2026-06-02T21:55:10-03:00`
- DEV snippet CTA atualizado para `/pages/guia-adidas-sambae`: `True`

## Observação de escopo
A page object do Shopify precisa existir para o link `/pages/guia-adidas-sambae` responder 200. Ela foi criada/publicada; o link DEV usa `preview_theme_id=155065450718`.
Tema production não foi alterado.

## QA
```json
{
  "action": "created",
  "page_id": 127575949534,
  "page_handle": "guia-adidas-sambae",
  "page_published_at": "2026-06-02T21:55:10-03:00",
  "snippet_cta_changed": true,
  "render": {
    "page_dev": {
      "url": "https://lksneakers.com.br/pages/guia-adidas-sambae?preview_theme_id=155065450718",
      "status": 200,
      "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae",
      "bytes": 426521,
      "counts": {
        "lk-lkgoc-page--adidas-sambae": 1,
        "GUIA LK · ADIDAS SAMBAE": 4,
        "Adidas Sambae: plataforma gum": 9,
        "href=\"/pages/guia-adidas-sambae\"": 0,
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 0,
        "404 – Não Encontrado": 0,
        "FAQPage": 1
      }
    },
    "page_plain": {
      "url": "https://lksneakers.com.br/pages/guia-adidas-sambae",
      "status": 200,
      "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae",
      "bytes": 428352,
      "counts": {
        "lk-lkgoc-page--adidas-sambae": 1,
        "GUIA LK · ADIDAS SAMBAE": 4,
        "Adidas Sambae: plataforma gum": 8,
        "href=\"/pages/guia-adidas-sambae\"": 0,
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 0,
        "404 – Não Encontrado": 0,
        "FAQPage": 1
      }
    },
    "collection_dev": {
      "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718&qa=page-link-created",
      "status": 200,
      "final_url": "https://lksneakers.com.br/collections/adidas-sambae?qa=page-link-created",
      "bytes": 565100,
      "counts": {
        "lk-lkgoc-page--adidas-sambae": 0,
        "GUIA LK · ADIDAS SAMBAE": 0,
        "Adidas Sambae: plataforma gum": 1,
        "href=\"/pages/guia-adidas-sambae\"": 1,
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 0,
        "404 – Não Encontrado": 0,
        "FAQPage": 1
      }
    }
  },
  "production_theme_changed": false,
  "note": "Shopify page object is public/published so the page URL exists; dev link uses preview_theme_id."
}
```

## Rollback
- Se precisar remover a page: deletar/ocultar page id `127575949534`.
- Reaplicar `snippet-guide.before.liquid` no asset `snippets/lk-sambae-204l-guide.liquid` do tema DEV para voltar o CTA ao anchor anterior.
