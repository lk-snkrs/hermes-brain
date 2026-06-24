# DEV Preview — P1 LKGOC Lite: Crocs McQueen + Alo Yoga

**Gerado:** 2026-06-23T18:34:49.526990+00:00  
**Writes externos:** Shopify DEV/unpublished somente  
**Production/main:** intocado  
**values_printed:** false  

## Tema verificado

| Campo | Valor |
|---|---|
| Theme ID | `155065450718` |
| Theme name | `lk-new-theme/dev` |
| Role | `unpublished` |

## O que foi feito em DEV

- Inserido conteúdo LKGOC Lite para `alo-yoga-1` no snippet `snippets/lk-goc-collection.liquid`.
- Inserido conteúdo LKGOC Lite para `crocs-mcqueen` no snippet `snippets/lk-goc-collection.liquid`.
- Ajustado `sections/lk-collection.liquid` no DEV para renderizar o guide desses dois handles.
- Padrão usado: Guia LK pós-grid, FAQ único, bloco citável, schema `FAQPage`, linguagem premium sem promessa pública de estoque/prazo.

## QA público do preview DEV

| Página | HTTP | Guia LK | FAQPage | Copy específica | Liquid error | Preview URL |
|---|---:|---:|---:|---:|---:|---|
| alo | 200 | 1 | 1 | sim | não | https://lksneakers.com.br/collections/alo-yoga-1?_ab=0&_fd=0&_sc=1&preview_theme_id=155065450718 |
| crocs | 200 | 1 | 1 | sim | não | https://lksneakers.com.br/collections/crocs-mcqueen?_ab=0&_fd=0&_sc=1&preview_theme_id=155065450718 |

## Production untouched check

| Página | HTTP | Guia LK em produção | FAQPage em produção | Copy DEV apareceu em produção? |
|---|---:|---:|---:|---:|
| alo | 200 | 0 | 0 | não |
| crocs | 200 | 0 | 0 | não |

## Screenshots gerados

| Página | Mobile | Desktop |
|---|---|---|
| alo | `preview-final-alo-mobile.png` | `preview-final-alo-desktop.png` |
| crocs | `preview-final-crocs-mobile.png` | `preview-final-crocs-desktop.png` |

## Rollback DEV

Rollback local preparado:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/dev-preview-p1-crocs-alo-20260623/rollback_dev_p1_crocs_alo.py`

## Aprovação necessária para produção

> Aprovo promover para produção o LKGOC Lite de Crocs McQueen e Alo Yoga conforme preview DEV no tema `lk-new-theme/dev` (`role: unpublished`, theme `155065450718`), limitado a Guia LK pós-grid, FAQ único, bloco citável e schema FAQPage dessas duas collections, sem mexer em preço, estoque, produtos, ordenação, campanhas, GMC, Klaviyo ou checkout, com backup, readback, QA público e rollback.

## Artefatos

- `receipt.json`
- `section-render-receipt.json`
- `preview-public-qa-after-section.json`
- `preview-final-screenshot-manifest.json`
- `production-untouched-check.json`
- `rollback_dev_p1_crocs_alo.py`