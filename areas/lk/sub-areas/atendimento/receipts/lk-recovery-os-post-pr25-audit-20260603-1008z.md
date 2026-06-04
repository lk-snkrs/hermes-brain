---
title: LK Recovery OS — novo audit pós parser Klaviyo/PR25
date: 2026-06-03T10:08:00Z
area: lk/atendimento
system: recovery-os
status: parcialmente_funcionando_em_atencao
scope: read-only audit
---

# Escopo

Lucas pediu novo audit e reflexão após deploy/merge do parser Klaviyo `identity_hints`.

Audit read-only realizado sobre:

- Git/local/CI
- Cloudflare Worker e KV
- Shopify webhooks e checkouts abertos
- Fallback DB Postgres/PostgREST
- Identity graph Klaviyo/cart/email/phone
- Safety/customer-send flags por evidência indireta e mensagens

# Evidência coletada

## Código/Git/CI

```text
local git: ## main...origin/main
HEAD: 8d61531 fix: parse Klaviyo identity hints (#25)
npm test: 8 files / 49 tests passed
GitHub Actions CI main: success
Vercel status: success
PR25: merged, merge_commit_sha 8d615311ce89c44dd0e0c58143286bc180dcd34d
```

## Worker/DB health

```text
https://recovery.lucascimino.com/healthz => HTTP 200 {"service":"lk-recovery","status":"ok"}
https://recovery-db.lucascimino.com/healthz => HTTP 200 {"service":"lk-recovery-db","status":"ok"}
```

Cloudflare:

```text
latest Worker deploy: dae2afe0-0f27-4de2-8ed9-9b78487b5942 at 2026-06-03T09:47:11Z
CHECKOUT_BUFFER_KV: []
```

## Shopify

```text
webhooks_total: 17
Recovery OS webhooks:
- checkouts/create -> https://recovery.lucascimino.com/shopify/checkouts/create
- checkouts/update -> https://recovery.lucascimino.com/shopify/checkouts/update
- orders/create -> https://recovery.lucascimino.com/shopify/orders/create
```

Lifecycle adicional observado:

```text
orders/create -> https://lucascimino.com/webhook/shopify
```

Checkouts REST 72h:

```text
checkouts_72h_total: 16
open_72h: 16
todos com recovery_url: sim
```

## DB geral

```text
raw_events: 12902, latest 2026-06-03 10:08:15Z
checkouts: 31, latest_seen 2026-06-02 21:46:05Z
recovery_candidates: 104, latest_update 2026-06-03 10:06:06Z
recovery_messages: 0
raw_retry_or_error_24h: 0
```

Eventos 24h principais:

```text
storefront identity_update/view_product: vivo até 2026-06-03 10:08Z
klaviyo_webhook events: vivo até 2026-06-03 10:08Z
storefront begin_checkout: 1 em 2026-06-03 04:56Z
shopify_checkouts_backfill checkout_started: 31 em 2026-06-03 00:10Z
```

## Klaviyo / identity graph após patch

Storefront 60 min:

```text
storefront_60m: 593
with_identity_hints: 593
with_kla_cookie: 593
with___kla_id: 593
with_cart_token: 593
with_email_hash: 0
with_phone_hash: 0
```

Identity links 60 min:

```text
identity_links_60m: 2579
klaviyo_profile_links_60m: 700
cart_links_60m: 168
email_hash_links_60m: 700
phone_hash_links_60m: 179
latest_klaviyo_profile: 2026-06-03 10:08:18Z
latest_cart_token: 2026-06-03 10:08:11Z
```

# Achado crítico

Há um gap concreto no plano de Shopify checkout lifecycle:

```text
Shopify open checkouts 72h: 16
Encontrados no DB checkouts: 15
Faltando no DB: 1
```

Checkout faltante:

```text
gid://shopify/Checkout/39581254648030
Shopify created_at: 2026-06-03T02:10:31-03:00
Shopify updated_at: 2026-06-03T02:10:31-03:00
recovery_url: true
line_items: 1
DB checkouts: ausente
```

Interpretação:

- Webhook Shopify está configurado.
- Worker e DB estão saudáveis.
- KV buffer está vazio.
- Mas não há evidência de `checkout_started` live vindo de Shopify webhook após o backfill de 00:10Z.
- O checkout Shopify mais recente de 05:10Z não persistiu em `checkouts`.

# Veredito

Status: parcialmente funcionando / em atenção.

Funciona com boa evidência:

- Worker online.
- DB fallback online.
- Storefront beacon vivo.
- Cookie Klaviyo chegando em `identity_hints`.
- Parser pós-deploy ligando `klaviyo_profile_id`, `email_hash`, `phone_hash`, `cart_token` no identity graph.
- CI/main limpo.
- Envios cliente não aconteceram (`recovery_messages = 0`).

Não está comprovado como 100% funcionando:

- Captura live de checkout Shopify via webhooks `checkouts/create/update` para persistência em `checkouts`.
- Há 1 checkout open Shopify ausente do DB.

# Recomendação

Não ativar recuperação real ainda.

Próximo approval packet recomendado:

1. Diagnóstico read-only/observability de delivery Shopify/Cloudflare para o checkout ausente.
2. Adicionar auditoria explícita para webhook ingress: path/topic, hmac_ok/hmac_fail, checkout_id, persist_ok/persist_buffered.
3. Só depois fazer backfill pontual do checkout ausente, se Lucas aprovar write DB.
4. Manter `dry_run/internal-only/live-send off` até `Shopify open checkouts == DB checkouts` e surgirem eventos live de `checkout_started` via webhook, não só backfill.
