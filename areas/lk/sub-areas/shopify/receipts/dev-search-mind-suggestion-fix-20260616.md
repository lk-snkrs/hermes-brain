# Receipt — DEV search suggestion fix: Nike Mind

Data: 2026-06-16
Perfil: lk-shopify
Escopo aprovado: corrigir busca Nike Mind em tema DEV somente

## Ação executada

Atualizado somente o asset Shopify DEV:

- Tema DEV: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `sections/lk-search.liquid`

Não houve alteração em:

- tema Production
- produto
- coleção
- preço
- estoque
- variante
- checkout
- tags/metafields
- campanhas/canais externos

## Mudança

1. Expandido o alias da coleção `Nike Mind 001 e 002` para capturar buscas conservadoras:
   - `mind`
   - `nike mind`
   - `nike mind 001`
   - `nike mind 002`
   - `mind 001`
   - `mind 002`
   - aliases existentes de Mind preservados

2. Adicionado guard específico para impedir que `nike mind` também puxe a coleção ampla `Nike` como segunda sugestão.

## Readback

- DEV antes: `b1063d65e2ca0f6dfbc0867443ec39f419e9a55b9c41247e02591d9c8a676e55`
- DEV após alias: `f90b2975becbb75e1e809724404ee6a0c6eadbe998c5caae4b82280f5213afbc`
- DEV final após guard: `85d7f5e7051a1f6890e1eae435e01551d0cbaf9feaec72fc9e5cbf91ac0393a0`
- Readback DEV bateu com target: sim
- Production antes/depois: `b1063d65e2ca0f6dfbc0867443ec39f419e9a55b9c41247e02591d9c8a676e55`
- Production unchanged: sim
- Secrets impressos: não (`values_printed=false`)

## QA DEV preview

Preview com cookie de tema DEV validou:

- `mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `mind 001` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `mind 002` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike` → `/collections/nike-todos-os-modelos` / `Nike`
- `vomero` → `/collections/nike-vomero-premium`
- `vomero 5` → `/collections/nike-vomero-5` + `/collections/nike-vomero-premium`
- `204l` → `/collections/new-balance-204l`
- `9060` → `/collections/new-balance-9060`
- `530` → `/collections/new-balance-530`

Todos os probes retornaram HTTP 200 e sem `Liquid error`.

## Artefatos

- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/search-mind-suggestion-fix-20260616.md`
- QA público inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/search-suggestion-visible-blocks.json`
- Readback alias: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/dev-mind-search-fix-apply-readback.json`
- Readback guard: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/dev-mind-search-nike-guard-readback.json`
- QA DEV final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/dev-preview-search-mind-fix-qa-v2.json`
- Asset DEV final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/dev-lk-search-after-mind-fix-final.liquid`

## Rollback

Para rollback DEV, restaurar `sections/lk-search.liquid` no tema `155065450718` a partir de:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/dev-lk-search-before-mind-fix.liquid`

Production não precisa de rollback porque não foi alterado.

## Próximo passo

Se Lucas aprovar Production, promover este mesmo diff de DEV para Production com fluxo seguro:

1. branch/PR a partir de Production atual;
2. aplicar somente o diff aprovado de `sections/lk-search.liquid`;
3. merge/promoção scoped;
4. readback Production;
5. QA público nas queries `mind`, `nike mind`, `nike`, `vomero`, `204l`, `9060`, `530`.
