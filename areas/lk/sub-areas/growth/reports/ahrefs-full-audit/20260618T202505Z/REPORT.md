# Ahrefs Full Audit — LK Sneakers

- Generated UTC: 2026-06-18 20:25:12
- Project: Lksneakers
- Project ID: `9609836`
- Target: `lksneakers.com.br/`
- Last crawl/status: `2026-06-18T19:46:19Z` / `Completed`
- Health Score: **93**
- URLs crawled/total reported: **34329**
- URLs with errors: **2241**
- URLs with warnings: **10047**
- URLs with notices: **10011**
- Fonte: Ahrefs Site Audit API v3 via Doppler; values_printed=false
- Escopo: read-only; nenhuma alteração externa executada

## Veredito executivo

O audit está **correto e acionável**: a LK tem health score alto, mas há problemas técnicos concentrados em links quebrados/4XX, imagens quebradas ou pesadas, canonical/orphan/internal linking e hygiene on-page. A prioridade comercial deve ser corrigir primeiro o que afeta crawl, UX mobile e confiança de PDP/collection.

## Prioridades recomendadas

### P0 — Broken links / 404 / 4XX
- Evidência: 12 issue types; soma reportada: 0
- Por quê: Impacta rastreamento, UX e pode enviar usuário para páginas mortas.
  - `c64d3b5a-d0f4-11e7-8ed1-001e67ed4656` — 4XX page receives organic traffic | error | count 0
  - `c0e87084-feaf-11e8-8c05-001e67ed4657` — Image broken | error | count 0
  - `34412dfa-feb0-11e8-a306-001e67ed4657` — Page has broken image | error | count 0
  - `c64d8074-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to 4XX | error | count 0
  - `c64dae3f-d0f4-11e7-8ed1-001e67ed4656` — 404 page | error | count 0

### P0 — Broken images
- Evidência: 2 issue types; soma reportada: 0
- Por quê: Afeta confiança visual e conversão em PDP/collection; há sinais de bug de renderização Judge.me/template.
  - `c0e87084-feaf-11e8-8c05-001e67ed4657` — Image broken | error | count 0
  - `34412dfa-feb0-11e8-a306-001e67ed4657` — Page has broken image | error | count 0

### P1 — Canonical/orphan/indexability
- Evidência: 19 issue types; soma reportada: 0
- Por quê: Evita desperdício de crawl budget e consolida sinais de páginas comerciais.
  - `c64d5626-d0f4-11e7-8ed1-001e67ed4656` — Duplicate pages without canonical | error | count 0
  - `c64d84df-d0f4-11e7-8ed1-001e67ed4656` — Noindex page receives organic traffic | error | count 0
  - `c64d8074-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to 4XX | error | count 0
  - `c64d79e8-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to 5XX | error | count 0
  - `c64d54e6-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to redirect | error | count 0

### P1 — Imagens grandes/performance
- Evidência: 1 issue types; soma reportada: 0
- Por quê: Ganho provável em mobile/CWV e percepção premium.
  - `c64d8113-d0f4-11e7-8ed1-001e67ed4656` — Image file size too large | error | count 0

### P2 — Metadata/duplicatas/H1
- Evidência: 26 issue types; soma reportada: 0
- Por quê: Higiene SEO para CTR e legibilidade de coleção/PDP.
  - `c64d5626-d0f4-11e7-8ed1-001e67ed4656` — Duplicate pages without canonical | error | count 0
  - `c64d7795-d0f4-11e7-8ed1-001e67ed4656` — Multiple meta description tags | error | count 0
  - `c64d81a5-d0f4-11e7-8ed1-001e67ed4656` — Multiple title tags | error | count 0
  - `c64d7840-d0f4-11e7-8ed1-001e67ed4656` — Title tag missing or empty | error | count 0
  - `c64d9d0b-d0f4-11e7-8ed1-001e67ed4656` — H1 tag missing or empty | warning | count 0

## Top 40 issues por severidade/volume

