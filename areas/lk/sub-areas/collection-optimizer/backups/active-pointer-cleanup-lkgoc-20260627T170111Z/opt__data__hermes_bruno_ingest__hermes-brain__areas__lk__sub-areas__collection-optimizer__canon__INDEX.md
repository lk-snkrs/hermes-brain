# LKGOC Canon Index — Collection Optimizer

Atualizado: 20260627T165047Z
Status: **canônico operacional para o profile `lk-collection-optimizer`**.

## Regra de ownership

`[LK] Otimização de Coleções` / `lk-collection-optimizer` é o dono lógico e operacional do LKGOC.

Os documentos `LKGOC-*` foram migrados fisicamente para `areas/lk/sub-areas/collection-optimizer/`. Arquivos remanescentes em `growth/LKGOC-*` são apenas redirects legados, não fonte primária. Quando houver conflito:

1. Esta camada `collection-optimizer` define ownership, handoffs e guardrails de execução LKGOC.
2. A suite `collection-optimizer/LKGOC-*` continua sendo fonte canônica de conteúdo/contrato até migração física completa.
3. Regras novas de `collection-optimizer/rules/` vencem wording antigo que bloqueie DEV/unpublished ou trate Growth como dono.
4. Production/main/customer-facing sempre exige aprovação explícita Lucas + rollback + readback + receipt.

## Ordem obrigatória de leitura para execução LKGOC

1. `collection-optimizer/MAPA.md`
2. `collection-optimizer/canon/INDEX.md` este arquivo
3. `collection-optimizer/rules/LKGOC-DEV-PRODUCTION-PRECEDENCE.md`
4. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-PADRAO-CANONICO.md`
5. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-PRD.md`
6. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-INPUT-CONTRACT.md`
7. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-EVIDENCE-PACKET.md`
8. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-EXECUTION-WORKFLOW.md`
9. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-SCORECARD-100.md`
10. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-MAPA-JA-FEITO.md`
11. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`
12. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-QA-SCREENSHOT-STANDARD.md`
13. `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-THEME-TARGET-CONTEXT.md`
14. Playbook aplicável em `collection-optimizer/playbooks/`
15. Workdir/receipt/approval packet da coleção alvo

## Artefatos canônicos físicos em `collection-optimizer/`

- `LKGOC-PADRAO-CANONICO.md`
- `LKGOC-STANDARD-V1-LK-GOC.md`
- `LKGOC-PRD.md`
- `LKGOC-INPUT-CONTRACT.md`
- `LKGOC-EVIDENCE-PACKET.md`
- `LKGOC-EXECUTION-WORKFLOW.md`
- `LKGOC-SCORECARD-100.md`
- `LKGOC-IMPACT-REVIEW.md`
- `LKGOC-MAPA-JA-FEITO.md`
- `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`
- `LKGOC-QA-SCREENSHOT-STANDARD.md`
- `LKGOC-THEME-TARGET-CONTEXT.md`

## Handoffs obrigatórios

- Growth amplo/GA4/GSC/GMC/paid/influencer/PageSpeed/SEO técnico amplo → `lk-growth`.
- Produto novo/PDP/theme geral/collection object/metafields/tags/deploy técnico → `lk-shopify`.
- Estoque, disponibilidade, pronta entrega, grade/tamanho, Tiny/Shopify stock, ruptura/reposição → `lk-stock`.

## Shopify e produção

- Shopify Admin GraphQL read-only: usar CLI oficial `/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'`.
- Mutations/Admin write direto: bloqueado por padrão; exceção só com aprovação escopada.
- DEV/unpublished/branch: permitido para preview/QA quando role/target for verificado e o trabalho estiver marcado como draft/preview.
- Production/main/customer-facing: bloqueado sem aprovação explícita atual, rollback, readback e receipt.

## Namespace

- Novas classes estruturais LKGOC: `lk-goc-*`.
- `lk-204l-*`, `lk-lkgoc-*` e `lk-collection-v2` são gold source/compatibilidade/transição, não namespace preferencial novo.


## Redirects legados em `growth/`

Os arquivos `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/LKGOC-*` foram substituídos por stubs de redirect para preservar links/workers antigos. Novas leituras e writes canônicos devem usar `collection-optimizer/LKGOC-*`.
