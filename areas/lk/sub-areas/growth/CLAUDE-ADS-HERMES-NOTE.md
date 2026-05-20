# Claude Ads no universo LK Growth / Hermes

Data: 2026-05-19
Fonte: https://github.com/AgriciDaniel/claude-ads
Versão/repo lido: public release v1.7.1 no README; commit local `283d9d4`
Status: instalado no perfil `lk-growth` como skills Hermes

## O que é

Claude Ads é um framework de auditoria e otimização paid media multi-plataforma. Cobre Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple e Amazon Ads, com 250+ checks, score 0-100, templates por indústria, auditoria de tracking/attribution e fluxo criativo.

No contexto LK, ele entra como camada especialista de paid/influencer demand signals dentro de Growth, conectando campanhas, criativos e tracking a CRO/SEO/GEO e PDP/collection diagnosis.

## Instalação Hermes

Categoria local: `paid-media`

- Main orchestrator: `ads`
- Sub-skills instaladas:
  - `ads-audit`
  - `ads-google`
  - `ads-meta`
  - `ads-youtube`
  - `ads-linkedin`
  - `ads-tiktok`
  - `ads-microsoft`
  - `ads-apple`
  - `ads-amazon`
  - `ads-attribution`
  - `ads-server-side-tracking`
  - `ads-creative`
  - `ads-landing`
  - `ads-budget`
  - `ads-plan`
  - `ads-competitor`
  - `ads-math`
  - `ads-test`
  - `ads-dna`
  - `ads-create`
  - `ads-generate`
  - `ads-photoshoot`

Arquivos principais:

- `/opt/data/profiles/lk-growth/skills/paid-media/ads/SKILL.md`
- `/opt/data/profiles/lk-growth/skills/paid-media/ads/references/`
- `/opt/data/profiles/lk-growth/skills/paid-media/ads/scripts/`
- `/opt/data/profiles/lk-growth/skills/paid-media/ads/references/hermes-lk-adaptation.md`

## Como usar no Hermes

1. Carregar `ads` como skill orquestradora.
2. Para trabalhos focados, carregar sub-skill específica:
   - Google Ads: `ads-google`
   - Meta Ads: `ads-meta`
   - Tracking/attribution: `ads-attribution` + `ads-server-side-tracking`
   - Criativos: `ads-creative`
   - Landing/PDP: `ads-landing`
   - Budget: `ads-budget`
3. Antes de auditoria ou plano, inferir ou coletar:
   - indústria/business type;
   - spend mensal e split por plataforma;
   - objetivo primário;
   - plataformas ativas;
   - janela analisada;
   - fonte dos dados.
4. Para `/ads audit`, usar `delegate_task` do Hermes no lugar dos Task agents do Claude Code. Os prompts originais de agentes foram copiados para `ads/references/agents/` como templates de contexto.

## Principais comandos/conceitos

- `/ads audit`: auditoria multi-plataforma com Ads Health Score 0-100.
- `/ads google`: Google Ads, Search, PMax, AI Max, Demand Gen, YouTube.
- `/ads meta`: Meta Ads no contexto Andromeda + GEM + Lattice; foco forte em diversidade criativa e CAPI/Pixel.
- `/ads attribution`: GA4, Consent Mode V2, AdAttributionKit, MMP, server-side stitching.
- `/ads tracking`: sGTM, CAPI Gateway, dedup, hashing, hit ratio.
- `/ads landing`: qualidade de landing/PDP para campanhas.
- `/ads budget`: alocação, bidding, pacing e suficiência de orçamento.
- `/ads creative`: fadiga, diversidade de conceitos, formatos e risco de clustering.
- `/ads math`: CPA, ROAS, break-even, budget forecasting, LTV:CAC.
- `/ads test`: hipótese, significância, amostra e duração de A/B test.

## Scoring

- Score 0-100 por plataforma.
- Grade:
  - A: 90-100
  - B: 75-89
  - C: 60-74
  - D: 40-59
  - F: <40
- Severidade:
  - Critical: multiplicador 5.0
  - High: 3.0
  - Medium: 1.5
  - Low: 0.5
- WARNING vale 50% do peso; N/A sai do denominador.

Pesos relevantes:

- Google: tracking 25%, wasted spend/negatives 20%, estrutura 15%, keywords/QS 15%, ads/assets 15%, settings 10%.
- Meta: Pixel/CAPI 30%, creative 30%, estrutura 20%, audience 20%.
- TikTok: creative 30%, technical setup 25%, bidding/learning 20%, structure/settings 15%, performance 10%.

## Quality gates que importam para LK

- Nunca recomendar Broad Match sem Smart Bidding.
- Nunca recomendar edição durante learning phase ativa.
- Tracking/privacy antes de otimização: Consent Mode V2, Pixel/CAPI, Enhanced Conversions, dedup.
- Meta: diversidade criativa agora é alavanca central; variações quase iguais podem cair em clustering/Andromeda retrieval suppression.
- Meta e TikTok exigem suficiência de orçamento por CPA para sair de learning.
- Negativas devem vir de Search Terms Report real, não de chute.
- Para e-commerce, conectar paid signals com PDP/collection, feed, catálogo, checkout e GA4/Shopify revenue.

## Guardrails LK

- Uso read-only por padrão.
- Nenhum write em campanhas, budget, criativos, audience, pixel, tracking, Klaviyo ou Shopify production sem aprovação explícita no turno.
- Recomendações devem virar decision packet: impacto, esforço, risco, rollback, aprovação necessária e janela de revisão.
- Paid media é contexto de demanda e gargalo comercial; não substitui Shopify/GA4/GSC/GMC como fonte de verdade de receita/conversão.
- Manter tom premium/minimal/humano e evitar taxonomia pública de pronta entrega/encomenda/estoque.

## Integrações de dados LK

Já disponíveis no ambiente Growth:

- Meta Ads API read-only: OK.
- GA4: OK.
- Shopify: OK.
- GSC/GMC: OK.
- PageSpeed/CrUX: OK.
- Klaviyo: OK.
- Ahrefs: OK.
- DataForSEO MCP: instalado/validado, requer reload/restart para toolset ativo.

Pendência possível:

- Google Ads API/MCP específico para pulling GAQL ainda não foi configurado nesta etapa. Claude Ads suporta manual exports ou MCP Google Ads; para LK, se necessário, configurar depois com token read-only/escopo mínimo.

## Observação de dependências

Scripts de PDF/landing/screenshot foram copiados. Dependências Python estão listadas em `ads/requirements.txt`. Não foram instaladas globalmente nesta etapa para evitar mutação ampla do runtime. Usar/instalar sob demanda em venv/perfil quando um fluxo exigir PDF/landing screenshot.
