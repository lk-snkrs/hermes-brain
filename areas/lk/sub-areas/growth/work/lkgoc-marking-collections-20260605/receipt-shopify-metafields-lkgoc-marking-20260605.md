# Receipt — Marcação Shopify LKGOC

Data/hora: 2026-06-05T16:56:32
Aprovador: Lucas Cimino no Telegram: "Aprovado… use também uma tag na colação por favor".

## Coleções marcadas
- `new-balance-204l`
- `new-balance-9060`
- `new-balance-530`

## Metafields aplicados em `custom.*`
- `custom.lkgoc_status = optimized`
- `custom.lkgoc_pattern = 204l_canonical`
- `custom.lkgoc_tag = LK Growth Optimized Collection`
- `custom.lkgoc_last_optimized_at = 2026-06-05T16:56:12Z`

## Sobre tag nativa
A API Shopify para `CollectionInput` não expõe campo `tags`, e `Collection` não implementa interface `Taggable` na versão consultada. Portanto, a marcação tipo tag foi aplicada como metafield canônico `custom.lkgoc_tag`.

## Evidência
- Introspecção: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-marking-collections-20260605/collection-input-introspection.json`
- Before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-marking-collections-20260605/before-collections.json`
- Write response: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-marking-collections-20260605/metafields-set-response.json`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-marking-collections-20260605/readback-after-marking.json`

## Rollback
Remover ou limpar os quatro metafields `custom.lkgoc_*` nas coleções acima via `metafieldsDelete`/Admin API.
