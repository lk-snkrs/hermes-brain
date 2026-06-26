# Receipt — LKGOC coll-rich-content guard

Data: 2026-06-05T17:55:31

## Executado
- Regra LKGOC criada: remover/ocultar `.coll-rich-content` legado em coleções LKGOC.
- Tema DEV `155065450718` (`lk-new-theme/dev`, role unpublished) atualizado.
- Tema Production `155065417950` (`lk-new-theme/production`, role live/main) atualizado após comando "seguir".
- Arquivo alterado: `sections/lk-collection.liquid`.

## Guard aplicado
A renderização do bloco legado agora exige:
- coleção não ter `custom.lkgoc_status = optimized`;
- handle não ser um dos LKGOC conhecidos: `new-balance-204l`, `new-balance-9060`, `new-balance-530`, `onitsuka-tiger-mexico-66`.

## Backups
- DEV backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/before__sections__lk-collection__dev-155065450718__20260605T174736.liquid`
- Production backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/before__sections__lk-collection__production-155065417950__20260605T175028.liquid`

## Readback
- Production readback confirmou guard no arquivo.
- Tamanho final production: abaixo de 256KiB.

## QA público
- 530, 204L e Mexico 66: sem div legado nas leituras públicas.
- 9060: código/readback corrigido; leituras públicas alternaram entre resposta nova sem legado e resposta antiga com legado, indicando cache/edge Shopify ainda propagando.

## Evidências
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/qa-preview-html-div-no-coll-rich-results.json
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/receipt-production-coll-rich-guard-qa-curl-20260605.json
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/receipt-production-9060-after-edge-touch-20260605.json
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/production-candidate-coll-rich-guard-report.json

## Próximo se persistir no browser do Lucas
Se a 9060 continuar mostrando "Perguntas Frequentes" antigo depois de limpar cache/aguardar propagação, executar plano B: remover o FAQ legado da descrição/metafield da coleção ou aplicar bypass de cache por atualização de recurso de coleção, com rollback.
