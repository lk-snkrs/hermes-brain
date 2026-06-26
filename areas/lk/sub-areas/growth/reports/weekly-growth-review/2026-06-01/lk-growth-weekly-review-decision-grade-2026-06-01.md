# LK Growth OS — Weekly Growth Review decision-grade

**Data:** 2026-06-01  
**Janela principal:** evidências read-only disponíveis até 2026-05-31 / Meta Ads 2026-05-25 a 2026-05-31  
**Modo:** read-only / preview-only  
**Writes executados:** 0  
**Segredos impressos:** não  

## Resumo executivo

**Veredito:** a LK tem base Growth saudável e dados comerciais suficientes para priorizar a semana, mas há 4 frentes que merecem ação agora: PDPs com tráfego alto e baixa conversão, coleções fortes sem camada GEO/FAQPage completa, Merchant local inventory com reprovação massiva de `link_template`, e funil pago com muito clique barato mas baixa passagem para landing/page decision.

**Nota Growth operacional atual:** **76/100**  
**Nota pública SEO/CRO técnica:** **88/100**  
**Meta próxima:** **80/100 operacional** sem produção automática; subir por packets aprováveis.

Por que 76 e não mais alto:

- Shopify/GA4/GMC/Meta read-only estão utilizáveis o suficiente para priorização comercial.
- PageSpeed público/lab está bom, mas o conector PageSpeed deu timeout e CrUX retornou 404 sem field record nesta rodada.
- GSC direto não foi reconsultado nesta execução; há sinais derivados/relatórios anteriores, mas a cobertura de CTR/query por página fica **parcial**.
- Merchant tem preço final limpo, mas ainda carrega um problema crítico local: **10.436 ofertas locais reprovadas em Shopping por `mhlsf_full_missing_valid_link_template`**.

## Fontes consultadas

- **Brain / checklist canônico:** `ESCOPO-18-TOPICOS.md`.
- **Connector probe read-only:** Google token OK; GA4 LK OK; GA4 generic 403; PageSpeed timeout; CrUX 404 sem record.
- **GMC weekly review 2026-05-31:** 21.338 productstatuses + 21.338 products.
- **Collections SEO/GEO 2026-05-31:** 179 coleções Shopify Admin read-only; GA4 collections 90d; HTML público.
- **PDP Priority 2026-05-31:** 1.805 produtos active/published; 2.426 linhas GA4 PDP; Shopify live catch-up de pedidos.
- **Mobile/Visual + Claude SEO audit 2026-05-31:** home, collections, PDP, busca, carrinho, robots, llms.txt.
- **Meta Ads read-only:** account last_7d, 2026-05-25 a 2026-05-31.
- **DataForSEO SERP/keyword:** consultas mobile Brasil para New Balance 204L e Onitsuka Tiger Mexico 66 + volumes de termos P1.

## Alertas / anomalias

1. **GMC local inventory / Shopping:** `mhlsf_full_missing_valid_link_template` em **10.436 ofertas locais**. Isso é P0 de Merchant health, mas exige investigação read-only da origem local inventory / link_template antes de qualquer feed/ProductInput write.
2. **PDP com demanda alta e vazamento:** `Yeezy Foam Runner MX Cinder` tem **30.811 views 90d e 0 pedidos/receita** no relatório PDP; precisa packet de decisão, não alteração automática.
3. **PDPs líderes com title longo e alt faltante:** Top PDPs como Nike Moon Shoe Jacquemus, Onitsuka Sabot, Samba OG Crochet e NB 1906L aparecem com título longo/imagens sem alt.
4. **Coleções estratégicas sem FAQPage parity:** New Balance, Lançamentos, Adidas, Nike e Air Jordan aparecem com FAQ visível sem FAQPage schema ou descrições curtas/ausentes; isso reduz elegibilidade para resposta/citação estruturada.
5. **Meta Ads com ROAS forte, mas atrito de landing:** Meta Ads reportou spend **R$ 7.301,03**, 19.758 clicks, 6.415 landing page views, 181 add to cart, 32 checkouts e 31 purchases. ROAS de plataforma **10,36**, mas click → LPV é **32,47%** e LPV → ATC **2,82%**; isso sugere gargalo de carregamento/qualificação/landing ou tracking, não necessariamente problema de mídia.
6. **PageSpeed/CrUX não decision-grade nesta execução:** Lighthouse público anterior está bom, mas o conector PageSpeed timeout e CrUX 404 impedem afirmar CWV field data atual.
7. **Metricool incompleto:** Meta via Metricool retornou HTTP 500; Google Ads via Metricool retornou `[]`. Usei Meta Ads direto como fonte parcial.

