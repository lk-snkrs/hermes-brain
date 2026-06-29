# Approval Packet — LK Shopify stock webhooks audit/correction, no duplicates — 2026-06-28

## 1. Veredito curto

- Tipo de ação: **auditar e corrigir webhooks existentes**, não criar novo fluxo paralelo.
- Alvo exato: Shopify LK `lk-sneakerss.myshopify.com` + rotas Hermes/Vercel já existentes para estoque.
- Risco: **A3 se houver update/create/delete em Shopify webhookSubscriptions**; **A1/A2 local** para auditoria/relatório/testes dry-run.
- Status recomendado: **não duplicar**. Primeiro descobrir/validar o que já existe; depois corrigir somente endpoint/tópico/assinatura se estiver divergente.

## 2. Fonte viva e evidências

Evidência coletada em 2026-06-28:

1. **Broker Shopify OK**
   - `/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk`
   - Resultado: `status=ok`, `method=broker_shopify_store_execute`, `rc=0`, `values_printed=false`.

2. **Shopify Admin GraphQL read-only OK**
   - Loja: `LK`, domínio `lk-sneakerss.myshopify.com`.
   - Audit: `exit_code=0`, `mode=read_only`, `values_printed=false`.

3. **Readback Shopify via app/auth atual**
   - `webhookSubscriptions(first:100)` retornou `nodes=[]`.
   - Interpretação: o app/auth atual não enxerga subscriptions registradas para ele. Isso **não prova** que não exista webhook em outro app/legado; por isso a ação correta não é criar às cegas.

4. **Registro Hermes local confirma rotas existentes**
   - `lk-shopify-tiny-stock-sync`
     - eventos: `orders/paid`, `orders/cancelled`
     - script: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
     - descrição: Shopify paid/cancelled → Tiny official stock dry-run/local refresh; sem Shopify/Tiny writes.
   - `lk-shopify-tiny-stock-sync-dryrun`
     - eventos: `orders/paid`, `orders/cancelled`
     - script: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
   - `lk-stock-shopify-sales-os`
     - eventos: `orders/create`, `orders/paid`, `orders/updated`, `orders/cancelled`, `refunds/create`
     - script: `/opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py`
   - `lk-stock-shopify-order-paid`
     - evento: `orders/paid`
     - script: `/opt/data/scripts/lk_stock_gate_b_webhook_ingest.py`

5. **Teste público assinado do endpoint existente**
   - Endpoint testado: `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`
   - Payload: pedido fake `#HERMES-AUDIT-DRYRUN-20260628`, SKU inexistente de auditoria.
   - Assinatura: `X-Shopify-Hmac-Sha256`, secret via Doppler dentro do processo; nenhum valor impresso.
   - Resultado: HTTP `200`, `status=dry_run_recorded`, `event=orders/paid`, `processed_count=1`, `would_update_count=0`, `blocked_count=1`, `write_executed=false`, `values_printed=false`.
   - Ledger local existe e recebeu entrada bloqueada segura; total observado: 61 linhas.

## 3. Diagnóstico

O erro do approval anterior foi assumir “criar 2 webhooks novos”. A evidência correta mostra:

- **Hermes já tem rotas locais existentes** para o fluxo Shopify→Stock/Tiny.
- **Endpoint público de `lk-shopify-tiny-stock-sync` funciona** com HMAC Shopify e grava dry-run/ledger sem write externo.
- **Shopify Admin GraphQL no app/auth atual retorna zero subscriptions**, então falta reconciliar a camada Shopify Admin: pode estar ausente no app atual, em outro app/legado, ou registrada fora da visibilidade do OAuth atual.

Portanto, o caminho seguro é **auditar e corrigir subscriptions existentes/esperadas**, evitando duplicata.

## 4. Alteração proposta

### Fase 1 — auditoria/correção read-only/local permitida

Executar sem Shopify write:

