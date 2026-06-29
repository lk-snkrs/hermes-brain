# Approval Packet — LK Shopify stock webhooks → Tiny stock truth dry-run — 2026-06-28

> **SUPERSEDED / não usar para execução.** Lucas corrigiu que os webhooks já existem e que a ação correta é auditar/corrigir, não criar novo. Usar o packet substituto: `areas/lk/sub-areas/stock/approval-packets/shopify-stock-webhook-audit-correction-20260628.md`.

## 1. Veredito curto

- Tipo de ação: **write Shopify Admin controlado** para criar/ativar webhook subscriptions.
- Alvo exato: loja `lk-sneakerss.myshopify.com`, eventos `ORDERS_PAID` e `ORDERS_CANCELLED`.
- Endpoint proposto: `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`.
- Risco: **A3 write externo** (criação de webhook Shopify) + execução operacional de evento real em dry-run/local ledger.
- Status recomendado: **ativar somente dry-run/sem write de estoque**, com readback e teste assinado.

## 2. Fonte viva e evidências

- Shopify read-only consultado em 2026-06-28 via Hermes Central Integration Auth Broker:
  - `hermes-cli-integrations smoke shopify_lk`: `status=ok`, `method=broker_shopify_store_execute`, `rc=0`, `values_printed=false`.
  - `shop { name myshopifyDomain }`: `LK`, `lk-sneakerss.myshopify.com`, audit `exit_code=0`, `mode=read_only`, `values_printed=false`.
  - `webhookSubscriptions(first:100)`: `nodes=[]`.
- Contexto Stock OS/Inventory Hub:
  - auditoria anterior confirmou Supabase/Hub lendo snapshot, mas não real-time;
  - webhooks oficiais Shopify não estavam registrados no app/auth atual;
  - Tiny continua fonte de verdade de estoque; Shopify é gatilho.
- Lacunas/incertezas:
  - é necessário confirmar no momento da execução se o endpoint Vercel/Hermes responde a POST assinado antes de criar/considerar ativo;
  - readback Shopify retornou zero webhooks para o app/auth atual, mas não prova inexistência em outros apps legados fora deste auth.

## 3. Snapshot antes

- Estado Shopify webhooks antes: `webhookSubscriptions.nodes=[]` via Admin GraphQL read-only no app/auth atual.
- IDs/handles/variant IDs envolvidos: nenhum produto/variant específico; escopo por evento de pedido.
- Backup/rollback path previsto:
  - salvar JSON do readback antes em `areas/lk/sub-areas/stock/reports/shopify-stock-webhooks-before-20260628.json`;
  - salvar IDs dos webhooks criados em relatório/receipt;
  - rollback é deletar exatamente os webhook subscription IDs criados neste pacote.
- Hash/contagem/estado antes: contagem antes `0` webhooks retornados.

## 4. Alteração proposta

Criar exatamente as subscriptions abaixo via Shopify Admin GraphQL, usando o broker central:

1. Webhook `ORDERS_PAID`
   - Tópico: `ORDERS_PAID`
   - Callback URL: `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`
   - Formato: `JSON`
   - Motivo: venda paga deve disparar reconciliação do saldo oficial Tiny por SKU/variante.
   - Fonte/critério: Tiny é estoque verdadeiro; Shopify é evento.

2. Webhook `ORDERS_CANCELLED`
   - Tópico: `ORDERS_CANCELLED`
   - Callback URL: `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`
   - Formato: `JSON`
   - Motivo: cancelamento deve disparar nova leitura Tiny; não calcular devolução por soma/subtração local.
   - Fonte/critério: cancelamento é gatilho de reconciliação, não cálculo de estoque.

Operação pós-evento aprovada nesta fase:

