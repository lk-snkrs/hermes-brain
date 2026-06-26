# Receipt — Curadoria LK PDP title/label light hotfix — merge para Production — 2026-06-06

## Escopo aprovado

Lucas aprovou: `provo merge para Production do hotfix light Outras variações`.

Interpretação operacional: aprovação explícita para **merge para Production** do hotfix de tipografia já validado em DEV.

## Escopo executado

- Repo: `lk-snkrs/lk-new-theme`
- Base: `production`
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/29`
- Merge: squash merge concluído
- Commit merge: `a042033e0a5e5cc0a34cab2bf59e4921a483b294`
- Asset: `assets/lk-variante.css`
- Shopify theme: `155065417950`
- Role: `main`

Não alterado:

- Produtos
- Preços
- Estoque
- Checkout
- Imagens
- Snippets/Liquid
- Apps/campanhas

## Mudança

Adicionado override CSS final para a Curadoria LK PDP:

```css
/* LK Curadoria PDP title/label light hotfix 2026-06-06: "Outras variações" and product labels must render light. */
.lk-variante__title,
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label,
.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{
  font-weight:300 !important;
}
```

## Verificação GitHub

- PR mergeable state: `clean`
- `git diff --check`: passed
- Arquivos alterados: somente `assets/lk-variante.css`
- Diff stat: `1 file changed, 7 insertions(+)`
- Branch temporário removido: sim

## Readback Shopify Production

- SHA live antes: `b4673719c878d3314c243580db9404e31e2156dda677edd8587197fcfd5947cd`
- SHA repo/live depois: `7f014399ad96fd55ec33229bea1758c9c5f4db66c066e65a87511046adb6914a`
- Hotfix presente no live readback: sim
- Convergência Shopify: tentativa `2`
- `font-weight:300 !important` count depois: `2`
- `font-weight:400` count depois: `0`

Arquivos:

- Backup antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-production-20260606/20260606T145156Z-production-theme-155065417950-assets__lk-variante.before.css`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-production-20260606/20260606T145156Z-production-theme-155065417950-assets__lk-variante.after.css`
- JSON receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-production-20260606/20260606T145156Z-merge-receipt.json`

## QA live computed

### Adidas Tokyo regular

URL: `https://lksneakers.com.br/products/tenis-adidas-tokyo-off-white-core-black-branco?hermes_qa=prod_title_light_deep1`

- Bloco renderizou: `true`
- Marker: `top30-adidas-tokyo-regular`
- Título: `Outras variações`
- `titleFontWeight`: `300`
- `labelFontWeight`: `300`
- `labelAfterContent`: `"Core Black"`
- `labelAfterFontWeight`: `300`

### New Balance 530

URL: `https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?hermes_qa=prod_title_light_deep2`

- Bloco renderizou: `true`
- Marker: `top30-nb-530`
- Título: `Outras variações`
- `titleFontWeight`: `300`
- `labelFontWeight`: `300`
- `labelAfterContent`: `none`
- `labelAfterFontWeight`: `300`

## Caveat

A PDP `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme` não renderizou bloco Curadoria em Production no momento do QA; por isso a QA live de tipografia foi feita em PDPs que renderizam o bloco em Production. O hotfix é global para `assets/lk-variante.css` e readback do asset main confirmou a mudança.

## Rollback

Opções:

1. Reverter o PR/commit `a042033e0a5e5cc0a34cab2bf59e4921a483b294` na branch `production`; ou
2. Restaurar o backup `before.css` acima no asset `assets/lk-variante.css` do tema Production `155065417950`.
