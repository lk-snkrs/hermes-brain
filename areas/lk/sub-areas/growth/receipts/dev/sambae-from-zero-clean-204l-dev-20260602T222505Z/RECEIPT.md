# Receipt — Sambae DEV from zero clean 204L-style

Data UTC: 2026-06-02T22:25:11Z
Tema DEV: 155065450718
Produção: não alterada.

## Implementação limpa
- Snippet hero: `snippets/lk-sambae-204l-hero.liquid`
- Snippet guia pós-grid: `snippets/lk-sambae-204l-guide.liquid`
- Section só recebe dois renders pequenos e explícitos.
- Guia inserido imediatamente antes de `Mobile Filter Sheet`, ou seja, depois do grid/paginação de produtos.

## QA asset
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "section_bytes": 254154,
  "under_256kb": true,
  "hero_render_count": 1,
  "guide_render_count": 1,
  "guide_before_mobile_filter": true,
  "hero_after_204l_branch_area": true,
  "old_wrong_refs": 0,
  "hero_snippet_has_readmore_toggle": true,
  "hero_snippet_uses_204l_class": true,
  "guide_snippet_has_postgrid_id": true,
  "guide_snippet_has_card": true,
  "guide_snippet_has_schema": true
}
```

## QA render com cookie de preview Shopify
```json
{
  "len": 564036,
  "hero": 6,
  "guide": 7,
  "card": 1,
  "read_more": 7,
  "ler_menos_js": 2,
  "cookies": "Z7jMxnqYM_EYh45nrJgTsRGxtPOME5B2VYJitl4Nxnx0CNDvmW4POIF4GVc7dKoJC-8G3vRSeMdYFh8V3Wt9Qq34bygN-WjrYGerYOTlQ3fqx1GeK70MVL6jnHDJUiNU6P3YqKgjjWSl__ssqXFbecLVi1oqWWcMalTMgNQzmnzipmxksVT1EftBCpxxgMqYNYhdN8qRUJTcgxN3CibPGP_uiGglZwv9QTmzUKhFxT8aZqQh5R9wPTXgmbo5br9z5F__fjZGZoQDv3Xf2qDnwvDhGLRLbCCzYaQPgFZQudZjkRKonulZB3VkmWYzLZjHQ6NVTMPhdh7hk:\nlksneakers.com.br\tFALSE\t/\tFALSE\t1811975208\tlocalization\tBR\n.lksneakers.com.br\tTRUE\t/\tFALSE\t1811996808\t_shopify_y\t71c07445-757d-4d0a-96c5-89c069e287c0\n.lksneakers.com.br\tTRUE\t/\tFALSE\t1780441008\t_shopify_s\t5a9430f2-8b8e-4768-b3fd-6f1f1d4b5b4e\n#HttpOnly_lksneakers.com.br\tFALSE\t/\tTRUE\t1811975208\t_shopify_analytics\t:AZ6KclBtAAEAovWW-p-1GMUxcupKr7R3xLxT-GpTnYCwyEs7RqA9i8cUgVNdxFnvexPrrJ8QY1L0qunFZEywFBOHO-bvn46DqcRUPwFRacnJui3NCST2cvfcXM0hv5aqUFLTn-8VYNtR-XlN:\n#HttpOnly_lksneakers.com.br\tFALSE\t/\tTRUE\t1811975208\t_shopify_marketing\t:AZ6KclBtAAEAVIjgs_sROCZoO7CK9bjaioCZixyFCL7rU54Wq-TC3xXrSoYW0aG8M1_7lvFQWjp6HgmVOYtYNqpII2y5jQNoolxtalIvMuZxWD02e08a8rtYiyJaXPaBSSTj:\n"
}
```

## QA visual screenshots
```json
{
  "sambae-dev-clean-desktop.png": {
    "exists": true,
    "bytes": 870033
  },
  "sambae-dev-clean-mobile.png": {
    "exists": true,
    "bytes": 168086
  },
  "cookie_html_markers": {
    "hero": 6,
    "guide": 7,
    "card": 1,
    "ler_menos_js": 2
  }
}
```
