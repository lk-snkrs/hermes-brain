# Rotina — Sync Log LK

## O que roda

Registro de início/fim dos scripts de sincronização LK para auditoria operacional.

Script relacionado:

- `scripts/sync_log.py`

## Quando usar

No começo e no fim de cada script de sync LK.

Exemplo:

```bash
doppler run --project lc-keys --config prd -- python3 scripts/sync_log.py start lk_shopify_sync "syncing orders"
doppler run --project lc-keys --config prd -- python3 scripts/sync_log.py end lk_shopify_sync "orders synced"
```

## Ferramentas e dados

- Supabase LK `cnjimxglpktznenpbail`.
- Tabela `lk_intel.sync_log`.

## Credenciais

Buscar em Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ACCESS_TOKEN` ou `SUPABASE_MANAGEMENT_TOKEN`.

## Verificação

1. Confirmar inserção do evento `start`.
2. Confirmar inserção do evento `end`.
3. Em falha, registrar erro e não afirmar sync concluído sem evidência.
