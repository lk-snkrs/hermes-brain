# Audit — LK Growth OS crons + tooling coverage

Data UTC: 2026-06-03T15:19:44.702547+00:00
Status: read-only audit
Writes externos: não
Arquivos de cron alterados: não

## Pergunta

Verificar se os crons da Agenda v2 estão suficientemente documentados para usar ao máximo as ferramentas disponíveis: Shopify, GA4/Google Analytics, GSC, GMC, Klaviyo/CRM, DataForSEO, Ahrefs/backlinks, Google/Metricool/Meta Ads, PageSpeed/CrUX/CWV, schema/GEO e a camada Claude-SEO.

## Evidências verificadas

- Cron real: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Docs canônicos: `ESCOPO-18-TOPICOS.md`, `HEARTBEAT.md`, `IMPACT-REVIEWS.md`.
- Approval packet Agenda v2: `approval-packets/lk-growth-cron-agenda-v2-20260603.md`.
- Skill importada: `skills/content-seo/README.md` com fontes `claude-seo` e `claude-blog`.
- Skill Google/Claude SEO: `skills/content-seo/seo/scripts/google_auth.py --check --json`.
- MCPs testados em read-only: DataForSEO, Metricool brand profile, Meta ad accounts.

## Disponibilidade real de ferramentas

### Disponíveis / confirmadas

- Claude-SEO camada `seo`: operacional.
- Google Search Console via service account: disponível.
- GA4 Data API via service account: disponível.
- Google Indexing API: disponível, mas write-like; usar só com aprovação quando submissão alterar estado.
- DataForSEO MCP: disponível e retornou dados de keyword overview Brasil.
- Metricool read-only: disponível para LK Sneakers; inclui conectores Meta Ads, Google Ads, GMB, Instagram etc.
- Meta Ads read-only: disponível; existe conta ativa LK.Sneakers.
- Shopify: há histórico/scripts/receipts; usar como fonte de verdade quando credencial/rotina local estiver ativa. Writes exigem aprovação.
- GMC/Simprosys: há rotina e cron dedicado; writes/feed exigem aprovação.

### Parcial / precisa hardening

- PageSpeed/CrUX: skill `seo` reportou sem API key para PSI/CrUX. O pacote `blog-google` tentou criar `.venv` e falhou por ausência de `python3.13-venv`. Portanto, CWV/PageSpeed está documentado nos crons, mas a execução automática pode cair para público/sem dados ou depender de outro caminho.
- Ahrefs: a skill cita Ahrefs/backlinks em referências, mas não há conector Ahrefs autenticado confirmado. Há scripts para Moz/DataForSEO/CommonCrawl/backlinks. Melhor documentar como “backlinks/off-site via DataForSEO/Moz/CommonCrawl quando disponível”, não como Ahrefs garantido.
- Klaviyo analytics: há histórico/receipts e guardrails, mas não identifiquei ferramenta read-only canônica explícita no cron para métricas Klaviyo. Deve entrar como sinal CRM quando houver conector/script autorizado; disparos continuam proibidos sem aprovação.
- Google Ads direto: Metricool tem adwords associado e há Google Ads Keyword Planner no Claude-SEO, mas Ads campaign analytics no cron deve usar Metricool read-only quando disponível.

## Avaliação dos crons Agenda v2

### Segunda — LK Growth Weekly Command Center

Status: bom como visão executiva, mas pode ficar mais decision-grade.

Cobertura atual:
- Cita Shopify/GA4, GSC, GMC, PageSpeed/CrUX, SERP, Brain, paid/influencer/CRM.
- Exige top 5 e 18 tópicos.

Gap:
- Não nomeia explicitamente os conectores MCP disponíveis: DataForSEO, Metricool, Meta Ads read-only.
- Não exige bloco “fontes consultadas vs indisponíveis”.
- Não exige reconciliação Shopify ↔ GA4 ↔ paid/CRM quando houver divergência.

Ajuste recomendado:
- Incluir checklist de fontes por prioridade: Shopify/GA4/GSC/GMC primeiro; DataForSEO/SERP/Metricool/Meta/Klaviyo como contexto; diagnóstico público por último.

### Terça — SEO/GSC + GEO Opportunities Review

Status: bom, mas subaproveita DataForSEO e Claude-SEO.

