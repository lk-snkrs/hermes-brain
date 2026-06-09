# Receipt — LKGOC PR39 merge dev + Shopify DEV preview

Data UTC: 20260608T154813Z
Status: Merge em dev e push para Shopify DEV/unpublished concluídos

## Decisão operacional Lucas
Lucas instruiu: merge em dev deve ser feito pelo agente sozinho para esse fluxo.

## GitHub
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/39
- Branch origem: `hermes/204l-mobile-gold-fix-20260608`
- Base: `dev`
- Merge commit em dev: `c117b8d`
- Commits incluídos:
  - `130ac40` — improve NB 204L mobile gold hero
  - `807f478` — polish NB 204L mobile gold source

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado no HTML preview: `unpublished`
- Push executado apenas nos arquivos alterados do PR.
- Production/main não foi alterado.

## Preview
- Home preview: https://lk-sneakerss.myshopify.com?preview_theme_id=155065450718
- Coleção 204L preview: https://lk-sneakerss.myshopify.com/collections/new-balance-204l?preview_theme_id=155065450718

## Verificação
- `shopify theme push`: sucesso para `lk-new-theme/dev` (#155065450718)
- Fetch preview confirmou:
  - `Shopify.theme.name`: `lk-new-theme/dev`
  - `Shopify.theme.id`: `155065450718`
  - `Shopify.theme.role`: `unpublished`
  - `Shopify.previewMode`: `true`
