# LK Campaign Attribution Dictionary — seed v0.1

Status: seed read-only criado a partir dos relatórios versionados em 2026-05-10. Não é verdade final de ROAS; é o primeiro mapa para evitar confundir ROAS atribuído pela plataforma com venda operacional da LK.

Fontes usadas:

- `reports/lk-meta-campaign-title-roas-readonly-2026-05-10.md`
- `reports/lk-roas-influencer-correction-readonly-2026-05-10.md`
- `reports/lk-paid-attribution-brief-real-2026-05-08-v03.md`
- `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`

## Regras deste seed

- `Meta attributed ROAS` é apenas sinal de plataforma.
- `Shopify evidence revenue` só entra quando há cupom, UTM, landing, referrer ou note attribute compatível.
- `operational_roas` fica `[não calcular ainda]` quando custo e receita não estão amarrados por janela/naming/cupom confiável.
- Qualquer recomendação de campanha, orçamento, compra, WhatsApp, Notion ou Shopify/Tiny write exige aprovação de Lucas.

## Entradas por influencer

### influencer_silvia_heinz_2025_12_2026_05

- status: `mapped_operational_roas_provisional`
- influencer_name: Silvia Heinz
- influencer_handle: `[a confirmar]`
- platform: Meta Ads + Shopify evidence
- paid_source: Meta Marketing API
- commercial_window: `2025-12-01` a `2026-05-10`
- meta_name_patterns:
  - `Silvia`
  - `Silvia Heinz`
  - `influencer Silvia`
- known_campaign_contexts:
  - `Pareto.Vendas-Adv [ Geral] | Stories | [influencer Silvia | start 20-12-25 | Onitsuka Sabot Stories 3]`
  - `Pareto,lancamento,Jacquemus | Lista Zipper | [influencer Silvia 24-03-26] - jacquemus]Lista Compradores`
  - `Pareto,lancamento,Jacquemus | Lista VIP | [influencer Silvia 11-03-26] - jacquemus]Lista Compradores`
- Shopify evidence found:
  - pedidos web com evidência textual: 209
  - receita Shopify com evidência: R$ 650.658,20
  - evidências: discount_code, landing_site, note_attributes
  - linhas de produto casadas no audit de estoque: 107
  - receita de linhas casadas: R$ 319.927,85
- Meta platform signal:
  - spend: R$ 50.311,49
  - compras Meta: 822
  - valor Meta atribuído: R$ 2.560.642,92
  - Meta attributed ROAS: 50,90x
- Produtos associados:
  - Tênis Nike Moon Shoe SP Jacquemus Off White
  - Tênis Nike Moon Shoe SP Jacquemus Medium Brown
  - Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege
  - Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto
  - Tênis Onitsuka Tiger Mexico 66 White Black Branco
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
  - Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege
- product_theme: Jacquemus/Nike, Onitsuka, feminino premium/curadoria
- confidence_level: média
- operational_roas_provisional: **12,93x** = Shopify evidence revenue R$ 650.658,20 / Meta related spend R$ 50.311,49. Usar como métrica provisória, não como autorização de verba.
- operational_roas: `[substituído por operational_roas_provisional]`
- estoque consequence: checar SKUs Jacquemus/Nike e Onitsuka associados no Tiny `LK | CONTROLE ESTOQUE`; vários SKUs Jacquemus aparecem em ruptura ou exigem mapa SKU Tiny.
- próxima ação: confirmar handle/cupom oficial e separar campanhas Jacquemus vs Onitsuka para evitar misturar produto e público.

### influencer_helena_lunardelli_2025_12_2026_05

- status: `mapped_operational_roas_provisional`
- influencer_name: Helena Lunardelli
- influencer_handle: `[a confirmar]`
- platform: Meta Ads + Shopify evidence + GA4/Shopify cupom
- paid_source: Meta Marketing API
- commercial_window: `2025-12-01` a `2026-05-10`
- meta_name_patterns:
  - `Helena`
  - `Helena Lunardelli`
  - `Dia das Mães | Helena`
- known_campaign_contexts:
  - `Pareto.Vendas-Adv [ Dia das Mães | Helena] Campanha`
  - `[PD][FUNDO] ADV+ | Simples | Vendas Advantage+ [clube do sky] | [influencer Helena | start 07-12-25 | Stories 5]`
