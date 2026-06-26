# LK Compras — Correção de lógica de sourcing econômico Droper/fora

Gerado em: `2026-05-14T23:30:51.494561+00:00`

Status: `corrected_sourcing_economics_payload_no_write`

## Correção Lucas

> O 2 e o 3 são a mesma coisa: ou compramos na Droper/grupo de compras ou trazemos de fora. Sempre usar lógica de margem. Se vendemos um tênis por R$ 2.399, não podemos pagar R$ 2.200 na Droper; nesse caso, se quisermos lucro, tem que trazer de fora ou pular.

## Regra corrigida para o LK OS

- Não existe “card Droper” separado de “card StockX/GOAT”.
- Existe **um card de sourcing por produto/tamanho vendido e zerado**, com alternativas:
  - Droper/grupo de compras/nacional;
  - fora/importação/StockX/GOAT;
  - pular se nenhuma rota fecha margem.
- Droper é primeiro sinal de disponibilidade/preço, não recomendação automática de compra.
- Júlio deve receber decisão comparativa por margem, não só link.

## Heurística provisória usada até calibrar margem alvo

- Margem bruta antes de taxas/frete/imposto < 20%: nacional/Droper não recomendado; buscar fora se quiser lucro.
- 20% a 35%: borderline; comparar fora antes de comprar.
- ≥ 35%: Droper pode ser candidato, mas ainda conferir logística/preço atual.

## Resumo dos 15 com Droper

- `borderline_compare_import_before_buying`: 5
- `droper_economics_too_thin_import_required_if_want_profit`: 5
- `reject_droper_route_import_or_skip`: 2
- `droper_candidate_but_still_compare_import_group_before_buying`: 3

## Payload corrigido — card único de sourcing por item

