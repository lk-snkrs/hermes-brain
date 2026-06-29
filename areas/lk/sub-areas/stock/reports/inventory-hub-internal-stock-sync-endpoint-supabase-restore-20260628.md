# Report — Inventory Hub protected Stock OS sync endpoint + Supabase sync restore — 2026-06-28

## Status

Concluído dentro do escopo aprovado.

## O que foi alterado

### Inventory Hub / Vercel

Commit deployado:

```text
ab7133267938d139932b7f36a04008fd67f99117
fix(stock): add protected stock sync snapshot endpoint
```

Endpoint novo:

```text
GET /api/internal/stock-os/sync-snapshot?q=all&limit=20000
```

Propriedades:

- protegido por machine auth via `STOCK_OS_API_BASIC_AUTH_USER/PASSWORD` ou token equivalente;
- não usa a senha do dashboard público;
- retorna JSON de Stock OS/Supabase contract;
- sem Tiny write;
- sem Shopify write;
- `values_printed=false`.

Deploy Vercel:

```text
Production: https://inventory-id3e3oqht-lk-snkrs-projects.vercel.app
Alias: https://hub.lksnk.dev
Status: Ready
```

### Doppler / broker

- Copiados do Vercel `inventory-hub` para Doppler `lc-keys/prd`:
  - `STOCK_OS_API_BASE_URL`
  - `STOCK_OS_API_BASIC_AUTH_USER`
  - `STOCK_OS_API_BASIC_AUTH_PASSWORD`
- Atualizado `/opt/data/scripts/hermes_doppler.py` para injetar esses nomes no profile `lk-stock`.
- Inventory `lk-stock`: `present_count=14`, `missing_count=0`, `values_printed=false`.

### Sync script

Arquivo atualizado:

```text
/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py
```

Mudanças:

- default source agora é `https://hub.lksnk.dev/api/internal/stock-os/sync-snapshot?q=all&limit=20000`;
- roda via Doppler `--profile lk-stock`;
- aceita payload `results` ou `produtos`, mas valida antes de write;
- rejeita timestamps inválidos em rows para evitar falha de cast;
- valida MR530SG antes de escrever;
- escreve somente `public.lk_stock_snapshots` e `public.lk_stock_items`.

## Verificações

### Testes locais

```text
node --test --test-concurrency=1
```

Resultado:

```text
154 passed / 154
```

Observação: `npm test` paralelo bateu um bug do runner Node (`ERR_TEST_FAILURE Unable to deserialize cloned data` em subprocesso), então rodei sequencialmente como gate forte; passou 154/154.

### GitHub

```text
local HEAD = ab7133267938d139932b7f36a04008fd67f99117
origin/production = ab7133267938d139932b7f36a04008fd67f99117
```

### Endpoint vivo

`/api/internal/stock-os/sync-snapshot?q=MR530SG&limit=50`:

```json
{
  "http": 200,
  "status": "confirmado",
  "result_count": 9,
  "total_count": 9,
  "truncated": false,
  "source_observed_at": "2026-06-26T09:20:06+00:00",
  "results_count": 9,
  "values_printed": false
}
```

Dry-run do script:

```json
{
  "status": "dry_run_ok",
  "run_id": "20260626T092006Z",
  "source_rows": 8550,
  "mr530sg": {
    "rows": 8550,
    "mr530sg_rows": 98,
    "mr530sg_positive_units": 26.0
  },
  "supabase_write": 0,
  "values_printed": false
}
```

### Supabase write/readback

Execução manual do sync:

```json
{
  "status": "ok",
  "run_id": "20260626T092006Z",
  "items": 8550,
  "total_count": 8550,
  "result_count": 8550,
  "source_observed_at": "2026-06-26T09:20:06+00:00",
  "imported_at": "2026-06-28T19:59:02.438673+00:00",
  "duplicate_business_rows": 0,
  "critical_sentinels": [
    {
      "status": "ok",
      "sentinel": "MR530SG",
      "mismatch_count": 0,
      "obsolete_count": 0
    }
  ],
  "source_validation": {
    "rows": 8550,
    "mr530sg_rows": 98,
    "mr530sg_positive_units": 26.0
  },
  "supabase_write": 1,
  "values_printed": false
}
```

Readback Supabase após cron/manual run:

```text
run_id=20260626T092006Z
items=8550
total_count=8550
result_count=8550
imported_at=2026-06-28T20:00:18.536398+00
MR530SG rows=9
MR530SG units=11
```

### Cron

Cron `c45da7bb0fcb`:

```text
last_run_at=2026-06-28T20:00:37.711929+00:00
last_status=ok
next_run_at=2026-06-29T05:20:00+00:00
```

## Guardrails

- Supabase write: executado somente em `public.lk_stock_snapshots` e `public.lk_stock_items`.
- Tiny write: `0`.
- Shopify write: `0`.
- Schema/migration: `0`.
- Envio externo: `0`.
- Secrets impressos: `0`.
- `values_printed=false`.

## Limitação importante

O endpoint e o sync agora estão funcionando, mas `source_observed_at` continua `2026-06-26T09:20:06Z`. Ou seja: restauramos o contrato seguro de sync e o cron voltou a executar OK, mas isso **ainda não prova que os deltas real-time do webhook/Tiny estão entrando no snapshot**.

Próxima etapa recomendada: ligar/promover o ledger/local event processor ao snapshot ou a uma tabela delta Supabase, com novo approval específico.
