# Dry-run V2 com guardrails — Auto-ordenação de coleções Shopify LK

Data: 2026-05-26T13:56:13.122604+00:00
Modo: read-only / sem mutations / sem Shopify writes

## Resumo executivo

- Coleções lidas: 177
- Coleções elegíveis após guardrails: 118
- Coleções puladas/revisão manual: 59
- Coleções elegíveis cujo top 8 mudaria: 104
- Pilotos recomendados: 10
- API calls Shopify read-only: 206
- Acessos/GA4: não usados nesta rodada; score baseado em vendas locais 180d (unidades + receita).

## Guardrails aplicados

- Top 8 protegido: mínimo 4 slots para best-sellers/performance.
- Novidade limitada: máximo 4 slots de produtos novos 90d no top 8.
- Excluir da primeira aplicação coleções amplas com mais de 250 produtos.
- Exigir sort manual; coleções com sort nativo Shopify continuam só em preview.
- Sale/outlet/promo/collab/todos: revisão manual antes de qualquer apply.

## Coleções piloto recomendadas

### Nude Project (`/nude-project`)
- Produtos: 90; novos 90d: 7; movimentos estimados: 79 (88%); score piloto: 77.5556
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 4 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Camiseta Nude Project Global Soon — motivo: best_seller_protegido; antes: #7; vendas 180d: 7 un / R$ 6999.93
  - 2. Camiseta Nude Project Global Soon Black Preto — motivo: best_seller_protegido; antes: #10; vendas 180d: 4 un / R$ 3999.96
  - 3. Moletom Nude Project Kill Bill Zip-Up Ash Cinza — motivo: best_seller_protegido; antes: #49; vendas 180d: 3 un / R$ 4699.97
  - 4. Camiseta Nude Project Xoxo Cinza — motivo: best_seller_protegido; antes: #8; vendas 180d: 2 un / R$ 1999.98
  - 5. Moletom Nude Project Cult Hoodie Black/Beige Preto — motivo: novo_90d_limitado; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 6. Moletom Nude Project Side-Eye Zip-Up Black Preto — motivo: novo_90d_limitado; antes: #2; vendas 180d: 0 un / R$ 0.0
  - 7. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo — motivo: novo_90d_limitado; antes: #38; vendas 180d: 0 un / R$ 0.0
  - 8. Camiseta Nude Project Kora Black Preto — motivo: novo_90d_limitado; antes: #3; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Nude Project Honor Tee Marshmallow Off White (#4); Camiseta Nude Project Honor Tee Black Preto (#5); Camiseta Nude Project Berry Tee White Branco (#6)

### Jacquemus (`/jacquemus`)
- Produtos: 35; novos 90d: 4; movimentos estimados: 17 (49%); score piloto: 76.375
- Mix top 8: 4 best-sellers protegidos; 2 novidades; 0 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — motivo: best_seller_protegido; antes: #4; vendas 180d: 46 un / R$ 237899.55
  - 2. Tênis Nike Moon Shoe SP Jacquemus Off White — motivo: best_seller_protegido; antes: #2; vendas 180d: 42 un / R$ 209999.58
  - 3. Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom — motivo: best_seller_protegido; antes: #1; vendas 180d: 30 un / R$ 149999.7
  - 4. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto — motivo: best_seller_protegido; antes: #5; vendas 180d: 25 un / R$ 131999.76
  - 5. Tênis Nike Moon Shoe SP Jacquemus University Red Vermelho — motivo: novo_90d_limitado; antes: #6; vendas 180d: 23 un / R$ 129799.79
  - 6. Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa — motivo: novo_90d_limitado; antes: #3; vendas 180d: 3 un / R$ 14999.97
  - 7. Óculos de Sol Jacquemus JAC4C2SUN Animal Print — motivo: fallback_performance; antes: #30; vendas 180d: 1 un / R$ 1749.99
  - 8. Boné Jacquemus La Casquette Artichaut Black Preto — motivo: fallback_performance; antes: #7; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Jacquemus x Nike Logo Branco (#8)

