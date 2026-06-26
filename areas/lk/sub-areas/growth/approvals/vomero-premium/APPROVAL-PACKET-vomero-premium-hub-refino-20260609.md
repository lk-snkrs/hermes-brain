# Approval Packet — Nike Vomero Premium hub/refino SEO-GEO-CRO

Data: 2026-06-09T18:54:29.819533+00:00
Status: **draft/read-only** — nenhum write executado.
Dono: LK Growth
Escopo: Shopify SEO/CRO, GEO/AI Search, schema, links internos e QA de snippets.

## 1) Decisão pedida

Aprovar preparação/execução controlada em **dev/draft** para refino do hub Nike Vomero Premium, com produção somente após novo approval por URL/campo.

## 2) Por que agora

Fatos coletados:

- `nike vomero premium`: **22.200 buscas/mês** no Google Brasil; pico recente de **49.500/mês** em mar/abr 2026; competição HIGH; intenção transacional no Keyword Overview.
- `nike vomero premium masculino`: **1.000 buscas/mês**, intenção transacional.
- `nike vomero premium feminino`: **260 buscas/mês**, intenção mista informacional/transacional/comercial.
- AI search volume:
  - `vomero premium`: **19/mês** e crescente.
  - `nike vomero premium`: **10/mês** e crescente.
- SERP mobile para `nike vomero premium lksneakers`:
  - anúncio LK para coleção em #1 paid;
  - coleção LK em #1 orgânico;
  - bloco Popular Products com vários SKUs LK;
  - Nike oficial, Droper, Sportline, VK, MT Sneakers e outros aparecem como competição/preço.
- SERP `site:lksneakers.com.br nike vomero premium` mostra múltiplos ativos LK: PDPs, guia, blog e subdomínio blog.

Interpretação:

- Não é uma frente de criação do zero. A LK já tem boa presença.
- O risco principal é **canibalização/desalinhamento entre coleção, guia, PDPs e blog**, além de snippets com copy inconsistente.
- Melhor alavanca: transformar a coleção em página transacional principal, guia em apoio consultivo/GEO, PDPs em conversão, blog em descoberta.

## 3) Evidência pública auditada

Arquivo técnico:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/vomero/vomero-public-hub-audit-20260609T185308Z.json`

### Coleção principal

URL: `https://lksneakers.com.br/collections/nike-vomero-premium`

- Status: 200
- Title: Nike Vomero Premium — Comprar | LK Sneakers
- Meta: Nike Vomero Premium: running heritage com amortecimento Zoom Air e design contemporâneo. 15 modelos na LK Sneakers, Jardins SP. Frete grátis, 10x sem juros.
- H1: ['Nike Vomero Premium']
- Schema detectado: AggregateRating, Answer, BreadcrumbList, City, CollectionPage, DefinedRegion, FAQPage, GeoCoordinates, ItemList, ListItem, MerchantReturnPolicy, MonetaryAmount...
- FAQPage schema: sim
- Termos sensíveis: {'pronta entrega': False, 'encomenda': False, 'sob encomenda': False, 'estoque': False, 'disponibilidade': True, 'sujeito a encomenda': False}

### Guia

URL: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`

- Status: 200
- Title: Nike Vomero Premium | Guia LK
- Meta: Guia LK do Nike Vomero Premium: tecnologia, conforto, design e como escolher modelos desejados com segurança.
- H1: ['Nike Vomero Premium: Guia Completo 2026']
- Schema detectado: AggregateRating, City, DefinedRegion, GeoCoordinates, MerchantReturnPolicy, MonetaryAmount, OfferShippingDetails, OpeningHoursSpecification, PostalAddress, QuantitativeValue, ShippingDeliveryTime, ShippingRateSettings
- FAQPage schema: não
- Termos sensíveis: {'pronta entrega': False, 'encomenda': False, 'sob encomenda': False, 'estoque': False, 'disponibilidade': False, 'sujeito a encomenda': False}

### PDPs auditados

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-white-bright-crimson-branco`
  - title: Nike Vomero Premium Original | LK Sneakers
  - meta: Nike Vomero Premium original na LK: amortecimento máximo, presença fashion e curadoria premium com atendimento humano para orientar a escolha.
  - Product schema: sim | FAQPage: sim
  - termos sensíveis: {'pronta entrega': False, 'encomenda': True, 'sob encomenda': True, 'estoque': False, 'disponibilidade': True, 'sujeito a encomenda': False}
- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-tangerine-tint-laranja`
  - title: Tênis Nike Vomero Premium Tangerine Tint Laranja por R$ 4.999,99 em até 10x | LK Sneakers
  - meta: Nike Vomero O Vomero é um tênis de corrida da Nike com amortecimento Zoom Air e perfil bulky, ideal para uso urbano e quem busca conforto com estética de runner premium. O cabedal do modelo Tangerine Tint combina mesh respirável com sobreposições em materiais técnicos, oferecendo estrutura leve e ventilação para o dia
  - Product schema: sim | FAQPage: sim
  - termos sensíveis: {'pronta entrega': False, 'encomenda': True, 'sob encomenda': True, 'estoque': False, 'disponibilidade': True, 'sujeito a encomenda': True}
- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-sail-coconut-milk-branco`
  - title: Tênis Nike Vomero Premium Sail Coconut Milk Branco | LK Sneakers
  - meta: Tênis Nike Vomero Premium Sail Coconut Milk Branco original. ✓ 100% autêntico ✓ 10x sem juros ✓ Frete grátis +R$499
  - Product schema: sim | FAQPage: sim
  - termos sensíveis: {'pronta entrega': False, 'encomenda': True, 'sob encomenda': True, 'estoque': False, 'disponibilidade': True, 'sujeito a encomenda': False}
- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-alabaster-amarelo`
  - title: Tênis Nike Vomero Premium Alabaster Amarelo por R$ 4.499,99 em até 10x | LK Sneakers
  - meta: Tênis Nike Vomero Premium Alabaster Amarelo: running premium com amortecimento ZoomX. Curadoria LK · 100% original · 10x sem juros · Frete grátis.
  - Product schema: sim | FAQPage: sim
  - termos sensíveis: {'pronta entrega': False, 'encomenda': True, 'sob encomenda': True, 'estoque': False, 'disponibilidade': True, 'sujeito a encomenda': False}

## 4) Achados principais

### A) Coleção deve ser a URL transacional principal

- A coleção já ranqueia como orgânico #1 para busca com LK e aparece como destino do anúncio.
- Meta atual é boa e comercial: “15 modelos”, Jardins SP, frete grátis, 10x.
- Deve receber links internos consistentes vindos do guia, blog e PDPs.

Recomendação:

- Manter coleção como destino principal para intenção “comprar Nike Vomero Premium”.
- Evitar que o guia tente competir com a coleção em CTA transacional primário.

### B) Guia é bom para GEO, mas parece sem FAQPage schema detectado

- Guia tem H1 e meta adequados.
- Na auditoria pública, o guia **não mostrou FAQPage schema**, enquanto coleção/PDPs mostraram FAQPage.

Recomendação:

- Adicionar bloco FAQ citável no guia com respostas curtas e schema FAQPage, se o template permitir.
- Direcionar CTAs do guia para a coleção e para SKUs prioritários, não para termos de disponibilidade.

### C) PDPs têm Product/Offer schema, mas copy/snippet está inconsistente entre SKUs

- Alguns PDPs têm meta premium forte.
- Outros usam meta truncada ou genérica, por exemplo Tangerine Tint com descrição longa demais.
- Vários PDPs expõem termos operacionais no HTML: `encomenda`, `sob encomenda`, `disponibilidade`.

Bloqueio:

- Termos operacionais foram encaminhados para `lk-stock`:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/handoffs/growth-handoff-vomero-operational-terms-20260609T185324Z.md`