1. Snapshot atual do Shopify Admin GraphQL `webhookSubscriptions(first:100)`.
2. Snapshot sanitizado do registry Hermes local para rotas Shopify/stock.
3. Teste assinado de `orders/paid` e `orders/cancelled` no endpoint existente, usando payload fake e SKU inexistente.
4. Verificar que scripts downstream mantêm `write_executed=false` e não enviam mensagem externa.
5. Produzir relatório com matriz:
   - tópico esperado;
   - endpoint esperado;
   - existe no Hermes local?;
   - existe no Shopify current app?;
   - POST assinado OK?;
   - ledger OK?;
   - correção necessária.

### Fase 2 — correção Shopify, somente se necessária e aprovada

Se a auditoria confirmar que o webhook Shopify atual está ausente/divergente para o app/auth governado, corrigir **sem duplicar**:

- Se existir subscription com mesmo tópico mas endpoint errado: usar `webhookSubscriptionUpdate` no ID existente.
- Se existir subscription duplicada: preparar lista de IDs duplicados e pedir aprovação específica para deletar duplicatas.
- Se não existir subscription visível no app/auth atual: criar apenas a subscription faltante, depois readback.

Tópicos/endpoint alvo para este fluxo específico:

| Tópico Shopify | Endpoint canônico |
|---|---|
| `ORDERS_PAID` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` |
| `ORDERS_CANCELLED` | `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync` |

## 5. Padrão canônico aplicado

- `hermes-central-integration-auth-broker`: Shopify CLI oficial via broker; sem OAuth direto por agente.
- `lk-shopify-readonly`: readback antes de qualquer Shopify mutation; webhook write só com approval e rollback.
- `lk-stock`: Tiny/Stock OS é fonte de verdade; Shopify é gatilho; dry-run/local ledger antes de mirror.
- Regra de Lucas neste turno: **webhooks já existem; auditar/corrigir, não criar novo**.

## 6. Readback e verificação esperados

Antes de qualquer write Shopify:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
```

Readback Shopify:

```graphql
query WebhooksReadback {
  webhookSubscriptions(first: 100) {
    nodes {
      id
      topic
      format
      endpoint { __typename ... on WebhookHttpEndpoint { callbackUrl } }
    }
  }
}
```

Condição de sucesso da correção:

- nenhum webhook duplicado no mesmo tópico/endpoint;
- `ORDERS_PAID` e `ORDERS_CANCELLED` apontam para o endpoint canônico quando essa for a camada escolhida;
- POST assinado nos tópicos aprovados retorna 2xx/202 e gera ledger dry-run;
- inválido/sem assinatura é rejeitado;
- `write_executed=false`, `tiny_write=false`, `shopify_inventory_write=false`, `external_send=false`.

## 7. Rollback

- Para update: reverter para os valores de endpoint/formato do snapshot antes.
- Para create: deletar exatamente o ID criado.
- Para delete de duplicata: recriar somente se necessário usando snapshot antes.
- Pausar rota Hermes/Vercel se houver risco operacional.
- Tiny e estoque Shopify permanecem intocados nesta fase.

## 8. O que NÃO está aprovado

- Criar webhooks duplicados sem tentar reconciliar existentes.
- Write de estoque Shopify.
- Write em Tiny.
- Produto/SKU/preço/tema/campanha/Klaviyo/WhatsApp/email.
- Outros tópicos além dos explicitamente auditados/aprovados.
- Reauth/OAuth manual fora do central integration auth broker.

## 9. Texto de aprovação para Telegram

> Aprovo auditar e corrigir os webhooks Shopify existentes da LK, sem criar duplicata: usar Hermes Central Integration Auth Broker para readback, comparar com as rotas Hermes já existentes, testar POST assinado em dry-run/local ledger, e só se houver divergência atualizar o webhook existente ou criar apenas o tópico faltante `ORDERS_PAID`/`ORDERS_CANCELLED` para `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`, com snapshot antes, readback depois, receipt e rollback por update reverso/delete do ID criado. Não aprovo write de estoque Shopify, write Tiny, produto/preço/tema/campanha/cliente/fornecedor nem webhooks duplicados.
