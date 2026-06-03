# Curadoria LK — Batch 9 read-only candidate packet / aprovação para Dev

## Status

Pacote montado em modo read-only. Nenhum upload de tema foi executado.

## Fontes lidas

- Shopify Theme Asset API GET — Production `snippets/lk-variante-top30-visited.liquid`.
- Shopify Products API GET — catálogo ativo/publicado.
- Shopify Orders API GET — janela de 180 dias, pedidos paid-like e não cancelados, sem PII no relatório.
- Storefront público `/products/{handle}.js` — disponibilidade pública dos handles selecionados.

## Batch 9 recomendado para Dev

1. Adidas Samba Jane regular
   - Marker proposto: `top30-adidas-samba-jane-regular`
   - Produtos: 7
   - Sinal 180d nos selecionados: 25 unidades / 24 pedidos
   - Observação: separado de Samba OG/Tokyo/Jane-adjacent; grupo limpo de Samba Jane.

2. Yeezy 350 regular
   - Marker proposto: `top30-yeezy-350-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 24 unidades / 24 pedidos
   - Filtro: exclui Foam Runner, Slide, 500 e 700.

3. Alo Accolade line
   - Marker proposto: `top30-alo-accolade-line`
   - Produtos: 8
   - Sinal 180d nos selecionados: 19 unidades / 14 pedidos
   - Apparel segue regra LK de linha/look coerente.

4. Alo Airbrush line
   - Marker proposto: `top30-alo-airbrush-line`
   - Produtos: 8
   - Sinal 180d nos selecionados: 3 unidades / 3 pedidos
   - Apparel segue regra LK de linha/look coerente.

5. Alo Serenity Coverup line
   - Marker proposto: `top30-alo-serenity-coverup-line`
   - Produtos: 7
   - Sinal 180d nos selecionados: 0 unidades / 0 pedidos nos 180d lidos
   - Motivo: grupo de apparel por linha/modelo coerente e com handles públicos disponíveis.

## Bloqueados / removidos na limpeza

- Nike SB Dunk: bloqueado porque o set disponível é pesado em collabs/cápsulas; misturar essas colaborações violaria a regra de separar cápsulas.
- Nike Air Max 1: bloqueado porque o set disponível era quase todo collab/cápsula (Patta/Concepts/Kasina/Stranger Things), não grupo regular limpo.
- Lululemon Define: bloqueado porque só encontrou 5 candidatos ativos/públicos; com o produto atual excluído, renderizaria 4 cards.
- Alo `becalm`/Coverup: removido do grupo Serenity Coverup porque o handle é inconsistente, embora o título público pareça relacionado.

## QA read-only/local

Arquivos:

- `batch9-discovery-readonly.json`
- `batch9-cluster-discovery.json`
- `batch9-apparel-term-discovery.json`
- `batch9-selected-final.json`
- `batch9-proposed-append.liquid`
- `batch9-proposed-static-qa.json`

Resultado:

- Cada grupo selecionado tem `handles_count > 5`.
- Simulação: cada current renderiza 5 cards.
- Produto atual nunca aparece nos próprios cards.
- Imagens: URLs Shopify CDN válidas.
- Malformed URL count: 0.
- Aspas/backslash problemáticas: 0.
- Balanceamento básico Liquid:
  - `for/endfor`: 10/10
  - `if/endif`: 15/15
- Sem upload Dev/Production nesta etapa.

## Risco

- Baixo/médio se aprovado para Dev: alteração de tema no Dev, sem afetar Production.
- Alo Airbrush/Serenity Coverup têm menor sinal recente de vendas; entraram por cobertura semântica/linha e disponibilidade pública.
- Apparel Alo segue a exceção aprovada para linha/look coerente; sneakers mantêm separação por silhueta/cápsula.

## Rollback planejado para Dev

Antes de qualquer upload no Dev, snapshot do asset Dev atual e do Production atual. Rollback do Dev = re-upar o snapshot `dev_before_batch9.liquid`.

## Não-ações

Não foi alterado:

- Dev theme
- Production theme
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

Para aplicar esse pacote no Dev theme, Lucas precisa aprovar explicitamente:

`Pode aplicar no Dev o Batch 9 da Curadoria LK com Adidas Samba Jane, Yeezy 350, Alo Accolade, Alo Airbrush e Alo Serenity Coverup, sem mexer em Production/produtos/preço/estoque/apps.`
