# LK OS — Supplier Quote Send Preview, 2026-05-12

> **SUPERCEDIDO / NÃO USAR PARA ENVIO — correção Lucas 2026-05-12:** este preview foi invalidado. A lógica correta não é enviar cotação genérica para fornecedores/grupo de compras. Reposição só deve iniciar quando houver venda/pedido de produto com estoque zerado/stockout confirmado. Fluxo correto: confirmar SKU/tamanho + stockout → consultar Droper → se não tiver, comparar StockX vs GOAT pelo menor custo viável → preparar tarefa Notion/Júlio com link/custo/contexto. Hermes nunca compra, reserva, escolhe endereço/importador ou aciona fornecedor autonomamente.

Generated at: `2026-05-12T21:01:35.409926+00:00`

## Veredito

Preview invalidado por correção operacional de Lucas. Nada foi enviado. Não usar este artefato como autorização, destino ou copy de cotação.

## Resumo

- Mensagens preview: 4
- Quantidade referência de cotação, não compra: 24
- Sinal de receita Shopify: R$ 77.799,81
- Opcionais não incluídos por padrão: New Balance 530
- Supplier contact / external send / purchase / PO / reservation / writes: 0

## Mensagens preview — não enviadas

### 1. Nike Moon Shoe SP Jacquemus
- Status: `ready_for_lucas_destination_and_send_approval`
- Itens/P0/P1: 5 / 2 / 3
- Quantidade referência, não compra: 10
- Receita Shopify sinal: R$ 48.999,92
- Mensagem:
```text
[DESTINO: fornecedor a confirmar por Lucas/Júlio]
[ASSUNTO/CONTEXTO: Cotação LK — Nike Moon Shoe SP Jacquemus]

Olá, preciso validar disponibilidade e custo para Nike Moon Shoe SP Jacquemus.
Isto é consulta de disponibilidade/preço, ainda não é pedido de compra.
Itens para cotação:
- SKU HV8547-200-38 | tamanho 38 | referência cotação 3 un | prioridade P0
- SKU HV8547-002-36 | tamanho 36 | referência cotação 3 un | prioridade P0
- SKU HV8547-001-1 | tamanho 34 | referência cotação 1 un | prioridade P1
- SKU HV8547-001-7 | tamanho 40 | referência cotação 1 un | prioridade P1
- SKU HV8547-601-37 | tamanho 37 | referência cotação 2 un | prioridade P1
Responder por favor: custo unitário, disponibilidade imediata, lead time, condição de pagamento e validade da cotação.
Não separar, reservar ou faturar sem confirmação posterior.

Observação interna: enviar somente após Lucas/Júlio aprovar destino e envio. Esta mensagem não autoriza compra, reserva, faturamento ou separação.
```

### 2. New Balance 9060
- Status: `ready_for_lucas_destination_and_send_approval`
- Itens/P0/P1: 3 / 2 / 1
- Quantidade referência, não compra: 8
- Receita Shopify sinal: R$ 18.799,93
- Mensagem:
```text
[DESTINO: fornecedor a confirmar por Lucas/Júlio]
[ASSUNTO/CONTEXTO: Cotação LK — New Balance 9060]

Olá, preciso validar disponibilidade e custo para New Balance 9060.
Isto é consulta de disponibilidade/preço, ainda não é pedido de compra.
Itens para cotação:
- SKU U9060CCC-4 | tamanho 37 | referência cotação 3 un | prioridade P0
- SKU U9060WHT-4 | tamanho 37 | referência cotação 3 un | prioridade P0
- SKU U9060ERB-3 | tamanho 36 | referência cotação 2 un | prioridade P1
Responder por favor: custo unitário, disponibilidade imediata, lead time, condição de pagamento e validade da cotação.
Não separar, reservar ou faturar sem confirmação posterior.

Observação interna: enviar somente após Lucas/Júlio aprovar destino e envio. Esta mensagem não autoriza compra, reserva, faturamento ou separação.
```

### 3. Nike Mind 002
- Status: `ready_for_lucas_destination_and_send_approval`
- Itens/P0/P1: 1 / 1 / 0
- Quantidade referência, não compra: 3
- Receita Shopify sinal: R$ 6.399,98
- Mensagem:
```text
[DESTINO: fornecedor a confirmar por Lucas/Júlio]
[ASSUNTO/CONTEXTO: Cotação LK — Nike Mind 002]

Olá, preciso validar disponibilidade e custo para Nike Mind 002.
Isto é consulta de disponibilidade/preço, ainda não é pedido de compra.
Itens para cotação:
- SKU HQ4308-003-5 | tamanho 36 | referência cotação 3 un | prioridade P0
Responder por favor: custo unitário, disponibilidade imediata, lead time, condição de pagamento e validade da cotação.
Não separar, reservar ou faturar sem confirmação posterior.

Observação interna: enviar somente após Lucas/Júlio aprovar destino e envio. Esta mensagem não autoriza compra, reserva, faturamento ou separação.
```

### 4. Comme des Garçons PLAY Polo
- Status: `ready_for_lucas_destination_and_send_approval`
- Itens/P0/P1: 1 / 1 / 0
- Quantidade referência, não compra: 3
- Receita Shopify sinal: R$ 3.599,98
- Mensagem:
```text
[DESTINO: fornecedor a confirmar por Lucas/Júlio]
[ASSUNTO/CONTEXTO: Cotação LK — Comme des Garçons PLAY Polo]

Olá, preciso validar disponibilidade e custo para Comme des Garçons PLAY Polo.
Isto é consulta de disponibilidade/preço, ainda não é pedido de compra.
Itens para cotação:
- SKU CDGP2 | tamanho G/L | referência cotação 3 un | prioridade P0
Responder por favor: custo unitário, disponibilidade imediata, lead time, condição de pagamento e validade da cotação.
Não separar, reservar ou faturar sem confirmação posterior.

Observação interna: enviar somente após Lucas/Júlio aprovar destino e envio. Esta mensagem não autoriza compra, reserva, faturamento ou separação.
```

## Approval wording

`Aprovo enviar as 4 mensagens de cotação P1 exatamente como preview, para os fornecedores/destinos que eu indicar, apenas para disponibilidade/custo/lead time; não autorizo compra, reserva, PO, Shopify/Tiny/preço/estoque/campanha.`

## Não executado

- supplier_contact
- external_send
- purchase
- purchase_order
- reservation
- shopify_write
- tiny_write
- price_or_stock_change
- campaign_send
- database_write
- marketplace_lookup
- n8n_flow_creation

## Próximo gate

Não executar envio real a partir deste preview. O próximo fluxo correto é um router de reposição por pedido/stockout: SKU/tamanho vendido ou solicitado com estoque zero confirmado; Droper primeiro; StockX vs GOAT só se Droper não tiver; tarefa Notion/Júlio, sem compra automática.
