# PRD LKGOC — Salomon XT-6

Criado em: 2026-06-15T14:47:45Z
Owner: [LK] Otimização de Coleções / LKGOC
Status: DEV_BUILD_ALLOWED / PRODUCTION_BLOCKED

## Pedido Lucas
Criar coleção e Guia LK para os 3 Salomon XT-6 usando o padrão LKGOC.

## Diagnóstico inicial
- Produtos novos existem como draft:
  - 9241776849118 — Tênis Salomon XT-6 Cloudburst Icy Pink Rosa Rosa
  - 9241776881886 — Tênis Salomon XT-6 Vanilla Ice Almond Milk Bege Bege
  - 9241776914654 — Tênis Salomon XT-6 Vanilla Ice Oxford Tan Bege Bege
- Existe uma coleção Shopify `Salomon XT-6` / handle `salomon-xt-6` / id `1128312635614`.
- Erro operacional: a coleção está `published_at=null`, template default/null e sem experiência LKGOC/Guia LK; para Lucas, na prática, não existe coleção utilizável/pública.
- Os produtos têm collects para essa coleção, mas continuam draft; nada está customer-facing.

## Escopo LKGOC correto
1. Usar Gold Source New Balance 204L como shell visual.
2. Collection LKGOC: hero curto + grid produto-first + teaser/ponte para guia.
3. Guia LK completo em `/pages/guia-salomon-xt-6`, não dentro da collection.
4. DEV/unpublished theme `lk-new-theme/dev` id `155065450718`, role verificado `unpublished`.
5. Production/main bloqueado até approval Lucas.

## Defaults aprovados para seguir sem perguntar
- Collection handle: `salomon-xt-6`.
- Guia handle: `guia-salomon-xt-6`.
- CTA collection → `/pages/guia-salomon-xt-6`.
- CTA guia → `/collections/salomon-xt-6`.
- Tom: premium, curadoria, outdoor urbano/gorpcore, autenticidade, atendimento humano.
- Sem linguagem pública de pronta entrega/estoque.

## Bloqueios de Production
- Falta QA visual side-by-side com 204L.
- Falta media manifest editorial/lifestyle/on-foot para hero.
- Produtos/coleção ainda draft/unpublished.
- Merge/promoção para production exige approval explícito.
