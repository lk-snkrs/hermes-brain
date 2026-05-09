# LK Ads Intelligence — Metricool Google Ads + Meta direto

Data: 2026-05-09
Status: rotina read-only validada com dados reais; sem ação externa, sem alteração de campanhas.

## Fontes oficiais v0.1

- Google Ads: Metricool API, brand `LK Sneakers`, `blogId=6217010`, conta Google Ads `1628971213`.
- Meta Ads: Meta Marketing API direta, conta ativa `act_1242062509867163`.
- Metricool Meta Ads: conectado na brand, mas aponta para `act_10153947479906477`; tratar como conta antiga/sem spend até reconciliação.
- Receita real/ROAS site: cruzar depois com Shopify web revenue. Meta/Google conversion value é atribuição de plataforma, não verdade final.

## Janela testada

- Período: 2026-04-09 a 2026-05-09

## Google Ads via Metricool

- Status endpoint: `200`
- Campanhas retornadas: 21
- Gasto: R$ 28.679,93
- Cliques: 36.167
- Impressões: 1.932.481
- Conversões atribuídas: 810,42
- Valor de conversão atribuído: R$ 182.418,03
- ROAS plataforma calculado: 6,36

Top campanhas Google por gasto:
- R$ 9.744,48 · ROAS 4,78 · `20840173127` · [PD] Brasil | Search - Marca
- R$ 4.601,88 · ROAS 8,53 · `22585163189` · Pareto [Pmax - Marcas Luxo Moda]
- R$ 4.009,86 · ROAS 11,41 · `22177356369` · [PD][FUNDO] Pmax | Search DSA
- R$ 3.883,38 · ROAS 4,11 · `22349812311` · Pareto.Shopping
- R$ 1.873,41 · ROAS 8,56 · `22187666566` · [PD] [FUNDO] PMAX Streetwear
- R$ 1.705,07 · ROAS 10,64 · `20883210454` · [PD][FUNDO] | Performance Max | Todos os Tênis
- R$ 1.470,26 · ROAS 0,50 · `22477923762` · Pareto.pmax.loja-fisica
- R$ 1.391,58 · ROAS 0,00 · `21479537742` · [PD] [MEIO] | Demand Gen | Tráfego
- R$ 0,00 · ROAS — · `20725499935` · LK.Sneakers
- R$ 0,00 · ROAS — · `20729443160` · Teste

## Meta Ads direto

- Status endpoint: `200`
- Campanhas retornadas: 8
- Gasto: R$ 39.937,29
- Cliques: 101.814
- Impressões: 1.571.871
- Compras atribuídas Meta: 287,00
- Valor atribuído Meta: R$ 890.966,61
- ROAS plataforma calculado: 22,31

Top campanhas Meta por gasto:
- R$ 10.762,43 · ROAS 27,11 · `120210118442410224` · [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+)
- R$ 9.243,50 · ROAS 21,88 · `120241297336180224` · Pareto.lancamento.Jacquemus
- R$ 6.089,79 · ROAS 24,85 · `120206303993560224` · [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas )
- R$ 4.481,33 · ROAS — · `120210400473720224` · [PD][MEIO] TRAF (antiga Simples | Tráfego)
- R$ 4.252,97 · ROAS 17,98 · `120223728385160224` · Pareto.Vendas-Adv [ Geral]
- R$ 3.114,71 · ROAS 35,51 · `120242040260550224` · Pareto.Vendas [Masculino]
- R$ 1.531,03 · ROAS 38,22 · `120215662888410224` · [Pareto] [FUNDO] DABA
- R$ 461,53 · ROAS — · `120207942153600224` · [PD] [TOPO] Alcance Loja Física (antiga Simples | Alcance - Loja e Bairros)

## Influencer/product fit — regra v0.1

O objetivo não é só saber campanha vencedora; é ligar influência/campanha a produto, marca, modelo, tamanho e consequência de estoque.

Campos mínimos que o LK OS precisa extrair/normalizar:

- `platform`: google_ads/meta_ads/klaviyo/organic
- `campaign_id` e `campaign_name`
- `influencer_or_creator`: extraído de naming, UTM, cupom ou manual mapping
- `product_signal`: produto/modelo/marca detectados por nome de campanha, landing page, criativo, cupom, UTMs e Shopify orders
- `spend`, `clicks`, `sessions`, `orders`, `shopify_revenue`, `platform_conversion_value`
- `stock_consequence`: vendeu e quebrou estoque? vendeu tamanho específico? gerou encomenda?

Regra de decisão: plataforma mostra sinal de mídia; Shopify confirma venda; Tiny confirma consequência de estoque.

## Achados operacionais

- Google Ads via Metricool está pronto para entrar no LK OS agora.
- Meta via Metricool está conectado, mas na conta antiga; usar Meta direto para dados reais até reconectar Metricool à conta ativa.
- A aprovação Standard/Basic do Google Ads API direta continua útil, mas deixou de ser bloqueador para Google Ads porque Metricool já fornece campanhas/custo/conversões.
- Próximo passo técnico: cruzar este custo por campanha com Shopify orders por UTM/source/campaign/coupon/landing page e GA4 sessões/campanhas.

## Segurança

- Tokens e secrets ficam apenas no Doppler.
- Este documento contém IDs operacionais e métricas, não contém tokens.
