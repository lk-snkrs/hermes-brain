# LK SEO/GSC + GEO Opportunities Review — 2026-06-09

Status: **read-only / preview**  
Writes externos: **0**  
Período GSC analisado: **2026-05-12 → 2026-06-06**; comparação: **2026-04-16 → 2026-05-11**  
Entrega: cron semanal LK Growth; relatório salvo no Brain.

## 1) Fontes verificadas

- **Tooling readiness LK Growth:** OK; GSC/GA4/URL Inspection/PageSpeed-CrUX/Klaviyo/Ahrefs disponíveis em modo read-only.
- **Google Auth Claude-SEO:** Tier 2 para GSC, URL Inspection e GA4; PageSpeed/CrUX nativo da skill sem API key no config, mas wrapper Doppler LK Growth operacional.
- **GSC Search Analytics:** 1.000 linhas query+page; total amostrado atual: **4.173 cliques / 509.358 impressões / CTR 0,82%**.
- **GSC período anterior:** 1.000 linhas; **4.077 cliques / 369.839 impressões / CTR 1,10%**.
- **GA4 orgânico top pages:** disponível; período **2026-05-12 → 2026-06-08**.
- **GSC URL Inspection:** 3 URLs verificadas; todas **Submitted and indexed**, canonical self-match e crawled as mobile.
- **Shopify Admin read-only:** SEO title/meta de produtos/coleções candidatos lidos via GraphQL query-only.
- **HTML público/schema:** títulos, metas, H1 e schema dos candidatos lidos publicamente.
- **CrUX/PageSpeed wrapper:** field data mobile consultado para Onitsuka collection e Nike Mind PDP; sinais bons/sem bloqueio material.
- **llms.txt / llms-full.txt / agents.md:** públicos, HTTP 200.
- **Klaviyo analytics read-only:** 7 dias; Received Email 28.352, Opened 19.851, Clicked 347, Started Checkout 191; commerce events zerados em Klaviyo, tratar como diagnóstico de tracking/atribuição, não como prova de receita zero.
- **Ahrefs:** domain rating **35,0**, ahrefs rank **2.403.622** para `lksneakers.com.br`.

## 2) Fontes parciais/indisponíveis

- **DataForSEO/SERP/PAA/AI mentions:** MCP/DataForSEO não está exposto neste runtime de cron; `web_search`/`web_extract` externo retornou Unauthorized. Resultado: SERP/PAA/LLM mentions ficam **parciais/direcionais** nesta entrega.
- **Shopify receita/pedidos por URL:** não foi recalculado neste cron; GA4 orgânico foi usado como sinal de tráfego/engajamento. Prioridades abaixo são **GSC+GA4 demand-grade**, mas não são ranking final de receita.
- **GMC:** fora do foco desta rotina SEO/GSC+GEO; não houve write nem fetch/reprocess.

## 3) Leitura executiva

**Fato:** impressões orgânicas cresceram forte no recorte amostrado (**+139.519 impressões**, +37,7%), mas CTR médio caiu de **1,10% → 0,82%**. Isso indica ganho de superfície/descoberta, porém com snippets/landing mismatch ou dispersão de URLs em queries grandes.

**Interpretação:** há três frentes claras:
1. Capturar CTR em queries grandes com posição 4–15.
2. Transformar coleções com demanda em LKGOC/source assets, sem executar no LK Growth.
3. Reforçar GEO/AI citation em páginas que já indexam e já têm schema/llms, mas ainda precisam de respostas mais extraíveis e cobertura de prompts “original / onde comprar / adulto / Brasil”.

**Nota de confiança:** média-alta para demanda GSC/GA4 e indexação; média para concorrência/SERP/AI visibility por falta de DataForSEO/web search neste runtime.

---

# Até 3 oportunidades SEO

## SEO 1 — Nike Mind 001: demanda enorme, CTR quase zero e dispersão de URLs/PDPs