- `c64d5626-d0f4-11e7-8ed1-001e67ed4656` — Duplicate pages without canonical | severity: error | count: 0 | counts: `{}`
- `c64d34be-d0f4-11e7-8ed1-001e67ed4656` — 3XX page receives organic traffic | severity: error | count: 0 | counts: `{}`
- `c64d558c-d0f4-11e7-8ed1-001e67ed4656` — 403 page receives organic traffic | severity: error | count: 0 | counts: `{}`
- `c64d3b5a-d0f4-11e7-8ed1-001e67ed4656` — 4XX page receives organic traffic | severity: error | count: 0 | counts: `{}`
- `c64d3a17-d0f4-11e7-8ed1-001e67ed4656` — Double slash in URL | severity: error | count: 0 | counts: `{}`
- `c64d84df-d0f4-11e7-8ed1-001e67ed4656` — Noindex page receives organic traffic | severity: error | count: 0 | counts: `{}`
- `9111b6c4-198e-401d-a91e-156f97f83d59` — Robots.txt has syntax error | severity: error | count: 0 | counts: `{}`
- `1f27ccb2-ebfe-4941-af1e-972a56cd6ed5` — Robots.txt has too many redirects or redirect loop | severity: error | count: 0 | counts: `{}`
- `91326507-26f0-4b4b-a680-bfdff5dd74c7` — Robots.txt is not accessible | severity: error | count: 0 | counts: `{}`
- `c64d7795-d0f4-11e7-8ed1-001e67ed4656` — Multiple meta description tags | severity: error | count: 0 | counts: `{}`
- `c64d81a5-d0f4-11e7-8ed1-001e67ed4656` — Multiple title tags | severity: error | count: 0 | counts: `{}`
- `c64d7840-d0f4-11e7-8ed1-001e67ed4656` — Title tag missing or empty | severity: error | count: 0 | counts: `{}`
- `c0e87084-feaf-11e8-8c05-001e67ed4657` — Image broken | severity: error | count: 0 | counts: `{}`
- `c64d8113-d0f4-11e7-8ed1-001e67ed4656` — Image file size too large | severity: error | count: 0 | counts: `{}`
- `34412dfa-feb0-11e8-a306-001e67ed4657` — Page has broken image | severity: error | count: 0 | counts: `{}`
- `c64d8074-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to 4XX | severity: error | count: 0 | counts: `{}`
- `c64d79e8-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to 5XX | severity: error | count: 0 | counts: `{}`
- `c64d54e6-d0f4-11e7-8ed1-001e67ed4656` — Canonical points to redirect | severity: error | count: 0 | counts: `{}`
- `910e33d1-443b-4606-b950-deb7c659510f` — Page size exceeds Googlebot's 2 MB crawl limit | severity: error | count: 0 | counts: `{}`
- `c64dae3f-d0f4-11e7-8ed1-001e67ed4656` — 404 page | severity: error | count: 0 | counts: `{}`
- `c64da643-d0f4-11e7-8ed1-001e67ed4656` — 4XX page | severity: error | count: 0 | counts: `{}`
- `c64d40b0-d0f4-11e7-8ed1-001e67ed4656` — 500 page | severity: error | count: 0 | counts: `{}`
- `c64d38a1-d0f4-11e7-8ed1-001e67ed4656` — 5XX page | severity: error | count: 0 | counts: `{}`
- `c64d3811-d0f4-11e7-8ed1-001e67ed4656` — Timed out | severity: error | count: 0 | counts: `{}`
- `c64dab77-d0f4-11e7-8ed1-001e67ed4656` — JavaScript broken | severity: error | count: 0 | counts: `{}`
- `56c9d152-feb4-11e8-b65d-001e67ed4657` — Page has broken JavaScript | severity: error | count: 0 | counts: `{}`
- `c64d3d21-d0f4-11e7-8ed1-001e67ed4656` — Canonical URL has no incoming internal links | severity: error | count: 0 | counts: `{}`
- `c64d82d6-d0f4-11e7-8ed1-001e67ed4656` — HTTPS page has internal links to HTTP | severity: error | count: 0 | counts: `{}`
- `c64d7e96-d0f4-11e7-8ed1-001e67ed4656` — Orphan page (has no incoming internal links) | severity: error | count: 0 | counts: `{}`
- `c64d358b-d0f4-11e7-8ed1-001e67ed4656` — CSS broken | severity: warning | count: 0 | counts: `{}`
- `c64d859f-d0f4-11e7-8ed1-001e67ed4656` — CSS file size too large | severity: warning | count: 0 | counts: `{}`
- `18babe02-feb5-11e8-b126-001e67ed4657` — CSS redirects | severity: warning | count: 0 | counts: `{}`
- `7945ee9a-feb5-11e8-9c77-001e67ed4657` — HTTPS page links to HTTP CSS | severity: warning | count: 0 | counts: `{}`
- `3a68909c-feb5-11e8-a4c3-001e67ed4657` — Page has broken CSS | severity: warning | count: 0 | counts: `{}`
- `5b4053a4-feb5-11e8-a8ae-001e67ed4657` — Page has redirected CSS | severity: warning | count: 0 | counts: `{}`
- `8ca9e4b6-2258-4a46-ba98-66f008848db1` — Robots.txt changed | severity: warning | count: 0 | counts: `{}`
- `c64d9d0b-d0f4-11e7-8ed1-001e67ed4656` — H1 tag missing or empty | severity: warning | count: 0 | counts: `{}`
- `c64da01e-d0f4-11e7-8ed1-001e67ed4656` — Low word count | severity: warning | count: 0 | counts: `{}`
- `57751310-001c-11e8-b746-001e67ed4656` — Meta description tag missing or empty | severity: warning | count: 0 | counts: `{}`
- `c64d31f0-d0f4-11e7-8ed1-001e67ed4656` — Meta description tag missing or empty | severity: warning | count: 0 | counts: `{}`

## Amostras por issue selecionada

## Pacote de decisão / execução

### Pode fazer sem aprovação
- Continuar diagnóstico read-only; agrupar URLs por template/collection/PDP; preparar diff/preview em dev theme; preparar lista de redirects proposta.

### Exige aprovação explícita
- Criar/editar redirects Shopify em produção.
- Alterar theme production, snippets Judge.me, links em menus/collections/PDPs ou conteúdo visível.
- Alterar apps, feed GMC ou Merchant Center.

### Rollback sugerido
- Redirects: exportar lista antes/depois; reversão via remoção em lote.
- Theme: trabalhar em dev theme; rollback por theme preview/duplicated theme.
- Conteúdo/meta: export antes/depois + revisão de impacto em ~7 dias.

## Arquivos de evidência
- Pasta: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-full-audit/20260618T202505Z`
- `issues-summary.csv`
- `issues-normalized.json`
- `selected-page-explorer-details.json`
- `page-explorer-*.csv/json`
- `api-log.json` com status HTTP e sem token
