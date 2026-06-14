Status: DRAFT / NÃO PUBLICADO
Owner: [LK] Otimização de Coleções
Data UTC: 20260613T095018Z
Coleção alvo: New Balance 2002R
Handle proposto: new-balance-2002r


# Approval Packet — New Balance 2002R LKGOC

## Pedido
Criar a nova coleção otimizada `New Balance 2002R` no padrão LKGOC, usando o Gold Source `New Balance 204L` como shell visual.

## O que já foi verificado
- Handle `new-balance-2002r`: não existe no Shopify no momento da checagem read-only.
- Handle `new-balance-2002r-protection-pack`: não existe.
- Existem PDPs relacionados encontrados por busca Shopify read-only, mas disponibilidade/grade não foi consultada nem validada para decisão; se necessário, handoff obrigatório para `lk-stock`.
- Tema DEV canônico: `lk-new-theme/dev`, ID `155065450718`, role `UNPUBLISHED`.
- Tema Production: `lk-new-theme/production`, ID `155065417950`, role `MAIN` — sem write direto.
- Demanda principal: `new balance 2002r` com 8.100 buscas/mês no Brasil e intenção transacional.
- SERP tem PAA e Popular Products; oportunidade é coleção + guia de escolha/autenticidade.

## Proposta de execução
1. Criar coleção `New Balance 2002R` com handle `new-balance-2002r`.
2. Aplicar regra/condição de coleção para produtos New Balance 2002R, preferencialmente por tag/metafield seguro e não por busca frágil.
3. Criar/ligar template LKGOC no DEV/unpublished copiando o shell 204L.
4. Adaptar apenas conteúdo, links, imagens e FAQ do 2002R.
5. Criar Guia LK pós-grid, depois de todos os produtos.
6. Inserir FAQPage schema coerente.
7. Rodar QA: readback, mobile/desktop, side-by-side 204L vs 2002R, DOM ordem produtos → guia.
8. Enviar preview para aprovação de Lucas.
9. Só depois de aprovação: merge/deploy via fluxo GitHub/Shopify controlado para Production.

## Decisões necessárias de Lucas
- Aprovar criação da coleção customer-facing `New Balance 2002R` em Production?
- Aprovar o handle `new-balance-2002r`?
- Confirmar se a coleção deve cobrir apenas `2002R` ou incluir explicitamente `Protection Pack` dentro da mesma coleção com subbloco editorial.
- Aprovar asset hero lifestyle/on-foot/editorial quando eu apresentar o media manifest.

## Risco
- Médio se a coleção for publicada sem asset editorial aprovado ou sem regra de produto robusta.
- Baixo para build DEV/unpublished: pode ser feito sem afetar cliente.
- Alto para Production sem QA visual: proibido pelo padrão LKGOC.

## Rollback
- DEV: restaurar assets/template/metafields de snapshot pré-build.
- Production: não executar sem snapshot, diff, aprovação e plano de reversão.
- Se coleção nova for criada em Production, rollback é despublicar/remover links da navegação e restaurar template/SEO/metafields anteriores, mantendo receipt.

## Status recomendado
`GO_DEV_PREVIEW` agora; `PRODUCTION_BLOCKED` até aprovação explícita de Lucas + asset hero + QA visual.
