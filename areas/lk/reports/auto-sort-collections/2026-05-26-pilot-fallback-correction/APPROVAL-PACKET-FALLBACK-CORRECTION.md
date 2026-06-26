# Approval packet — correção das 10 coleções piloto com fallback Shopify para esgotados

Data: 2026-05-26
Destino: LK Shopify/Growth write-enabled

## Pedido limpo

Lucas aprovou corrigir as 10 coleções piloto usando:

- Tiny como sinal primário de estoque;
- fallback Shopify para produtos sem match Tiny, mas com todas as variantes zeradas;
- snapshot antes do write;
- mover esgotados ao final;
- `collectionReorderProducts`;
- poll correto via `job(id:)`;
- readback pós-write;
- receipt;
- sem cron;
- sem mexer em produto, preço, estoque, tema ou campanha.

## Evidências do erro anterior

Na coleção `Nude Project`, o produto `Moletom Nude Project Side-Eye Zip-Up Black Preto` apareceu na posição 6 com selo ESGOTADO no storefront.

Diagnóstico read-only já realizado:

- Shopify produto individual: 5 variantes, todas com `inventory_quantity = 0`.
- Tiny: sem match para os SKUs `NUD-2464734-*` no snapshot local.
- Script anterior: endpoint `collections/{id}/products` não trouxe `variants/SKUs`, causando classificação `unknown_no_sku` e impedindo a regra de esgotado-final.

## Regra corrigida

Classificação de estoque para merchandising de coleção:

1. Se Tiny tem SKU com saldo positivo: `in_stock_tiny_signal`.
2. Se Tiny conhece todos os SKUs e todos estão zerados: `out_of_stock_tiny_signal`.
3. Se Tiny não conhece ou é parcial, mas Shopify conhece variantes e todas estão zeradas: `out_of_stock_shopify_fallback`.
4. Se Tiny não conhece ou é parcial, mas Shopify tem alguma variante positiva: `in_stock_shopify_fallback_tiny_missing_or_partial`.
5. Não afirmar que fallback Shopify é verdade Tiny; rotular separadamente.

Todos os status que começam com `out_of_stock` devem ir para o bloco final da coleção.

## Preview específico já validado para Nude Project

Com a regra corrigida:

- `Moletom Nude Project Side-Eye Zip-Up Black Preto`: posição atual 6 → posição proposta 68.
- `Camiseta Baby Look Nude Project Juicy Cherry Branca`: posição atual 10 → posição proposta 70.
- Top 8 proposto da Nude fica sem produtos esgotados visíveis.

## Execução necessária

Executar em contexto write-enabled:

1. Recomputar as 10 coleções piloto com produto individual/GraphQL variants, não confiar em `collections/{id}/products` para variants.
2. Criar snapshot imediato pré-write com ordem live atual e target proposto.
3. Aplicar `collectionReorderProducts` por coleção.
4. Calcular moves sequenciais a partir da ordem live → target, não usar moves absolutos ingênuos.
5. Poll com query:

```graphql
query job($id: ID!) { job(id: $id) { id done } }
```

6. Readback REST/GraphQL da ordem live.
7. Confirmar que cada coleção bate com o target.
8. Gerar receipt final.
9. Rodar scan simples de segredos nos artefatos antes de compartilhar caminhos.

## Escopo das 10 coleções piloto

- Nude Project
- Jacquemus
- Saint Studio
- Calça | Apparels
- Pace
- Aimé Leon Dore
- Nike Mind
- Onitsuka Tiger Mexico 66
- Onitsuka Tiger Mexico 66 Sabot
- Shorts

## Bloqueio neste turno

Apesar da aprovação do Lucas, a rota atual de execução bloqueou ferramenta operacional por classificar o pedido como LK operations sensível/read-only. Nenhum Shopify/Tiny write foi executado neste turno.

## Rollback

Rollback deve restaurar a ordem da coleção usando o snapshot pré-write imediato gerado no próprio run de correção, com a mesma mutation `collectionReorderProducts`, polling via `job(id:)` e readback final.

## Não ações

- Não criar cron.
- Não alterar produtos.
- Não alterar preço.
- Não alterar estoque/disponibilidade.
- Não alterar tema.
- Não alterar SEO/tags.
- Não alterar checkout.
- Não alterar campanha/comunicação.

## Completeness hardening — 2026-06-14

Decisão solicitada / ação proposta: autorizar uma correção write-enabled única nas 10 coleções piloto para mover produtos esgotados ao final usando Tiny como sinal primário e Shopify fallback apenas quando Tiny estiver ausente/parcial.

Escopo permitido: recomputar as 10 coleções listadas, criar snapshot pré-write, aplicar somente `collectionReorderProducts`, fazer polling `job(id:)`, readback da ordem live e receipt final sanitizado.

O que continua bloqueado: nenhum cron, nenhuma alteração de produto, preço, estoque, disponibilidade, tags, SEO, tema, checkout, campanha, cliente, GMC, Tiny write ou lógica fora das 10 coleções piloto.

Opções de aprovação: Lucas pode `Aprovar correção das 10 coleções piloto`, `Ajustar escopo`, `Preview/read-only novamente` ou `Bloquear`. Sem aprovação textual clara e atual, este packet permanece histórico/documental e não autoriza execução.

Secret hygiene: `values_printed=false`; artefatos e receipts devem passar por scan de segredos antes de compartilhamento e nunca devem incluir tokens, service keys, previews de credencial ou dados sensíveis desnecessários.
