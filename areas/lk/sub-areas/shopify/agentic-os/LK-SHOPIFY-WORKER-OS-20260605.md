# LK Shopify Worker OS — tema, CRO, preços e features

Data: 2026-06-05
Status: documentação operacional local; sem novo runtime, cron ou write externo nesta etapa.
Dono: LK Shopify, agente permanente da superfície Shopify da LK Sneakers.

## Decisão

LK Shopify deve ter um pool nomeado de **workers temporários** para executar tarefas técnicas de loja com mais qualidade. Esses workers não são agentes permanentes, não têm bot, não têm memória própria, não têm cron e não fazem writes por conta própria.

Regra de ativação: quando Lucas usa o **LK Shopify** para uma demanda de superfície Shopify, o agente deve classificar a demanda, escolher o playbook canônico e acionar automaticamente o subconjunto mínimo de workers necessário. Não deve ativar todos os workers por padrão. Lucas não precisa pedir manualmente “use os subagentes/workers” para tarefas normais; a seleção faz parte do fluxo operacional do LK Shopify.

Terminologia canônica: usar **workers temporários** ou **subtarefas delegadas**. Evitar chamar LK Growth, LK Shopify, LK Ops, LK Trends ou `[LK] Otimização de Coleções` de “subagentes”; eles são agentes/perfis/especialistas permanentes quando existentes.

O LK Shopify é normalmente usado por Lucas para:

- correções de tema;
- CRO e melhorias de conversão;
- mudanças de preço quando a decisão/fonte já está aprovada;
- implementação de features no site;
- cart drawer/minicart;
- ajustes de produto, coleção, page, menu, tags, metafields e SEO fields;
- QA visual e readback depois de execução aprovada.

## Fronteiras obrigatórias

- LKGOC, guia de coleção e experiência editorial de coleção pertencem a `[LK] Otimização de Coleções`.
- LK Growth traz hipóteses, sinais, métricas, CRO/GEO/SEO e impacto comercial.
- LK Ops/Tiny validam estoque, disponibilidade, promessa comercial e, quando aplicável, fonte de preço.
- LK Shopify implementa ou prepara a implementação na superfície Shopify: theme, product, collection, page, metafield, app/config, price field, menu, tag, SEO field, dev theme, readback e rollback.

## Tipos de trabalho que LK Shopify pode cobrir

### 1. Theme fixes

Exemplos:

- bug de layout no mobile;
- seção quebrada;
- CSS desalinhado;
- Liquid/snippet/section com comportamento errado;
- imagem, botão, CTA, card ou grid com problema;
- ajuste de header, menu, footer, PDP, collection page, cart, search ou landing.

Regra: primeiro diagnóstico/read-only ou dev theme; produção só com aprovação escopada.

### 2. CRO e UX

Exemplos:

- melhorar PDP acima da dobra;
- CTA, prova social, badges, frete, parcelamento, confiança;
- ordem de seções;
- PDP sticky add-to-cart;
- filtros/sort de coleção;
- coleção produto-first;
- landing/page performance;
- microcopy de compra;
- reduzir fricção no carrinho.

Regra: se a hipótese de CRO vier de Growth, Growth mede impacto; Shopify materializa preview/execução técnica.

### 3. Preço e promoção

LK Shopify pode operacionalizar mudanças de preço quando Lucas/LK Ops aprovaram o escopo exato.

Exemplos:

- alterar price/compare-at price de produto/variante;
- aplicar ou remover preço promocional;
- preparar preview de preço antes/depois;
- readback depois da alteração;
- conferir risco de sobrescrever preço vindo de Tiny/feed/app.

Bloqueios:

- não decide preço;
- não promete preço para cliente;
- não altera estoque/disponibilidade;
- não faz bulk sem lista exata, snapshot, rollback e aprovação.

### 4. Features no site

Exemplos de features que LK Shopify pode projetar/implementar com approval packet:

