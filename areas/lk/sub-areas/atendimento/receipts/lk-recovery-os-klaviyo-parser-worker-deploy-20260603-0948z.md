---
title: LK Recovery OS — deploy Worker parser Klaviyo identity_hints
date: 2026-06-03T09:48:00Z
area: lk/atendimento
system: recovery-os
status: production_worker_deployed_sends_disabled
approval: Lucas respondeu "Aprovo" ao approval packet de deploy apenas do Worker
---

# Resumo

Deploy de produção realizado apenas no Cloudflare Worker `lk-recovery` para corrigir o parser Klaviyo em visitantes não logados.

Escopo aprovado/executado:

- Deployar somente o Worker Recovery OS com correção local em `extractKlaviyoSignals()`.
- Sem mexer no tema Shopify.
- Sem ativar envios WhatsApp/e-mail/Klaviyo.
- Sem alterar Tiny/Shopify/Chatwoot além do deploy do Worker.

# Mudança implantada

Arquivo local alterado antes do deploy:

- `/opt/data/lk-recovery-os/workers/recovery-os/src/klaviyo.ts`
- teste novo: `/opt/data/lk-recovery-os/workers/recovery-os/tests/klaviyo.test.ts`

Parser passou a ler sinais Klaviyo também em:

```text
identity_hints.kla_cookie
identity_hints.__kla_id
identity_hints.klaviyo_kla_id
identity_hints.klaviyo_profile_id
identity_hints.klaviyo_id
identity_hints.klaviyo_kx
identity_hints.klaviyo_email
identity_hints.klaviyo_phone
```

# Pré-flight

Comando:

```text
npm test
```

Resultado:

```text
Test Files: 8 passed (8)
Tests: 49 passed (49)
```

# Deploy

Primeira tentativa com `npm run deploy` falhou por Node local 20.19.2 enquanto Wrangler exige Node >=22.

Deploy efetivo executado com Node 22 via:

```text
npx -y node@22 node_modules/wrangler/bin/wrangler.js deploy
```

Resultado:

```text
Uploaded lk-recovery
Deployed lk-recovery triggers
custom domain: recovery.lucascimino.com
schedule: */10 * * * *
Current Version ID: dae2afe0-0f27-4de2-8ed9-9b78487b5942
```

# Safety flags observadas no deploy

Wrangler mostrou as flags de segurança intactas:

```text
LK_RECOVERY_DRY_RUN=true
LK_CHATWOOT_INTERNAL_ONLY=true
LK_LIVE_SEND_ENABLED=false
LK_WHATSAPP_SEND_ENABLED=false
LK_EMAIL_SEND_ENABLED=false
LK_SUPPORT_PROVIDER=chatwoot
```

# Pós-deploy imediato

Health checks:

```text
https://recovery.lucascimino.com/healthz => HTTP 200 {"service":"lk-recovery","status":"ok"}
https://recovery-db.lucascimino.com/healthz => HTTP 200 {"service":"lk-recovery-db","status":"ok"}
```

Cloudflare/KV:

```text
CHECKOUT_BUFFER_KV: []
```

DB fallback:

```text
recovery_messages_total: 0
buffered_raw_errors: 0
```

Storefront últimos 30 min:

```text
storefront_30m: 250
with_kla_cookie: 250
with_email_hash: 0
with_phone_hash: 0
with_cart_token: 250
```

Identity graph últimos 30 min:

```text
identity_links_30m: 1226
klaviyo_like_links_30m: 343
cart_links_30m: 72
email_hash_links_30m: 801
phone_links_30m: 283
key_type klaviyo_profile_id: 343, latest 2026-06-03 09:48:06Z
```

# Veredito

Produção recebeu o patch do parser Klaviyo. Captura/ligação de identidade Klaviyo está aparecendo no DB após o deploy, e envios ao cliente permanecem desligados.

# Observação operacional

Código local ficou modificado/uncommitted após o deploy. Recomendado abrir PR/commit separado para rastreabilidade, se Lucas aprovar fluxo GitHub depois.
