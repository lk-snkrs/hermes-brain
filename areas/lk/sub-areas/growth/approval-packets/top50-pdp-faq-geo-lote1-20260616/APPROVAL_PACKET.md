# Approval Packet — Top 50 PDP FAQ/GEO/CRO — Lote 1

Gerado: 2026-06-16T16:53:54.103233+00:00

## Status
- Escopo proposto: atualizar `descriptionHtml` de 10 PDPs com descrição curta, bloco de valor e FAQ específico.
- Writes externos executados agora: 0.
- Não inclui: preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp, SEO title/meta, theme production ou FAQ global.
- Rollback: snapshot Shopify `shopify-lote1-before.json` + payload anterior por produto.

## Evidência usada
- Shopify 90d: 1.205 pedidos, Top 50 por receita.
- Shopify readback atual dos 10 produtos.
- Fetch público dos 10 PDPs.
- DataForSEO Keyword Overview + SERP/PAA para clusters: New Balance 204L, New Balance 9060, Nike Mind 001/002, Onitsuka Mexico 66, Nike Moon Shoe Jacquemus.
- Ahrefs API validada e organic keywords testado.
- Claude SEO / FAQ Real Intent Gate aplicado como critic pass.

## Produtos do Lote 1

### 1. Tênis New Balance 204L Arid Timberwolf Bege
- URL: https://lksneakers.com.br/products/tenis-new-balance-204l-timberwolf-bege
- Handle: `tenis-new-balance-204l-timberwolf-bege`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 2243 / 1896 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 2. Tênis New Balance 204L Mushroom Arid Stone Marrom
- URL: https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom
- Handle: `tenis-new-balance-204l-mushroom-arid-stone-marrom`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 2155 / 1901 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 3. Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza
- URL: https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza
- Handle: `slide-nike-mind-001-light-smoke-grey-cinza`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 1979 / 2019 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 4. Tênis Nike Mind 002 Light Smoke Grey Cinza
- URL: https://lksneakers.com.br/products/tenis-nike-mind-002-light-smoke-grey-cinza
- Handle: `tenis-nike-mind-002-light-smoke-grey-cinza`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 1836 / 1848 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 5. Tênis New Balance 9060 Bisque Sea Salt Bege
- URL: https://lksneakers.com.br/products/tenis-new-balance-9060-bisque-sea-salt-bege
- Handle: `tenis-new-balance-9060-bisque-sea-salt-bege`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 3107 / 1797 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 6. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo
- Handle: `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 3230 / 1922 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 7. Tênis Onitsuka Tiger Mexico 66 White Black Branco
- URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-white-black-branco
- Handle: `tenis-onitsuka-tiger-mexico-66-white-black-branco`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 3174 / 1890 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 8. Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom
- URL: https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown
- Handle: `tenis-nike-moon-shoe-sp-jacquemus-medium-brown`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 1883 / 1932 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 9. Tênis Nike Moon Shoe SP Jacquemus Off White
- URL: https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-white
- Handle: `tenis-nike-moon-shoe-sp-jacquemus-off-white`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 1814 / 1928 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

### 10. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto
- URL: https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto
- Handle: `tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto`
- Escopo: substituir/normalizar descrição HTML atual por bloco proposto.
- Tamanho atual/proposto: 1873 / 1915 chars
- FAQ: específico por intenção real; sem perguntas de prazo/estoque/pronta entrega/encomenda.

## Payload proposto
Arquivo JSON completo: `work/top50-product-faq-geo-lote1-20260616/lote1-proposed-payload.json`

## QA obrigatório se aprovado
1. Snapshot antes de aplicar.
2. Aplicar somente `descriptionHtml` dos 10 product IDs listados.
3. Readback Shopify por ID/handle.
4. Fetch público dos 10 PDPs.
5. Validar presença de novas perguntas e ausência de termos operacionais proibidos no bloco novo.
6. Registrar receipt + rollback.
7. D7/D14: GSC queries, cliques/CTR, GA4 PDP engagement, Shopify add-to-cart/purchase quando disponível.

## Risco
- Baixo/médio: alteração editorial em PDPs de alta receita.
- Risco principal: conteúdo longo demais no mobile; por isso não mexer em layout agora.
- Theme/FAQ global: fora do escopo; se aparecer duplicidade visual, abrir dev-preview separado.

## Aprovação necessária
Para aplicar, Lucas precisa aprovar explicitamente:

```
Aprovo aplicar o Lote 1 Top 50 PDP FAQ/GEO de 2026-06-16 nos 10 PDPs listados, somente no campo descriptionHtml/descrição dos produtos, com rollback/readback/fetch público, sem alterar preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp, SEO title/meta ou theme production.
```
