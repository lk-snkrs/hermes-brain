# Receipt — Task Router corrigido para piloto Shopify Collections LK

Data: 2026-05-26

## Pedido

Corrigir o Task Router local para reconhecer `LK Shopify/Growth write-enabled` + auto-ordenação de coleções / `collectionReorderProducts` como execução aprovada quando houver aprovação explícita de Lucas.

## Alteração feita

Arquivo editado:

`/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`

Foi adicionada uma rota específica antes das regras genéricas de LK/Tiny/Shopify:

- `route_id`: `lk-shopify-collections-auto-ordering-write-enabled`
- `context`: `lk_growth_shopify`
- `action`: `executar_aqui`
- `handoff_required`: `false`
- permitido no escopo: snapshot, leitura Tiny/SQLite, `collectionReorderProducts` escopado, poll, readback e receipt
- continuam exigindo aprovação nova: escopo novo, cron, produto/preço/estoque/disponibilidade, theme/SEO/tags/checkout, campanha/comunicação

## Teste executado

Foi testada a classificação com o pedido aprovado de Lucas contendo:

- `LK Shopify/Growth write-enabled`
- execução do apply aprovado
- Tiny/SQLite para esgotados
- `collectionReorderProducts`
- sem cron
- aprovação explícita atual

Resultado retornado pelo router:

- `route_id`: `lk-shopify-collections-auto-ordering-write-enabled`
- `action`: `executar_aqui`
- `handoff_required`: `false`

## Não ações

- Não houve Shopify write nesta correção.
- Não houve Tiny write.
- Não houve cron.
- Não houve Docker/gateway/container/restart.

## Próximo passo

Enviar/rodar novamente o pedido LK Shopify/Growth write-enabled para o apply. O roteamento local agora deve classificar como execução permitida dentro do escopo aprovado.