Cobertura atual:
- GSC, SERP/PAA, concorrência, GEO, llms/agents, FAQ/schema.

Gap:
- Não obriga uso da camada Claude-SEO/FLOW quando houver URL/oportunidade relevante.
- Não menciona DataForSEO como fonte de volume, SERP, competidores, LLM mentions e keyword intent.
- Não exige output de “query → URL → ação → métrica esperada”.

Ajuste recomendado:
- Adicionar: usar Claude-SEO `seo`/`blog-google` quando aplicável; usar DataForSEO para volume, SERP, competidores e AI/LLM visibility; comparar com GSC antes de recomendar write.

### Quarta — CRO/PDP Funnel Review

Status: bom na priorização, mas precisa explicitar Shopify/GA4/Klaviyo/Meta/Metricool.

Cobertura atual:
- PDP mobile, checkout/funil, collections → PDP, reviews, PageSpeed/CWV, eventos.

Gap:
- Não instrui a cruzar GA4 funnel com Shopify orders/revenue.
- Não explicita Klaviyo analytics como sinal de abandono, flows, campanhas e intenção de compra.
- Não cita paid/influencer demand: Meta/Metricool pode indicar produto com tráfego pago e PDP travando.

Ajuste recomendado:
- Incluir matriz: tráfego pago/CRM/social → landing/PDP → add-to-cart → checkout → order/revenue. Se dados faltarem, marcar não decision-grade.

### Quinta — GMC/Product Data + Local Inventory

Status: forte.

Cobertura atual:
- GMC issues, GTIN/MPN/brand/condition/images/titles/variantes, Shopify↔GMC, Simprosys, LIA_, GBP store_code, supplemental feed, schema Product/Offer.

Gap:
- Não cita DataForSEO Merchant/SERP shopping como validação de competição/merchant listing.
- Não separa “health feed” de “oportunidade comercial de product data”.

Ajuste recomendado:
- Adicionar DataForSEO Merchant/SERP quando relevante e bloco de impacto comercial por SKU/coleção.

### Sexta — Experiment Ledger + Impact Review

Status: bom.

Cobertura atual:
- Receipts, mudanças 7–14 dias, GSC/GA4/Shopify/GMC/PageSpeed, classificação, handoff LKGOC.

Gap:
- Não exige Klaviyo/paid/context em mudanças que receberam campanha ou social push.
- Não exige “fonte indisponível” para cada experimento.

Ajuste recomendado:
- Para cada experimento: fontes verificadas, fontes ausentes, confidence score, próxima decisão.

### Sábado — Storefront QA Light Monitor

Status: adequado como monitor leve.

Gap:
- Não deve virar auditoria pesada. Está correto ficar local/anomalia.
- Pode incluir checagem leve de schema JSON-LD e llms/agents, sem ferramentas autenticadas.

## Veredito

A Agenda v2 está correta estruturalmente, mas ainda está documentada como “intenção de cobertura”. Para extrair o máximo, os prompts dos crons precisam ficar mais operacionais: quais fontes usar, em que ordem, como declarar indisponibilidade e quando chamar Claude-SEO/DataForSEO/Metricool/Meta/Klaviyo.

## Recomendação P0 — patch local nos prompts dos crons

Sem write externo, ajustar apenas `/opt/data/profiles/lk-growth/cron/jobs.json` com backup para inserir:

1. Bloco obrigatório “Fontes e ferramentas”.
2. Uso explícito de Claude-SEO no SEO/GEO e no Weekly.
3. DataForSEO em SEO/GEO e GMC/comparativo SERP.
4. Metricool/Meta Ads como paid/influencer context no Weekly/CRO.
5. Klaviyo analytics como CRM signal no Weekly/CRO/Impact Review quando conector/script estiver disponível.
6. Bloco “decision-grade”: fontes verificadas, ausentes e confiança.
7. Guardrail reforçado: Indexing API, GMC, Shopify, Klaviyo, Ads e production writes só com aprovação.

## Risco

Baixo. Mudança seria só local em prompts de cron. Não altera Shopify/GMC/Ads/Klaviyo/GA4. Precisa backup e receipt.

## Rollback

Restaurar backup de `jobs.json` anterior ao patch.

## Status de aprovação

A auditoria foi executada. Para aplicar o patch nos prompts reais, precisa confirmação do Lucas: “aprovo patch dos prompts”.
