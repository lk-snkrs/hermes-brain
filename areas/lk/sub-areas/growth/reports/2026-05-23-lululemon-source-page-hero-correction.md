# LK GEO Source Page — correção hero Lululemon por bestseller

Data: 2026-05-23

## Correção de Lucas

Lucas apontou que a página de Lululemon usou como foto principal um produto fraco/menos vendido. Regra consolidada: source pages LK devem usar como hero/main photo o produto relevante mais vendido no Shopify, não uma escolha arbitrária.

## Dado verificado

Fonte: Shopify Admin GraphQL read-only, orders `status:any`, pedidos cancelados excluídos, 5.367 pedidos escaneados.

Top Lululemon por unidades:

1. Jaqueta Lululemon Define Nulu — 37 unidades / 34 pedidos — `jaqueta-lululemon-define-nulu` — ACTIVE
2. Lululemon Align™ High-Rise Short 6" Rose/Gold — 7 unidades / 2 pedidos — DRAFT, excluído do hero/cards públicos
3. Calça Lululemon Scuba Mid-Rise Wide-Leg Regular — 5 unidades / 5 pedidos — ACTIVE
4. Camiseta Lululemon Swiftly Tech 2.0 Hip Length — 4 unidades / 3 pedidos — ACTIVE
5. Jaqueta Lululemon Define Cropped Nulu Light Ivory/Gold/Gold Off White — 4 unidades / 3 pedidos — ACTIVE

## Ação aplicada

- Hero e primeiro produto da página Lululemon corrigidos para `Jaqueta Lululemon Define Nulu`.
- Produtos relacionados reordenados por vendas e status ativo:
  - Jaqueta Lululemon Define Nulu
  - Calça Lululemon Scuba Mid-Rise Wide-Leg Regular
  - Camiseta Lululemon Swiftly Tech 2.0 Hip Length
  - Jaqueta Lululemon Define Cropped Nulu Light Ivory/Gold/Gold Off White
- O handle original `/pages/lululemon-original-brasil` ficou preso em `page_cache` público antigo mesmo após Admin readback correto e recriação com mesmo handle.
- Para entregar link aprovado visualmente agora, foi criada URL final nova: `https://lksneakers.com.br/pages/lululemon-original-brasil-guia-lk`.
- Foi criado redirect Admin de `/pages/lululemon-original-brasil` para `/pages/lululemon-original-brasil-guia-lk`; cache público antigo pode demorar a expirar.

## QA final

URL final validada: `https://lksneakers.com.br/pages/lululemon-original-brasil-guia-lk`

- HTTP 200
- Hero contém `Jaqueta Lululemon Define Nulu`
- Imagem hero contém `jaqueta-lululemon-define-nulu-lk-11020158`
- Daydrift ausente da página final
- 4 cards de produto
- 1 H1 no HTML final
- `FAQPage` presente
- Termos proibidos: 0 ocorrências de pronta entrega, encomenda, estoque, marketplace, legit-check

## Learning loop

- Memória atualizada.
- Skill `lk-seo-weekly-improvement` atualizada com pitfall/regra de hero por bestseller.
- Cron D+7 Packet D atualizado para usar a URL final nova e verificar o hero bestseller.

## Rollback

- Backups em `areas/lk/sub-areas/growth/receipts/shopify-source-pages/`.
- Se necessário, remover página `lululemon-original-brasil-guia-lk`, remover redirect `488915566814`, e restaurar backup da página antiga em `lululemon-recreate-page-cache-20260523/old-page-*.backup.json`.
