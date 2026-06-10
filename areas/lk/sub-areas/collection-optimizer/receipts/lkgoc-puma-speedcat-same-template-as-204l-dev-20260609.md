# Receipt — Puma Speedcat usando o mesmo template da collection 204L

Data: 2026-06-09

## Pedido Lucas
Refazer e colocar a Puma Speedcat como tema/template da collection na Shopify, usando o mesmo template da collection New Balance 204L.

## Correção aplicada
1. Releitura via Shopify Admin API:
   - `new-balance-204l` usa `template_suffix = ""` (template default da collection).
   - `puma-speedcat` estava usando `template_suffix = "puma-speedcat"`.
2. Alterei a collection Shopify Puma Speedcat para usar o mesmo template da 204L:
   - `template_suffix = ""`.
3. Refeito o LKGOC no **mesmo template default da 204L**, não em `view=lkgoc` e não em `collection.puma-speedcat`.

## Branch DEV
- Branch: `hermes/lkgoc-template-standard-20260609`
- Commit: `632255d Add Speedcat to default collection template like 204L`
- Push: realizado para GitHub.

## DEV Shopify
Aplicado em theme DEV/unpublished:
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`

Assets alterados no DEV:
- `sections/lk-collection.liquid`
  - adiciona hero Speedcat no mesmo template default usado pela 204L.
  - adiciona desc override Speedcat no mesmo mecanismo da 204L.
  - adiciona render do guide Speedcat no mesmo fluxo pós-grid.
- `snippets/lk-goc-puma-speedcat-guide-panel.liquid`
  - guide pós-grid Speedcat.

## Preview correto
Sem `view=lkgoc`:
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

## QA real — DEV preview
Speedcat mobile e desktop:
- roleUnpublished: true
- Liquid error: false
- viewLkgoc: false
- h1: Puma Speedcat
- hero: true
- hero aria: Contexto editorial Puma Speedcat
- guide: true
- guide id: lk-guia-puma-speedcat
- grid: true
- gridBeforeGuide: true
- texto herdado de New Balance/204L dentro da Speedcat: false
- texto Speedcat presente: true
- linguagem proibida estoque/pronta entrega: false

Comparativo 204L no mesmo DEV preview:
- hero 204L: true
- guide 204L: true
- gridBeforeGuide: true

## Evidências
- QA JSON: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-same-template-204l-20260609/qa_default_template_dev_result.json`
- Speedcat mobile: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-same-template-204l-20260609/speedcat-mobile-default-template-dev.png`
- Speedcat desktop: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-same-template-204l-20260609/speedcat-desktop-default-template-dev.png`
- 204L mobile comparativo: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-same-template-204l-20260609/nb204l-mobile-default-template-dev.png`

## Guardrail
Production theme/main não foi alterado. O objeto da collection Shopify Speedcat foi alterado para o mesmo template_suffix da 204L conforme pedido explícito.
