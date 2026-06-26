# Receipt — DEV Size Guide Black 70 Backdrop — 2026-06-16

## Motivo

Lucas esclareceu o comportamento correto: ao abrir o Guia de Tamanhos, o fundo da página deve ficar preto com 70% de opacidade. O ajuste fullscreen branco anterior foi removido porque não correspondia ao visual desejado.

## Escopo executado

Somente DEV theme:

- Theme: `lk-new-theme/dev`
- Theme id: `155065450718`
- Role: `unpublished`

Arquivo alterado:

- `sections/lk-pdp.liquid`

Production não foi alterada.

## Alteração

No mobile (`max-width: 749px`):

- `.sg-modal.is-open`: `background: rgba(0,0,0,0.70)`
- `.sg-modal__backdrop`: `position: fixed; inset: 0; background: rgba(0,0,0,0.70)`
- Painel volta a ser um modal/painel branco, não fullscreen branco:
  - `padding-top: 58px`
  - painel começa em `top=58px`
  - topo visível é o backdrop preto 70%, não a imagem da PDP

## Backup

Backup DEV antes do patch:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/backups/dev-sizeguide-black70-backdrop-20260616/sections__lk-pdp.liquid.before.liquid`

## Readback

- DEV before sha256: `7268f5d1fcbc16fd09fb3cbf869fc195bd75845b3ef5af0b71d65cce8236404c`
- DEV target/post sha256: `006dcb8fe9e83c996514e60eb77ca1dd0e2dabf16cfa259df7b424a787362b0e`
- DEV matches target: `true`
- Production unchanged: `true`

## QA mobile

Script:

`/tmp/lkqa-cdp/dev_sizeguide_black70_backdrop_20260616.js`

Resultado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-black70-backdrop-20260616/dev-sizeguide-black70-backdrop-results.json`

Screenshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-sizeguide-black70-backdrop-20260616/vomero-premium-sizeguide-black70-backdrop-dev.jpg`

QA em mobile `390x844` no PDP Vomero Premium:

- modal aberto: `true`
- modal background: `rgba(0, 0, 0, 0.7)`
- backdrop background: `rgba(0, 0, 0, 0.7)`
- backdrop position: `fixed`
- painel começa em `top=58px`
- amostra no topo (`y=20`) retorna `.sg-modal__backdrop`, não PDP atrás
- Liquid errors: `0`
- overflow horizontal: `false`
- copy Vomero Premium preservada: `true`

## Links de preview

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto?preview_theme_id=155065450718`
- `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege?preview_theme_id=155065450718`

## Status

- DEV corrigido para fundo preto 70%.
- Production intacta.
- QA mobile passou.
