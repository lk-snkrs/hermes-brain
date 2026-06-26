# Ahrefs P0 Fix Packet — LK Sneakers

- Escopo: P0 Ahrefs técnico — broken links/4XX/404 e broken images.
- Status: read-only; writes externos = 0.
- Fonte: Ahrefs Site Audit API via relatório full audit `20260618T202702Z`.
- `values_printed=false`.

## Resumo

- **Page has links to broken page**: 100 amostras exportadas no pacote
- **Page has broken image**: 53 amostras exportadas no pacote
- **404 page**: 19 amostras exportadas no pacote
- **4XX page**: 19 amostras exportadas no pacote
- **Image broken**: 7 amostras exportadas no pacote

## Diagnóstico por bloco

### 1) Links internos para páginas quebradas / 404 / 4XX

- Problema principal: URLs de collection com filtros e alguns links de blog/home apontam para destinos 404/4XX.
- Linhas de collection filtrada no pacote: **83**
- Top collections filtradas:
  - `/collections/nike-mind-001`: 17
  - `/collections/air-jordan-4`: 6
  - `/collections/camiseta-1`: 5
  - `/collections/nike-todos-os-modelos`: 4
  - `/collections/onitsuka-tiger-mexico-66`: 4
  - `/collections/sneakers`: 3
  - `/collections/lululemon`: 3
  - `/collections/alo-yoga-1`: 3
  - `/collections/new-balance-9060`: 3
  - `/collections/new-balance-204l`: 3
- 404/4XX com ação sugerida estão em `p0-404-page.csv`, `p0-4xx-page.csv` e `p0-redirect-candidates-review-required.csv`.

### 2) Imagens quebradas

- Imagens Judge.me/objeto serializado: **3** linhas.
- Imagens externas quebradas/limitadas: **4** linhas.
- A causa mais clara é renderização de objeto de imagem como URL em `/products/{"original"=>...}`.
- Correção deve ser em dev theme/snippet/app primeiro; não aplicar direto em produção.

## Top exemplos críticos

- **Page has broken image** `200` — https://lksneakers.com.br/collections/nike-mind-001
  - tráfego Ahrefs: 115.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo
  - tráfego Ahrefs: 1.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-white
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/oculos-de-sol-jacquemus-jac5c2sun-branco
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/oculos-de-sol-jacquemus-jac2c2sun-bege
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-university-red-vermelho
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/air-jordan-4-craft-medium-olive
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto
  - tráfego Ahrefs: 1.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-pale-pink-rosa
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/bolsa-jacquemus-le-chiquito-noeud-bag-light-pink-rosa
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/camiseta-jacquemus-the-typo-azul
  - tráfego Ahrefs: 3.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/bone-jacquemus-la-casquette-artichaut-black-preto
  - tráfego Ahrefs: 0.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.
- **Page has broken image** `200` — https://lksneakers.com.br/products/bolsa-jacquemus-le-chiquito-moyen-bag-light-pink-rosa
  - tráfego Ahrefs: 34.0
  - ação: Inspecionar imagens quebradas na página; se vier de conteúdo externo/blog, trocar/remover; se app/snippet, corrigir em dev theme.

## Plano de execução proposto

### Etapa A — Sem write externo
- Validar URLs candidatas e agrupar por origem: home/menu, blog, collection filter, PDP, app/snippet.
- Abrir dev theme e localizar snippet que renderiza imagem Judge.me como objeto.
- Preparar patch em dev theme/preview e lista final de redirects.

### Etapa B — Com aprovação explícita
- Aplicar redirects Shopify production somente para URLs com destino confirmado.
- Remover/corrigir links em conteúdo/blog/home/menu/template.
- Corrigir snippet/app Judge.me em production após teste no dev theme.

## Risco e rollback
- Redirects: risco baixo/médio; rollback removendo redirects criados via lista exportada.
- Theme/snippet: risco médio; usar dev theme, preview e rollback por versão/theme duplicado.
- Conteúdo/blog: risco baixo; manter export/snapshot antes/depois.

## Arquivos
- Pasta: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-p0-fix-packet/20260618T205642Z`
- `p0-all-records.csv`
- `p0-404-page.csv`
- `p0-4xx-page.csv`
- `p0-page-has-links-to-broken-page.csv`
- `p0-page-has-broken-image.csv`
- `p0-image-broken.csv`
- `p0-redirect-candidates-review-required.csv`
- `p0-summary.json`
