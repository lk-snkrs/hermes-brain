# Approval Packet — Ativar webhook Shopify Sales OS

Data: 2026-06-14T00:18:17Z
Dono: `lk-stock`
Status: **preview preparado; não ativado**

## Pedido

Ativar ingestão incremental de vendas Shopify para o **Shopify Sales OS** local, espelhando o padrão Stock OS/Tiny: Shopify evento → proxy/webhook seguro → normalizador → SQLite local → summary/dashboard.

## O que será ativado somente após aprovação final

- Tópicos Shopify sugeridos V1:
  - `orders/paid`
  - `orders/create`
  - `orders/updated`
- Tópicos V1.1 depois:
  - `refunds/create`
  - `orders/cancelled`
- Rota pública recomendada conforme regra Brain:
  - `https://hermes-webhooks.lucascimino.com/webhooks/lk/shopify-sales-os`
- Upstream interno/local:
  - script normalizador `areas/lk/sub-areas/stock/scripts/shopify_sales_os.py ingest-file`
  - DB `areas/lk/sub-areas/stock/data/shopify_sales_os.db`
  - summary `areas/lk/sub-areas/stock/data/shopify_sales_os_summary.json`

## Segurança obrigatória

- Validar `X-Shopify-Hmac-Sha256` no ingresso público.
- Preservar raw body para HMAC.
- Rejeitar evento sem HMAC válido.
- Idempotência por `topic + event_id/order_id + payload_hash`.
- Não imprimir secrets, payload completo em log público, token ou webhook secret.
- Não fazer write Shopify/Tiny.

## Writes externos previstos

- **Agora:** nenhum. Packet é preview.
- **Na ativação futura:** criar/alterar subscription webhook no Shopify ou configurar rota no proxy público. Isso é write externo e exige aprovação explícita com tópico/rota/rollback.

## Rollback

- Desativar webhook/subscription Shopify.
- Bloquear rota no proxy.
- Manter DB local como histórico read-only; se houver ingestão incorreta, marcar evento como `ignored/failed` e reprocessar fixture/payload localmente.

## Smoke pós-ativação

1. Enviar fixture assinado para rota staging/local.
2. Confirmar HTTP 2xx sem imprimir segredo.
3. Confirmar linha nova em `shopify_sales_event_ledger`.
4. Confirmar `shopify_orders`/`shopify_order_line_items` atualizados.
5. Rodar `export-summary`.
6. Confirmar `/api/vendas/shopify-sales-os` no dashboard.
7. Guardrails: Shopify write `0`, Tiny write `0`, external write runtime `0`, public availability `0`, auto purchase `0`.

## Decisão solicitada

Aprovar ou não, em próxima etapa, a ativação real dos webhooks Shopify nos tópicos listados acima.
