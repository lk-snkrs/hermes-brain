# Receipt — Sambae page layout fix

Data UTC: 2026-06-03T00:58:55Z
Page: `guia-adidas-sambae`
Produção theme alterado: **não**. Page body atualizada para corrigir layout.

## Correção
- Escape do wrapper Shopify `.page-width.section-spacing` para a page LKGOC.
- Hero full-bleed com `width:100vw` e margens `calc(50% - 50vw)`.
- H1 padrão da page oculto para evitar duplicidade.

## QA final render
```json
{
  "url": "https://lksneakers.com.br/pages/guia-adidas-sambae?preview_theme_id=155065450718&qa=layout-fixed-final",
  "status": 200,
  "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae?qa=layout-fixed-final",
  "bytes": 427439,
  "counts": {
    "LK fix: let LKGOC guide escape": 1,
    "body:has(.lk-lkgoc-page--adidas-sambae)": 6,
    "lk-lkgoc-hero{width:100vw": 1,
    "lk-lkgoc-page--adidas-sambae": 7,
    "404 – Não Encontrado": 0
  },
  "screenshots": {
    "page-layout-fixed-desktop.png": {
      "exists": true,
      "bytes": 715826
    },
    "page-layout-fixed-mobile.png": {
      "exists": true,
      "bytes": 390559
    }
  }
}
```

## Rollback
Reaplicar `page.before.html` no body da page id `127575949534`.
