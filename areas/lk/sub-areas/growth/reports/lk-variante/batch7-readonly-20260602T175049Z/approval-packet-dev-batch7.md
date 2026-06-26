# Curadoria LK — Batch 7 read-only candidate packet / aprovação para Dev

## Status

Pacote montado em modo read-only. Nenhum upload de tema foi executado.

## Fontes lidas

- Shopify Theme Asset API GET — Production `snippets/lk-variante-top30-visited.liquid` e snippets Curadoria relacionados.
- Shopify Products API GET — catálogo ativo/publicado.
- Shopify Orders API GET — janela de 180 dias, pedidos pagos/paid-like e não cancelados, sem PII no relatório.
- Storefront público `/products/{handle}.js` — disponibilidade pública dos handles selecionados.

## Batch 7 recomendado para Dev

1. Adidas Samba OG regular
   - Marker proposto: `top30-adidas-samba-og-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 15 unidades / 15 pedidos
   - Filtro: exclui Samba Jane, Wales Bonner, Kith, Messi, Pony, Liberty London, Leopard Pack, kids e variações materialmente distintas.

2. Nike Dunk Low regular
   - Marker proposto: `top30-nike-dunk-low-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 11 unidades / 11 pedidos
   - Filtro: exclui SB, Travis, Off-White, Supreme, Ambush, Union, Fragment, CLOT, Stranger Things, kids/GS/PS/TD.

3. Adidas Tokyo regular
   - Marker proposto: `top30-adidas-tokyo-regular`
   - Produtos: 6
   - Sinal 180d nos selecionados: 11 unidades / 11 pedidos
   - Filtro: exclui MJ/Jane/collabs para manter linha regular.

4. Puma Speedcat regular
   - Marker proposto: `top30-puma-speedcat-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 9 unidades / 8 pedidos

5. Air Jordan 4 regular
   - Marker proposto: `top30-nike-air-jordan-4-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 0 unidades / 0 pedidos nos 180d lidos
   - Motivo: expansão semântica limpa com estoque/handles públicos; menor prioridade comercial, mas grupo viável.
   - Filtro: exclui collabs/cápsulas e RM x Nigel.

## Bloqueados / removidos na limpeza

- New Balance 204L, Onitsuka Mexico 66 Sabot, parte de Samba/Taekwondo: bloqueados por overlap com Curadoria já coberta ou por não restar >5 opções limpas após excluir collabs/cápsulas.
- Taekwondo regular: bloqueado porque, após remover Caroline Hu x CLOT e cross-brand/itens suspeitos, não sobrou quantidade segura suficiente para 5 cards com current excluído.

## QA read-only/local

Arquivos:

- `batch7-readonly-candidates.json`
- `batch7-duplicate-coverage-check.json`
- `batch7-expanded-safe-candidates.json`
- `batch7-strict-safe-candidates.json`
- `batch7-proposed-append.liquid`
- `batch7-proposed-static-qa.json`

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

- Baixo/médio: se aprovado, será alteração de tema no Dev, ainda sem afetar Production.
- Air Jordan 4 tem menor sinal de pedidos recente; incluído por viabilidade semântica/cobertura, não por performance.
- Adidas Tokyo tem só 6 handles limpos, mas passa a regra (>5) e renderiza 5 alternativas.

## Rollback planejado para Dev

Antes de qualquer upload no Dev, snapshot do asset Dev atual e do Production atual. Rollback do Dev = re-upar o snapshot `dev_before_batch7.liquid`.

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

`Pode aplicar no dev o Batch 7 da Curadoria LK com Adidas Samba OG, Nike Dunk Low, Adidas Tokyo, Puma Speedcat e Air Jordan 4, sem mexer em Production/produtos/preço/estoque/apps.`