**Cadeia obrigatória**
- **Query/tema:** `nike mind 001`, `chinelo nike mind 001`, `mind 001`, `slide nike mind 001`.
- **URL atual/candidata:**
  - PDP principal: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`
  - PDP Pearl Pink: `https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa`
  - Collection candidata/hub: `https://lksneakers.com.br/collections/nike-mind-001`
- **Evidência GSC:**
  - Black Chrome PDP: **53.614 impressões / 29 cliques / CTR 0,05% / pos. média 8,1** em queries posição 4–15.
  - Pearl Pink PDP: **28.749 impressões / 12 cliques / CTR 0,04% / pos. 8,9**.
  - Collection Nike Mind 001: **5.165 impressões / 66 cliques / CTR 1,28% / pos. 8,4**.
  - Query `nike mind 001` também aparece em URLs com parâmetros Shopping/variant (`?currency=BRL...stkn=...`), sinal de dispersão/canonical tracking a monitorar.
- **Evidência GA4:** PDP Black Chrome tem **208 sessões orgânicas**, bounce **43,3%**, engagement **56,7%**.
- **URL Inspection:** Black Chrome **Submitted and indexed**, canonical Google = user canonical, crawled mobile em **2026-06-09T00:36:30Z**.
- **HTML/Shopify:** title atual **“Nike Mind 001 Black Chrome Original | LK Sneakers”** (49 chars), meta 144 chars, H1 único; Product/FAQ/Breadcrumb/Review snippets detectados.
- **Schema issue:** URL Inspection mostra Product snippets com warnings de `review`/`aggregateRating` ausentes e Merchant listings com múltiplos warnings `Invalid object type for field shippingRate`.
- **CrUX:** PDP com LCP **1.362ms good**, CLS **0,0 good**, TTFB **613ms good**.
- **Hipótese:** o problema não é indexação nem velocidade; é captura de snippet/landing e consolidação de intenção. A collection/hub pode capturar o termo genérico, enquanto PDPs capturam colorways, mas hoje há competição interna e CTR muito baixo.
- **Ação preview:** preparar packet SEO técnico + GEO para Nike Mind: revisar title/meta por papel de URL, fortalecer collection como hub “Nike Mind 001 e 002 original”, revisar links internos entre PDPs e collection, investigar schema `shippingRate` em dev/Shopify surface, sem mexer em preço/estoque/copy pública sem aprovação.
- **Métrica esperada:** CTR de queries `nike mind 001` e `chinelo nike mind 001`; sessões orgânicas nos PDPs e collection; warnings rich results pós-readback.

**Approval packet necessário se for executar:** Shopify SEO field/theme/schema/internal link write exige aprovação explícita. Rollback: snapshot de `seo.title`, `seo.description`, schema/theme asset e readback pós-mutação.

## SEO 2 — Onitsuka Tiger broad collection: maior oportunidade de CTR em coleção com tráfego orgânico real

**Cadeia obrigatória**
- **Query/tema:** `onitsuka tiger`, `tenis onitsuka tiger`, `onitsuka`, `tenis tiger`, `tenis tiger onitsuka`.
- **URL atual/candidata:** `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`
- **Evidência GSC:** agregado posição 4–15: **36.261 impressões / 194 cliques / CTR 0,54% / pos. 7,5**. Query principal `onitsuka tiger`: **24.395 impressões / 73 cliques / CTR 0,30% / pos. 8,3**.
- **Evidência GA4:** maior landing orgânica do período: **879 sessões / 787 usuários / 1.787 pageviews / engagement 77,5%**.
- **URL Inspection:** **Submitted and indexed**, canonical match, crawled mobile em **2026-06-08T11:32:33Z**.
- **HTML/Shopify:** title **“Onitsuka Tiger Original | Mexico 66 e Curadoria LK”**, meta 131 chars, H1 único, FAQPage/Breadcrumb/CollectionPage/ItemList presentes.
- **CrUX:** Onitsuka collection com CLS **0,08 good**, TTFB **436ms good**, FCP **1.013ms good**; LCP/INP não vieram no payload consultado, então sem diagnóstico material de CWV.
- **Hipótese:** a coleção já é tecnicamente limpa, mas broad query em pos. 8 com CTR 0,30% sugere falta de snippet/copy orientado a “original no Brasil”, diferença de modelos e intenção transacional.
- **Ação preview:** gerar handoff LKGOC para [LK] Otimização de Coleção: bloco citável, FAQ único por objeções reais, reforço de source/guide e revisão de snippet; LK Growth não executa coleção.
- **Métrica esperada:** CTR da query `onitsuka tiger` e variações; posição média 4–10; sessões orgânicas na collection; cliques em links para PDPs.

