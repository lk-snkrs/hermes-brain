# LK Inventory Hub — correção/deploy endpoint upstream Stock OS sync

Data: 2026-07-01
Profile executor: `lk-stock`
Pedido Lucas: `CORRIGIR: corrigir/deployar o endpoint/fonte Hub upstream`

## Resultado

Corrigido e deployado em produção no Vercel. O domínio `https://hub.lksnk.dev` voltou a responder o Hub correto e o endpoint protegido de sync Stock OS agora retorna payload completo a partir do Supabase read model.

## Causa raiz

Havia dois problemas combinados:

1. O código atual do repo `lk-snkrs/inventory-hub` já tinha a lógica Supabase-first correta para `/api/internal/stock-os/sync-snapshot`, mas `hub.lksnk.dev` não estava servindo esse runtime: retornava `404` em `/health` e no endpoint interno.
2. O deploy inicial via CLI relinkou para o Vercel project acessível `inventory-hub` (`prj_HRmd1pjRnNVQpPzfwDWw2Fb4OgtR`), mas esse project ainda não tinha o domínio `hub.lksnk.dev` nem as envs necessárias de Supabase/Stock OS auth.

## Ações executadas

### Local verification antes do deploy

- `npm ci`
- `npm run build` → passou
- `env -u SUPABASE_LK_URL -u SUPABASE_LK_SERVICE_KEY -u SUPABASE_URL -u SUPABASE_SERVICE_ROLE_KEY -u STOCK_OS_SOURCE npm test` → `176 pass / 0 fail`
- Smoke local governado do client Supabase:
  - `rows=8550`
  - `mr_rows=98`
  - `mr_units=26`

### Deploy Vercel

Projeto Vercel final:

- team: `lk-snkrs-projects`
- project: `inventory-hub`
- project id: `prj_HRmd1pjRnNVQpPzfwDWw2Fb4OgtR`
- deploy production URL: `https://inventory-g7thf1glf-lk-snkrs-projects.vercel.app`
- alias final: `https://hub.lksnk.dev`

Comandos usados via Doppler/broker, sem imprimir secrets:

- `vercel pull --environment=production`
- `vercel build --prod`
- `vercel deploy --prebuilt --prod --yes`

### Env Vercel adicionada

Adicionadas em Production, valores criptografados no Vercel e não impressos:

- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`
- `STOCK_OS_API_BASIC_AUTH_USER`
- `STOCK_OS_API_BASIC_AUTH_PASSWORD`

Env local `.vercel/.env.production.local` foi removido após deploy.

### Domínio Vercel

Adicionado/readback:

```json
{
  "domains": [
    {"name": "hub.lksnk.dev", "verified": true, "projectId": "prj_HRmd1pjRnNVQpPzfwDWw2Fb4OgtR"},
    {"name": "inventory-hub-five-gamma.vercel.app", "verified": true, "projectId": "prj_HRmd1pjRnNVQpPzfwDWw2Fb4OgtR"}
  ],
  "values_printed": false
}
```

## Verificação live

### Public health

`https://hub.lksnk.dev/health`

```json
{
  "ok": true,
  "service": "lk-estoque-web",
  "source": "Stock OS API",
  "hub_shell": "v2",
  "hub_build": "dashboard-4-build"
}
```

### Endpoint interno sem auth

`https://hub.lksnk.dev/api/internal/stock-os/sync-snapshot?q=all&limit=5`

Resultado esperado e confirmado:

```json
{"status":"unauthorized","values_printed":false}
```

### Endpoint interno com auth governada

`https://hub.lksnk.dev/api/internal/stock-os/sync-snapshot?q=all&limit=20000`

Resultado confirmado:

```json
{
  "status": "confirmado",
  "source": "Stock OS DB",
  "current_stage": "inventory_hub_internal_stock_sync_snapshot",
  "rows": 8550,
  "result_count": 8550,
  "total_count": 8550,
  "truncated": false,
  "mr_rows": 98,
  "mr_units": 26.0,
  "u204_qty": 2.0,
  "values_printed": false
}
```

## Verificação cron/sync

Dry-run do sync Supabase depois do deploy:

```json
{
  "status": "dry_run_ok",
  "run_id": "20260626T092006Z",
  "source_rows": 8550,
  "mr530sg": {"rows": 8550, "mr530sg_rows": 98, "mr530sg_positive_units": 26.0},
  "supabase_write": 0,
  "values_printed": false
}
```

Cron `LK Stock OS Supabase read-model sync hourly` executado manualmente após correção:

- `job_id`: `c45da7bb0fcb`
- `last_status`: `ok`

Readback Supabase após cron:

```json
{
  "status": "ok",
  "run_id": "20260626T092006Z",
  "items": 8550,
  "duplicate_business_rows": 0,
  "critical_sentinels": [{"status":"ok","sentinel":"MR530SG","mismatch_count":0,"obsolete_count":0}],
  "supabase_write": 0,
  "values_printed": false
}
```

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Customer/WhatsApp send: 0
- Secrets impressos: 0
- Vercel prod/env/domain writes: executados sob aprovação explícita do Lucas para corrigir/deployar o Hub upstream
- `.vercel/.env.production.local`: removido

## Rollback

Se precisar reverter:

1. Remover `hub.lksnk.dev` do Vercel project `prj_HRmd1pjRnNVQpPzfwDWw2Fb4OgtR` ou reatribuir ao project anterior conhecido.
2. Promover um deployment anterior no Vercel para `hub.lksnk.dev`.
3. Remover as envs adicionadas se o domínio/project for desativado:
   - `SUPABASE_LK_URL`
   - `SUPABASE_LK_SERVICE_KEY`
   - `STOCK_OS_API_BASIC_AUTH_USER`
   - `STOCK_OS_API_BASIC_AUTH_PASSWORD`

## Status final

`hub.lksnk.dev` corrigido. Endpoint/fonte Hub upstream voltou a entregar payload completo e o sentinel MR530SG não falha mais.