- cart drawer / minicart;
- upsell/cross-sell no cart drawer;
- barra de frete grátis/progresso;
- botão sticky add-to-cart;
- quick add / quick view;
- size guide/tabela de medidas;
- bloco de entrega/frete estimado;
- badges de confiança/pagamento/parcelamento;
- wishlist/back-in-stock quando houver app ou integração aprovada;
- recomendação de produtos relacionados;
- melhoria de busca/filtros/sort;
- landing page/página promocional;
- blocos de reviews/Judge.me;
- tracking/event QA quando uma feature mexe no fluxo de compra.

Regra: feature nova exige escopo, dev theme ou ambiente seguro, QA, rollback e aprovação antes de produção.

### 5. Apps, integrações e tracking

LK Shopify pode diagnosticar e preparar mudanças relacionadas a apps/configurações quando o impacto for na superfície Shopify.

Exemplos:

- app de reviews;
- app de frete/estimador;
- app de wishlist/back-in-stock;
- pixels/events no tema;
- scripts no theme;
- integrações que afetam cart/PDP/collection.

Bloqueios:

- webhook/app/API/automação externa exigem aprovação separada;
- Klaviyo/Meta/GMC/ads não viram write por Shopify sem packet específico;
- nunca expor tokens/secrets.

## Pool recomendado de workers temporários

### 1. Shopify Surface Mapper

Identifica o objeto/superfície exata.

Entrega:

- tipo: product, variant, collection, page, theme, section, snippet, asset, menu, tag, metafield, SEO field, price, app/config, cart, search;
- handle/ID/URL/admin path quando disponível;
- estado atual;
- dependências;
- risco de tocar superfície errada.

### 2. Theme/Feature Architect

Projeta tecnicamente correções de tema e features como cart drawer.

Entrega:

- arquitetura da mudança;
- arquivos/sections/snippets/assets prováveis;
- dev theme necessário ou não;
- dependências de app/script;
- riscos de performance, UX e regressão;
- plano de implementação sem publicar.

### 3. CRO/UX Reviewer

Avalia impacto de conversão e experiência.

Entrega:

- fricção atual;
- hipótese CRO;
- melhoria esperada;
- métrica de follow-up;
- risco de piorar compra/mobile;
- recomendação de QA.

### 4. Price/Promo Change Controller

Controla mudanças de preço/promos já aprovadas.

Entrega:

- fonte/decisão aprovada;
- lista exata de produtos/variantes;
- preço atual e preço proposto;
- compare-at price quando aplicável;
- risco de overwrite por Tiny/feed/app;
- rollback e readback.

### 5. Preview/Diff Builder

Transforma demanda em preview técnico.

Entrega:

- antes/depois;
- diff textual/estrutural;
- campos/arquivos afetados;
- mutation/payload shape quando aplicável;
- status: local preview, dev theme, approval-ready ou blocked.

### 6. Shopify QA Visual Worker

Valida visualmente desktop/mobile.

Entrega:

- QA por viewport;
- screenshots quando aplicável;
- bugs visuais;
- checagem de CTA, imagem, espaçamento, contraste, legibilidade;
- risco para produção.

### 7. SEO/Metafield Checker

Valida campos técnicos Shopify.

Entrega:

- title/meta/handle/headings/alt/tags/metafields/schema;
- campos atuais e propostos;
- risco de canibalização ou sobrescrever campo bom;
- handoff para `[LK] Otimização de Coleções` se virar LKGOC.

### 8. App/Integration/Tracking Checker

Avalia dependências de app, script, pixel ou tracking.

Entrega:

- apps/scripts envolvidos;
- eventos afetados: add_to_cart, begin_checkout, purchase, view_item, etc.;
- risco de duplicar script/pixel;
- impacto em Klaviyo/Meta/GMC/analytics;
- bloqueio se exigir credencial, app install, webhook ou automação externa.

### 9. Rollback/Risk Reviewer

Classifica risco e bloqueia execução insegura.

