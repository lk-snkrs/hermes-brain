# LK OS, Weekly Quote Validation Preview read-only, 2026-05-11

Generated at: `2026-05-11T19:28:02.542351+00:00`
Week: `2026-05-04` to `2026-05-10`

## Escopo

Preview interno para transformar a fila Stock/SKU em validação de fornecedor, lead time e margem. Quantidade abaixo é referência para cotação, não autorização de compra.

## Resumo

- Linhas avaliadas: 14
- P0: 6
- P1: 8
- Bloqueadas até resolver SKU/Tiny: 3
- Grupos de cotação: 8
- Quantidade referência para cotação, não compra: 26
- Sinal de receita Shopify: R$ 89.669,71
- Fonte de venda: `fact_shopify`
- Fonte de estoque: `fact_tiny_stock`
- Tetos de custo: `derived_reconciliation`, calculados a partir do preço médio vendido e margem alvo.

## Grupos de cotação preview

### 1. Nike Moon Shoe SP Jacquemus
- Itens: 5 | P0: 2 | P1: 3
- Quantidade referência para cotação: 10
- Receita Shopify sinal: R$ 48.999,92
- Brief interno: Validar disponibilidade e custo para Nike Moon Shoe SP Jacquemus. Quantidade é referência de cotação, não compra aprovada. HV8547-200-38 tamanho 38: ref 3 un, teto custo 50% margem R$ 2.999,99, prioridade P0. HV8547-002-36 tamanho 36: ref 3 un, teto custo 50% margem R$ 2.749,99, prioridade P0. HV8547-001-1 tamanho 34: ref 1 un, teto custo 50% margem R$ 3.499,99, prioridade P1. HV8547-001-7 tamanho 40: ref 1 un, teto custo 50% margem R$ 3.499,99, prioridade P1. HV8547-601-37 tamanho 37: ref 2 un, teto custo 50% margem R$ 2.999,99, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 2. New Balance 9060
- Itens: 3 | P0: 2 | P1: 1
- Quantidade referência para cotação: 8
- Receita Shopify sinal: R$ 18.799,93
- Brief interno: Validar disponibilidade e custo para New Balance 9060. Quantidade é referência de cotação, não compra aprovada. U9060CCC-4 tamanho 37: ref 3 un, teto custo 50% margem R$ 1.399,99, prioridade P0. U9060WHT-4 tamanho 37: ref 3 un, teto custo 50% margem R$ 1.299,99, prioridade P0. U9060ERB-3 tamanho 36: ref 2 un, teto custo 50% margem R$ 1.299,99, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 3. Nike Mind 002
- Itens: 1 | P0: 1 | P1: 0
- Quantidade referência para cotação: 3
- Receita Shopify sinal: R$ 6.399,98
- Brief interno: Validar disponibilidade e custo para Nike Mind 002. Quantidade é referência de cotação, não compra aprovada. HQ4308-003-5 tamanho 36: ref 3 un, teto custo 50% margem R$ 1.599,99, prioridade P0. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 4. Comme des Garçons PLAY Polo
- Itens: 1 | P0: 1 | P1: 0
- Quantidade referência para cotação: 3
- Receita Shopify sinal: R$ 3.599,98
- Brief interno: Validar disponibilidade e custo para Comme des Garçons PLAY Polo. Quantidade é referência de cotação, não compra aprovada. CDGP2 tamanho G/L: ref 3 un, teto custo 50% margem R$ 900,00, prioridade P0. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 5. New Balance 530
- Itens: 1 | P0: 0 | P1: 1
- Quantidade referência para cotação: 2
- Receita Shopify sinal: R$ 5.999,97
- Brief interno: Validar disponibilidade e custo para New Balance 530. Quantidade é referência de cotação, não compra aprovada. MR530EMA-5 tamanho 38: ref 2 un, teto custo 50% margem R$ 1.000,00, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 6. Onitsuka Tiger Mexico 66
- Itens: 1 | P0: 0 | P1: 1
- Quantidade referência para cotação: 0
- Receita Shopify sinal: R$ 4.799,98
- Brief interno: Validar disponibilidade e custo para Onitsuka Tiger Mexico 66. Quantidade é referência de cotação, não compra aprovada. 1183C102751-3 tamanho 36: ref 0 un, teto custo 50% margem R$ 1.199,99, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 7. Camiseta Saint Studio Boxy
- Itens: 1 | P0: 0 | P1: 1
- Quantidade referência para cotação: 0
- Receita Shopify sinal: R$ 619,98
- Brief interno: Validar disponibilidade e custo para Camiseta Saint Studio Boxy. Quantidade é referência de cotação, não compra aprovada. SST-6502622-M tamanho M/M: ref 0 un, teto custo 50% margem R$ 155,00, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

