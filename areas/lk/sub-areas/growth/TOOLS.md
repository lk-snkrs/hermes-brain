# TOOLS — LK Growth OS

## Google

- Google Analytics / GA4: tráfego, canais, landing pages, conversão, receita e funil.
- Google Search Console: queries, páginas, CTR, posição, sitemaps, inspeção de URL.
- Google Merchant Center: status de produtos, issues, feed e supplemental feed.
- PageSpeed Insights / CrUX: Core Web Vitals, field data e performance mobile.
- Google Ads/Keyword Planner quando disponível: volume/demanda; não editar campanhas sem aprovação.
- Google Business Profile quando aplicável: local SEO read-only.

## Shopify LK

- Admin GraphQL read-only para produtos, coleções, SEO fields, status e evidência.
- Theme dev/unpublished para CRO previews.
- Production writes apenas com aprovação explícita, rollback e verificação.

## SEO/GEO

- Skills `seo-google`, `seo-technical`, `seo-page`, `seo-content`, `seo-ecommerce`, `seo-schema`, `seo-geo`.
- Public crawl/sitemap/robots/HTML/schema/llms.txt.
- SERP/concorrência quando necessário.

## CRM/Paid como sinais

- Klaviyo: sinal de campanha/engajamento; não enviar sem aprovação.
- Meta/Google Ads: sinal de demanda/performance; não editar sem aprovação.
- Influencer/Pareto/FHITS: contexto de produto e demanda; separar responsabilidades.

## Secrets

Credenciais vivem no Doppler `lc-keys/prd`. Documentar nomes, nunca valores.

Secret novo do bot:

- `TELEGRAM_LK_GROWTH_BOT_TOKEN`
