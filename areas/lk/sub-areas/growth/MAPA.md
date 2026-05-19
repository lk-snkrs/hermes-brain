# MAPA — LK Growth OS

Subárea especialista da LK Sneakers para Search, Google, Merchant, Analytics, CRO e AI Visibility.

## Missão

Transformar dados de GA4, Search Console, Merchant Center, Shopify, SERP e auditorias técnicas em uma fila semanal de melhorias comerciais para LK: mais tráfego qualificado, melhor CTR, melhor conversão e maior visibilidade em IA, sempre com preview e aprovação antes de writes.

## Escopo

Escopo canônico detalhado: `ESCOPO-18-TOPICOS.md`.

- GA4 / Google Analytics: sessões, usuários, conversão, receita, landing pages, funil e impacto pós-mudança.
- Google Search Console: queries, páginas, impressões, cliques, CTR, posição, indexação, sitemaps e inspeção de URL.
- Google Merchant Center: reprovações, warnings, feed, atributos, preço, disponibilidade e supplemental feed.
- Shopify SEO: title/meta, H1, descrições, canonicals, PDPs, coleções, handles e schema.
- Shopify CRO/theme: PDP mobile, collection pages, filtros, ordenação, CTA, trust blocks, reviews e dev-theme previews.
- GEO / AI Search: `llms.txt`, blocos citáveis, FAQ, schema e estrutura para ChatGPT/Perplexity/Gemini/AI Overviews.
- PageSpeed / CrUX / Core Web Vitals: LCP, INP, CLS e performance mobile.
- Reviews/prova social: Judge.me ou fonte equivalente, snippets e impacto de conversão.
- Paid/influencer signals como contexto: Pareto, FHITS, Meta/Google Ads, produtos divulgados e gargalos de PDP/coleção.
- Claude Blog/content engine: briefs, outlines, artigos/FAQs, clusters, schema editorial, GEO/AEO e repurpose quando a oportunidade for conteúdo/taxonomia comercial.
- Concorrência/SERP e Google Business/local SEO quando aplicável.

## Checklist canônico — 18 tópicos

Antes de declarar um diagnóstico de Growth completo, verificar os 18 tópicos em `ESCOPO-18-TOPICOS.md`: GA4, GSC, GMC, Shopify SEO, Shopify CRO, GEO/AI Search, PageSpeed/CrUX/CWV, schema, reviews, paid signals, influencer/social demand, concorrência/SERP, Google Business/local, Klaviyo/CRM signals, catálogo/product data quality, conteúdo/taxonomia comercial, mensuração/QA de eventos e impact review/experimentation.

## Fontes de verdade

1. Dados comerciais e conversão: Shopify, GA4, GSC e GMC.
2. Demanda/search: GSC, SERP, paid/influencer signals.
3. Diagnóstico público: HTML, PageSpeed, robots/sitemap, schema e `llms.txt`.
4. Brain/Hermes: decisões, guardrails, histórico, skills e rotinas.

## Regras LK críticas

- Relatório SEO/CRO sem dados de vendas, visitas/sessões, conversão, receita, GSC/CTR ou demanda deve ser marcado como não decision-grade.
- Stock/Tiny pode ser contexto operacional, mas não critério decisivo de SEO/CRO.
- Não falar publicamente em pronta entrega/encomenda/estoque como taxonomia; disponibilidade e prazo vão para chat/atendimento.
- Alterações de theme sempre primeiro em dev theme/preview.
- Writes em Shopify, GMC/feed, campanhas, Klaviyo/WhatsApp/email, preço, estoque ou produção exigem aprovação explícita atual de Lucas.

## Agente Telegram

- Perfil Hermes: `lk-growth`.
- Bot Telegram: `LKGrowth_HermesBot`.
- Secret Doppler: `TELEGRAM_LK_GROWTH_BOT_TOKEN` em `lc-keys/prd`.
- Canal recomendado: `[LK] Growth OS` ou DM com o bot para temas de SEO/GMC/CRO/GA4/GSC/GEO.

## Arquivos desta subárea

- `SOUL.md` — identidade do agente.
- `AGENTS.md` — regras operacionais e aprovações.
- `TOOLS.md` — ferramentas e integrações.
- `MEMORY.md` — memória local da subárea.
- `HEARTBEAT.md` — cadência e checks.
- `ESCOPO-18-TOPICOS.md` — checklist canônico do escopo Growth.
- `CRONS-MIGRATION.md` — mapa de migração das rotinas/cron jobs para o LK Growth OS.
- `CONNECTORS-READONLY-INVENTORY.md` — status dos conectores Shopify, GA4, GSC, GMC, PSI/CrUX, Klaviyo e Meta.
- `CLAUDE-ADS-HERMES-NOTE.md` — nota operacional da instalação Claude Ads/AgriciDaniel no universo LK Growth e modo de uso Hermes.
- `CLAUDE-BLOG-HERMES-NOTE.md` — nota operacional da instalação Claude Blog/AgriciDaniel no universo LK Growth e uso diário para conteúdo/GEO/FAQ/clusters.
- `IMPACT-REVIEWS.md` — política e estado dos follow-ups/impact reviews no profile `lk-growth`.
- `rotinas/growth-decision-router.md` — matriz de decisão para escolher GA4/GSC/GMC/Shopify/CRO/GEO/Ads/Blog/DataForSEO por sintoma.
- `rotinas/dataforseo-mcp-reload-approval-2026-05-19.md` — approval packet para expor DataForSEO MCP no runtime ativo sem violar guardrails de VPS/Hermes.
- `templates/growth-audit-output-template.md` — template padrão de auditoria Growth com fatos, interpretação, recomendação, approval packet, rollback e review de impacto.
- `reports/growth-360-smoke-test-2026-05-19.md` — validação documental do fluxo 360º e próximos critérios de smoke test live controlado.
- `projetos/growth-action-prd-2026-05-19.md` — PRD de ação para cadência semanal orientada a receita, conversão e reviews D+7.
- `contexto/` — mapas por fonte e domínio.
- `rotinas/` — rotinas operacionais.
- `templates/` — formatos padronizados de auditoria/approval packet.
- `skills/` — processos repetíveis.
- `projetos/` — PRDs, backlog e approval log.
