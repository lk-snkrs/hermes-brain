# Follow-up — Stock OS Supabase sync source auth and source-quality gate — 2026-06-28

## Status

A credencial de leitura Stock OS foi desbloqueada no Doppler, mas a fonte disponível por Vercel/VPS ainda **não é segura para promover ao Supabase**.

## Ações executadas

1. Copiei do Vercel `inventory-hub` para Doppler `lc-keys/prd` os nomes:
   - `STOCK_OS_API_BASE_URL`
   - `STOCK_OS_API_BASIC_AUTH_USER`
   - `STOCK_OS_API_BASIC_AUTH_PASSWORD`
2. Atualizei `/opt/data/scripts/hermes_doppler.py` para injetar esses nomes no profile `lk-stock`.
3. Atualizei `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py` para usar `--profile lk-stock` no helper Doppler.
4. Testei fonte protegida via Basic Auth com `values_printed=false`.

## Resultado

A fonte protegida responde, mas o endpoint JSON seguro de lookup não está disponível como JSON:

- `/health`: HTTP 200
- `/api/lk-stock/lookup?q=all&limit=5`: HTTP 200, mas retorna HTML do dashboard, não JSON
- `/api/estoque`: HTTP 200 JSON, mas é o payload de dashboard com `produtos`

## Bloqueio de qualidade

Ao normalizar `/api/estoque` para payload de sync, o gate MR530SG bloqueou:

```json
{
  "status": "alert",
  "reason": "RuntimeError",
  "detail": "source_mr530sg_sentinel_failed:rows=138:units=0",
  "values_printed": false
}
```

Amostra da fonte mostra muitos modelos 530 com `estoque=0`; isso contradiz o Supabase/Hub anterior onde MR530SG tinha unidades positivas. Portanto **não escrevi Supabase**.

## Writes executados

- Doppler secret write: nomes Stock OS copiados de Vercel para `lc-keys/prd`, sem imprimir valores.
- Script local: atualizado.
- Supabase write: `0`.
- Tiny write: `0`.
- Shopify write: `0`.
- Deploy/Vercel: `0`.

## Próxima decisão

A correção correta agora é publicar/ativar um endpoint interno protegido que retorne o mesmo contrato de `/api/lk-stock/lookup` como JSON, mas usando a fonte certa e passando a sentinela MR530SG antes do Supabase write.

Isso exige escopo novo porque envolve deploy/Vercel ou alteração de superfície de produção.
