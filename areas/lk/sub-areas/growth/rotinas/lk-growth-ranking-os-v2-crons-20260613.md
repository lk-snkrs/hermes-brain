# LK Growth Ranking OS v2 — crons segunda a sábado

Data: 2026-06-13
Status: aprovado por Lucas no Telegram e aplicado localmente em `/opt/data/profiles/lk-growth/cron/jobs.json`.
Backup: `/opt/data/profiles/lk-growth/cron/jobs.json.bak_lk_growth_ranking_os_v2_20260613T213750Z`.

## North Star

Melhorar ranking e visibilidade qualificada da LK Sneakers no Google e nas LLMs, com impacto comercial.

## Goals

### 30 dias
- Manter lista viva das 20 páginas prioritárias da LK: collections, PDPs, guias e páginas citáveis.
- Gerar pelo menos 1 oportunidade acionável por dia útil de Growth.
- Otimizar ou preparar approval packet para 4 collections/PDPs, 4 oportunidades Google/GSC e 4 oportunidades GEO/LLM.
- Manter ranking/experiment ledger com query, URL, hipótese, métrica e impacto.

### 60 dias
- Melhorar CTR de páginas com alta impressão e baixa CTR.
- Levar páginas em posição 8–20 para Top 10 quando houver fit de intenção.
- Consolidar clusters prioritários: New Balance, Onitsuka Tiger, Adidas Samba/Jane, Puma Speedcat, Nike/Jacquemus/Moon Shoe e sneakers premium/originais no Brasil.

### 90 dias
- Aumentar cliques orgânicos qualificados, Top 10/Top 5/Top 3, AI mentions/citations e contribuição orgânica para sessões/conversão/receita.

## Grade semanal v2

- Segunda 08:30 BRT — `LK Ranking Command Center`
  - Escolhe Top 5 oportunidades e 1–3 páginas foco da semana.

- Terça 08:30 BRT — `LK Google SEO Opportunity Factory`
  - Transforma GSC/SERP em 1 approval packet Google SEO: title/meta/H1/copy/FAQ/schema/internal links.

- Quarta 08:30 BRT — `LK Collection/PDP Optimization Factory`
  - Melhora uma página comercial por semana com SEO + CRO + GEO; LKGOC obrigatório para collections.

- Quinta 08:30 BRT — `LK Merchant/Product Data Ranking Review`
  - Usa Merchant/product data/schema para elegibilidade, Shopping visibility e qualidade comercial.

- Sexta 08:30 BRT — `LK GEO/LLM Citation Factory`
  - Gera oportunidade de citação em ChatGPT, Perplexity, Gemini, AI Overviews: bloco answer-first, FAQ, schema, entity clarity.

- Sábado 08:30 BRT — `LK QA + Impact Review Saturday`
  - QA técnico leve + leitura de impacto 7/14 dias. Silent se OK sem aprendizado material.

## Monitores mantidos

- `LK AI/GEO Endpoints Monitor`: diário 06:10 e 14:10 BRT.
- `LK Growth Cron Delivery Watchdog`: diário 18:00 BRT.
- `LK Growth D+14 impact review — product operational copy cleanup`: pontual em 2026-06-19 16:00 BRT.

## Guardrails

- Read-only/preview por padrão.
- Claude SEO obrigatório como camada diagnóstica quando aplicável: `seo`, `seo-google`, `seo-page`, `seo-content`, `seo-sxo`, `seo-schema`, `seo-ecommerce`, `seo-geo`, `seo-dataforseo`.
- Dados comerciais/demanda vencem HTML público: Shopify/GA4/GSC/GMC/DataForSEO/SERP quando disponíveis.
- Sem writes externos sem aprovação explícita atual.
- Estoque/disponibilidade operacional pertence ao `lk-stock`.
- Linguagem premium LK; não usar pronta entrega/encomenda/estoque como taxonomia pública.

## Rollback

Restaurar backup:

```bash
cp /opt/data/profiles/lk-growth/cron/jobs.json.bak_lk_growth_ranking_os_v2_20260613T213750Z /opt/data/profiles/lk-growth/cron/jobs.json
```

## Reminder OS

Reminder OS loop needed: yes.
Reminder OS owner: LK Growth / profile lk-growth.
Reminder OS next action: retomar o Growth Ranking OS v2 pelo último output dos crons, verificar oportunidade acionável/approval packet pendente e continuar do ponto parado quando Lucas pedir “continuar/retomar/onde paramos”.
Reminder OS review trigger: após o Ranking Command Center de segunda ou quando Lucas pedir retomada do Growth Ranking OS.
Reminder OS evidence: este documento + `/opt/data/profiles/lk-growth/cron/jobs.json` + `areas/operacoes/reminder-os/reminders.jsonl` id `rem-lk-growth-ranking-os-v2-continuity-20260613`.
Status: active.
Motivo: além do cron/watchdog, Lucas quer continuidade operacional para trabalhos interrompidos e retomada sem depender do histórico do chat.
