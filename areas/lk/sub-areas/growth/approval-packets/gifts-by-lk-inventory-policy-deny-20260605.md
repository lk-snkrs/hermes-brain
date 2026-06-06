# Approval Packet — Gifts by LK. inventory policy DENY

Data UTC: 2026-06-05T17:07:44Z

## Pedido

Garantir que todos os produtos da coleção **Gifts by LK.** estejam sem a opção Shopify **"Continuar vendendo sem estoque"**.

## Evidência read-only

- Coleção: **Gifts by LK.**
- Handle: `giftable`
- Collection ID: `gid://shopify/Collection/1126715719902`
- Produtos na coleção: **63**
- Variantes atualmente com `inventoryPolicy=CONTINUE`: **538**
- Dessas, variantes com quantidade <= 0: **261**
- Variantes já `DENY` mas sem estoque: **25**
- Evidência local detalhada: `/opt/data/tmp/gifts_by_lk_inventory_policy_readonly.json`

## Mudança proposta

Executar mutation Shopify Admin GraphQL para alterar apenas:

- De: `inventoryPolicy=CONTINUE`
- Para: `inventoryPolicy=DENY`
- Escopo: **538 variantes** dos produtos da coleção `giftable` que hoje estão em CONTINUE.

Não alterar:

- quantidade de estoque;
- preço;
- título, descrição, SEO;
- coleção;
- tema;
- produto/variante além do campo de política de venda sem estoque.

## Impacto esperado

- Produto/variante com estoque real positivo continua vendável.
- Produto/variante ao chegar a 0 deixa de aceitar venda sem estoque.
- Reduz risco comercial/operacional de pedidos sem disponibilidade real na curadoria Gifts.

## Risco

- Baixo/médio: pode reduzir conversões de itens sem estoque, mas é intencional para evitar venda sem disponibilidade.
- Risco operacional principal: se algum item com demanda deveria aceitar encomenda/atendimento manual, ele deixará de vender automaticamente.

## Rollback

- Reverter as mesmas variantes alteradas para `inventoryPolicy=CONTINUE`, usando a lista de variant IDs salva no receipt da execução.
- Como rollback altera política de venda, também exige aprovação explícita.

## Aprovação necessária

Shopify production write. Frase sugerida para Lucas:

> Pode aplicar na Shopify production: na coleção Gifts by LK. (`giftable`), alterar todas as variantes atualmente com `inventoryPolicy=CONTINUE` para `DENY`, sem mexer em estoque, preço, tema ou conteúdo. Registrar receipt e rollback.

## Produtos afetados — títulos únicos

- New Balance 9060 Black Cement "Black Cat" Preto
- Tênis Adidas Ballerina Bad Bunny Off White Black Gum Branco
- Tênis Adidas Gazelle Indoor Bad Bunny Cabo Rojo Rosa
- Tênis Adidas Handball Spezial Earth Strata Gum Marrom
- Tênis Adidas SL 72 Og Court Green Cow Print Bege
- Tênis Adidas Samba OG Cow Print Bege
- Tênis Adidas Samba OG Cream White Cardboard Creme
- Tênis Adidas Samba OG Crochet Pack Orbit Green Verde
- Tênis Adidas Samba OG Crochet Pack Sand Strata Bege
- Tênis Adidas Samba OG Earth Strata Wonder White Marrom
- Tênis Adidas Samba OG Sanda Strata Sky Tint Bege
- Tênis Adidas Samba OG Silver Metallic Cracked Leather Prateado
- Tênis Adidas Taekwondo Mei Ballet Black Gum Preto
- Tênis Adidas Taekwondo Mei Cow Print (Women's) Animal Print
- Tênis Adidas Tokyo Core Black Preto
- Tênis Adidas Tokyo Silver Metallic Prata
- Tênis Alo Yoga ALO Runner Branco
- Tênis New Balance 530 Silver White Branco
- Tênis New Balance 530 Steel Grey Cinza
- Tênis New Balance 530 White Natural Indigo Branco
- Tênis New Balance 530 White Pearl Grey Branco
- Tênis New Balance 9060 Grey Day 2025 Cinza
- Tênis New Balance 9060 Rose Sugar Angora Rosa
- Tênis New Balance 9060 Sea Salt Concrete Branco
- Tênis New Balance 9060 Slate Grey Cinza
- Tênis New Balance 9060 Sparrow Flat Taupe Marrom
- Tênis Nike Air Jordan 1 Low Black Medium Grey Cinza
- Tênis Nike Air Jordan 1 Low Bred Toe Vermelho
- Tênis Nike Air Jordan 1 Low Og Mocha Marrom
- Tênis Nike Air Jordan 1 Low Panda (2023) Preto
- Tênis Nike Air Jordan 1 Low SE 'Light Steel Grey' Cinza
- Tênis Nike Air Jordan 1 Low SE Concord Preto
- Tênis Nike Air Jordan 1 Low Smoke Grey Toe Cinza
- Tênis Nike Air Jordan 1 Low Vintage Grey Cinza
- Tênis Nike Air Jordan 1 Retro Low OG Zion Williamson Voodoo Alternate Azul
- Tênis Nike Air Rift Sail Bege
- Tênis Nike Cortez Forrest Gump 2024 Branco
- Tênis Nike Cortez Valentine's Day Branco
- Tênis Nike Dunk Low Black OG Panda Preto
- Tênis Nike Dunk Low Cacao Wow Marrom
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
- Tênis Puma Speedcat Archive Haute Coffee Frosted Ivory Marrom
- Tênis Puma Speedcat Og Black White Preto
- Tênis Yeezy Boost 350 V2 Boné Branco
- Tênis Yeezy Boost 350 V2 Onyx Preto
- Tênis adidas Gazelle Indoor Collegiate Green Verde
- Tênis adidas Gazelle x CLOT Linen Khaki Light Blue Marrom
- Tênis adidas SL 72 Og Cow Print Bege
- Tênis adidas SL 72 Og Maroon Almost Yellow Marrom
- Tênis adidas Samba OG Cream White Core Black Bege
- Tênis adidas Samba Og  x Naked Consortium Off White Crystal White Branco
- Tênis adidas Samba Og Maroon Cream White Vinho
- Tênis adidas Samba Og Marron Sand Strata Pony Vinho
- Tênis adidas Samba Og Off White Cyber Metallic Branco
- Tênis adidas Samba Og Preloved Red Leopard Pack Marrom
- Tênis adidas Samba Og x Sporty & Rich USA Branco
