# Receipt — Curadoria LK PDP title/label light hotfix DEV — 2026-06-06

## Escopo aprovado

Lucas aprovou explicitamente: `Aprovo hotfix DEV agora`.

Hotfix aplicado somente no tema DEV/unpublished para corrigir tipografia do bloco `Outras variações` / produtos de `Outras variações`.

## Shopify write

- Tema: `155065450718`
- Role: `unpublished`
- Asset: `assets/lk-variante.css`
- Ação: `PUT`
- Production: não alterado
- Produtos/preços/estoque/checkout/apps: não alterados

## Mudança

Adicionado hotfix CSS no fim de `assets/lk-variante.css`:

```css
/* LK Curadoria PDP title/label light hotfix 2026-06-06: "Outras variações" and product labels must render light. */
.lk-variante__title,
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label,
.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{
  font-weight:300 !important;
}
```

## Readback

- Status: `ok`
- Convergência: tentativa `2`
- SHA antes: `ab25b871819f9e5699490bb68303909cd5ff96610db39a37ffc0d04e2edd0128`
- SHA depois/readback: `98c8b47b854670e226c65d52f97d3d14967451119722a87873d1617f07521a5e`
- Hotfix de título presente: sim
- `font-weight:300 !important` count: `2`
- `font-weight:400` antigo: `0`

Arquivos:

- Backup antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-dev-20260606/20260606T144629Z-dev-theme-155065450718-assets__lk-variante.before.css`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-dev-20260606/20260606T144629Z-dev-theme-155065450718-assets__lk-variante.after.css`
- JSON receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-title-label-light-dev-20260606/20260606T144629Z-receipt.json`

## QA visual/computed DEV

PDP validado:

- URL: `https://lksneakers.com.br/products/tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme?preview_theme_id=155065450718&hermes_qa=title_light_1`
- Bloco renderizou: `true`
- Marker: `top30-adidas-tokyo-regular`
- Título: `Outras variações`
- `titleFontWeight`: `300`
- `labelFontWeight`: `300`
- `eyebrowFontWeight`: `500` (mantido; não estava no escopo)

Outras duas URLs testadas não renderizaram o bloco nesse estado de preview/catálogo, então não foram usadas como evidência de tipografia.

## Rollback

Restaurar o backup `before.css` acima no asset `assets/lk-variante.css` do tema DEV `155065450718`.
