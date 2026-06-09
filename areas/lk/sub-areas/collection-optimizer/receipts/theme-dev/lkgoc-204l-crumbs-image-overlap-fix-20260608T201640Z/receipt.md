# LKGOC 204L — crumbs/image overlap fix — DEV/unpublished

Data: 2026-06-08T20:16:40Z
Solicitação Lucas: corrigir linha `.coll-banner__crumbs` que estava cortando/vazando sobre a imagem principal da Rosalía.

## Escopo
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role operacional: `unpublished`
- Arquivos alterados:
  - `layout/theme.liquid`
  - `snippets/lk-goc-collection.liquid` já continha o ajuste anterior de fonte/bottom image
- Coleção: `new-balance-204l`
- Produção: não alterada.

## Mudança principal
Adicionado override tardio em `layout/theme.liquid`, depois dos overrides globais do tema:

- Esconde `.coll-banner__crumbs` somente em página com `Contexto editorial New Balance 204L`.
- Remove `border-bottom` do `.coll-banner` nesse contexto.
- Reduz o pull vertical do collage desktop de `-34px` para `-18px` via override final.
- Reforça `object-position:center bottom!important` para a imagem principal (`.lk-goc-card--large img` / `.lk-204l-card--large img`) depois do CSS global que usava `center 24%`.

## Evidência
- `shopify theme push --theme 155065450718 --only layout/theme.liquid --only snippets/lk-goc-collection.liquid --allow-live=false` retornou sucesso para `lk-new-theme/dev`.
- Pull remoto do tema confirmou:
  - bloco `lk-goc-204l-crumbs-image-overlap-fix-20260608` presente em `layout/theme.liquid`;
  - `display:none!important` para `.coll-banner__crumbs`;
  - `translateY(-18px)!important` e `margin-bottom:-18px!important`;
  - override tardio `object-position:center bottom!important`;
  - snippet ainda contém ajustes de fonte e bottom image.

## Rollback
- Remover o bloco `<style id="lk-goc-204l-crumbs-image-overlap-fix-20260608">…</style>` de `layout/theme.liquid` e fazer push para o tema DEV.
- Backup pré-alteração salvo em `before__layout__theme.liquid`.
