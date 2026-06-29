# Audit — LK Shopify webhooks existentes / Stock OS — 2026-06-28

## Veredito

Lucas estava certo: **os webhooks já existem**. O erro anterior foi olhar só o `webhookSubscriptions` do OAuth/app oficial do Shopify CLI e concluir `nodes=[]` como se fosse ausência global.

A auditoria correta mostra:

- **Shopify current CLI app**: não enxerga subscriptions (`nodes=[]`).
- **Admin token/custom app fallback read-only governado**: enxerga subscriptions reais existentes.
- **Hermes local registry**: já tem rotas para `lk-shopify-tiny-stock-sync` e `lk-stock-shopify-sales-os`.
- **Endpoint público `lk-shopify-tiny-stock-sync` funciona** com HMAC Shopify e grava dry-run/ledger sem write externo.

## Fonte / caminho de acesso

| Fonte | Caminho | Resultado |
|---|---|---|
| Broker Shopify | `/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk` | `status=ok`, `method=broker_shopify_store_execute`, `values_printed=false` |
| Shopify official CLI app | `hermes-cli-run --audit-json shopify store execute ... webhookSubscriptions` | `nodes=[]`, audit OK, `values_printed=false` |
| Shopify Admin token/custom-app helper | `/opt/data/scripts/shopify_admin_graphql_cli.py` via Doppler | webhooks reais encontrados, `values_printed=false` |
| Vercel/Hermes endpoint health | `https://hermes-webhooks.lucascimino.com/health` | `{"status":"ok","platform":"webhook"}` |
| Endpoint assinado | `POST /webhooks/lk-shopify-tiny-stock-sync` | paid/cancelled OK dry-run; invalid signature 401 |

## Webhooks Shopify relevantes encontrados

### Fluxo Tiny stock sync — alvo de estoque

| ID | Topic | Endpoint | Status auditado |
|---|---|---|---|
| `gid://shopify/WebhookSubscription/1646886125790` | `ORDERS_PAID` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` | Existe / correto |
| `gid://shopify/WebhookSubscription/1646886158558` | `ORDERS_CANCELLED` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` | Existe / correto |

### Fluxo Sales OS — leitura de vendas / dashboard

| ID | Topic | Endpoint | Status auditado |
|---|---|---|---|
| `gid://shopify/WebhookSubscription/1656034590942` | `ORDERS_CREATE` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` | Existe |
| `gid://shopify/WebhookSubscription/1656034623710` | `ORDERS_PAID` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` | Existe |
| `gid://shopify/WebhookSubscription/1656034656478` | `ORDERS_UPDATED` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` | Existe |
| `gid://shopify/WebhookSubscription/1656034689246` | `ORDERS_CANCELLED` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` | Existe |
| `gid://shopify/WebhookSubscription/1656034722014` | `REFUNDS_CREATE` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` | Existe |

## Rotas Hermes locais relevantes

| Rota | Eventos | Script | Observação |
|---|---|---|---|
| `lk-shopify-tiny-stock-sync` | `orders/paid`, `orders/cancelled` | `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py` | Local dry-run / sem Shopify/Tiny writes |
| `lk-shopify-tiny-stock-sync-dryrun` | `orders/paid`, `orders/cancelled` | `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py` | Rota/legado dry-run |
| `lk-stock-shopify-sales-os` | `orders/create`, `orders/paid`, `orders/updated`, `orders/cancelled`, `refunds/create` | `/opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py` | Sales OS / dashboard |
| `lk-stock-shopify-order-paid` | `orders/paid` | `/opt/data/scripts/lk_stock_gate_b_webhook_ingest.py` | Gate B local |

## Teste assinado do endpoint `lk-shopify-tiny-stock-sync`

Endpoint:

```text
https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync
```

Resultados:

| Topic | Assinatura | HTTP | Resultado seguro |
|---|---:|---:|---|
| `orders/paid` | válida | `200` | `dry_run_recorded`, `processed_count=1`, `would_update_count=0`, `blocked_count=1`, `write_executed=false` |
| `orders/cancelled` | válida | `200` | `dry_run_recorded`, `processed_count=1`, `would_update_count=0`, `blocked_count=1`, `write_executed=false` |
| `orders/paid` | inválida | `401` | rejeitado |

Ledger local:

- Arquivo: `/opt/data/hermes_bruno_ingest/local_sql/lk_shopify_tiny_stock_sync_dryrun/ledger.ndjson`
- Linhas observadas após teste: `63`
- Entradas finais: `orders/paid` e `orders/cancelled` com `status=blocked`, `write_executed=false`.

## Diagnóstico

1. **Não falta webhook Shopify para o fluxo `lk-shopify-tiny-stock-sync`.** Os dois tópicos essenciais existem e apontam para o endpoint canônico.
2. **O endpoint público está operacional e seguro.** HMAC válido aceita; HMAC inválido rejeita; payload fake vira dry-run/ledger bloqueado, sem write.
3. **O `nodes=[]` do official CLI era uma limitação de contexto/app, não ausência real de webhook.** Para auditoria de webhooks existentes, o caminho precisa distinguir app OAuth oficial versus custom app/Admin token.
4. **Não executei correção Shopify porque não havia divergência confirmada no alvo principal.** Criar novo webhook agora causaria duplicata.

## Correções aplicadas nesta rodada

- O approval anterior de “criar 2 webhooks” foi marcado como **SUPERSEDED / não usar para execução**.
- Criado packet substituto com regra correta: `areas/lk/sub-areas/stock/approval-packets/shopify-stock-webhook-audit-correction-20260628.md`.
- Skill do broker já contém a lição: `webhookSubscriptions.nodes=[]` no app atual não equivale a ausência global; reconciliar registry/rotas legadas antes de criar.

## O que NÃO foi feito

- Não criei webhook novo.
- Não atualizei/deletou webhook Shopify.
- Não fiz write em Shopify inventory.
- Não fiz write em Tiny.
- Não mandei WhatsApp/email/Klaviyo/Meta.
- Não imprimi secrets/tokens (`values_printed=false`).

## Próxima decisão recomendada

Como os webhooks de estoque existem e o endpoint está OK, a próxima investigação do problema “estoque real / Inventory Hub não atualiza tudo” deve focar no **downstream**:

1. o script `lk_shopify_tiny_stock_sync_dryrun.py` está só em dry-run/local ledger;
2. verificar se o ledger alimenta Supabase/Stock OS ou se fica isolado;
3. conferir freshness do sync Supabase/Stock OS após eventos reais;
4. se quiser que evento atualize read model real, preparar aprovação separada para promover do dry-run para update local/Supabase, ainda sem Shopify/Tiny writes.
