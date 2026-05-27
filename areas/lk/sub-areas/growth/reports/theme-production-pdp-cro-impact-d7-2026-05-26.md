# LK Theme Production PDP CRO — Impact Review D+7

Data da revisão: 2026-05-26T15:32Z  
Mudança revisada: produção Shopify `lk-new-theme/production`, theme ID `155065417950`, asset `sections/lk-pdp.liquid`, promovida em 2026-05-19.  
Receipt base: `areas/lk/sub-areas/growth/reports/theme-production-pdp-cro-promotion-2026-05-19.md`.

## Escopo e guardrails

- Tipo: revisão de impacto CRO/PDP D+7.
- Ações executadas: somente leitura read-only em GA4, GSC, Shopify Admin GraphQL e storefront público.
- Writes: 0.
- Não executado: Shopify/theme write, produto, preço, estoque, campanha, Klaviyo, Merchant Center, atendimento ou qualquer envio externo.

## Página representativa

`https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto`

Validação storefront sem `preview_theme_id`:

- URL testada: `https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto?lkprodqa=20260526D7mobile`.
- Viewport mobile em Chromium headless: `390 × 844`, user agent iPhone.
- `preview_theme_id`: ausente.
- `COMPRE JÁ`: visível; botão `350.19 × 50`, `display=block`, `visibility=visible`, `opacity=1`.
- `ADICIONAR AO CARRINHO`: visível; `350.19 × 52`.
- Trust grid: visível; bloco com Google, Autenticidade, Parcele em, Loja Física renderizado em grid `350.19 × 52`.
- Aviso: `Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp` presente e visível.
- Observação: no mobile, a leitura DOM encontrou no bloco visível Google/Autenticidade/Parcele/Loja; não encontrou `Troca grátis` e `Atendimento humano` dentro do bloco de trust mobile visível. Isso não bloqueia o CTA, mas vale revisar se a intenção era manter todos os selos no mobile.

## Janelas comparadas

- Baseline: 2026-05-12 a 2026-05-18.
- Pós-mudança GA4/Shopify: 2026-05-19 a 2026-05-25.
- Pós-mudança GSC: 2026-05-19 a 2026-05-23, por latência usual do Search Console.

## GA4 — PDP representativa

Fonte: GA4 Data API read-only, dimensão `pagePath=/products/tenis-adidas-samba-jane-black-white-gum-preto`.

| Métrica | Baseline | Pós | Variação |
|---|---:|---:|---:|
| Sessions | 38 | 32 | -15,8% |
| Total users | 35 | 32 | -8,6% |
| Screen page views / view_item | 66 | 36 | -45,5% |
| User engagement duration | 390s | 160s | -59,0% |
| Add_to_cart | 1 | 1 | estável |
| Add_to_cart / view_item | 1,52% | 2,78% | melhora nominal, amostra baixa |

Interpretação: queda de tráfego/visualizações na PDP, mas o evento de carrinho não caiu. Como a amostra é pequena, a melhora de taxa é direcional, não conclusiva.

## Shopify — pedidos da PDP representativa

Fonte: Shopify Admin GraphQL read-only; produto encontrado por handle.

| Métrica | Baseline | Pós |
|---|---:|---:|
| Pedidos escaneados na loja | 85 | 91 |
| Pedidos contendo o produto | 0 | 1 |
| Quantidade vendida do produto | 0 | 1 |
| Receita de linha do produto | R$ 0,00 | R$ 1.199,99 |

Interpretação: houve 1 venda da PDP representativa no período pós-mudança contra zero na semana anterior. É um sinal positivo, mas não prova causalidade isolada da alteração de tema.

## GSC — PDP representativa

Fonte: Search Console read-only `sc-domain:lksneakers.com.br`, filtro exato de página.

| Métrica | Baseline | Pós parcial |
|---|---:|---:|
| Cliques | 0 | 0 |
| Impressões | 97 | 79 |
| CTR | 0% | 0% |
| Posição média | 3,74 | 4,67 |

Interpretação: sem anomalia de indexação/renderização detectada; a página continua com impressões. Não há clique orgânico nas duas janelas. A leve piora de posição/impressões deve ser tratada como ruído/variação de demanda, não como efeito esperado de CRO.

## Conclusão executiva

- A mudança segue funcional em produção: `COMPRE JÁ`, botão de carrinho, trust area e aviso continuam renderizando sem `preview_theme_id` em PDP pública.
- Não encontrei sinal de quebra de conversão: add_to_cart ficou estável na PDP testada e houve 1 pedido do produto no pós-mudança.
- O tráfego da PDP caiu no pós, então o impacto de conversão ainda não é decision-grade por volume.
- Principal anomalia a revisar: no mobile, o trust grid visível parece mostrar Google/Autenticidade/Parcele/Loja, mas não todos os selos esperados (`Troca grátis` e `Atendimento humano`) no bloco visível. Não exige rollback; é candidato a QA visual em dev theme.

## Recomendação

- Manter a mudança em produção; não há evidência para rollback.
- Abrir ajuste/QA pequeno em dev theme para confirmar se todos os trust blocks devem aparecer no mobile ou se a simplificação atual é intencional.
- Reavaliar em +7 dias com mais volume, idealmente agregando 10–20 PDPs afetadas pelo mesmo componente, não apenas a PDP representativa.
