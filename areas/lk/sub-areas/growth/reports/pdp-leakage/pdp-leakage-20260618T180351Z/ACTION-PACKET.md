# PDP Leakage — Decision Packet

## Veredito executivo
O diagnóstico encontrou muito tráfego concentrado em poucos PDPs com venda baixa/zero. A maior oportunidade não é “SEO genérico”: é separar tráfego curioso/viral/não-sneaker de PDPs com intenção real e baixa conversão.

## Buckets de ação

### 1) Revisão comercial / causa antes de copy
Produtos com alto tráfego e 0 venda em 180d. Não consultar estoque neste agente; se a hipótese for grade/disponibilidade, acionar lk-stock.
- Tênis Yeezy Foam Runner MX Cinder Marrom — views180 130672, vendas180 0, score 113.0
- Tênis Mule Bravest Studios Bear Claw Black Preto — views180 23879, vendas180 0, score 57.21
- Tênis Nike SB Dunk Low Sandy Bodecker (Ebay 2022) Colorido — views180 21378, vendas180 0, score 55.91
- Lip Case Rhode By Hailey Bieber Limited Edition Shade Amarelo — views180 14388, vendas180 0, score 52.25
- Chinelo Havaianas Top Dolce & Gabbana Florals Rosa — views180 11130, vendas180 0, score 50.55
- Adidas Taekwondo Mei Ballet Preto e Branco — views180 9047, vendas180 0, score 49.46
- Tênis Nike Travis Scott x Air Jordan 1 Low OG Reverse Mocha Bege — views180 9003, vendas180 0, score 49.44
- Tênis Adidas Taekwondo Mei Ballet Clear Sky Gum Azul — views180 6242, vendas180 0, score 48.0
- Tênis Nike Air Jordan 1 Retro Low Fragment Design x Travis Scott Couro Branco Preto Azul — views180 6232, vendas180 0, score 47.99
- Tênis Yeezy Foam Runner Onyx Preto — views180 4744, vendas180 0, score 47.22

### 2) CRO/copy com maior chance real
Produtos com venda existente, mas taxa baixa frente ao tráfego. Bons candidatos para PDP trust/copy/FAQ/imagem/linkagem.
- Lip Case Rhode By Hailey Bieber — views180 105664, vendas180 1.0, taxa 9e-06, score 81.93
- Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege — views180 63357, vendas180 24.0, taxa 0.000379, score 59.68
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — views180 42947, vendas180 38.0, taxa 0.000885, score 48.82

### 3) SEO/meta básico faltando
- Tênis Nike Vomero Premium White Lapis Total Orange Off White — falta SEO title; views180 1378, vendas180 0
- Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — falta SEO title, SEO description; views180 687, vendas180 0
- Tênis Nike Vomero Premium Volt Tint Sapphire Verde — falta SEO title; views180 620, vendas180 0
- Tênis New Balance Gator Run Timberwolf Bege — falta SEO title, SEO description; views180 615, vendas180 0
- Tênis Nike x Tom Sachs Mars Yard 3.0 Bege — falta SEO title, SEO description; views180 523, vendas180 0

### 4) Tráfego não-sneaker / possível ruído de catálogo
- Lip Case Rhode By Hailey Bieber — views180 105664, vendas180 1.0
- Lip Case Rhode By Hailey Bieber Limited Edition Shade Amarelo — views180 14388, vendas180 0
- Chinelo Havaianas Top Dolce & Gabbana Florals Rosa — views180 11130, vendas180 0
- KAWS Holiday Taipei Vinyl Figure Brown Toy Art Marrom — views180 2240, vendas180 0
- Pop Mart Labubu The Monsters Big into Energy Series ID  Vinyl Plush Pendant (Secret) — views180 2174, vendas180 0

## Recomendação de próximo sprint
1. Preparar pacote CRO/copy para 5 PDPs vendidos com tráfego alto: Onitsuka Tiger Mexico 66 Sabot Birch Peacoat, Nike Moon Shoe SP Jacquemus Alabaster e próximos vendidos da lista completa.
2. Para 0 venda + alto tráfego: abrir revisão de causa, não reescrever às cegas. Se envolver disponibilidade/grade, handoff para lk-stock.
3. Corrigir metadados faltantes de PDPs com tráfego: Vomero Premium White, Onitsuka x Versace, Vomero Premium Volt, NB Gator Run, Mars Yard 3.0 — somente com aprovação de Shopify SEO fields.
4. Produtos não-sneaker com tráfego alto devem ser tratados como rota separada de catálogo/conteúdo, não misturados com CRO de tênis.

## Aprovação necessária
- Writes Shopify em title/meta/descrição/PDP: exigem aprovação explícita.
- Qualquer validação de estoque/disponibilidade: dono é lk-stock.
- Este packet é read-only; writes=0; values_printed=false.
