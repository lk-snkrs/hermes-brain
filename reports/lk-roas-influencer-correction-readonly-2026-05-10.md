# LK ROAS Influencer Correction — read-only — 2026-05-10

Período investigado: `2025-12-01` a `2026-05-10`.
Modo: read-only. Nenhuma alteração em Meta, Google, Shopify, Tiny, campanhas, orçamentos, Notion ou WhatsApp.

## Diagnóstico
O ROAS de 50–70x de Lala/Helena/Silvia **não deve ser usado como ROAS real da LK**. Ele é valor atribuído pelo Meta a anúncios com nome de influencer, dentro de campanhas broad/Advantage+/remarketing. A correção é separar três coisas: custo/exposição Meta, receita Shopify comprovada, e ROAS operacional reconciliado.

## Sanity check do período
- Shopify web revenue: **R$ 4.423.457,58**.
- Meta spend conta inteira: **R$ 190.458,60**.
- Google Ads spend via Metricool: **R$ 123.816,30**.
- Spend pago consolidado simples: **R$ 314.274,90**.
- Site ROAS simples, Shopify web / Meta+Google: **14.08x**.
- Valor atribuído pelo Meta conta inteira: **R$ 11.457.768,12**.
- Meta platform value / Shopify web revenue: **2.59x**.

Leitura: o Meta atribui mais valor do que a receita web total do Shopify no mesmo período. Isso sozinho prova que platform value não pode ser tratado como verdade operacional.

## Meta Ads — influencers, 1d_click
- **Lala Noleto**: spend R$ 25.750,26; compras Meta 519; valor Meta R$ 1.686.413,85; ROAS plataforma 65.49x; ads matched 19.
- **Helena Lunardelli**: spend R$ 24.364,51; compras Meta 627; valor Meta R$ 1.720.526,49; ROAS plataforma 70.62x; ads matched 28.
- **Silvia Heinz**: spend R$ 50.311,49; compras Meta 822; valor Meta R$ 2.560.642,92; ROAS plataforma 50.90x; ads matched 33.

## Shopify — evidência direta encontrada
- **Lala Noleto**: pedidos web com cupom/UTM/landing/referrer/note textual: **0**; receita Shopify com evidência: **R$ 0,00**; evidências: `{}`.
- **Helena Lunardelli**: pedidos web com cupom/UTM/landing/referrer/note textual: **37**; receita Shopify com evidência: **R$ 154.482,04**; evidências: `{'note_attributes': 27, 'discount_code': 4, 'landing_site': 15}`.
  - 2x Jason Markk Repel Spray Impermeabilizante | JM3 | None
  - 2x Slide Nike Mind 001 Black Chrome Preto | HQ4307-001-10 | 43
  - 2x Tênis New Balance 204L Arid Timberwolf Bege | U204LMMC-5 | 38
  - 1x Tênis adidas Samba Og Supplier Colour Off White Gum Prata | JI4219-4 | 37
  - 1x Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | 1183C102751-2 | 35
  - 1x Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | 1183C102751-3 | 36
  - 1x Tênis Onitsuka Tiger Mexico 66 SD Vin Clay Canyon Cream Marrom | 1183C015.205-3 | 36
  - 1x Tênis New Balance 9060 Sea Salt Concrete Branco | U9060ECA-10 | 40
- **Silvia Heinz**: pedidos web com cupom/UTM/landing/referrer/note textual: **209**; receita Shopify com evidência: **R$ 650.658,20**; evidências: `{'discount_code': 208, 'landing_site': 2, 'note_attributes': 1}`.
  - 11x Jason Markk Repel Spray Impermeabilizante | JM3 | None
  - 9x Jason Markk Essential Kit de Limpeza | 300110 | None
  - 5x Tênis New Balance 204L Arid Timberwolf Bege | U204LMMC-3 | 36
  - 5x Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege | 1183C123.252-4 | 37
  - 3x Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege | 1183C123.252-6 | 39
  - 3x Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto | HV8547-001-8 | 41
  - 3x Tênis Nike Moon Shoe SP Jacquemus Medium Brown | HV8547-200-38 | 38
  - 3x Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege | 1183C123.252-7 | 40

## Causa provável do erro
- O cálculo anterior fez `valor atribuído Meta / spend Meta` por anúncio com nome de influencer.
- Muitos anúncios estão dentro de estruturas broad/Advantage+/RMKT; o Meta dá crédito para compras que podem ter vindo por outras jornadas.
- `action_values` do Meta é atribuição, não receita contábil. Pode ultrapassar a receita Shopify porque há sobreposição, janela de atribuição e créditos por clique/view.
- Para Lala, Shopify não mostrou evidência textual direta por cupom/UTM/landing no recorte lido; logo não dá para afirmar produto/receita real da Lala sem dicionário/cupom/UTM correto.
- Silvia e Helena têm evidência Shopify direta, mas ainda precisa deduplicar e conectar ao custo correto antes de falar em ROAS operacional.

## Correção operacional
1. Trocar `ROAS Influencer Meta` por `Meta attributed ROAS` com selo de alerta.
2. Criar `ROAS Operacional Influencer` só quando houver Shopify evidence: cupom, UTM, landing/referrer, note_attributes, produto/tamanho vendido.
3. Criar dicionário canônico de influencers: nome, grafias, handles, cupons, UTMs, campaign/adset/ad patterns e janelas reais de campanha.
4. Para decisão de estoque, usar tabela: `influencer → produto/SKU/tamanho → receita Shopify comprovada → custo pago relacionado → estoque Tiny → risco/ação`.
5. Enquanto o dicionário não existir, reportar os 50–70x como **dado incorreto para decisão**, não como performance.