**Handoff gerado:** `areas/lk/sub-areas/growth/handoffs/lkgoc-seo-gsc-geo-onitsuka-nb204l-20260609.md`.

## SEO 3 — New Balance 204L: queda material após pico e necessidade de refresh/handoff LKGOC

**Cadeia obrigatória**
- **Query/tema:** `new balance 204l`, `nb 204l`, `new balance 204 l`, `newbalance 204l`.
- **URL atual/candidata:** `https://lksneakers.com.br/collections/new-balance-204l`
- **Evidência GSC atual:** **11.078 impressões / 59 cliques / CTR 0,53% / pos. 9,3** em queries posição 4–15.
- **Queda vs período anterior:** query principal `new balance 204l` caiu de **91 cliques / 18.427 impressões / CTR 0,49% / pos. 8,0** para **18 cliques / 7.318 impressões / CTR 0,25% / pos. 10,3** (**-73 cliques, -11.109 impressões, piora +2,3 posições**).
- **Evidência GA4:** collection com **231 sessões orgânicas**, engagement **71,0%**.
- **URL Inspection:** **Submitted and indexed**, canonical match, crawled mobile em **2026-06-08T12:33:16Z**.
- **HTML/Shopify:** title **“New Balance 204L Original | Curadoria LK Sneakers”**, meta 143 chars, H1 único, FAQPage/CollectionPage/ItemList presentes.
- **Hipótese:** queda pode ser sazonal/SERP-lançamento, mas a combinação posição 10 + CTR 0,25% indica necessidade de refresh de conteúdo/FAQ/source page com ângulos de colorway, versão, forma, styling e originalidade.
- **Ação preview:** manter como oportunidade LKGOC; não executar no LK Growth. Revalidar pesquisa SERP/DataForSEO quando disponível antes de mudar copy. Aproveitar o handoff LKGOC já existente de 2026-06-08 e anexar estes dados de queda.
- **Métrica esperada:** recuperação de impressões/cliques na query principal, CTR >0,5% e retorno para posição média <8.

**Approval packet necessário se for executar:** aprovação de coleção/LKGOC + Shopify/dev preview; produção só com aprovação separada.

---

# Até 3 oportunidades GEO / AI Search

## GEO 1 — llms/agents: cobertura existe, mas broad Onitsuka está desalinhado entre `llms.txt` e `agents.md`

**Cadeia obrigatória**
- **Query/tema:** `onitsuka tiger`, `onde comprar onitsuka tiger no brasil`, `onitsuka tiger original`.
- **URL atual/candidata:** broad collection `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`; model collection `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`.
- **Evidência:** `agents.md` contém `onitsuka-tiger-todos-os-modelos`; `llms.txt` e `llms-full.txt` contêm `onitsuka-tiger-mexico-66`, mas **não** contêm `onitsuka-tiger-todos-os-modelos`.
- **GSC:** broad collection é a maior landing orgânica e tem CTR 0,54% em 36.261 impressões.
- **Hipótese:** AI crawlers recebem orientação para Mexico 66, mas podem não receber a URL broad que captura a demanda genérica `onitsuka tiger`.
- **Ação preview:** atualizar proposta de `llms.txt`/`llms-full.txt` para incluir a broad collection com descrição curta e citação de Mexico 66/outros modelos; manter `agents.md` como está ou adicionar prompt mais direto de compra segura/original no Brasil.
- **Métrica esperada:** presença em AI answer/text citation para prompts de compra/original; GSC CTR broad query; tráfego orgânico na collection.