### 1. Tênis New Balance 204L Arid Timberwolf Bege — 37
- SKU: `U204LMMC-4`
- Demanda 120d: 8 un · R$ 22.399,92
- Preço médio vendido 120d: R$ 2.799,99
- Droper/grupo nacional encontrado: New Balance 204L Mushroom Arid Stone · R$ 1.999,90 · https://droper.app/produto/1102527
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 800,09 (28.6%)
- Rota econômica corrigida: `borderline_compare_import_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 2. Tênis New Balance 204L Arid Timberwolf Bege — 39
- SKU: `U204LMMC-6`
- Demanda 120d: 7 un · R$ 19.599,93
- Preço médio vendido 120d: R$ 2.799,99
- Droper/grupo nacional encontrado: New Balance 204L Mushroom Arid Stone · R$ 2.380,00 · https://droper.app/produto/1089615
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 419,99 (15.0%)
- Rota econômica corrigida: `droper_economics_too_thin_import_required_if_want_profit`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 3. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 38
- SKU: `1183A201-126-5`
- Demanda 120d: 6 un · R$ 14.399,94
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 Black White · R$ 1.890,00 · https://droper.app/produto/980040
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 509,99 (21.2%)
- Rota econômica corrigida: `borderline_compare_import_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 4. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 37
- SKU: `1183A201-126-4`
- Demanda 120d: 5 un · R$ 11.999,95
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 Black White · R$ 1.890,00 · https://droper.app/produto/980040
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 509,99 (21.2%)
- Rota econômica corrigida: `borderline_compare_import_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 5. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 38
- SKU: `HV8547-700-5`
- Demanda 120d: 4 un · R$ 23.999,96
- Preço médio vendido 120d: R$ 5.999,99
- Droper/grupo nacional encontrado: Jacquemus x Nike Moon Shoe SP Alabaster Feminino · R$ 6.500,00 · https://droper.app/produto/1045237
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ -500,01 (-8.3%)
- Rota econômica corrigida: `reject_droper_route_import_or_skip`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 6. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37
- SKU: `HV8547-700-4`
- Demanda 120d: 4 un · R$ 19.999,96
- Preço médio vendido 120d: R$ 4.999,99
- Droper/grupo nacional encontrado: Jacquemus x Nike Moon Shoe SP Alabaster Feminino · R$ 6.500,00 · https://droper.app/produto/1045237
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ -1.500,01 (-30.0%)
- Rota econômica corrigida: `reject_droper_route_import_or_skip`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 7. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — 41.5
- SKU: `1183C102.751`
- Demanda 120d: 4 un · R$ 9.599,96
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 Kill Bill · R$ 1.890,00 · https://droper.app/produto/980772
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 509,99 (21.2%)
- Rota econômica corrigida: `borderline_compare_import_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 8. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 35
- SKU: `JR9446-2`
- Demanda 120d: 4 un · R$ 8.799,96
- Preço médio vendido 120d: R$ 2.199,99
- Droper/grupo nacional encontrado: adidas Samba OG Crochet Sand Strata Sky Tint · R$ 1.299,99 · https://droper.app/produto/1119428
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 900,00 (40.9%)
- Rota econômica corrigida: `droper_candidate_but_still_compare_import_group_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 9. Tênis New Balance 204L Arid Timberwolf Bege — 38
- SKU: `U204LMMC-5`
- Demanda 120d: 3 un · R$ 8.399,97
- Preço médio vendido 120d: R$ 2.799,99
- Droper/grupo nacional encontrado: New Balance 204L Mushroom Arid Stone · R$ 1.999,90 · https://droper.app/produto/1102535
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 800,09 (28.6%)
- Rota econômica corrigida: `borderline_compare_import_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 10. Tênis New Balance 204L Arid Timberwolf Bege — 40
- SKU: `U204LMMC-7`
- Demanda 120d: 3 un · R$ 8.399,97
- Preço médio vendido 120d: R$ 2.799,99
- Droper/grupo nacional encontrado: New Balance 204L Mushroom Arid Stone · R$ 2.380,00 · https://droper.app/produto/1089615
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 419,99 (15.0%)
- Rota econômica corrigida: `droper_economics_too_thin_import_required_if_want_profit`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 11. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 36
- SKU: `1183A201-126-3`
- Demanda 120d: 3 un · R$ 7.199,97
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 White Black · R$ 1.999,99 · https://droper.app/produto/977539
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 400,00 (16.7%)
- Rota econômica corrigida: `droper_economics_too_thin_import_required_if_want_profit`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 12. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 40
- SKU: `1183A201-126-7`
- Demanda 120d: 3 un · R$ 7.199,97
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 White Black · R$ 2.389,70 · https://droper.app/produto/977545
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 10,29 (0.4%)
- Rota econômica corrigida: `droper_economics_too_thin_import_required_if_want_profit`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 13. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 36
- SKU: `JR9446-3`
- Demanda 120d: 3 un · R$ 6.599,97
- Preço médio vendido 120d: R$ 2.199,99
- Droper/grupo nacional encontrado: adidas Samba OG Crochet Sand Strata Sky Tint · R$ 899,00 · https://droper.app/produto/1070315
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 1.300,99 (59.1%)
- Rota econômica corrigida: `droper_candidate_but_still_compare_import_group_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 14. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 35
- SKU: `1183A201-126-2`
- Demanda 120d: 1 un · R$ 2.399,99
- Preço médio vendido 120d: R$ 2.399,99
- Droper/grupo nacional encontrado: Onitsuka Tiger Mexico 66 White Black · R$ 2.199,99 · https://droper.app/produto/1065840
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 200,00 (8.3%)
- Rota econômica corrigida: `droper_economics_too_thin_import_required_if_want_profit`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

### 15. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 38
- SKU: `JR9446-5`
- Demanda 120d: 1 un · R$ 2.199,99
- Preço médio vendido 120d: R$ 2.199,99
- Droper/grupo nacional encontrado: adidas Samba OG Crochet Sand Strata Sky Tint · R$ 1.299,99 · https://droper.app/produto/1119263
- Margem bruta antes de taxas/frete/imposto se comprar na Droper: R$ 900,00 (40.9%)
- Rota econômica corrigida: `droper_candidate_but_still_compare_import_group_before_buying`
- Card Júlio correto: comparar Droper/grupo vs fora/importação; comprar só se margem/logística fizer sentido; caso contrário buscar fora ou pular.

## 3 sem match exato Droper

- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 36 · SKU `HV8547-700-3` · 3 un · R$ 15.999,97 · entra no mesmo card como rota fora/importação/StockX/GOAT se aprovado lookup read-only.
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37.5 · SKU `HV8547-700-10` · 1 un · R$ 4.999,99 · entra no mesmo card como rota fora/importação/StockX/GOAT se aprovado lookup read-only.
- Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 42.5 · SKU `1183C015101` · 1 un · R$ 2.499,99 · entra no mesmo card como rota fora/importação/StockX/GOAT se aprovado lookup read-only.

## Não executado

- Notion write.
- Compra/reserva/pagamento.
- Contato fornecedor/vendedor.
- WhatsApp.
- StockX/GOAT lookup.
- Shopify/Tiny/Merchant write.

## Próximo artefato correto

Gerar, se aprovado, **payload único de sourcing Júlio** com alternativas e decisão econômica por item. Não criar 15 cards Droper como recomendação de compra isolada.