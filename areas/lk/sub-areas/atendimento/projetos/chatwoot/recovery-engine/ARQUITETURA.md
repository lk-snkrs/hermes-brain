# Arquitetura — Motor de Recuperação (lk-chatwoot)

Atualizado em: `2026-06-10` · Fonte: `/opt/data/lk-chatwoot-v2`

## Visão geral do fluxo

```
Shopify webhooks ──► Webhooks::ShopifyController ──► services Shopify::* ──► Recovery::ConversationDispatcher ──► Evolution API ──► WhatsApp
Klaviyo flows  ──► Webhooks::KlaviyoController ──► Klaviyo::AbandonedCartService ──┘                      (espelha de volta na inbox #3)
UI Recuperação ──► RecoverySettingsController ──► Recovery::BroadcastService / BroadcastSendJob ──┘
```

Tudo que envia mensagem converge no **`Recovery::ConversationDispatcher`** — ponto único de gating, sanitização, resolução de template e interpolação.

## Backend (Ruby)

### app/services/recovery/
- **conversation_dispatcher.rb** — cria contato+conversa+labels+custom_attributes+nota; decide canal: `Channel::Whatsapp` (template Meta via Cloud API) OU `Channel::Api`+Evolution (texto). Sanitização de placeholders (`PLACEHOLDER_TEMPLATE_VALUES`: "(vazio)", "vazio", "null"...); guard: identificador não resolvido na biblioteca NÃO envia (nota+warn); JSON malformado → não envia. **Interpolação** `interpolate(text, conversation)`: `{{nome}}` (nome real; ignora nomes auto-gerados tipo "wispy-cherry-569"), `{{produto}}`←cart_items, `{{valor}}`←cart_value formatado R$ 1.234,56, `{{link}}`←cart_recovery_url|tracking_url, `{{pedido}}`←order_number, `{{rastreio}}`←tracking_url; placeholder sem valor é removido com limpeza de espaços/pontuação.
- **evolution_sender.rb** — `POST {EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE}` (header apikey; body {number, text}; número só dígitos). Timeouts 10s/25s. Telefone mascarado em log. `configured?(account)`.
- **template_library.rb** — parseia `RECOVERY_TEMPLATE_LIBRARY` (textarea na aba Config). Formato: `nome :: texto` por linha; linhas seguintes sem `::` continuam o texto até a próxima entrada; aceita acentos no nome. `resolve(account, nome)` → texto.
- **settings_resolver.rb** — lê `accounts.recovery_settings` (jsonb) com fallback GlobalConfig. ~30 KEYS.
- **segments.rb** — relations RFM sobre `contacts.additional_attributes` (shopify_total_spent etc.). ATENÇÃO: segmentos se sobrepõem (winback ≈ 66% da base).
- **broadcast_service.rb** — cria broadcast; `whatsapp_connected?` = Cloud API OU Evolution; amostra de 3 (simulada = só nota com preview; real = envia e grava `last_broadcast_at`).

### app/jobs/
- **shopify/abandoned_checkout_job.rb** — executa cada toque: re-checa `recovered?`, checa compra posterior (RecoveryEventLog purchase) → `mark_recovered!`; **claim atômico** (`update_all ... WHERE touches_sent < touch`); template `SHOPIFY_RECOVERY_TEMPLATE_{n}` com fallback; após último toque → status `notified`.
- **shopify/followup_job.rb** — follow-up pós-entrega (delay `SHOPIFY_FOLLOWUP_DELAY_MINUTES`).
- **recovery/broadcast_send_job.rb** — envio em massa: claim atômico do broadcast (status→sending), BATCH=100, CAP 7 dias por contato (`last_broadcast_at`, gravado ANTES do envio), pacing 0.2s, trava `sendable_inbox?`.

