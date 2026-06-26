# Receipt — Shopify Production hotfix New Balance 204L

Data: 2026-05-27
Origem: Lucas Cimino / Telegram
Tema: `lk-new-theme/production`
Theme ID: `155065417950`
URL: https://lksneakers.com.br/collections/new-balance-204l

## Escopo aprovado executado

- H1 `New Balance 204L`: aumento de `48px` para `52px` via override escopado à coleção 204L.
- Kicker: de `Curadoria LK · New Balance 204L` para `Curadoria LK`.
- Grid/paginação: de `24` para `20` produtos por página no template `collection.json`.

## Assets alterados

- `sections/lk-collection.liquid`
- `templates/collection.json`

## Backup / rollback

Backup local:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-hotfix-20260527-125430`

Arquivo de readback API:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/204l-hotfix-20260527-125430/receipt-api-readback.json`

Rollback: reaplicar os dois assets salvos no backup acima.

## Readback API

- `kicker_clean`: true
- `kicker_old_absent`: true
- `h1_override`: true
- `products_per_page_20`: true

SHA antes:

- `sections/lk-collection.liquid`: `45d5fc9cc918952b7a508b21b3fbd8369f2b8272c06bd74a7063424e637587da`
- `templates/collection.json`: `952b42732ae843553ec415d53bc3950dfe16f0e3393d4d64c1d569af8ddd4c93`

SHA depois:

- `sections/lk-collection.liquid`: `25d7e34434eec8cb4e95f7c5fc91431fc92852686a59276dfb7dd0b8467cafa1`
- `templates/collection.json`: `eaa311f84581fbd9bb124c1af132c4383f503fe175128a88a77860d2cd82b962`

## QA público

URL validada com cachebuster:

`https://lksneakers.com.br/collections/new-balance-204l?hermes_postpatch_browser=20260527_1258`

Resultado DOM/computed style:

- H1: `New Balance 204L`
- Fonte computada H1: `52px`
- Kicker: `Curadoria LK`
- Produto links únicos no grid principal: `20`
- Override CSS `font-size:52px!important`: presente

## Não alterado

- Produto, preço, estoque, filtros, ordenação comercial, checkout, apps, campanhas, Klaviyo, Meta/Google Ads, GMC e menus.

## Revisão de impacto

Revisar em aproximadamente 7 dias: comportamento de cliques/engajamento da coleção, PDP views a partir da coleção, add-to-cart e conversão via GA4/Shopify/GSC quando disponível.
