# LKGOC Adidas Samba image layout + modal hotfix — dev theme

- UTC: 20260604T092109Z
- Theme: lk-new-theme/dev (#155065450718)
- Asset: snippets/lk-goc-adidas-samba.liquid
- Escopo visual: mobile (`@media(max-width:749px)`) no bloco Adidas Samba/LKGOC

## Ajustes
- Primeira imagem “Samba · fashion week”: forçada vertical (`aspect-ratio:3/4`) e ocupando a coluna esquerda.
- Outras duas imagens: forçadas horizontais (`aspect-ratio:1.55/1`) na coluna direita.
- Popup in-page corrigido: clique em qualquer imagem abre modal com imagem ampliada.
- Corrigido bug de JS causado por seletores vazios legados (`', .'`) e mismatch `.is-open` vs `.is-visible`.

## QA
```json
{
  "mobile_layout_marker": true,
  "first_card_vertical": true,
  "secondary_cards_horizontal": true,
  "modal_visible_css": true,
  "clean_modal_selector": true,
  "click_opens_modal": true,
  "removed_empty_selector_in_script": true,
  "hash_match_local_readback": true,
  "readback_sha256": "dcca1d46d5ff212a10f4484e3e7243b0649b9ce302cbac3d1e19552282a58aac"
}
```

## Rollback
- Reverter `snippets/lk-goc-adidas-samba.liquid` para `before__snippets__lk-goc-adidas-samba.liquid`.