Entrega:

- risco A0-A4;
- snapshot/backup necessário;
- dev theme/branch obrigatório para qualquer mudança de tema; produção/live nunca recebe write direto, apenas via GitHub PR → merge/deploy/readback;
- rollback viável;
- dependência Tiny/GMC/feed/app;
- aprovação necessária.

### 10. Readback/Receipt Verifier

Verifica execução aprovada.

Entrega:

- readback do objeto vivo;
- comparação com approval packet;
- evidência antes/depois;
- receipt Brain;
- pendências/follow-up.

## Seleção de workers por tipo de demanda

### Correção de tema simples

1. Shopify Surface Mapper
2. Theme/Feature Architect
3. Preview/Diff Builder
4. Shopify QA Visual Worker
5. Rollback/Risk Reviewer
6. Readback/Receipt Verifier após execução aprovada

### CRO/PDP/collection surface

1. Shopify Surface Mapper
2. CRO/UX Reviewer
3. Preview/Diff Builder
4. Shopify QA Visual Worker
5. Rollback/Risk Reviewer
6. Readback/Receipt Verifier após execução aprovada

Se for LKGOC/guia/experiência editorial de coleção, rotear o dono para `[LK] Otimização de Coleções`.

### Mudança de preço

1. Shopify Surface Mapper
2. Price/Promo Change Controller
3. Preview/Diff Builder
4. Rollback/Risk Reviewer
5. Readback/Receipt Verifier após execução aprovada

Preço precisa fonte/decisão aprovada e lista exata; estoque/disponibilidade continuam Tiny/LK Ops.

### Feature nova, como cart drawer

1. Shopify Surface Mapper
2. Theme/Feature Architect
3. CRO/UX Reviewer
4. App/Integration/Tracking Checker
5. Preview/Diff Builder
6. Shopify QA Visual Worker
7. Rollback/Risk Reviewer
8. Readback/Receipt Verifier após execução aprovada

Feature nova deve começar em PRD/preview/dev theme; produção só após aprovação escopada.

## Score técnico ampliado 0-100

- Escopo e objeto exato: 0-10
- Fonte/decisão viva quando envolve preço/produto/status: 0-10
- Arquitetura técnica/feature clara: 0-10
- Preview/diff claro: 0-15
- QA visual/mobile: 0-10
- Tracking/app/dependências avaliadas: 0-10
- Risco de produção baixo ou controlado: 0-10
- Rollback pronto: 0-10
- Readback verificável: 0-10
- Aderência a padrão LK/Shopify: 0-5

Classificação:

- 90-100: approval packet forte.
- 75-89: bom preview, mas precisa ressalva/QA adicional.
- 60-74: bloquear execução; faltam evidências.
- <60: gap report.

## Approval packet mínimo para feature/theme

Deve conter:

- objetivo da mudança;
- superfície exata;
- arquivos/objetos prováveis;
- preview/diff;
- dev theme ou ambiente de teste;
- QA desktop/mobile;
- impacto esperado;
- tracking/app risk;
- rollback;
- readback;
- frase de aprovação escopada.

## Frase de aprovação recomendada

> Aprovo LK Shopify executar exatamente este pacote: [ação], [alvo], [campos/arquivos], [dev theme ou produção], com snapshot/readback/receipt/rollback. Não aprovo alterações fora deste escopo, nem preço/estoque/campanha/app/webhook externo fora do que está listado.

## Critério de sucesso

LK Shopify está bem documentado quando consegue receber pedidos como:

- “corrigir esse bug no tema”;
- “melhorar o CRO dessa PDP”;
- “mudar preço desses produtos”;
- “criar cart drawer”;
- “implementar quick add”;
- “ajustar metafields/SEO fields”;
- “fazer readback do que foi alterado”;

…e transformar cada um em fluxo seguro: scope → workers certos → preview/diff → QA → risk/rollback → approval → execução escopada → readback/receipt.
