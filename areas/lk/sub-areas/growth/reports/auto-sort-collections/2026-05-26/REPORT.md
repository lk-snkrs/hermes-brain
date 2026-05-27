# Dry-run — Auto-ordenação de coleções Shopify LK

Data: 2026-05-26T13:48:07.320158+00:00
Modo: read-only / sem mutations / sem Shopify writes

## Resumo executivo

- Coleções lidas: 177
- Coleções elegíveis para aplicação futura: 134
- Coleções puladas: 43
- Coleções elegíveis cujo top 8 mudaria: 119
- API calls Shopify read-only: 206
- Acessos/GA4: não usados nesta rodada; score baseado em vendas locais 180d (unidades + receita).

## Critério aplicado

- Primeiro até 8 produtos novos nos últimos 90 dias.
- Se faltar produto novo, completar com best-sellers por score de unidades/receita 180d.
- Restante ordenado por performance, com pequeno bônus de recência.
- Aplicação futura bloqueada para coleções com sort diferente de `manual`.

## Top coleções com mudança no top 8

### Todos os Produtos (`/ultimos-lancamentos-2`)
- Produtos: 2313; novos 90d: 186; movimentos estimados: 2306
- Top 8 proposto:
  - 1. Jaqueta Lululemon Define Nulu Black Plum/Gold Roxo — motivo: novo_90d; antes: #2313; vendas 180d: 0 un / R$ 0.0
  - 2. Jaqueta Lululemon Define Nulu Black/Gold Preto — motivo: novo_90d; antes: #2312; vendas 180d: 0 un / R$ 0.0
  - 3. Camiseta Lululemon Manga Longa Swiftly Tech Shirt 2.0 Hip Length Lotus Lavender Roxo — motivo: novo_90d; antes: #2311; vendas 180d: 0 un / R$ 0.0
  - 4. Jaqueta Lululemon Define Luon White Branco — motivo: novo_90d; antes: #2310; vendas 180d: 0 un / R$ 0.0
  - 5. Meia Saint Studio Pima Branco — motivo: novo_90d; antes: #2309; vendas 180d: 0 un / R$ 0.0
  - 6. Meia Saint Studio Pima Marrom — motivo: novo_90d; antes: #2308; vendas 180d: 0 un / R$ 0.0
  - 7. Meia Saint Studio Pima Cooper Bege — motivo: novo_90d; antes: #2307; vendas 180d: 0 un / R$ 0.0
  - 8. Suéter Saint Studio Moletom Quarter Zip Marrom — motivo: novo_90d; antes: #2306; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis New Balance 9060 Rich Oak Marrom (#1); Mule Lululemon SwayDay Misty Grey Cinza (#2); Mule Lululemon SwayDay Nutmeg Bege (#3); Mule Lululemon SwayDay Black Preto (#4); Mule Lululemon SwayDay Blissful Pink Rosa (#5); Tênis Onitsuka Tiger Moage CO Cream Black Bege (#6); Tênis Adidas Gazelle Stack Collegiate Green Cream White Verde (#7); Tênis New Balance 204L Arid Timberwolf Bege (#8)

### Tênis e Sneakers Originais (`/sneakers`)
- Produtos: 1246; novos 90d: 120; movimentos estimados: 1245
- Top 8 proposto:
  - 1. Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco — motivo: novo_90d; antes: #1246; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Herit Era Ash Cinza — motivo: novo_90d; antes: #1245; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Herit Era Nerano Azul — motivo: novo_90d; antes: #1244; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Herit Age Mink Marrom — motivo: novo_90d; antes: #1243; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis On Running Loewe LightSpray Cloudmonster Branco — motivo: novo_90d; antes: #1242; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis On Running Cloudsolo Loewe Teal Eggshell Azul — motivo: novo_90d; antes: #1241; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis On Running Cloudsolo Loewe Sand Burgundy Bege — motivo: novo_90d; antes: #1240; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis On Running Cloudsolo Loewe Burgundy Eggshell Bordô — motivo: novo_90d; antes: #1239; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis New Balance 204L Arid Timberwolf Bege (#1); Tênis New Balance 204L Mushroom Arid Stone Marrom (#2); Tênis New Balance 9060 Bisque Sea Salt Bege (#3); Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege (#4); Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege (#5); Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege (#6); Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo (#7); Tênis Onitsuka Tiger Mexico 66 White Black Branco (#8)

### Apparels (`/roupas`)
- Produtos: 723; novos 90d: 46; movimentos estimados: 723
- Top 8 proposto:
  - 1. Jaqueta Lululemon Define Nulu Black Plum/Gold Roxo — motivo: novo_90d; antes: #723; vendas 180d: 0 un / R$ 0.0
  - 2. Jaqueta Lululemon Define Nulu Black/Gold Preto — motivo: novo_90d; antes: #722; vendas 180d: 0 un / R$ 0.0
  - 3. Camiseta Lululemon Manga Longa Swiftly Tech Shirt 2.0 Hip Length Lotus Lavender Roxo — motivo: novo_90d; antes: #721; vendas 180d: 0 un / R$ 0.0
  - 4. Jaqueta Lululemon Define Luon White Branco — motivo: novo_90d; antes: #720; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Aimé Leon Dore Postcard Cream Bege — motivo: novo_90d; antes: #719; vendas 180d: 0 un / R$ 0.0
  - 6. Camisa Aimé Leon Dore Soccer Jersey Pristine Bege — motivo: novo_90d; antes: #718; vendas 180d: 0 un / R$ 0.0
  - 7. Camiseta Aimé Leon Dore Dove Breakfast White Branco — motivo: novo_90d; antes: #717; vendas 180d: 0 un / R$ 0.0
  - 8. Camiseta Aimé Leon Dore Saint George Asphalt Preto — motivo: novo_90d; antes: #716; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camisa Saint Studio Pima Listrada Azul (#1); Shorts Saint Studio Everywear Preto (#2); Shorts Saint Studio Everywear Caqui Bege (#3); Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto (#4); Calça Saint Studio Jeans Baggy Risca de Giz Azul (#5); Camiseta Saint Studio Boxy Supima Off Gola Vermelha Branco (#6); Camiseta Saint Studio Boxy Supima It's All Good Preto (#7); Camiseta Saint Studio Boxy Supima Cool Branco (#8)

