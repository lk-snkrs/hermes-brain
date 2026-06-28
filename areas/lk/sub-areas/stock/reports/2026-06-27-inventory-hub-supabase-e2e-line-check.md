# Inventory Hub / Supabase — E2E linha final

Data: 2026-06-27
Agente: lk-stock
Escopo: Stock OS, Shopify Sales OS, Compras e dashboard Inventory Hub (`hub.lksnk.dev`) como base confiável Supabase.

## Veredito

**Ainda não posso declarar o Hub público 100% correto em produção**, porque o smoke público mostrou que a aba/API de **Vendas** em `hub.lksnk.dev` ainda está lendo artefatos legados/stale (`source=shopify_sales_os_db`) em vez do novo read model Supabase direto.

O backend Supabase e o código corrigido foram verificados localmente. Falta aprovação/deploy para publicar a correção no Hub público.

## Evidência Supabase — fonte confiável

### Stock OS

- `hub.lksnk.dev/api/estoque/bootstrap?pageSize=2`: `200`
- `total=12592`
- `source=Stock OS API`
- guardrails: `tiny_write=0`, `shopify_write=0`, `public_availability_safe=0`, `availability_claim_allowed=0`

### Sales OS Supabase direto

Teste do loader Supabase no repo `inventory-hub` com Doppler:

- summary source: `supabase_direct_shopify_sales_os`
- generated_at: `2026-06-27T13:55:05.211426Z`
- totals: `orders=2074`, `revenue=6817938.08`, `units=2831`
- search source: `supabase_direct_shopify_sales_os_paid_active_line_items`
- search generated_at: `2026-06-27T13:55:05.245006Z`
- search items: `1709`
- search totals: `products=1709`, `orders=2810`, `units=2831`, `revenue=6668537.22`
- guardrails: `shopify_write=0`, `tiny_write=0`, `external_write=0`, `public_availability_promise=0`, `auto_purchase=0`

### Compras

- `hub.lksnk.dev/compras/api/health`: `200`
- `store=supabase`
- guardrails: `tinyWrite=0`, `shopifyWrite=0`, `compraAutomatica=0`

## Falha encontrada no Hub público

Smoke público atual:

| Endpoint | Status | Fonte atual | Problema |
|---|---:|---|---|
| `/api/vendas/shopify-sales-os` | 200 | `shopify_sales_os_db` | stale/legado |
| `/api/vendas/search?q=nike` | 200 | `shopify_sales_os_db_paid_active_line_items` | stale/legado |

Dados públicos atuais observados:

- `/api/vendas/shopify-sales-os`: `generated_at=2026-06-22T08:50:46.524554Z`, `orders=2026`, `revenue=6673711.38`, `units=3424`
- `/api/vendas/search?q=nike`: `generated_at=2026-06-14T22:15:01.786789Z`, `products=1632`, `revenue=6248684.2`

Isso diverge do Supabase direto atual e prova que o Hub público ainda não está usando a nova base de Vendas como canônica.

## Correção preparada localmente

Arquivos alterados no repo `/opt/data/worktrees/lk-stock/inventory-hub`:

- `src/sales-read-model.js`
  - adicionados loaders async Supabase:
    - `loadShopifySalesOsSummaryAsync()`
    - `loadShopifySalesSearchIndexAsync()`
  - leitura server-side via REST Supabase usando `SUPABASE_LK_URL` + `SUPABASE_LK_SERVICE_KEY`/service role.
  - fallback local preservado apenas quando Supabase não estiver configurado.

- `src/index.js`
  - endpoints de Vendas passam a chamar os loaders Supabase async:
    - `/api/vendas/shopify-sales-os`
    - `/api/vendas/search`
    - `/api/vendas/product-360`
    - `/api/vendas/top-sem-cobertura`
    - `/api/vendas/decision-queues`
    - `/api/vendas/lista-julio`
    - `/api/vendas/saneamento-identidade`
    - `/api/vendas/alerts`
    - `/api/vendas/health`
    - `/api/vendas/executive-summary`

## Verificação local da correção

Com Supabase env via Doppler e app local `PORT=3187`:

| Endpoint local | Resultado |
|---|---|
| `/api/vendas/shopify-sales-os` | `200`, source `supabase_direct_shopify_sales_os`, orders `2074` |
| `/api/vendas/search?q=nike` | `200`, source `supabase_direct_shopify_sales_os_paid_active_line_items`, items `1709` |
| `/api/vendas/health` | `200`, status `ok`, summary age `0.08h`, search items `1709` |
| `/api/vendas/product-360?q=nike` | `200`, source `Shopify Sales OS search index + Stock OS API` |
| `/api/estoque/bootstrap?pageSize=2` | `200`, total `12592` |

Testes:

```text
node --check src/sales-read-model.js && node --check src/index.js && npm test
49 tests
49 pass
0 fail
```

## Guardrails preservados

- Shopify write: `0`
- Tiny write: `0`
- external/customer-facing send: `0`
- public availability promise: `0`
- secrets printed: `false`

## Bloqueio atual

Deploy/produção é write externo/prod. Falta aprovação escopada do Lucas para publicar a correção no `inventory-hub`/`hub.lksnk.dev`.

## Próxima ação recomendada

Aprovar deploy do patch `inventory-hub` para produção, escopo estrito:

- publicar apenas mudanças em `src/sales-read-model.js` e `src/index.js`;
- objetivo: Vendas do Hub ler `lk_shopify_sales_*` Supabase server-side;
- sem Shopify/Tiny write;
- sem alteração de estoque/preço/produto/campanha;
- pós-deploy: smoke público em `/health`, `/api/estoque/bootstrap`, `/api/vendas/shopify-sales-os`, `/api/vendas/search?q=nike`, `/api/vendas/health`, `/compras/api/health`, `/vendas`, `/compras`.
