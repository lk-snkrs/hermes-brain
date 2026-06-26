# LKGOC Vomero Premium — padrão 204L aplicado em DEV

Data: 2026-06-09T20:19:15.017247Z

## Escopo
Aplicar na collection `nike-vomero-premium` o padrão visual LKGOC definido no gold source New Balance 204L.

## Ambiente
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado antes do write: `unpublished`
- Production: não alterada

## Assets alterados no DEV
- `sections/lk-collection.liquid`
  - adicionado render do snippet Vomero Premium hero 204L clone.
- `snippets/lk-goc-nike-vomero-premium-hero-204l-clone.liquid`
  - criado a partir do bloco real 204L, mantendo classes e comportamento visual.
- `templates/collection.vomero-premium-lkgoc.json`
  - alternate template para preview com `?view=vomero-premium-lkgoc`.

## Referências pesquisadas
- Shopify JSON templates
- Shopify sections
- Shopify alternate templates
- Shopify section settings/schema
- Shopify metafields/metaobjects
- Nike About: Vomero Premium/Plus official release.

## QA
- Readback HTTP Vomero: 200
- Liquid error: 0
- Hero Vomero: presente
- Guide Vomero: presente
- H1: 1
- Hero duplicado: não observado
- Desktop: banner top/height alinhado à 204L após ocultar breadcrumbs
- Guide desktop: largura alinhada à 204L (`1376px` em viewport 1440)
- Mobile/desktop screenshots salvos em `/opt/data/profiles/lk-collection-optimizer/output/vomero-premium-lkgoc-20260609/`

## Pendências antes de Production
- QA visual humano pelo Lucas.
- Confirmar se imagens de produto LK/CDN são suficientes ou se será necessário media manifest para imagens editoriais externas.
- Preparar approval packet e rollback.
- Não publicar sem aprovação explícita.

## Rollback DEV
Backups em:
`/opt/data/profiles/lk-collection-optimizer/output/vomero-premium-lkgoc-20260609/dev-backup-before-vomero-put/`


## QA final pós-ajuste de geometria
- Desktop Vomero banner: top `100`, bottom `211.03125`, height `111.03125` — igual 204L.
- Desktop Vomero preview: top `211.03125`; altura `390` vs 204L `398` — diferença residual de conteúdo/texto, aceitável para DEV visual humano.
- Desktop Vomero collage: top `140.03125`, bottom `590.03125`, height `450` — igual 204L.
- Desktop Vomero guide: width `1376`, left `32` — igual 204L.
- Mobile render: sem Liquid error, 1 H1, hero e guide presentes.