Até retorno, Growth não deve propor remoção/alteração desses termos em produção.

### D) Competição de preço é agressiva; LK precisa defender premium/trust

SERP trouxe concorrentes com preços mais baixos e Nike oficial com preço menor. A LK não deve competir só por preço; precisa reforçar:

- curadoria premium;
- autenticidade;
- atendimento humano;
- experiência Jardins/SP;
- escolha assistida de numeração/modelo;
- segurança de compra.

## 5) Proposta de alterações — sem publicar ainda

### 5.1 Guia `/pages/nike-vomero-premium-guia`

Objetivo: GEO + orientação consultiva.

Adicionar/ajustar seção FAQ com respostas citáveis:

1. **O que é o Nike Vomero Premium?**
   - Resposta draft: “O Nike Vomero Premium é uma leitura maximalista da linha Vomero, combinando amortecimento alto, unidades Zoom Air e visual de running contemporâneo. Na LK, ele é tratado como sneaker de curadoria: técnico no conforto, mas pensado também para uso urbano e composição de estilo.”

2. **Qual a diferença entre Nike Vomero Premium e Vomero 5?**
   - Resposta draft: “O Vomero 5 tem perfil mais clássico de runner retrô, enquanto o Vomero Premium aposta em proporção mais alta, presença visual maior e sensação de amortecimento mais extrema. A escolha depende do estilo: discreto e versátil no Vomero 5; marcante e fashion no Vomero Premium.”

3. **O Nike Vomero Premium é confortável para uso urbano?**
   - Resposta draft: “Sim. A proposta do modelo combina amortecimento macio e estrutura de running, o que favorece uso urbano e longos períodos em pé. Como a silhueta é alta e presente, a adaptação pode variar por perfil de uso.”

4. **Como escolher a cor do Nike Vomero Premium?**
   - Resposta draft: “Cores claras como Sail/Coconut Milk e White/Bright Crimson tendem a funcionar melhor em looks limpos e casuais. Cores vibrantes ou contrastadas criam ponto focal. Para uma escolha segura, a LK recomenda considerar rotina de uso, guarda-roupa e orientação humana pelo atendimento.”

5. **Onde comprar Nike Vomero Premium original no Brasil?**
   - Resposta draft: “A LK Sneakers trabalha com curadoria de sneakers originais, atendimento humano e experiência premium no Jardins, em São Paulo. A coleção Nike Vomero Premium reúne modelos selecionados para compra online e orientação personalizada.”

CTA recomendado no guia:

- Primário: “Ver coleção Nike Vomero Premium na LK” → `/collections/nike-vomero-premium`
- Secundário: “Falar com atendimento para escolher o modelo” → canal existente, sem promessa de disponibilidade.

### 5.2 Coleção `/collections/nike-vomero-premium`

Objetivo: conversão e entidade transacional.

Proposta:

- Manter title/meta atuais por enquanto — já estão bons.
- Adicionar bloco curto no corpo da coleção, se ainda não estiver claro acima/abaixo do grid:

Draft:

> Nike Vomero Premium na LK: uma curadoria de runners de presença marcante, com amortecimento elevado, estética contemporânea e atendimento humano para orientar sua escolha. Explore modelos selecionados e encontre a cor que melhor conversa com seu estilo.

Links internos recomendados:

- Para guia: “Entenda o Nike Vomero Premium” → `/pages/nike-vomero-premium-guia`
- Para blog lifestyle: “Por que virou fenômeno de lifestyle” → `/blogs/novidades/nike-vomero-premium-por-que-o-running-mais-alto-do-mundo-virou-fenomeno-de-lifestyle`

### 5.3 PDPs

Objetivo: reduzir inconsistência de snippet e aumentar trust.

Prioridade de revisão:

