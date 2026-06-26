# LK Sneakers — Claude-SEO Ecommerce Audit

Data: 2026-06-06/07 UTC  
Escopo: auditoria SEO ecommerce Shopify usando playbook Claude-SEO (`seo-audit`, `seo-ecommerce`, `seo-google`, `seo-geo`) com checks públicos + GSC/GA4 read-only quando disponível.  
Status: decision-grade para SEO/GEO/on-page; performance CWV parcialmente limitada porque PageSpeed/CrUX API retornou rate limit/sem API key no check local.

## Nota geral

- **SEO Health Score:** **77/100 — B**
- **Business type detectado:** ecommerce Shopify premium / sneaker boutique com loja física e compra assistida.

## Notas por categoria — pesos Claude-SEO

- **Technical SEO:** 80/100
- **Content Quality:** 76/100
- **On-page SEO:** 74/100
- **Schema / Structured Data:** 84/100
- **Performance / CWV direcional:** 55/100
- **AI Search / GEO:** 92/100
- **Images:** 90/100

Cálculo ponderado Claude-SEO: 77.48/100.

## Fontes verificadas

- `fetch_page.py` + `parse_html.py` na Home.
- `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `agents.md`, `.well-known/ucp`.
- Sitemap crawl: 5 sitemaps, 2.122 URLs descobertas.
- Crawl amostral: 260 URLs, incluindo home, collections, pages e PDPs.
- GSC 28 dias: páginas e query/page.
- GA4 28 dias: organic + top landing pages.
- Playwright mobile direcional: home, coleção NB 204L, PDP Onitsuka Kill Bill.
- DataForSEO SERP branded/site query.

## Fatos principais

### O que está forte

1. **Base técnica Shopify saudável**
   - Home HTTP 200, canonical presente, sitemap ativo e atualizado.
   - `robots.txt` permite produtos, coleções, blogs e sitemap para Googlebot.
   - Segurança básica OK: HSTS, CSP, X-Frame-Options, X-Content-Type-Options.

2. **GEO / AI visibility está acima da média**
   - `llms.txt`: 48.541 chars, atualizado em 2026-06-05.
   - `llms-full.txt`: 120.042 chars.
   - `agents.md`: 8.222 chars com contexto comercial, páginas prioritárias, instruções para agentes e UCP.
   - `.well-known/ucp`: HTTP 200 JSON.
   - `robots.txt` libera GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, OAI-SearchBot e Google-Extended.

3. **Schema ecommerce bom nas páginas prioritárias**
   - PDP amostrada contém `Product`, `Offer`, `Brand`, `FAQPage`, `BreadcrumbList`, `Organization` e políticas de shipping/return.
   - Coleções aparecem com `CollectionPage` e `ItemList` em várias páginas.
   - FAQPage presente em páginas editoriais/guia.

4. **Demanda orgânica real já existe**
   - GA4 organic 28d: 15.079 sessões, 14.049 usuários, 28.031 pageviews.
   - GSC top pages 28d:
     - Onitsuka todos os modelos: 768 cliques / 54.859 impressões / CTR 1,40% / pos. 6,8.
     - Lululemon: 691 cliques / 25.509 impressões / CTR 2,71% / pos. 5,0.
     - Home: 404 cliques / 31.719 impressões / CTR 1,27% / pos. 7,6.
     - Onitsuka Mexico 66: 394 cliques / 18.854 impressões / CTR 2,09% / pos. 4,0.
     - Air Jordan Travis Scott: 220 cliques / 26.759 impressões / CTR 0,82% / pos. 6,4.
     - New Balance 204L: 185 cliques / 23.543 impressões / CTR 0,79% / pos. 8,4.

5. **Imagens com alt text estão boas na amostra**
   - Crawl amostral: 3.381 imagens, 0 alt missing detectado nas páginas 200.

## Principais problemas

### P1 — Performance/mobile e excesso de scripts

Playwright mobile direcional:

- Home: 271 requests, 85 scripts, timeout em `networkidle`; DCL 4.188ms, load 4.784ms.
- Collection NB 204L: 282 requests, 87 scripts, timeout em `networkidle`; DCL 2.328ms, load 4.226ms.
- PDP Onitsuka Kill Bill: 319 requests, 92 scripts, timeout em `networkidle`; DCL 2.232ms, load 4.546ms.

Erros/avisos recorrentes:

- CORS em `recovery.lucascimino.com/links/whatsapp/mint`.
- CORS em `n8n.lucascimino.com/webhook/lk-cart-intent-v1`.
- `[ET] tracker not configured`.
- PDP: Judge.me com warning de `missing jdgm key`.

Impacto provável: CWV, INP, carregamento percebido e confiança/reviews em PDP.  
Próximo passo: auditoria de tags/scripts P1 antes de mexer em layout.

### P1 — CTR baixo em páginas de alta demanda

GSC mostra oportunidade clara:

- `onitsuka tiger`: 23.946 impressões, CTR 0,29%, posição 8,3.
- `lululemon`: 16.638 impressões, CTR 0,70%, posição 5,4.
- `new balance 204l`: página com 23.543 impressões e CTR 0,79%.
- Air Jordan Travis Scott: 26.759 impressões e CTR 0,82%.

Interpretação: autoridade/posição já existe; oportunidade está em title/meta, snippet, FAQ/blocos citáveis e prova de autenticidade/compra segura.

### P1 — Meta descriptions/titles inconsistentes em páginas editoriais e institucionais

Crawl amostral de 260 URLs:

- 108 páginas sem meta description — parte contaminada por 429 do crawler, mas páginas 200 também aparecem.
- 34 descriptions >160 chars.
- 28 titles >60 chars.
- 15 titles curtos.
- Exemplos reais 200:
  - `/pages/reviews`: sem meta description.
  - `/pages/acompanhe-seu-pedido`: sem meta description.
  - `/pages/adidas-samba-vs-campus-00s`: description 320 chars.
  - `/pages/new-balance-530-vs-2002r`: description 320 chars.
  - `/pages/onitsuka-tiger-vs-asics-gel-1130`: title 82 chars, description 320 chars.

Impacto: snippets truncados e perda de CTR em páginas que poderiam funcionar como source pages/GEO.

### P2 — H1 múltiplo em algumas páginas

Exemplos 200:

- `/pages/autenticidade`: 2 H1.
- `/pages/sobre-a-lk-sneakers-e-apparels`: 2 H1.
- `/pages/guia-adidas-samba`: 2 H1.
- `/pages/guia-onitsuka-tiger-mexico-66`: 2 H1.
- `/pages/guia-adidas-sambae`: 2 H1.

Impacto moderado: não é P0, mas reduz clareza semântica e disciplina de template.

### P2 — Rate limiting/challenge para crawl agressivo

No crawl de 260 URLs, após muitas requisições rápidas surgiram 105 respostas 429 com texto `Your connection needs to be verified before you can proceed`.

Interpretação: provavelmente defesa anti-bot/Cloudflare/Shopify por cadência de auditoria, não prova de bloqueio Google. Mesmo assim, precisa cuidado para não endurecer demais contra bots úteis de SEO/AI.

## Recomendações priorizadas

### 1. Corrigir camada de scripts/tags que afeta performance e reviews

- Dono sugerido: Shopify/Tech + Growth diagnóstico.
- Ação: revisar origem e necessidade de `recovery`, webhook `n8n`, `[ET] tracker`, Judge.me key, duplicações de scripts e pings.
- Impacto: alto em CRO/PDP mobile e CWV.
- Risco: médio se remover tracker necessário sem mapear evento.
- Aprovação: necessária para qualquer alteração em theme/app/script production.
- Rollback: snapshot do tema/config + reativação dos snippets/app embeds removidos.

### 2. Sprint CTR para páginas com alta impressão e CTR baixo

Prioridade:

1. Onitsuka Tiger todos os modelos.
2. Lululemon.
3. New Balance 204L.
4. Air Jordan Travis Scott.
5. Guia de tamanhos.

Ação: title/meta + FAQ/snippet + blocos citáveis, sem prometer disponibilidade pública; usar linguagem premium/curadoria/autenticidade/atendimento humano.

### 3. Normalizar metadados das páginas editoriais/source pages

- Reduzir descriptions de 320 chars para 140–155 chars.
- Resolver pages sem description.
- Ajustar titles longos para 50–60 chars quando possível.
- Priorizar páginas com GSC ou links internos fortes.

### 4. Corrigir H1 múltiplo em templates/editoriais

- Trocar segundo H1 por H2/Hero heading estilizado.
- Aplicar primeiro em guias e páginas institucionais de alta visibilidade.

### 5. Manter e expandir GEO, mas com governança

- `llms.txt`, `llms-full.txt`, `agents.md` e UCP são diferencial forte.
- Próximo passo: garantir que páginas prioritárias tenham blocos citáveis próprios e FAQPage único, sem duplicação.

## Quick wins sem write externo imediato

- Gerar packet de titles/metas para páginas editoriais com `desc_len=320` e páginas sem description.
- Criar lista de H1 múltiplo para LKGOC/Shopify Tech corrigir em template ou páginas.
- Rodar auditoria isolada de scripts com mapa de app embeds/snippets antes de qualquer alteração.

## O que precisa aprovação antes de executar

- Alterar title/meta/description visível em produção.
- Alterar tema, snippets, app embeds, Judge.me, tags ou scripts em produção.
- Alterar schema injetado por theme/app.
- Qualquer ajuste em Shopify production.

## Anexo técnico

Artefatos locais da coleta:

- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/home_parse.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/sitemap_urls.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/crawl_sample.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/audit_crawl_summary.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/gsc_pages_28d.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/gsc_query_page_28d.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/ga4_organic_28d.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/ga4_top_pages_28d.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/playwright_perf.json`