**Write requerido:** atualização de `llms.txt`/`llms-full.txt`/theme/page pública exige aprovação. Sem write neste cron.

## GEO 2 — Nike Mind 001: página já tem schema e agents/llms, mas precisa de bloco citável “o que é / para quem é / original no Brasil”

**Cadeia obrigatória**
- **Query/tema:** `nike mind 001`, `chinelo nike mind 001`, `slide nike mind 001`, `nike mind 001 original`.
- **URL atual/candidata:** collection `https://lksneakers.com.br/collections/nike-mind-001` + PDPs de colorway.
- **Evidência GSC:** soma dos principais PDPs/collection supera **87k impressões** no recorte, com CTR extremamente baixa nos PDPs.
- **Evidência pública:** `llms.txt`, `llms-full.txt` e `agents.md` contêm `nike-mind-001`; PDP tem Product/FAQ schema e URL Inspection PASS.
- **Hipótese:** existe descoberta, mas falta uma resposta self-contained de 134–167 palavras com “Nike Mind 001 é...”, materiais/silhueta/conforto, diferença 001/002 e orientação humana de compra. Isso favorece ChatGPT/Perplexity/Gemini/AI Overviews sem depender de mais uma meta genérica.
- **Ação preview:** preparar bloco citável + FAQ único para collection/hub e revisar schema FAQPage parity; investigar warnings `shippingRate` como tema técnico separado.
- **Métrica esperada:** CTR e sessões orgânicas em collection/PDPs; AI text citation/merchant-card separadas quando DataForSEO/AI mentions estiver operacional.

**Write requerido:** copy/schema/collection update é Shopify/theme/page write; precisa approval packet e rollback.

## GEO 3 — Crocs Relâmpago McQueen: demanda explodiu; guia existe, mas `agents.md` não prioriza o tema

**Cadeia obrigatória**
- **Query/tema:** `crocs mcqueen`, `crocs relampago mcqueen`, `crocs relampago mcqueen adulto`, `crocs relâmpago mcqueen original`.
- **URL atual/candidata:** PDP `https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`; guia `https://lksneakers.com.br/pages/crocs-relampago-mcqueen-guia`.
- **Evidência GSC:** PDP principal posição 4–15 soma **43.564 impressões / 92 cliques / CTR 0,21% / pos. 7,5**. Guia soma **9.675 impressões / 31 cliques / CTR 0,32% / pos. 10,3** para queries adult/original.
- **Evidência pública:** `llms.txt` e `llms-full.txt` contêm `crocs-relampago-mcqueen`; `agents.md` **não** contém o termo.
- **Hipótese:** a guide/source architecture já existe, mas o arquivo de instrução para agentes não coloca Crocs McQueen como prioridade comercial/AI Search; isso reduz clareza para prompts conversacionais de “adulto/original/onde comprar”.
- **Ação preview:** adicionar Crocs McQueen ao `agents.md` como priority commercial page e revisar o guia com bloco de resposta direta para adulto/original; sem prometer disponibilidade pública, usar linguagem de curadoria/autenticidade/atendimento humano.
- **Métrica esperada:** CTR de queries `crocs relampago mcqueen adulto/original`; sessões no guia e PDP; AI citation state (`text_citation` vs `merchant_card`).

**Write requerido:** atualização de agents/page/FAQ/schema exige aprovação explícita.

---

## 4) Approval packets preview-only