## Oportunidades Top 5 — impacto / esforço / risco

### 1) PDP CRO/SEO packets para Top 5 páginas de demanda e vazamento

**Fato verificado:** Top PDPs por relatório decision-grade de 2026-05-31:

- Nike Moon Shoe SP Jacquemus Alabaster — 24.321 views 90d, 53 pedidos, R$ 292.399,46, CVR proxy 0,22%.
- Onitsuka Tiger Mexico 66 Sabot Birch Peacoat — 19.423 views, 24 pedidos, R$ 54.999,75, CVR 0,12%.
- Adidas Samba OG Crochet Pack Sand Strata — 11.203 views, 35 pedidos, R$ 85.799,61, CVR 0,31%.
- Yeezy Foam Runner MX Cinder — 30.811 views, 0 pedidos, R$ 0, CVR 0,00%.
- New Balance 1906L Khaki — 9.907 views, 10 pedidos, R$ 27.499,89, CVR 0,10%.

**Interpretação:** há tráfego suficiente para justificar melhoria de decisão mobile, title/meta, alt e micro-FAQ por produto. O caso Yeezy é alerta máximo: tráfego alto sem venda.

**Recomendação:** gerar packets preview-only por PDP com:

- SEO title/meta propostos;
- bloco de decisão mobile sem copy redundante;
- FAQ curto por objeção de compra;
- checklist Product schema / reviews / imagem alt;
- hipótese + métrica D+7.

**Impacto:** alto.  
**Esforço:** médio.  
**Risco:** baixo se ficar em preview/dev.  
**Rollback:** reverter SEO fields/body/theme ao snapshot anterior se aprovado no futuro.  
**Aprovação necessária:** sim, antes de qualquer Shopify SEO/body/theme/image write.

### 2) Coleções com tráfego + gap GEO: New Balance, Lançamentos e Air Jordan/Lululemon

**Fato verificado:** relatório de coleções leu 179 coleções e GA4 collections 90d. Destaques:

- `new-balance`: 4.886 views 90d, body words 0, FAQ visível sem FAQPage, imagens sem alt.
- `lancamentos`: 4.510 views 90d / 284 views 30d, FAQ sem FAQPage, meta curta.
- `air-jordan`: 4.982 views 90d / 980 views 30d, body 495 words, FAQ sem FAQPage.
- `lululemon`: 4.691 views 90d / 1.299 views 30d, FAQPage OK, mas title/meta curtos e alt faltante.

**Interpretação:** coleções já recebem demanda; a oportunidade é transformar páginas comerciais em ativos citáveis e mais claros para IA/Google sem perder produto-first.

**Recomendação:** preparar 3 packets de coleção:

1. New Balance — maior lacuna estrutural.
2. Lançamentos — alta intenção e frescor.
3. Air Jordan ou Lululemon — escolher por prioridade comercial da semana.

Cada packet deve incluir title/meta, intro mobile, FAQ visível + FAQPage, links internos e, se necessário, source-page/guia editorial.

**Impacto:** alto.  
**Esforço:** médio.  
**Risco:** médio se mexer em coleção/tema; baixo enquanto preview.  
**Rollback:** snapshot de SEO fields/description/theme section antes de qualquer write futuro.  
**Aprovação necessária:** sim para produção; dev theme também exige aprovação por ser write.

