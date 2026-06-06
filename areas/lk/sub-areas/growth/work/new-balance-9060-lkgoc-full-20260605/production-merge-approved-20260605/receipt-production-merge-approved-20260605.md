# Receipt — New Balance 9060 Full LKGOC Production Merge

Data/hora: 2026-06-05T12:20:56.483060
Aprovação: Lucas via Telegram — "Aprovo para a Production fazer merge"

## Tema
- Production theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role verificado antes do write: `main`
- DEV source: `lk-new-theme/dev` / `155065450718` / `unpublished`

## Assets alterados em production
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-204l-guide-panel.liquid`
- `snippets/lk-goc-new-balance-9060-guide-panel.liquid`
- `snippets/lk-goc-new-balance-9060-hero-204l-clone.liquid`
- `snippets/lk-goc-guide-contract.liquid`
- `snippets/lk-goc-title-headline-contract.liquid`
- `snippets/lk-goc-title-headline-contract-v2.liquid`

## Backups / rollback local
- Production before section: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-9060-lkgoc-full-20260605/production-merge-approved-20260605/prod-before__sections__lk-collection.liquid`
- Candidate final section: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-9060-lkgoc-full-20260605/production-merge-approved-20260605/prod-candidate-v3__sections__lk-collection.liquid`
- PUT response: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-9060-lkgoc-full-20260605/production-merge-approved-20260605/put-production-merge-response.json`

## Observações técnicas
- Shopify recusou inicialmente seção acima de 256KB. Correção: contratos CSS movidos para snippets renderizados e seção mantida abaixo do limite.
- Readback Admin API confirmou assets finais no theme production.
- Edge/cache pública apresentou alternância temporária entre HTML antigo e novo durante QA pós-merge. Isso parece propagação/cache Shopify/CDN, não erro de asset: o readback Admin API contém o código final.

## Rollback
Restaurar `sections/lk-collection.liquid` usando `prod-before__sections__lk-collection.liquid` e remover/ignorar snippets novos, se necessário.

## Revisão de impacto
Agendar revisão em ~7 dias: GSC/GA4/Shopify para collection `new-balance-9060`.
