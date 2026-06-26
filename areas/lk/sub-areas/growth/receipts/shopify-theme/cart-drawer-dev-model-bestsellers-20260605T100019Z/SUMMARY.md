# LK Cart Drawer — model best-sellers upsell DEV — 2026-06-05

## Escopo aprovado

Lucas aprovou alterar o upsell do cart drawer em Dev para parar de sugerir produtos genéricos e mostrar best sellers do mesmo modelo/silhueta.

## Mudança aplicada

Asset Shopify alterado somente em Dev/unpublished:

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-cart-drawer.liquid`

Nova lógica:

1. Detecta modelo/silhueta do item no carrinho por handle/título.
2. Busca coleção canônica do modelo com `sort_by=best-selling`.
3. Exclui produto já no carrinho.
4. Filtra produtos disponíveis.
5. Mantém matching de tamanho quando há variante do mesmo tamanho.
6. Renderiza até 4 cards.
7. Fallback sem shuffle aleatório: `Mais vendidos LK` via coleção all best-selling.

## Modelos mapeados inicialmente

- New Balance 530 → `new-balance-530`
- New Balance 9060 → `new-balance-9060`
- Adidas Samba → `adidas-samba`
- Adidas Gazelle → `adidas-gazelle`
- Adidas Campus → `adidas-campus`
- Onitsuka Tiger Mexico 66 → `onitsuka-tiger-mexico-66`
- Nike Cortez → `nike-cortez`
- Nike Dunk Low → `nike-dunk-low`
- Air Jordan 1 Low → `air-jordan-1-low`
- Adidas Spezial → `adidas-spezial`
- ASICS Gel-Kayano 14 → `asics-gel-kayano-14`

## Readback

- Dev before SHA: `4c8aae9b0ad17a95a491e389d104ec937ccd77a6988f20b386c4ec829d402e9d`
- Dev target/readback SHA: `aa185c16d14b7ffeb288991fdcc4ce935b27f7a5f7dba88b099cef4f21b33d47`
- Readback OK: `True`
- Production before SHA: `74d5295e0fd6f8ed9b8d3b230483a1e235f7fdd14acc63f76e167937fbc1139b`
- Production after SHA: `74d5295e0fd6f8ed9b8d3b230483a1e235f7fdd14acc63f76e167937fbc1139b`
- Production unchanged: `True`

## QA browser mobile

Produto usado no carrinho:

- `new-balance-530-white-natural-indigo-1`
- Variant usada: `34` / `45022132797662`

Resultado:

- Drawer abriu: `True`
- Título do upsell: `Mais vendidos do modelo`
- Produto atual excluído dos upsells: `True`

Upsells renderizados:

- `tenis-new-balance-530-silver-white-branco` — Tênis New Balance 530 Silver White Branco
- `tenis-new-balance-530-arid-stone-cinza` — Tênis New Balance 530 Arid Stone Cinza
- `tenis-new-balance-530-brown-tan-marrom` — Tênis New Balance 530 Brown Tan Marrom
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual` — Tênis New Balance 530 Turtledove Mushroom Mesh Bege

## Artifacts

- Receipt dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-model-bestsellers-20260605T100019Z`
- Screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-model-bestsellers-20260605T100019Z/cart-drawer-model-bestsellers-mobile.png`
- QA JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-model-bestsellers-20260605T100019Z/cdp-model-bestsellers-check.json`

## Rollback

Restaurar `dev-snippet-before.liquid` no tema Dev.
Production não requer rollback porque não foi alterada.
