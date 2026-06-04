# Approval Packet — LK-GOC Standard v1 204L DEV → Production

Data UTC: 20260603T162846Z

## Pedido
Aprovação separada para, depois de QA visual humano, promover para Production as mudanças feitas em DEV no padrão LK-GOC v1.

## Escopo aprovado e executado em DEV
Tema DEV: `156623372510`
Role: `unpublished`
Nome: `LK Curadoria Force Fix Preview 2026-06-03`

Assets DEV migrados:
- `sections/lk-collection.liquid`
- `sections/lk-nb204l-guide-lkgoc.liquid`

## O que mudou
### Collection 204L
- Migração para namespace `lk-goc-*`.
- Remoção do namespace transitório `lk-lkgoc-*` do bloco 204L renderizado.
- Preservação de `lk-204l-*` como legado visual.
- JS mantém seletores `lk-goc-*` + `lk-204l-*`.

### Guia 204L completo
- Adição do contrato `lk-goc-guide-*`:
  - root;
  - hero;
  - sections;
  - grids/cards;
  - FAQ;
  - CTA.
- Remoção de `lk-lkgoc-*`.
- FAQ schema preservado.

## QA técnico realizado
Receipt principal:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-standard-v1-204l-collection-guide-dev-20260603T162613Z/RECEIPT.json`

Receipt guia isolado:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-standard-v1-guide-isolated-put-20260603T162732Z/checks.json`

Receipt preview QA:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-standard-v1-preview-qa-20260603T162802Z/preview-checks.json`

Resultados:
- Collection preview status 200.
- Guia preview status 200.
- `Liquid error` ausente.
- `imagem pendente` ausente.
- Collection renderiza `lk-goc-coll-preview--204l`.
- Guia renderiza `lk-goc-guide--new-balance-204l`.
- FAQ schema preservado no guia.

## Pendência antes do merge
- QA visual humano desktop/mobile nos previews DEV.

## Rollback
Arquivos before salvos nos receipts DEV:
- collection: receipt principal, `before__sections__lk-collection.liquid`
- guia: receipt principal/isolado, `before__sections__lk-nb204l-guide-lkgoc.liquid` ou `before.liquid`

## Risco
Baixo/médio:
- baixo para SEO/schema porque conteúdo e FAQ schema foram preservados;
- médio visual porque ainda falta QA visual humano mobile/desktop.

## Aprovação necessária
Aprovação explícita de Lucas para merge/promoção Production depois do QA visual.
