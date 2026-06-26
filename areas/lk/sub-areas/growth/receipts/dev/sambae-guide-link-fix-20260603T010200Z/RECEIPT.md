# Receipt — Sambae DEV guide link fix

Data UTC: 2026-06-03T00:17:25Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Problema
`/pages/guia-adidas-sambae` não existe no Shopify e retorna 404.

## Correção DEV
CTA do guia Sambae alterado de:
`/pages/guia-adidas-sambae`
para:
`/collections/adidas-sambae#lk-guia-adidas-sambae`

## QA final
```json
{
  "readback": {
    "theme_id": "155065450718",
    "production_changed": false,
    "readback_old_count": 0,
    "readback_new_count": 1,
    "readback_bytes": 6915
  },
  "render": {
    "old_page": {
      "url": "https://lksneakers.com.br/pages/guia-adidas-sambae?preview_theme_id=155065450718",
      "status": 404,
      "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae",
      "bytes": 433245,
      "counts": {
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 0,
        "href=\"/pages/guia-adidas-sambae\"": 0,
        "lk-guia-adidas-sambae": 0,
        "404 – Não Encontrado": 3
      }
    },
    "new_anchor": {
      "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718#lk-guia-adidas-sambae",
      "status": 200,
      "final_url": "https://lksneakers.com.br/collections/adidas-sambae#lk-guia-adidas-sambae",
      "bytes": 562916,
      "counts": {
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 1,
        "href=\"/pages/guia-adidas-sambae\"": 0,
        "lk-guia-adidas-sambae": 28,
        "404 – Não Encontrado": 0
      }
    },
    "collection_render": {
      "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718&qa=guide-link-fix-final",
      "status": 200,
      "final_url": "https://lksneakers.com.br/collections/adidas-sambae?qa=guide-link-fix-final",
      "bytes": 562916,
      "counts": {
        "href=\"/collections/adidas-sambae#lk-guia-adidas-sambae\"": 1,
        "href=\"/pages/guia-adidas-sambae\"": 0,
        "lk-guia-adidas-sambae": 28,
        "404 – Não Encontrado": 0
      }
    }
  }
}
```

## Rollback
Reaplicar `guide.before.liquid` em `snippets/lk-sambae-204l-guide.liquid` do tema DEV.
