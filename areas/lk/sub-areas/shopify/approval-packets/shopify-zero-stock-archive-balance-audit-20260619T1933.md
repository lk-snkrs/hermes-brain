# Shopify zero-stock archive balance audit — 2026-06-19T19:33Z

## Motivo

Lucas corrigiu que `variant_count`/"variantes zeradas" não é prova suficiente. O critério correto para arquivar é saldo total 0 em todas as variantes vendáveis/SKUs do produto.

## Fonte auditada

- Stock OS DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260619T162035Z.db`
- Critério da lista original: `ACTIVE + published/online + >=360d without paid purchase + every variant exact handle+SKU in Stock OS local_consult_safe=1 identity_resolved_safe=1 explicit zero stock observation`
- Tabela auditada: `current_local_stock`
- Campos usados: `stock_quantity_sum_observed`, `stock_quantity_max_observed`, `stock_positive_observed`, `stock_zero_observed`, `stock_source`, `source_observed_at`, `local_consult_safe`, `identity_resolved_safe`.

## Resultado

- Produtos arquivados auditados: 28
- Produtos arquivados com todas as variantes/SKUs confirmadas saldo 0: 28/28
- Produtos arquivados com saldo positivo observado: 0
- Produtos arquivados com SKU ausente/unsafe/ambíguo na DB local: 0
- Próximo lote de 10 auditado: 10/10 com todas as variantes/SKUs confirmadas saldo 0
- Próximo lote com saldo positivo observado: 0
- Próximo lote com SKU ausente/unsafe/ambíguo: 0

## Observação importante

O texto anterior no Telegram usou `Variantes zeradas: N`, mas esse rótulo era ruim. O número `N` é a quantidade de variantes/SKUs auditados do produto. A confirmação real de estoque zero veio de `current_local_stock`/Tiny full sync, por SKU, com `local_consult_safe=1`, `identity_resolved_safe=1` e estoque observado 0.

## Próxima regra operacional

Em lotes futuros, não apresentar `variant_count` como `variantes zeradas`. Usar `SKUs auditados: N` e, quando necessário, `saldo total confirmado: 0` com freshness/fonte.