### Saint Studio (`/saint-studio`)
- Produtos: 82; novos 90d: 17; movimentos estimados: 82 (100%); score piloto: 75.5
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 4 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Camiseta Saint Studio Classy Suedine Supima Chairs Branco — motivo: best_seller_protegido; antes: #12; vendas 180d: 15 un / R$ 5117.85
  - 2. Calça Saint Studio Alfaiataria Leve Prega Dupla Marrom — motivo: best_seller_protegido; antes: #19; vendas 180d: 6 un / R$ 3719.94
  - 3. Calça Saint Studio Alfaiataria Leve Prega Dupla Preta — motivo: best_seller_protegido; antes: #15; vendas 180d: 4 un / R$ 2479.96
  - 4. Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza — motivo: best_seller_protegido; antes: #16; vendas 180d: 4 un / R$ 2479.96
  - 5. Meia Saint Studio Pima Branco — motivo: novo_90d_limitado; antes: #82; vendas 180d: 0 un / R$ 0.0
  - 6. Meia Saint Studio Pima Marrom — motivo: novo_90d_limitado; antes: #81; vendas 180d: 0 un / R$ 0.0
  - 7. Meia Saint Studio Pima Cooper Bege — motivo: novo_90d_limitado; antes: #80; vendas 180d: 0 un / R$ 0.0
  - 8. Suéter Saint Studio Moletom Quarter Zip Marrom — motivo: novo_90d_limitado; antes: #79; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Saint Studio Oversized Suedine Supima Areia Bege (#1); Shorts Saint Studio Plissado Tech Preto (#2); Camisa Saint Studio Pima Listrada Azul (#3); Shorts Saint Studio Everywear Preto (#4); Shorts Saint Studio Everywear Caqui Bege (#5); Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto (#6); Calça Saint Studio Jeans Baggy Risca de Giz Azul (#7); Camiseta Saint Studio Boxy Supima Off Gola Vermelha Branco (#8)

### Calça | Apparels (`/calca-streetwear`)
- Produtos: 70; novos 90d: 5; movimentos estimados: 68 (97%); score piloto: 75.2143
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 1 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Calça Alo Yoga Suit Up Trouser (Regular) Preto — motivo: best_seller_protegido; antes: #5; vendas 180d: 24 un / R$ 37199.76
  - 2. Calça Alo Yoga Suit Up Trouser (Long) Preto — motivo: best_seller_protegido; antes: #3; vendas 180d: 10 un / R$ 15499.9
  - 3. Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho — motivo: best_seller_protegido; antes: #6; vendas 180d: 7 un / R$ 10849.93
  - 4. Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Gravel Bege — motivo: best_seller_protegido; antes: #7; vendas 180d: 6 un / R$ 9599.94
  - 5. Calça Pace PF SweatPants Preto — motivo: novo_90d_limitado; antes: #68; vendas 180d: 7 un / R$ 3119.93
  - 6. Calça Saint Studio Wide Alfaiataria Caqui — motivo: novo_90d_limitado; antes: #59; vendas 180d: 3 un / R$ 1249.97
  - 7. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo — motivo: novo_90d_limitado; antes: #34; vendas 180d: 0 un / R$ 0.0
  - 8. Calça Saint Studio Jeans Baggy Risca de Giz Azul — motivo: novo_90d_limitado; antes: #1; vendas 180d: 1 un / R$ 489.99
