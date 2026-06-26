# Correction packet — esgotados ainda aparecendo no topo (Nude Project)

Data: 2026-05-26
Coleção: Nude Project (`/collections/nude-project`)
Tipo: diagnóstico read-only + correção local do script; sem Shopify write neste turno.

## Evidência visual

Screenshot enviado por Lucas mostra produto com selo `ESGOTADO` na segunda linha da grade da coleção Nude Project, ainda acima de produtos disponíveis.

Produto identificado:

- `Moletom Nude Project Side-Eye Zip-Up Black Preto`
- Shopify product ID: `9175542464734`
- posição live observada via Admin read-only: 6

## Evidência Shopify read-only

Leitura Admin REST read-only da coleção Nude Project confirmou:

- coleção `Nude Project` está com `sort_order = manual`
- produto `Moletom Nude Project Side-Eye Zip-Up Black Preto` está na posição 6
- variantes do produto retornaram `inventory_quantity = [0, 0, 0, 0, 0]`
- sinal merchandising Shopify: todas as variantes <= 0, logo deve ser tratado como `out_of_stock_shopify_fallback` quando Tiny não der match

Também foi encontrado outro produto all-zero no topo 12:

- `Camiseta Baby Look Nude Project Juicy Cherry Branca`, posição 10, variantes `[0,0,0,0,0]`

## Causa raiz

O script de apply ainda classificava apenas `out_of_stock_tiny_signal` como esgotado final.

Quando o SKU não tinha match no Tiny, o produto ficava como `unknown_missing_tiny_signal` e continuava elegível para top 8/performance, mesmo aparecendo como `ESGOTADO` no storefront.

## Correção local aplicada no script

Arquivo corrigido localmente:

`/opt/data/hermes_bruno_ingest/scripts/lk_collection_auto_sort_apply_pilot_20260526.py`

Mudanças:

1. adicionada função `shopify_all_variants_zero_or_negative(product)`;
2. `classify_stock()` agora retorna `out_of_stock_shopify_fallback` quando não há Tiny positivo e todas as variantes Shopify têm inventory <= 0;
3. `proposed_order()` agora move qualquer status que começa com `out_of_stock_` para o final;
4. reason code novo: `esgotado_shopify_fallback_final`;
5. snapshot agora separa:
   - `sold_out_product_ids_final_bucket`
   - `sold_out_tiny_product_ids_final_bucket`
   - `sold_out_shopify_fallback_product_ids_final_bucket`
6. poll corrigido para `job(id: $id) { id done }`.

Validação local:

- `python3 -m py_compile ...` OK.

## O que NÃO foi feito

- Não executei `collectionReorderProducts` neste turno.
- Não criei cron.
- Não alterei produto, preço, estoque, tema, SEO, tag, checkout, campanha ou comunicação.

## Próximo passo para corrigir a vitrine

Executar o apply corrigido, limitado às 10 coleções piloto já aprovadas, com:

1. snapshot pré-write imediato;
2. classificação Tiny primária + fallback Shopify all-zero;
3. esgotados no final;
4. `collectionReorderProducts`;
5. poll;
6. readback;
7. receipt final.

Rollback: restaurar a ordem do snapshot pré-write imediato via `collectionReorderProducts`, com poll/readback.
