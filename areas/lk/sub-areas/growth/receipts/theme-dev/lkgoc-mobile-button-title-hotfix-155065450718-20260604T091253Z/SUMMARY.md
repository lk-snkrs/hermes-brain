# LKGOC mobile button/title hotfix — dev theme

- UTC: 20260604T091253Z
- Theme: lk-new-theme/dev (#155065450718)
- Role verificado via Shopify CLI: unpublished
- Asset alterado: snippets/lk-goc-adidas-samba.liquid
- Escopo: apenas mobile (`@media(max-width:749px)`)

## Alterações
- `lk-goc-read-more` virou botão real no mobile: pill, border, padding, radius, min-height e sem dependência de `lk-204l`.
- `coll-banner__title` em páginas com `.lk-goc-coll-preview`: `margin-top:.737em` (+10% vs default `.67em`) e `margin-bottom:3px` (50% menor que o ritmo ativo de 6px).

## QA
- Readback do asset remoto feito e hash confere com candidato local.
- Marcador CSS encontrado no readback.

## Rollback
- Reverter `snippets/lk-goc-adidas-samba.liquid` para `before__snippets__lk-goc-adidas-samba.liquid` deste receipt.
