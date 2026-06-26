# Curadoria LK — Batch 7 Dev upload / approval packet Production

## Status

Batch 7 aplicado no Dev theme após aprovação explícita de Lucas: `Aprovo`.

- Dev theme ID: `155065450718`
- Production theme ID: `155065417950`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Dev readback: match
- Production unchanged: true
- Dev SHA prefix: `91c5bed42a99`

## Grupos no Batch 7

1. Adidas Samba OG regular
   - Marker: `top30-adidas-samba-og-regular`
   - Produtos no grupo: 8
   - Sinal 180d no pacote read-only: 15 unidades / 15 pedidos
   - Filtro: exclui Samba Jane, Wales Bonner, Kith, Messi, Pony, Liberty London, Leopard Pack, kids e variações distintas.

2. Nike Dunk Low regular
   - Marker: `top30-nike-dunk-low-regular`
   - Produtos no grupo: 8
   - Sinal 180d no pacote read-only: 11 unidades / 11 pedidos
   - Filtro: exclui SB, Travis, Off-White, Supreme, Ambush, Union, Fragment, CLOT, Stranger Things, kids/GS/PS/TD.

3. Adidas Tokyo regular
   - Marker: `top30-adidas-tokyo-regular`
   - Produtos no grupo: 6
   - Sinal 180d no pacote read-only: 11 unidades / 11 pedidos

4. Puma Speedcat regular
   - Marker: `top30-puma-speedcat-regular`
   - Produtos no grupo: 8
   - Sinal 180d no pacote read-only: 9 unidades / 8 pedidos

5. Air Jordan 4 regular
   - Marker: `top30-nike-air-jordan-4-regular`
   - Produtos no grupo: 8
   - Sinal 180d no pacote read-only: 0 unidades / 0 pedidos
   - Incluído por cobertura semântica limpa/viável, não por performance recente.

## QA Dev

Arquivos de evidência:

- `dev-upload-readback-report.json`
- `dev-static-api-qa-batch7.json`
- `dev_before_batch7.liquid`
- `prod_before_batch7.liquid`
- `dev_after_batch7.liquid`
- `dev_readback_batch7.liquid`

Resultado: pass

- Markers Batch 7 no Dev readback: 5/5, exatamente 1 ocorrência cada.
- Cada grupo tem `handles_count > 5`.
- Simulação: cada current renderiza 5 cards.
- Produto atual nunca aparece nos próprios cards.
- Imagens: URLs Shopify CDN válidas.
- Amostras públicas `/products/{handle}.js`: OK.
- Malformed URL count: 0.
- Backslash quote count: 0.
- Balanceamento básico Liquid:
  - `for/endfor`: 10/10
  - `if/endif`: 15/15
- Production unchanged: true.

## Risco

- Baixo/médio: mudança de tema PDP, visual/CRO. Ainda não afeta Production.
- Air Jordan 4 tem menor sinal de pedidos recentes; incluído como cobertura semântica.
- Adidas Tokyo tem 6 handles limpos, passa a regra e renderiza 5 alternativas.

## Rollback Dev

Re-upar:

- `dev_before_batch7.liquid`

para:

- `snippets/lk-variante-top30-visited.liquid` no Dev theme.

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

Se aprovado, executar promoção Dev→Production do mesmo asset Dev do Batch 7:

`Aprovado subir Batch 7 Curadoria LK para Production`

Escopo da aprovação: somente `snippets/lk-variante-top30-visited.liquid` no Production theme. Sem produto, preço, estoque, checkout, apps, GMC/feed, Klaviyo/Meta/Tiny ou campanha.
