# Router correction receipt — LK Shopify/Growth write-enabled unlock

Data: 2026-05-26

## Pedido limpo

Lucas exigiu desbloquear o roteamento para `LK Shopify/Growth write-enabled` após o Task Router continuar classificando o apply aprovado como Hermes Geral/read-only.

## Alteração local executada

Arquivo alterado:

`/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`

Rota ajustada:

`lk-shopify-collections-auto-ordering-write-enabled`

## O que foi ampliado

A rota agora reconhece, além dos termos técnicos antigos:

- `esgotados no final`
- `esgotados ao final`
- `coleções piloto` / `10 coleções piloto`
- `fallback Shopify`
- `mover esgotados`
- `corrigir as 10 coleções`
- `LK Shopify/Growth write-enabled`
- variação com espaço: `L K Shopify/Growth write-enabled`
- `desbloquear`, `liberar`

## Resultado esperado do router

Pedidos com a combinação de LK Shopify/Growth write-enabled + desbloqueio ou com coleção auto-ordering + aprovação explícita devem sair como:

- `action`: `executar_aqui`
- `context`: `lk_growth_shopify`
- `handoff_required`: `false`
- permitidos: snapshot, Tiny/SQLite read, `collectionReorderProducts`, poll, readback, receipt
- ainda bloqueados sem nova aprovação: cron, escopo novo, produto/preço/estoque/disponibilidade, theme/SEO/tags/checkout, campanha/comunicação

## Verificação

A leitura do arquivo confirmou o patch nas linhas da rota. A execução de teste por terminal/execute_code ainda foi bloqueada pelo preflight da própria mensagem atual, então o teste dinâmico precisa ocorrer no próximo turno já roteado corretamente.

## Importante

Nenhum write Shopify foi executado neste turno.
Nenhum produto/preço/estoque/tema/campanha foi alterado.
Nenhum cron foi criado.
