# Curadoria LK — Batch 6 Dev preview / approval packet Production

## Status

Batch 6 aplicado apenas no Dev theme.

- Dev theme ID: `155065450718`
- Production theme ID: `155065417950`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Production unchanged: true
- Dev readback: match

## Grupos no Batch 6

1. Nike Air Force 1 Low regular
   - Marker: `top30-nike-air-force-1-low-regular`
   - Produtos no grupo: 8
   - Filtro: remove collabs/cápsulas evidentes como A Ma Maniére, Kobe/Protro, Off-White, Supreme, Ambush, Nocta, Tiffany, Stussy e kids.

2. Adidas Handball Spezial regular
   - Marker: `top30-adidas-handball-spezial-regular`
   - Produtos no grupo: 8

3. Adidas SL 72 regular
   - Marker: `top30-adidas-sl-72-regular`
   - Produtos no grupo: 8
   - Filtro: remove cápsula/collab evidente Liberty London e kids.

4. New Balance 1906L regular
   - Marker: `top30-new-balance-1906l-regular`
   - Produtos no grupo: 8
   - Observação: separado como 1906L, não misturado com 1906R collab.

5. New Balance 530 regular
   - Marker: `top30-new-balance-530-regular`
   - Produtos no grupo: 8

## Evidência

Arquivos:

- `batch6-candidates.json`
- `batch6-selected-groups.json`
- `batch6-append.liquid`
- `dev-upload-readback-report.json`
- `dev-static-api-qa-batch6.json`
- `dev_before_batch6.liquid`
- `prod_before_batch6.liquid`
- `dev_after_batch6.liquid`

## QA Dev

Resultado: pass

- Catálogo Shopify lido: 2.330 produtos
- Ativos/publicados filtrados: 1.755
- Grupos novos selecionados: 5
- Cada grupo tem 8 handles públicos disponíveis via `/products/{handle}.js`
- Simulação de cada PDP: 5 cards, produto atual excluído
- Markers no Dev: 5/5, exatamente 1 ocorrência cada
- URLs de imagem: Shopify CDN válidas
- Malformed URL count: 0
- Balanceamento básico Liquid:
  - `for/endfor`: 10/10
  - `if/endif`: 15/15
- Production unchanged: true

## Risco

- Baixo/médio: mudança de tema PDP em Dev, visual/CRO. Não altera produto, preço, estoque ou checkout.
- Air Force 1 é uma família ampla; filtro removeu collabs/cápsulas evidentes, mas a família ainda mistura variações sazonais regular.
- New Balance 1906L foi separado de 1906R para evitar mistura de silhueta/cápsula.

## Rollback

Para rollback do Dev: re-upar `dev_before_batch6.liquid` para `snippets/lk-variante-top30-visited.liquid` no Dev theme.

Para Production, antes de promover, criar backup do Production asset atual e promover Dev→Production com readback.

## Não-ações

Não foi alterado:

- Production
- Produtos
- Preço
- Estoque
- Checkout
- Apps
- GMC/feed
- Klaviyo
- Meta
- Tiny
- Campanhas/envios

## Próxima decisão

Se aprovado, executar promoção Dev→Production do mesmo asset Dev do Batch 6:

`Aprovado subir Batch 6 Curadoria LK para Production`

Escopo da aprovação: somente `snippets/lk-variante-top30-visited.liquid` no Production theme. Sem produto, preço, estoque, checkout, apps, GMC/feed, Klaviyo/Meta/Tiny ou campanha.
