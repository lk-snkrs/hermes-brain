# Receipt — Curadoria LK PDP Cloudsolo Loewe Production merge

Data: 2026-06-06T10:19:45Z

## Aprovação

Lucas aprovou seguir e fazer merge para Production do pacote Curadoria LK PDP Cloudsolo Loewe já aplicado e validado no DEV.

## Escopo executado

Asset promovido:

- `snippets/lk-variante-top30-visited-v2.liquid`

Mudança:

- adiciona o grupo `top30-on-running-cloudsolo-loewe` nos arrays `lk_top30_*`;
- 16 handles;
- 16 labels;
- 16 imagens.

Não foram alterados:

- produtos;
- preço;
- estoque;
- checkout;
- apps;
- campanhas;
- GMC/Meta/Klaviyo/Tiny.

## Preflight

DEV:

- theme ID: `155065450718`
- name: `lk-new-theme/dev`
- role: `unpublished`

Production:

- theme ID: `155065417950`
- name: `lk-new-theme/production`
- role: `main`

## GitHub merge

PR:

- https://github.com/lk-snkrs/lk-new-theme/pull/25

Commit/merge:

- head SHA: `d2b988f024b89106cb7cb8ceaa3810aace083ac0`
- merge SHA: `a7b0bfe648a9086da9d208ab77298ef5deff9207`

Verificações locais:

- `git diff --check`: passou
- arquivos alterados: apenas `snippets/lk-variante-top30-visited-v2.liquid`
- diff: `1 file changed, 6 insertions(+), 5 deletions(-)`

## Shopify Production readback

Backup antes do merge:

- `20260606T101945Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.before.liquid`

Readback após sync/deploy:

- `20260606T101945Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.after.liquid`

Poll Shopify Production:

- tentativa 1: marker `0`, SHA antigo `493429e95ac5717563b0f3411031d89accc043ca91493f6c0cf8c4a632068a7f`
- tentativa 2: marker `1`, SHA novo `4b0835bf2d5b12928aebc9a6a71733d86909bb7971a4cfc00a22ef28fcbb3a3f`

Readback final validado:

- marker count: `1`
- arrays: `[28, 28, 28, 28, 28]`
- arrays alinhados: `true`
- new index: `27`
- handles: `16`
- labels: `16`
- images: `16`
- malformed https: `0`

## QA live público

Arquivo:

- `20260606T101945Z-production-live-cdp-qa-summary.json`

### Lime Green

URL:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-lime-green-amarelo?_qa=cloudsolo_prod_qa_1`

Resultado:

- bloco: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Black`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- span font-weight: `400`
- visual `::after` font-weight: `300`

### Black

URL:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-black-preto?_qa=cloudsolo_prod_qa_2`

Resultado:

- bloco: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Lime Green`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- span font-weight: `400`
- visual `::after` font-weight: `300`

### Teal Eggshell

URL:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1?_qa=cloudsolo_prod_qa_3`

Resultado:

- bloco: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Lime Green`, `Black`, `Turquoise`, `White Light Grey`, `White Orange`
- span font-weight: `400`
- visual `::after` font-weight: `300`

## Rollback

Opções:

1. Reverter o PR/merge commit no GitHub; ou
2. Restaurar o backup Production:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-cloudsolo-loewe-production-20260606/20260606T101945Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.before.liquid`

## Status final

Production merge + Shopify readback + QA live público: **passou**.
