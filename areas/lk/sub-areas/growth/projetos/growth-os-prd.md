# PRD — LK Growth OS

## Problema

As conversas de SEO, GMC, CRO, GA4, GSC, GEO e Shopify ficam misturadas com LK OS, Mission Control, Mordomo, Zipper, SPITI e infra. Isso cria perda de contexto, dificuldade de retomada e risco de priorização errada.

## Solução

Criar um agente/perfil especialista: **LK Growth OS**, com bot Telegram próprio, Brain/subárea própria e permissões limitadas.

## Produto

Agente especialista que transforma dados read-only em pacotes de decisão para Lucas:

Escopo canônico completo em `../ESCOPO-18-TOPICOS.md`, com 18 tópicos:

1. GA4/Analytics;
2. Google Search Console;
3. Google Merchant Center;
4. Shopify SEO técnico/on-page;
5. Shopify CRO/dev theme;
6. GEO/AI Search;
7. PageSpeed/CrUX/Core Web Vitals;
8. schema/structured data;
9. reviews/prova social;
10. paid media signals;
11. influencer/social demand signals;
12. concorrência/SERP;
13. Google Business/local SEO quando aplicável;
14. Klaviyo/CRM signals;
15. catálogo/product data quality;
16. conteúdo e taxonomia comercial;
17. mensuração e QA de eventos;
18. impact review/experimentation.

## Fase 1 — Feita

- Perfil Hermes `lk-growth` criado.
- Bot Telegram `LKGrowth_HermesBot` validado.
- Token salvo no Doppler como `TELEGRAM_LK_GROWTH_BOT_TOKEN`.
- Gateway secundário iniciado.
- Identidade inicial e Brain/subárea documentados.
- Checklist canônico de 18 tópicos criado em `ESCOPO-18-TOPICOS.md` e referenciado no `MAPA.md`.

## Fase 2 — Em andamento / parcialmente feita

Feito:

- Cron migration map criado em `../CRONS-MIGRATION.md`.
- Weekly Growth Review migrado para o profile `lk-growth` como job `738d3deabaeb`.
- GMC Review read-only migrado para o profile `lk-growth` como job `1240644c5f3f`.
- Jobs antigos equivalentes no Hermes principal pausados para evitar duplicidade: `15777e3416dc` e `d4c26da4cd48`.
- Canal validado por Lucas.
- Inventário read-only de conectores criado em `../CONNECTORS-READONLY-INVENTORY.md`:
  - Shopify Admin OK;
  - GSC OK;
  - GMC OK;
  - GA4 parcial: `GOOGLE_ANALYTICS_PROPERTY_ID` OK; `GA4_LK_PROPERTY_ID`/`GA4_PROPERTY_ID` com HTTP 403 nas service accounts atuais;
  - PageSpeed/CrUX bloqueado no teste atual por quota/API (`429`/`403`);
  - Klaviyo e Meta/Paid inventariados, pendentes de validação read-only.
- Política de impact reviews criada em `../IMPACT-REVIEWS.md`.
- Impact review SEO title/meta P1 migrado para o profile `lk-growth`:
  - antigo `a7e883edd200` pausado no Hermes principal;
  - novo `c45cda5fe2df` ativo no `lk-growth`, entrega `telegram`, schedule `2026-05-25T14:34:23Z`.

Pendente operacional:

- Validar primeira entrega real dos crons no canal definitivo.
- Resolver permissão GA4 da property LK atual.
- Definir API/caching para PSI/CrUX recorrente.
- Validar Klaviyo e Meta read-only.
- Criar primeiro Weekly Growth Review decision-grade dentro do novo canal.

## Fase 3 — Depois

- Ligar Approval Packets ao Mission Control.
- Converter próximos 7-day impact reviews para nascerem no `lk-growth`.
- Criar automações adicionais apenas após cadência aprovada e com rollback documentado.

## PRD de ação comercial

A execução prática do Growth OS passa a ser detalhada em `growth-action-prd-2026-05-19.md`, com prioridade explícita para vender mais, converter mais e gerar mais receita. Esse PRD define cadência por dia da semana, scoring P0/P1/P2, backlog inicial, roadmap de 90 dias e impact review D+7.

## Guardrails

Sem writes externos automáticos. Qualquer Shopify/GMC/theme/campanha/email/WhatsApp/produção exige aprovação explícita atual de Lucas.
