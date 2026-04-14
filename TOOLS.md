# TOOLS.md — Infraestrutura e Integrações Hermes

> Guia de setup de todas as ferramentas + credenciais + troubleshooting
> **Última atualização:** 2026-04-14

---

## 🔐 Armazenamento de Credenciais

**REGRA OURO:** Todas as credenciais em **Doppler** (secretos manager centralizado).

- ✅ **Nunca** hardcodadas em arquivos
- ✅ **Nunca** em `.env` manual (Doppler sync)
- ✅ **Sempre** rotacionáveis (3 em 3 meses)

```bash
# Verificar credenciais armazenadas
doppler secrets list

# Adicionar/atualizar
doppler secrets set NOME_DA_CREDENCIAL='valor'

# Obter valor plain
doppler secrets get NOME --plain
```

---

## ✅ INTEGRADAS & ATIVAS

### 1️⃣ Shopify LK

**Status:** ✅ Ativo
**Store:** lksneakers.com.br (OS 2.0)
**API Key:** Doppler (`SHOPIFY_ACCESS_TOKEN`)
**Token:** `***USE_DOPPLER***` — nunca commitar valor real
**API Version:** 2024-01
**Scopes:** read_products, read_orders, read_customers, write_inventory
**Uso:** Dados de vendas, estoque, clientes
**Cron:** LK Daily Digest (7h), LK Intel Sync (0h)

**Troubleshoot:**
```bash
# Testar conexão Shopify
curl -X GET "https://lksneakers.myshopify.com/admin/api/2024-01/shops.json" \
  -H "X-Shopify-Access-Token: $(doppler secrets get SHOPIFY_ACCESS_TOKEN --plain)"
```

---

### 2️⃣ Supabase LK

**Status:** ✅ Ativo
**Project ID:** `cnjimxglpktznenpbail`
**Service Key:** Doppler (`SUPABASE_LK_SERVICE_KEY`)
**Tables:**
- customers (24k registros)
- orders (5.5k)
- order_items (7.4k)
- products (2.1k)
- customer_rfm
- analytics

**Uso:** Analytics, RFM, customer data, cross-sell
**Cron:** LK Intel Sync (0h), Cross-sell (3x/dia)

**Troubleshoot:**
```bash
# Testar conexão
curl -X GET "https://cnjimxglpktznenpbail.supabase.co/rest/v1/customers?select=*&limit=1" \
  -H "apikey: $(doppler secrets get SUPABASE_LK_SERVICE_KEY --plain)" \
  -H "Authorization: Bearer $(doppler secrets get SUPABASE_LK_SERVICE_KEY --plain)"
```

---

### 3️⃣ Supabase Zipper Vendas

**Status:** ✅ Ativo
**Project ID:** `pcstqxpdzibheuopjkas`
**Uso:** Vendas reais de obras (vendas_tango)
**Tables:** vendas_tango (2.058 registros)

**Troubleshoot:**
```bash
# Testar conexão
curl -X GET "https://pcstqxpdzibheuopjkas.supabase.co/rest/v1/vendas_tango?select=*&limit=1" \
  -H "apikey: $(doppler secrets get SUPABASE_ZIPPER_SERVICE_KEY --plain)" \
  -H "Authorization: Bearer $(doppler secrets get SUPABASE_ZIPPER_SERVICE_KEY --plain)"
```

---

### 4️⃣ Supabase SPITI / CRM

**Status:** ✅ Ativo
**Project ID:** `rmdugdkantdydivgnimb`
**Uso:** Leilão SPITI (spiti_lotes), CRM Zipper (crm_spiti), contacts
**Tables:**
- spiti_lotes
- spiti_contacts
- crm_spiti
- spiti_parcelas_pagamento

