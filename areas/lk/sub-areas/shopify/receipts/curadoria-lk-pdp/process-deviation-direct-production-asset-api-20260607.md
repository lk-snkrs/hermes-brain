# Process deviation — direct Production Asset API instead of GitHub PR

Data UTC: 2026-06-07T19:54:36Z

## Contexto

Lucas perguntou: “O correto, não deveria ser no github?” após a limpeza AJ4 da Curadoria LK PDP ter sido aplicada em Production via Shopify Asset API.

## Reconhecimento

Sim. Para mudanças de tema/Liquid/CSS/JS/snippet/section em Production, o fluxo correto da LK Shopify é:

1. DEV/unpublished theme;
2. readback + QA;
3. GitHub branch/PR;
4. merge para `production`;
5. deploy/readback Shopify;
6. QA público;
7. receipt/rollback.

A execução anterior fez um write direto no asset Production via Shopify Asset API. Embora tenha sido escopada, aprovada para Production, com backup/readback/QA/receipt, isso foi uma divergência do processo preferido/correto porque pulou o registro GitHub/PR.

## Escopo afetado

- Theme Production: `lk-new-theme/production` / `155065417950` / role `main`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Mudança: remoção do handle indisponível `tenis-air-jordan-4-retro-military-blue-branco` do marker `top30-air-jordan-4-regular`
- Receipt original: `prod-aj4-unavailable-cleanup-20260607T180043Z/receipt.md`
- Commit receipt original: `042ecf7 docs(lk-shopify): record Production AJ4 curadoria cleanup`

## Estado técnico verificado na execução original

- Production target/readback SHA12: `811dbe5bdec7` / `811dbe5bdec7`
- Production before SHA12: `c64dafba4777`
- DEV inalterado: `aba2ed49b088`
- QA estático: arrays alinhados; handle exato removido ausente; bad URL/placeholder `0`
- QA público amostral: PDPs AJ4 retornaram 200, marker/Curadoria presentes nos controles, sem Liquid error

## Risco de processo

- GitHub pode ficar divergente do source real Shopify se o asset versionado não receber o mesmo diff.
- Próximo deploy via GitHub/theme pipeline pode reverter a limpeza se o repositório ainda contiver o handle removido.
- Auditoria/review ficou incompleta porque não houve PR antes do write Production.

## Correção recomendada

Fazer uma reconciliação GitHub/PR sem novo write em Shopify inicialmente:

1. localizar o repositório/branch fonte do tema `lk-new-theme/production`;
2. comparar o asset versionado com o readback Shopify Production atual;
3. criar branch com o mesmo diff cirúrgico se necessário;
4. abrir PR para `production` documentando que Shopify já contém o readback aprovado;
5. após merge, verificar que GitHub e Shopify continuam equivalentes;
6. não fazer novo deploy/write se o source Shopify já estiver correto, salvo se o pipeline exigir.

## Rollback operacional existente

Backup Production salvo em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-aj4-unavailable-cleanup-20260607T180043Z/production-before.liquid`

## Aprendizado

Para próximos casos: “Aprovo Production” em mudança de tema deve acionar o caminho GitHub PR/production branch, não write direto via Asset API, a menos que Lucas aprove explicitamente um hotfix direto/emergencial.
