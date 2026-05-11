---
name: lk-seo-weekly-improvement
description: "Use for LK Sneakers weekly SEO/CRO improvement loop: Claude SEO audit scores, Search Console/Merchant/PDP prioritization, page improvement goals, and read-only weekly recommendations with approval before Shopify/theme/content writes."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [lk-sneakers, seo, cro, claude-seo, weekly-audit, search-console, merchant-center, pdp]
    related_skills: [seo-audit, seo-page, seo-content, seo-ecommerce, seo-google, seo-schema, seo-geo, lk-shopify-readonly, lk-shopify-product-upload]
---

# LK SEO Weekly Improvement

## Overview

Use this skill when Lucas asks for the LK **SEO/CRO module**, weekly SEO page improvements, Claude SEO audit score, Search Console opportunities, Merchant Center/feed problems, or PDP improvement goals.

Lucas may say “CO”, “C.O.”, “SEO”, “Claude SEO”, “nota”, “audit”, “melhorias de página”, or “processo semanal”. In this LK context, interpret it as **SEO + CRO page improvement loop**, not as a one-off report.

The objective is not to produce a loose SEO audit. The objective is to create a weekly, scored improvement queue that makes LK product/category pages better over time.

## Source Hierarchy

1. Public site / PDP HTML: `https://lksneakers.com`.
2. Claude SEO skill family from `AgriciDaniel/claude-seo` installed in Hermes: `seo-audit`, `seo-page`, `seo-content`, `seo-ecommerce`, `seo-schema`, `seo-geo`, `seo-google` when available.
3. Google Search Console: queries, impressions, clicks, CTR, average position.
4. Google Merchant Center: feed/disapproval/product data issues when credentials/workflow are available.
5. Shopify read-only: product title, handle, SEO fields, tags, vendor, product type, PDP status.
6. Shopify writes/theme/content changes only after Lucas approves a preview.

## Weekly Cadence

Default cadence: weekly, Monday morning BRT.

Each run should produce:

- Overall SEO/CRO Health Score: 0–100.
- Score breakdown:
  - Technical/indexability.
  - On-page title/meta/H1/headings.
  - Content quality/E-E-A-T/helpfulness.
  - Product/e-commerce SEO/schema.
  - AI Search/GEO readiness.
  - Images/alt/performance risks.
  - Search Console opportunity quality.
  - Merchant/feed risk if available.
- Top opportunities for the week.
- Target score for next week.
- Fixed improvement queue with owner/risk/approval status.

## Page Selection Logic

Prioritize pages in this order:

1. PDPs with traffic/impressions but low CTR or weak conversion.
2. PDPs with strong product/commercial importance from LK OS stock/sales signals.
3. PDPs newly uploaded via `lk-shopify-product-upload`.
4. Category/collection pages with organic opportunity.
5. Pages with Merchant Center/feed issues.
6. Homepage only when technical/sitewide issue exists.

Do not audit 500 pages every week if the actionable queue is small. Prefer a focused weekly batch:

- 1 site-level health snapshot.
- 5–10 priority PDP/category pages.
- 3–7 concrete improvements.

## Workflow

1. Identify scope and week date.
2. Run/read Claude SEO audit signals:
   - `seo-audit` for site-level health.
   - `seo-page` for selected PDP/category URLs.
   - `seo-content` for E-E-A-T, helpfulness and AI readability.
   - `seo-ecommerce` for Product SEO/schema/merchant/product listing quality.
   - `seo-schema`/`seo-geo` where relevant.
3. Pull Search Console and Merchant Center signals when available; if unavailable, mark as pending and do not invent data.
4. Produce a scorecard and compare to prior saved score if one exists.
5. Create an improvement queue:
   - page URL;
   - current issue;
   - expected impact;
   - effort;
   - risk;
   - recommended change;
   - approval required;
   - target score uplift.
6. Save a dated report in Hermes Brain under `reports/` or `areas/lk/rotinas/` when running inside the Brain repo.
7. If any change would write to Shopify, theme, app, Merchant Center, GSC, feed, or public content, stop at preview and ask Lucas for explicit approval.

## Score Targets

Use scores as operating goals, not vanity metrics.

Recommended targets:

- 0–59: Critical — fix indexability/metadata/schema/content basics first.
- 60–74: Needs work — choose 3–5 high-leverage improvements.
- 75–84: Good — improve priority PDPs and AI/GEO structure.
- 85–92: Strong — focus on compounding gains, internal links, rich snippets, Merchant hygiene.
- 93–100: Excellent — maintenance, experimentation and monitoring.

Every weekly report should include:

- Current score.
- Previous score, if available.
- Target for next run.
- Which actions are needed to raise the score.

## Approval Boundaries

Free without approval:

- Public/read-only SEO audit.
- Search Console/Merchant read-only checks.
- Shopify read-only checks.
- Drafting title/meta/body/schema/alt recommendations.
- Creating a preview and improvement queue.

Requires Lucas approval:

- Updating Shopify product/page/collection SEO fields.
- Updating product description/body HTML.
- Changing images/alt text in Shopify.
- Editing theme/liquid/app settings.
- Changing Merchant Center/feed settings.
- Publishing content, campaigns or customer-facing messaging.

Requires plan + rollback:

- Sitewide theme or template changes.
- Bulk SEO updates.
- Feed automation.
- Any cron that writes externally.

## Output Format for Lucas

Use Portuguese, executive and direct:

- Veredito curto.
- Nota SEO/CRO atual: X/100.
- Meta próxima: Y/100.
- O que melhorou/piorou vs semana anterior.
- Top 5 ações da semana.
- PDPs/páginas prioritárias.
- O que posso preparar agora sem aprovação.
- O que exige aprovação antes de escrever.
- O que não fiz.

## Common Pitfalls

1. **Relatório solto.** SEO só vale se virar fila de melhoria de página/PDP.
2. **Confundir auditoria com write.** Audit e preview são livres; writes precisam aprovação.
3. **Auditar tudo e não priorizar nada.** Weekly loop deve escolher poucas ações de alto impacto.
4. **Ignorar conversão.** LK SEO deve melhorar tráfego qualificado e PDP, não só nota técnica.
5. **Inventar GSC/Merchant data.** Se API não estiver disponível, declarar pendente.
6. **Usar score como vaidade.** Score deve ter meta e ações para subir.

## Verification Checklist

- [ ] Claude SEO/SEO skills loaded or referenced.
- [ ] Site/PDP URLs checked read-only.
- [ ] Scorecard generated with categories.
- [ ] Prior score compared if available.
- [ ] Improvement queue created.
- [ ] Writes separated from read-only recommendations.
- [ ] Lucas approval requested for any public change.
- [ ] Report saved when operating inside Hermes Brain.
