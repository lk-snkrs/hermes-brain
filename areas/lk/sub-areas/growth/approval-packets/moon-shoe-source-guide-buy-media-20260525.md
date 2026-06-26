# Approval packet — Moon Shoe source guide: CTA + matérias destacadas

Data: 2026-05-25
Escopo: LK Sneakers / Growth / Shopify theme
Ambiente alterado: dev theme `lk-new-theme/dev` (`155065450718`) apenas
Produção: não alterada

## Pedido de Lucas

1. Na página do guia editorial, incluir link claro para a coleção para compra dos produtos.
2. Na página do guia editorial, incluir principais matérias destacando o modelo e por que ele é relevante, como Vogue, Hypebeast e outros veículos importantes de moda.

## Implementado em preview/dev

- CTA hero alterado para: `Comprar produtos da coleção` → `/collections/nike-x-jacquemus-moon-shoe-sp`.
- CTA antes da seleção relacionada: `Ver produtos da coleção`.
- Novo bloco editorial `Sinais de moda` com três cards externos:
  - Vogue — spring sneaker collaborations / Jacquemus x Nike Moon Shoes.
  - Hypebeast — Spring 2026 colorways e arquivo Moon Shoe 1972.
  - Hypebae — reinvenção minimalista do Moon Shoe, Bill Bowerman e DNA de corrida.
- Links externos com `rel="nofollow noopener"` e `target="_blank"`.

## Preview

https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?view=moon-source&preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1&lkqa=20260525-142206

## Checks

- Dev theme only: OK
- Readback Shopify: OK
- CTA compra: OK
- Bloco de matérias: OK
- Termos proibidos: `estoque=0`, `encomenda=0`, `pronta entrega=0`
- Visual desktop: OK via screenshot/vision

## Risco

Baixo. Alteração em snippet do guia editorial, sem mexer em preço, estoque, produto, feed, checkout ou campanhas.

## Rollback

Reenviar o backup `snippet.before.liquid` salvo em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/moon-shoe-source-buy-media-dev-20260525-142206/snippet.before.liquid`

## Aprovação necessária

Para publicar em produção, Lucas precisa aprovar explicitamente a promoção do mesmo snippet do dev theme para o tema live.
