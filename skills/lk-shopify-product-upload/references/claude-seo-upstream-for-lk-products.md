# Claude SEO upstream mapping for LK product uploads

Session context: Lucas linked `https://github.com/AgriciDaniel/claude-seo` and asked whether the LK Shopify upload skill will use it.

## Resolution

Yes. For Hermes, “Claude SEO” maps to the installed content-seo skill family derived from `AgriciDaniel/claude-seo`, primarily:

- `seo-content` — content quality, E-E-A-T/helpfulness, AI citation/readability, non-generic copy.
- `seo-ecommerce` — product-page SEO, product schema considerations, marketplace/product listing quality.
- `seo-page` — page-level title/meta/on-page checks when useful.

## Repository facts verified via GitHub API on 2026-05-11

- Repo: `AgriciDaniel/claude-seo`
- Description: Universal SEO skill for Claude Code with SEO sub-skills/sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, ecommerce SEO, Google APIs and reporting.
- Default branch: `main`
- License: MIT
- Relevant folders: `skills/seo-content`, `skills/seo-ecommerce`, `skills/seo-page`, etc.

## How to apply in LK product upload

1. Research the sneaker/model first; do not invent history.
2. Draft factual LK-premium product copy.
3. Run the Claude SEO refinement lens:
   - entity clarity: official model, brand, colorway, collab/release where sourced;
   - product SEO: readable title, meta description, tags, alt-text pattern;
   - E-E-A-T/helpfulness: specific facts, no empty marketing claims;
   - GEO/AI readability: concise extractable statements;
   - duplication control: do not paste generic marketplace/manufacturer copy.
4. Include the refined copy in the Shopify preview before asking Lucas for approval.

## Pitfall

Do not tell Lucas “Claude SEO is external/not available” if the installed `seo-content` / `seo-ecommerce` skills are present. Treat the linked repo as upstream/source family, not as a blocker.