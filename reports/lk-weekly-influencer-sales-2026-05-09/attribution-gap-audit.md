# LK — Auditoria de gaps de atribuição semanal por influencer

Janela: 2026-05-03 a 2026-05-09 (BRT)

## Conclusão executiva

A correção do `ad_id` resolveu o caso mais claro: **Fiorela** deixou de aparecer zerada em Shopify e passou a ter 1 pedido / R$ 8.729,97 com ponte por `ad_id Meta` exato.

Para os demais influencers com Shopify zerado, não encontrei ponte segura por `ad_id` exato nesta janela. Existem sinais Meta fortes, mas sem ponte Shopify verificável; portanto continuam como `meta_signal_only`, não como venda/produto atribuído.

## Status por influencer com sinal Meta e Shopify zerado

### Lala Noleto

- Meta: 15 compras canônicas / spend R$ 1.726,17 / valor Meta R$ 22.959,96.
- Shopify com ponte segura: 0 pedidos.
- Leitura: **Meta signal only**. Falta ponte Shopify por texto ou `ad_id` exato.

### Ju Mesquita

- Meta: 8 compras canônicas / spend R$ 902,33 / valor Meta R$ 12.269,98.
- Shopify com ponte segura: 0 pedidos.
- Leitura: **Meta signal only**. Falta ponte Shopify por texto ou `ad_id` exato.

### Arlindo

- Meta: 7 compras canônicas / spend R$ 920,18 / valor Meta R$ 15.659,97.
- Shopify com ponte segura: 0 pedidos.
- Leitura: **Meta signal only**. Falta ponte Shopify por texto ou `ad_id` exato.

### Mariah

- Meta: 1 compra canônica / spend R$ 6,45 / valor Meta R$ 2.199,99.
- Shopify com ponte segura: 0 pedidos.
- Leitura: **Meta signal only**.

### Maria Fernanda

- Meta: 0 compras canônicas / spend R$ 488,54 / cliques 8.358.
- Shopify com ponte segura: 0 pedidos.
- Leitura: muito clique e zero compra Meta/Shopify; investigar tracking/criativo/tráfego, mas não atribuir produtos.

## Potenciais pedidos sem atribuição segura

Foi encontrado 1 pedido com `campaign_id`/`adset_id` de estrutura compartilhada, mas sem `ad_id` exato suficiente para atribuição segura:

- Pedido Shopify: #147294
- Valor: R$ 2.090,00
- Produto: Tênis Adidas Samba OG Cream White Cardboard Creme / SKU JI3185-2 / tam. 35
- Candidatos por campanha/adset genérico: Fiorela, Helena Lunardelli, Lala Noleto, Malu Borges, Renata, Silvia Henz, Taby.
- Decisão: **não atribuir**. Campanha/adset genérico agrupa vários influencers e geraria falso positivo.

## Regra operacional preservada

- Atribuir produto vendido só com:
  - ponte textual clara; ou
  - `ad_id` Meta exato no Shopify (`utm_content`, `ad_id`, `fb_ad_id`) pertencente ao anúncio de influencer.
- Não atribuir produto por `campaign_id` ou `adset_id` genérico.
- Quando houver sinal Meta sem ponte Shopify, classificar como `meta_signal_only`.
