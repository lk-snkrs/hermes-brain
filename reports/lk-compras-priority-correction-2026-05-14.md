# LK Compras — Correção de prioridade: demanda + estoque + margem

Gerado em: `2026-05-14T23:32:22.941640+00:00`

Status: `priority_logic_corrected_no_external_writes`

## Correção Lucas

> Se o Alabaster 37.5 vendeu apenas 1 unidade, por que ele seria prioridade? Prioridade deveria ser produto/tamanho que mais vendemos e está zerado no Tiny ou está para acabar.

## Regra corrigida

- Prioridade não é “existe no Droper” nem “sem match no Droper”.
- Prioridade é: **demanda real por produto/tamanho + Tiny zerado ou estoque baixo + viabilidade econômica**.
- 1 venda em 120 dias vira backlog/watchlist, não prioridade, salvo exceção estratégica explícita.
- “Está para acabar” precisa ser tratado como fila separada de `low_stock`: Tiny > 0, mas abaixo de limiar dado pela velocidade de venda.
- Droper/grupo e fora/importação são alternativas no mesmo card, depois da priorização.

## Heurística corrigida usada agora

- P1: 5+ unidades vendidas em 120d e Tiny zerado/baixo.
- P2: 3–4 unidades vendidas em 120d e Tiny zerado/baixo.
- P3: 2 unidades vendidas em 120d; watchlist.
- P4: 1 unidade vendida em 120d; backlog, não prioridade automática.

## Resultado por prioridade

- `P1_restock_candidate_high_demand`: 4
- `P2_restock_candidate_medium_demand`: 10
- `P4_backlog_not_priority_single_sale`: 4

## Correção específica — Alabaster 37.5

- Produto: Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37.5
- SKU: `HV8547-700-10`
- Vendas 120d: 1 un
- Classificação corrigida: `P4_backlog_not_priority_single_sale`
- Conclusão: não deve ser prioridade operacional agora; fica em backlog/watchlist ou exceção estratégica se Lucas/Júlio quiserem especificamente esse tamanho.

## Ranking corrigido

### 1. Tênis New Balance 204L Arid Timberwolf Bege — 37
- SKU: `U204LMMC-4`
- Vendas 120d: 8 un
- Receita 120d: R$ 22.399,92
- Preço médio vendido: R$ 2.799,99
- Prioridade corrigida: `P1_restock_candidate_high_demand`
- Rota econômica: `compare_import_before_national_buy`
- Margem Droper antes de taxas/frete/imposto: R$ 800,09 (28,6%)

### 2. Tênis New Balance 204L Arid Timberwolf Bege — 39
- SKU: `U204LMMC-6`
- Vendas 120d: 7 un
- Receita 120d: R$ 19.599,93
- Preço médio vendido: R$ 2.799,99
- Prioridade corrigida: `P1_restock_candidate_high_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ 419,99 (15,0%)

### 3. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 38
- SKU: `1183A201-126-5`
- Vendas 120d: 6 un
- Receita 120d: R$ 14.399,94
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P1_restock_candidate_high_demand`
- Rota econômica: `compare_import_before_national_buy`
- Margem Droper antes de taxas/frete/imposto: R$ 509,99 (21,2%)

