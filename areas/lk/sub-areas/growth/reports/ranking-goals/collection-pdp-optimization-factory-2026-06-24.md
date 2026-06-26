# LK Growth — Collection/PDP Optimization Factory — 2026-06-24

**Modo:** read-only / approval packet.  
**Writes externos:** 0. Sem Shopify/theme/GMC/feed/GA4/GSC/Klaviyo/WhatsApp/Ads/preço/estoque/desconto write.  
**values_printed:** false.  
**Rotina:** quarta-feira — Collection/PDP Optimization Factory.  
**Página foco:** `https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`.

## Veredito

Há achado material e decisão acionável: a página foco da semana deve ser o **PDP Onitsuka Tiger Mexico 66 Kill Bill**, mas **não recomendo write imediato** antes de fechar o D+7/D+14 da frente Onitsuka collection. O packet seguro agora é de **limpeza SEO/CRO/GEO do PDP**: corrigir meta truncada, unificar orientação de fit, revisar FAQ real-intent e alinhar Product/FAQ schema sem mexer em preço, estoque, desconto ou campanha.

Status: **decision-grade para preparar preview/approval packet**, por combinar Shopify/GA4/GSC do refresh, GSC router, QA público e SERP fallback. Limitações: DataForSEO MCP não exposto nesta runtime; PageSpeed/CrUX não foi reexecutado; estoque/Tiny não consultado por regra `lk-stock`.

## Por que esta página

- Decision-grade refresh 2026-06-23: PDP Kill Bill é P1, score 100, `decision_grade_refresh_ready_for_preview`.
- GA4/GSC refresh: **146 sessões**, **CVR 0,68%**, **11.070 impressões**, **CTR 0,42%**.
- Shopify/local combinado: **131 unidades**, **R$ 314.398,69** em vendas combinadas para priorização.
- GSC router: Onitsuka broad é maior ativo SEO (`onitsuka tiger` 110 cliques / 30.916 impressões / CTR 0,36% / posição 7,8), e o PDP Kill Bill é o principal best-seller/porta de decisão dentro do cluster.
- SERP fallback para `Onitsuka Tiger Mexico 66 forma grande pequena Brasil`: concorrente Accio aparece acima; LK collection aparece, mas o PDP precisa responder sizing/fit com mais clareza e menos conflito.

## Histórico verificado antes de recomendar

- `handoffs/theme-faq-onitsuka-lote1-20260616.md`: dois PDPs Onitsuka, incluindo Kill Bill, continuavam exibindo FAQ antigo/legado no HTML público após lote de FAQ.
- `reports/impact-reviews/onitsuka-tiger-improvement-20260617-queued.md`: D+7 programado para 2026-06-24 e D+14 para 2026-07-01.
- `reports/ranking-goals/mind002-onitsuka-readonly-execution-20260622.md`: Onitsuka broad e Mexico 66 já têm title/meta fortes e FAQPage único; recomendação era não mexer em title/meta collection e limpar apenas redundância visual.
- `receipts/shopify-production/onitsuka-visual-section-noop-production-20260622T195245Z.md`: produção já teve no-op visual legacy aprovado/aplicado; não sugerir a mesma correção como nova.

## QA público da página foco

