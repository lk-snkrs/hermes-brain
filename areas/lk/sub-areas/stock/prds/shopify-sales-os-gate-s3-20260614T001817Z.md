# Shopify Sales OS — Gate S3 DB local + backfill + webhook approval packet

Data: 2026-06-14T00:18:17Z
Perfil dono: `lk-stock`
Status: implementação autorizada por Lucas para Gate S3, com ativação real de webhook condicionada a approval packet.

## Objetivo

Replicar para vendas Shopify o padrão do Stock OS/Tiny:

1. **Database local SQLite** como caminho quente para consultas e analytics.
2. **Backfill read-only Shopify Orders** para reconstruir histórico.
3. **Sync incremental/webhook** por eventos Shopify (`orders/paid`, `orders/create`, `orders/updated`, `refunds/create` em fases).
4. **Dashboard/API** lendo a DB local em vez de relatórios soltos.
5. **Approval packet** para ativação do webhook no Shopify/proxy público, sem ativar write externo sem aceite final.

## Guardrails

- Shopify write: `0` durante backfill/ingest local.
- Tiny write: `0`.
- External write: `0`, exceto eventual ativação futura de webhook depois de aprovação escopada.
- Public availability promise: `0`.
- Auto purchase: `0`.
- DB local não substitui fonte Shopify para auditoria financeira; é read model operacional.

## Schema V1

Tabelas:

- `shopify_orders`: pedido normalizado, status, valores, origem/canal, timestamps e payload bruto.
- `shopify_order_line_items`: item/sku/variant/produto/quantidade/receita estimada.
- `shopify_sales_event_ledger`: idempotência de webhook/backfill por topic/event/hash.
- `shopify_sales_sync_state`: checkpoints de backfill/sync.

## Runtime V1

Script canônico:

`areas/lk/sub-areas/stock/scripts/shopify_sales_os.py`

Comandos:

```bash
python3 areas/lk/sub-areas/stock/scripts/shopify_sales_os.py init-db
python3 areas/lk/sub-areas/stock/scripts/shopify_sales_os.py ingest-file --payload areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json --topic orders/paid
python3 areas/lk/sub-areas/stock/scripts/shopify_sales_os.py export-summary
python3 areas/lk/sub-areas/stock/scripts/shopify_sales_os.py backfill --since 2026-01-01 --limit 250
```

## Backfill

- Usa Shopify Admin GraphQL read-only.
- Paginação por `orders(first: 50, after, query: created_at:>=...)`.
- Commit idempotente por `topic + event_id + payload_hash`.
- Checkpoint em `shopify_sales_sync_state.last_backfill`.

## Webhook

- Ingest local verifica HMAC quando `SHOPIFY_WEBHOOK_SECRET`/header forem fornecidos.
- Payload é normalizado e gravado localmente.
- Ativação no Shopify/proxy público exige approval packet com rota, tópico, segredo, rollback e smoke.

## Dashboard/API

- Endpoint alvo: `/api/vendas/shopify-sales-os`.
- Aba Vendas deve mostrar status da DB local, freshness, total de pedidos/unidades/receita, canais e top produtos.
- Analytics atual pode continuar como fallback enquanto o backfill completa.

## Critério de aceite

- Testes offline com fixture passam.
- Backfill read-only real roda com `values_printed=false` e sem segredo impresso.
- Summary local é exportado para JSON consumível pelo dashboard.
- API/dashboard leem o summary local.
- Approval packet criado; webhook real não ativado sem aprovação final.
