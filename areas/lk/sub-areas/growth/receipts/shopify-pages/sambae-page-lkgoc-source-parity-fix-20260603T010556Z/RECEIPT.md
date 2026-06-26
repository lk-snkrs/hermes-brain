# Receipt — Sambae Page LKGOC source parity fix

Data UTC: 2026-06-03T01:06:29+00:00
Página: `/pages/guia-adidas-sambae`
Page ID: `127575949534`

## Correção aplicada
- Removido layout boxed antigo `.lk-lkgoc-page`.
- Recriada page no contrato visual da 204L Gold Source/LKGOC: root `.lk-source-page--sambae`, hero `.lk-hero`, seções, tabela, style grid, bloco media, FAQ e CTA final.
- CSS de full-width usa os mesmos seletores estruturais do padrão 204L para escapar do wrapper do tema.

## QA render
```json
{
  "prod": {
    "status": 200,
    "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae?lkqa=lkgoc-source-parity-final",
    "bytes": 428352,
    "sha256": "0b4037f97f7965a614ab8dde369aaa4e8c688aa784f2594955cbe66b17ea264d",
    "markers": {
      "LK LKGOC PAGE MARKER: adidas-sambae-guide-v2": 0,
      "LK fix: Sambae page uses exact 204L/LKGOC Gold Source layout contract": 0,
      "lk-source-page--sambae": 0,
      "lk-hero": 0,
      "lk-style-grid": 0,
      "lk-media": 0,
      "lk-shop-cta": 0,
      "lk-lkgoc-page": 7,
      "404 – Não Encontrado": 0
    }
  },
  "dev": {
    "status": 200,
    "final_url": "https://lksneakers.com.br/pages/guia-adidas-sambae?lkqa=lkgoc-source-parity-final",
    "bytes": 436757,
    "sha256": "faf93c097d546ec472c70c3ea76e498aee097a4a80808c3f715a14e59854fa3f",
    "markers": {
      "LK LKGOC PAGE MARKER: adidas-sambae-guide-v2": 1,
      "LK fix: Sambae page uses exact 204L/LKGOC Gold Source layout contract": 1,
      "lk-source-page--sambae": 76,
      "lk-hero": 6,
      "lk-style-grid": 4,
      "lk-media": 19,
      "lk-shop-cta": 8,
      "lk-lkgoc-page": 0,
      "404 – Não Encontrado": 0
    }
  }
}
```

## Screenshots
```json
{
  "sambae-lkgoc-fixed-desktop.png": {
    "exists": true,
    "bytes": 1120342
  },
  "sambae-lkgoc-fixed-mobile.png": {
    "exists": true,
    "bytes": 390973
  }
}
```

## Rollback
Restaurar `page.before.json` via Shopify Admin API para o page id `127575949534`.
