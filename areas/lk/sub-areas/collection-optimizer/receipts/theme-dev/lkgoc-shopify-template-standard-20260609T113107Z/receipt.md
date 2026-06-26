# Receipt — LKGOC Shopify template padrão

Data UTC: 20260609T113107Z

## Pedido Lucas
Replicar LKGOC na Shopify usando um template padrão de coleção otimizada, não criando layout do zero por coleção.

## Execução local/DEV branch
- Worktree: `/opt/data/worktrees/lk-new-theme-lkgoc-template-standard-20260609`
- Branch: `hermes/lkgoc-template-standard-20260609`
- Base: `origin/dev`

## Artefatos criados/alterados
- `templates/collection.lkgoc.json`
- `sections/lk-collection.liquid` — setting `lkgoc_template_mode`
- `reports/lkgoc-template-standard-20260609.md`

## Verificação realizada
- JSON do novo template validado localmente.
- Schema JSON de `sections/lk-collection.liquid` validado localmente.
- Todos os templates `collection*.json` parseados com sucesso após remoção do header comment Shopify.

## Bloqueios/limites
- `shopify theme check` foi tentado, mas ficou pendente e bateu timeout de 300s no ambiente local. Não houve substituição por resultado inventado.
- Nenhum write em Shopify/Production foi feito.

## Próximo passo
Fazer push/PR ou aplicar em tema DEV/unpublished para preview real, readback API e QA visual 204L side-by-side. Production só via approval Lucas + GitHub DEV → merge Production → deploy/promoção controlada.