### 3) GMC P0 local `link_template` + P1 color/data quality

**Fato verificado:** GMC 2026-05-31:

- 21.338 productstatuses e products, sem divergência de cobertura.
- `price_mismatch`: 0; `price_out_of_range`: 0.
- `mhlsf_full_missing_valid_link_template`: 10.436 ofertas locais reprovadas em Shopping.
- `landing_page_error`: 17 instâncias / 15 produtos.
- `missing_item_attribute_for_product_type`: 2.772 instâncias / 1.239 produtos.
- Preview de cor: 925 high-confidence, 314 revisão humana.

**Interpretação:** preço está verde; próximo impacto em Merchant é data quality/local feed. O `link_template` não deve ser tratado como 404 ou preço — é investigação de data source/local inventory.

**Recomendação:** criar packet read-only de investigação:

- mapear data source local / store code / link_template;
- amostrar 20 ofertas locais `local:*`;
- separar erro de template vs PDP real;
- manter missing color em pacote separado e só high-confidence.

**Impacto:** alto para Shopping/local.  
**Esforço:** médio/alto.  
**Risco:** alto se escrever feed errado; baixo em diagnóstico.  
**Rollback:** obrigatório antes de qualquer feed/ProductInput/datafeed write.  
**Aprovação necessária:** sim para qualquer GMC/feed write/fetchNow.

### 4) Paid → Landing CRO: usar Meta Ads como sinal de gargalo, não como verdade financeira final

**Fato verificado:** Meta Ads account last_7d:

- Spend: R$ 7.301,03.
- Impressions: 356.552.
- Clicks: 19.758.
- Landing page views: 6.415.
- Add to cart: 181.
- Initiate checkout: 32.
- Purchases: 31.
- Purchase value: R$ 75.675,15.
- ROAS plataforma: 10,36.
- Métricas derivadas: CTR 5,54%, CPC R$ 0,37, CPLPV R$ 1,14, click→LPV 32,47%, LPV→ATC 2,82%, CPA purchase R$ 235,52, AOV R$ 2.441,13.

**Interpretação:** mídia parece eficiente em plataforma, mas a transição clique → landing e landing → carrinho merece auditoria por criativo/UTM/landing/PDP. Como é `platform_signal`, deve ser reconciliado com Shopify/GA4 antes de decisão de orçamento.

**Recomendação:** gerar um mapa read-only campanha → landing/PDP/coleção para cruzar com Top PDPs e coleções. Não alterar orçamento/campanhas.

**Impacto:** médio/alto.  
**Esforço:** baixo/médio.  
**Risco:** baixo em análise; alto se mexer em campanha sem reconciliação.  
**Rollback:** não aplicável em read-only; se houver campanha futura, snapshot de budget/adset/ad antes.  
**Aprovação necessária:** sim para qualquer Meta/Google Ads write.

### 5) Correções globais low-risk de semântica pública: OG, H1 carrinho, parser HTML e alt

**Fato verificado:** auditoria mobile/visual 2026-05-31:

- Home Performance ~0,89 / SEO ~0,92, mas title 78 caracteres e meta 187 caracteres.
- OG title da home está genérico: `LK`.
- Carrinho vazio não tem H1; mensagem principal é H2.
- DataForSEO sinalizou erro de HTML parser em várias páginas.
- `llms.txt` existe, responde 200 e tem ~49 KB.

**Interpretação:** performance não é o gargalo principal; semântica/HTML/SEO social e pequenos bugs de estrutura podem elevar score e confiança de crawlers/IA.

**Recomendação:** preparar approval packet técnico com before/after para:

- OG home;
- title/meta principais;
- H1 do carrinho;
- parser mismatch em componente global/footer/newsletter;
- alt faltante em imagens prioritárias.

