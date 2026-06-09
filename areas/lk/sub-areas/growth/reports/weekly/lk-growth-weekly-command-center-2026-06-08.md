# LK Growth Weekly Command Center — 2026-06-08

Gerado em: `2026-06-08T11:45:56+00:00`  
Perfil: `lk-growth`  
Modo: `read-only / preview-only`  
Writes externos: `0`  
Status: `decision-grade parcial` — há GA4/GSC/GMC/Shopify/Meta/Klaviyo/Ahrefs/DataForSEO, mas PageSpeed/CrUX ficou parcial e parte da demanda/conversão ainda precisa reconciliação por URL antes de qualquer write.

## Resumo executivo

- **Nota Growth operacional:** **78/100**. Boa base autenticada para abrir a semana, com GSC, GA4 orgânico, GMC, Shopify refresh histórico/recente, Meta Ads, Klaviyo, DataForSEO e Ahrefs. Penalização principal: PageSpeed/CrUX parcial, Metricool Meta Ads 500, GA4 genérico 403, e parte dos dados comerciais por URL vem do refresh 2026-05-18 com atualização parcial, não de uma nova recomputação completa de pedidos por URL.
- **Nota pública SEO/CRO técnica:** **97,1/100**. Camada Claude SEO em 8 URLs P1 encontrou HTML/schema/conteúdo muito fortes; isso é diagnóstico secundário, não substitui priorização comercial.
- **Orgânico está relevante:** GA4 orgânico 28 dias (`2026-05-11` → `2026-06-07`) trouxe **15.472 sessões**, **14.396 usuários**, **28.776 pageviews**, média **552,6 sessões/dia**.
- **Top orgânico por landing page:** Onitsuka todos os modelos (**865 sessões**), Lululemon (**754**), home (**741**), Onitsuka Mexico 66 (**383**), New Balance 204L (**230**), Air Jordan Travis Scott (**224**), Crocs McQueen PDP (**208**), Nike Mind PDP/collection (**202/197**), guia de tamanhos (**196**).
- **Maior alavanca da semana:** fechar lacunas de CTR/GEO em coleções com demanda e receita: Onitsuka, Lululemon, New Balance 204L, Nike Mind, Samba Jane.
- **Maior risco operacional:** GMC segue com escala de reprovações/diagnósticos: **21.402 products/statuses**, **11.835 Shopping disapproved**, **1.431 produtos com `landing_page_error`**, **712 com `missing_item_attribute_for_product_type`**, e **10.441 `mhlsf_full_missing_valid_link_template`** em local inventory/LIA. Não é preço/PDP 404: é contrato de `link_template` local inventory.

## Fontes verificadas, indisponíveis e confiança

### Fontes verificadas