### Nike (`/nike-todos-os-modelos`)
- Produtos: 613; novos 90d: 54; movimentos estimados: 610
- Top 8 proposto:
  - 1. Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco — motivo: novo_90d; antes: #613; vendas 180d: 0 un / R$ 0.0
  - 2. Tenis Nike Craft General Purpose Shoe Tom Sachs Field Brown Marrom — motivo: novo_90d; antes: #612; vendas 180d: 0 un / R$ 0.0
  - 3. Tenis Nike Craft General Purpose Shoe Tom Sachs Archive Dark Sulfur — motivo: novo_90d; antes: #611; vendas 180d: 0 un / R$ 0.0
  - 4. Tenis Nike Craft General Purpose Shoe Tom Sachs — motivo: novo_90d; antes: #610; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis Tom Sachs x NikeCraft General Purpose Summit White Branco — motivo: novo_90d; antes: #609; vendas 180d: 0 un / R$ 0.0
  - 6. Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul — motivo: novo_90d; antes: #606; vendas 180d: 0 un / R$ 0.0
  - 7. Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa — motivo: novo_90d; antes: #605; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis Nike Air Force 1 Low Protro Kobe Bryant Siempre Hermanos Marrom — motivo: novo_90d; antes: #604; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom (#1); Tênis Nike Moon Shoe SP Jacquemus Off White (#2); Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa (#3); Tênis Nike SB Zoom Air Paul Rodriguez 1 Habanero Red All-Star Vermelho (#4); Tênis Nike Vomero Premium Alabaster Amarelo (#5); Tênis Nike Vomero Premium SP Black Mini Chrome Swoosh Preto (#6); Tênis Nike Vomero Premium Particle Rose Burgundy Rosa (#7); Tênis Nike Vomero Premium Flat Stout Marrom (#8)

### Camiseta (`/camiseta-1`)
- Produtos: 311; novos 90d: 26; movimentos estimados: 309
- Top 8 proposto:
  - 1. Camiseta Lululemon Manga Longa Swiftly Tech Shirt 2.0 Hip Length Lotus Lavender Roxo — motivo: novo_90d; antes: #311; vendas 180d: 0 un / R$ 0.0
  - 2. Camiseta Aimé Leon Dore Postcard Cream Bege — motivo: novo_90d; antes: #310; vendas 180d: 0 un / R$ 0.0
  - 3. Camiseta Aimé Leon Dore Dove Breakfast White Branco — motivo: novo_90d; antes: #309; vendas 180d: 0 un / R$ 0.0
  - 4. Camiseta Aimé Leon Dore Saint George Asphalt Preto — motivo: novo_90d; antes: #308; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Aimé Leon Dore Saint George Coconut Milk Bege — motivo: novo_90d; antes: #307; vendas 180d: 0 un / R$ 0.0
  - 6. Camiseta Pace Óxido Cotton Code Grey Cinza — motivo: novo_90d; antes: #306; vendas 180d: 0 un / R$ 0.0
  - 7. Camiseta Pace Tsuho Regular Stone Washed Black Preto — motivo: novo_90d; antes: #305; vendas 180d: 0 un / R$ 0.0
  - 8. Camiseta Kith Brush Vintage Boxy Alex Silk Off White — motivo: novo_90d; antes: #304; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Saint Studio Boxy Supima Off Gola Vermelha Branco (#1); Camiseta Saint Studio Boxy Supima It's All Good Preto (#2); Camiseta Saint Studio Boxy Supima Cool Branco (#3); Camiseta Saint Studio Boxy Supima Mid Century Branco (#4); Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (#5); Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White (#6); Camiseta Pace Buero Washed Black Preto (#7); Camiseta Pace Buero Off White (#8)

### Adidas (`/adidas-todos-os-modelos`)
- Produtos: 265; novos 90d: 14; movimentos estimados: 265
- Top 8 proposto:
  - 1. Tênis Adidas by Stella McCartney Sportswear X Trainers Bold Gold Amarelo — motivo: novo_90d; antes: #265; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Adidas by Stella McCartney Sportswear X Trainers Core Black Preto — motivo: novo_90d; antes: #264; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Adidas by Stella McCartney Sportswear X Trainers Brown Mauve Gum — motivo: novo_90d; antes: #263; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Adidas by Stella McCartney Sportswear X Trainers Cloud White Ivory Branco — motivo: novo_90d; antes: #262; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis adidas Ballerina Bad Bunny Flamboyan Vermelho — motivo: novo_90d; antes: #261; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Bad Bunny x Adidas BADBO 1.0 Rise Branco — motivo: novo_90d; antes: #242; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis Adidas Taekwondo Mei Ballet Cream White Branco — motivo: novo_90d; antes: #243; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis Adidas Tokyo Mary Jane Crystal Sky Cream White Azul — motivo: novo_90d; antes: #244; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: adidas Wmns Tokyo MJ 'Core Black Cream White Gold Metallic' (#1); Tênis Adidas Samba Disney 101 Dalmatians Penny Branco (#2); Tênis Adidas Samba OG Earth Strata Wonder White Marrom (#3); Tênis Adidas Samba OG Cream White Cardboard Creme (#4); Tênis Adidas Taekwondo Mei Ballet Black Gum Preto (#5); Tênis Adidas Samba OG Crochet Pack Sand Strata Bege (#6); Tênis adidas SL 72 Og Maroon Almost Yellow Marrom (#7); Tênis adidas Yeezy Boost 350 V2 "Steel Grey" Cinza (#8)

### Air Jordan (`/air-jordan`)
- Produtos: 215; novos 90d: 1; movimentos estimados: 204
- Top 8 proposto:
  - 1. Tênis Nike Air Jordan 1 Low SE Repaired Denim Swoosh Azul — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul — motivo: fallback_best_seller; antes: #2; vendas 180d: 9 un / R$ 17999.91
  - 3. Tênis Nike Air Jordan 1 Low SE Gs "Gold Toe" Preto — motivo: fallback_best_seller; antes: #119; vendas 180d: 7 un / R$ 13999.93
  - 4. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Medium Olive Verde — motivo: fallback_best_seller; antes: #67; vendas 180d: 3 un / R$ 29199.98
  - 5. Tênis Nike Air Jordan 4 Retro Metallic Gold Branco — motivo: fallback_best_seller; antes: #4; vendas 180d: 4 un / R$ 11299.96
  - 6. Tênis Nike Air Jordan 1 High Og Black Metallic Gold Preto — motivo: fallback_best_seller; antes: #80; vendas 180d: 4 un / R$ 8799.96
  - 7. Tênis Nike Air Jordan 1 Retro Low OG Zion Williamson Voodoo Alternate Azul — motivo: fallback_best_seller; antes: #17; vendas 180d: 3 un / R$ 11999.97
  - 8. Tênis Nike Air Jordan 3 Retro Black Cat Preto — motivo: fallback_best_seller; antes: #58; vendas 180d: 3 un / R$ 11399.97