**Impacto:** médio.  
**Esforço:** baixo/médio.  
**Risco:** médio se theme production; baixo em dev/preview.  
**Rollback:** backup de asset/theme + SEO fields antes de qualquer aplicação.  
**Aprovação necessária:** sim para theme/Shopify production; dev theme também precisa aprovação.

## SERP / demanda — sinais vivos

### New Balance 204L

- DataForSEO Brasil/mobile: `new balance 204l` com volume 9.900, competição alta, intent transactional.
- Tendência anual reportada: +404.900%; trimestre +650%.
- SERP mobile para `new balance 204l original brasil`: domínio oficial New Balance domina posições orgânicas 1–5; LK aparece em Popular Products como seller para `Tênis New Balance 204L Mushroom Arid Stone Marrom`, preço R$ 2.799,99.
- Interpretação: LK tem presença comercial em merchant card, mas o texto orgânico é dominado pela marca oficial; precisa source/collection content para capturar intenção `onde comprar`, `original`, `feminino`, `bege`, etc.

### Onitsuka Tiger Mexico 66

- DataForSEO Brasil/mobile: `onitsuka tiger mexico 66` com volume 6.600, competição alta, intent transactional.
- SERP mobile para `onitsuka tiger mexico 66 original brasil`: LK rankeia **#1 orgânico** com a coleção `onitsuka-tiger-mexico-66`.
- PAA inclui: “Onde comprar Onitsuka Tiger original no Brasil?”, “Qual a diferença entre Asics e Onitsuka Tiger?”, etc.
- Interpretação: esta é uma página que já venceu parte da SERP; deve receber proteção e melhoria medida, não reescrita agressiva.

## 18 tópicos — cobertura

| # | Tópico | Status | Evidência / limite |
|---|---|---|---|
| 1 | GA4 | **Verificado parcial** | GA4 LK property OK; relatórios PDP/collections usam GA4 90d. Funil GA4 completo PDP→checkout não foi reextraído nesta rodada. |
| 2 | GSC | **Parcial / pendente** | Há histórico/roteadores, mas não houve extração GSC live nesta execução; CTR/query por URL fica não decision-grade. |
| 3 | GMC | **Verificado** | GMC weekly 2026-05-31 com 21.338 statuses/products; preço final limpo; link_template/local e missing attrs pendentes. |
| 4 | Shopify SEO | **Verificado parcial** | Shopify Admin read-only em coleções/PDPs; title/meta/H1 públicos avaliados; nenhum SEO field write. |
| 5 | Shopify CRO/theme | **Verificado parcial** | Auditoria mobile/visual pública; nenhum dev/prod theme write. |
| 6 | GEO / AI Search | **Verificado parcial** | `llms.txt` 200; coleção/PDP com gaps FAQPage/citability; SERP DataForSEO para 204L/Onitsuka. Sem baseline ChatGPT/Perplexity live. |
| 7 | PageSpeed / CrUX / CWV | **Parcial** | Lighthouse público bom; PageSpeed connector timeout; CrUX 404 sem field record. Não decision-grade para field CWV. |
| 8 | Schema | **Parcial** | PDP exemplo com Product/Breadcrumb/FAQPage forte; várias coleções com FAQ visível sem FAQPage. |
| 9 | Reviews / prova social | **Parcial** | PDP exemplo tem reviews/schema; Judge.me/review coverage por catálogo não foi rechecada live. |
| 10 | Paid media | **Verificado parcial** | Meta Ads account last_7d obtido; Metricool Meta 500; Metricool Google Ads `[]`; plataforma precisa reconciliação Shopify/GA4. |
| 11 | Influencer/social demand | **Parcial** | SERP social/Instagram aparece em 204L; sem FHITS/influencer live nesta rodada. |
| 12 | Concorrência/SERP | **Verificado parcial** | SERP mobile Brasil para 204L e Onitsuka; não é auditoria competitiva completa. |
| 13 | Google Business/local SEO | **Pendente/parcial** | Local inventory GMC analisado; GBP/local profile não auditado nesta rodada. |
| 14 | Klaviyo/CRM signals | **Pendente** | Não reconsultado nesta rotina; sem sends ou alterações. |
| 15 | Catálogo/product data quality | **Verificado** | GMC missing attributes/color + Shopify 1.805 active/published + PDP candidate set. |
| 16 | Conteúdo/taxonomia comercial | **Verificado parcial** | Coleções estratégicas e PDPs priorizados; taxonomia completa/menu não auditada ponta a ponta. |
| 17 | Mensuração/QA de eventos | **Parcial** | Meta events disponíveis; GA4 probe OK; discrepâncias click→LPV e PageSpeed/CrUX limitam decisão. |
| 18 | Impact review/experimentation | **Parcial / pendente** | Existem filas e hipóteses; D+7/D+14 precisa ser amarrado a cada packet aprovado. |