1. White Bright Crimson — já tem meta premium boa; usar como padrão.
2. Tangerine Tint — meta muito longa/genericona; precisa revisão.
3. Sail Coconut Milk — meta boa e objetiva.
4. Alabaster — meta boa.

Não mexer agora em frases de disponibilidade/encomenda até retorno do `lk-stock`.

Meta pattern aprovado para draft, sem termos operacionais:

> Nike Vomero Premium [cor] original na LK: amortecimento alto, estética running premium e curadoria com atendimento humano para orientar sua escolha.

## 6) Links internos recomendados

Modelo de arquitetura:

- Coleção = hub comercial/transacional.
- Guia = hub consultivo/GEO/FAQ.
- Blog = descoberta/lifestyle, linkando para guia e coleção.
- PDPs = conversão, com link contextual para coleção e guia.

Âncoras recomendadas:

- `Nike Vomero Premium na LK`
- `coleção Nike Vomero Premium`
- `guia Nike Vomero Premium`
- `como escolher o Nike Vomero Premium`
- `Vomero Premium original`

Evitar:

- âncoras com “pronta entrega”, “estoque”, “sob encomenda” ou promessas de prazo.

## 7) Risco, esforço e rollback

Impacto esperado:

- Médio/alto em SEO/GEO e CTR qualificado.
- Médio em conversão, principalmente se links guia → coleção/PDP forem reforçados.

Esforço:

- Baixo/médio: conteúdo curto + FAQ schema + links internos.

Risco:

- Baixo se feito primeiro em draft/dev.
- Médio se alterar PDPs com termos operacionais sem validação de estoque — por isso está bloqueado.

Rollback:

- Salvar HTML/metafields atuais antes de qualquer write.
- Reverter title/meta/body/sections ao snapshot anterior.
- Impact review D+7 em GSC/GA4/Shopify.

## 8) O que posso fazer sem aprovação agora

- Preparar snippets finais em arquivo local.
- Montar JSON-LD FAQ draft para o guia.
- Criar checklist de QA por URL.
- Preparar plano de execução em dev theme/draft.

## 9) O que precisa aprovação explícita

- Publicar FAQ/schema no guia.
- Alterar body da coleção.
- Alterar title/meta/body de PDPs.
- Alterar theme/sections em produção.
- Qualquer ajuste envolvendo disponibilidade, prazo, encomenda, estoque ou promessa operacional.

## 10) Checklist canônico 18 tópicos

- GA4: pendente; necessário para decision-grade de conversão.
- GSC: pendente; necessário para CTR/query por URL.
- GMC: não mexido; checar residual separadamente.
- Shopify SEO: audit público feito; writes pendentes de aprovação.
- Shopify CRO/theme: proposta conceitual; dev/draft antes de produção.
- GEO/AI Search: AI volumes coletados; FAQ citável recomendado.
- PageSpeed/CrUX/CWV: PSI estava bloqueado por quota 429 na triagem anterior.
- Schema: coleção/PDPs OK; guia sem FAQPage detectado.
- Reviews: ratings aparecem em SERP/Popular Products; origem/schema precisa validação.
- Paid media: SERP mostrou anúncio LK para coleção.
- Influencer/social demand: não verificado nesta rodada.
- Concorrência/SERP: Nike oficial, Droper, Sportline, VK, MT Sneakers observados.
- Google Business/local: Jardins SP aparece na proposta e meta da coleção.
- Klaviyo/CRM signals: não verificado.
- Catálogo/product data quality: parcial por SERP/schema; GMC/Shopify pendentes.
- Conteúdo/taxonomia comercial: proposta feita; termos operacionais bloqueados por stock.
- Mensuração/QA eventos: pendente.
- Impact review/experimentation: D+7 recomendado após qualquer publicação.

## Approval solicitado

Aprovar apenas a próxima etapa segura:

**“Preparar draft/dev do FAQ + links internos do hub Nike Vomero Premium, sem publicar e sem alterar termos operacionais/estoque.”**
