# Stock Cockpit human decision queue — 2026-06-30

- generated_at_utc: `2026-06-30T14:41:01.475354+00:00`
- values_printed: false
- external_writes: 0

## Por que existe

Lucas pediu "vamos corrigir". A checagem viva mostrou que a correção automática ainda é insegura:

- Shopify duplicate 18: `write_ready=0`.
- Tiny missing 116: `write_ready=0`.

Então a correção segura agora é transformar isso em fila de decisão exata para `lk-shopify`/`lk-stock`/Lucas/Júlio preencherem os alvos. Depois disso, o Hermes consegue gerar dry-run e executar somente as linhas aprovadas.

## Arquivos de decisão

- `areas/lk/sub-areas/stock/reports/stock-cockpit-human-decision-queue-20260630/shopify_duplicate18_decision_form.csv`
- `areas/lk/sub-areas/stock/reports/stock-cockpit-human-decision-queue-20260630/tiny_missing116_decision_form.csv`

## Campos que desbloqueiam write

### Shopify duplicate 18

Preencher por variante:

- `decision_target_sku`
- `decision_action`: `keep_current`, `set_target_sku`, `blank_sku` ou `ignore`

Com isso dá para gerar preview SKU-only com rollback por `variant_id`.

### Tiny missing 116

Preencher por linha:

- `decision_tiny_id`
- `decision_target_codigo`
- `decision_action`: `set_codigo_existing_tiny`, `create_tiny_variation`, `mark_no_cadastro` ou `wait_shopify_dedupe`

Com isso dá para usar `lk-tiny produtos codigo-alterar --dry-run` e só depois live write aprovado.

## Estado final desta execução

Nenhum write externo executado. A correção avançou até o limite seguro: filas exatas de decisão + preview dos 18 duplicados.