- Shopify evidence found:
  - pedidos web com evidência textual: 37
  - receita Shopify com evidência: R$ 154.482,04
  - evidências: note_attributes, discount_code, landing_site
  - cupom observado em 2026-05-08: `HELENA10`
  - linhas de produto casadas no audit de estoque: 13
  - receita de linhas casadas: R$ 27.169,87
- Meta platform signal:
  - spend: R$ 24.364,51
  - compras Meta: 627
  - valor Meta atribuído: R$ 1.720.526,49
  - Meta attributed ROAS: 70,62x
- Produtos associados:
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
  - Tênis adidas Samba Og Supplier Colour Off White Gum Prata
  - Tênis Onitsuka Tiger Mexico 66 SD Vin Clay Canyon Cream Marrom
  - Tênis New Balance 9060 Sea Salt Concrete Branco
  - Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege
  - Tênis Onitsuka Tiger Mexico 66 SD Birch Metropolis Bege
  - Onitsuka Tiger Mexico 66 Paraty Natural Navy Bege
- product_theme: Dia das Mães, feminino premium, Onitsuka/New Balance/Adidas
- confidence_level: média
- operational_roas_provisional: **6,34x** = Shopify evidence revenue R$ 154.482,04 / Meta related spend R$ 24.364,51. Usar como métrica provisória; separar Dia das Mães/ADV+ antes de escalar.
- operational_roas: `[substituído por operational_roas_provisional]`
- estoque consequence: checar Onitsuka Kill Bill e New Balance 9060 por tamanho; há sinais de ruptura em Kill Bill e baixa cobertura em NB/Onitsuka no relatório de estoque.
- próxima ação: confirmar padrões oficiais de UTM/cupom e separar tráfego Helena de tráfego genérico ADV+.

### influencer_lala_noleto_2025_12_2026_05

- status: `ambiguous_meta_signal_only`
- influencer_name: Lala Noleto
- influencer_handle: `[a confirmar]`
- platform: Meta Ads; Shopify evidence ainda não encontrada
- paid_source: Meta Marketing API
- commercial_window: `2025-12-01` a `2026-05-10`
- meta_name_patterns:
  - `Lala`
  - `Lala Noleto`
  - `Lala noleto`
- known_campaign_contexts:
  - `[PD][FUNDO] ADV+ | Simples | Vendas Advantage+ [clube do sky] | [influencer Lala noleto]`
- Shopify evidence found:
  - pedidos web com cupom/UTM/landing/referrer/note textual: 0
  - receita Shopify com evidência direta: R$ 0,00
- Meta platform signal:
  - spend: R$ 25.750,26
  - compras Meta: 519
  - valor Meta atribuído: R$ 1.686.413,85
  - Meta attributed ROAS: 65,49x
- Produtos associados: `[a confirmar]`
- product_theme: `[a confirmar]`
- confidence_level: baixa para venda operacional; média para exposição/spend Meta
- operational_roas_provisional: **0,00x / não conclusivo** = Shopify evidence revenue R$ 0,00 / Meta related spend R$ 25.750,26. Não usar como campanha perdedora sem descobrir cupom/UTM/landing/brief real.
- operational_roas: `[não calcular como verdade operacional]`
- estoque consequence: nenhuma decisão de estoque até encontrar cupom/UTM/landing/produto Shopify compatível.
- próxima ação: descobrir cupom/UTM/landing/brief real de Lala ou marcar como campanha sem evidência Shopify direta no recorte.

### influencer_ju_mesquita_2026_02

- status: `draft`
- influencer_name: Ju Mesquita
- influencer_handle: `[a confirmar]`
- platform: Meta Ads
- commercial_window: start citado `25-02-26`
- meta_name_patterns:
  - `Ju Mesquita`
- known_campaign_contexts:
  - `[PD] [FUNDO] RMKT | RMKT (Site + Instagram + Vídeo) | [influencer Ju Mesquita | start 25-02-26 | Onitsuka]`
  - `[PD] [FUNDO] RMKT | RMKT (Site + Instagram + Vídeo) | [influencer Ju Mesquita | start 25-02-26 | New Balance 204 L]`
- Meta platform signal observado em 2026-05-08:
  - Onitsuka: gasto R$ 31,21; compras Meta 3; valor Meta R$ 6.840,00; ROAS plataforma 219,16x
  - New Balance 204L: gasto R$ 111,96; compras Meta 0; valor Meta R$ 0,00
