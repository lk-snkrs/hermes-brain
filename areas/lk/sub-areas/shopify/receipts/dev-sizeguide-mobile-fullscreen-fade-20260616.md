# Receipt — DEV Size Guide Mobile Fullscreen Fade — 2026-06-16

## Motivo

Lucas revisou o primeiro ajuste do fade e mostrou screenshot onde o topo superior ainda exibia a imagem da PDP atrás do Guia de Tamanhos. O problema real era que, no mobile, ainda havia uma janela visual acima do painel do modal.

## Escopo executado

Somente DEV theme:

- Theme: `lk-new-theme/dev`
- Theme id: `155065450718`
- Role: `unpublished`

Arquivo alterado:

- `sections/lk-pdp.liquid`

Production não foi alterada.

## Alteração

No `@media (max-width: 749px)`, o modal do Guia passou a ocupar a viewport inteira:

- `.sg-modal` mobile: `align-items: stretch`, `justify-content: stretch`, `padding: 0`
- `.sg-modal.is-open` mobile: `background: rgba(0,0,0,0.78)`
- `.sg-modal__backdrop` mobile: `position: fixed`, `inset: -12px 0 0`, `background: rgba(0,0,0,0.78)`
- `.sg-modal__panel` mobile: `width: 100%`, `height: 100dvh`, `max-height: 100dvh`, `border: 0`, `border-radius: 0`, `transform: none`
- Header considera `env(safe-area-inset-top)`

Objetivo: impedir que a página/PDP apareça por cima ou atrás no topo do modal em mobile.

## Backup

Backup DEV antes do patch:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/backups/dev-sizeguide-mobile-fullscreen-fade-20260616/sections__lk-pdp.liquid.before.liquid`

## Readback

- DEV before sha256: `0b3c749c72cf86f2a8e72a0761349cf9cdbabe4f7fb900ee10c31eec9cacc20c`
- DEV target/post sha256: `7268f5d1fcbc16fd09fb3cbf869fc195bd75845b3ef5af0b71d65cce8236404c`
- DEV matches target: `true`
- Production unchanged: `true`

## QA mobile

Script:

`/tmp/lkqa-cdp/dev_sizeguide_mobile_fullscreen_fade_20260616.js`

Resultado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-mobile-fullscreen-fade-20260616/dev-sizeguide-mobile-fullscreen-fade-results.json`

Screenshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-mobile-fullscreen-fade-20260616/vomero-premium-sizeguide-fullscreen-fade-dev.jpg`

QA em mobile `390x844` no PDP Vomero Premium:

- modal existe: `true`
- modal aberto: `true`
- `aria-hidden=false`
- modal position: `fixed`
- modal rect: `top=0`, `height=844`
- modal background: `rgba(0, 0, 0, 0.78)`
- backdrop background: `rgba(0, 0, 0, 0.78)`
- panel background: `rgb(255,255,255)`
- panel rect: `top=0`, `height=844`
- amostras no topo (`y=5`, `y=20`) retornam elementos do modal/header, não PDP atrás
- Liquid errors: `0`
- overflow horizontal: `false`
- copy Vomero Premium preservada: `true`

## Links de preview

- Base DEV: `https://lksneakers.com.br/?preview_theme_id=155065450718`
- Vomero Premium PDP DEV: `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto?preview_theme_id=155065450718`
- Nike Mind 002 PDP DEV: `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege?preview_theme_id=155065450718`

## Rollback

Reaplicar o backup `sections__lk-pdp.liquid.before.liquid` no DEV theme `155065450718` via Asset API e confirmar SHA de volta para:

`0b3c749c72cf86f2a8e72a0761349cf9cdbabe4f7fb900ee10c31eec9cacc20c`

## Status final

- DEV corrigido novamente, agora com modal mobile fullscreen.
- Production intacta.
- QA mobile passou.
- Próxima decisão: Lucas revisar no iPhone real e confirmar visual.
