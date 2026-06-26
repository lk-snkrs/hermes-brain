# LK Crisp Inbox Anchor Patch — 2026-05-21

## Objetivo
Corrigir a lacuna em que envios WhatsApp via Crisp Template API retornam `request_accepted` e/ou são enviados pelo WhatsApp, mas não aparecem como conversa visível na Inbox Crisp.

## Aprovação
Lucas aprovou no Telegram: "Pode fazer aprovado".

## Fonte técnica verificada
Documentação Crisp REST API v1:
- `POST /v1/website/{website_id}/conversation`: cria conversa, mas a própria doc informa que a conversa não fica visível na Inbox até existir uma mensagem com `from: user`.
- `POST /v1/website/{website_id}/conversation/{session_id}/message`: envia/loga mensagem na conversa existente, exigindo `type`, `from`, `origin` e `content`.

## Snapshot/rollback
Snapshots antes da alteração:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-kWQbmEMuvdipcGjd-LK---Checkout-Abandonado-30min-24h-72h-Polling-GraphQL---Crisp-ATIVO-.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-8heG4ZyRp85p0MQj-LK---Crisp-WhatsApp-Callback-Capture-ATIVO-.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-HTTOStvvzcz0sELN-LK---Crisp-WhatsApp-Callback-Debug.json`

Rollback: restaurar o snapshot do workflow `8heG4ZyRp85p0MQj` ou remover os nodes `Prepare Crisp Inbox Anchor` e `Crisp REST Anchor Inbox Message` e a conexão paralela a partir de `Prepare Callback Receipt SQL`.

## Workflow alterado
- ID: `8heG4ZyRp85p0MQj`
- Nome: `LK - Crisp WhatsApp Callback Capture (ATIVO)`
- Nova versão n8n: `4a623a7a-2c1c-4d64-be9c-e844388ab0c9`
- `activeVersionId` confirmado igual à versão atual.

## Alteração aplicada
Adicionada ramificação paralela no callback da Crisp:

`Prepare Callback Receipt SQL` → `Prepare Crisp Inbox Anchor` → `Crisp REST Anchor Inbox Message`

A ramificação:
- só executa se houver `session_id` no callback;
- não executa em callbacks com erro/falha/rejeição;
- chama Crisp REST API com credencial n8n `Crisp REST Website Basic Auth - LK`;
- usa `X-Crisp-Tier: website`;
- cria uma mensagem de ancoragem com:
  - `type: text`
  - `from: user`
  - `origin: urn:crisp.im:whatsapp:0`
  - `stealth: true`
  - `automated: true`
  - `properties.lk_anchor_only: true`

## Segurança
- Não reenvia WhatsApp.
- Não altera Shopify, cupom, template ou cliente.
- Não expõe tokens.
- A mensagem REST é apenas artefato de Inbox/log, em modo `stealth`.

## Verificação executada
- Readback do workflow confirmou nodes novos e conexão paralela.
- Webhook de verificação sem `session_id` retornou HTTP 200 e gravou receipt no Supabase.
- A branch `Prepare Crisp Inbox Anchor` retornou 0 items quando não havia `session_id`, como esperado.
- Callback storage existente continuou funcionando.

## Pendência / validação final
A validação final depende do próximo callback real da Crisp contendo `session_id`. Quando ocorrer, verificar:
- execução do node `Crisp REST Anchor Inbox Message`;
- HTTP 202/200 da Crisp REST;
- conversa visível na Inbox;
- ausência de segundo envio ao cliente.