## Atualização 2026-06-07 — PageSpeed via Doppler confirmado

Lucas confirmou que a chave estava no Doppler. Reexecutei `google_auth.py --check` com `doppler run --project lc-keys --config prd`; resultado: PageSpeed Insights v5, CrUX API e CrUX History API OK.

### PageSpeed / CrUX mobile — URLs críticas

- **/**
  - Lighthouse mobile: Performance 48/100; SEO 92/100; Best Practices 92/100; Accessibility 92/100
  - Lab: FCP 5510.294166282305; LCP 16387.65996054642; TBT 350.5; CLS None; Speed Index 10837.570734652067
- **/collections/lululemon**
  - Lighthouse mobile: Performance 83/100; SEO 92/100; Best Practices 92/100; Accessibility 91/100
  - Lab: FCP 2189.4684373861046; LCP 3001.0026610977675; TBT 337.49903904802886; CLS 0.02191; Speed Index 3870.5397847693894
- **/collections/new-balance-204l**
  - PSI/Lighthouse: erro `Request failed: Response ended prematurely`
- **/collections/onitsuka-tiger-todos-os-modelos**
  - PSI/Lighthouse: erro `PageSpeed Insights request timed out (120s). The target page may be very slow.`
- **/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo**
  - Lighthouse mobile: Performance 66/100; SEO 92/100; Best Practices 92/100; Accessibility 94/100
  - Lab: FCP 2576.002527722313; LCP 3751.0038758408805; TBT 587.5; CLS 0.000153; Speed Index 5515.747581582437

