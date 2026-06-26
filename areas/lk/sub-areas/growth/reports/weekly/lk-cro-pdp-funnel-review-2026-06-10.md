# LK CRO/PDP Funnel Review — 2026-06-10

- Rotina: semanal read-only — LK CRO/PDP Funnel Review.
- Janela principal: GA4/Klaviyo/Shopify últimos 7 dias até 2026-06-09/10; Shopify decision refresh desde 2026-04-17.
- Postura: **read-only/preview**.
- Writes externos: **0**.
- Produção/Shopify/theme/checkout/Klaviyo/WhatsApp/Ads: **não alterado**.

## Veredito executivo

**Gargalo principal: PDP mobile / decisão antes de adicionar ao carrinho.**

O checkout não aparece como o primeiro gargalo nesta semana: o maior vazamento está antes, entre visualização de PDP/listagem e `add_to_cart`.

Evidência principal:

- GA4 mobile: **42.609 sessões**, **574 add_to_cart**, **149 checkouts**, **35 purchases**, **R$ 80.752,88** de receita reportada.
- Mobile ratios:
  - add_to_cart / sessions: **1,35%**.
  - begin_checkout / sessions: **0,35%**.
  - purchases / sessions: **0,082%**.
  - add_to_cart → checkout: **26,0%**.
  - checkout → purchase: **23,5%**.
- Eventos GA4 sitewide:
  - `view_item`: **54.318**.
  - `add_to_cart`: **765**.
  - `begin_checkout`: **210**.
  - `purchase`: **44**.
  - `view_item → add_to_cart`: **1,41%**.
- Shopify últimos 7 dias: **85 pedidos lidos**, **78 válidos**, **R$ 214.309,73**, sendo **53 web** e **25 POS**.
- Produto campeão Shopify 7d: **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo** com **9 unidades**.
- PageSpeed/CrUX no PDP Nike Mind Black Chrome: LCP **1.367 ms bom**, FCP **1.211 ms bom**, CLS **0,00 bom**, TTFB **589 ms bom**. Performance não é o gargalo primário deste PDP.

Nível de confiança: **alto para direção do gargalo PDP/mobile**, médio para atribuição por página específica porque GA4 e Shopify usam janelas/atribuições diferentes e Klaviyo commerce está zerado.

## Fontes verificadas

- Readiness local: `/opt/data/profiles/lk-growth/scripts/lk_growth_tooling_readiness.py --json` → OK; GA4/GSC/PageSpeed/Klaviyo/Ahrefs declarados disponíveis; sem imprimir secrets.
- GA4 Data API read-only:
  - dispositivo/funil: sessões, usuários, add_to_cart, checkout, purchase, revenue.
  - eventos essenciais: `view_item`, `view_item_list`, `add_to_cart`, `view_cart`, `begin_checkout`, `purchase`.
  - landing pages mobile.
- Shopify Admin REST read-only:
  - pedidos últimos 7 dias, source, landing_site e line items agregados.