| Campo | Estado |
|---|---|
| HTTP | 200 |
| Canonical | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo` |
| Title atual | `Onitsuka Tiger Mexico 66 Kill Bill Amarelo | LK Sneakers` — 56 chars |
| Meta atual | `Onitsuka Tiger Mexico 66 Kill Bill Amarelo original na LK Sneakers, com alta procura, curadoria premium, autenticidade garantida e compra segura em até…` — 152 chars |
| H1 | `Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo` |
| JSON-LD | 4 blocos; Product=1; FAQPage=1; Breadcrumb=1 |
| Reviews/prova social | página mostra 9 avaliações no resumo extraído |
| Risco público detectado | termo operacional `encomenda` apareceu no HTML público; não usar isso como SEO/copy pública nova |

## Diagnóstico SEO / CRO / GEO

### SEO

- Title atual está dentro do tamanho, mas pode capturar melhor a intenção `original`, `Kill Bill` e `Mexico 66` sem depender da collection.
- Meta atual termina truncada em `em até…`, o que enfraquece snippet/CTR e pode puxar linguagem de compra incompleta.
- Cluster Onitsuka tem demanda forte; o PDP deve linkar melhor para `/collections/onitsuka-tiger-todos-os-modelos` e `/collections/onitsuka-tiger-mexico-66` como caminhos de escolha, não só relacionados genéricos.

### CRO

- PDP tem prova social real; manter reviews próximos da decisão ajuda confiança.
- A orientação de fit aparece com duas ênfases: `fiel ao tamanho/forma estreita` e `subir meio número`. Isso pode travar escolha de tamanho. O ideal é uma resposta única, cautelosa e orientada por atendimento humano.
- Evitar qualquer reforço público de disponibilidade/prazo/estoque; se houver bloco operacional atual, tratar como ajuste CRO/theme separado com aprovação.

### GEO / AI Search

- Product, FAQPage e Breadcrumb já existem; oportunidade não é “adicionar schema”, mas garantir que o FAQ visível e o FAQPage tenham as mesmas perguntas e uma só orientação de fit.
- Faltam blocos mais citáveis para `Mexico 66 Kill Bill original`, `diferença Mexico 66 vs Mexico 66 SD`, `forma grande ou pequena` e `por que Kill Bill é procurado`.
- SERP fallback mostrou concorrentes e marketplace/brand assets; LK precisa responder como boutique/curadoria com autenticidade, contexto cultural e escolha assistida.

## Approval packet — preview proposto

### 1) SEO title

- **Atual:** `Onitsuka Tiger Mexico 66 Kill Bill Amarelo | LK Sneakers` — 56 chars
- **Proposto:** `Onitsuka Tiger Mexico 66 Kill Bill Original | LK` — 50 chars
- **Risco:** baixo; SEO field write exige aprovação explícita.

### 2) Meta description

- **Atual:** `Onitsuka Tiger Mexico 66 Kill Bill Amarelo original na LK Sneakers, com alta procura, curadoria premium, autenticidade garantida e compra segura em até…` — 152 chars
- **Proposta:** `Onitsuka Tiger Mexico 66 Kill Bill original na LK: colorway amarelo e preto, curadoria exclusiva, autenticidade e atendimento humano para escolher.` — 145 chars
- **Hipótese:** remover truncamento e linguagem incompleta, mantendo entidade + confiança + escolha assistida.

### 3) Bloco curto de decisão / copy citável

> O Onitsuka Tiger Mexico 66 Kill Bill é a colorway amarela e preta mais reconhecida do Mexico 66, associada ao visual usado por Uma Thurman em Kill Bill e à silhueta baixa da marca japonesa. Na LK, a curadoria prioriza pares originais, acabamento, proporção e orientação humana para comparar tamanho, material e uso com segurança antes da compra.

- Uso sugerido: próximo à descrição/FAQ, sem competir com CTA.
- Não mencionar estoque, pronta entrega, encomenda ou prazo.

### 4) FAQ — Real Intent Gate

| Pergunta proposta | Fonte de intenção | generic-filler |
|---|---|---:|
| O Onitsuka Tiger Mexico 66 Kill Bill é original? | objeção comercial específica + intenção `original` | false |
| Qual a diferença entre Onitsuka Tiger Mexico 66 e Mexico 66 SD? | comparação entre versões; GSC/cluster Mexico 66 | false |
| O Onitsuka Tiger Mexico 66 tem a forma grande ou pequena? | sizing/material; SERP fallback de forma/tamanho | false |
| Por que o Mexico 66 Kill Bill é tão procurado? | cultura pop/colorway específica | false |
| Como usar o Onitsuka Tiger Mexico 66 Kill Bill em looks atuais? | styling/decisão de compra | false |

**Resposta de fit recomendada:** não afirmar regra absoluta. Usar linguagem: forma baixa e mais estreita; se estiver entre tamanhos ou tiver pé largo, atendimento humano pode orientar a melhor escolha com base no uso e no calçado de referência.

### 5) Schema / QA

- Manter Product/Offer/AggregateRating/Breadcrumb existentes.
- Manter apenas **1 FAQ visível** e **1 FAQPage JSON-LD** com perguntas idênticas.
- Se o FAQ legado ainda aparecer no render final, o write precisa passar por dev-theme/preview, não só `descriptionHtml`.

### 6) Linkagem interna

- PDP Kill Bill → `/collections/onitsuka-tiger-mexico-66` com âncora `ver outros Onitsuka Tiger Mexico 66`.
- PDP Kill Bill → `/collections/onitsuka-tiger-todos-os-modelos` com âncora `comparar Onitsuka Tiger na curadoria LK`.
- Collection Onitsuka broad/Mexico 66 → manter Kill Bill como destaque/best-seller quando aplicável, sem alterar ordenação/estoque.

## Métrica de sucesso

- **GSC:** CTR do PDP Kill Bill e queries `onitsuka tiger mexico 66 kill bill`, `mexico 66 kill bill`, `onitsuka tiger original`.
- **CTR alvo inicial:** PDP sair de 0,42% para ≥0,75% sem queda material de posição.
- **GA4/Shopify:** sessões orgânicas do PDP, PDP views, add-to-cart e conversão; Shopify segue fonte oficial de pedidos/receita.
- **GEO:** FAQPage único; resposta citável para `forma`, `original`, `Mexico 66 vs SD` e `Kill Bill`.

## Risco / rollback / aprovação necessária

- **Risco:** baixo para SEO title/meta; médio para FAQ/copy visível por depender de theme/PDP FAQ legado.
- **Rollback:** snapshot de `seo.title`, `seo.description`, `descriptionHtml`, FAQ/schema e asset/section se o tema estiver envolvido; reverter campo a campo se D+7/D+14 indicar queda de CTR/conversão ou render duplicado.
- **Aprovação necessária:** qualquer Shopify SEO field, description, FAQ, schema ou theme/dev-theme write exige aprovação explícita atual de Lucas. Dev-theme preview também é write e precisa aprovação.

## Próximo passo recomendado

1. Fechar D+7 Onitsuka collection em read-only antes de aplicar qualquer mudança nova.
2. Se Lucas aprovar, preparar **DEV preview** para o PDP Kill Bill quando o ajuste tocar FAQ/theme legado; se for só SEO title/meta, executar via Shopify Admin com rollback/readback após aprovação específica.

## Não executado

- Nenhum write Shopify, theme, GMC/feed, GA4/GSC config, Ads, Klaviyo, WhatsApp, preço, desconto ou estoque.
- Não consultei Tiny/estoque; disponibilidade operacional pertence ao `lk-stock`.
- Não publiquei title/meta/copy/FAQ/schema/internal links; tudo está em preview/approval packet.
