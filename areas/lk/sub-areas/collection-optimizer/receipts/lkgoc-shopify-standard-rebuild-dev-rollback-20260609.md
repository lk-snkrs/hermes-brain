# Receipt — Rollback DEV LKGOC rebuild

Data: 2026-06-09  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role verificado: `unpublished`  
Production: não alterada

## Motivo

Lucas validou visualmente que o rebuild `collection.lkgoc` piorou a experiência. O hero ficou visualmente inferior ao padrão aprovado, com proporção ruim e imagens de produto soltas em fundo branco.

## Ação executada

Rollback imediato em DEV:

- restaurado `sections/lk-collection.liquid` a partir de `dev-backup-before-put/`;
- restaurado `templates/collection.lkgoc.json` a partir de `dev-backup-before-put/`;
- removidos assets novos:
  - `sections/lk-goc-collection-hero.liquid`;
  - `sections/lk-goc-collection-guide.liquid`.

## Verificação pós-rollback

Preview `/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`:

- HTTP 200;
- role unpublished presente;
- Liquid error: 0;
- `data-lkgoc-standard="hero-v1"`: 0;
- `data-lkgoc-standard="guide-v1"`: 0;
- texto `Motorsport baixo`: 0.

## Decisão

Não seguir com rebuild visual baseado em produto cutout/white background. Próxima tentativa deve partir do recorte visual real aprovado da 204L, com screenshot comparativo antes de qualquer novo upload DEV.
