# Handoff — CRO Collection → PDP — Onitsuka/Lululemon — 2026-06-10

Destino: **[LK] Otimização de Coleção**
Origem: LK Growth — rotina semanal read-only CRO/PDP Funnel Review
Status: preview/handoff; **sem write externo**.

## Por que existe handoff

A rotina semanal de CRO/PDP detectou que parte do gargalo mobile está em **Collection → PDP / decisão pré-carrinho**, mas não deve executar LKGOC automaticamente.

## Alvos

1. `/collections/onitsuka-tiger-todos-os-modelos`
   - GA4 mobile 7d: 244 sessões, 6 add_to_cart, 0 checkout, 0 purchase.
   - Decision refresh: P1 comercial; 803 unidades combinadas e R$ 1.931.932,01 em vendas combinadas para priorização.
2. `/collections/lululemon`
   - GA4 mobile 7d: 187 sessões, 5 add_to_cart, 0 checkout, 0 purchase.
   - Decision refresh: P1 comercial; 51 unidades combinadas e R$ 64.199,49 em vendas combinadas para priorização.

## Hipótese

O usuário chega à coleção mobile, vê produtos/preço/filtros, mas a decisão para entrar no PDP certo ou avançar ao carrinho ainda está fraca. QA público detectou filtros/linguagem de disponibilidade/estoque que podem gerar ruído com o guardrail LK.

## Pedido para o especialista

Preparar apenas **avaliação/preview DEV** de UX collection/cards/filtros/ordenação, sem produção:

- manter coleção product-first;
- não iniciar LKGOC textual/guia sem decisão separada;
- verificar se `Disponibilidade / Em estoque` está visualmente dominante e se há alternativa premium/menos operacional;
- avaliar cards/fotos/preço/filtros/ordenação no mobile;
- propor microteste com métrica: collection landing → PDP click/select_item e add_to_cart/session.

## Guardrails

- Não usar estoque/pronta entrega/encomenda como taxonomia pública.
- Não executar write Shopify/theme/collection sem aprovação explícita atual de Lucas.
- Produção bloqueada.
- Qualquer LKGOC/guia/coleção otimizada deve seguir o canônico LKGOC e padrão 204L/Moon Shoe.

## Evidência completa

Relatório Growth: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/weekly/lk-cro-pdp-funnel-review-2026-06-10.md`