### 4. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 37
- SKU: `1183A201-126-4`
- Vendas 120d: 5 un
- Receita 120d: R$ 11.999,95
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P1_restock_candidate_high_demand`
- Rota econômica: `compare_import_before_national_buy`
- Margem Droper antes de taxas/frete/imposto: R$ 509,99 (21,2%)

### 5. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 38
- SKU: `HV8547-700-5`
- Vendas 120d: 4 un
- Receita 120d: R$ 23.999,96
- Preço médio vendido: R$ 5.999,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ -500,01 (-8,3%)

### 6. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37
- SKU: `HV8547-700-4`
- Vendas 120d: 4 un
- Receita 120d: R$ 19.999,96
- Preço médio vendido: R$ 4.999,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ -1.500,01 (-30,0%)

### 7. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — 41.5
- SKU: `1183C102.751`
- Vendas 120d: 4 un
- Receita 120d: R$ 9.599,96
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `compare_import_before_national_buy`
- Margem Droper antes de taxas/frete/imposto: R$ 509,99 (21,2%)

### 8. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 35
- SKU: `JR9446-2`
- Vendas 120d: 4 un
- Receita 120d: R$ 8.799,96
- Preço médio vendido: R$ 2.199,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `national_possible_but_compare_import_group`
- Margem Droper antes de taxas/frete/imposto: R$ 900,00 (40,9%)

### 9. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 36
- SKU: `HV8547-700-3`
- Vendas 120d: 3 un
- Receita 120d: R$ 15.999,97
- Preço médio vendido: R$ 5.333,32
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `lookup_import_only_if_priority_or_strategic_exception`
- Margem Droper antes de taxas/frete/imposto: n/d

### 10. Tênis New Balance 204L Arid Timberwolf Bege — 38
- SKU: `U204LMMC-5`
- Vendas 120d: 3 un
- Receita 120d: R$ 8.399,97
- Preço médio vendido: R$ 2.799,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `compare_import_before_national_buy`
- Margem Droper antes de taxas/frete/imposto: R$ 800,09 (28,6%)

### 11. Tênis New Balance 204L Arid Timberwolf Bege — 40
- SKU: `U204LMMC-7`
- Vendas 120d: 3 un
- Receita 120d: R$ 8.399,97
- Preço médio vendido: R$ 2.799,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ 419,99 (15,0%)

### 12. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 36
- SKU: `1183A201-126-3`
- Vendas 120d: 3 un
- Receita 120d: R$ 7.199,97
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ 400,00 (16,7%)

### 13. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 40
- SKU: `1183A201-126-7`
- Vendas 120d: 3 un
- Receita 120d: R$ 7.199,97
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ 10,29 (0,4%)

### 14. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 36
- SKU: `JR9446-3`
- Vendas 120d: 3 un
- Receita 120d: R$ 6.599,97
- Preço médio vendido: R$ 2.199,99
- Prioridade corrigida: `P2_restock_candidate_medium_demand`
- Rota econômica: `national_possible_but_compare_import_group`
- Margem Droper antes de taxas/frete/imposto: R$ 1.300,99 (59,1%)

### 15. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37.5
- SKU: `HV8547-700-10`
- Vendas 120d: 1 un
- Receita 120d: R$ 4.999,99
- Preço médio vendido: R$ 4.999,99
- Prioridade corrigida: `P4_backlog_not_priority_single_sale`
- Rota econômica: `lookup_import_only_if_priority_or_strategic_exception`
- Margem Droper antes de taxas/frete/imposto: n/d

### 16. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 42.5
- SKU: `1183C015101`
- Vendas 120d: 1 un
- Receita 120d: R$ 2.499,99
- Preço médio vendido: R$ 2.499,99
- Prioridade corrigida: `P4_backlog_not_priority_single_sale`
- Rota econômica: `lookup_import_only_if_priority_or_strategic_exception`
- Margem Droper antes de taxas/frete/imposto: n/d

### 17. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 35
- SKU: `1183A201-126-2`
- Vendas 120d: 1 un
- Receita 120d: R$ 2.399,99
- Preço médio vendido: R$ 2.399,99
- Prioridade corrigida: `P4_backlog_not_priority_single_sale`
- Rota econômica: `import_or_skip_national_not_viable`
- Margem Droper antes de taxas/frete/imposto: R$ 200,00 (8,3%)

### 18. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 38
- SKU: `JR9446-5`
- Vendas 120d: 1 un
- Receita 120d: R$ 2.199,99
- Preço médio vendido: R$ 2.199,99
- Prioridade corrigida: `P4_backlog_not_priority_single_sale`
- Rota econômica: `national_possible_but_compare_import_group`
- Margem Droper antes de taxas/frete/imposto: R$ 900,00 (40,9%)

## Não executado

- Nenhum Notion write.
- Nenhuma compra/reserva.
- Nenhum contato/WhatsApp.
- Nenhum lookup StockX/GOAT.
- Nenhum write Shopify/Tiny/Merchant.