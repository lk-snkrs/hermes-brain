# LKGOC Adidas Samba mobile title spacing — dev theme

- UTC: 20260604T091758Z
- Theme: lk-new-theme/dev (#155065450718)
- Asset: snippets/lk-goc-adidas-samba.liquid
- Escopo: apenas mobile (`@media(max-width:749px)`) e Adidas Samba/LKGOC (`.lk-goc-coll-preview--204l`)

## Ajuste
- `coll-banner__title` top: `.737em` → `.6633em` (-10%)
- `coll-banner__title` bottom: `3px` → `2.7px` (-10%)

## QA
```json
{
  "margin_top_6633": true,
  "margin_bottom_2_7": true,
  "scoped_samba_lkgoc": true,
  "mobile_only": true,
  "hash_match_local_readback": true,
  "readback_sha256": "62a5c84bec1066f3d9f3a8a95881c03447ade551242fe7dcdd7a58d2af195346"
}
```

## Rollback
- Reverter `snippets/lk-goc-adidas-samba.liquid` para `before__snippets__lk-goc-adidas-samba.liquid`.
