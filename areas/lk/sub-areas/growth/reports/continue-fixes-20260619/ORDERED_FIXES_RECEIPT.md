# LK Growth — Ordered SEMrush fixes receipt — 2026-06-19

- Escopo aprovado por Lucas: fazer todos na ordem recomendada.
- Writes executados: Shopify dev theme + production theme/page template/llms assets; SEMrush crawl launch nos 2 projetos.
- values_printed=false; estoque não consultado; nenhum write em GMC/GA4/GSC/ads/Klaviyo.

## 1. /llms.txt normalizado

- `templates/llms.txt.liquid` reescrito em formato llms.txt limpo.
- H1 único, seções claras, regras de IA e source pages prioritárias.
- Verificação pública: status `200`, h1_count `1`, old_v7_h1 `False`.

## 2. Links sem anchor text — filtros de cor

- Corrigido `sections/lk-collection.liquid` em dev e production.
- Color chips agora têm `aria-label` e texto screen-reader (`span.flt-sr`).
- Verificação collections Adidas Campus/Japan: empty=0.
- Verificação collection Sneakers estabilizou no poll: `{'i': 2, 'status': 200, 'empty': 0, 'chips': 32, 'chips_aria': 32, 'chips_text': 32, 'sample': '<a aria-label="Filtrar por cor Amarela (15)" class="flt-color-chip is-dark" href="/collections/sneakers?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F14" style="background-col'}`

## 3. Guia Salomon XT-6 — links externos

- Corrigido `templates/page.guia-salomon-xt6-lkgoc.json` em dev e production.
- Hypebeast search substituído por source interna `Blog LK`.
- Salomon root `/` substituído por `/en-us` para evitar redirect/root issue.
- Verificação pública final: `{'i': 4, 'status': 200, 'hype_exact': False, 'salomon_root_exact': False, 'external': ['https://wa.me/5511949565000', 'https://www.salomon.com/en-us', 'https://www.highsnobiety.com/search/?q=salomon%20xt-6', 'https://www.vogue.com/search?q=salomon%20sneakers', 'https://lksneakers.troquefacil.com.br']}`

## 4. WhatsApp 429

- Mantido como falso positivo monitorado/rate-limit de terceiro.
- Não alterado porque valida publicamente para usuário e mexer nos CTAs teria risco comercial desnecessário.

## 5. SEMrush recrawl

- Launch executado para os 2 projetos SEMrush.
- Project `16150947` launch HTTP `200` response `{ "snapshot_id": "6a355ce25b22e6773399a3dd"}`
- Project `29110159` launch HTTP `200` response `{ "snapshot_id": "6a355ce3f24f0f526db9f2e6"}`
- Crawl segue assíncrono; poll em background salvando `semrush-postfix-poll-final.json` e `SEMRUSH_POSTFIX_POLL.md`.

## Rollback

- Rollback JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/continue-fixes-20260619/rollback-before-all-ordered-fixes.json`
- Execution receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/continue-fixes-20260619/execution-receipt.json`
- Public verify JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/continue-fixes-20260619/post-execution-public-verify.json`
- SEMrush launch receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/continue-fixes-20260619/semrush-launch-receipt.json`