### Packet A — Nike Mind SEO/GEO/schema pilot
- **Impacto esperado:** alto; maior volume de impressões do lote.
- **Esforço:** médio; revisão de snippet/copy + schema warnings + links internos.
- **Risco:** médio; mexe em storefront/schema se aprovado.
- **Rollback:** snapshot de SEO fields, page/collection content, theme/schema asset; readback Admin + HTML + URL Inspection posterior.
- **Aprovação necessária:** “Aprovo preparar o piloto Nike Mind SEO/GEO/schema no dev/preview, sem produção.”

### Packet B — Onitsuka LKGOC handoff
- **Impacto esperado:** alto; maior landing orgânica e CTR baixo.
- **Esforço:** médio/alto; LKGOC/source/FAQ precisa de owner de coleção.
- **Risco:** médio; mudança visível em coleção.
- **Rollback:** snapshot da collection, template/section dev, SEO fields, FAQ/schema.
- **Aprovação necessária:** aprovar handoff para [LK] Otimização de Coleção revisar e preparar preview.

### Packet C — llms/agents GEO alignment
- **Impacto esperado:** médio; melhora instrução para AI crawlers e descoberta de source pages.
- **Esforço:** baixo/médio.
- **Risco:** baixo se feito com diff pequeno; ainda é public write.
- **Rollback:** snapshot dos arquivos atuais `llms.txt`, `llms-full.txt`, `agents.md`.
- **Aprovação necessária:** “Aprovo atualizar llms/agents conforme packet GEO, com rollback.”

## 5) Checklist 18 tópicos — status nesta rotina

1. GA4: **verificado parcial** — orgânico/top pages; sem receita/pedidos por URL neste cron.
2. GSC: **verificado** — queries, páginas, CTR, posição, quedas e URL Inspection.
3. GMC: **não aplicável ao foco / não alterado**.
4. Shopify SEO: **verificado read-only** — SEO title/meta dos candidatos.
5. Shopify CRO: **parcial** — sinais de bounce/engagement; sem tema/dev preview.
6. GEO/AI Search: **verificado parcial** — llms/agents/schema; sem DataForSEO/AI mentions runtime.
7. PageSpeed/CrUX/CWV: **parcial** — CrUX em 2 URLs; sem auditoria PSI completa.
8. Schema: **verificado parcial** — detectado por HTML/URL Inspection; warnings Nike Mind.
9. Reviews/prova social: **parcial** — rich result Review snippets detectado; sem Judge.me deep dive.
10. Paid media signals: **parcial** — GSC mostrou URLs com parâmetros Shopping; sem Meta/Google Ads leitura neste cron.
11. Influencer/social demand: **não verificado** nesta rotina.
12. Concorrência/SERP: **pendente/parcial** — DataForSEO/web_search indisponível no runtime.
13. Google Business/local: **não aplicável ao foco**; agents/llms citam loja física/Jardins.
14. Klaviyo/CRM: **verificado parcial** — engajamento email e started checkout; commerce events zerados em Klaviyo.
15. Catálogo/product data quality: **parcial** — schema Product/Merchant warnings; sem GMC feed review.
16. Conteúdo/taxonomia comercial: **verificado** — oportunidades de collection/source/FAQ sem usar estoque/pronta-entrega como taxonomia.
17. Mensuração/QA eventos: **parcial** — Klaviyo commerce zero é possível tracking gap; GA4 orgânico OK.
18. Impact review/experimentation: **pendente** — próximos packets devem criar D+7 review.

## 6) O que não foi feito

- Nenhum write em Shopify, GSC, tema, schema, llms/agents, GMC, Klaviyo, Ads ou páginas.
- Nenhuma alteração de title/meta/copy visível.
- Nenhuma execução LKGOC; apenas handoff local.
- Nenhuma promessa de estoque/disponibilidade/prazo.
- Nenhuma recomendação baseada apenas em HTML público; oportunidades usam GSC + GA4/Index/Shopify quando disponíveis.
