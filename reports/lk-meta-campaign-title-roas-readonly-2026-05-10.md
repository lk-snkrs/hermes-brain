# LK Meta Campaign Title ROAS — read-only — 2026-05-10

Período: `2025-12-01` a `2026-05-10`. Modo read-only.

## Como ler
- **Meta attributed ROAS por título de campanha** = `Meta action_values / Meta spend`, agrupado no nível `campaign_name`. É o ROAS que o Meta reporta por título.
- **Shopify UTM ROAS encontrado** = receita Shopify web de pedidos cujo `utm_campaign` bateu de forma estrita com o título da campanha Meta. Esse é mais operacional, mas só aparece quando o UTM está bem gravado.
- Removi matching frouxo por `contains` porque ele confundia campanhas genéricas como `Pareto.Vendas [Masculino]` com UTMs de Helena/Dia das Mães.
- Se Shopify UTM estiver zerado, não significa que a campanha não vendeu; significa que não encontrei evidência direta por título/UTM nesse recorte.

## Totais
- Campanhas Meta lidas: **8**
- Spend Meta por campanhas: **R$ 190.469,81**
- Valor Meta atribuído por campanhas: **R$ 11.457.768,12**
- Shopify web revenue no período: **R$ 4.423.457,58**

## Top campanhas por spend — Meta title ROAS vs Shopify evidence
### Pareto.Vendas-Adv [ Geral]
- Família: `advantage/broad`
- Spend Meta: **R$ 62.523,72**; compras Meta: **1503**; valor Meta: **R$ 3.863.919,30**; Meta attributed ROAS: **61.80x**
- Shopify UTM match estrito: pedidos **0**; receita **R$ 0,00**; ROAS Shopify/Meta spend: **0.00x**

### [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)
- Família: `advantage/broad`
- Spend Meta: **R$ 36.296,67**; compras Meta: **771**; valor Meta: **R$ 2.542.659,81**; Meta attributed ROAS: **70.05x**
- Shopify UTM match estrito: pedidos **3**; receita **R$ 10.799,98**; ROAS Shopify/Meta spend: **0.30x**
  - UTM `[PD][FUNDO] ADV  (antiga Simples | Vendas Advantage )`: 3 pedidos / R$ 10.799,98 (exact_full)
  - 1x Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege | 1183A872.101-3 | 36
  - 1x Tênis New Balance 204L Mushroom Arid Stone Marrom | U204LMMA-4 | 37
  - 1x Tênis New Balance 530 'Silver Metallic Black Cement' Prateado | U530ESA-9 | 42
  - 1x New Balance 9060 Black Cement "Black Cat" Preto | U9060ZGE | 37
  - 1x Tênis Adidas Samba OG Crochet Pack Sand Strata Bege | JR9446-3 | 36

### [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )
- Família: `remarketing`
- Spend Meta: **R$ 32.274,10**; compras Meta: **783**; valor Meta: **R$ 2.320.329,06**; Meta attributed ROAS: **71.89x**
- Shopify UTM match estrito: pedidos **6**; receita **R$ 18.489,97**; ROAS Shopify/Meta spend: **0.57x**
  - UTM `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )`: 6 pedidos / R$ 18.489,97 (exact_full)
  - 1x Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege | 1183C015101-14 | 42.5
  - 1x Tênis Onitsuka Tiger Tiger Corsair A55 Midnight Cream Azul | 1183C317-401-10 | 43
  - 1x Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | 1183B566021-4 | 37
  - 1x Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | None | 35.5
  - 1x Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | None | 43

### Pareto.lancamento.Jacquemus
- Família: `other`
- Spend Meta: **R$ 17.853,12**; compras Meta: **285**; valor Meta: **R$ 1.218.679,74**; Meta attributed ROAS: **68.26x**
- Shopify UTM match estrito: pedidos **0**; receita **R$ 0,00**; ROAS Shopify/Meta spend: **0.00x**

### [PD][MEIO] TRAF (antiga Simples | Tráfego)
- Família: `other`
- Spend Meta: **R$ 17.397,13**; compras Meta: **3**; valor Meta: **R$ 7.125,00**; Meta attributed ROAS: **0.41x**
- Shopify UTM match estrito: pedidos **0**; receita **R$ 0,00**; ROAS Shopify/Meta spend: **0.00x**

### [Pareto] [FUNDO] DABA
- Família: `other`
- Spend Meta: **R$ 16.526,39**; compras Meta: **444**; valor Meta: **R$ 1.037.493,36**; Meta attributed ROAS: **62.78x**
- Shopify UTM match estrito: pedidos **15**; receita **R$ 41.027,24**; ROAS Shopify/Meta spend: **2.48x**
  - UTM `[PD] [FUNDO] DABA`: 15 pedidos / R$ 41.027,24 (exact_norm)
  - 1x Camisa Aphase Check - Light Yellow Bege | 20054-3 | L/G
  - 1x Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege | 1183C015-202-9 | 42
  - 1x Tênis Onitsuka Tiger California 78 EX Monument Blue Cream Azul | 1183A355.405-8 | 41
  - 1x Tênis New Balance 530 White Natural Indigo Branco | MR530SG-3 | 37
  - 1x Tênis Nike Moon Shoe SP Jacquemus Off White | None | 38

### Pareto.Vendas [Masculino]
- Família: `other`
- Spend Meta: **R$ 5.203,60**; compras Meta: **120**; valor Meta: **R$ 467.561,85**; Meta attributed ROAS: **89.85x**
- Shopify UTM match estrito: pedidos **0**; receita **R$ 0,00**; ROAS Shopify/Meta spend: **0.00x**

### [PD] [TOPO] Alcance Loja Física (antiga Simples | Alcance - Loja e Bairros)
- Família: `other`
- Spend Meta: **R$ 2.395,08**; compras Meta: **0**; valor Meta: **R$ 0,00**; Meta attributed ROAS: **0.00x**
- Shopify UTM match estrito: pedidos **0**; receita **R$ 0,00**; ROAS Shopify/Meta spend: **0.00x**

## Próxima correção necessária
Para fechar ROAS operacional por título de campanha, a LK precisa de um dicionário de campaign naming/UTM: `campaign_name Meta → utm_campaign Shopify/GA4 → criativo/influencer/produto esperado`. Sem isso, o Meta title ROAS serve como diagnóstico de plataforma; o Shopify UTM match estrito serve como verdade parcial.