### app/services/shopify/
- **checkout_tracking_service.rb** — upsert por (account, checkout_id) [índice único]; agenda toques só no 1º upsert; `delays(account)` parseado e **ordenado**; `mark_recovered` por checkout_id/cart_token em orders/*.
- **order_notification_service.rb** — notificações do ciclo; **dedup persistente** `RecoveryEventLog.claim!("order:{id}:{kind}")`; followup 1x por pedido.
- **tag_trigger_service.rb** — tag do pedido → template (`SHOPIFY_TAG_TRIGGERS` JSON); dedup 30d (Rails.cache=Redis).
- **contact_sync_service.rb** — grava stats Shopify no contato (orders_count, total_spent, aov, last_order_*...) em orders/create|paid|updated.
- **customer_summary_service.rb** — Customer 360 ao vivo (cache 5min). Pendência conhecida: sem tratamento 429, matching email-OU-phone limit:1.

### Controllers / Models / Migrações
- **webhooks/shopify_controller.rb** — HMAC verificado (secure_compare); topics: checkouts/create|update, orders/create|paid|updated, fulfillments/create|update; `record_purchase` grava compra no RecoveryEventLog (email downcase + phone dígitos); rescue→200 (não retry).
- **webhooks/klaviyo_controller.rb** — token SÓ via header (`X-Chatwoot-Token` ou Bearer); enfileira KlaviyoCartJob.
- **api/v1/accounts/recovery_settings_controller.rb** — show/update (segredos mascarados ••••+4; update ignora máscara), templates, test, metrics, segments, broadcasts (create/preview/send com anti-duplo-enqueue).
- **models**: `ShopifyRecoveryCheckout` (status pending/notified/recovered), `RecoveryBroadcast` (draft→…→sent/blocked/failed), `RecoveryEventLog` (`claim!` atômico via unique [account_id, dedup_key]; usado p/ dedup pedido, followup 1x e registro de compras).
- **migrações próprias**: 20260603120000 (shopify_recovery_checkouts), 20260604130000 (touches), 20260605120000 (recovery_broadcasts), **20260610150000 (recovery_event_logs)**.

## Frontend (Vue 3)
- `routes/dashboard/settings/recovery/Index.vue` — página com abas; journeys em fluxograma; badge e tempos derivados das flags/delays REAIS; biblioteca de templates; broadcast.
- `TemplatePicker.vue` — combobox buscável (nomes da biblioteca; aceita texto livre).
- `ShopifyCustomer360.vue` / `ShopifyOrderItem.vue` — painel 360 na conversa e na página de contato.

## Configuração (accounts.recovery_settings, conta 1)
Chaves principais: `SHOPIFY_RECOVERY_ENABLED`, `SHOPIFY_RECOVERY_DELAYS` (min, csv), `SHOPIFY_RECOVERY_TEMPLATE_1/2/3`, `SHOPIFY_NOTIFY_ENABLED`, `SHOPIFY_CREATED/APPROVED/SHIPPING/DELIVERED/FOLLOWUP_TEMPLATE`, `SHOPIFY_FOLLOWUP_DELAY_MINUTES`, `SHOPIFY_TAG_TRIGGERS`, `RECOVERY_TEMPLATE_LIBRARY`, `SHOPIFY_RECOVERY_INBOX_ID=3`, `KLAVIYO_RECOVERY_INBOX_ID=3`, `KLAVIYO_WEBHOOK_TOKEN`, `EVOLUTION_API_URL/INSTANCE/API_KEY`. Campos `SHOPIFY_DISCOUNT_TOUCH_1/2/3` e BROWSE/CHECKOUT/WINBACK_TEMPLATE são **planejados** (backend ainda não lê).

## Infra
- Docker compose em `/opt/chatwoot/` (rails, sidekiq, postgres pgvector/pg16 `chatwoot_production`, redis). Cache Rails = **Redis** (namespace cw_cache).
- Evolution API no Railway (instância "LK Flagship" = 551123671467; SERVER_URL corrigido 10/jun). Inbox #3 webhook: `https://evolution-api-production-fa87.up.railway.app/chatwoot/webhook/LK%20Flagship`.
- Stack legado `lk-recovery-db` (Postgres+PostgREST) — decisão: NÃO usar como cérebro; tudo no Chatwoot.
