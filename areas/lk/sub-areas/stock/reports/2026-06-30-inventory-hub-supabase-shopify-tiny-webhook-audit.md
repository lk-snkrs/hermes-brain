# Auditoria — Inventory Hub / Supabase / Shopify / Tiny / Webhooks

Data UTC: 2026-06-30
Agente: `lk-stock`
Escopo: read-only/local audit + probes no-op de webhook; sem Tiny write, sem Shopify mutation, sem deploy, sem restart.

## Veredito executivo

1. **Supabase read models estão gravando dados e estão protegidos no escopo auditado.**
   - `public.lk_stock_*` e `public.lk_shopify_sales_*` têm RLS ligado e `anon/authenticated grants = 0`.
   - Stock read model: latest snapshot com `8550` linhas, `duplicate_business_rows=0`, `public_safe_sum=0`, `availability_claim_sum=0`.
   - Sales OS: `2421` orders, `3518` line_items, `2838` paid_enriched, `1719` search_items, `2421` event ledger rows.

2. **Caminho de gravação está claro, mas existem dois mundos convivendo:**
   - Estoque/Tiny: Stock OS/Hub snapshot -> `lk_stock_os_supabase_sync.py` -> Supabase `lk_stock_snapshots` + `lk_stock_items`.
   - Vendas Shopify: `lk_shopify_sales_os_supabase_direct.py` -> Supabase `lk_shopify_sales_*` + JSON artifacts.
   - Porém o container `lk-estoque-web` em produção local está com código mais antigo do que o repo `inventory-hub`: não contém `/api/lk-stock/lookup` nem `/api/stock-cockpit/v2/*` no `/app/src/index.js`.

3. **Inventory Hub em produção não está lendo tudo do Supabase novo.**
   - `/api/vendas/shopify-sales-os` no container responde `source=shopify_sales_os_db`, `generated_at=2026-06-22T08:50:46.524554Z`, assinatura legada/stale.
   - O repo atual tem loader Supabase-first para vendas e lookup Supabase para estoque, mas essa versão não está refletida no container `lk-estoque-web`.
   - Portanto: Supabase está atualizado, mas o Hub/produção ainda pode exibir dados/rotas antigas.

4. **Webhooks Shopify -> Hermes -> dry-run Tiny estão funcionando para a rota principal, mas ainda em modo dry-run.**
   - `hermes-webhooks` custom domain health: `200 {status: ok, platform: webhook}`.
   - Hermes central webhook platform ativo em `HERMES_HOME=/opt/data` com rotas `lk-shopify-tiny-stock-sync`, `lk-stock-*`, `lk-stock-tiny-*` etc.
   - Probe signed no-op `lk-shopify-tiny-stock-sync`: HTTP `200`, `status=ignored`, `reason=order_not_paid`, `transport=hermes_run_script`, `write_executed=false`.
   - Ledger real dry-run tem 84 linhas; última linha auditada em `2026-06-30T10:20:53Z` para pedido `#147976`, status `blocked`, `block_reason=tiny_no_match`.
   - Logs recentes mostram POST reais Shopify para `lk-shopify-tiny-stock-sync` com HTTP `200`.

5. **Assinaturas Shopify visíveis via OAuth oficial atual retornaram `nodes=[]`.**
   - Isso significa “nenhuma subscription visível para esse app/contexto OAuth”, não prova ausência global de webhooks na loja.
   - Como há POSTs reais `Shopify-Captain-Hook` chegando ao Hermes, existe algum upstream ativo fora da visibilidade desse OAuth/app atual.

6. **Tiny webhook route não está comprovada end-to-end.**
   - Rota local existe (`lk-stock-tiny-stock-snapshot`), proxy aceita lógica para Tiny, mas probe no-op assinado com segredo disponível retornou HTTP `401`.
   - Conclusão: Shopify webhook principal funciona; Tiny/Olist webhook route precisa reconciliação de segredo/upstream antes de ser chamado de funcionando.

