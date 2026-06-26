# Production receipt — P1 LKGOC Lite Crocs McQueen + Alo Yoga

**Gerado:** 2026-06-23T18:44:33.992150+00:00  
**Aprovação:** Lucas aprovou no turno atual.  
**Escopo:** Guia LK pós-grid, FAQ único, bloco citável e schema FAQPage para Alo Yoga e Crocs McQueen.  
**Fora do escopo:** preço, estoque, produtos, ordenação, campanhas, GMC, Klaviyo, checkout.  
**values_printed:** false

## Execução

- O DEV preview foi promovido, mas o patch direto em `sections/lk-collection.liquid` bateu o limite Shopify de 256KB.
- Para evitar duplicidade/risco, restaurei os assets de tema alterados durante a tentativa e deixei a execução final em `descriptionHtml` das collections, com backups.
- Admin/preview main confirmou os blocos em `alo-yoga-1` e `crocs-mcqueen`.

## QA final

| URL | Modo | HTTP | Guia LK | FAQPage | Copy específica | Liquid error | Leitura |
|---|---|---:|---:|---:|---:|---:|---|
| https://lksneakers.com.br/collections/alo-yoga-1 | plain/cache atual | 200 | 0 | 0 | não | não | ⚠️ cache público ainda antigo |
| https://lksneakers.com.br/collections/crocs-mcqueen | plain/cache atual | 200 | 0 | 0 | não | não | ⚠️ cache público ainda antigo |
| https://lksneakers.com.br/collections/alo-yoga-1?preview_theme_id=155065417950 | preview_theme_id main / bypass cache | 200 | 1 | 1 | sim | não | ✅ render confirmado |
| https://lksneakers.com.br/collections/crocs-mcqueen?preview_theme_id=155065417950 | preview_theme_id main / bypass cache | 200 | 2 | 1 | sim | não | ✅ render confirmado |

## Status de propagação

- **Admin/preview main:** confirmado para Alo e Crocs, sem Liquid error.
- **URL plain:** ainda retornou HTML antigo no momento do QA. Interpretação: cache/propagação Shopify/CDN; não fiz novo write para evitar duplicidade.
- Recheck recomendado em 30–60 min e D+1.

## Rollback

Rollback preparado:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260623T1840Z-p1-crocs-alo-lkgoc-lite-production/rollback_p1_crocs_alo_production.py`

## Artefatos

- `receipt.json`
- `crocs-collection-description-receipt.json`
- `cleanup-theme-use-collection-body-receipt.json`
- `final-public-qa.json`
- `final-screenshot-manifest.json`
- `rollback_p1_crocs_alo_production.py`