- Shopify/commercial decision refresh:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-seo-cro-decision-grade-refresh-2026-05-18.md` atualizado na execução atual, com vendas Shopify ao vivo até 2026-06-10.
- PageSpeed/CrUX wrapper read-only:
  - `/opt/data/profiles/lk-growth/scripts/lk_pagespeed_crux_readonly.py` para PDP Nike Mind Black Chrome.
- Klaviyo analytics read-only:
  - métricas encontradas: Active on Site, Placed Order, Added to Cart, Clicked Email, Started Checkout, Opened Email, Received Email.
  - agregados de commerce/engajamento vieram **0** na janela, tratado como lacuna de tracking/atribuição CRM, não como prova de ausência de demanda.
- Ahrefs read-only:
  - domain rating **35,0**; usado apenas como sinal off-site contextual.
- QA público HTML mobile-user-agent, sem interação de compra:
  - PDP Nike Mind Black Chrome.
  - PDP Nike Vomero Premium Flat Stout.
  - Collection Onitsuka Tiger.
  - Collection Lululemon.

## Fontes parciais/ausentes

- Metricool/Meta Ads: não houve ferramenta MCP disponível neste runtime; usei UTMs/landing_site Shopify como proxy de paid/social demand.
- Checkout real: não testei fluxo interativo nem criei carrinho/checkout para evitar side effect; usei GA4 + Shopify read-only.
- Reviews/Judge.me: presença pública detectada, mas não consultei API/app interna de reviews.
- GSC granular do dia: usado via refresh comercial existente e relatórios recentes; não rodei nova extração GSC por página nesta rotina focada em funil.
- DataForSEO/AI visibility: não material para o gargalo de conversão desta semana; não foi acionado.

## Gargalo principal — PDP mobile antes do carrinho

### Por que é o gargalo

1. O mobile concentra a maior parte do tráfego e receita GA4 da semana, mas o `add_to_cart/session` é baixo: **1,35%**.
2. O vazamento `view_item → add_to_cart` é maior do que o vazamento no checkout: apenas **1,41%** dos `view_item` viram add_to_cart, enquanto **21,0%** dos checkouts viram purchase.
3. Produtos e coleções com alta demanda aparecem com sessões e add_to_cart, mas sem checkout na semana:
   - `/products/tenis-nike-vomero-premium-flat-stout-marrom...`: **237 sessões mobile**, **6 add_to_cart**, **0 checkout**, **0 purchase**.
   - `/products/slide-nike-mind-001-black-chrome-preto`: **96 sessões mobile**, **3 add_to_cart**, **0 checkout**, **0 purchase**.
   - `/collections/onitsuka-tiger-todos-os-modelos`: **244 sessões mobile**, **6 add_to_cart**, **0 checkout**, **0 purchase**.
   - `/collections/lululemon`: **187 sessões mobile**, **5 add_to_cart**, **0 checkout**, **0 purchase**.
4. O PDP Nike Mind Black Chrome tem CrUX bom; não parece ser problema primário de velocidade.
5. QA público mostrou que CTA, preço, WhatsApp/chat, Judge.me, Product schema e FAQPage existem — logo o problema provável é **hierarquia/clareza/convencimento acima da dobra e confiança de decisão**, não ausência absoluta dos elementos.

### Observação de guardrail de copy

No PDP Nike Mind Black Chrome, o HTML público contém FAQ com a frase: **“Itens sob encomenda seguem prazo estimado de 4 a 6 semanas”**. Isso conflita com o guardrail LK atual de não usar `sob encomenda/pronta entrega/estoque` como taxonomia pública. Não alterei nada; recomendo tratar como microteste de copy/FAQ em preview.

Nas collections, o filtro público ainda expõe **“Disponibilidade / Em estoque”** como linguagem de filtro. Isso pode ser tema/filtro nativo e exige cuidado; não é recomendado mexer sem pacote visual/Shopify próprio.

## Testes pequenos recomendados

### Teste 1 — PDP mobile: compactar decisão acima da dobra nos PDPs P1

- Alvos iniciais sugeridos:
  - `slide-nike-mind-001-black-chrome-preto`.
  - `tenis-nike-vomero-premium-flat-stout-marrom`.
  - opcionalmente `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo` por volume Shopify, mas com cuidado porque já vende bem.
- Hipótese: melhorar a leitura mobile de mídia → nome/marca → preço → tamanho → CTA → trust/atendimento aumenta `add_to_cart/session`.
- Mudança proposta em preview DEV, sem produção:
  - garantir que `Adicionar ao carrinho` fique visualmente dominante no mobile;
  - manter `Compre Já` apenas se não competir com o CTA primário;
  - trust/atendimento humano discreto abaixo dos botões, sem bloco pesado;
  - evitar frases redundantes repetindo o título do produto;
  - não usar copy pública de `pronta entrega/sob encomenda/estoque`.
- Impacto esperado: alto.
- Esforço: médio.
- Risco: médio visual; baixo operacional se feito em dev theme.
- Rollback: reverter asset/section/snippet do dev theme; produção intacta até aprovação.
- Métrica primária: `add_to_cart/session` mobile por PDP.
- Métricas secundárias: `begin_checkout/session`, purchases, revenue, click WhatsApp se mensurado.
- Janela de revisão: D+7 e D+14 após publicação aprovada.
- Aprovação necessária: **sim** para qualquer theme/Shopify write; LK Growth pode preparar packet/handoff sem write.

### Teste 2 — FAQ/copy PDP: remover taxonomia pública de “sob encomenda” em PDPs P1

- Alvo inicial: PDP Nike Mind Black Chrome e próximos PDPs P1 com FAQ semelhante.
- Hipótese: uma resposta de prazo com linguagem premium e atendimento humano reduz fricção sem criar taxonomia operacional pública.
- Preview de direção de copy, não aplicado:
  - substituir prazo operacional rígido por: “O prazo pode variar por tamanho/modelo e região. A LK confirma disponibilidade e prazo no atendimento humano antes da finalização quando necessário.”
  - manter autenticidade, curadoria exclusiva e confirmação via chat como reforço.
- Impacto esperado: médio em confiança; alto em aderência de marca/guardrail.
- Esforço: baixo/médio, depende se está em tema, metafield, template ou body/schema.
- Risco: baixo se escopo for FAQ/copy; risco médio se envolver template global.
- Rollback: snapshot do conteúdo/asset anterior e restauração do FAQ anterior.
- Métrica primária: `add_to_cart/session` mobile nos PDPs alterados.
- Métrica secundária: cliques em chat/WhatsApp e checkout/session.
- Janela de revisão: D+7.
- Aprovação necessária: **sim** para qualquer alteração visível em Shopify/theme.

### Teste 3 — Collections → PDP: handoff de collection UX sem LKGOC nesta rotina

- Alvos com evidência mobile nesta semana:
  - `/collections/onitsuka-tiger-todos-os-modelos`: **244 sessões mobile**, **6 add_to_cart**, **0 checkout**.
  - `/collections/lululemon`: **187 sessões mobile**, **5 add_to_cart**, **0 checkout**.
- Hipótese: filtros/ordenação/cards e atalhos de decisão precisam ajudar o usuário a chegar no PDP certo; collection não deve virar novo LKGOC neste cron.
- Direção de teste:
  - QA mobile de cards, preço, foto principal, filtros e ordenação;
  - reduzir ruído de “Disponibilidade/Em estoque” se confirmado como visualmente dominante;
  - manter coleção product-first e rotear qualquer otimização textual/guia para `[LK] Otimização de Coleção`.
- Impacto esperado: médio/alto para Onitsuka; médio para Lululemon.
- Esforço: médio.
- Risco: médio porque envolve collection UI e possivelmente filtros.
- Rollback: dev theme snapshot; produção intacta até approval.
- Métrica primária: collection landing → PDP click/select_item e add_to_cart/session dos produtos vindos da coleção.
- Janela de revisão: D+7/D+14.
- Aprovação necessária: **sim** para qualquer theme/collection write; handoff recomendado antes.

## Handoff obrigatório — [LK] Otimização de Coleção

Não executei LKGOC nem modifiquei coleção.

Handoff recomendado para `[LK] Otimização de Coleção`:

- Escopo: avaliar Onitsuka Tiger e Lululemon apenas como **gargalo Collection → PDP**, não como LKGOC automático.
- Evidência: sessões mobile relevantes, add_to_cart baixo e zero checkout/purchase na janela GA4; Onitsuka é P1 comercial no decision refresh.
- Pedido para Lucas aprovar/ver: preparar preview DEV de UX collection/cards/filtros/ordenação, mantendo copy premium e sem taxonomia pública de estoque.
- Produção: bloqueada até aprovação explícita.

## Mensuração / QA de eventos

Eventos essenciais existem no GA4:

- `view_item` OK.
- `view_item_list` OK.
- `add_to_cart` OK.
- `view_cart` OK.
- `begin_checkout` OK.
- `purchase` OK.

Ponto de atenção:

- Klaviyo encontrou as métricas esperadas, mas agregou **0** em commerce/engajamento nos últimos 7 dias. Como Shopify e GA4 mostram atividade forte, isso sugere lacuna de ingestão/atribuição Klaviyo ou ausência de eventos associados à API consultada. Não recomendo decisão de CRM baseada nesse zero sem diagnóstico específico.

## Status dos 18 tópicos canônicos nesta rotina CRO

1. GA4: **verificado** — funil/device/events/landing mobile.
2. GSC: **parcial** — usado via refresh/relatórios recentes, sem nova extração granular.
3. GMC: **não material nesta rotina** — sem write; não houve novo diagnóstico GMC.
4. Shopify SEO: **parcial** — QA público de title/H1/schema; sem edição.
5. Shopify CRO: **verificado** — PDP mobile, collections, CTA/trust/copy por QA público + GA4.
6. GEO/AI Search: **não material** para o gargalo desta semana.
7. PageSpeed/CrUX/CWV: **verificado** para PDP Nike Mind Black Chrome; bom.
8. Schema: **parcial** — Product/FAQPage detectados publicamente; sem validação rich-results completa.
9. Reviews/prova social: **parcial** — Judge.me detectado publicamente; sem API interna.
10. Paid media: **parcial** — UTMs/landing_site Shopify usados; Metricool/Meta MCP não disponível neste runtime.
11. Influencer/social demand: **parcial** — Shopify landing_site contém UTMs de influencer/paid social; sem Metricool/FHITS.
12. Concorrência/SERP: **não acionado**; não necessário para o gargalo de funil desta semana.
13. Google Business/local: **não aplicável** nesta rotina.
14. Klaviyo/CRM: **verificado, mas lacuna** — métricas existem, agregados 0; precisa diagnóstico.
15. Catálogo/product data quality: **parcial** — sem foco GMC; PDP público OK para preço/schema básico.
16. Conteúdo/taxonomia comercial: **verificado** — risco detectado em copy `sob encomenda` e filtro `Em estoque`.
17. Mensuração/QA de eventos: **verificado** — eventos GA4 essenciais presentes; divergência GA4 ↔ Shopify/Klaviyo declarada.
18. Impact review/experimentation: **definido** — D+7/D+14 para testes propostos.

## O que posso preparar sem aprovação

- Packet de CRO PDP mobile para 2 PDPs P1, com antes/depois, selectors prováveis, QA checklist e rollback.
- Handoff formal para LK Shopify preparar preview no dev theme.
- Handoff para `[LK] Otimização de Coleção` avaliar Onitsuka/Lululemon como Collection → PDP, sem executar LKGOC.
- Diagnóstico específico Klaviyo tracking read-only.

## O que exige aprovação antes de executar

- Qualquer alteração em Shopify product/page/collection/theme.
- Qualquer ajuste de FAQ/copy visível.
- Qualquer mudança em filtro/ordenação/cards/collection UI.
- Qualquer alteração de checkout, Klaviyo, WhatsApp, e-mail, Meta/Google Ads ou campanha.

## Arquivos/evidências locais geradas

- GA4 funnel JSON: `/tmp/lk_cro_ga4_20260610.json`.
- Shopify orders 7d JSON: `/tmp/lk_shopify_orders_7d_20260610.json`.
- PageSpeed/CrUX PDP JSON: `/tmp/lk_cro_pagespeed_pdp_nike_mind_20260610.json`.
- Klaviyo JSON: `/tmp/lk_cro_klaviyo_20260610.json`.
- Ahrefs JSON: `/tmp/lk_cro_ahrefs_20260610.json`.
- QA público JSONL: `/tmp/lk_cro_public_qa_20260610.jsonl`.

## Não feito

- Nenhum write externo.
- Nenhuma criação de carrinho/checkout real.
- Nenhum publish, theme upload, Shopify mutation, Klaviyo send, WhatsApp, campanha ou feed/GMC.
- Nenhum uso de estoque/Tiny como critério de priorização SEO/CRO.
