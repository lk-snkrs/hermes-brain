# Receipt — LKGOC Shopify Standard Rebuild em DEV

Data: 2026-06-09  
Dono: `[LK] Otimização de Coleções` / LKGOC  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role verificado antes do write: `unpublished`  
Production: **não alterada**

## Objetivo

Reconstruir o padrão LKGOC para escalar coleções Shopify sem remendos por coleção.

## Arquitetura criada em DEV

- `templates/collection.lkgoc.json`
  - Ordem: hero → grid → guide.
- `sections/lk-goc-collection-hero.liquid`
  - Hero reutilizável baseado no gold visual 204L.
  - Conteúdo por settings no template; futuro: metafields/metaobjects.
- `sections/lk-goc-collection-guide.liquid`
  - Guide reutilizável com bullets e FAQ via blocks/settings.
- `sections/lk-collection.liquid`
  - Patch seguro: novo setting `grid_only`.
  - Quando `grid_only=true`, não renderiza banner antigo nem hero/guide acoplados.
  - Preserva filtros, ordenação, grid e paginação/load more existentes.

## Prova aplicada

Collection de teste: `/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`

## Readback HTTP

- Status: 200
- Role unpublished encontrado: 1
- `Liquid error`: 0
- `data-lkgoc-standard="hero-v1"`: 1
- `data-lkgoc-standard="guide-v1"`: 1
- `lk-guia-puma-speedcat`: 1
- `<div class="coll-banner">`: 0
- `lk-goc-coll-preview--speedcat`: 0
- `coll-grid`: presente

## QA Playwright

Mobile:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- oldSpeedcat: 0
- bannerElements: 0
- grid: true
- visibleBad: false

Desktop:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- oldSpeedcat: 0
- bannerElements: 0
- grid: true
- visibleBad: false

## Evidências locais

- HTML readback: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/readback-puma-speedcat-lkgoc-after-gridonly.html`
- QA script: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/qa_lkgoc_rebuild.js`
- Screenshot mobile: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/rebuild-mobile.png`
- Screenshot desktop: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/rebuild-desktop.png`
- Backups DEV antes do put: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/dev-backup-before-put/`

## Rollback DEV

Restaurar assets de `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-rebuild-standard-20260609/dev-backup-before-put/` para:

- `sections/lk-collection.liquid`
- `sections/lk-goc-collection-hero.liquid` se existia; antes estava ausente.
- `sections/lk-goc-collection-guide.liquid` se existia; antes estava ausente.
- `templates/collection.lkgoc.json`

## Observações

- Primeiro upload do template foi sanitizado pela Shopify e removeu `grid_only`; após o schema já estar salvo no tema, o template foi reenviado e manteve `grid_only:true`.
- Production não foi tocada.
- Próximo passo antes de qualquer Production: QA visual humano + approval Lucas + promoção controlada.
