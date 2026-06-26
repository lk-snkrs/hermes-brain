# LKGOC Adidas Samba mobile fix2 — dev theme

- Theme: lk-new-theme/dev (#155065450718)
- Asset: snippets/lk-goc-adidas-samba.liquid
- Escopo: mobile/tablet pequeno (`max-width:989px`) no LKGOC Adidas Samba

## Ajustes
- Título `coll-banner__title`: margem superior `.6633em` → `.59697em` (-10%); margem inferior `2.7px` → `2.43px` (-10%).
- Layout mobile reforçado por CSS + JS inline para vencer overrides globais 204L:
  - primeira imagem: coluna esquerda, vertical `3/4`
  - duas seguintes: coluna direita, horizontais `1.55/1`
  - sem `max-height`/crop do container escondendo as imagens

## QA
```json
{
  "final_marker": true,
  "top_spacing_59697": true,
  "bottom_spacing_243": true,
  "first_card_vertical_css": true,
  "secondary_horizontal_css": true,
  "inline_js_enforcement": true,
  "mobile_scope_989": true,
  "hash_match_local_readback": true,
  "readback_sha256": "b22a802ce8e20c832b7787eb47496286e0fa0e8c4322e9c0ce73dd93c2287824"
}
```

## Rollback
- Reverter `snippets/lk-goc-adidas-samba.liquid` para `before__snippets__lk-goc-adidas-samba.liquid`.
