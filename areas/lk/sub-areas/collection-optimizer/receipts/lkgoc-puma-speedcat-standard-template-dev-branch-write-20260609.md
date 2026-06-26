# Receipt — LKGOC Puma Speedcat standard template / DEV branch write

Data: 2026-06-09

## Aprovação
Lucas aprovou write na branch DEV.

## Branch
- Repo: `lk-snkrs/lk-new-theme`
- Worktree: `/opt/data/worktrees/lk-new-theme-lkgoc-template-standard-20260609`
- Branch: `hermes/lkgoc-template-standard-20260609`
- Commit: `c653339 Fix LKGOC standard template flow for Speedcat`
- Push: realizado para `origin/hermes/lkgoc-template-standard-20260609`

## Correção conceitual
O erro anterior era tratar Puma Speedcat como template/classe/HTML próprio.

Correção aplicada:
- `templates/collection.lkgoc.json` permanece como template padrão de coleção otimizada.
- `sections/lk-collection.liquid` agora usa `section.settings.lkgoc_template_mode` como gatilho real para renderizar LKGOC.
- `snippets/lk-goc-collection.liquid` recebeu conteúdo específico da Speedcat dentro do componente compartilhado.
- Não foi criado `templates/collection.puma-speedcat.json` no branch.

## Assets alterados
- `sections/lk-collection.liquid`
  - hero LKGOC renderiza quando `section.settings.lkgoc_template_mode` está ativo.
  - guide LKGOC renderiza quando `section.settings.lkgoc_template_mode` está ativo.
- `snippets/lk-goc-collection.liquid`
  - adicionado branch `puma-speedcat` no hero.
  - adicionado branch `puma-speedcat` no guide.
  - conteúdo herdado de New Balance/204L removido dos blocos Speedcat.

## DEV Shopify aplicado
Também aplicado no tema DEV/unpublished:
- Theme ID: `155065450718`
- Theme name: `lk-new-theme/dev`
- Role: `unpublished`
- Assets enviados:
  - `templates/collection.lkgoc.json`
  - `sections/lk-collection.liquid`
  - `snippets/lk-goc-collection.liquid`

## Preview correto
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`

## QA real
Resultado estrito:
- DEV/unpublished: true
- Liquid error: false
- usa template custom `collection.puma-speedcat`: false
- hero Speedcat: true
- guide Speedcat: true
- grid: true
- grid antes do guide: true
- texto New Balance/204L herdado no hero Speedcat: false
- texto New Balance/204L herdado no guide Speedcat: false
- linguagem proibida estoque/pronta entrega: false

Evidências:
- `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/qa_view_lkgoc_strict_result.json`
- `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/speedcat-mobile-view-lkgoc.png`
- `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-template-standard-fix-20260609/speedcat-desktop-view-lkgoc.png`

## Guardrail
Production/main não foi alterada. Collection object `template_suffix` também não foi alterado.
