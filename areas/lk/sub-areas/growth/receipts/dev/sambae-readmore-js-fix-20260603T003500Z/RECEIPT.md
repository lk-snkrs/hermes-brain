# Receipt — Sambae DEV read-more JS fix

Data UTC: 2026-06-03T00:13:35Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Causa
O JS do hero tinha erro de sintaxe da migração dual-class:
`ev.(target.classList.contains(...))`.

Isso fazia o script inteiro quebrar e o listener do botão **Ler mais** não era registrado.

## Correção
Corrigido para `ev.target.classList.contains(...)` nos assets DEV afetados.

## QA final
```json
{
  "assets": {
    "snippets/lk-sambae-204l-hero.liquid": {
      "bytes": 5104,
      "bad_count": 0,
      "good_count": 1,
      "open204LReveal": 3
    },
    "sections/lk-collection.liquid": {
      "bytes": 257217,
      "bad_count": 0,
      "good_count": 4,
      "open204LReveal": 12
    }
  },
  "render": {
    "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718&qa=readmore-fixed-final",
    "status": 200,
    "final_url": "https://lksneakers.com.br/collections/adidas-sambae?qa=readmore-fixed-final",
    "bytes": 562917,
    "counts": {
      "ev.(target": 0,
      "ev.target.classList.contains": 2,
      "lk-lkgoc-read-more": 2,
      "lk-204l-read-more": 5,
      "open204LReveal": 3,
      "if (readMore) readMore.addEventListener": 1,
      "lk-lkgoc-collage": 2,
      "lk-lkgoc-card--large": 2
    }
  }
}
```

## Rollback
Reaplicar os arquivos `.before.liquid` deste diretório nos respectivos assets DEV.
