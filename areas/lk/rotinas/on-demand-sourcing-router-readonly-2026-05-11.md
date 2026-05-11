# LK OS, On-demand Sourcing Router read-only, 2026-05-11

Generated at: `2026-05-11T20:13:01.193261+00:00`
Week: `2026-05-04` to `2026-05-10`

## Veredito operacional

O próximo bloco seguro foi materializar o router de sourcing sob demanda. Isto prepara o caminho para GOAT/Droper/StockX/KicksDev apenas quando houver decisão comercial específica, sem criar full-sync de preços externos.

## Resumo

- Linhas de sourcing roteadas: 8
- Prontas somente depois de aprovação manual: 4
- Opcionais para agrupar com P0: 1
- Bloqueadas por dados: 3
- Quantidade referência de cotação, não compra: 26
- Sinal de receita Shopify: R$ 89.669,71

## Regra principal

- GOAT, Droper, StockX e KicksDev são ferramentas on-demand para compra/reposição/subida específica.
- Não são tabelas permanentes de preço externo dentro do SQL local da LK.
- Se algum resultado externo for persistido no futuro, deve ser resumo por decisão: item consultado, fonte, timestamp, custo estimado, confiança, cheapest viable source e validade.
- Para StockX/GOAT, sempre identificar US Men vs US Women e normalizar para LK/BR/EU antes de comparar tamanho.

## Fila roteada

### LK-SOURCING-20260504-20260510-01 | Nike Moon Shoe SP Jacquemus
- Status: `ready_for_manual_quote_approval_then_on_demand_lookup`
- Lookup externo agora: `False`
- Gatilho exigido: `approve_quote_only_or_explicit_sourcing_research`
- Gate de aprovação: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras, se aprovado: GOAT, Droper, StockX, KicksDev
- Receita Shopify sinal: R$ 48.999,92
- Motivo: P0 pronto para decisão; pesquisa externa só deve ocorrer no escopo desta decisão, não em sync permanente.

### LK-SOURCING-20260504-20260510-02 | New Balance 9060
- Status: `ready_for_manual_quote_approval_then_on_demand_lookup`
- Lookup externo agora: `False`
- Gatilho exigido: `approve_quote_only_or_explicit_sourcing_research`
- Gate de aprovação: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras, se aprovado: GOAT, Droper, StockX, KicksDev
- Receita Shopify sinal: R$ 18.799,93
- Motivo: P0 pronto para decisão; pesquisa externa só deve ocorrer no escopo desta decisão, não em sync permanente.

### LK-SOURCING-20260504-20260510-03 | Nike Mind 002
- Status: `ready_for_manual_quote_approval_then_on_demand_lookup`
- Lookup externo agora: `False`
- Gatilho exigido: `approve_quote_only_or_explicit_sourcing_research`
- Gate de aprovação: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras, se aprovado: GOAT, Droper, StockX, KicksDev
- Receita Shopify sinal: R$ 6.399,98
- Motivo: P0 pronto para decisão; pesquisa externa só deve ocorrer no escopo desta decisão, não em sync permanente.

### LK-SOURCING-20260504-20260510-04 | Comme des Garçons PLAY Polo
- Status: `ready_for_manual_quote_approval_then_on_demand_lookup`
- Lookup externo agora: `False`
- Gatilho exigido: `approve_quote_only_or_explicit_sourcing_research`
- Gate de aprovação: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras, se aprovado: GOAT, Droper, StockX, KicksDev
- Receita Shopify sinal: R$ 3.599,98
- Motivo: P0 pronto para decisão; pesquisa externa só deve ocorrer no escopo desta decisão, não em sync permanente.

### LK-SOURCING-20260504-20260510-05 | New Balance 530
- Status: `optional_hold_until_p0_bundle`
- Lookup externo agora: `False`
- Gatilho exigido: `lucas_julio_decide_bundle_with_p0`
- Gate de aprovação: manual_bundle_decision_required
- Fontes futuras, se aprovado: GOAT, Droper, StockX, KicksDev
- Receita Shopify sinal: R$ 5.999,97
- Motivo: P1 opcional; só pesquisar mercado externo se for agrupado com uma cotação P0 aprovada.

### LK-SOURCING-20260504-20260510-06 | Onitsuka Tiger Mexico 66
- Status: `blocked_needs_data`
- Lookup externo agora: `False`
- Gatilho exigido: `resolve_sku_tiny_data_first`
- Gate de aprovação: data_resolution_before_any_sourcing
- Fontes futuras, se aprovado: n/d
- Receita Shopify sinal: R$ 4.799,98
- Motivo: Linha precisa resolver dados antes de GOAT/Droper/StockX/KicksDev ou fornecedor.

### LK-SOURCING-20260504-20260510-07 | Camiseta Saint Studio Boxy
- Status: `blocked_needs_data`
- Lookup externo agora: `False`
- Gatilho exigido: `resolve_sku_tiny_data_first`
- Gate de aprovação: data_resolution_before_any_sourcing
- Fontes futuras, se aprovado: n/d
- Receita Shopify sinal: R$ 619,98
- Motivo: Linha precisa resolver dados antes de GOAT/Droper/StockX/KicksDev ou fornecedor.

### LK-SOURCING-20260504-20260510-08 | Bearbrick Series 48
- Status: `blocked_needs_data`
- Lookup externo agora: `False`
- Gatilho exigido: `resolve_sku_tiny_data_first`
- Gate de aprovação: data_resolution_before_any_sourcing
- Fontes futuras, se aprovado: n/d
- Receita Shopify sinal: R$ 449,97
- Motivo: Linha precisa resolver dados antes de GOAT/Droper/StockX/KicksDev ou fornecedor.

## O que não foi feito

- Nenhuma chamada a GOAT, Droper, StockX ou KicksDev.
- Nenhum full-sync de preço externo.
- Nenhum fornecedor foi contatado.
- Nenhuma compra, PO, reserva ou pagamento.
- Nenhum Shopify/Tiny write, alteração de preço/estoque/produto, campanha, cliente, banco de produção ou cron.

## Próximo passo seguro

Quando Lucas/Júlio aprovar uma família específica, preencher somente aquela decisão com pesquisa externa sob demanda e devolver cheapest viable option com custo estimado, lead time, margem e validade. Ainda assim, compra/PO continua sendo aprovação separada.
