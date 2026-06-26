# LK Growth — Doppler integrations audit

Data UTC: 2026-06-03T17:53:40+00:00

Escopo: varredura read-only de nomes de secrets em Doppler `lc-keys/prd`. Valores não foram impressos nem persistidos.

## Integrações já úteis para LK Growth

### Core commerce / product truth
- Shopify: `SHOPIFY_*` presentes. Útil para PDP, collections, product data, tags, theme/readback. Writes exigem aprovação.
- Tiny ERP: `TINY_*` presentes. Probe read-only OK via busca de produtos; útil para catálogo, disponibilidade operacional, SKU/GTIN/MPN/brand, qualidade de dados. Não usar estoque como critério SEO isolado.

### Google / Merchant / Analytics
- GA4 LK: `GA4_LK_*`, `GA4_PROPERTY_ID`, service account presentes.
- GSC: `GSC_SITE_URL` e service account Google presentes.
- Google Ads: `GOOGLE_ADS_*` presentes.
- Merchant: `MERCHANT_CENTER_ID_LK` presente.
- PageSpeed/CrUX: `PAGESPEED_API_KEY` e `GOOGLE_API_KEY` presentes; wrapper validado.

### Search / SEO / GEO
- DataForSEO: credentials presentes e MCP já funcional.
- Ahrefs: token presente e endpoint domain-rating validado.
- SEMrush: `SEMRUSH_API_KEY` presente; probe domain_ranks BR OK.

### CRM / retention / demand signals
- Klaviyo: `KLAVIYO_API_KEY` presente; analytics read-only validado.
- MailerLite: API presente; probe subscribers OK. Útil se ainda houver listas/segmentos históricos fora do Klaviyo.
- Crisp: tokens presentes; rota testada `/profile` falhou por endpoint, mas credencial existe. Útil para intenção, dúvidas por produto, gargalos de PDP/checkout, consultas de autenticidade/prazo.

### Paid/social
- Metricool: `METRICOOL_*` presentes; MCP já funcional.
- Meta Ads: `META_*` presentes; MCP read-only funcional.
- Instagram Graph: token presente, mas probe falhou por token inválido/expirado. Precisa renovar se quisermos social organic insights.

### Automation / logs / storage
- N8N: `N8N_*` presentes. Útil para consultar execuções/workflows read-only, mas writes exigem cuidado.
- Supabase LK: `SUPABASE_LK_*` presentes. Útil para recovery/CRM/logs/attribution se houver tabelas relevantes.
- Cloudflare/R2: presentes. Útil para cache/CDN/storage diagnóstico; mudanças exigem aprovação.
- GitHub/Vercel: presentes. Útil para previews/PRs/dev deploys, não para operação Growth diária sem escopo.

## Probes feitos

- SEMrush: OK; `domain_ranks` BR respondeu com header válido.
- Tiny: OK; busca read-only de produto retornou status OK e 100 registros de probe.
- MailerLite: OK; endpoint subscribers respondeu.
- Instagram Graph: falhou HTTP 400; token invalidado/expirado.
- Crisp: credencial presente; endpoint testado não existe/rota incorreta. Precisa mapear endpoint correto.

## Recomendação de uso nos crons

1. Weekly Command Center:
   - Shopify + GA4 + GSC + GMC + Klaviyo + Meta/Metricool + DataForSEO + Ahrefs/SEMrush.
2. SEO/GSC + GEO:
   - GSC + DataForSEO + Ahrefs + SEMrush + PageSpeed/CrUX + schema/llms.
3. CRO/PDP Funnel:
   - Shopify + GA4 + Klaviyo + Crisp + PageSpeed/CrUX + Meta/Metricool demand.
4. GMC/Product Data:
   - GMC + Shopify + Tiny + Simprosys contexto + DataForSEO Merchant/SERP quando relevante.
5. Impact Review:
   - Shopify/GA4 revenue + GSC + Klaviyo + paid/social + Ahrefs/SEMrush para impacto SEO/off-site.

## Pendências recomendadas

- Renovar `INSTAGRAM_ACCESS_TOKEN` ou trocar para token long-lived/system user se social organic insights forem importantes.
- Criar wrapper Crisp read-only correto para conversas/tags/intenção, sem enviar mensagem.
- Criar wrapper SEMrush read-only padronizado para Domain Overview / Organic Keywords / Competitors.
- Criar wrapper Tiny product-data read-only com campos úteis para GMC/catalog QA.
- Validar Google Ads/Merchant scripts diretos além de MCP/skill, se necessário.

## Guardrails

- Nenhum valor de secret foi persistido.
- Todos os probes foram read-only.
- Writes em Shopify/Tiny/GMC/Ads/Klaviyo/Crisp/Cloudflare/N8N/Vercel/GitHub continuam exigindo aprovação explícita.


## Decisão de priorização — 2026-06-03T17:57:38+00:00

Decisão Lucas:
- SEMrush: migrar prioridade para Ahrefs; SEMrush fica fallback eventual.
- Crisp: não investir; migração para Chatwoot.
- Tiny/estoque: não usar como rotina Growth/critério decisivo, pois LK vende curadoria/sob encomenda.

Aplicação:
- Crons patchados para priorizar Ahrefs + DataForSEO + GSC.
- Conversational insights devem apontar para Chatwoot quando estiver disponível.
- Tiny permanece apenas contexto técnico eventual para GMC/schema/product data, sem taxonomia pública de estoque/disponibilidade.
