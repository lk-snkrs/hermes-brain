# Approval captured — aplicar correção de esgotados com fallback Shopify

Data: 2026-05-26
Destino: LK Growth / Shopify Collections
Status deste turno: approval captured + packet local; Shopify write não executado neste contexto.

## Pedido limpo

Lucas aprovou aplicar a correção da ordenação das 10 coleções piloto, corrigindo a lógica de esgotados para usar Tiny como fonte primária e fallback Shopify quando todas as variantes estiverem com inventory <= 0.

Escopo aprovado:

- 10 coleções piloto já trabalhadas;
- snapshot pré-write imediato;
- Tiny/SQLite como fonte primária de estoque;
- fallback Shopify all-zero para produtos sem match Tiny que aparecem ESGOTADO no storefront;
- mover qualquer `out_of_stock_*` para o final;
- aplicar `collectionReorderProducts`;
- poll do job via `job(id: $id) { id done }`;
- readback por coleção;
- receipt final;
- sem cron.

## Evidências

Screenshot de Lucas mostrou produto ESGOTADO no topo da coleção Nude Project.

Leitura Shopify Admin read-only confirmou:

- coleção `Nude Project` / `nude-project` / ID `445072474334`;
- produto `Moletom Nude Project Side-Eye Zip-Up Black Preto` / ID `9175542464734` na posição 6;
- variantes com inventory `[0, 0, 0, 0, 0]`;
- outro produto all-zero no top 12: `Camiseta Baby Look Nude Project Juicy Cherry Branca`, posição 10.

## Preview técnico já preparado

Script local corrigido:

`/opt/data/hermes_bruno_ingest/scripts/lk_collection_auto_sort_apply_pilot_20260526.py`

Correções:

1. `shopify_all_variants_zero_or_negative(product)` adicionado;
2. `classify_stock()` retorna `out_of_stock_shopify_fallback` quando Tiny não tem positivo e todas variantes Shopify <= 0;
3. `proposed_order()` move qualquer `out_of_stock_*` para o final;
4. reason code `esgotado_shopify_fallback_final`;
5. snapshot separa Tiny vs Shopify fallback;
6. poll corrigido para `job(id: $id) { id done }`;
7. validação local `py_compile` OK.

## Risco

- Altera merchandising público das 10 coleções piloto.
- Pode mover produtos com forte histórico de venda para baixo se estiverem all-zero no Shopify e sem Tiny positivo.
- Shopify fallback é sinal de merchandising, não substitui Tiny como verdade final de estoque.

## Bloqueio deste contexto

Neste turno, a execução está restrita a documentação/packet local. Não executar Shopify write aqui.

Não foi executado:

- `collectionReorderProducts`;
- cron;
- alteração de produto, preço, estoque, tema, SEO, tag, checkout, campanha ou comunicação.

## Rollback previsto

Antes do apply, gerar snapshot pré-write imediato da ordem atual das 10 coleções.

Rollback: restaurar `current_order_product_ids` do snapshot via `collectionReorderProducts`, com poll e readback por coleção.

## Próxima decisão / wording executável

Executar em contexto LK Shopify/Growth write-enabled:

`Aplicar correção nas 10 coleções piloto: snapshot imediato; Tiny primário; fallback Shopify all-zero para ESGOTADO; mover out_of_stock_* ao final; collectionReorderProducts; poll job(id); readback; receipt; sem cron; sem produto/preço/estoque/tema/SEO/tag/campanha.`