1. **Shopify / orders / membership — `fact_shopify`, parcial-atualizado**
   - Refresh decision-grade leu **647 pedidos desde 2026-04-17**, **558 pagos/considerados**, e validou **19/19 lookups** de produto/collection.
   - Base de priorização comercial usada: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.md`.

2. **GA4 — `fact_ga4`, verificado para orgânico**
   - Property `348553567`, janela `2026-05-11` → `2026-06-07`.
   - Total orgânico: **15.472 sessões**, **14.396 usuários**, **28.776 pageviews**.
   - Top pages extraídas via `ga4_report.py`.
   - Limitação: GA4 genérico retornou `403`; a property LK funcional está OK.

3. **GSC — `fact_gsc`, verificado**
   - `sc-domain:lksneakers.com.br`, janela `2026-05-11` → `2026-06-05`, **50 linhas**.
   - Queries/páginas principais: Lululemon, Onitsuka, Samba Jane, Nude Project, jaqueta Lululemon.

4. **GMC — `fact_gmc`, verificado por relatório recente**
   - Relatório autenticado 2026-06-04: **21.402 products/statuses**, `decision-grade` para triagem GMC.
   - Tentativa de rerun em 2026-06-08 excedeu 300s; usei o relatório vivo mais recente sem executar writes.

5. **DataForSEO — `platform_signal`/SERP demand**
   - Volume/intenção Brasil para termos prioritários:
     - `onitsuka tiger`: **33.100/mês**, transacional.
     - `nike mind 001`: **18.100/mês**, transacional + informacional.
     - `new balance 204l`: **9.900/mês**, transacional; pico recente muito forte.
     - `onitsuka tiger mexico 66`: **6.600/mês**, transacional.
     - `lululemon brasil`: **4.400/mês**, navegacional/comercial.
     - `adidas samba jane`: **2.400/mês**, transacional; tendência anual muito forte.
     - `air jordan travis scott`: **1.300/mês**, transacional.
     - `jaqueta lululemon`: **1.000/mês**, transacional.

6. **Meta Ads — `platform_signal`**
   - MCP Meta Ads last 7d funcionou; Metricool Meta Ads retornou HTTP 500.
   - Sinais visíveis: RMKT Geral gastou **R$ 686,44**, **2.701 cliques**, **2.053 landing page views**, **34 add to cart**, **8 initiate checkout**, **1 purchase**; ADV+ Geral gastou **R$ 1.176,95**, **1.274 cliques**, **41 add to cart**, **9 initiate checkout**, **6 purchases**. Números são plataforma Meta, não receita reconciliada Shopify.

7. **Klaviyo — `platform_signal`/CRM**
   - Read-only OK, últimos 7 dias.
   - E-mail teve abertura/clique, mas métricas `Active on Site`, `Placed Order`, `Added to Cart` vieram zeradas na API Klaviyo. Isso sugere lacuna de tracking/mapeamento Klaviyo ou janela/evento, não ausência de comportamento no site.
   - Clicked Email: contagens diárias **15, 60, 51, 60, 46, 47, 19, 4**.

8. **Ahrefs — `off-site signal`**
   - `lksneakers.com.br`: Domain Rating **35**, Ahrefs Rank **2.393.454**.

9. **PageSpeed/CrUX — parcial**
   - Readiness apontou `pagespeed_crux=true`, mas connector probe teve PageSpeed `TimeoutError` e CrUX `404`; Claude SEO Google config também apontou API key ausente no contexto nativo.
   - Conclusão: não usei CWV como critério decisivo desta semana.

### Fontes indisponíveis/parciais

- **Metricool Meta Ads:** HTTP 500; substituído por Meta Ads MCP read-only.
- **PageSpeed/CrUX:** parcial/instável; precisa normalizar `GOOGLE_API_KEY`/contexto Claude SEO antes de virar decision-grade CWV.
- **GA4 genérico:** 403; GA4 LK funcional OK.
- **GMC rerun 2026-06-08:** timeout 300s; usei relatório autenticado 2026-06-04.
- **Klaviyo conversão/eventos onsite:** eventos comerciais zerados na API; tratar como sinal de instrumentação/integração parcial.

## Alertas/anomalias

1. **GMC com risco material de Shopping/Local:** 11.835 itens Shopping disapproved e 1.431 `landing_page_error`. Há itens públicos OK na amostra, então não é simplesmente “produto inexistente”; precisa triagem por origem/link/reprocessamento, não delete em massa.
2. **`mhlsf_full_missing_valid_link_template` em 10.441 locais:** tratar como contrato `link_template`/`store_code` do local inventory/LIA. Bloquear `fetchNow`, ProductInput, feed e Shopify write até approval packet.
3. **Samba Jane tem demanda e fricção:** GSC `adidas samba jane` posição 5,5, CTR 1,64%; DataForSEO 2.400/mês transacional com pico 8.100 em abril; GA4 mostra 177 sessões orgânicas e bounce 42,9%/engagement 57,1%.
4. **Onitsuka tem muito volume, mas CTR baixo em head term:** `onitsuka tiger` com 24.448 impressões, CTR 0,29%, posição 8,3; DataForSEO 33.100/mês.
5. **Klaviyo: opens/clicks existem, eventos comerciais zerados:** risco de subatribuição ou tracking quebrado no CRM, principalmente se campanhas estão ajudando conversão mas Klaviyo não enxerga.
6. **PageSpeed/CrUX parcial:** não usar como bloqueio, mas normalizar porque CRO mobile depende de CWV real.

## Top 5 prioridades da semana

### 1) Onitsuka Tiger — recuperar CTR e capturar demanda head term

- **Alvos:** `/collections/onitsuka-tiger-todos-os-modelos`, `/collections/onitsuka-tiger-mexico-66`, PDP `mexico-66-kill-bill`.
- **Fato verificado:**
  - GA4 orgânico: Onitsuka todos os modelos **865 sessões**, Mexico 66 **383 sessões**.
  - GSC: `onitsuka tiger` **24.448 impressões**, CTR **0,29%**, posição **8,3**; `onitsuka tiger mexico 66` **6.785 impressões**, CTR **2,34%**, posição **2,5**; `tenis onitsuka tiger` **3.917 impressões**, CTR **1,51%**, posição **4,5**.
  - Shopify refresh: Onitsuka todos os modelos vendas combinadas **796 un. / R$ 1.914.732,08**; Mexico 66 **764 un. / R$ 1.825.032,40**; Kill Bill **115 un. / R$ 275.998,85**.
- **Interpretação:** maior oportunidade combinada de receita + demanda + CTR. SEO técnico está forte, então o ganho deve vir de snippet/copy de intenção, source pages e CRO de coleção/PDP.
- **Recomendação:** preparar pacote read-only de SERP/GEO para Onitsuka: title/meta alternativos, FAQ buyer-intent, source page “Onitsuka Tiger original no Brasil / Mexico 66 original”, e revisão de CTR por query.
- **Impacto esperado:** alto.
- **Esforço:** médio.
- **Risco:** médio se mexer em coleção já forte; baixo se começar por packet/preview.
- **Rollback:** manter snapshot de SEO fields/HTML antes de qualquer futura alteração; se tema/coleção, dev theme + rollback asset.
- **Aprovação necessária:** sim para qualquer Shopify SEO field, body, FAQ, schema ou theme.
- **Decision-grade:** sim para priorização; packet ainda pendente.

### 2) New Balance 204L — LKGOC/handoff por demanda explosiva

- **Alvo:** `/collections/new-balance-204l`.
- **Fato verificado:**
  - GA4 orgânico: **230 sessões**, engagement **71,3%**.
  - Shopify refresh: **396 un. / R$ 1.022.571,08** vendas combinadas.
  - DataForSEO: `new balance 204l` **9.900/mês**, transacional, crescimento anual muito forte; abril teve **40.500** buscas.
  - Claude SEO: **96/100**, já tecnicamente forte.
- **Interpretação:** demanda de mercado maior que tráfego atual capturado; é oportunidade de LKGOC/collection-source-page, não só ajuste de meta.
- **Recomendação:** handoff para **[LK] Otimização de Coleção**: revisar padrão 204L/guia, SERP live, FAQ único, citabilidade, source page e eventuais lacunas de produto/mídia.
- **Impacto esperado:** alto.
- **Esforço:** médio/alto.
- **Risco:** médio por envolver coleção/LKGOC e possível conteúdo visível.
- **Rollback:** dev preview/backup de SEO fields + collection body/theme asset antes de qualquer produção.
- **Aprovação necessária:** sim; LK Growth não executa alteração visual/textual LKGOC.
- **Decision-grade:** sim para handoff; execução depende do especialista e aprovação.

### 3) Nike Mind 001 — demanda alta, bounce alto no PDP principal

- **Alvos:** `/collections/nike-mind-001`, `/products/slide-nike-mind-001-black-chrome-preto`.
- **Fato verificado:**
  - GA4: collection **197 sessões**, PDP Black Chrome **202 sessões**, bounce PDP **43,6%**, engagement **56,4%**.
  - Shopify refresh: Nike Mind collection **142 un. / R$ 446.558,60**; PDP Black Chrome **31 un. / R$ 102.899,69**.
  - DataForSEO: `nike mind 001` **18.100/mês**, transacional + informacional.
  - Claude SEO: collection **97/100**.
- **Interpretação:** tráfego qualificado existe, mas PDP tem fricção relativa. A intenção é muito explicativa/informacional; precisa ponte entre “o que é Nike Mind” e compra segura.
- **Recomendação:** pacote CRO/GEO read-only: checar PDP mobile, provar se CTA/parcelamento/tamanho/FAQ estão claros, e ampliar source page/guia com CTA para coleção/PDP.
- **Impacto esperado:** alto.
- **Esforço:** médio.
- **Risco:** baixo em diagnóstico; médio se virar theme/PDP write.
- **Rollback:** dev theme para qualquer visual; snapshot product SEO/body antes de qualquer write.
- **Aprovação necessária:** sim para tema/PDP/source page.
- **Decision-grade:** sim para diagnóstico/prioridade; CRO exato ainda precisa QA visual.

### 4) Lululemon / Jaqueta Define — forte tráfego, CTR e demanda comercial

- **Alvos:** `/collections/lululemon`, `/products/jaqueta-lululemon-define-nulu`.
- **Fato verificado:**
  - GA4 orgânico: Lululemon **754 sessões**, bounce **21%**, engagement **79%**; Jaqueta Define **135 sessões**.
  - GSC: `lululemon` **17.600 impressões**, CTR **0,7%**, posição **5,3**; `lululemon brasil` **2.921 impressões**, CTR **13,11%**, posição **2,2**; `jaqueta lululemon` **40 cliques / 851 impressões**, CTR **4,7%**.
  - DataForSEO: `lululemon brasil` **4.400/mês**; `jaqueta lululemon` **1.000/mês**, transacional.
  - Shopify refresh: Lululemon collection **51 un. / R$ 64.399,49**.
- **Interpretação:** LK já tem autoridade para “Lululemon Brasil”; oportunidade é capturar termo genérico e PDP de jaqueta com copy/FAQ de escolha, autenticidade e modelagem.
- **Recomendação:** packet SEO/GEO de Lululemon: title/meta por intenção, source page “Lululemon original no Brasil”, FAQ comprador, e revisão Klaviyo/CRM para visitantes de alto interesse.
- **Impacto esperado:** médio/alto.
- **Esforço:** médio.
- **Risco:** médio por marca sensível; evitar linguagem de estoque/prazo pública.
- **Rollback:** snapshot SEO/body; dev theme para visual.
- **Aprovação necessária:** sim para Shopify/source page/Klaviyo sends.
- **Decision-grade:** sim para demanda; conversão por URL ainda parcial.

### 5) GMC Product Data Quality — atacar high-confidence sem tocar preço/promo

- **Alvos:** `missing_item_attribute_for_product_type`, `landing_page_error`, `mhlsf_full_missing_valid_link_template`.
- **Fato verificado:**
  - 712 produtos com atributo ausente; preview de cor com **393 high-confidence**.
  - 1.431 produtos com `landing_page_error`.
  - 10.441 local/LIA com `mhlsf_full_missing_valid_link_template`.
  - Price governance: 234 `price_updated`, 223 `strikethrough_price_updated` — não corrigir em bulk.
- **Interpretação:** existe ganho de servibilidade e ranking Shopping por atributo/link, mas preço/promocional segue bloqueado até source/overwrite/promo logic.
- **Recomendação:** separar dois packets:
  1. **Packet GMC B:** missing color high-confidence, sem medium/ambíguos.
  2. **Packet Local Inventory:** investigação `link_template`/store_code para `local:*`/`LIA_*`.
- **Impacto esperado:** médio/alto em Merchant; indireto em revenue.
- **Esforço:** médio.
- **Risco:** alto se mexer em feed/source errado; baixo se ficar em preview/readback.
- **Rollback:** snapshot Product/ProductInput/feed row por offerId antes de qualquer patch; readback e D+7.
- **Aprovação necessária:** sim para ProductInput/feed/datafeed/fetchNow/GMC write.
- **Decision-grade:** sim para triagem; não para execução sem approval packet final.

## Handoffs necessários

1. **[LK] Otimização de Coleção — New Balance 204L / Nike Mind / Onitsuka**
   - Motivo: oportunidade envolve LKGOC/source page/FAQ/citabilidade/copy visível.
   - LK Growth entrega evidência e prioridade; especialista prepara preview/pacote canônico.
   - Sem write de coleção, tema, SEO field ou source page nesta rotina.

2. **LK Shopify — se houver aprovação futura de tema/PDP/collection surface**
   - Motivo: qualquer dev theme/preview/readback/rollback Shopify surface deve ser executado pelo fluxo Shopify.
   - Escopo possível: QA mobile PDP Nike Mind/Samba Jane, collection snippets, FAQ/schema visível, preview dev.

3. **GMC/Product Data execution runner — só após aprovação**
   - Motivo: ProductInput/feed/local inventory writes têm risco de overwrite.
   - Escopo ainda sugerido: high-confidence color e local link_template investigation.

4. **CRM/Klaviyo — diagnóstico de tracking, não campanha**
   - Motivo: Klaviyo mostra opens/clicks, mas eventos comerciais zerados.
   - Próximo passo seguro: revisar integração/event mapping read-only; nenhum envio/campanha.

## Approval packets sugeridos — preview inline

### Packet 1 — Onitsuka CTR/GEO packet

- **Ação proposta:** preparar preview de title/meta/FAQ/source-page para Onitsuka Tiger + Mexico 66, sem publicar.
- **Alvos:** `/collections/onitsuka-tiger-todos-os-modelos`, `/collections/onitsuka-tiger-mexico-66`, PDP Kill Bill.
- **Autorizaria agora se aprovado:** apenas criação de pacote/preview local e handoff; não autoriza Shopify write.
- **Approval wording futuro para write:** “Aprovo aplicar exatamente o Packet Onitsuka [versão/data] nos campos/URLs listados, com backup e rollback.”

### Packet 2 — LKGOC New Balance 204L / Nike Mind handoff

- **Ação proposta:** abrir handoff para **[LK] Otimização de Coleção** com evidência GA4/GSC/DataForSEO/Shopify e pedido de preview canônico.
- **Autorizaria:** preparação de preview e pacote; não produção.
- **Risco:** copy pública e layout precisam aprovação visual/textual.

### Packet 3 — GMC high-confidence color

- **Ação proposta:** revisar `393` linhas high-confidence do preview `missing color`; preparar micro-piloto com 25–50 exact offerIds.
- **Não inclui:** medium/ambíguos, preço, salePrice, disponibilidade, fetchNow, Shopify/Tiny.
- **Rollback:** snapshot ProductInput/Product resource por offerId.
- **Aprovação necessária para executar:** explícita por quantidade e arquivo/offerIds.

### Packet 4 — GMC Local Inventory link_template

- **Ação proposta:** investigação/preview para `mhlsf_full_missing_valid_link_template`: data source local, store code, template esperado, amostras `local:*`/`LIA_*`.
- **Não inclui:** `fetchNow`, datafeed write, ProductInput write, Shopify write.
- **Aprovação necessária:** somente se for alterar feed/data source/local inventory.

### Packet 5 — Klaviyo tracking diagnostic

- **Ação proposta:** diagnóstico read-only de eventos Klaviyo: por que `Active on Site`, `Placed Order`, `Added to Cart` estão zerados enquanto `Opened/Clicked Email` existem.
- **Não inclui:** envio, campanha, flow, lista, perfil, template, cupom ou automação.
- **Aprovação necessária:** apenas para correção/configuração/envio futuro.

## 18 tópicos — cobertura

| Tópico | Status | Evidência / limitação |
|---|---|---|
| 1. GA4 | Verificado parcial | Orgânico 28 dias OK; property LK funcional; GA4 genérico 403; funil completo por URL não recomputado nesta rodada. |
| 2. GSC | Verificado | `sc-domain:lksneakers.com.br`, 50 linhas, queries/páginas principais. |
| 3. GMC | Verificado | Relatório autenticado 2026-06-04; rerun 2026-06-08 timeout, sem writes. |
| 4. Shopify SEO | Verificado parcial | Refresh Shopify e scorecard existentes; nenhum novo readback SEO field por alvo nesta rodada. |
| 5. Shopify CRO/theme | Parcial | Priorização por GA4/GSC; sem browser/QA visual nesta rotina. Execução é LK Shopify/dev theme. |
| 6. GEO/AI Search | Parcial | DataForSEO volume/intenção + scorecard citability; AI/LLM mention live não foi rodado nesta janela. |
| 7. PageSpeed/CrUX/CWV | Parcial/pendente | Timeout/CrUX 404/API-key-context inconsistente. Não decision-grade. |
| 8. Schema | Verificado parcial | Scorecard detectou FAQPage/Breadcrumb/Collection/Product-related schema nas P1; sem validação completa Rich Results. |
| 9. Reviews/prova social | Pendente | Não consultei Judge.me nesta rotina. |
| 10. Paid media | Parcial | Meta Ads MCP OK; Metricool 500; dados como `platform_signal`. |
| 11. Influencer/social demand | Parcial | Não houve FHITS/influencer específico; paid/social demand inferido só por Meta. |
| 12. Concorrência/SERP | Parcial | DataForSEO keyword overview/intent; sem SERP competitor page deep-dive por query. |
| 13. Google Business/local | Parcial | GMC local inventory/LIA observado; GBP/local SEO não auditado. |
| 14. Klaviyo/CRM signals | Verificado parcial | Klaviyo API read-only OK; eventos comerciais zerados, tracking precisa diagnóstico. |
| 15. Catálogo/product data quality | Verificado | GMC product data: missing attributes, landing, price governance, GTIN/policy/image. |
| 16. Conteúdo/taxonomia comercial | Verificado parcial | Prioridades por coleção/modelo; handoff LKGOC necessário para copy/guia. |
| 17. Mensuração/QA de eventos | Parcial | GA4/Klaviyo/Meta inconsistências; precisa QA específico. |
| 18. Impact review/experimentation | Parcial | Próximos writes devem ter D+7; nenhum experimento novo aplicado. |

## Próximos passos seguros

1. **Preparar Packet Onitsuka CTR/GEO read-only** com exact title/meta/FAQ/source-page preview, sem aplicar.
2. **Abrir handoff LKGOC** para New Balance 204L e Nike Mind com evidência deste relatório.
3. **Gerar micro-pilot preview GMC high-confidence color** com amostra de 25–50 offerIds e rollback planejado, sem ProductInput write.
4. **Montar packet local inventory `link_template`** para `mhlsf_full_missing_valid_link_template`, sem feed/fetchNow.
5. **Diagnóstico Klaviyo tracking read-only** para explicar eventos comerciais zerados vs email clicks/opens.
6. **Normalizar PageSpeed/CrUX tooling** para que a próxima semana tenha CWV decision-grade.

## O que não fiz

- Nenhum write em Shopify, GMC, GA4/GSC config, Ads, Klaviyo, WhatsApp, e-mail, theme production, preço, estoque ou checkout.
- Nenhum `fetchNow`, ProductInput PATCH, supplemental feed upload, campanha, flow, lista, template ou envio.
- Nenhuma alteração visual/textual de coleção/LKGOC.
- Nenhum contato externo.

## Artefatos usados

- `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.md`
- `reports/lk-seo-cro-claude-seo-scorecard-2026-05-18.md`
- `reports/lk-gmc-weekly-review-2026-06-04.md`
- GA4/GSC/Meta/Klaviyo/Ahrefs/DataForSEO lidos em runtime nesta rotina.
