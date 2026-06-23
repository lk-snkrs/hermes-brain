# Receipt — Shopify collection `Winter by LK`

- Data/hora: 2026-06-22 UTC
- Agente/profile: lk-growth
- Pedido: criar coleção de inverno de vestuário, somente camisetas manga longa, moletons, calças e jaquetas; esgotados por último.
- Aprovação informada no chat: “O lucas aprova”.
- Classificação: Shopify production write.

## Ação executada
Criada smart collection no Shopify production.

## Readback Shopify
- HTTP criação: 201
- HTTP readback: 200
- ID: `1128848883934`
- Título: `Winter by LK`
- Handle: `winter-by-lk`
- URL pública: `https://lksneakers.com.br/collections/winter-by-lk`
- Publicada em: `2026-06-22T13:30:38-03:00`
- Sort order registrado: `manual`
- Disjunctive/OR: `true`
- Count Admin por collection_id: `208`
- Count público renderizado na página: `129 itens`

## Regras da coleção
OR entre:
- `type equals Calça`
- `type equals Moletom`
- `type equals Jaqueta`
- `tag equals Camiseta Manga Longa`
- `tag equals Camiseta manga longa`

## Evidência pública
Fetch da URL pública retornou página ativa com title:
`Winter by LK: 129 modelos | LK Sneakers`

## Limite / ponto pendente
A regra “esgotados por último” não foi validada por consulta direta de estoque/inventory, pois LK Stock é o dono obrigatório de disponibilidade/estoque. A coleção foi criada e o tema renderiza a página pública; se for necessária garantia operacional de ordem por disponibilidade, deve haver validação/handoff com `lk-stock` ou ajuste seguro em dev theme/preview.

## Rollback
Excluir/despublicar a smart collection ID `1128848883934` / handle `winter-by-lk`. Se houver link de navegação adicionado futuramente, remover o link também.

## Secrets
Nenhum valor de secret impresso. `values_printed=false`.
