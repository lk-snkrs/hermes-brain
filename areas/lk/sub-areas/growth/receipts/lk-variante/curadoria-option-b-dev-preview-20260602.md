# Curadoria LK — Opção B Dev Preview — 2026-06-02

## Escopo aprovado
- Upload em Dev theme/unpublished do snippet `snippets/lk-variante-top30-visited.liquid`.
- Touch mínimo aprovado em Dev theme/unpublished da section `sections/lk-pdp.liquid` para recompilação.
- Sem Production, sem produto, sem preço, sem estoque, sem checkout, sem apps.

## Theme
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`

## Readback
- Snippet before SHA12: `a62a0ba774c3`
- Snippet proposed/readback SHA12: `3ddbc92afb29`
- Section touch readback SHA12: `bafc6a7d9624`

## QA preview correto
- Observação: `preview_theme_id` isolado era removido por redirect; QA válido exigiu abrir sessão/cookie de preview no domínio `lksneakers.com.br` antes das PDPs.
- Checked PDPs: 20
- Pass: True
- Falhas: 0

## Amostras
- `new-balance-530-white-natural-indigo-1` → `top30-nb-530` → Turtledove, Silver Cream, Silver White, Steel Grey, Silver Blue
- `adidas-campus-00s-dark-green` → `top30-adidas-campus-regular` → Crystal White, Grey Three, Ambient Sky, Bliss Pink, Scarlet Red
- `tenis-air-jordan-1-mid-glitter-swoosh-azul` → `top30-air-jordan-1-mid-regular` → Wolf Grey, Panda, Electro Orange, Canyon Rust, Aqua Tint
- `air-jordan-1-high-85-college-navy` → `top30-air-jordan-1-high-regular` → Atmosphere, Lost & Found, Dark Mocha, Lucky Green, Next Chapter
- `tenis-nike-shox-tl-black-cave-stone-preto` → `top30-nike-shox-tl-regular` → Black Yellow, Blue Tint Orange, Orewood Brown, Pumice Maroon, Sunrise Gradient
- `tenis-asics-gel-1130-black-pure-silver-prata` → `top30-asics-gel-1130-regular` → Black Silver #2, White Black #1, White Black #2, White Clay, White Silver
- `yeezy-foam-runner-carbon` → `top30-yeezy-foam-runner-regular` → MX Cinder, MX Sand Grey, Onyx, Sand, Stone Sage
- `tenis-air-force-1-low-07-panda-preto` → `top30-nike-air-force-1-low-regular` → Snake White, Snake Beige, Fire Red, UV Reactive, Vachetta Flax

## Rollback Dev
- Reenviar backup local `dev-before.liquid` para `snippets/lk-variante-top30-visited.liquid`.
- Reenviar backup local `dev-lk-pdp-before-touch.liquid` para `sections/lk-pdp.liquid` se necessário.

## Próximo gate
- Production exige aprovação explícita atual de Lucas.