**Troubleshoot:**
```bash
# Testar conexão
curl -X GET "https://rmdugdkantdydivgnimb.supabase.co/rest/v1/spiti_lotes?select=*&limit=1" \
  -H "apikey: $(doppler secrets get SUPABASE_SPITI_SERVICE_KEY --plain)" \
  -H "Authorization: Bearer $(doppler secrets get SUPABASE_SPITI_SERVICE_KEY --plain)"
```

---

### 5️⃣ Evolution API (WhatsApp)

**Status:** ✅ Ativo
**Endpoint:** `https://evolution-api-production-fa87.up.railway.app`
**API Key:** Doppler (`EVOLUTION_API_KEY`)
**Key (plain):** `916280cbd1df907615823ea5020f3d91`
**Header:** `apikey` (minúsculo)

**Instâncias:**
| Nome | Número | Uso |
|------|--------|-----|
| Clo | +5511985555245 | Envios LK + pessoal |
| SPITI | +5511991860369 | Recebe — SPITI Auction |
| Pessoal | +5511991203361 | Lucas pessoal |
| ZipperGaleria | +551143064306 | Zipper Galeria |

**Uso:** Envio de mensagens, leads, notificações
**Cron:** Spiti Lead Collector (30min), Cross-sell (3x/dia)

**Troubleshoot:**
```bash
# Listar instâncias
curl -X GET "https://evolution-api-production-fa87.up.railway.app/instance/list" \
  -H "apikey: 916280cbd1df907615823ea5020f3d91"
```

**Regras:**
- Links no caption de imagem NÃO são clicáveis → enviar URL como texto separado (1s delay)
- Limite: 20-30 mensagens por vez (timeout em 562 conversas)

---

### 6️⃣ Klaviyo

**Status:** ✅ Ativo
**API Key:** Doppler (`KLAVIYO_API_KEY`)
**Uso:** Email campaigns, segmentos, LK News (5.020 assinantes)
**Open Rate:** ~30% (VIP 55.6%)

**Troubleshoot:**
```bash
# Testar conexão
curl -X GET "https://a.klaviyo.com/api/profiles/" \
  -H "Authorization: Klaviyo-API-Key $(doppler secrets get KLAVIYO_API_KEY --plain)" \
  -H "revision: 2024-02-15"
```

---

### 7️⃣ Meta Ads

**Status:** ⚠️ Parcial
**Access Token:** Doppler (`META_ACCESS_TOKEN`)
**Uso:** Orgânicos e insights (não público ainda)

**Troubleshoot:**
```bash
# Testar token
curl -X GET "https://graph.facebook.com/v18.0/me/accounts" \
  -H "Authorization: Bearer $(doppler secrets get META_ACCESS_TOKEN --plain)"
```

---

### 8️⃣ Vercel

**Status:** ✅ Ativo
**Token:** Doppler (`VERCEL_TOKEN`)
**Projetos:**
- spiti-financial (spiti-financial.vercel.app)

**Troubleshoot:**
```bash
# Listar projetos
curl -X GET "https://api.vercel.com/v6/projects" \
  -H "Authorization: Bearer $(doppler secrets get VERCEL_TOKEN --plain)"
```

---

### 9️⃣ Railway

**Status:** ✅ Ativo
**Token:** Doppler (`RAILWAY_TOKEN`)
**Projetos:**
- lc-whatsapp (Zipper WhatsApp bot)
- zpr-cockpit
- zpr-auto-like

**Troubleshoot:**
```bash
# Ver status
railway logs --service lc-whatsapp
railway project list
```

---

### 🔟 Google Analytics

**Status:** ✅ Ativo
**Property:** lksneakers.com.br (GA4) + zippergaleria.com (GA4)
**Acesso:** Via Google Account (lucas@gmail.com)
**Uso:** Tráfego, conversões, comportamento
**Cron:** Relatório semanal (segunda 10h)

---

### 1️⃣1️⃣ Microsoft Clarity

**Status:** ✅ Ativo
**Property:** lksneakers.com.br + zippergaleria.com
**Acesso:** Via Microsoft Account (lucas@outlook.com)
**Uso:** Session recordings, heatmaps, UX
**Cron:** Relatório mensal (dia 15)