- validar assinatura Shopify no proxy/Hermes;
- deduplicar evento;
- resolver pedido/line item/SKU/variant/size;
- consultar Tiny read-only / Stock OS conforme guardrails;
- gravar ledger/receipt/proposta local;
- atualizar read model local/Supabase somente se o script ativo já estiver aprovado para write local operacional;
- **não** escrever estoque no Shopify;
- **não** escrever no Tiny;
- **não** enviar mensagem a cliente/fornecedor/equipe.

## 5. Padrão canônico aplicado

- `lk-shopify-readonly`: Shopify read-only first, then approval packet before any webhook write.
- `hermes-central-integration-auth-broker`: Shopify CLI oficial via `/opt/data/home/.local/bin/hermes-cli-run`, sem auth direto por agente.
- `lk-stock`: Tiny/Stock OS como fonte de verdade; Shopify apenas como gatilho/superfície.
- Histórico canônico: `areas/lk/rotinas/approval-packet-shopify-event-tiny-stock-sync-2026-05-26.md`, porém esta aprovação limita a fase atual a **webhook + dry-run/local ledger**, sem Shopify inventory mirror.

## 6. Readback e verificação esperados

Antes de executar:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
```

Criar subscriptions com mutation Shopify Admin GraphQL via broker central, usando `--allow-mutations` e referência desta approval packet.

Readback esperado:

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

Condição de sucesso:

- existem exatamente webhooks `ORDERS_PAID` e `ORDERS_CANCELLED` apontando para `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`;
- `format=JSON`;
- `values_printed=false`;
- teste assinado retorna 2xx/202 no ingresso e cria ledger/registro local sem write externo;
- teste inválido/sem assinatura é rejeitado no proxy/Hermes.

Condição de falha:

- Shopify mutation retorna `userErrors`;
- endpoint não aceita POST assinado;
- readback não mostra os dois tópicos esperados;
- script downstream tenta escrever Tiny/Shopify ou enviar mensagem externa;
- duplicata de webhook no mesmo endpoint/tópico.

Como provar que nada fora do escopo mudou:

- comparar readback antes/depois somente para webhookSubscriptions;
- registrar IDs criados;
- verificar que não houve mutation de product/variant/inventory/theme/menu/app além de `webhookSubscriptionCreate`;
- manter ledger com `shopify_write=false`, `tiny_write=false`, `external_send=false`.

## 7. Rollback

- Apagar exatamente os webhook subscription IDs criados por este pacote via `webhookSubscriptionDelete`.
- Fazer readback Shopify confirmando ausência dos dois IDs.
- Manter ledger local para auditoria; não apagar evidência sem backup.
- Se o downstream apresentar risco, pausar/desabilitar rota Hermes/Vercel e deletar subscriptions.
- Tiny permanece intocado.

## 8. O que NÃO está aprovado

- Write de estoque Shopify / `inventorySetQuantities` / `InventoryLevel`.
- Write em Tiny.
- Criação de produto, alteração de SKU, preço, status, tag, coleção, tema, app/config fora das webhook subscriptions listadas.
- GMC/Klaviyo/Meta/WhatsApp/email/campanha.
- Contato com cliente/fornecedor/equipe.
- Reauth/OAuth manual fora do central integration auth broker.
- Criar outros tópicos (`ORDERS_CREATE`, `ORDERS_UPDATED`, `REFUNDS_CREATE`, etc.) sem aprovação separada.

## 9. Texto de aprovação para Telegram

> Aprovo criar no Shopify LK exatamente 2 webhook subscriptions para `lk-sneakerss.myshopify.com`: `ORDERS_PAID` e `ORDERS_CANCELLED`, ambos apontando para `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync`, via Hermes Central Integration Auth Broker, com snapshot antes, readback depois, teste assinado, receipt e rollback por deletion dos IDs criados. Aprovo apenas dry-run/local ledger/reconciliação read-only com Tiny/Stock OS. Não aprovo write de estoque Shopify, write Tiny, produto/preço/tema/campanha/cliente/fornecedor ou outros tópicos fora do listado.