- Shopify evidence found: `[não consolidado neste seed]`
- Produtos esperados: Onitsuka; New Balance 204L
- confidence_level: baixa/média
- operational_roas: `[não calcular ainda]`
- próxima ação: buscar evidência Shopify por UTM/cupom/produtos Onitsuka/NB 204L na janela correta.

### influencer_mariah_adv_geral_2026_05

- status: `ambiguous`
- influencer_name: Mariah
- influencer_handle: `[a confirmar]`
- platform: Meta Ads
- known_campaign_contexts:
  - `[PD] [FUNDO] RMKT | RMKT (Site + Instagram + Vídeo) | [influencer Mariah- Adv geral]`
- Meta platform signal observado em 2026-05-08:
  - gasto R$ 0,14; compras Meta 3; valor Meta R$ 6.599,97; ROAS plataforma 47.142,64x
- Shopify evidence found: `[não consolidado neste seed]`
- confidence_level: baixa
- operational_roas: `[não calcular]`
- leitura: valor extremo em gasto mínimo é sinal de atribuição/plataforma; não usar para decisão de verba.
- próxima ação: auditar se Mariah tem cupom/UTM/landing/produto e se o gasto de R$ 0,14 é fragmento de campanha maior.

### influencer_arlindo_2026_04

- status: `draft`
- influencer_name: Arlindo
- influencer_handle: `[a confirmar]`
- platform: Meta Ads
- known_campaign_contexts:
  - `Pareto,Vendas [Masculino] | Masculino Segmentado | [influencer Arlindo 02-04-26] - Varios Looks]Lista Compradores`
- Meta platform signal observado em 2026-05-08:
  - gasto R$ 140,81; compras Meta 0; valor Meta R$ 0,00
- Shopify evidence found: `[não consolidado neste seed]`
- product_theme: masculino / vários looks
- confidence_level: baixa
- próxima ação: cruzar campanha masculina com Shopify/GA4 antes de concluir performance.

### influencer_maria_fernanda_2025_11

- status: `draft`
- influencer_name: Maria Fernanda
- influencer_handle: `[a confirmar]`
- platform: Meta Ads
- known_campaign_contexts:
  - `[PD][MEIO] TRAF | Simples | [Regiona l Camboriu - Curitiba] | [influencer Maria Fernanda - Video 2 - Nov 25]`
- Meta platform signal observado em 2026-05-08:
  - gasto R$ 108,03; compras Meta 0; valor Meta R$ 0,00
- Shopify evidence found: `[não consolidado neste seed]`
- product_theme: regional / tráfego
- confidence_level: baixa
- próxima ação: avaliar como campanha de tráfego/regional, não como venda direta.

## Entradas por campanha broad/estrutura

### campaign_pd_fundo_adv_plus

- status: `mapped`
- platform: Meta Ads + Shopify UTM evidence
- campaign_name: `[PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)`
- family: advantage/broad
- Meta period `2025-12-01` a `2026-05-10`:
  - spend: R$ 36.296,67
  - compras Meta: 771
  - valor Meta: R$ 2.542.659,81
  - Meta attributed ROAS: 70,05x
- Shopify UTM evidence:
  - pedidos: 3
  - receita: R$ 10.799,98
  - UTM: `[PD][FUNDO] ADV  (antiga Simples | Vendas Advantage )`
- Produtos/SKUs vendidos com match:
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege | 1183A872.101-3 | 36
  - Tênis New Balance 204L Mushroom Arid Stone Marrom | U204LMMA-4 | 37
  - Tênis New Balance 530 'Silver Metallic Black Cement' Prateado | U530ESA-9 | 42
  - New Balance 9060 Black Cement "Black Cat" Preto | U9060ZGE | 37
  - Tênis Adidas Samba OG Crochet Pack Sand Strata Bege | JR9446-3 | 36
- confidence_level: média para UTM strict; baixa para atribuição ampla Meta
- próxima ação: normalizar naming/UTM para evitar espaço/símbolo divergente entre campanha e Shopify.

### campaign_pd_fundo_rmkt

