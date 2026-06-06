# Cart Drawer Upsell — proposta model best sellers — 2026-06-05

## Feedback Lucas

- Cart drawer aprovado visualmente.
- Sugestões atuais não fazem sentido.
- Direção desejada: mostrar best sellers do mesmo modelo/silhueta.

## Diagnóstico

A lógica atual do drawer tenta primeiro Shopify Recommendations API:

- `/recommendations/products.json?intent=complementary`
- `/recommendations/products.json?intent=related`

Se a API não retorna bons itens, usa fallback genérico:

- `/products.json?limit=20`
- shuffle aleatório

Isso gera mistura ruim para LK, porque recomendações genéricas podem puxar roupas, marcas/modelos não relacionados ou produtos de outra intenção.

## Proposta

Trocar o upsell por hierarquia de curadoria:

1. Detectar o modelo/silhueta do item no carrinho por handle/título.
2. Buscar a coleção do modelo, ex.:
   - New Balance 530 → `/collections/new-balance-530/products.json?limit=12`
   - Adidas Samba → `/collections/adidas-samba/products.json?limit=12`
   - Adidas Gazelle → `/collections/adidas-gazelle/products.json?limit=12`
   - Adidas Campus → `/collections/adidas-campus/products.json?limit=12`
   - Onitsuka Tiger Mexico 66 → `/collections/onitsuka-tiger-mexico-66/products.json?limit=12`
   - New Balance 9060 → `/collections/new-balance-9060/products.json?limit=12`
   - Nike Cortez → `/collections/nike-cortez/products.json?limit=12`
3. Excluir o produto atual do carrinho.
4. Priorizar disponíveis e, quando possível, variantes no mesmo tamanho do carrinho.
5. Renderizar até 4 produtos.
6. Se não houver coleção/modelo detectado, não usar shuffle genérico; fallback seguro para coleção editorial/best sellers definida manualmente.

## Exemplo New Balance 530

Consulta pública read-only em `/collections/new-balance-530/products.json?limit=8` retornou:

- `new-balance-530-white-natural-indigo-1`
- `tenis-new-balance-530-silver-white-branco`
- `tenis-new-balance-530-arid-stone-cinza`
- `tenis-new-balance-530-brown-tan-marrom`
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual`
- `tenis-new-balance-530-white-pearl-grey-branco`
- `tenis-new-balance-530-silver-cream-prateado`
- `tenis-new-balance-530-x-salehe-bembury-prosperity-be-the-prize-verde`

Para carrinho com `new-balance-530-white-natural-indigo-1`, recomendação inicial proposta:

- Silver White
- Arid Stone
- Brown Tan
- Turtledove Mushroom Mesh

## Copy recomendada

Título do bloco:

- `Mais vendidos do modelo`

Subcopy curta opcional:

- `Outras cores do mesmo tênis`

## Escopo de preview write necessário

Asset: `snippets/lk-cart-drawer.liquid` no tema Dev/unpublished.

Modificar apenas a lógica de `loadRecommendationsFromCart`, `fallbackFromCollection` e título do bloco de upsell.

## Segurança

- Requer aprovação explícita de Lucas para escrever no theme Dev.
- Production segue intacta.
- Após write: readback SHA + QA preview + teste com item no carrinho.
