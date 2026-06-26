# Gate B — Local Verification Runbook

> Escopo: verificar a implementação local/offline/dry-run do Gate B. Não ativa webhook público, cron real, gateway, bot ou write externo.

## Pré-condições

- Rodar a partir da raiz do Brain: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Usar Python local disponível.
- Não usar secrets.
- Usar banco temporário fora do Brain ou em `/tmp`.

## Comando principal

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Critério de aceite:

- saída com todos os testes OK;
- zero failures/errors;
- nenhum arquivo `.db` real criado no Brain;
- writes externos `0`.

## Verificação manual do schema

```bash
python3 - <<'PY'
import sqlite3, tempfile
from pathlib import Path
schema = Path('areas/lk/sub-areas/stock/scripts/schema_gate_b.sql').read_text()
with tempfile.TemporaryDirectory() as tmp:
    db = Path(tmp) / 'gate_b.db'
    conn = sqlite3.connect(db)
    conn.executescript(schema)
    tables = {r[0] for r in conn.execute("select name from sqlite_master where type='table'")}
    print(sorted(tables))
PY
```

Deve listar, no mínimo:

- `products`
- `variants`
- `stock_snapshots`
- `sales_velocity`
- `demand_signals`
- `scores`
- `event_ledger`
- `receipts`
- `schema_migrations`

## Verificação manual de idempotência webhook fixture

```bash
DB=$(mktemp /tmp/lk-stock-gate-b.XXXXXX.db)
python3 areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py \
  --db "$DB" \
  --fixture areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json \
  --provider shopify \
  --event-type shopify_order_paid
python3 areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py \
  --db "$DB" \
  --fixture areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json \
  --provider shopify \
  --event-type shopify_order_paid
rm -f "$DB"
```

Critério de aceite:

- primeira execução: `status` = `processed`;
- segunda execução: `status` = `ignored`;
- `writes_externos` = `0` nas duas.

## Verificação manual de freshness cron dry-run

```bash
DB=$(mktemp /tmp/lk-stock-gate-b.XXXXXX.db)
python3 areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py \
  --db "$DB" \
  --fixture areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json \
  --provider shopify \
  --event-type shopify_order_paid
python3 areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py \
  --db "$DB" \
  --fixture areas/lk/sub-areas/stock/fixtures/webhook_tiny_stock_snapshot.json \
  --provider tiny \
  --event-type tiny_stock_snapshot
python3 areas/lk/sub-areas/stock/scripts/stock_daily_reconcile.py --db "$DB" --mode success
python3 areas/lk/sub-areas/stock/scripts/stock_daily_reconcile.py --db "$DB" --mode failure
python3 areas/lk/sub-areas/stock/scripts/stock_query_a1.py --db "$DB"
rm -f "$DB"
```

Critério de aceite:

- success marca `cron_diario`;
- failure marca `stale`;
- query A1 com `stale` inclui `NÃO CONFIRMADO` e pede Tiny/fonte viva;
- `telegram_sent` permanece `false` no OK;
- writes externos `0`.

## Se falhar

1. Não avançar para runtime.
2. Corrigir localmente com TDD.
3. Reexecutar o comando principal.
4. Gerar receipt novo com falha/correção/evidência.

## Próximo gate depois de passar

Só depois de testes executados e aprovados, preparar decisão de Lucas para runtime real usando:

`areas/lk/sub-areas/stock/approval-packets/gate-b-runtime-activation-preview.md`
