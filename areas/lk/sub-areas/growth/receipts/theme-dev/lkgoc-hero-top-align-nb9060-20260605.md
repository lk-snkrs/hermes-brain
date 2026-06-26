# Receipt — LKGOC Hero top align NB9060 DEV

Data: 2026-06-05T18:17:52

## Pedido Lucas
Topo das imagens do Hero deve alinhar com `.coll-banner__crumbs`.

## Executado
- Regra Brain criada: `rules/REGRA-LKGOC-HERO-IMAGENS-ALINHAR-COM-BREADCRUMBS.md`.
- Tema DEV atualizado: `155065450718`.
- Arquivo alterado: `snippets/lk-goc-new-balance-9060-hero-204l-clone.liquid`.
- Ajuste: collage desktop NB9060 `translateY(-34px)` → `translateY(-107px)` e `margin-bottom` equivalente.

## Backup
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-hero-top-align-20260605/before__snippets__lk-goc-new-balance-9060-hero-204l-clone.liquid`

## Readback
- Readback do snippet confirmou `translateY(-107px)` e `margin-bottom:-107px`.

## QA desktop 1280px
```json
{
  "url": "https://lksneakers.com.br/collections/new-balance-9060?qa=1780683453066",
  "crumbs": {
    "top": 140,
    "left": 40,
    "width": 1200,
    "height": 16,
    "bottom": 156
  },
  "collage": {
    "top": 140,
    "left": 638.8,
    "width": 602.8,
    "height": 332.8,
    "bottom": 472.8
  },
  "firstImg": {
    "top": 140,
    "left": 638.8,
    "width": 313.1,
    "height": 332.8,
    "bottom": 472.8
  },
  "deltaTop": 0,
  "css": "matrix(1, 0, 0, 1, 0, -107)"
}
```

## Evidência visual
- Before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-hero-top-align-20260605/nb9060-before-1280.png`
- After: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-hero-top-align-20260605/nb9060-after-1280.png`

## Nota
Production não foi alterado neste receipt. Merge para Production exige aprovação explícita atual do Lucas.