- status: `mapped`
- platform: Meta Ads + Shopify UTM evidence
- campaign_name: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )`
- family: remarketing
- Meta period `2025-12-01` a `2026-05-10`:
  - spend: R$ 32.274,10
  - compras Meta: 783
  - valor Meta: R$ 2.320.329,06
  - Meta attributed ROAS: 71,89x
- Shopify UTM evidence:
  - pedidos: 6
  - receita: R$ 18.489,97
  - UTM: `[PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )`
- Produtos/SKUs vendidos com match:
  - Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege | 1183C015101-14 | 42.5
  - Tênis Onitsuka Tiger Tiger Corsair A55 Midnight Cream Azul | 1183C317-401-10 | 43
  - Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | 1183B566021-4 | 37
  - Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata | [sem SKU] | 35.5
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | [sem SKU] | 43
- confidence_level: média para UTM strict; baixa/média para campanha inteira porque RMKT pode capturar demanda criada por outros canais.
- próxima ação: separar anúncios de influencer dentro da RMKT antes de atribuir produto a pessoa específica.

### campaign_pareto_fundo_daba

- status: `mapped`
- platform: Meta Ads + Shopify UTM evidence
- campaign_name: `[Pareto] [FUNDO] DABA`
- family: other/fundo
- Meta period `2025-12-01` a `2026-05-10`:
  - spend: R$ 16.526,39
  - compras Meta: 444
  - valor Meta: R$ 1.037.493,36
  - Meta attributed ROAS: 62,78x
- Shopify UTM evidence:
  - pedidos: 15
  - receita: R$ 41.027,24
  - UTM: `[PD] [FUNDO] DABA`
- Produtos/SKUs vendidos com match:
  - Camisa Aphase Check - Light Yellow Bege | 20054-3 | L/G
  - Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege | 1183C015-202-9 | 42
  - Tênis Onitsuka Tiger California 78 EX Monument Blue Cream Azul | 1183A355.405-8 | 41
  - Tênis New Balance 530 White Natural Indigo Branco | MR530SG-3 | 37
  - Tênis Nike Moon Shoe SP Jacquemus Off White | [sem SKU] | 38
- confidence_level: média
- próxima ação: investigar se DABA tem criativo/produto dominante ou se é campanha broad de fundo.

### campaign_pareto_vendas_adv_geral

- status: `ambiguous`
- campaign_name: `Pareto.Vendas-Adv [ Geral]`
- family: advantage/broad
- Meta period `2025-12-01` a `2026-05-10`:
  - spend: R$ 62.523,72
  - compras Meta: 1503
  - valor Meta: R$ 3.863.919,30
  - Meta attributed ROAS: 61,80x
- Shopify UTM strict evidence:
  - pedidos: 0
  - receita: R$ 0,00
- confidence_level: baixa para decisão operacional por título
- próxima ação: mapear quais UTMs/ads/influencers vivem dentro dessa campanha antes de qualquer conclusão.

### campaign_pareto_lancamento_jacquemus

- status: `ambiguous`
- campaign_name variants:
  - `Pareto.lancamento.Jacquemus`
  - `Pareto,lancamento,Jacquemus`
- family: lançamento/produto
- Meta period `2025-12-01` a `2026-05-10`:
  - spend: R$ 17.853,12
  - compras Meta: 285
  - valor Meta: R$ 1.218.679,74
  - Meta attributed ROAS: 68,26x
- Shopify UTM strict evidence:
  - pedidos: 0
  - receita: R$ 0,00
- influencers/criativos citados:
  - Silvia 11-03-26 Jacquemus
  - Silvia 24-03-26 Jacquemus
- Produtos esperados:
  - Nike Moon Shoe SP Jacquemus Off White
  - Nike Moon Shoe SP Jacquemus Medium Brown
  - Nike Moon Shoe SP Jacquemus Off Noir
- estoque consequence: Jacquemus aparece como marca/colab forte nos últimos 30/90 dias e com rupturas/mapa SKU Tiny pendente; precisa de stock intelligence antes de escalar campanha.
- confidence_level: baixa/média
- próxima ação: conectar campanha Jacquemus com UTMs/landing/produtos Shopify e estoque por tamanho.

## Próximas correções de tracking/naming

1. Padronizar futuras campanhas de influencer com `utm_campaign` e `utm_content` previsíveis.
2. Usar cupom único quando fizer sentido, mas não depender só de cupom porque parte da compra vem por landing/referrer/note attributes.
3. Separar campanha broad/Advantage+/RMKT da leitura de influencer; uma pessoa dentro da campanha não pode herdar todo o ROAS da estrutura.
4. Marcar todo relatório com quatro colunas: plataforma, Shopify evidence, operational ROAS, stock consequence.
5. Manter `Lala Noleto` como prioridade de investigação, porque há spend/plataforma forte e zero evidência Shopify direta encontrada no recorte.
