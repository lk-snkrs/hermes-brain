# Receipt — LKGOC Puma Speedcat DEV Preview

Data: 2026-06-09
Tema DEV: `155065450718` / `lk-new-theme/dev`
Role verificado por API: `unpublished`

## Ações executadas em DEV
- Criado `templates/collection.puma-speedcat.json` no tema DEV.
- Atualizado `snippets/lk-goc-collection.liquid` com branch `puma-speedcat` para hero e guia pós-grid.
- Atualizado `sections/lk-collection.liquid` para renderizar `puma-speedcat` no shell LKGOC.
- Atualizado `templates/page.guia-puma-speedcat-lkgoc.json` com Guia LK completo.
- Página admin `/pages/guia-puma-speedcat` continuou unpublished; template_suffix ajustado para `guia-puma-speedcat-lkgoc` sem publicar.

## Preview Collection
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

## QA Collection
Playwright:
- mobile: role unpublished true; Liquid error false; hero true; guide true; productLinks 13; visibleBad false.
- desktop: role unpublished true; Liquid error false; hero true; guide true; productLinks 13; visibleBad false.
- pós-grid confirmado: guide começa depois do grid e depois do último produto.

## Page status
Template do Guia LK está criado em DEV, mas a página está unpublished. Preview público retorna 404. Publicar/ativar página é customer-facing e exige aprovação explícita.

## Evidências locais
- Collection HTML: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/collection-preview-readback.html`
- Page 404 readback: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/page-preview-readback.html`
- Screenshot collection mobile: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-mobile-20260609.png`
- Screenshot collection desktop: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-desktop-20260609.png`
- Screenshot guide mobile: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-guide-mobile-20260609.png`
- Screenshot guide desktop: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-lkgoc-20260609/speedcat-collection-guide-desktop-20260609.png`

## Rollback DEV
Reaplicar backups locais pré-execução salvos no output ou remover os assets novos:
- `templates/collection.puma-speedcat.json`
- branch `puma-speedcat` em `snippets/lk-goc-collection.liquid`
- render puma-speedcat em `sections/lk-collection.liquid`
- `templates/page.guia-puma-speedcat-lkgoc.json`