## Pacotes de decisão / approval sugeridos

### Packet A — PDP Top 5 CRO/SEO preview

**Escopo:** 5 PDPs citados no Top 5.  
**Preview:** title/meta, decisão mobile, FAQ, schema/alt checklist.  
**Não autoriza:** Shopify write, tema, imagens, preço, estoque, GMC, campanhas.  
**Aprovação futura necessária:** “Aprovo aplicar Packet A em dev/SEO fields para os 5 PDPs listados”.

### Packet B — 3 coleções GEO/FAQPage preview

**Escopo recomendado:** New Balance, Lançamentos, Air Jordan ou Lululemon.  
**Preview:** copy demand-led, FAQ natural, FAQPage JSON-LD, links internos, source-page se necessário.  
**Não autoriza:** publicação em collection description/theme production.  
**Rollback futuro:** snapshot dos SEO fields/descriptionHtml/theme assets.

### Packet C — GMC local link_template investigation

**Escopo:** read-only map de `local:*`, data source, store code, link_template e amostra de 20 ofertas.  
**Não autoriza:** ProductInput/datafeed/feed rule/fetchNow.  
**Aprovação futura:** só após diagnóstico e rollback claro.

### Packet D — Paid landing reconciliation

**Escopo:** campanha/adset/ad → landing/PDP/collection → GA4/Shopify outcome.  
**Não autoriza:** budget, campanha, criativo ou público.  
**Decisão esperada:** quais landings/PDPs entram no sprint CRO da semana.

### Packet E — Semântica global low-risk em dev

**Escopo:** OG home, H1 cart, parser HTML, alt prioritário, title/meta home preview.  
**Não autoriza:** production theme.  
**Regra:** dev theme/preview primeiro; produção só com aprovação separada.

## Próximos passos seguros

1. **Preparar Packet A** com os 5 PDPs prioritários e before/after exato.
2. **Preparar Packet B** para 3 coleções, mantendo padrão produto-first e FAQ por objeção real.
3. **Rodar investigação read-only do GMC `link_template`** antes de qualquer proposta de correção.
4. **Reconciliar Meta Ads com Shopify/GA4** para decidir se gargalo é tracking, landing ou qualidade de tráfego.
5. **Revalidar PageSpeed/CrUX** em tentativa separada; se CrUX continuar 404, marcar como ausência de field data do origin e usar Lighthouse + GA4 comportamento.

## O que não foi feito

- Nenhum write em Shopify, GMC, GA4/GSC config, Ads, Klaviyo, WhatsApp, e-mail, theme production, preço, estoque ou checkout.
- Nenhuma alteração de campaign/budget/adset/ad.
- Nenhum feed/ProductInput/datafeed/fetchNow.
- Nenhum dev theme upload.
- Nenhuma publicação de copy, FAQ, schema ou SEO fields.

## Status final

O relatório semanal foi entregue como **decision-grade parcial**: há dados suficientes para priorizar Top 5 e packets, mas GSC live, CrUX/PageSpeed field data, Metricool e Klaviyo/CRM ainda ficam como cobertura parcial/pendente nesta execução.
