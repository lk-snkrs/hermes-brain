# Receipt — LKGOC Nike Vomero Premium production promotion

Data: 2026-06-13 UTC
Aprovação: Lucas via Telegram — "ficou aprovado, fazer merge da dev para production"

## Escopo publicado
- Collection hero LKGOC Nike Vomero Premium
- Guia LK `/pages/nike-vomero-premium-guia`
- Guia padrão LKGOC/204L gold source com referências Vogue, Highsnobiety, Nike Newsroom e Hypebeast
- Bloco final mobile corrigido com 6 best sellers dinâmicos da coleção `nike-vomero-premium`

## GitHub
- PR DEV: #75 — merged into `dev`
- PR Production: #76 — merged into `production`
- Production merge commit: `ab89abe`
- Promotion branch: `promote/lkgoc-vomero-premium-production`

## Shopify
- Production theme: `155065417950` / `lk-new-theme/production`
- Deploy: `shopify theme push --allow-live --nodelete` limitado a 5 arquivos

## Arquivos publicados
- `sections/lk-collection.liquid`
- `sections/main-page.liquid`
- `snippets/lk-goc-nike-vomero-premium-hero-204l-clone.liquid`
- `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid`
- `snippets/lk-goc-nike-vomero-premium-guide-page.liquid`

## Evidência
- Backup production antes do deploy: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/production/vomero-premium-approved-20260613T205800Z`
- Readback production pós-deploy: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/production/vomero-premium-approved-readback-20260613T205951Z`
- Página pública guia validada: `gold-source-rebuild`, `6 best sellers`, `Vogue`, `Highsnobiety`, `Hypebeast`, sem `Liquid error`
- Coleção pública validada: bloco `lk-goc-coll-preview` e `Contexto editorial Nike Vomero Premium` presentes, sem `Liquid error`

## Rollback
1. Restaurar arquivos do backup `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/production/vomero-premium-approved-20260613T205800Z` para um worktree baseado em `production`.
2. Abrir PR rollback para `production`.
3. Após merge aprovado, `shopify theme push --theme 155065417950 --allow-live --nodelete --only` nos mesmos arquivos.

## Revisão de impacto
- D+7 sugerido: 2026-06-20
- Checar: sessões da coleção, cliques no guia, CTR orgânico, conversão PDP e comportamento mobile no bloco de best sellers.
