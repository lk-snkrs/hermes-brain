# Receipt — DEV Curadoria LK PDP ASICS GT-2160 + Wales Bonner

Data UTC: 2026-06-08T01:14:52Z

## Escopo
- Aprovação recebida: `Aprovo` — interpretada como aprovação do escopo imediato DEV/unpublished previamente apresentado.
- Production/merge/deploy não aprovados e não executados.
- Theme DEV: `155065450718` (`lk-new-theme/dev`, unpublished).
- Asset principal: `snippets/lk-variante-top30-visited-v2.liquid`.
- Split snippet novo: `snippets/lk-variante-asics-gt2160-walesbonner-20260608.liquid`.

## Mudança
- `top30-asics-gt-2160-regular` — ASICS GT-2160: 6 handles.
- `top30-adidas-wales-bonner-samba` — Adidas Samba Wales Bonner: 3 handles.

## Evidência
- Doppler/Shopify usados sem imprimir valores: `values_printed=false`.
- Preflight público antes do write: `9` produtos `.js` OK; `9` imagens OK.
- PUT split status: `200`; PUT main status: `200`.
- Main SHA12 antes: `aba2ed49b088`; readback depois: `7b5e88f521ba`.
- Split SHA12 readback: `be2f6216c380`.
- Readback attempts: `1`.
- Render line count no main: `1`.
- Marker counts no split: `{'top30-asics-gt-2160-regular': 2, 'top30-adidas-wales-bonner-samba': 2}`.
- Handles presentes: `{'top30-asics-gt-2160-regular': True, 'top30-adidas-wales-bonner-samba': True}`.
- Current-product exclusion guard: `True`.
- Malformed URLs: `False`; placeholder images: `False`.
- Static/readback QA final: `True`.

## Rollback DEV
- Restaurar `dev-main-before.liquid` em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover/zerar o split snippet `snippets/lk-variante-asics-gt2160-walesbonner-20260608.liquid` se rollback completo for necessário.

## Arquivos
- `dev-main-before.liquid`
- `dev-main-new.liquid`
- `dev-split-new.liquid`
- `receipt.json`

## Preview QA público
- Theme readback: `lk-new-theme/dev` / role `unpublished`.
- `tenis-asics-gt-2160-white-putty-branco`: status `200`, final_url_contains_preview `False`, marker_present `False`, lk_variante_present `False`, current_product_excluded `True`.
- `tenis-adidas-samba-x-wales-bonner-wonder-white-marrom`: status `200`, final_url_contains_preview `False`, marker_present `False`, lk_variante_present `False`, current_product_excluded `True`.
- Caveat: se `preview_theme_id` for removido/redirecionado, classificar HTML público como inconclusivo e manter readback/static QA como evidência primária.
