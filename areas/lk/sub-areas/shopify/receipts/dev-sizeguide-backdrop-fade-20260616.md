# Receipt — DEV Size Guide Backdrop Fade — 2026-06-16

## Motivo

Lucas revisou o DEV no celular e apontou que, ao abrir o Guia de Tamanhos, ainda dava para ver a página atrás. A correção necessária era criar um fade/overlay real no fundo do modal.

## Escopo executado

Somente DEV theme:

- Theme: `lk-new-theme/dev`
- Theme id: `155065450718`
- Role: `unpublished`

Arquivo alterado:

- `sections/lk-pdp.liquid`

Production não foi alterada.

## Alteração

Antes, o overlay dependia principalmente de `.sg-modal__backdrop` absoluto dentro do modal. Em mobile/Safari, a página atrás ainda ficava visualmente aparente.

Depois:

- `.sg-modal.is-open` recebe `background: rgba(0,0,0,0.68)`
- `.sg-modal__backdrop` passa para `position: fixed`, `z-index: 0`, `background: rgba(0,0,0,0.68)`
- `.sg-modal__panel` recebe `z-index: 1`
- adicionados `backdrop-filter` e `-webkit-backdrop-filter`

## Backup

Backup DEV antes do patch:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/backups/dev-sizeguide-backdrop-fade-20260616/sections__lk-pdp.liquid.before.liquid`

## Readback

- DEV before sha256: `0f1101684a14656b1ff45a4b0d08b7e9a2aef0afb8c09fd22330ae917706605d`
- DEV target/post sha256: `0b3c749c72cf86f2a8e72a0761349cf9cdbabe4f7fb900ee10c31eec9cacc20c`
- DEV matches target: `true`
- Production unchanged: `true`

## QA mobile

Script:

`/tmp/lkqa-cdp/dev_sizeguide_backdrop_fade_20260616.js`

Resultado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-backdrop-fade-20260616/dev-sizeguide-backdrop-qa-results.json`

Screenshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-backdrop-fade-20260616/vomero-premium-sizeguide-backdrop-dev.jpg`

QA em mobile `390x844` no PDP Vomero Premium:

- modal existe: `true`
- modal aberto: `true`
- `aria-hidden=false`
- modal background: `rgba(0, 0, 0, 0.68)`
- backdrop background: `rgba(0, 0, 0, 0.68)`
- backdrop position: `fixed`
- panel z-index: `1`
- Liquid errors: `0`
- overflow horizontal: `false`
- copy Vomero Premium preservada: `true`

## Links de preview

- Base DEV: `https://lksneakers.com.br/?preview_theme_id=155065450718`
- Vomero Premium PDP DEV: `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto?preview_theme_id=155065450718`
- Nike Mind 002 PDP DEV: `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege?preview_theme_id=155065450718`

## Rollback

Reaplicar o backup `sections__lk-pdp.liquid.before.liquid` no DEV theme `155065450718` via Asset API e confirmar SHA de volta para:

`0f1101684a14656b1ff45a4b0d08b7e9a2aef0afb8c09fd22330ae917706605d`

## Status final

- DEV corrigido.
- Production intacta.
- QA mobile passou.
- Próxima decisão: Lucas revisar visualmente o DEV e aprovar ou pedir ajuste fino de intensidade do fade.