## Evidência resumida

### Supabase Stock OS

```json
{
  "stock_latest": {
    "run_id": "20260626T092006Z",
    "source": "Stock OS DB",
    "status": "confirmado",
    "truncated": false,
    "imported_at": "2026-06-30T10:20:27.588138+00:00",
    "total_count": 8550,
    "result_count": 8550,
    "source_observed_at": "2026-06-26T09:20:06+00:00"
  },
  "stock_items": {
    "rows": 8550,
    "distinct_business_rows": 8550,
    "negative_raw_rows": 0,
    "missing_sku_rows": 0,
    "public_safe_sum": 0,
    "availability_claim_sum": 0
  }
}
```

### Supabase Shopify Sales OS

```json
{
  "sales_counts": {
    "snapshots": 1,
    "orders": 2421,
    "line_items": 3518,
    "paid_enriched": 2838,
    "dimensions": 1961,
    "metadata": 823,
    "search_items": 1719,
    "events": 2421
  },
  "sales_latest": {
    "run_id": "20260630T102309",
    "source": "supabase_direct_shopify_sales_os",
    "generated_at": "2026-06-30T10:23:09.195211Z",
    "synced_at": "2026-06-30T10:23:10.328532+00:00"
  }
}
```

### Security/grants

- Tabelas `lk_stock_*` e `lk_shopify_sales_*`: RLS `true`.
- Grants para `anon`/`authenticated`: `0` em todas as tabelas do escopo auditado.

### Inventory Hub production/container

- `docker ps`: `lk-estoque-web` up, `lk-estoque-stock-api` healthy.
- `docker exec lk-estoque-web grep /app/src/index.js`:
  - contém `/api/vendas/shopify-sales-os`.
  - não contém `/api/lk-stock/lookup` nem `/api/stock-cockpit/v2`.
- API local container:
  - `/api/vendas/shopify-sales-os`: HTTP 200, `source=shopify_sales_os_db`, `generated_at=2026-06-22T08:50:46.524554Z`.
  - `/api/lk-stock/lookup?q=MR530SG&limit=20`: retorna HTML SPA, não JSON de API, porque rota não existe no código containerizado atual.
  - `/api/stock-cockpit/v2/health`: retorna HTML SPA, não JSON de API.

### Webhooks

- Central Hermes routes: `14 webhook subscription(s)` em `HERMES_HOME=/opt/data`.
- `hermes-webhooks` health: `https://hermes-webhooks.lucascimino.com/health` -> HTTP 200.
- Shopify official Admin readback: `webhookSubscriptions.nodes=[]` no app/contexto atual.
- Rota `lk-shopify-tiny-stock-sync` signed no-op: HTTP 200, ignored/no write.
- Rota `lk-stock-tiny-stock-snapshot` signed no-op: HTTP 401.
- Ledger dry-run: `/opt/data/hermes_bruno_ingest/local_sql/lk_shopify_tiny_stock_sync_dryrun/ledger.ndjson`, `84` linhas.

## Como os dados são salvos hoje

### Estoque / Tiny

1. Tiny continua sendo fonte viva de estoque.
2. O Stock OS/Hub fornece snapshot protegido por `/api/internal/stock-os/sync-snapshot`.
3. Cron `c45da7bb0fcb` roda `lk_stock_os_supabase_sync.py`.
4. Script valida payload, guardrails, sentinel MR530SG e dupes.
5. Escreve somente:
   - `public.lk_stock_snapshots`
   - `public.lk_stock_items`
6. Readback exige contagens iguais, sem truncamento, sem duplicate business rows, sem public availability flags.

### Vendas / Shopify