### 8. Bearbrick Series 48
- Itens: 1 | P0: 0 | P1: 1
- Quantidade referência para cotação: 0
- Receita Shopify sinal: R$ 449,97
- Brief interno: Validar disponibilidade e custo para Bearbrick Series 48. Quantidade é referência de cotação, não compra aprovada. MED-3410398-OS tamanho sem tamanho informado: ref 0 un, teto custo 50% margem R$ 75,00, prioridade P1. Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.

## Top itens com teto de custo

### 1. Tênis New Balance 9060 Rich Oak Marrom | 37
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `U9060CCC-4` | família: New Balance 9060
- Venda Shopify: 3 un, R$ 8.399,97, preço médio R$ 2.799,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 1.539,99 / R$ 1.399,99 / R$ 1.260,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 2. Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom | 38
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `HV8547-200-38` | família: Nike Moon Shoe SP Jacquemus
- Venda Shopify: 2 un, R$ 11.999,98, preço médio R$ 5.999,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 3.299,99 / R$ 2.999,99 / R$ 2.700,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 3. Tênis Nike Moon Shoe SP Jacquemus Off White | 36
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `HV8547-002-36` | família: Nike Moon Shoe SP Jacquemus
- Venda Shopify: 2 un, R$ 10.999,98, preço médio R$ 5.499,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 3.024,99 / R$ 2.749,99 / R$ 2.475,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 4. Tênis Nike Mind 002 Light Smoke Grey Cinza | 36
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `HQ4308-003-5` | família: Nike Mind 002
- Venda Shopify: 2 un, R$ 6.399,98, preço médio R$ 3.199,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 1.759,99 / R$ 1.599,99 / R$ 1.440,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 5. Tênis New Balance 9060 Sea Salt Moonbeam Branco | 37
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `U9060WHT-4` | família: New Balance 9060
- Venda Shopify: 2 un, R$ 5.199,98, preço médio R$ 2.599,99
- Tiny saldo: `-1.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 1.429,99 / R$ 1.299,99 / R$ 1.170,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 6. Polo Comme des Garçons PLAY Red Emblem White Branco | G/L
- Prioridade: P0 | status: `quote_preview_candidate`
- SKU: `CDGP2` | família: Comme des Garçons PLAY Polo
- Venda Shopify: 2 un, R$ 3.599,98, preço médio R$ 1.799,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 3
- Teto custo para margem 45/50/55%: R$ 989,99 / R$ 900,00 / R$ 810,00
- Gate lead time: p0_lead_time_sensitive | P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.
- Próximo passo interno: Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.

### 7. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto | 34
- Prioridade: P1 | status: `validate_before_quote`
- SKU: `HV8547-001-1` | família: Nike Moon Shoe SP Jacquemus
- Venda Shopify: 1 un, R$ 6.999,99, preço médio R$ 6.999,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 1
- Teto custo para margem 45/50/55%: R$ 3.849,99 / R$ 3.499,99 / R$ 3.150,00
- Gate lead time: p1_optional_or_bundle | P1 não é autorização de compra; cotar só se fizer sentido comercial.
- Próximo passo interno: Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.

### 8. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto | 40
- Prioridade: P1 | status: `validate_before_quote`
- SKU: `HV8547-001-7` | família: Nike Moon Shoe SP Jacquemus
- Venda Shopify: 1 un, R$ 6.999,99, preço médio R$ 6.999,99
- Tiny saldo: `0.0`
- Quantidade referência para cotação, não compra: 1
- Teto custo para margem 45/50/55%: R$ 3.849,99 / R$ 3.499,99 / R$ 3.150,00
- Gate lead time: p1_optional_or_bundle | P1 não é autorização de compra; cotar só se fizer sentido comercial.
- Próximo passo interno: Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.

### 9. Tênis New Balance 530 Silver White Branco | 38
- Prioridade: P1 | status: `validate_before_quote`
- SKU: `MR530EMA-5` | família: New Balance 530
- Venda Shopify: 3 un, R$ 5.999,97, preço médio R$ 1.999,99
- Tiny saldo: `1.0`
- Quantidade referência para cotação, não compra: 2
- Teto custo para margem 45/50/55%: R$ 1.099,99 / R$ 1.000,00 / R$ 900,00
- Gate lead time: p1_optional_or_bundle | P1 não é autorização de compra; cotar só se fizer sentido comercial.
- Próximo passo interno: Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.

### 10. Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa | 37
- Prioridade: P1 | status: `validate_before_quote`
- SKU: `HV8547-601-37` | família: Nike Moon Shoe SP Jacquemus
- Venda Shopify: 2 un, R$ 11.999,98, preço médio R$ 5.999,99
- Tiny saldo: `2.0`
- Quantidade referência para cotação, não compra: 2
- Teto custo para margem 45/50/55%: R$ 3.299,99 / R$ 2.999,99 / R$ 2.700,00
- Gate lead time: p1_optional_or_bundle | P1 não é autorização de compra; cotar só se fizer sentido comercial.
- Próximo passo interno: Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.

### 11. Tênis New Balance 9060 Angora Sea Salt Bege | 36
- Prioridade: P1 | status: `validate_before_quote`
- SKU: `U9060ERB-3` | família: New Balance 9060
- Venda Shopify: 2 un, R$ 5.199,98, preço médio R$ 2.599,99
- Tiny saldo: `1.0`
- Quantidade referência para cotação, não compra: 2
- Teto custo para margem 45/50/55%: R$ 1.429,99 / R$ 1.299,99 / R$ 1.170,00
- Gate lead time: p1_optional_or_bundle | P1 não é autorização de compra; cotar só se fizer sentido comercial.
- Próximo passo interno: Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.

### 12. MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado) | sem tamanho informado
- Prioridade: P1 | status: `sku_resolution_first`
- SKU: `MED-3410398-OS` | família: Bearbrick Series 48
- Venda Shopify: 3 un, R$ 449,97, preço médio R$ 149,99
- Tiny saldo: `n/d`
- Quantidade referência para cotação, não compra: 0
- Teto custo para margem 45/50/55%: R$ 82,49 / R$ 75,00 / R$ 67,50
- Gate lead time: blocked_until_sku_tiny_resolution | Resolver SKU/Tiny antes de cotar ou comprar.
- Próximo passo interno: Resolver SKU/Tiny antes de qualquer cotação externa.

### 13. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo | 36
- Prioridade: P1 | status: `sku_resolution_first`
- SKU: `1183C102751-3` | família: Onitsuka Tiger Mexico 66
- Venda Shopify: 2 un, R$ 4.799,98, preço médio R$ 2.399,99
- Tiny saldo: `n/d`
- Quantidade referência para cotação, não compra: 0
- Teto custo para margem 45/50/55%: R$ 1.319,99 / R$ 1.199,99 / R$ 1.080,00
- Gate lead time: blocked_until_sku_tiny_resolution | Resolver SKU/Tiny antes de cotar ou comprar.
- Próximo passo interno: Resolver SKU/Tiny antes de qualquer cotação externa.

### 14. Camiseta Saint Studio Boxy Supima Breuer Preto | M/M
- Prioridade: P1 | status: `sku_resolution_first`
- SKU: `SST-6502622-M` | família: Camiseta Saint Studio Boxy
- Venda Shopify: 2 un, R$ 619,98, preço médio R$ 309,99
- Tiny saldo: `n/d`
- Quantidade referência para cotação, não compra: 0
- Teto custo para margem 45/50/55%: R$ 170,49 / R$ 155,00 / R$ 139,50
- Gate lead time: blocked_until_sku_tiny_resolution | Resolver SKU/Tiny antes de cotar ou comprar.
- Próximo passo interno: Resolver SKU/Tiny antes de qualquer cotação externa.

## O que não foi feito

- Nenhum fornecedor foi contatado.
- Nenhuma compra, PO ou reserva foi feita.
- Nenhum write em Shopify, Tiny, preço, estoque, campanha, cliente ou banco de produção.
- Nenhum envio externo e nenhum cron ativado.

## Aprovação necessária para avançar

Para enviar qualquer brief a fornecedor, Lucas/Júlio precisam aprovar destino, escopo, itens e quantidade de cotação. Compra continua sendo uma aprovação separada depois de custo, lead time e margem reais.
