# Rotina — Supabase Audit Read-only

Objetivo: auditar dados Supabase de LK, Zipper e SPITI com consultas seguras, separando bases e evitando escrita acidental.

## Integração

- Doc: `empresa/integracoes/supabase.md`.
- LK: `SUPABASE_LK_URL`, `SUPABASE_LK_SERVICE_KEY`.
- Zipper Vendas: `SUPABASE_ZIPPER_VENDAS_URL`, `SUPABASE_ZIPPER_VENDAS_SERVICE_KEY`.
- SPITI/Zipper CRM: `SUPABASE_SPITI_URL`, `SUPABASE_SPITI_SERVICE_KEY`.

## Permissões

- Read-only: SELECT, contagens, amostras limitadas, schema introspection.
- Write: INSERT/UPDATE interno exige objetivo claro e aprovação quando afetar operação real.
- External-send: não aplicável diretamente, mas outputs usados em contato externo exigem preview.
- Admin/destructive: SQL DDL, RLS, keys, roles, deletes, truncates, backups/restores exigem aprovação explícita + rollback.

## Regras críticas

- Nunca misturar Zipper Vendas (`vendas_tango`) com SPITI/Zipper CRM.
- Para SPITI, email segue fonte de verdade para totais de lance quando houver divergência.
- Preferir LIMIT em exploração inicial.
- Nunca imprimir service keys.

## Procedimento

1. Confirmar existência dos secrets relevantes via Doppler.
2. Escolher base correta antes de consultar.
3. Rodar consulta read-only e limitada.
4. Registrar fonte, tabela e timestamp da consulta.
5. Se precisar escrever, parar e preparar plano/aprovação.
