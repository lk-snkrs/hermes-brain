# LK Growth OS — Escopo canônico de 18 tópicos

Este é o checklist canônico que o LK Growth OS deve considerar antes de dizer que uma análise de Growth/SEO/GMC/CRO está completa.

## 18 tópicos obrigatórios

1. **GA4 / Google Analytics** — sessões, usuários, receita, conversão, canais, landing pages e funil PDP → carrinho → checkout.
2. **Google Search Console** — queries, páginas, impressões, cliques, CTR, posição, indexação, sitemaps e inspeção de URL.
3. **Google Merchant Center** — issues, warnings, feed, produtos reprovados, preço, disponibilidade, atributos e supplemental feeds.
4. **Shopify SEO técnico/on-page** — title, meta description, H1, headings, canonicals, handles, coleções, PDPs e páginas.
5. **Shopify CRO / UX mobile** — PDP mobile, coleções, filtros, ordenação, CTA, trust blocks, checkout friction e preview em dev theme.
6. **GEO / AI Search** — `llms.txt`, blocos citáveis, FAQs, estrutura para ChatGPT, Perplexity, Gemini e AI Overviews.
7. **PageSpeed / CrUX / Core Web Vitals** — LCP, INP, CLS, performance mobile e field data.
8. **Schema / structured data** — Product, Offer, AggregateRating, Breadcrumb, Organization, FAQ e validação de rich results.
9. **Reviews / prova social** — Judge.me ou fonte equivalente, snippets, rating, UGC e impacto em conversão.
10. **Paid media signals** — Meta Ads, Google Ads, Pareto e campanhas como sinal de demanda/gargalo; sem editar campanhas sem aprovação.
11. **Influencer / social demand signals** — FHITS, creators, produtos divulgados, picos de demanda e gargalos em PDP/coleção.
12. **Concorrência / SERP** — players, títulos, snippets, PAA, merchant listings, gaps de conteúdo e diferencial premium da LK.
13. **Google Business / local SEO** — quando aplicável: presença local, mapas, reviews locais e consistência NAP.
14. **Klaviyo / CRM signals** — campanhas, engajamento, fluxos e listas como sinal de demanda; sem disparos sem aprovação.
15. **Catálogo / product data quality** — GTIN, MPN, brand, condition, images, alt text, variantes, disponibilidade e consistência Shopify ↔ GMC.
16. **Conteúdo e taxonomia comercial** — coleções, descrições, FAQ, guias, links internos, breadcrumbs e linguagem premium sem falar pronta entrega/encomenda/estoque como taxonomia pública.
17. **Mensuração e QA de eventos** — eventos GA4, ecommerce tracking, UTMs, consent, atribuição, divergências Shopify ↔ GA4 e qualidade dos dados.
18. **Impact review / experimentation** — antes/depois, receipt, rollback, janela de ~7 dias, classificação de impacto e próximos testes.

## Regra decision-grade

Uma recomendação só é **decision-grade** quando combina, quando disponível:

- dado comercial/conversão: Shopify e/ou GA4;
- dado de demanda/search: GSC, SERP, paid/influencer signals;
- dado de saúde técnica: PageSpeed/CrUX, schema, HTML, GMC;
- risco, rollback, evidência e aprovação necessária.

Se faltarem os dados autenticados relevantes, declarar explicitamente: **não decision-grade ainda**.

## Guardrail de writes

Por padrão, o LK Growth OS opera read-only/preview. Writes em Shopify, GMC, GA4/GSC config, Ads, Klaviyo, theme production, preço, estoque, checkout, WhatsApp/e-mail ou qualquer canal externo exigem aprovação explícita atual de Lucas, evidência e rollback.
