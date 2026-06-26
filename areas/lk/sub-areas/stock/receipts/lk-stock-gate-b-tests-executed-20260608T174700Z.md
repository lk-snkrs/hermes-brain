# Receipt — Gate B testes executados e correção local

Data UTC: 2026-06-08T17:47:00Z

## Pedido

Lucas respondeu que agora era possível executar comandos e pediu para executar/corrigir.

## Comandos executados

### 1. Tentativa inicial com `python`

```bash
python -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
/usr/bin/bash: line 3: python: command not found
```

Correção aplicada: usar `python3`, que é o binário disponível no host.

### 2. Testes offline

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado final:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 2.937s

OK
```

### 3. Validação manual do schema

Resultado:

```text
tables_ok= True
tables= ['demand_signals', 'event_ledger', 'products', 'receipts', 'sales_velocity', 'schema_migrations', 'scores', 'sqlite_sequence', 'stock_snapshots', 'variants']
```

### 4. Validação manual de idempotência webhook fixture

Resultado:

- primeira execução: `status = processed`;
- segunda execução: `status = ignored`;
- `writes_externos = 0` nas duas.

### 5. Validação manual de freshness/query A1

Resultado:

- `stock_daily_reconcile --mode success`: `freshness = cron_diario`, `telegram_sent = false`, `writes_externos = 0`;
- `stock_daily_reconcile --mode failure`: `freshness = stale`, `receipt_created = true`, `telegram_sent = false`, `writes_externos = 0`;
- `stock_query_a1`: gerou P0 com `Freshness: stale` e aviso `NÃO CONFIRMADO — consultar Tiny/fonte viva agora antes de afirmar disponibilidade/ruptura`.

## Correções aplicadas

1. Fixture `webhook_shopify_order_paid.json` ajustada de `quantity: 3` para `quantity: 6` para representar demanda forte e permitir cenário P0 quando combinado com estoque Tiny crítico.
2. Runbook atualizado para usar `python3` em vez de `python`.
3. Runbook atualizado para carregar primeiro a fixture Shopify de venda e depois a fixture Tiny, garantindo que a query A1 tenha demanda + estoque crítico para validar o bloqueio `stale`.
4. Plano atualizado para marcar Task 10 como executada com evidência real.
5. Skill `lk-stock` atualizada para usar `python3 -m unittest ...` como comando canônico.

## Status final

- Testes offline: passaram, 11/11.
- Runtime externo ativado: 0.
- Writes externos: 0.
- Webhook público: não ativado.
- Cron real: não ativado.
- Gateway/bot: não ativado.
- Tiny/Shopify write: 0.