---

### 1️⃣2️⃣ GitHub

**Status:** ✅ Ativo
**SSH Key:** `/root/.ssh/id_rsa`
**Repos:**
- lk-snkrs/lk-new-theme (dev branch)
- cerebro-cimino (OpenClaw source)
- hermes-brain (Hermes memory)

**Troubleshoot:**
```bash
# Testar SSH
ssh -T git@github.com

# Status hermes-brain
cd /root/hermes-brain && git status
```

---

### 1️⃣3️⃣ Doppler

**Status:** ✅ Ativo (Secrets Manager Central)
**Projeto:** `lc-keys`
**Config:** `prd`
**CLI:** Instalado na VPS

**Troubleshoot:**
```bash
doppler whoami
doppler secrets list
```

---

## ⏳ IMPLEMENTANDO

### Google Calendar

**Status:** ❌ TODO
**Credencial:** Doppler (`GOOGLE_CALENDAR_CREDENTIALS_JSON`)
**Setup:** OAuth2 em Google Cloud + salvar em Doppler
**Resultado esperado:** Daily briefing com eventos

### RapidAPI (Twitter/Instagram/Reddit)

**Status:** ❌ TODO
**Credencial:** Doppler (`RAPIDAPI_KEY`)
**Monitores:**
- Twitter trending sneakers
- Instagram competitors (@palmtree48, @hypeconcept, @juicysneakers)
- Reddit insights (r/Sneakers, r/Streetwear, r/Shoes)

---

## 📋 Phase 2

### Notion API
**Status:** ❌ TODO
**Credencial:** Já em Doppler (`NOTION_API_KEY`)

### Attentive API
**Status:** ❌ TODO
**Credencial:** Doppler (`ATTENTIVE_API_KEY`)

### KicksDB
**Status:** ✅ Ativo
**Credencial:** Doppler (`KICKSDB_API_KEY`)
**Uso:** Monitor preços concorrentes

### Tiny ERP
**Status:** ✅ Ativo
**Token:** Doppler (`TINY_API_TOKEN`) — Júlio usa
**Uso:** Financeiro LK

### Judge.me
**Status:** ✅ Ativo
**Token:** Doppler (`JUDGEME_API_TOKEN`)
**Uso:** Reviews LK

### Metricool
**Status:** ✅ Ativo
**Token:** Doppler (`METRICOOL_API_TOKEN`) — Renan usa
**Uso:** Social media analytics

---

## 🧠 Hermes Brain

**Path:** `/root/hermes-brain/` (VPS)
**Fonte original:** `/root/cerebro-cimino/` (OpenClaw)
**Skills:** hermes-brain, lk-crosssell, lk-leads-esfriando, heartbeat-rotativo
**Sync:** `/root/hermes-brain/sync_hermes.sh` (diário)

**Scripts principais:**
- `/root/lk-price/` — monitor concorrentes
- `/root/lk-geo/` — Reddit scanner
- `/root/lc-whatsapp/` — WhatsApp bot Zipper

---

## 📞 Troubleshooting Rápido

| Problema | Comando |
|----------|---------|
| Credencial expirada | `doppler secrets set NOME='novo-valor'` |
| API retorna 401 | Verificar Doppler → credencial errada/expirada |
| Supabase não conecta | Verificar PROJECT_ID + SERVICE_KEY |
| Evolution API offline | Checar Railway do serviço |
| Cron não roda | Verificar `cronjob list` e logs |
| Hermes fora do ar | `systemctl --user restart hermes-gateway` |

---

## 📚 Referências

- Doppler docs: https://docs.doppler.com/
- Shopify API: https://shopify.dev/
- Supabase: https://supabase.com/docs
- Evolution API: https://github.com/EvolutionAPI/evolution-api

---

*Criado em: 2026-04-14 — baseado no TOOLS.md do CWC (OpenClaw)*
