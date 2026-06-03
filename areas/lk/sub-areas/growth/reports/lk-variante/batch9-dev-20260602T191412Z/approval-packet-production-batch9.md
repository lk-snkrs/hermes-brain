# Curadoria LK — Batch 9 Dev apply receipt / approval packet Production

## Aprovação Dev

Lucas aprovou via botão inline: `Pode aplicar no Dev o Batch 9`.

## Status

Batch 9 aplicado apenas no Dev theme.

- Dev theme ID: `155065450718`
- Production theme ID: `155065417950`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Dev readback: match
- Production unchanged: true
- SHA Dev readback final: `0b530160154a`

## Grupos no Batch 9 Dev

1. Adidas Samba Jane regular
   - Marker: `top30-adidas-samba-jane-regular`
   - Produtos finais: 7
   - Handles públicos e disponíveis: 7/7
   - Sinal 180d nos selecionados: 25 unidades / 24 pedidos

2. Yeezy 350 regular
   - Marker: `top30-yeezy-350-regular`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8
   - Sinal 180d nos selecionados: 24 unidades / 24 pedidos

3. Alo Accolade line
   - Marker: `top30-alo-accolade-line`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8
   - Sinal 180d nos selecionados: 19 unidades / 14 pedidos

4. Alo Airbrush line
   - Marker: `top30-alo-airbrush-line`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8
   - Sinal 180d nos selecionados: 3 unidades / 3 pedidos

5. Alo Serenity Coverup line
   - Marker: `top30-alo-serenity-coverup-line`
   - Produtos finais: 7
   - Handles públicos e disponíveis: 7/7
   - Sinal 180d nos selecionados: 0 unidades / 0 pedidos nos 180d lidos

## Limpezas / bloqueios

- Nike SB Dunk: bloqueado porque o set disponível é pesado em collabs/cápsulas.
- Nike Air Max 1: bloqueado porque o set disponível era quase todo collab/cápsula.
- Lululemon Define: bloqueado porque só encontrou 5 candidatos públicos; renderizaria 4 cards após excluir current.
- Alo `becalm`/Coverup: removido por handle inconsistente, apesar de título público relacionado.

## QA Dev final

Arquivos:

- `dev-upload-readback-report.json`
- `dev-final-qa-batch9.json`
- `dev_before_batch9.liquid`
- `prod_before_batch9.liquid`
- `dev_readback_batch9.liquid`

Resultado: pass

- Markers no Dev: 5/5, exatamente 1 ocorrência cada
- Cada grupo tem `handles_count > 5`
- Simulação de cada PDP: 5 cards
- Produto atual excluído
- Todos os handles selecionados retornam `/products/{handle}.js` com HTTP 200
- Todos os handles selecionados estão `available=true`
- URLs de imagem: Shopify CDN válidas
- Malformed URL count: 0
- Literais `Liquid error` / `Liquid syntax error`: 0
- Production unchanged: true

## Risco

- Baixo/médio: mudança de tema em Dev; se promovida para Production, afeta visual/CRO de PDPs desses grupos.
- Alo Airbrush/Serenity Coverup têm menor sinal recente de vendas; entraram por cobertura semântica/linha e disponibilidade pública.
- Apparel Alo segue a exceção LK de linha/look coerente; sneakers mantêm separação por silhueta/cápsula.

## Rollback Dev

Rollback do Dev: re-upar `dev_before_batch9.liquid` para `snippets/lk-variante-top30-visited.liquid` no Dev theme.

## Próxima decisão

Se aprovado, executar promoção Dev→Production do mesmo asset Dev final do Batch 9:

`Aprovado subir Batch 9 Curadoria LK para Production`

Escopo da aprovação: somente `snippets/lk-variante-top30-visited.liquid` no Production theme. Sem produto, preço, estoque, checkout, apps, GMC/feed, Klaviyo/Meta/Tiny ou campanha.