### Leitura revisada de performance

- O CrUX real está melhor que o lab Playwright/PSI sugeria em várias páginas: LCP/INP/CLS p75 aparecem como `good` nas URLs com dados CrUX.

- Mesmo assim, a Home teve Lighthouse mobile Performance 48/100 e LCP lab ~16,4s; PDP amostrada 66/100 e TBT ~588ms. Então a prioridade continua sendo reduzir JS/terceiros e corrigir erros de console, não mexer primeiro em layout.

- Nota revisada de Performance: **65/100** em vez de 55/100. Nota geral revisada: **~80/100 — B+**.


### Scan Shopify production theme — origem de parte dos scripts

- Tema produção escaneado read-only: **6 assets com matches**.

  - `assets/lk-judgeme.css` — Judge.me
  - `layout/theme.liquid` — WhatsApp recovery endpoint, Judge.me, n8n
  - `sections/lk-pdp.liquid` — Judge.me
  - `snippets/judgeme_widgets.liquid` — Judge.me
  - `snippets/lk-whatsapp-widget.liquid` — WhatsApp recovery endpoint
  - `snippets/product-structured-data.liquid` — Judge.me

Atenção: `n8n` e `[ET] tracker` não apareceram nos assets líquidos do tema; provavelmente vêm de app embed, customer pixel, GTM/Metricool/Pareto ou script externo. Não removi nada em produção nesta etapa sem mapear a origem exata.


## Atualização 2026-06-07 — P1 fixes executados

Após aprovação “Seguir”, foram executados writes escopados em produção, com rollback salvo:

- WhatsApp recovery mint CORS mitigado: hash mint pausado por opt-in; CTA WhatsApp preservado.
- n8n cart-intent CORS mitigado: dual-write n8n desativado; Recovery OS `/events/storefront` preservado.
- ScriptTag estático `track.lksneakers.com.br/static/tracker.js` removido por emitir `[ET] tracker not configured`; `et-tracker.liquid` permanece ativo.
- Tema passou a respeitar SEO metafields em Shopify Pages.
- Titles/metas aplicados e validados em 5 páginas editoriais/institucionais.

Receipt: `EXECUTION-RECEIPT-20260607-P1-FIXES.md`.
