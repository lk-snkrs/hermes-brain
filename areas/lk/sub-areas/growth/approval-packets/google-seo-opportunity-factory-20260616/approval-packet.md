# Approval Packet — Google SEO Opportunity Factory — 2026-06-16

**Rotina:** terça-feira — LK Google SEO Opportunity Factory / LK Growth Ranking OS v2  
**Modo:** read-only / preview-only  
**Writes externos:** 0  
**values_printed:** false  
**Status:** precisa aprovação explícita de Lucas antes de qualquer Shopify/theme/content/schema production write.

## Veredito

A oportunidade material de hoje é **Nike Mind 001 Black Chrome**. O GSC mostra demanda excepcional com CTR praticamente nulo: a query `nike mind 001` gera **37.488 impressões / 5 cliques / CTR 0,01% / posição 9,1** para o PDP `slide-nike-mind-001-black-chrome-preto`. O cluster Nike Mind também tem sinal comercial validado em Shopify read-only: **R$ 231.199,30 / 70 unidades / 49 pedidos em 90 dias**.

Status de decisão: **decision-grade para demanda GSC + prioridade comercial de cluster; parcial para SERP live/DataForSEO**, porque DataForSEO/MCP não está exposto nesta sessão e `web_search` retornou erro de token. Foi usada checagem pública alternativa em DuckDuckGo Lite apenas como proxy de SERP, não como fonte final Google.

## URL foco

