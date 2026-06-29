# Approval Packet — Restaurar Stock OS → Supabase sync recorrente — 2026-06-28

## Veredito curto

- Tipo de ação: **write controlado em Supabase LK** (`public.lk_stock_snapshots`, `public.lk_stock_items`).
- Motivo: Inventory Hub lê Supabase corretamente, mas o snapshot Supabase está parado em `2026-06-26`; cron atual só valida readback e não publica snapshot novo.
- Risco: A3 database write operacional.
- Escopo: restaurar pipeline de snapshot completo Stock OS/Hub → Supabase. **Sem write Tiny, sem write Shopify, sem contato externo.**

## Evidência do problema

- Webhooks Shopify existem e funcionam.
- `lk_shopify_tiny_stock_sync_dryrun.py` grava local ledger/local SQLite, mas não Supabase.
- Supabase latest:
  - `run_id=20260626T092006Z`
  - `total_count=8550`
  - `imported_at=2026-06-26T17:08:56Z`
- Cron `c45da7bb0fcb` roda OK, mas o script atual `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py` apenas lê/valida `lk_stock_*` e sentinela MR530SG; não faz fetch/upsert.

## Ação proposta

Restaurar comportamento documentado do cron `LK Stock OS Supabase read-model sync hourly`:

1. Fazer backup do script atual e do estado Supabase atual.
2. Buscar fonte Stock OS completa server-side:
   - preferencial: `https://hub.lksnk.dev/api/lk-stock/lookup?q=all&limit=20000` com auth governada;
   - ou adapter/Stock OS interno equivalente se o Hub exigir sessão não disponível.
3. Validar payload antes de qualquer write:
   - `truncated=false`;
   - `result_count == total_count == len(results)`;
   - guardrails `public_availability_safe=0`, `availability_claim_allowed=0`;
   - contagem mínima coerente;
   - sentinela MR530SG ainda presente.
4. Criar `snapshot_run_id` novo.
5. Inserir/upsert `lk_stock_snapshots`.
6. Inserir `lk_stock_items` do novo snapshot.
7. Readback Supabase:
   - latest run_id novo;
   - item count = source count;
   - public/availability sums = 0;
   - MR530SG count/units OK.
8. Verificar Inventory Hub lendo latest Supabase.
9. Registrar receipt.

## Rollback

- Como não vamos apagar snapshot antigo, rollback primário é voltar o latest usado pelo Hub removendo/arquivando o snapshot novo se ele falhar validação pós-write.
- Antes de qualquer delete de snapshot novo, salvar IDs/counts e readback.
- Reverter script para backup se o cron falhar.
- Tiny/Shopify permanecem intocados.

## Não aprovado neste packet

- write Tiny;
- write Shopify inventory/produto/webhook;
- mutation de schema/migration Supabase;
- envio WhatsApp/email/Klaviyo/Meta;
- criação de cron novo;
- deploy Vercel/VPS/Docker;
- usar dado de fixture/teste como operacional.

## Texto de aprovação

> Aprovo restaurar o sync recorrente Stock OS → Supabase para o Inventory Hub: editar o script `lk_stock_os_supabase_sync.py`, com backup, para buscar snapshot completo Stock OS/Hub, validar contagens/guardrails/MR530SG, escrever somente em `public.lk_stock_snapshots` e `public.lk_stock_items`, fazer readback e rollback se falhar. Não aprovo write Tiny, write Shopify, schema/migration, deploy, envio externo ou criação de cron novo.
