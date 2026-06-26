# Receipt — Sambae page mobile 2-column correction

Data UTC: 2026-06-03T11:07:47.350010+00:00
Página: `/pages/guia-adidas-sambae`
Page ID: `127575949534`

## Escopo solicitado
- Seleção Adidas Sambae deve ter **duas colunas no mobile**.
- Produtos devem estar em **quantidade par**.
- Bloco **“Por que entra no radar da curadoria LK”** também deve ter **duas colunas no mobile**.

## Alterações aplicadas
- CSS mobile atualizado:
  - `.lk-products` em `repeat(2, minmax(0, 1fr))` no mobile.
  - `.lk-media-grid` em `repeat(2, minmax(0, 1fr))` no mobile.
  - cards da curadoria compactados para caber em 2 colunas: padding, title, body e label reduzidos.
  - cards de produto compactados: padding e fonte reduzidos.
- Validação de quantidade de produtos:
  - `6` produtos renderizados.
  - Quantidade par: `true`.

## Evidência
- `page.before.json`: snapshot pré-write.
- `page.after.json`: snapshot pós-write.
- `public.render.html`: render público validado.
- `sambae-mobile-2col-after.png`: screenshot mobile pós-ajuste.

## QA público
- Marker `mobile-2col-products-curadoria`: presente.
- CSS 2 colunas para produtos/curadoria: presente.
- Produtos renderizados: 6.

## Rollback
- Restaurar `body_html` de `page.before.json` via Admin API `PUT /pages/127575949534.json`.
