# Receipt — LKGOC Puma Speedcat DEV

Data: 20260606T172640Z
Status: **DEV_PREVIEW_OK / PRODUCTION_BLOCKED**

## Escopo executado

Coleção: `puma-speedcat`
Tema DEV: `155065450718` — `lk-new-theme/dev` — `role: unpublished`
Production/main: **não escrito**

## Assets Shopify alterados no DEV

- `snippets/lk-goc-collection.liquid`
- `sections/lk-collection.liquid`

## O que foi construído

- Hero LKGOC para Puma Speedcat no componente único `lk-goc-collection`.
- Imagens editoriais principais de veículos de moda/referência:
  - Vogue US
  - Vogue Brasil / Globo
  - Overkill
- Guia editorial pós-grid com densidade LKGOC.
- FAQ em 2 colunas no desktop.
- FAQPage schema.
- Grid de produtos preservado antes do guia.

## Preview DEV

Abrir nesta sequência para garantir cookie de preview:

1. `https://lk-sneakerss.myshopify.com/?preview_theme_id=155065450718`
2. `https://lk-sneakerss.myshopify.com/collections/puma-speedcat`

Alternativa provável:

`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

## QA final

Status: `PASS`

Checks principais:

- ✅ has_puma_hero
- ✅ has_puma_guide_id
- ✅ has_vogue_us_image
- ✅ has_vogue_br_image
- ✅ has_overkill_image
- ✅ has_faq_schema
- ✅ has_faq_grid_css
- ✅ no_liquid_error
- ✅ uses_dev_theme_assets
- ✅ hero_before_grid
- ✅ guide_after_grid
- ❌ production_write
- ✅ puma-speedcat-lkgoc-dev-dom-desktop.png_exists
- ✅ puma-speedcat-lkgoc-dev-dom-mobile.png_exists

## Evidência DEV/Production

DEV:

- Snippet tem Puma: `True`
- Snippet tem Vogue assets: `True`
- Section tem Puma: `True`

Production/main:

- Tema main: `155065417950` — `lk-new-theme/production`
- Main snippet com marker Puma LKGOC: `False`
- Main section com marker Puma LKGOC: `False`

## Rollback DEV

Snapshots antes do write salvos em:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/snippets__lk-goc-collection.liquid.before`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/sections__lk-collection.liquid.before`

Rollback: restaurar esses dois assets no tema DEV `155065450718`, após verificar `role: unpublished`.

## Arquivos de QA

- DOM DEV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/qa-final/dev-preview-dom-python-cookie.html`
- Screenshot desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/qa-final/puma-speedcat-lkgoc-dev-dom-desktop.png`
- Screenshot mobile: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/qa-final/puma-speedcat-lkgoc-dev-dom-mobile.png`
- Media manifest: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/MEDIA-MANIFEST.json`
- DEV/Prod guard: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-dev-build-20260606T171642Z/DEV-PROD-GUARD-READBACK.json`

## Decisão necessária

Nenhuma aprovação necessária para manter no DEV.

Para Production: **PRODUCTION_BLOCKED** até Lucas aprovar merge/promoção DEV → Production.