- Sairiam do top 8: Tênis Nike Air Jordan 4 RM x Nigel Sylvester Driveway Grey Cinza (#3); Tênis Nike Air Jordan 1 Low Vintage Grey Cinza (#5); Tênis Nike Air Jordan 1 Low "Palomino" Marrom (#6); Tênis Nike Air Jordan 4 Frozen Moments Cinza (#7); Tênis Nike Air Jordan 1 Low Purple Roxo (#8)

### Air Jordan 1 (`/air-jordan-1`)
- Produtos: 206; novos 90d: 6; movimentos estimados: 202
- Top 8 proposto:
  - 1. Tênis Jordan 11 Retro Low University Blue 2026 Azul — motivo: novo_90d; antes: #206; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal — motivo: novo_90d; antes: #205; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Nike Air Jordan 1 Low SE Repaired Denim Swoosh Azul — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Nike Air Jordan 1 High Virgil Abloh Archive x Alaska Branco — motivo: novo_90d; antes: #203; vendas 180d: 1 un / R$ 5999.99
  - 5. Tênis Nike Air Jordan 1 Low OG Chinese New Year 2026 Cinza — motivo: novo_90d; antes: #202; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Nike Air Jordan 1 High Fragment Design x Union LA Varsity Red Branco — motivo: novo_90d; antes: #201; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul — motivo: fallback_best_seller; antes: #2; vendas 180d: 9 un / R$ 17999.91
  - 8. Tênis Nike Air Jordan 1 Low SE Gs "Gold Toe" Preto — motivo: fallback_best_seller; antes: #87; vendas 180d: 7 un / R$ 13999.93
- Sairiam do top 8: Tênis Nike Air Jordan 1 Low Vintage Grey Cinza (#3); Tênis Nike Air Jordan 1 Low "Palomino" Marrom (#4); Tênis Nike Air Jordan 1 Low Purple Roxo (#5); Tênis Nike Air Jordan 1 Low OG Olive Verde (#6); Tênis Nike Air Jordan 1 Mid SE Electro Orange Laranja (#7); Tênis Nike Air Jordan 1 Low White University Red Branco (#8)

### Nike Dunk (`/nike-dunk`)
- Produtos: 180; novos 90d: 0; movimentos estimados: 176
- Top 8 proposto:
  - 1. Tênis Nike Dunk Low Stranger Things Phantom Branco — motivo: fallback_best_seller; antes: #3; vendas 180d: 3 un / R$ 16499.97
  - 2. Tênis Nike Dunk Low Cacao Wow Marrom — motivo: fallback_best_seller; antes: #90; vendas 180d: 3 un / R$ 5099.97
  - 3. Tênis Nike Sb Dunk Low Pro Triple White Branco — motivo: fallback_best_seller; antes: #30; vendas 180d: 3 un / R$ 4799.97
  - 4. Tênis Nike Dunk Low Black OG Panda Preto — motivo: fallback_best_seller; antes: #157; vendas 180d: 3 un / R$ 4799.97
  - 5. Tênis Nike Dunk Sb x Verdy Visty Azul — motivo: fallback_best_seller; antes: #22; vendas 180d: 2 un / R$ 8999.98
  - 6. Tênis Nike Dunk Low SE Animal Colorido — motivo: fallback_best_seller; antes: #71; vendas 180d: 2 un / R$ 5999.98
  - 7. Tênis Nike SB Dunk Low Pro St. Patrick's Day Verde — motivo: fallback_best_seller; antes: #150; vendas 180d: 2 un / R$ 5999.98
  - 8. Nike Dunk SB Dunk Low QS BHM Rodeo Verde — motivo: fallback_best_seller; antes: #10; vendas 180d: 2 un / R$ 4399.98
- Sairiam do top 8: Tênis Nike Air Dunk Jumbo Medium Olive Verde (#1); Tênis Nike Dunk Low SE Australia Marrom (#2); Tênis Nike Dunk Low Baroque Brown Marrom (#4); Livro Rizzoli Nike SB: The Dunk Book (#5); Tênis Nike Dunk Low Cactus Plant Flea Market Swamp Sponge Photo Blue Colorido (#6); Tênis Nike SB Dunk Low Supreme 94 Black Preto (#7); Tênis Nike SB Dunk Low Supreme 94 White Metallic Silver Branco (#8)

### Onitsuka Tiger (`/onitsuka-tiger-todos-os-modelos`)
- Produtos: 159; novos 90d: 18; movimentos estimados: 158
- Top 8 proposto:
  - 1. Tênis Onitsuka Tiger Mexico 66 Fringe Yellow/Black Amarelo — motivo: novo_90d; antes: #138; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — motivo: novo_90d; antes: #131; vendas 180d: 1 un / R$ 2999.99
  - 3. Tênis Onitsuka Tiger Mexico 66 Fringe Black/Black Preto — motivo: novo_90d; antes: #139; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown Blue Marrom — motivo: novo_90d; antes: #140; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — motivo: novo_90d; antes: #141; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Metallic Têniss Silver Gold Prateado — motivo: novo_90d; antes: #142; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Blue Azul — motivo: novo_90d; antes: #130; vendas 180d: 1 un / R$ 8499.99
  - 8. Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege (#2); Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo (#3); Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege (#4); Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege (#5); Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege (#6); Tênis Onitsuka Tiger Mexico 66 White Black Branco (#7); Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege (#8)

### Athleisure (`/athleisure`)
- Produtos: 156; novos 90d: 4; movimentos estimados: 155
- Top 8 proposto:
  - 1. Jaqueta Lululemon Define Nulu Black Plum/Gold Roxo — motivo: novo_90d; antes: #156; vendas 180d: 0 un / R$ 0.0
  - 2. Jaqueta Lululemon Define Nulu Black/Gold Preto — motivo: novo_90d; antes: #155; vendas 180d: 0 un / R$ 0.0
  - 3. Camiseta Lululemon Manga Longa Swiftly Tech Shirt 2.0 Hip Length Lotus Lavender Roxo — motivo: novo_90d; antes: #154; vendas 180d: 0 un / R$ 0.0
  - 4. Jaqueta Lululemon Define Luon White Branco — motivo: novo_90d; antes: #153; vendas 180d: 0 un / R$ 0.0
  - 5. Calça Alo Yoga Suit Up Trouser (Regular) Preto — motivo: fallback_best_seller; antes: #6; vendas 180d: 24 un / R$ 37199.76
  - 6. Jaqueta Lululemon Define Nulu — motivo: fallback_best_seller; antes: #5; vendas 180d: 16 un / R$ 22399.84
  - 7. Calça Alo Yoga Suit Up Trouser (Long) Preto — motivo: fallback_best_seller; antes: #3; vendas 180d: 10 un / R$ 15499.9
  - 8. Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho — motivo: fallback_best_seller; antes: #9; vendas 180d: 7 un / R$ 10849.93
- Sairiam do top 8: Lululemon Align™ High-Rise Short 6" Rose/Gold (#1); Short Lululemon Shake It Out High-Rise Running 2.5" (#2); Pullover Alo Yoga Accolade 1/4 Zip Preto (#4); Top Alo Yoga Aspire (#7); Tênis Alo Yoga ALO Runner Branco (#8)

### Acessórios (`/acessorios`)
- Produtos: 147; novos 90d: 5; movimentos estimados: 146
- Top 8 proposto:
  - 1. Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom — motivo: novo_90d; antes: #147; vendas 180d: 0 un / R$ 0.0
  - 2. Boné Aimé Leon Dore Sun Faded Unisphere Agave Green Verde — motivo: novo_90d; antes: #140; vendas 180d: 0 un / R$ 0.0
  - 3. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo — motivo: novo_90d; antes: #57; vendas 180d: 0 un / R$ 0.0
  - 4. Calça Saint Studio Jeans Baggy Risca de Giz Azul — motivo: novo_90d; antes: #1; vendas 180d: 1 un / R$ 489.99
  - 5. Tênis ASICS Marvel vs. Bonécom x Kith x ASICS Gel Kayano 14 Ryu Branco — motivo: novo_90d; antes: #146; vendas 180d: 1 un / R$ 3799.99
  - 6. Tênis New Balance 9060 Boné Sparrow Marrom — motivo: fallback_best_seller; antes: #143; vendas 180d: 6 un / R$ 16799.94
  - 7. Boné 5 Panel Aimé Leon Dore Unisphere Branco — motivo: fallback_best_seller; antes: #73; vendas 180d: 5 un / R$ 4999.95
  - 8. Moletom Alo Yoga Sweet EsBonée Zip Up Ivory Creme — motivo: fallback_best_seller; antes: #145; vendas 180d: 3 un / R$ 3899.96
- Sairiam do top 8: Boné Alo Yoga Off-Duty Preto (#2); Boné Alo Yoga Off-Duty Branco (#3); Boné Saint Studio Art Department Azul (#4); Boné Kith Script Logo Classic Boné Nocturnal Branco/Azul (#5); Calça Saint Studio Jeans Claro Baggy Azul (#6); Boné Alo Yoga Washed Off-Duty (#7); Calça Saint Studio Jeans Baggy Preta (#8)

### New Balance (`/new-balance-todos-os-modelos`)
- Produtos: 139; novos 90d: 16; movimentos estimados: 138
- Top 8 proposto:
  - 1. Tênis New Balance 204L Slate Grey Raincloud Cinza — motivo: novo_90d; antes: #139; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis New Balance 204L x Atmos Cow Girl Brown Marrom — motivo: novo_90d; antes: #138; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis New Balance 990v6 Made in USA Cinza Castlerock — motivo: novo_90d; antes: #137; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis New Balance 1906L Black Suede Preto — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis New Balance 204L Raincloud Ash Wood Cinza — motivo: novo_90d; antes: #128; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis New Balance 530 Beige Angora Creme — motivo: novo_90d; antes: #117; vendas 180d: 2 un / R$ 3599.98
  - 7. Tênis New Balance 204L Lone Star Grey Cinza — motivo: novo_90d; antes: #129; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis New Balance 204L Reflection Bege — motivo: novo_90d; antes: #130; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: New Balance 1906L 'Silver Metallic Black' Grey (#2); Tênis New Balance 204L Arid Timberwolf Bege (#3); Tênis New Balance 204L Mushroom Arid Stone Marrom (#4); Tênis New Balance 9060 Bisque Sea Salt Bege (#5); Tênis New Balance 9060 Mushroom Arid Stone Bege (#6); Tênis New Balance 9060 Rich Oak Marrom (#7); Tênis New Balance 9060 Cortado Marrom (#8)

### Alo Yoga (`/alo-yoga-1`)
- Produtos: 115; novos 90d: 0; movimentos estimados: 109
- Top 8 proposto:
  - 1. Calça Alo Yoga Suit Up Trouser (Regular) Preto — motivo: fallback_best_seller; antes: #3; vendas 180d: 24 un / R$ 37199.76
  - 2. Calça Alo Yoga Suit Up Trouser (Long) Preto — motivo: fallback_best_seller; antes: #1; vendas 180d: 10 un / R$ 15499.9
  - 3. Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho — motivo: fallback_best_seller; antes: #6; vendas 180d: 7 un / R$ 10849.93
  - 4. Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Gravel Bege — motivo: fallback_best_seller; antes: #8; vendas 180d: 6 un / R$ 9599.94
  - 5. Tênis Alo Yoga ALO Runner Preto — motivo: fallback_best_seller; antes: #73; vendas 180d: 5 un / R$ 11999.95
  - 6. Tênis Alo Yoga Alo Runner Pink Rosa — motivo: fallback_best_seller; antes: #11; vendas 180d: 4 un / R$ 9599.96
  - 7. Tênis Alo Yoga ALO Runner Branco — motivo: fallback_best_seller; antes: #4; vendas 180d: 4 un / R$ 9599.96
  - 8. Regata Alo Yoga Ribbed Prosper Branco — motivo: fallback_best_seller; antes: #9; vendas 180d: 5 un / R$ 4249.95
- Sairiam do top 8: Pullover Alo Yoga Accolade 1/4 Zip Preto (#2); Top Alo Yoga Aspire (#5); Short Alo Yoga Match Point (#7)

### Moletom (`/moletom-1`)
- Produtos: 110; novos 90d: 3; movimentos estimados: 109
- Top 8 proposto:
  - 1. Suéter Saint Studio Moletom Quarter Zip Marrom — motivo: novo_90d; antes: #110; vendas 180d: 0 un / R$ 0.0
  - 2. Moletom Nude Project Cult Hoodie Black/Beige Preto — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 3. Moletom Nude Project Side-Eye Zip-Up Black Preto — motivo: novo_90d; antes: #2; vendas 180d: 0 un / R$ 0.0
  - 4. Moletom Nude Project Kill Bill Zip-Up Ash Cinza — motivo: fallback_best_seller; antes: #64; vendas 180d: 3 un / R$ 4699.97
  - 5. Moletom Alo Yoga Sweet EsBonée Zip Up Ivory Creme — motivo: fallback_best_seller; antes: #3; vendas 180d: 3 un / R$ 3899.96
  - 6. Moletom Aimé Leon Dore Unisphere Botanical Green Verde — motivo: fallback_best_seller; antes: #44; vendas 180d: 2 un / R$ 4049.98
  - 7. Moletom Alo Yoga Cropped Accolade Preto — motivo: fallback_best_seller; antes: #52; vendas 180d: 2 un / R$ 2699.98
  - 8. Moletom Pace Uniforma Stone Black Preto — motivo: fallback_best_seller; antes: #12; vendas 180d: 2 un / R$ 2321.99
- Sairiam do top 8: Moletom Slyce Off Court Stadium Verde (#4); Moletom Represent Clo Masking Tape Initial Cedar Marrom (#5); Moletom Represent Clo Owners Club Zip Ash Grey Cinza (#6); Moletom Represent Clo Owners Club Flat White Branco (#7); Moletom Represent Clo Out of The Shadows Stained Black Preto (#8)

### Onitsuka Tiger Mexico 66 (`/onitsuka-tiger-mexico-66`)
- Produtos: 101; novos 90d: 7; movimentos estimados: 101
- Top 8 proposto:
  - 1. Tênis Onitsuka Tiger Mexico 66 Fringe Yellow/Black Amarelo — motivo: novo_90d; antes: #101; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — motivo: novo_90d; antes: #81; vendas 180d: 1 un / R$ 2999.99
  - 3. Tênis Onitsuka Tiger Mexico 66 Fringe Black/Black Preto — motivo: novo_90d; antes: #100; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — motivo: novo_90d; antes: #99; vendas 180d: 0 un / R$ 0.0
  - 5. Tênis Onitsuka Tiger Mexico 66 Sabot Black/Black Preto — motivo: novo_90d; antes: #98; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Onitsuka Tiger Mexico 66 Sabot Dark Brown Marrom — motivo: novo_90d; antes: #97; vendas 180d: 0 un / R$ 0.0
  - 7. Tênis Onitsuka Tiger Mexico 66 Sabot Natural Cream Bege — motivo: novo_90d; antes: #96; vendas 180d: 0 un / R$ 0.0
  - 8. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — motivo: fallback_best_seller; antes: #1; vendas 180d: 77 un / R$ 184799.23
- Sairiam do top 8: Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege (#2); Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege (#3); Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege (#4); Tênis Onitsuka Tiger Mexico 66 White Black Branco (#5); Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege (#6); Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom (#7); Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata (#8)

### Adidas Samba (`/samba`)
- Produtos: 96; novos 90d: 3; movimentos estimados: 84
- Top 8 proposto:
  - 1. Tênis Adidas Samba Jane Chalk White Wonder Quartz Branco — motivo: novo_90d; antes: #96; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis adidas Samba OG Crystal Linen Ivory Gum Branco — motivo: novo_90d; antes: #95; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Adidas Samba OG Giraffe Print Grey Crystal White Gold Bege — motivo: novo_90d; antes: #94; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — motivo: fallback_best_seller; antes: #1; vendas 180d: 41 un / R$ 89999.59
  - 5. Tênis Adidas Samba OG Earth Strata Wonder White Marrom — motivo: fallback_best_seller; antes: #5; vendas 180d: 10 un / R$ 22499.92
  - 6. Tênis Adidas Samba OG Crochet Pack Orbit Green Verde — motivo: fallback_best_seller; antes: #9; vendas 180d: 9 un / R$ 17999.91
  - 7. Tênis Adidas Samba Disney 101 Dalmatians Penny Branco — motivo: fallback_best_seller; antes: #13; vendas 180d: 6 un / R$ 11999.94
  - 8. Tênis Adidas Samba Jane 'White Black' Branco — motivo: fallback_best_seller; antes: #10; vendas 180d: 5 un / R$ 9999.95
- Sairiam do top 8: Tênis adidas Samba OG White Black Gum Branco (#2); Tênis adidas Samba OG "Core Black Wonder" White Preto (#3); Tênis adidas Samba Og Off White Cyber Metallic Branco (#4); Tênis adidas Samba Og Preloved Red Leopard Pack Marrom (#6); Tênis adidas Samba Cardboard Marrom (#7); Tênis Adidas Samba Jane 'Black White Gum' Preto (#8)

### Adidas Samba (`/adidas-samba`)
- Produtos: 96; novos 90d: 3; movimentos estimados: 85
- Top 8 proposto:
  - 1. Tênis Adidas Samba Jane Chalk White Wonder Quartz Branco — motivo: novo_90d; antes: #94; vendas 180d: 0 un / R$ 0.0
  - 2. Tênis adidas Samba OG Crystal Linen Ivory Gum Branco — motivo: novo_90d; antes: #95; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Adidas Samba OG Giraffe Print Grey Crystal White Gold Bege — motivo: novo_90d; antes: #96; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — motivo: fallback_best_seller; antes: #1; vendas 180d: 41 un / R$ 89999.59
  - 5. Tênis Adidas Samba OG Earth Strata Wonder White Marrom — motivo: fallback_best_seller; antes: #4; vendas 180d: 10 un / R$ 22499.92
  - 6. Tênis Adidas Samba OG Crochet Pack Orbit Green Verde — motivo: fallback_best_seller; antes: #9; vendas 180d: 9 un / R$ 17999.91
  - 7. Tênis Adidas Samba Disney 101 Dalmatians Penny Branco — motivo: fallback_best_seller; antes: #14; vendas 180d: 6 un / R$ 11999.94
  - 8. Tênis Adidas Samba Jane 'White Black' Branco — motivo: fallback_best_seller; antes: #10; vendas 180d: 5 un / R$ 9999.95
- Sairiam do top 8: Tênis adidas Samba OG White Black Gum Branco (#2); Tênis adidas Samba OG "Core Black Wonder" White Preto (#3); Tênis adidas Samba Og Preloved Red Leopard Pack Marrom (#5); Tênis adidas Samba Og Off White Cyber Metallic Branco (#6); Tênis adidas Samba Cardboard Marrom (#7); Tênis Adidas Samba Jane 'Black White Gum' Preto (#8)

### Nude Project (`/nude-project`)
- Produtos: 90; novos 90d: 7; movimentos estimados: 77
- Top 8 proposto:
  - 1. Moletom Nude Project Cult Hoodie Black/Beige Preto — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 2. Moletom Nude Project Side-Eye Zip-Up Black Preto — motivo: novo_90d; antes: #2; vendas 180d: 0 un / R$ 0.0
  - 3. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo — motivo: novo_90d; antes: #38; vendas 180d: 0 un / R$ 0.0
  - 4. Camiseta Nude Project Kora Black Preto — motivo: novo_90d; antes: #3; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Nude Project Honor Tee Marshmallow Off White — motivo: novo_90d; antes: #4; vendas 180d: 0 un / R$ 0.0
  - 6. Camiseta Nude Project Honor Tee Black Preto — motivo: novo_90d; antes: #5; vendas 180d: 0 un / R$ 0.0
  - 7. Camiseta Nude Project Berry Tee White Branco — motivo: novo_90d; antes: #6; vendas 180d: 0 un / R$ 0.0
  - 8. Camiseta Nude Project Global Soon — motivo: fallback_best_seller; antes: #7; vendas 180d: 7 un / R$ 6999.93
- Sairiam do top 8: Camiseta Nude Project Xoxo Cinza (#8)

### Aimé Leon Dore (`/aime-leon-dore`)
- Produtos: 89; novos 90d: 11; movimentos estimados: 89
- Top 8 proposto:
  - 1. Camiseta Aimé Leon Dore Postcard Cream Bege — motivo: novo_90d; antes: #89; vendas 180d: 0 un / R$ 0.0
  - 2. Camisa Aimé Leon Dore Soccer Jersey Pristine Bege — motivo: novo_90d; antes: #88; vendas 180d: 0 un / R$ 0.0
  - 3. Camiseta Aimé Leon Dore Dove Breakfast White Branco — motivo: novo_90d; antes: #87; vendas 180d: 0 un / R$ 0.0
  - 4. Camiseta Aimé Leon Dore Saint George Asphalt Preto — motivo: novo_90d; antes: #86; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Aimé Leon Dore Saint George Coconut Milk Bege — motivo: novo_90d; antes: #85; vendas 180d: 0 un / R$ 0.0
  - 6. Camiseta Aimé Leon Dore ALD Golf Swing Coconut Milk Off White — motivo: novo_90d; antes: #84; vendas 180d: 0 un / R$ 0.0
  - 7. Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom — motivo: novo_90d; antes: #83; vendas 180d: 0 un / R$ 0.0
  - 8. Camisa Aimé Leon Dore Fassianos Half-Zip Cycling Off White — motivo: novo_90d; antes: #82; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (#1); Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White (#2); Camiseta Aimé Leon Dore Embroidered Logo Marrom (#3); Camiseta Aimé Leon Dore Unisphere Verde (#4); Camiseta Aimé Leon Dore Musician Graphic Off White (#5); Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White (#6); Camiseta Aimé Leon Dore Unisphere Black White Preto (#7); Camiseta Aimé Leon Dore Unisphere Pristine Off White (#8)

### Boné | Apparels (`/bone-streetwear`)
- Produtos: 86; novos 90d: 3; movimentos estimados: 86
- Top 8 proposto:
  - 1. Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom — motivo: novo_90d; antes: #86; vendas 180d: 0 un / R$ 0.0
  - 2. Boné Aimé Leon Dore Sun Faded Unisphere Agave Green Verde — motivo: novo_90d; antes: #79; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis ASICS Marvel vs. Bonécom x Kith x ASICS Gel Kayano 14 Ryu Branco — motivo: novo_90d; antes: #85; vendas 180d: 1 un / R$ 3799.99
  - 4. Tênis New Balance 9060 Boné Sparrow Marrom — motivo: fallback_best_seller; antes: #82; vendas 180d: 6 un / R$ 16799.94
  - 5. Boné 5 Panel Aimé Leon Dore Unisphere Branco — motivo: fallback_best_seller; antes: #27; vendas 180d: 5 un / R$ 4999.95
  - 6. Moletom Alo Yoga Sweet EsBonée Zip Up Ivory Creme — motivo: fallback_best_seller; antes: #84; vendas 180d: 3 un / R$ 3899.96
  - 7. Boné 5 Panel Aimé Leon Dore Unisphere Azul — motivo: fallback_best_seller; antes: #28; vendas 180d: 3 un / R$ 2999.97
  - 8. Boné Kith Script Logo Classic Boné Nocturnal Branco/Azul — motivo: fallback_best_seller; antes: #26; vendas 180d: 3 un / R$ 2399.97
- Sairiam do top 8: Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White (#1); Boné Lululemon Structured Ball 1998 Branco (#2); Boné Lululemon Structured Ball Boné Collegiate Bege/Bordô (#3); Boné Lululemon Classic Ball Tennis Crest Branco (#4); Boné Aimé Leon Dore x Porsche Colorblock Logo Jet Black Preto (#5); Boné Aimé Leon Dore Porsche Nylon Logo Jet Black Preto (#6); Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo (#7); Boné Aimé Leon Dore x Porsche Nylon Logo Pine Grove Verde (#8)

### Saint Studio (`/saint-studio`)
- Produtos: 82; novos 90d: 17; movimentos estimados: 82
- Top 8 proposto:
  - 1. Meia Saint Studio Pima Branco — motivo: novo_90d; antes: #82; vendas 180d: 0 un / R$ 0.0
  - 2. Meia Saint Studio Pima Marrom — motivo: novo_90d; antes: #81; vendas 180d: 0 un / R$ 0.0
  - 3. Meia Saint Studio Pima Cooper Bege — motivo: novo_90d; antes: #80; vendas 180d: 0 un / R$ 0.0
  - 4. Suéter Saint Studio Moletom Quarter Zip Marrom — motivo: novo_90d; antes: #79; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Saint Studio Oversized Suedine Supima Areia Bege — motivo: novo_90d; antes: #1; vendas 180d: 0 un / R$ 0.0
  - 6. Shorts Saint Studio Plissado Tech Preto — motivo: novo_90d; antes: #2; vendas 180d: 0 un / R$ 0.0
  - 7. Suéter Tricô Saint Studio Colméia Cinza — motivo: novo_90d; antes: #36; vendas 180d: 1 un / R$ 300.99
  - 8. Calça Saint Studio Wide Alfaiataria Caqui — motivo: novo_90d; antes: #53; vendas 180d: 3 un / R$ 1249.97
- Sairiam do top 8: Camisa Saint Studio Pima Listrada Azul (#3); Shorts Saint Studio Everywear Preto (#4); Shorts Saint Studio Everywear Caqui Bege (#5); Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto (#6); Calça Saint Studio Jeans Baggy Risca de Giz Azul (#7); Camiseta Saint Studio Boxy Supima Off Gola Vermelha Branco (#8)

### Pace (`/pace`)
- Produtos: 75; novos 90d: 7; movimentos estimados: 74
- Top 8 proposto:
  - 1. Camiseta Pace Óxido Cotton Code Grey Cinza — motivo: novo_90d; antes: #75; vendas 180d: 0 un / R$ 0.0
  - 2. Camiseta Pace Tsuho Regular Stone Washed Black Preto — motivo: novo_90d; antes: #74; vendas 180d: 0 un / R$ 0.0
  - 3. Suéter Pace Overlock Black Vintage Preto — motivo: novo_90d; antes: #73; vendas 180d: 0 un / R$ 0.0
  - 4. Calça Pace PF SweatPants Preto — motivo: novo_90d; antes: #5; vendas 180d: 7 un / R$ 3119.93
  - 5. Calça Pace Nomo Tailoring Trousers Preto — motivo: novo_90d; antes: #1; vendas 180d: 1 un / R$ 1099.99
  - 6. Camiseta Pace Buero Washed Black Preto — motivo: novo_90d; antes: #2; vendas 180d: 1 un / R$ 319.99
  - 7. Camiseta Pace Buero Off White — motivo: novo_90d; antes: #3; vendas 180d: 1 un / R$ 319.99
  - 8. Camiseta Pace Double Satire Off White — motivo: fallback_best_seller; antes: #8; vendas 180d: 6 un / R$ 1349.94
- Sairiam do top 8: Camiseta Pace Cotton Code Preta (#4); Camiseta Pace Cotton Code Branca (#6); Camisa Pace EOT Cuban Collar Preto (#7)

### Calça | Apparels (`/calca-streetwear`)
- Produtos: 70; novos 90d: 5; movimentos estimados: 68
- Top 8 proposto:
  - 1. Calça Pace PF SweatPants Preto — motivo: novo_90d; antes: #68; vendas 180d: 7 un / R$ 3119.93
  - 2. Calça Saint Studio Wide Alfaiataria Caqui — motivo: novo_90d; antes: #59; vendas 180d: 3 un / R$ 1249.97
  - 3. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo — motivo: novo_90d; antes: #34; vendas 180d: 0 un / R$ 0.0
  - 4. Calça Saint Studio Jeans Baggy Risca de Giz Azul — motivo: novo_90d; antes: #1; vendas 180d: 1 un / R$ 489.99
  - 5. Calça Pace Nomo Tailoring Trousers Preto — motivo: novo_90d; antes: #2; vendas 180d: 1 un / R$ 1099.99
  - 6. Calça Alo Yoga Suit Up Trouser (Regular) Preto — motivo: fallback_best_seller; antes: #5; vendas 180d: 24 un / R$ 37199.76
  - 7. Calça Alo Yoga Suit Up Trouser (Long) Preto — motivo: fallback_best_seller; antes: #3; vendas 180d: 10 un / R$ 15499.9
  - 8. Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho — motivo: fallback_best_seller; antes: #6; vendas 180d: 7 un / R$ 10849.93
- Sairiam do top 8: Calça Saint Studio Wide Cargo Preta (#4); Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Gravel Bege (#7); Calça Saint Studio Alfaiataria Leve Prega Dupla Preta (#8)

### Nike Dunk SB (`/nike-dunk-sb`)
- Produtos: 69; novos 90d: 3; movimentos estimados: 69
- Top 8 proposto:
  - 1. Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul — motivo: novo_90d; antes: #69; vendas 180d: 0 un / R$ 0.0
  - 2. Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa — motivo: novo_90d; antes: #68; vendas 180d: 0 un / R$ 0.0
  - 3. Tênis Nike SB Air Jordan 4 x Retro SP Navy Branco — motivo: novo_90d; antes: #67; vendas 180d: 0 un / R$ 0.0
  - 4. Tênis Nike Sb Dunk Low Pro Triple White Branco — motivo: fallback_best_seller; antes: #14; vendas 180d: 3 un / R$ 4799.97
  - 5. Tênis Nike Dunk Sb x Verdy Visty Azul — motivo: fallback_best_seller; antes: #11; vendas 180d: 2 un / R$ 8999.98
  - 6. Tênis Nike SB Dunk Low Pro St. Patrick's Day Verde — motivo: fallback_best_seller; antes: #55; vendas 180d: 2 un / R$ 5999.98
  - 7. Nike Dunk SB Dunk Low QS BHM Rodeo Verde — motivo: fallback_best_seller; antes: #6; vendas 180d: 2 un / R$ 4399.98
  - 8. Tênis Nike SB Dunk Low Pro ISO Black Gum Preto — motivo: fallback_best_seller; antes: #43; vendas 180d: 2 un / R$ 3399.98
- Sairiam do top 8: Tênis Nike SB Zoom Air Paul Rodriguez 1 Habanero Red All-Star Vermelho (#1); Livro Rizzoli Nike SB: The Dunk Book (#2); Tênis Nike SB Dunk Low Supreme 94 Black Preto (#3); Tênis Nike SB Dunk Low Supreme 94 White Metallic Silver Branco (#4); Tênis Nike SB Dunk Low Pro x Hayley Wilson Black and Court Purple Roxo (#5); Tênis Nike SB x Air Jordan 4 Navy Branco (#7); Tênis Nike Sb Dunk Low x The Wizard of OZ Poppy Field Vermelho (#8)

### Collectibles (`/collectibles`)
- Produtos: 66; novos 90d: 0; movimentos estimados: 66
- Top 8 proposto:
  - 1. Pop Mart Labubu The Monsters Coca Cola Series Surprise Shake Vinyl Plush Figure Pingente — motivo: fallback_best_seller; antes: #50; vendas 180d: 4 un / R$ 3099.96
  - 2. Pop Mart Labubu The Monsters Have a Seat HEHE Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #49; vendas 180d: 3 un / R$ 1784.97
  - 3. MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado) — motivo: fallback_best_seller; antes: #1; vendas 180d: 3 un / R$ 449.97
  - 4. Pop Mart Labubu The Monsters - Zimomo Angel In Clouds Vinyl Face Doll Branco (59cm) — motivo: fallback_best_seller; antes: #59; vendas 180d: 1 un / R$ 8499.99
  - 5. Pop Mart Labubu The Monsters Big into Energy Series Luck Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #13; vendas 180d: 2 un / R$ 1999.98
  - 6. Pop Mart Labubu The Monsters Have a Seat Vinyl Plush Pingente [Blind Box Lacrada] — motivo: fallback_best_seller; antes: #11; vendas 180d: 2 un / R$ 1699.98
  - 7. Pop Mart Labubu The Monsters Zimomo I Found You Vinyl Doll + Tote Bag Marrom (59cm) — motivo: fallback_best_seller; antes: #58; vendas 180d: 1 un / R$ 5949.99
  - 8. MEDICOM TOY - Bearbrick Jean-Michel Basquiat #10 1000% Toy Art Multi-Color — motivo: fallback_best_seller; antes: #32; vendas 180d: 1 un / R$ 4299.99
- Sairiam do top 8: Pop Mart Labubu The Monsters Coca Cola Series Mysterious Guest Vinyl Plush Figure (Secret) (#2); Pop Mart Labubu The Monsters Big into Energy Series ID  Vinyl Plush Pendant (Secret) (#3); Pop Mart The Monsters Labubu Coca-Cola Series Sealed Case [10 Blind Boxes Lacradas] (#4); Pop Mart Labubu The Monsters Coca-Cola Series Crazy Ride Figure (#5); Pop Mart Labubu The Monsters Coca-Cola Series Gift Delivery Figure (#6); Pop Mart Labubu The Monsters Coca-Cola Series Vacation Fit Figure (#7); Pop Mart Labubu The Monsters Coca Cola Series Vinyl Face Sealed Case [6 Blind Boxes Lacradas] (#8)

### Pop Mart (`/pop-mart`)
- Produtos: 60; novos 90d: 0; movimentos estimados: 59
- Top 8 proposto:
  - 1. Pop Mart Labubu The Monsters Coca Cola Series Surprise Shake Vinyl Plush Figure Pingente — motivo: fallback_best_seller; antes: #47; vendas 180d: 4 un / R$ 3099.96
  - 2. Pop Mart CryBaby Crying Again Series Vinyl Face Plush Single Blind Box — motivo: fallback_best_seller; antes: #49; vendas 180d: 3 un / R$ 2549.97
  - 3. Pop Mart Labubu The Monsters Have a Seat HEHE Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #46; vendas 180d: 3 un / R$ 1784.97
  - 4. Pop Mart Labubu The Monsters - Zimomo Angel In Clouds Vinyl Face Doll Branco (59cm) — motivo: fallback_best_seller; antes: #57; vendas 180d: 1 un / R$ 8499.99
  - 5. Pop Mart Labubu The Monsters Big into Energy Series Luck Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #24; vendas 180d: 2 un / R$ 1999.98
  - 6. Pop Mart Labubu The Monsters Have a Seat Vinyl Plush Pingente [Blind Box Lacrada] — motivo: fallback_best_seller; antes: #22; vendas 180d: 2 un / R$ 1699.98
  - 7. Pop Mart Pluto - Mickey Family Cute Together Keychain Series Figures (Aberto) — motivo: fallback_best_seller; antes: #7; vendas 180d: 2 un / R$ 769.98
  - 8. Pop Mart Labubu The Monsters Zimomo I Found You Vinyl Doll + Tote Bag Marrom (59cm) — motivo: fallback_best_seller; antes: #56; vendas 180d: 1 un / R$ 5949.99
- Sairiam do top 8: Pop Mart Secret Huguinho, Zezinho, Luizinho - Mickey Family Cute Together Keychain Series Figures (Aberto) (#1); Pop Mart Teco - Mickey Family Cute Together Keychain Series Figures (Aberto) (#2); Pop Mart Tico - Mickey Family Cute Together Keychain Series Figures (Aberto) (#3); Pop Mart Pateta - Mickey Family Cute Together Keychain Series Figures (Aberto) (#4); Pop Mart Margarida - Mickey Family Cute Together Keychain Series Figures (Aberto) (#5); Pop Mart Donald - Mickey Family Cute Together Keychain Series Figures (Aberto) (#6); Pop Mart Minnie - Mickey Family Cute Together Keychain Series Figures (Aberto) (#8)

### Supreme (`/supreme`)
- Produtos: 52; novos 90d: 0; movimentos estimados: 22
- Top 8 proposto:
  - 1. Tênis Nike Air Force 1 Low x Supreme Wheat Marrom — motivo: fallback_best_seller; antes: #15; vendas 180d: 2 un / R$ 5999.98
  - 2. Tênis Nike Air Force 1 Low x Supreme Black Preto — motivo: fallback_best_seller; antes: #16; vendas 180d: 2 un / R$ 5199.98
  - 3. Tênis Nike SB Dunk Low Supreme 94 Black Preto — motivo: fallback_best_seller; antes: #4; vendas 180d: 1 un / R$ 3999.99
  - 4. Tênis Nike SB Dunk Low Supreme 94 White Metallic Silver Branco — motivo: fallback_best_seller; antes: #5; vendas 180d: 0 un / R$ 0.0
  - 5. Camiseta Supreme "Washed Script Black" Preto — motivo: fallback_best_seller; antes: #19; vendas 180d: 0 un / R$ 0.0
  - 6. Tênis Nike Air Force 1 Low x Supreme White Branco — motivo: fallback_best_seller; antes: #20; vendas 180d: 0 un / R$ 0.0
  - 7. Boné Supreme Military Camp Boné (SS25) Tan Bege — motivo: fallback_best_seller; antes: #21; vendas 180d: 0 un / R$ 0.0
  - 8. Boné Supreme Military Camp Boné (SS25) Coral Laranja — motivo: fallback_best_seller; antes: #22; vendas 180d: 0 un / R$ 0.0
- Sairiam do top 8: Bota Timberland 6" Premium Waterproof Boot Supreme Multi-Color Colorido (#1); Bota Timberland 6" Premium Waterproof Boot Supreme Wheat Bege (#2); Bota Timberland 6" Premium Waterproof Boot Supreme Black Preto (#3); Waist Bag Supreme Preto FW 24 Vermelho (#6); Waist Bag Supreme Preto FW 24 Preto (#7); Boné 6 Panel Supreme Pigment S Logo Rosa (#8)

### New Balance 9060 (`/new-balance-9060`)
- Produtos: 51; novos 90d: 0; movimentos estimados: 49
- Top 8 proposto:
  - 1. Tênis New Balance 9060 Bisque Sea Salt Bege — motivo: fallback_best_seller; antes: #2; vendas 180d: 40 un / R$ 95759.61
  - 2. Tênis New Balance 9060 Mushroom Arid Stone Bege — motivo: fallback_best_seller; antes: #3; vendas 180d: 28 un / R$ 75599.72
  - 3. Tênis New Balance 9060 Sea Salt Moonbeam Branco — motivo: fallback_best_seller; antes: #4; vendas 180d: 24 un / R$ 62399.76
  - 4. Tênis New Balance 9060 Triple White Branco — motivo: fallback_best_seller; antes: #5; vendas 180d: 19 un / R$ 52399.82
  - 5. Tênis New Balance 9060 Rich Oak Marrom — motivo: fallback_best_seller; antes: #6; vendas 180d: 17 un / R$ 40799.83
  - 6. New Balance 9060 Black Cement "Black Cat" Preto — motivo: fallback_best_seller; antes: #24; vendas 180d: 8 un / R$ 19999.92
  - 7. Tênis New Balance 9060 Angora Sea Salt Bege — motivo: fallback_best_seller; antes: #12; vendas 180d: 7 un / R$ 18199.93
  - 8. Tênis New Balance 9060 Rose Sugar Angora Rosa — motivo: fallback_best_seller; antes: #10; vendas 180d: 7 un / R$ 16799.93
- Sairiam do top 8: Tênis New Balance 9060 Cortado Marrom (#1); Tênis New Balance 9060 Team Away Grey Cinza (#7); Tênis New Balance 9060 Earth Shadow Flat Taupe Marrom (#8)

### Labubu (`/labubu`)
- Produtos: 47; novos 90d: 0; movimentos estimados: 43
- Top 8 proposto:
  - 1. Pop Mart Labubu The Monsters Coca Cola Series Surprise Shake Vinyl Plush Figure Pingente — motivo: fallback_best_seller; antes: #35; vendas 180d: 4 un / R$ 3099.96
  - 2. Pop Mart Labubu The Monsters Have a Seat HEHE Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #34; vendas 180d: 3 un / R$ 1784.97
  - 3. Pop Mart Labubu The Monsters - Zimomo Angel In Clouds Vinyl Face Doll Branco (59cm) — motivo: fallback_best_seller; antes: #44; vendas 180d: 1 un / R$ 8499.99
  - 4. Pop Mart Labubu The Monsters Big into Energy Series Luck Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #12; vendas 180d: 2 un / R$ 1999.98
  - 5. Pop Mart Labubu The Monsters Have a Seat Vinyl Plush Pingente [Blind Box Lacrada] — motivo: fallback_best_seller; antes: #10; vendas 180d: 2 un / R$ 1699.98
  - 6. Pop Mart Labubu The Monsters Zimomo I Found You Vinyl Doll + Tote Bag Marrom (59cm) — motivo: fallback_best_seller; antes: #43; vendas 180d: 1 un / R$ 5949.99
  - 7. Pop Mart Labubu The Monsters Let's Checkmate Series Vinyl Plush Hanging Card — motivo: fallback_best_seller; antes: #45; vendas 180d: 1 un / R$ 1499.99
  - 8. Pop Mart Labubu The Monsters Have a Seat SISI Vinyl Plush Pingente — motivo: fallback_best_seller; antes: #16; vendas 180d: 1 un / R$ 849.99
- Sairiam do top 8: Pop Mart Labubu The Monsters Coca Cola Series Mysterious Guest Vinyl Plush Figure (Secret) (#1); Pop Mart Labubu The Monsters Big into Energy Series ID  Vinyl Plush Pendant (Secret) (#2); Pop Mart The Monsters Labubu Coca-Cola Series Sealed Case [10 Blind Boxes Lacradas] (#3); Pop Mart Labubu The Monsters Coca-Cola Series Crazy Ride Figure (#4); Pop Mart Labubu The Monsters Coca-Cola Series Gift Delivery Figure (#5); Pop Mart Labubu The Monsters Coca-Cola Series Vacation Fit Figure (#6); Pop Mart Labubu The Monsters Coca Cola Series Vinyl Face Sealed Case [6 Blind Boxes Lacradas] (#7); Pop Mart Labubu The Monsters Coca Cola Series Vinyl Face [Blind Box Lacrada] (#8)

## Coleções puladas

- sort_order_nao_manual:best-selling: 22
- menos_de_4_produtos: 11
- sort_order_nao_manual:created-desc: 6
- sort_order_nao_manual:most-relevant: 4

## Rollback

- Snapshot salvo em `rollback-snapshot.json`.
- Para aplicação futura, restaurar `current_order_product_ids` via `collectionReorderProducts`, aguardando job e validando readback.

## Arquivos

- `dry-run.json`: relatório completo.
- `top8-preview.csv`: preview tabular por coleção/produto.
- `rollback-snapshot.json`: ordem atual para rollback futuro.

## Não feito

- Nenhuma mutation Shopify.
- Nenhum cron criado.
- Nenhuma alteração em produto, coleção, estoque, preço, tema, SEO ou campanha.