# Receipt — tentativa de correção Alo/Crocs + rollback

Data: 2026-06-25  
Agente: `[LK] Otimização de Coleções` / LKGOC  
Aprovação: Lucas disse “seguir, pode faze” no turno atual.  
Writes externos: Shopify collection `descriptionHtml` para `alo-yoga-1` e `crocs-mcqueen`, depois rollback.  
values_printed: false

## Escopo aprovado/interpretação

Aplicar a correção preparada para reduzir duplicidade editorial em Alo Yoga e ajustar Crocs McQueen.

## O que foi feito

1. Backup Admin de `descriptionHtml` dos dois handles.
2. Aplicação dos payloads corrigidos via Shopify Admin GraphQL.
3. Readback Admin confirmou atualização:
   - `alo-yoga-1`: `updatedAt=2026-06-25T18:51:08Z`, payload continha correção.
   - `crocs-mcqueen`: `updatedAt=2026-06-25T18:51:09Z`, payload continha correção.
4. QA público detectou regressão de hierarquia:
   - Alo Yoga passou a mostrar bloco novo antes do grid e ainda mantinha bloco antigo depois do grid, gerando duplicidade pior.
   - Crocs McQueen passou a mostrar o bloco do guia antes de `1 itens/Ordenar`, violando regra LKGOC de pós-grid.
5. Rollback executado imediatamente usando backups do receipt.
6. QA público pós-rollback confirmou retorno ao estado anterior.

## Resultado final

**Rollback concluído. Produção voltou ao estado anterior à tentativa.**

Pós-rollback:

| Handle | HTTP | FAQPage | Liquid error | Novo payload ainda público? | Observação |
|---|---:|---:|---:|---:|---|
| `alo-yoga-1` | 200 | 1 | não | não | voltou ao estado anterior; ainda existe duplicidade leve já conhecida, mas pós-grid preservado. |
| `crocs-mcqueen` | 200 | 1 | não | não | voltou ao estado anterior; conteúdo principal `Como escolher Crocs McQueen` aparece depois de `Ordenar`. |

## Diagnóstico

A correção **não deve ser feita via `collection.descriptionHtml`** para esse caso. O tema renderiza parte da descrição no topo/hero da coleção, antes do grid, o que quebra o contrato LKGOC de pós-grid. A solução correta precisa ser em **theme/section pós-grid** ou fluxo `lk-shopify` com controle do template, não apenas body_html/descriptionHtml.

## Artefatos

- Tentativa/apply: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260625T-alo-crocs-lkgoc-lite-production-correction/apply-receipt.json`
- Rollback script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260625T-alo-crocs-lkgoc-lite-production-correction/rollback_restore_descriptionHtml.py`
- QA pós-rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260625T-alo-crocs-lkgoc-lite-production-correction/public-readback-after-rollback.json`

## Próximo passo correto

Handoff para `lk-shopify`/theme:

- criar seção pós-grid controlada para esses handles;
- não usar `descriptionHtml` como mecanismo de correção LKGOC;
- aplicar em DEV/branch;
- QA visual/DOM mobile+desktop;
- approval Lucas antes de production.

## Rollback

Rollback já executado e verificado. Backups permanecem no receipt da tentativa.
