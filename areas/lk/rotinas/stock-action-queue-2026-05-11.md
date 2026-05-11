# LK Stock Action Queue — influencer → produto/SKU/tamanho → ação

Status: fila operacional read-only para decisão de Lucas. Não é ordem de compra, não contata fornecedor, não altera Shopify/Tiny/Notion e não aciona campanha.
Gerado em: `2026-05-11`. Fonte principal: `reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.json`. Período Shopify/Tiny: `2026-02-09..2026-05-10`.

## Regra de uso
- Shopify informa venda/produto/SKU/tamanho/evidência de origem.
- Tiny `LK | CONTROLE ESTOQUE` informa o estoque operacional.
- Ação `repor estoque` aqui significa **preparar decisão/preview**, não comprar.
- Itens `sem SKU no Shopify` ou `mapear SKU no Tiny` são saneamento de cadastro antes de decisão comercial.
- Sourcing externo/Monbam/Droper só deve ser acionado depois de sinal interno e aprovação Lucas quando envolver contato/compra.

## Resumo executivo
- ruptura agora: 97 linhas
- baixo estoque: 6 linhas
- mapear SKU no Tiny: 8 linhas
- sem SKU no Shopify: 25 linhas
- ok/monitorar: 2 linhas

- Silvia Heinz: 122 linhas; ruptura agora: 86, sem SKU no Shopify: 23, baixo estoque: 6, ok/monitorar: 1, mapear SKU no Tiny: 6
- Helena Lunardelli: 16 linhas; sem SKU no Shopify: 2, ok/monitorar: 1, ruptura agora: 11, mapear SKU no Tiny: 2
- Lala Noleto: sem ponte Shopify direta no recorte; fica fora da fila de estoque até descobrir cupom/UTM/landing/brief/ad_id real.

## Fila A — Preview para Lucas: repor estoque / checar sourcing

Itens com venda casada, SKU presente e estoque Tiny zerado/baixo. Ainda exigem aprovação antes de compra/fornecedor.

1. **Tênis Nike Air Jordan 4 Retro Metallic Gold Branco / SKU AQ9129-170-7 / tam. 40**
   - influencer: Silvia Heinz; vendido no match: 4 un.; receita: R$ 13.399,96; pedidos: 4
   - evidência Shopify: discount_code:4
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
2. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-38 / tam. 38**
   - influencer: Silvia Heinz; vendido no match: 3 un.; receita: R$ 14.999,97; pedidos: 3
   - evidência Shopify: discount_code:3
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
3. **Tênis Onitsuka Tiger Mexico 66 White Black Branco / SKU 1183A201-126-3 / tam. 36**
   - influencer: Silvia Heinz; vendido no match: 3 un.; receita: R$ 7.199,97; pedidos: 3
   - evidência Shopify: discount_code:3
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
4. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom / SKU HV8547-200-38 / tam. 38**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 11.999,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
5. **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-8 / tam. 41**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 11.999,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
6. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-39 / tam. 39**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 9.999,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
7. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-38 / tam. 38**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 9.999,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
8. **Tênis Onitsuka Tiger Mexico 66 Paraty Birch Cream Bege / SKU 1183B601.200-6 / tam. 39**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 4.599,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
9. **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-7 / tam. 40**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 4.399,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
10. **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-5 / tam. 38**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 4.399,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
11. **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-4 / tam. 37**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 4.399,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
12. **Jason Markk Essential Kit de Limpeza / SKU 300110 / tam. [sem variant]**
   - influencer: Silvia Heinz; vendido no match: 2 un.; receita: R$ 399,98; pedidos: 2
   - evidência Shopify: discount_code:2
   - Tiny `LK | CONTROLE ESTOQUE`: -2; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
13. **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-5 / tam. 38**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 5.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
14. **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-7 / tam. 40**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 5.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
15. **Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo / SKU HV8547-700-7 / tam. 40**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 5.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
16. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-36 / tam. 36**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
17. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-39 / tam. 39**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: -1; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
18. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-34 / tam. 34**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
19. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-37 / tam. 37**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
20. **Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa / SKU HV8547-601-34 / tam. 34**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
21. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-37 / tam. 37**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
22. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-36 / tam. 36**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
23. **Tênis Nike Vomero Premium SP Black Mini Chrome Swoosh Preto / SKU IQ0627-001 / tam. 43**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 4.499,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
24. **Tênis Onitsuka Tiger Moage White/White Branco / SKU 1183B555.102-6 / tam. 39**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 3.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta
25. **Tênis Nike Vomero Premium Flat Stout Marrom / SKU IQ0028-200 / tam. 42**
   - influencer: Silvia Heinz; vendido no match: 1 un.; receita: R$ 3.999,99; pedidos: 1
   - evidência Shopify: discount_code:1
   - Tiny `LK | CONTROLE ESTOQUE`: 0; leitura: **ruptura agora**
   - ação recomendada: repor estoque ou checar sourcing; confiança: alta

## Fila B — Corrigir/mapear SKU antes de decidir

1. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 37**
   - influencer: Silvia Heinz; vendido: 3 un.; receita: R$ 14.999,97; evidência: discount_code:2, landing_site:2
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
2. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 36**
   - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 9.999,98; evidência: discount_code:2
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
3. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU [sem SKU no Shopify] / tam. 36**
   - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 9.999,98; evidência: discount_code:2
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
4. **Tênis New Balance 204L Cortado Marrom / SKU [sem SKU no Shopify] / tam. 39**
   - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 5.599,98; evidência: discount_code:2
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
5. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-4 / tam. 37**
   - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.799,98; evidência: discount_code:2
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
6. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU [sem SKU no Shopify] / tam. 38**
   - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 4.999,99; evidência: note_attributes:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
7. **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 38**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
8. **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU [sem SKU no Shopify] / tam. 44**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
9. **Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom / SKU [sem SKU no Shopify] / tam. 36**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.499,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
10. **Tênis Nike Mind 002 Light Khaki Bege / SKU [sem SKU no Shopify] / tam. 41**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.199,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
11. **Tênis Nike Mind 002 Light Smoke Grey Cinza / SKU [sem SKU no Shopify] / tam. 41**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.199,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
12. **Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom / SKU [sem SKU no Shopify] / tam. 42.5**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.999,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
13. **Tênis New Balance 204L Cortado Marrom / SKU [sem SKU no Shopify] / tam. 37**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.799,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
14. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-2 / tam. 35**
   - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
15. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-3 / tam. 36**
   - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 2.399,99; evidência: note_attributes:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
16. **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata / SKU 1183B566021-4 / tam. 37**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
17. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-8 / tam. 42.5**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
18. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-9 / tam. 40**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
19. **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU 1183C102751-6 / tam. 39**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
20. **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata / SKU [sem SKU no Shopify] / tam. 35.5**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
21. **Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege / SKU ONI-3740254-39 / tam. 39**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.199,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **mapear SKU no Tiny**; ação: corrigir/mapear SKU Tiny antes de decisão
22. **Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza / SKU [sem SKU no Shopify] / tam. 38**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.199,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
23. **Moletom Alo Yoga Cropped Serenity Coverup Black Preto / SKU [sem SKU no Shopify] / tam. S/P**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 1.799,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
24. **Tênis Nike Air Jordan 1 Low White University Red Branco / SKU [sem SKU no Shopify] / tam. 36**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 1.499,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
25. **Camiseta Aimé Leon Dore Musician Graphic Off White / SKU [sem SKU no Shopify] / tam. S/P**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 1.299,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
26. **Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza / SKU [sem SKU no Shopify] / tam. L/G**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 619,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
27. **Rhode Pocket Blush / SKU [sem SKU no Shopify] / tam. Sleepy Girl - Soft Mauve**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 399,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
28. **Camiseta Pace Buero Washed Black Preto / SKU [sem SKU no Shopify] / tam. S/P**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 319,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
29. **Camiseta Pace Cotton Code Branca / SKU [sem SKU no Shopify] / tam. G/L**
   - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 216,99; evidência: landing_site:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda
30. **Camiseta Pace Cotton Code Branca / SKU [sem SKU no Shopify] / tam. G/L**
   - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 216,99; evidência: discount_code:1
   - Tiny: sem saldo confiável; leitura: **sem SKU no Shopify**; ação: corrigir SKU Shopify/Tiny via preview; não comprar ainda

## Fila C — Monitorar, sem ação agora

1. **Tênis New Balance 204L Mushroom Arid Stone Marrom / SKU U204LMMA-4 / tam. 37**
   - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 5.599,98; evidência: discount_code:2
   - Tiny: 4; leitura: **ok/monitorar**; ação: não agir; monitorar
2. **Tênis New Balance 204L Arid Timberwolf Bege / SKU U204LMMC-3 / tam. 36**
   - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 2.799,99; evidência: landing_site:1, note_attributes:1
   - Tiny: 2; leitura: **ok/monitorar**; ação: não agir; monitorar

## Preview de decisão para Lucas

Aprovar agora apenas significa autorizar o próximo passo de investigação/execução indicado, não campanha automática.

```text
Aprovo Fila A do Stock Action Queue para checar sourcing/reposição dos itens com ruptura/baixo estoque, sem compra automática e sem contato externo sem novo preview.
```

Opções mais conservadoras:

```text
Aprovo só Silvia Heinz — itens com ruptura agora e SKU presente.
```

```text
Aprovo só Helena Lunardelli — itens com ruptura agora e SKU presente.
```

## Próximas tarefas
- Transformar Fila A aprovada em checagem de sourcing por sinal, priorizando Monbam/Droper quando aplicável.
- Resolver Fila B como saneamento SKU: separar `[sem SKU no Shopify]` de `mapear SKU no Tiny`.
- Atualizar o dicionário campaign/influencer quando handles/cupons oficiais forem confirmados.
- Não criar campanha, Klaviyo, WhatsApp, compra ou alteração de estoque sem aprovação explícita.