- `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`
- URL canônica verificada no HTML: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`

## Queries alvo

1. `nike mind 001` — principal: alta impressão, CTR 0,01%, posição 9,1.
2. `chinelo nike mind 001` — 10.308 impressões / 6 cliques / CTR 0,06% / posição 6,0.
3. `nike mind 001 brasil` — intenção sugerida pelo cluster e SERP proxy; precisa validação DataForSEO/Google live.
4. `nike mind 001 original` — intenção de autenticidade e compra segura, fit direto com LK.
5. `nike mind 001 black chrome` — intenção colorway/PDP.

## Evidência GSC / comercial / SERP

### GSC — Search Console read-only

Fonte: `reports/lk-search-console-readonly-router-2026-05-11.md`, gerado em `2026-06-16T11:32:40Z`, janela `2026-05-17 → 2026-06-13`, property `sc-domain:lksneakers.com.br`.

- `nike mind 001` → PDP Black Chrome: 5 cliques / 37.488 impressões / CTR 0,01% / posição 9,1.
- `nike mind 001` → PDP Pearl Pink: 11 cliques / 30.802 impressões / CTR 0,04% / posição 9,0.
- `chinelo nike mind 001` → PDP Black Chrome: 6 cliques / 10.308 impressões / CTR 0,06% / posição 6,0.
- Collection `/collections/nike-mind-001`: 199 cliques / 15.922 impressões / CTR 1,25% / posição 7,5.

### Shopify / comercial

Fonte: `areas/lk/sub-areas/growth/reports/ranking-goals/revenue-informed-priority-clusters-20260613.md`.

- Nike Mind cluster: R$ 231.199,30 / 70 unidades / 49 pedidos / share 6,3% nos últimos 90 dias.
- Produtos do cluster no Top Products: `Tênis Nike Mind 002 Light Smoke Grey` e `Slide Nike Mind 001 Light Smoke Grey` aparecem como evidência de demanda comercial real.

### SERP live / concorrência

- DataForSEO/MCP: **não disponível nesta sessão**; não foi inventado volume/posição.
- `web_search`: indisponível por erro de token.
- Fallback público DuckDuckGo Lite para `nike mind 001 brasil original` mostrou concorrentes/players: Original São Paulo, Nike.com.br, Nike PT, LK collection, Juicy Sneakers, Mercado Livre, 6ix, Accio Brasil, Farfetch e Netshoes. Usar apenas como proxy de paisagem competitiva; não substituir Google SERP/DataForSEO.

## Diagnóstico on-page do PDP

Fonte: HTML público do PDP, read-only.

- Title atual: `Nike Mind 001 Black Chrome Original | LK Sneakers` — 49 caracteres.
- Meta atual: `Nike Mind 001 Black Chrome original na LK: slide escultural com conforto sensorial, curadoria premium e atendimento humano para confirmar o par.` — 144 caracteres.
- H1 atual: `Chinelo Slide Nike Mind 001 Black Chrome Preto` — 46 caracteres.
- H1 count: 1.
- H2 count: 3: `Slide Nike Mind 001 Black Chrome Preto`, `Relacionados`, `O que é raro, merece ser encontrado.`
- Schema detectado: Organization/ShoeStore/ClothingStore, Product, BreadcrumbList, FAQPage.
- FAQPage atual: 7 perguntas; há perguntas úteis de tamanho/originalidade, mas o conjunto ainda mistura perguntas genéricas (`prazo`, `embalagem`, `parcelar`) com baixa captura de intenção `Brasil/original/onde comprar`.
- Imagens: 31 tags `<img>`, sem `alt` ausente no HTML bruto.

## Problema de ranking/CTR/intenção

A página está em posição média competitiva (Top 10) mas quase não captura clique. O problema provável não é indexação básica: é **mismatch de snippet/intenção** para uma busca ampla (`nike mind 001`) e para variações de compra segura no Brasil. O snippet atual é elegante, mas não explicita suficientemente `no Brasil`, `original`, `Black Chrome` como intenção de compra/segurança; o H1 ainda abre com `Chinelo Slide`, que pode reduzir correspondência com a forma como o usuário busca (`Nike Mind 001`).

## Proposta concreta — preview para aprovação

### 1) Shopify SEO fields — SEO-field-only

- **Title proposto:** `Nike Mind 001 Black Chrome Original no Brasil | LK`  
  Caracteres: 50.
- **Meta proposta:** `Nike Mind 001 Black Chrome original no Brasil: slide escultural da linha Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`  
  Caracteres: 146.

Risco: baixo/médio. Altera snippet, não altera preço, produto, disponibilidade, campanha ou estoque. Pode impactar CTR; precisa D+7/D+14 GSC.

### 2) H1 / copy visível — precisa aprovação separada

- **H1 proposto:** `Nike Mind 001 Black Chrome original`  
  Caracteres: 35.
- **Bloco answer-first proposto para PDP/collection, 134–167 palavras:**

> O Nike Mind 001 Black Chrome é o slide escultural da linha Nike Mind, conhecido pelo formato anatômico, visual futurista e acabamento preto com efeito cromado. A busca pelo modelo cresceu porque ele mistura conforto sensorial, design de objeto e presença de moda — não é um chinelo básico, mas uma peça de styling para quem procura um Nike Mind original no Brasil. Na LK, a curadoria prioriza pares autênticos, seleção premium e atendimento humano para orientar modelo, tamanho e prazo pelo chat quando necessário. Para quem está comparando versões, o Black Chrome tende a ser a opção mais versátil: funciona com alfaiataria casual, denim, looks minimalistas e produções streetwear, mantendo a leitura experimental da linha Mind sem perder usabilidade.

Risco: médio. É alteração visível; precisa preservar linguagem premium e não criar taxonomia pública de disponibilidade.

### 3) FAQ / FAQPage — trocar perguntas genéricas por intenção de compra

Manter 1 FAQ canônico visível + JSON-LD em paridade. Proposta de perguntas:

1. `O Nike Mind 001 Black Chrome é original?`
2. `Onde comprar Nike Mind 001 original no Brasil?`
3. `O Nike Mind 001 tem a forma grande ou pequena?`
4. `Qual a diferença entre Nike Mind 001 e Nike Mind 002?`
5. `Como usar o Nike Mind 001 Black Chrome no dia a dia?`

Risco: médio. FAQPage em e-commerce é mais útil para IA/LLM do que para rich result Google; deve evitar prometer disponibilidade/prazo e evitar claims de sizing sem evidência.

### 4) Links internos

- Do PDP Black Chrome → `/collections/nike-mind-001` com anchor `ver curadoria Nike Mind 001 e 002`.
- Do PDP → guia/source page futura ou existente quando houver: `guia Nike Mind original no Brasil`.
- Da collection `/collections/nike-mind-001` → PDP Black Chrome como colorway-chave.

Risco: baixo/médio. Se for body/theme/link visível em produção, precisa aprovação e rollback.

### 5) Schema

- Manter Product + BreadcrumbList.
- Revisar FAQPage para paridade exata com perguntas visíveis se o FAQ for atualizado.
- Não recomendar HowTo.
- Não depender de FAQ rich results no Google; valor principal é LLM/GEO e clareza semântica.

## Impacto esperado

- CTR alvo para `nike mind 001` no PDP Black Chrome: sair de **0,01%** para pelo menos **0,3–0,5%** em D+14, mantendo posição Top 10.
- Ganho potencial: tráfego qualificado sem depender de campanha; cluster tem receita real e volume comercial.
- Métricas de revisão: GSC cliques/impressões/CTR/posição por query+URL; Shopify landing/orders como influência parcial; GA4 orgânico se conector estiver OK.

## Aprovação necessária

Para executar em produção, Lucas precisa aprovar explicitamente algo como:

`Aprovo aplicar o packet Nike Mind 001 Black Chrome de 2026-06-16 somente nos campos/textos listados, com rollback, sem alterar preço, estoque, desconto, campanhas, GMC/feed ou theme production fora do escopo.`

Sem essa aprovação: manter como preview/read-only.

## Rollback planejado se aprovado no futuro

1. Antes de qualquer mutation, reconsultar Shopify Admin read-only para capturar `seo.title`, `seo.description`, H1/body atual e seção/asset se houver tema.
2. Salvar rollback JSON/MD com valores anteriores e timestamp.
3. Aplicar somente os campos aprovados.
4. Readback Admin + HTML público/cache-bust.
5. Agendar D+7/D+14 impact review GSC/GA4/Shopify.

## Não executado

- Não alterei Shopify, theme, GMC/feed, GSC/GA4 config, Ads, Klaviyo, WhatsApp, preço, estoque ou desconto.
- Não consultei estoque/disponibilidade operacional.
- Não publiquei copy, FAQ, schema ou links internos.
- Não usei DataForSEO como fonte factual porque o MCP/tooling não estava disponível nesta sessão.