- Sairiam do top 8: Calça Pace Nomo Tailoring Trousers Preto (#2); Calça Saint Studio Wide Cargo Preta (#4); Calça Saint Studio Alfaiataria Leve Prega Dupla Preta (#8)

### Pace (`/pace`)
- Produtos: 75; novos 90d: 7; movimentos estimados: 75 (100%); score piloto: 75.125
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 3 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Calça Pace PF SweatPants Preto — motivo: best_seller_protegido; antes: #5; vendas 180d: 7 un / R$ 3119.93
  - 2. Camiseta Pace Double Satire Off White — motivo: best_seller_protegido; antes: #8; vendas 180d: 6 un / R$ 1349.94
  - 3. Regata Pace Waffle Knit Off White — motivo: best_seller_protegido; antes: #10; vendas 180d: 6 un / R$ 1103.94
  - 4. Regata Pace Pattent Dark Grey Cinza — motivo: best_seller_protegido; antes: #9; vendas 180d: 5 un / R$ 874.95
  - 5. Camiseta Pace Óxido Cotton Code Grey Cinza — motivo: novo_90d_limitado; antes: #75; vendas 180d: 0 un / R$ 0.0
  - 6. Camiseta Pace Tsuho Regular Stone Washed Black Preto — motivo: novo_90d_limitado; antes: #74; vendas 180d: 0 un / R$ 0.0
  - 7. Suéter Pace Overlock Black Vintage Preto — motivo: novo_90d_limitado; antes: #73; vendas 180d: 0 un / R$ 0.0
  - 8. Calça Pace Nomo Tailoring Trousers Preto — motivo: novo_90d_limitado; antes: #1; vendas 180d: 1 un / R$ 1099.99
- Sairiam do top 8: Camiseta Pace Buero Washed Black Preto (#2); Camiseta Pace Buero Off White (#3); Camiseta Pace Cotton Code Preta (#4); Camiseta Pace Cotton Code Branca (#6); Camisa Pace EOT Cuban Collar Preto (#7)

### Aimé Leon Dore (`/aime-leon-dore`)
- Produtos: 89; novos 90d: 11; movimentos estimados: 89 (100%); score piloto: 74.625
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 4 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Camiseta Aimé Leon Dore Unisphere Pristine Off White — motivo: best_seller_protegido; antes: #8; vendas 180d: 7 un / R$ 9099.93
  - 2. Boné 5 Panel Aimé Leon Dore Unisphere Branco — motivo: best_seller_protegido; antes: #62; vendas 180d: 5 un / R$ 4999.95
  - 3. Camiseta Aimé Leon Dore Unisphere Preto — motivo: best_seller_protegido; antes: #56; vendas 180d: 4 un / R$ 5199.96
  - 4. Camiseta Aimé Leon Dore Unisphere Black White Preto — motivo: best_seller_protegido; antes: #7; vendas 180d: 3 un / R$ 3899.97
  - 5. Camiseta Aimé Leon Dore Postcard Cream Bege — motivo: novo_90d_limitado; antes: #89; vendas 180d: 0 un / R$ 0.0
  - 6. Camisa Aimé Leon Dore Soccer Jersey Pristine Bege — motivo: novo_90d_limitado; antes: #88; vendas 180d: 0 un / R$ 0.0
  - 7. Camiseta Aimé Leon Dore Dove Breakfast White Branco — motivo: novo_90d_limitado; antes: #87; vendas 180d: 0 un / R$ 0.0
  - 8. Camiseta Aimé Leon Dore Saint George Asphalt Preto — motivo: novo_90d_limitado; antes: #86; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (#1); Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White (#2); Camiseta Aimé Leon Dore Embroidered Logo Marrom (#3); Camiseta Aimé Leon Dore Unisphere Verde (#4); Camiseta Aimé Leon Dore Musician Graphic Off White (#5); Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White (#6)

### Nike Mind (`/nike-mind-001`)
- Produtos: 18; novos 90d: 11; movimentos estimados: 12 (67%); score piloto: 74.25
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 3 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza — motivo: best_seller_protegido; antes: #4; vendas 180d: 37 un / R$ 111699.64
  - 2. Chinelo Slide Nike Mind 001 Black Chrome Preto — motivo: best_seller_protegido; antes: #2; vendas 180d: 26 un / R$ 81599.74
  - 3. Tênis Nike Mind 002 Light Smoke Grey Cinza — motivo: best_seller_protegido; antes: #3; vendas 180d: 12 un / R$ 37599.88
  - 4. Chinelo Slide Nike Mind 001 Light Bone Bege — motivo: best_seller_protegido; antes: #5; vendas 180d: 11 un / R$ 32949.9
  - 5. Tênis Nike Mind 002 Grey Football Grey Cinza — motivo: novo_90d_limitado; antes: #10; vendas 180d: 1 un / R$ 3199.99
  - 6. Chinelo Slide Nike Mind 001 Blackened Blue Azul — motivo: novo_90d_limitado; antes: #12; vendas 180d: 0 un / R$ 0.0
  - 7. Chinelo Slide Nike Mind 001 Mineral Slate Verde — motivo: novo_90d_limitado; antes: #13; vendas 180d: 0 un / R$ 0.0
  - 8. Chinelo Slide Nike Mind 001 Pearl Pink Rosa — motivo: novo_90d_limitado; antes: #14; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis Nike Mind 002 Black Hyper Crimson Preto (#1); Tênis Nike Mind 002 Light Khaki Bege (#6); Chinelo Slide Nike Mind 001 Solar Red Vermelho (#7); Tênis Nike Mind 002 Sail Bege (#8)

### Onitsuka Tiger Mexico 66 (`/onitsuka-tiger-mexico-66`)
- Produtos: 101; novos 90d: 7; movimentos estimados: 98 (97%); score piloto: 73.8676
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 3 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — motivo: best_seller_protegido; antes: #1; vendas 180d: 77 un / R$ 184799.23
  - 2. Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — motivo: best_seller_protegido; antes: #3; vendas 180d: 47 un / R$ 103399.53
  - 3. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — motivo: best_seller_protegido; antes: #4; vendas 180d: 44 un / R$ 109999.56
  - 4. Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege — motivo: best_seller_protegido; antes: #2; vendas 180d: 39 un / R$ 97399.61
  - 5. Tênis Onitsuka Tiger Mexico 66 Fringe Yellow/Black Amarelo — motivo: novo_90d_limitado; antes: #101; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — motivo: novo_90d_limitado; antes: #81; vendas 180d: 1 un / R$ 2999.99
  - 7. Tênis Onitsuka Tiger Mexico 66 Fringe Black/Black Preto — motivo: novo_90d_limitado; antes: #100; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — motivo: novo_90d_limitado; antes: #99; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis Onitsuka Tiger Mexico 66 White Black Branco (#5); Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege (#6); Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom (#7); Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata (#8)

### Onitsuka Tiger Mexico 66 Sabot (`/onitsuka-tiger-mexico-66-sabot`)
- Produtos: 13; novos 90d: 4; movimentos estimados: 10 (77%); score piloto: 73.1442
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 4 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — motivo: best_seller_protegido; antes: #1; vendas 180d: 47 un / R$ 103399.53
  - 2. Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege — motivo: best_seller_protegido; antes: #2; vendas 180d: 30 un / R$ 65999.7
  - 3. Tênis Onitsuka Tiger Mexico 66 Sabot Oatmeal Habanero Bege — motivo: best_seller_protegido; antes: #7; vendas 180d: 13 un / R$ 28599.87
  - 4. Tênis Onitsuka Tiger Mexico 66 Sabot Black Cream Preto — motivo: best_seller_protegido; antes: #3; vendas 180d: 10 un / R$ 21999.9
  - 5. Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — motivo: novo_90d_limitado; antes: #13; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Onitsuka Tiger Mexico 66 Sabot Black/Black Preto — motivo: novo_90d_limitado; antes: #12; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis Onitsuka Tiger Mexico 66 Sabot Dark Brown Marrom — motivo: novo_90d_limitado; antes: #11; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis Onitsuka Tiger Mexico 66 Sabot Natural Cream Bege — motivo: novo_90d_limitado; antes: #10; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis Onitsuka Tiger Mexico 66 Sabot Cream Mustard Bege (#4); Tênis Onitsuka Tiger Mexico 66 Sabot Crystal Pink Cream Rosa (#5); Tênis Onitsuka Tiger Mexico 66 Sabot Iron Navy Cream Azul (#6); Tênis Onitsuka Tiger Mexico 66 Sabot Cream Kale Bege (#8)

### Shorts (`/shorts`)
- Produtos: 28; novos 90d: 4; movimentos estimados: 24 (86%); score piloto: 72.8214
- Mix top 8: 4 best-sellers protegidos; 4 novidades; 3 novidades sem venda 180d.
- Top 8 proposto:
  - 1. Shorts Fear Of God Essentials Classic Sweatshort Vintage Black Preto — motivo: best_seller_protegido; antes: #5; vendas 180d: 3 un / R$ 3599.97
  - 2. Shorts Slyce Frenchterry Off White — motivo: best_seller_protegido; antes: #6; vendas 180d: 3 un / R$ 910.29
  - 3. Shorts Aphase Relaxed - Stoned Black Preto — motivo: best_seller_protegido; antes: #11; vendas 180d: 3 un / R$ 776.97
  - 4. Shorts Pace Midmasa Tailored Charcoal — motivo: best_seller_protegido; antes: #13; vendas 180d: 2 un / R$ 1035.99
  - 5. Shorts Saint Studio Plissado Tech Preto — motivo: novo_90d_limitado; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 6. Shorts Saint Studio Everywear Preto — motivo: novo_90d_limitado; antes: #2; vendas 180d: 0 un / R$ 0.0
  - 7. Shorts Saint Studio Everywear Caqui Bege — motivo: novo_90d_limitado; antes: #3; vendas 180d: 0 un / R$ 0.0
  - 8. Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto — motivo: novo_90d_limitado; antes: #4; vendas 180d: 1 un / R$ 449.99
- Sairiam do top 8: Shorts Represent Clo Owners Club Flat White Branco (#7); Shorts Represent Clo Owners Club Flat Black Preto (#8)

## Coleções amplas/sensíveis excluídas da primeira aplicação

- Todos os Produtos (`/ultimos-lancamentos-2`): 2313 produtos; motivo: colecao_ampla_gt_250_produtos
- Tênis e Sneakers Originais (`/sneakers`): 1246 produtos; motivo: colecao_ampla_gt_250_produtos
- Apparels (`/roupas`): 723 produtos; motivo: colecao_ampla_gt_250_produtos
- Nike (`/nike-todos-os-modelos`): 613 produtos; motivo: colecao_ampla_gt_250_produtos
- Camiseta (`/camiseta-1`): 311 produtos; motivo: colecao_ampla_gt_250_produtos
- Adidas (`/adidas-todos-os-modelos`): 265 produtos; motivo: colecao_ampla_gt_250_produtos
- Onitsuka Tiger (`/onitsuka-tiger-todos-os-modelos`): 159 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- New Balance (`/new-balance-todos-os-modelos`): 139 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- On Running (`/on-running-todos-os-modelos`): 22 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Asics (`/asics-todos-os-modelos`): 17 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Puma (`/puma-todos-os-modelos`): 17 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Adidas Handball Spezial (`/adidas-handball-spezial`): 15 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Collab com Artistas (`/collab-com-artistas`): 15 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Adidas Taekwondo Mei Ballet (`/adidas-taekwondo-mei-ballet`): 14 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Dane-se x Rubem Valentim (`/dane-se-x-rubem-valentim`): 10 produtos; motivo: sensivel_revisao_manual_sale_todos_collab
- Vans (`/vans-todos-os-modelos`): 4 produtos; motivo: sensivel_revisao_manual_sale_todos_collab

## Motivos de skip/revisão

- sort_order_nao_manual:best-selling: 22
- menos_de_4_produtos: 11
- sensivel_revisao_manual_sale_todos_collab: 10
- colecao_ampla_gt_250_produtos: 6
- sort_order_nao_manual:created-desc: 6
- sort_order_nao_manual:most-relevant: 4

## Rollback

- Snapshot salvo em `rollback-snapshot-v2-guardrails.json`.
- Para aplicação futura, restaurar `current_order_product_ids` via `collectionReorderProducts`, aguardando job e validando readback.

## Arquivos

- `dry-run-v2-guardrails.json`: relatório completo.
- `top8-preview-v2-guardrails.csv`: preview tabular por coleção/produto.
- `rollback-snapshot-v2-guardrails.json`: ordem atual para rollback futuro.

## Não feito

- Nenhuma mutation Shopify.
- Nenhum cron criado.
- Nenhuma alteração em produto, coleção, estoque, preço, tema, SEO ou campanha.