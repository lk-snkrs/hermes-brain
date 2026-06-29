# Restore attempt — Stock OS → Supabase recurring sync — 2026-06-28

## Status

Parcialmente restaurado, mas **bloqueado por autenticação da fonte Stock OS/Hub** antes de qualquer write Supabase.

## O que foi feito

- Backup criado do script anterior `lk_stock_os_supabase_sync.py` em `profiles/lk-stock/backups/stock-os-supabase-sync-restore-*`.
- Script `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py` reescrito para voltar a ter pipeline de write:
  1. buscar payload completo Stock OS (`q=all&limit=20000`);
  2. validar contagem, `truncated=false`, guardrails e MR530SG;
  3. escrever somente `public.lk_stock_snapshots` e `public.lk_stock_items`;
  4. readback + sentinela.
- `--readback-only` preservado para diagnóstico.
- `--dry-run` implementado para validar fonte sem write.

## Verificações executadas

### Py compile + readback Supabase

Comando:

```bash
python3 -m py_compile /opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py
/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py --readback-only --verbose
```

Resultado:

```json
{
  "status": "ok",
  "run_id": "20260626T092006Z",
  "items": 8550,
  "total_count": 8550,
  "result_count": 8550,
  "supabase_write": 0,
  "critical_sentinels": [
    {"status":"ok","sentinel":"MR530SG","mismatch_count":0,"obsolete_count":0}
  ],
  "values_printed": false
}
```

### Dry-run com fonte real Hub

Comando:

```bash
/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py --dry-run --verbose
```

Resultado:

```json
{
  "status": "alert",
  "component": "lk_stock_os_supabase_sync",
  "reason": "RuntimeError",
  "detail": "source_fetch_http_401:Senha obrigatoria",
  "guardrails": {
    "tiny_write": 0,
    "shopify_write": 0,
    "public_availability_promise": 0
  },
  "values_printed": false
}
```

### Dry-run com fixture local sem write

Comando com `--source-file` sintético MR530SG e `--min-rows 6`:

```json
{
  "status":"dry_run_ok",
  "run_id":"20260628T184000Z",
  "source_rows":6,
  "mr530sg":{"rows":6,"mr530sg_rows":6,"mr530sg_positive_units":9.0},
  "supabase_write":0,
  "values_printed":false
}
```

Isso valida o caminho de parsing/validação sem tocar Supabase.

## Bloqueio atual

O Hub `https://hub.lksnk.dev/api/lk-stock/lookup?...` exige senha. No Doppler do perfil `lk-stock` não há:

- `DASHBOARD_PASSWORD`
- `STOCK_OS_API_BASIC_AUTH`
- `STOCK_OS_API_BASIC_AUTH_USER`
- `STOCK_OS_API_BASIC_AUTH_PASSWORD`

O Vercel tem variáveis `STOCK_OS_API_*`, mas elas aparecem como encrypted/sensitive via API e não são recuperáveis como valor pelo agente sem imprimir/copiar segredo. Portanto, o script restaurado não consegue buscar a fonte completa localmente.

## Writes executados

- Supabase write: `0`
- Tiny write: `0`
- Shopify write: `0`
- deploy/VPS/Docker: `0`
- external send: `0`
- secrets printed: `0`

## Próximo passo necessário

Escolher um caminho seguro para a fonte:

1. **Preferido:** adicionar ao Doppler `lc-keys/prd` para perfil `lk-stock` uma credencial de leitura do Hub/Stock OS (`DASHBOARD_PASSWORD` ou `STOCK_OS_API_BASIC_AUTH_USER/PASSWORD`) sem imprimir valores; depois rodar o sync.
2. Alternativa: aprovar auditoria read-only via VPS/stock-api interno para obter o payload sem passar pelo Hub protegido.
3. Alternativa: criar endpoint interno server-side específico para sync com token governado, depois atualizar cron.

Enquanto isso, o cron deixa de ser silent-stale: ele falhará com alerta local se não conseguir a fonte, em vez de dizer OK sobre snapshot antigo.
