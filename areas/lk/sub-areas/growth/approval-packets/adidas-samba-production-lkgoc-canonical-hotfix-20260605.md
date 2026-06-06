# Approval packet — Adidas Samba Production LKGOC canonical hotfix

Data: 2026-06-05T18:36:19

## Correção de rota
O packet anterior que sugeria subir `lk-samba-204l-*` foi marcado como **SUPERSEDED — NÃO EXECUTAR**.

Lucas corrigiu corretamente: Adidas Samba deve seguir o padrão padronizado **LK-GOC**, não snippets legados `lk-samba-204l-*`.

## Problema atual em Production
URL: `https://lksneakers.com.br/collections/adidas-samba?readmore_fix=1`

O tema Production `155065417950` está com `sections/lk-collection.liquid` renderizando nomes antigos:
- `lk-samba-204l-hero-v2`
- `lk-samba-204l-guide-v2`

Esses snippets estão ausentes em Production, causando Liquid error visível.

## Correção correta proposta
1. Subir o snippet canônico do DEV para Production:
   - `snippets/lk-goc-adidas-samba.liquid`
2. Alterar Production `sections/lk-collection.liquid` somente nos renders da Adidas Samba:
   - Hero: `render 'lk-goc-adidas-samba', part: 'hero'`
   - Guide: `render 'lk-goc-adidas-samba', part: 'guide'`
3. Não subir `lk-samba-204l-*`.

## Arquivos candidatos preparados
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/candidate/sections/lk-collection.liquid`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/candidate/snippets/lk-goc-adidas-samba.liquid`

## Validações locais do candidate
- refs antigas no section candidato: `0`
- refs novas `lk-goc-adidas-samba`: `2`
- snippet canônico presente e com comentário: `Namespace: lk-goc-* only`

## Escopo
- Production theme write: sim, exige aprovação explícita do Lucas.
- Sem alteração de preço/produto/checkout/campanha/metafields.
- Correção restrita a Liquid/snippet da coleção Adidas Samba.

## Rollback
- Restaurar `sections/lk-collection.liquid` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/prod/sections/lk-collection.liquid`.
- Remover/ignorar `snippets/lk-goc-adidas-samba.liquid` se necessário.

## QA pós-apply obrigatório
- URL production sem `Liquid error`.
- Hero renderizando `.lk-goc-coll-preview--adidas-samba`.
- Guia renderizando `#lk-guia-adidas-samba` / `.lk-goc-guide-panel`.
- `.coll-rich-content` legado ausente se coleção estiver optimized.
- Desktop: “Ler mais” não visível se regra LKGOC desktop se aplicar ao componente.
- Screenshot desktop/mobile.
