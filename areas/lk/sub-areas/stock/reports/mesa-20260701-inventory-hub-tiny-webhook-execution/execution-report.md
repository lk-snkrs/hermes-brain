# Mesa 2026-07-01 — LK Stock Inventory Hub + Tiny/Olist webhook execution

- timestamp: 2026-07-01T10:32:28Z
- owner: `lk-stock`
- approval: Lucas pediu `Corrigir ambos`
- values_printed: false
- external_writes: 0
- docker_redeploy_executed: false
- tiny_write: 0
- shopify_write: 0
- supabase_write: 0

## Resultado executivo

Ambos os pontos foram fechados com readback:

1. **Inventory Hub stale** — não exigiu redeploy/container restart porque o runtime vivo já estava atualizado. O container `lk-estoque-web` roda a imagem `lk-estoque-web-web:20260630T105802Z` e as rotas que antes faltavam já existem e respondem JSON.
2. **Tiny/Olist webhook 401** — reconciliado por assinatura correta do proxy público. O erro `401 invalid_generic_signature` ocorria quando o probe usava assinatura Hermes/local; o proxy público Tiny/Olist espera assinatura provider-specific com `LK_STOCK_TINY_WEBHOOK_SECRET` em `x-webhook-signature`. Probe público passou.
3. **Achado adjacente corrigido** — duas rotas LK Stock Shopify Gate B falhavam `script_failed` porque faltavam módulos no Brain ativo. Foram restaurados `stock_event_normalizer.py` e `stock_webhook_ingest.py` do backup Brain, com backup/manifest, e o certificador público completo passou em 14/14 rotas.

## Evidência Inventory Hub

| Probe | Resultado |
|---|---|
| `/health` | HTTP 200 JSON, `hub_shell=v2`, `hub_build=dashboard-4-build` |
| `/api/vendas/shopify-sales-os` | HTTP 200 JSON, `source=supabase_direct_shopify_sales_os`, `generated_at=2026-07-01T05:44:35.942274Z` |
| `/api/lk-stock/lookup?q=MR530SG&limit=20` | HTTP 200 JSON, `source=Stock OS DB`, `result_count=8` |
| `/api/stock-cockpit/v2/health` | HTTP 200 JSON, `source=Stock OS API`, `totalRows=8550`, `status=attention` |

Conclusão: o packet stale ficou **superseded por estado vivo atualizado**; não houve Docker/container restart.

## Evidência Tiny/Olist

| Rota | Local gateway | Público `hermes-webhooks` | Writes |
|---|---:|---:|---:|
| `lk-stock-tiny-stock-snapshot` | 200 processed | 200 processed | 0 |
| `lk-stock-tiny-stock` | 200 processed | 200 processed | 0 |
| `lk-stock-tiny-events` | 200 ignored/unknown no-op | 200 ignored/unknown no-op | 0 |

## Certificação pública completa

- status: `pass`
- route_count: `14`
- pass_count: `14`
- attention_count: `0`
- external_writes: `0`

## Arquivos alterados

- Restaurados no Brain ativo:
  - `areas/lk/sub-areas/stock/scripts/stock_event_normalizer.py`
  - `areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py`
- Backup/manifest:
  - `areas/lk/sub-areas/stock/backups/webhook-script-modules-restore-20260701T103029Z/manifest.json`
- Referência operacional atualizada:
  - `/opt/data/profiles/lk-stock/skills/productivity/lk-inventory-hub/references/inventory-hub-docker-runtime-webhook-repair-20260630.md`

## Rollback

- Inventory Hub: nenhum redeploy foi feito; rollback não aplicável.
- Módulos Gate B: remover os dois módulos restaurados do Brain ativo ou restaurar a partir do backup/manifest citado, se houver regressão.
- Webhook secret: nenhum valor foi alterado. A correção foi operacional: usar o secret provider-specific correto no probe público.

## Guardrails preservados

- Sem Tiny write.
- Sem Shopify write.
- Sem Supabase write/migration.
- Sem Docker/VPS/Traefik restart.
- Sem gateway restart.
- Sem impressão de tokens/secrets/signatures.


## Verificação final

- `hermes_webhooks_14_route_certification`: `status=pass`, `route_count=14`, `pass_count=14`, `attention_count=0`, `external_writes=0`.
- `brain_health_check.py`: `All checks passed`.
- JSON parse dos artefatos: OK.
- Secret scan focado: `files_checked=9`, `possible_credential_value_hits=0`, `values_printed=false`.
