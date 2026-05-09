# Exemplo preenchido — Daily Sales Brief LK 07h

Status: exemplo fictício/read-only v0.1.
Período simulado: 2026-05-08 00:00–23:59.
Uso: validar formato antes de dados reais, cron ou envio recorrente.
Não faz: WhatsApp, Klaviyo, Shopify, Tiny, Notion, Meta, Google, n8n, preço, estoque ou compra.

## 1. Resumo executivo

Ontem a LK vendeu **R$ 18.740,00** em **8 pedidos** no exemplo.
Online: **R$ 12.990,00 / 5 pedidos**. Loja física: **R$ 5.750,00 / 3 pedidos**.
Conversão online simulada: **0,16%** vs baseline **0,13%** e meta **0,20%**.

Leitura principal: a venda foi puxada por New Balance e Onitsuka, mas dois tamanhos com boa saída estão em risco de ruptura.

Ação recomendada nº 1: aprovar checagem manual de fonte Brasil para os tamanhos 37 e 38 dos modelos com estoque livre baixo.

## 2. Vendas Shopify

- Receita total: R$ 18.740,00.
- Pedidos: 8.
- Ticket médio: R$ 2.342,50.
- Online: R$ 12.990,00 / 5 pedidos.
- Loja física: R$ 5.750,00 / 3 pedidos.
- Source/canal: 2 Google Ads, 1 Meta Ads, 1 influencer/UTM, 1 orgânico, 3 loja física.
- Variação vs média 7 dias: +18% em receita e +1 pedido.
- Anomalias: tráfego Meta alto, mas conversão abaixo de Google Ads no exemplo.

## 3. Conversão e CRO

- Conversão online Shopify Analytics: 0,16%.
- Sessões: 3.120.
- Add to cart: 42.
- Checkout iniciado: 18.
- Compra: 5.
- Páginas/produtos com tráfego e baixa conversão: PDP de `[modelo/cor]` com 410 sessões e 0 compra.
- Hipótese principal: tráfego chegou no produto certo, mas tamanho principal estava indisponível/pronta entrega não clara.
- Teste sugerido: melhorar bloco de disponibilidade por tamanho e CTA de encomenda humana no PDP.
- Aprovação necessária: aprovar criação de HTML visual do novo bloco PDP antes de qualquer uso externo.

## 4. Produtos/modelos/tamanhos vendidos

### Item A

```text
Produto/modelo: New Balance 860 [cor a confirmar]
Marca: New Balance
Tamanhos vendidos: 37, 38, 39
Canal/source: Google Ads + loja física
Influencer/campanha/UTM: não identificado
Status estoque Tiny por tamanho: 37 = 1 livre; 38 = 0; 39 = 2 livres
Status comercial: 37 pronta entrega aparente; 38 zerado; 39 pronta entrega aparente
Leitura: tamanho 38 vendeu e está zerado; tamanho 37 tem cobertura curta.
Ação sugerida: aprovar checagem Droper.app + grupo LK.Sneakers | Compras para 38 e 37.
Confiança: média, porque status de encomenda/reserva precisa conferência humana.
```

### Item B

```text
Produto/modelo: Onitsuka [modelo/cor a confirmar]
Marca: Onitsuka
Tamanhos vendidos: 36, 37
Canal/source: influencer/UTM + orgânico
Influencer/campanha/UTM: influencer_exemplo_maio
Status estoque Tiny por tamanho: 36 = 0; 37 = 3 livres
Status comercial: 36 zerado; 37 pronta entrega aparente
Leitura: influencer parece ter funcionado melhor para Onitsuka do que para Adidas neste exemplo.
Ação sugerida: registrar fit influencer × Onitsuka e preparar próxima recomendação de produto similar.
Confiança: baixa/média, porque cupom/UTM precisa validação.
```

## 5. Centro de Inteligência de Stock

- Produtos com risco de ruptura: New Balance 860 tamanho 37; Onitsuka tamanho 36 zerado.
- Produtos com lead time maior que cobertura: New Balance 860 tamanho 37, se reposição Brasil levar 7 dias e venda seguir no ritmo.
- Produtos que devem acionar busca de fonte/restock: New Balance 860 37/38; Onitsuka 36.
- Produtos para jogar no `LK.Sneakers | Compras` após aprovação: New Balance 860 38 primeiro; 37 segundo.
- Produtos com estoque alto e venda lenta: `[modelo/cor]` Nike tamanho 44, 5 pares livres e 0 venda em 30 dias no exemplo.
- Divergências Shopify × Tiny × pedido: conferir se pedido `#EXEMPLO-1042` tem tag de encomenda no pedido.

## 6. Recompra / CRM

- Vendas que geram oportunidade de segunda compra: clientes que compraram New Balance 860 podem receber curadoria futura de modelos running/lifestyle.
- Clientes elegíveis para recompra 90 dias: 14 clientes simulados sem compra recente, com histórico New Balance/Onitsuka.
- Segmentos por marca/tamanho: New Balance 37–39; Onitsuka 36–38.
- Sugestão Klaviyo: draft de campanha “running curado LK” para segmento New Balance, sem envio.
- Sugestão WhatsApp loja física: abordagem 1:1 apenas para clientes VIP, com aprovação.
- Aprovação necessária antes de enviar: sim, sempre.

## 7. Pricing signals

- Produto vendido com reposição mais cara que preço atual: New Balance 860 38 no exemplo.
- Produto com StockX/KicksDev/Droper relevante: consultar apenas se Lucas aprovar busca externa acionada por demanda.
- Sugestão de aumento: não sugerir agora sem preço de reposição validado.
- Sugestão de não mexer: manter Onitsuka 37, pois estoque ainda cobre venda simulada.
- Risco de conversão: aumento precipitado pode piorar meta 0,20%.
- Aprovação necessária: qualquer mudança de preço.

## 8. Conteúdo/campanha

- Sinal que virou pauta: New Balance 860 vendendo e com tamanho 38 zerado.
- Formato recomendado: blog curto + Instagram + PDP melhorado; Klaviyo só se estoque/fornecimento estiver seguro.
- Precisa seguir DesignMD LK: sim.
- Link/produto relacionado: `[link Shopify a preencher quando usar dados reais]`.
- Aprovação necessária: HTML visual para PDP/blog e aprovação Lucas antes de publicar/enviar.

## 9. Aprovações pendentes

```text
[ ] Aprovar checagem Droper.app para New Balance 860 37/38 — risco baixo — sem compra automática.
[ ] Aprovar mensagem rascunho para LK.Sneakers | Compras — motivo: reposição antes de ruptura — risco: preço/prazo ruim.
[ ] Aprovar criação de HTML visual para bloco PDP de disponibilidade por tamanho — motivo: CRO — risco: desalinhamento visual.
[ ] Aprovar draft Klaviyo de running/lifestyle — motivo: recompra — risco: enviar sem estoque suficiente.
```

## 10. O que não foi feito

- Nenhum WhatsApp/Klaviyo enviado.
- Nenhum blog/produto/tema publicado.
- Nenhum preço/estoque alterado.
- Nenhuma compra ou fornecedor acionado.
- Nenhum item Notion real criado.
