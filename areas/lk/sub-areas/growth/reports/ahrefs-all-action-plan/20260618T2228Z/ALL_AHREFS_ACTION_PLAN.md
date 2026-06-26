# LK Ahrefs — plano ALL issues

Gerado UTC: `2026-06-18T22:30:16Z`
Base Ahrefs: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-full-audit/20260618T202702Z`

## Snapshot

- Issue types ativos: `27`
- Errors ativos: `7`
- Warnings ativos: `5`
- Notices ativos: `15`

## Top issue types por volume

- `10003` — notice / Other: **Structured data has schema.org validation error**
- `7829` — warning / Links: **Page has links to broken page**
- `2175` — notice / Other: **Pages to submit to IndexNow**
- `976` — notice / Other: **More than three parameters in URL**
- `631` — warning / Content: **Meta description too long**
- `530` — notice / Content: **Page and SERP titles do not match**
- `353` — warning / Content: **Title too long**
- `269` — notice / Content: **Title too long**
- `219` — error / Links: **Orphan page (has no incoming internal links)**
- `154` — notice / Content: **Meta description too long**
- `98` — error / Links: **Canonical URL has no incoming internal links**
- `78` — warning / Images: **Missing alt text**
- `53` — error / Images: **Page has broken image**
- `29` — error / Images: **Image file size too large**
- `19` — error / Internal pages: **404 page**

## Fila recomendada

### P0
- `7829` — **Page has links to broken page** — P0/P1: maioria são URLs de filtro/facetas; precisa pacote separado por template/filtros, não redirect em massa
- `53` — **Page has broken image** — P0 pós-fix parcial: Judge.me aplicado; imagens externas Nike/Sneakerbar ainda pendentes
- `19` — **404 page** — P0 pós-fix: redirects/conteúdo aplicados; esperar recrawl/cache para limpar remanescentes
- `19` — **4XX page** — P0 pós-fix: redirects/conteúdo aplicados; esperar recrawl/cache para limpar remanescentes
- `7` — **Image broken** — P0 pós-fix parcial: Judge.me aplicado; imagens externas Nike/Sneakerbar ainda pendentes

### P1
- `10003` — **Structured data has schema.org validation error** — P1/P2 schema: validar amostras e corrigir template se real
- `976` — **More than three parameters in URL** — P1 técnico: facetas/filtros; avaliar canonicals/robots/internal links
- `219` — **Orphan page (has no incoming internal links)** — P1: arquitetura/linkagem interna; priorizar páginas comerciais indexáveis
- `98` — **Canonical URL has no incoming internal links** — P1: arquitetura/linkagem interna; priorizar páginas comerciais indexáveis
- `29` — **Image file size too large** — P1: performance/imagens; otimizar top templates/assets por impacto

### P2
- `631` — **Meta description too long** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `353` — **Title too long** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `269` — **Title too long** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `154` — **Meta description too long** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `78` — **Missing alt text** — P2: acessibilidade/imagem; resolver por template/metafield quando escalável
- `15` — **External 4XX** — P2: links externos; trocar/remover referências quebradas/redirect
- `14` — **Meta description too short** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `13` — **Meta description too short** — P2: higiene on-page; aplicar só em páginas com demanda/GSC
- `6` — **External 3XX redirect** — P2: links externos; trocar/remover referências quebradas/redirect

### P3
- `2175` — **Pages to submit to IndexNow** — P3/monitorar ou tratar em lote futuro
- `530` — **Page and SERP titles do not match** — P3/monitoramento: não mexer sem queda GSC/conversão
- `14` — **Multiple H1 tags** — P3/monitoramento: não mexer sem queda GSC/conversão
- `9` — **Pages have high AI content levels** — P3/monitorar ou tratar em lote futuro
- `1` — **H1 tag changed** — P3/monitoramento: não mexer sem queda GSC/conversão
- `1` — **Meta description changed** — P3/monitoramento: não mexer sem queda GSC/conversão
- `1` — **Title tag changed** — P3/monitoramento: não mexer sem queda GSC/conversão

### Monitorar
- `1` — **Robots.txt rules disallow to crawl** — Monitorar: verificar se é regra intencional Shopify

## Arquivos

- Matrix CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-all-action-plan/20260618T2228Z/all-ahrefs-issue-action-matrix.csv`
- Samples JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-all-action-plan/20260618T2228Z/page-explorer-samples.json`