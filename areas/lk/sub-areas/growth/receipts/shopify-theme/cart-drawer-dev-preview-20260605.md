# LK Cart Drawer — Dev preview criado — 2026-06-05

## Escopo

- Pedido Lucas: auditar carrinho/PDP atual, criar cart drawer em Dev preview e preparar refinamento CRO.
- Superfície: Shopify theme, `lk-new-theme/dev` apenas.
- Production/live: sem alteração.

## Evidência read-only inicial

- Live product `https://www.lksneakers.com.br/products/new-balance-530-white-natural-indigo-1` retornava `200`.
- Live HTML tinha header cart link `#lk-cart-icon`, mas não tinha markup real de drawer no DOM sem scripts:
  - `#cart-drawer`: ausente
  - `.cart-drawer-overlay`: ausente
- O snippet `snippets/lk-cart-drawer.liquid` já existia em Dev/Production, mas `layout/theme.liquid` não renderizava o snippet em Production e também não renderizava em Dev antes da ativação.

## Mudança aplicada em Dev

Tema verificado antes do write:

- Dev: `155065450718` — `lk-new-theme/dev` — `role=unpublished`
- Production: `155065417950` — `lk-new-theme/production` — `role=main`

Assets alterados apenas em Dev:

1. `layout/theme.liquid`
   - ativado `{% render 'lk-cart-drawer' %}` antes de `</body>`.
2. `snippets/lk-cart-drawer.liquid`
   - refinamento de reassurance no estado com itens:
     - `100% original + nota fiscal`
     - `Loja física Jardins/SP`
     - `10x sem juros`
     - `Troca grátis em 7 dias`
     - link `Ajuda pelo WhatsApp`
   - correções de acento em microcopy do drawer.

## Verificação

- Dev layout readback: contém `render 'lk-cart-drawer'`.
- Dev snippet readback final: SHA `4c8aae9b0ad1`, contém `cart-drawer__reassurance` e `Ajuda pelo WhatsApp`.
- Production layout readback: não contém render do drawer.
- Production snippet readback: SHA `74d5295e0fd6`, sem reassurance; Production não foi alterado.
- Public Dev preview HTML:
  - product preview `200`
  - cart preview `200`
  - contém `#cart-drawer` e `.cart-drawer-overlay`.
- Live product público continua sem `#cart-drawer`/overlay.
- Headless mobile QA via Chromium/CDP:
  - antes do clique: drawer presente, fechado.
  - após clique no ícone do carrinho: `drawerOpen=true`.

## Artifacts

- Activation receipt dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-preview-20260605T094119Z/`
- QA dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-qa-20260605T094216Z/`
- Refinement receipt dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-refine-20260605T094551Z/`
- Mobile screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-qa-20260605T094216Z/cart-drawer-mobile-open-2.png`

## Rollback

- Reverter em Dev:
  1. Remover render `lk-cart-drawer` de `layout/theme.liquid` usando backup `dev-layout-before.liquid`.
  2. Restaurar `snippets/lk-cart-drawer.liquid` usando `dev-snippet-before.liquid` do refinement receipt.
- Production rollback não necessário porque Production não foi alterado.

## Próximo passo recomendado

- Lucas revisar Dev preview visual.
- Se aprovado visualmente, preparar pacote de Production separado com backup live + readback + QA público.
- Antes de Production, ideal testar estado com item no carrinho em sessão de QA para validar reassurance, subtotal, quantidade e checkout link.
