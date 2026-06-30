# Stock Cockpit — Shopify duplicate first batch final status — 2026-06-30

- generated_at_utc: `2026-06-30T15:08:56.328207+00:00`
- values_printed: false
- actual_external_writes_verified: 0

## Pedido

Lucas aprovou o primeiro lote exato: 3 SKU-only writes com rollback/readback.

## Resultado

Nenhuma alteração foi aplicada no Shopify.

| Attempt | Método | Resultado | Readback |
|---|---|---|---|
| 1 | `productVariantsBulkUpdate` | Falhou: input `ProductVariantsBulkInput` não aceita `sku` | 0/3 alterados |
| 2 | `inventoryItemUpdate` | Falhou: `ACCESS_DENIED`, requer `write_inventory` e permissão de usuário para atualizar inventory item | 0/3 alterados |

## Readback final

- `45968993911006`: continua `183A872`.
- `45968993943774`: continua `183A872`.
- `47604797472990`: continua `FJ3453-200`.

## Integração Shopify

Smoke read-only do broker está OK:

- `shopify_lk`: `status=ok`, `method=broker_shopify_store_execute`, `values_printed=false`.

O bloqueio não é auth geral; é escopo/permissão para mutation de SKU via InventoryItem:

- requerido: `write_inventory` + permissão do usuário/app para atualizar inventory item.

## Próximo destravamento real

Abrir/autorizar reauth/ajuste controlado do Shopify broker com escopo/permissão `write_inventory`, ou executar esse lote por operador humano com permissão equivalente no Admin.

Depois da permissão, rerodar o mesmo packet:

- `areas/lk/sub-areas/stock/approval-packets/stock-cockpit-shopify-duplicate-first-batch-20260630/first_batch_proposed_targets.json`

## Não alterado

Tiny, Supabase, estoque, preço, título, imagem, coleção, texto de produto e fornecedores não foram alterados.
