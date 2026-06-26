# Next hubs SEO/GEO — triagem executiva

Data: 2026-06-09T18:50:09.180878+00:00
Status: **read-only / não decision-grade ainda** — faltam GA4, GSC, Shopify sales/conversão e GMC para priorização comercial final.

## Evidências coletadas

- SERP/DataForSEO mobile Brasil para: Lululemon, Nike Vomero Premium, New Balance 204L, Onitsuka Tiger e Crocs Relâmpago McQueen.
- Keyword Overview Brasil/DataForSEO.
- AI search volume/DataForSEO.
- Fetch público de páginas LK: status, title/meta, H1, canonical, schema e termos sensíveis.
- PageSpeed público tentado; bloqueado por quota Google PSI 429.

Arquivos:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/triage/next-hubs-public-seo-geo-triage-20260609T184859Z.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/triage/pagespeed-next-hubs-mobile-20260609T184925Z.json`

## Ranking recomendado agora

### P1 — Nike Vomero Premium — refino comercial/GEO

Fatos:
- Google volume: **22.200/mês** para `nike vomero premium`.
- Intenção: transactional.
- AI search volume: **10/mês** e crescente desde mar/2026.
- SERP site: LK aparece com múltiplos ativos:
  - produto em #1 para busca site;
  - guia em #3;
  - vários PDPs e blog posts.
- Página guia: 200, canonical OK, title/meta OK, H1 OK.
- Produto auditado: Product/Offer schema presente.

Interpretação:
- Já existe base forte. A oportunidade não é “criar do zero”; é **consolidar hub + links internos + FAQ/schema** para capturar busca transacional e comparação.
- Maior ganho provável: melhorar distribuição entre guia, PDPs e coleção/blog, evitando canibalização e aumentando conversão no PDP.

Risco/pendência:
- PDP contém termos `encomenda/sob encomenda` no HTML público; como envolve disponibilidade, precisa validação/handoff de stock antes de copy cleanup.

Ação sem aprovação:
- Preparar audit de canibalização e pacote de links internos/FAQ em dev/draft.

Precisa aprovação:
- Qualquer alteração em title/meta/body/theme/Shopify production.

### P2 — Crocs Relâmpago McQueen — proteger liderança + copy cleanup controlado

Fatos:
- Google volume: **33.100/mês** para `crocs relampago mcqueen`.
- Intenção: transactional.
- AI search volume: **36/mês**.
- SERP site combinada mostrou LK em posições fortes para página guia, produto e blog.
- Guia: FAQPage schema presente, title/meta/H1/canonical OK.
- Produto: Product/Offer schema presente.

Interpretação:
- Frente já está muito forte. Próximo passo deve ser **defensivo e CRO**, não recriação editorial.
- Ganho provável: reforçar CTA/link para PDP dentro do guia e checar se o snippet do produto está premium/sem fricção operacional.

Risco/pendência:
- PDP contém `encomenda/sob encomenda` no HTML público. Precisa validação com stock/operacional antes de mexer.

Ação sem aprovação:
- Criar pacote de QA + proposta de copy premium alternativa.

Precisa aprovação:
- Write em produto, page, blog ou theme.

### P3 — Lululemon — oportunidade de hub premium já iniciada

Fatos:
- Google volume: **4.400/mês** para `lululemon brasil`.
- Intenção principal: navigational; secundária commercial.
- `lululemon tenis`: 170/mês, transactional, com crescimento anual forte no dataset.
- AI search volume: **18/mês** para `lululemon brasil`.
- SERP site: coleção #1, guia #3, vários PDPs indexados.
- Coleção: title/meta/canonical/schema OK.
- Guia: title/meta/H1/canonical OK.

Interpretação:
- Melhor oportunidade para posicionamento de marca/curadoria premium, mas depende de dados de conversão e mix de catálogo.
- Como intenção é muito navegacional, precisa abordagem de **“original no Brasil + curadoria LK + atendimento humano”**, sem parecer marketplace genérico.

Risco/pendência:
- Coleção contém termo `estoque` no HTML público; não necessariamente problema isolado, mas por tocar disponibilidade deve ser revisado com cuidado.

Ação sem aprovação:
- Preparar mapa de links internos coleção ↔ guia ↔ PDPs e QA de FAQ/schema.

Precisa aprovação:
- Alterações em coleção/PDPs.

### P4 — New Balance 204L — impact review/refino, não nova frente

Fatos:
- Google volume: **9.900/mês**, pico recente alto; tendência anual muito forte no dataset.
- Intenção: transactional.
- Brain marca `new-balance-204l` como gold source visual/editorial LKGOC já trabalhado.
- SERP site: coleção #1 + blog posts + PDPs.

Interpretação:
- Não tratar como nova frente. Fazer **impact review** e ajustes pequenos se GSC/GA4 mostrar queda/CTR fraca.

Ação sem aprovação:
- Impact review read-only com GSC/GA4 quando conector disponível.

### P5 — Onitsuka Tiger — impact review + questão de snippet/termo operacional

Fatos:
- `onitsuka tiger mexico 66`: **6.600/mês**.
- `onitsuka tiger brasil`: **1.300/mês**.
- AI search volume: **52/mês** para `onitsuka tiger brasil`.
- Brain diz que Onitsuka já foi trabalhado; deve ser refino/impact review.
- SERP site: coleção e páginas relevantes indexadas.
- SERP mostrou snippet de produto com **“Pronta entrega”**; no fetch atual, meta do produto não mostra “Pronta entrega”, mas HTML contém termos operacionais `encomenda/sob encomenda/sujeito a encomenda`.

Ação tomada:
- Handoff registrado para `lk-stock`:
  - `areas/lk/sub-areas/stock/handoffs/growth-handoff-pronta-entrega-snippet-onitsuka-20260609T184808Z.md`

Interpretação:
- Não mexer em disponibilidade/copy operacional sem validação do dono de estoque.

## Checklist 18 tópicos — status desta triagem

- GA4: não verificado nesta rodada; necessário para decision-grade.
- GSC: não verificado nesta rodada; necessário para CTR/posição real.
- GMC: não verificado nesta rodada; residual ainda pendente.
- Shopify SEO: verificação pública parcial OK.
- Shopify CRO: inferido parcialmente; precisa dados de PDP/conversão.
- GEO/AI Search: volumes AI verificados; estrutura pública parcial OK.
- PageSpeed/CrUX/CWV: tentativa PSI bloqueada por 429; pendente.
- Schema: verificação pública parcial feita.
- Reviews: snippets/rating observados em SERP para PDPs; precisa validação origem/schema.
- Paid media: não verificado nesta rodada.
- Influencer/social demand: não verificado nesta rodada.
- Concorrência/SERP: SERP site e volumes coletados; SERP competitiva ampla pendente.
- Google Business/local: não aplicável nesta triagem específica, exceto menções Jardins no copy.
- Klaviyo/CRM signals: não verificado.
- Catálogo/product data quality: parcial via schema/snippet; precisa Shopify/GMC.
- Conteúdo/taxonomia comercial: verificado parcialmente; termos operacionais exigem cuidado.
- Mensuração/QA eventos: não verificado.
- Impact review/experimentation: recomendado para 204L e Onitsuka.

## Próximo passo recomendado

Executar agora, read-only:

1. **Vomero Premium**: audit de canibalização + proposta de hub/FAQ/link interno.
2. **Crocs Relâmpago McQueen**: QA defensivo do hub que já ranqueia + proposta de CRO/CTA.
3. **Lululemon**: mapa coleção/guia/PDPs e lacunas de schema/FAQ.
4. Aguardar/consultar retorno do `lk-stock` antes de qualquer copy cleanup envolvendo `pronta entrega/encomenda/estoque`.

## Approval necessário

Nenhum write foi executado. Para produção, será necessário approval explícito por URL/campo, com rollback e impact review D+7.