1. Cron `2fd03de2c8b8` roda `lk_shopify_sales_os_nightly_reconcile.py`.
2. Wrapper chama `lk_shopify_sales_os_supabase_direct.py`.
3. Shopify Admin GraphQL é tentado via broker/CLI oficial; fallback read-only token existe só para continuidade quando CLI OAuth não tem escopo de orders.
4. Escreve read-model Supabase:
   - `lk_shopify_sales_snapshots`
   - `lk_shopify_sales_orders`
   - `lk_shopify_sales_order_line_items`
   - `lk_shopify_sales_paid_line_items_enriched`
   - `lk_shopify_sales_product_dimensions`
   - `lk_shopify_sales_product_metadata`
   - `lk_shopify_sales_search_items`
   - `lk_shopify_sales_event_ledger`
5. Também gera JSON artifacts usados pelo dashboard/container.

## Como o Inventory Hub lê hoje

### No repo atual

- `src/stock-os.js`: Supabase service-role REST, snapshot latest, filtra query depois de buscar snapshot completo para buscas específicas.
- `src/sales-read-model.js`: tem `loadSalesReadModelAsync` Supabase-first, e fallback para JSON/local quando Supabase indisponível.
- `src/index.js`: expõe `/api/lk-stock/lookup`, `/api/stock-cockpit/v2/*`, `/api/vendas/shopify-sales-os`, `/api/vendas/search`, `/api/vendas/time-summary`.

### No container de produção auditado

- Código containerizado está defasado.
- Isso explica risco de o Hub estar mostrando:
  - Sales OS antigo (`shopify_sales_os_db`, 2026-06-22).
  - Ausência das rotas API novas de estoque/cockpit.

## Riscos / blockers

1. **Maior risco:** Supabase está bom, mas Hub em produção não está necessariamente consumindo o read model novo.
2. **Webhook Shopify funciona, mas não atualiza estoque em tempo real no Supabase/Shopify:** ainda é dry-run/local ledger e `write_executed=false`.
3. **Shopify webhook subscriptions invisíveis no OAuth oficial atual:** precisa reconciliação com app/legado antes de criar/alterar qualquer subscription para evitar duplicidade.
4. **Tiny webhook route 401:** provável desalinhamento de secret/proxy/upstream; não chamar de ativo.
5. **Hub public auth/env drift:** credenciais Doppler do profile não autenticaram `hub.lksnk.dev`; o container local tinha `DASHBOARD_PASSWORD` presente, mas domínio público retornou 401 para tentativas governadas. Precisa reconciliar env de runtime/Vercel/Traefik/Hostinger antes de depender de smoke público autenticado.

## Próximos passos recomendados

1. **Corrigir/deployar Inventory Hub para a versão Supabase-first atual** no runtime que serve `hub.lksnk.dev`/`lk-estoque-web`, com backup/rollback e aprovação escopada porque envolve produção/container/deploy.
2. **Após deploy**, verificar:
   - `/api/lk-stock/lookup?q=MR530SG&limit=20` retorna JSON e grade correta.
   - `/api/stock-cockpit/v2/health` retorna JSON.
   - `/api/vendas/shopify-sales-os` retorna `source=supabase_direct_shopify_sales_os` ou equivalente atual, não `shopify_sales_os_db`.
3. **Reconciliar Shopify webhook registry**: app atual vê `nodes=[]`, mas logs mostram webhooks reais chegando. Não criar duplicado antes de identificar app/subscription/legacy source.
4. **Reconciliar Tiny/Olist webhook secret/upstream** para `lk-stock-tiny-stock-snapshot` e refazer signed no-op até HTTP 200.
5. **Decidir se real-time stock sync avança de dry-run para write governado**. Hoje a automação lê Tiny e propõe set absoluto de estoque, mas não escreve Shopify/Tiny/Supabase real-time sem aprovação.

## Guardrails preservados

- Shopify mutation: 0.
- Tiny write: 0.
- Supabase write novo nesta auditoria: 0.
- Deploy/restart/container mutation: 0.
- Customer-facing send: 0.
- Secrets/tokens impressos: 0 (`values_printed=false`).
