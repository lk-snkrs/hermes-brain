# LK Growth — Decision Router

Data: 2026-05-19
Tipo: rotina read-only / roteamento de diagnóstico

## Objetivo

Definir qual camada do LK Growth OS deve ser usada para cada tipo de problema, evitando auditoria genérica e garantindo que recomendações comerciais sejam `decision-grade`.

## Regra central

Nunca priorizar apenas por HTML público. Para recomendar ação em página/produto/campanha, cruzar dados comerciais e demanda quando disponíveis: Shopify, GA4, GSC, GMC, CRM/Klaviyo, Meta/Paid, PageSpeed/CrUX e SERP.

Se a fonte obrigatória faltar, marcar como `não decision-grade` e transformar em pedido de dado ou smoke test read-only.

## Roteamento por sintoma

### 1. PDP ou collection com tráfego e baixa conversão

Usar:
- GA4: sessões, usuários, conversão, receita, landing page e funil.
- Shopify: produto, handle, preço, imagens, variantes e vendas.
- GSC: queries/páginas, CTR e posição.
- GMC: issues do item se for produto com Shopping/Free Listings.
- PageSpeed/CrUX: LCP, INP, CLS e performance mobile.
- Claude SEO: diagnóstico técnico/on-page/schema.
- Shopify CRO: CTA, trust, reviews, filtros, ordenação, mobile.

Saída esperada:
- fila P0/P1/P2;
- approval packet se houver write visível ou Shopify/theme/GMC;
- rollback e review de impacto em aproximadamente 7 dias se aprovado.

### 2. Busca informacional, FAQ, guia ou intenção topo/meio de funil

Usar:
- GSC: query, impressão, CTR, posição e páginas candidatas.
- SERP/DataForSEO: players, PAA, snippets, intent e lacunas.
- Claude Blog: brief, outline, FAQ, blocos citáveis, schema editorial e repurpose.
- Claude SEO/GEO: validação de citabilidade, schema e AI search readiness.

Saída esperada:
- brief editorial ou FAQ;
- proposta de cluster/hub-and-spoke;
- schema FAQ/Article quando aplicável;
- publicação somente após aprovação Lucas.

### 3. Queda ou warning no Google Merchant Center

Usar:
- GMC: product status, destination status, item issues e feed/source.
- Shopify: título, descrição, brand, GTIN/MPN, imagens, preço, disponibilidade e URL.
- GSC/GA4: impacto em tráfego/conversão quando relevante.
- Claude SEO/Ecommerce: qualidade de PDP e dados de produto.

Saída esperada:
- issue agrupado por tipo;
- preview de correção;
- rollback snapshot;
- aprovação explícita antes de supplemental feed, ProductInput, fetch/reprocess ou write.

### 4. Influencer, Meta, Google Ads ou campanha gerando demanda

Usar:
- Meta/Google/Pareto/Metricool: sinal de demanda, criativo, campanha, produto/influencer.
- Shopify: vendas, pedidos, produto/SKU/tamanho e receita.
- GA4: landing page e conversão.
- GSC: demanda orgânica residual ou branded/non-branded.
- Claude Ads: leitura de campanha, creative quality e landing page fit.
- Claude Blog/SEO: se a demanda pedir FAQ, guia, página de apoio ou cluster.

Saída esperada:
- separar platform signal de venda comprovada;
- detectar gargalo de PDP/collection/estoque operacional sem usar estoque como critério SEO isolado;
- recomendar CRO/conteúdo/landing apenas com evidência.

### 5. Performance/Core Web Vitals

Usar:
- CrUX origin-level para field data quando disponível.
- PSI/Lighthouse para lab data e oportunidades técnicas.
- Shopify theme/dev preview para mudanças visuais/técnicas.
- GA4/GSC para impacto comercial/SEO.

Saída esperada:
- diagnóstico por métrica: LCP, INP, CLS, TTFB;
- proposta em dev theme quando houver alteração de tema;
- nenhum publish sem aprovação.

### 6. AI Visibility / GEO

Usar:
- Claude SEO/Geo e Claude Blog/Geo.
- GSC/SERP/DataForSEO para demanda e entidades.
- Schema Product, FAQ, Breadcrumb e Article quando aplicável.
- `llms.txt`, blocos answer-first, fontes e legibilidade.

Saída esperada:
- oportunidades citáveis por página/cluster;
- FAQ ou bloco de resposta;
- schema proposto;
- sem publicação sem aprovação.

## Critérios mínimos de `decision-grade`

Uma recomendação Growth é decision-grade quando tem, conforme o caso:

- fonte comercial: Shopify/GA4/conversão/receita/pedidos;
- fonte de demanda: GSC/SERP/paid/influencer;
- fonte técnica: HTML/PageSpeed/schema/GMC;
- risco e rollback;
- indicação clara de aprovação necessária ou não.

## Ações livres

- leitura/auditoria read-only;
- scorecard;
- proposta/preview;
- approval packet;
- documentação no Brain;
- plano de rollback.

## Ações bloqueadas sem aprovação atual

- Shopify/theme/product/meta/description/schema write;
- GMC/feed/ProductInput/fetch que altere estado;
- GA4/GSC admin config;
- Meta/Google Ads changes;
- Klaviyo/WhatsApp/email/social send;
- preço, estoque, desconto ou checkout;
- produção/deploy/theme publish.
