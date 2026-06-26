# Receipt — LK WhatsApp responder / perguntas operacionais de reposição e qualidade

Data: 2026-05-26  
Área: LK Operações / WhatsApp responder  
Status: implementado e verificado

## Pedido limpo
Lucas aprovou seguir com as próximas possibilidades de perguntas para o Hermes no WhatsApp LK.

## O que foi implementado
- Intenção operacional read-only (`ops`) para perguntas de reposição, ruptura, baixo estoque e qualidade de cadastro.
- Resposta para `o que preciso repor hoje?` cruzando vendas Shopify recentes com estoque Tiny.
- Resposta para `quais produtos venderam e ficaram zerados?`.
- Resposta para `quais produtos estão com 1 par?` / baixo estoque.
- Resposta para `tem pedido pago sem SKU?` e `sem tamanho`, com exemplos de pedidos/itens problemáticos.
- Comparativo `vendas essa semana vs semana passada` além de `hoje vs ontem`.
- Help/examples atualizados com os novos comandos.

## Exemplos suportados
- `@Hermes o que preciso repor hoje?`
- `@Hermes quais produtos venderam e ficaram zerados?`
- `@Hermes quais produtos estão com 1 par?`
- `@Hermes tem pedido pago sem SKU?`
- `@Hermes vendas essa semana vs semana passada`

## Verificações
- `py_compile`: OK.
- Selftest offline/parser: OK.
- Selftest live Tiny read-only: OK.
- Shopify+Tiny live read-only para baixo estoque: OK.
- Shopify live read-only para qualidade de dados: OK.
- Shopify live read-only para semana vs semana passada: OK.
- Responder reiniciado na porta 8787.
- Health local `/wacli`: 200 OK.

## Guardrails
- Sem write Shopify/Tiny.
- Sem criação de compra automática.
- Sem reserva.
- Sem contato com cliente/fornecedor.
- Sem alteração em Docker, gateway principal, Traefik ou VPS.

## Observação operacional
As respostas de reposição são recomendações internas para revisão do time. Estoque Tiny pode aparecer como saldo negativo em alguns SKUs; a resposta usa `saldo` e não promete disponibilidade externa.
