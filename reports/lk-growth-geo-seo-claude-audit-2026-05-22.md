# LK Growth — Auditoria Completa GEO/SEO/Claude SEO — 2026-05-22

**Execução:** 2026-05-22 16:23 UTC
**Modo:** read-only; nenhum write em Shopify, tema, GMC, campanhas, Klaviyo/WhatsApp ou produção.
**Escopo:** LK Sneakers — Search, GEO/AI Search, Shopify SEO/CRO, schema, PageSpeed, GMC e 18 tópicos canônicos de Growth.
**Skills/metodologia usadas:** `seo-audit`, `seo-page`, `seo-schema`, `seo-ecommerce`, `seo-content`, `seo-technical`, `seo-dataforseo`, `lk-seo-weekly-improvement` + checklist canônico `ESCOPO-18-TOPICOS.md`.

---

## 1. Veredito executivo

A LK está **forte em SEO técnico básico e em páginas P1 comerciais**, mas está **subaproveitando AI Search/GEO** por três gargalos claros:

1. **`/llms.txt` e `/llms-full.txt` estão errados para GEO:** ambos redirecionam/servem `agents.md`, com instruções genéricas de agente/Shop/UCP, e **não contêm os marcadores comerciais P1**.
2. **Collections P1 têm bom title/meta/canonical/schema de coleção, mas faltam blocos citáveis e FAQPage:** as páginas têm H1 correto, ItemList/Breadcrumb, imagens com alt e Lighthouse SEO 92/100; porém só exibem praticamente um H2 genérico de marca (`Less noise, more identity.`), sem FAQ estruturado nem bloco editorial de 134–167 palavras.
3. **A LK já aparece em alguns lugares valiosos, mas ainda não vira “resposta padrão” em ChatGPT:** em ChatGPT para NB 204L, a LK aparece como merchant em um bloco de produto raro, mas **não é citada na lista textual de lojas confiáveis**. Para Nike Mind 001, o ChatGPT deu resposta genérica e **não citou LK**. No Google SERP, LK aparece bem para Kill Bill e Nike Mind, mas não domina a narrativa.

**Status decision-grade:** Parcialmente decision-grade para priorização e criação de approval packets, porque temos dados comerciais/GA4/GSC/Shopify recentes do refresh de 2026-05-18/22 + auditoria pública atual + DataForSEO. Não é decision-grade para mexer em produção sem novo approval explícito.

---

## 2. Principais evidências

### Dados comerciais e demanda já validados no refresh decision-grade

Top P1 com dados Shopify/GA4/GSC recentes:

- **Onitsuka Tiger todos os modelos:** 1.132 sessões; CVR 0,09%; 55.903 impressões; CTR 1,14%; vendas combinadas R$ 1,78M.
- **New Balance 204L:** 454 sessões; CVR 0,22%; 43.484 impressões; CTR 0,77%; vendas combinadas R$ 955k.
- **Air Jordan Travis Scott:** 207 sessões; 27.818 impressões; CTR 0,66%; vendas combinadas R$ 162k.
- **Lululemon:** 859 sessões; 25.178 impressões; CTR 3,03%; vendas combinadas R$ 56k.
- **Adidas Samba Jane:** 210 sessões; 17.701 impressões; CTR 1,21%; vendas combinadas R$ 320k.
- **Onitsuka Kill Bill PDP:** 146 sessões; CVR 0,68%; 11.070 impressões; CTR 0,42%; vendas combinadas R$ 256k.
- **Onitsuka Mexico 66 collection:** 748 sessões; 31.659 impressões; CTR 1,96%; vendas combinadas R$ 1,73M.
- **Nike Mind 001:** 133 sessões; 6.532 impressões; CTR 1,21%; vendas combinadas R$ 402k.

### Search demand — DataForSEO/Google Ads BR

Keywords auditadas:

- `new balance 204l`
- `nike mind 001`
- `onitsuka tiger mexico 66`
- `adidas samba jane`
- `air jordan travis scott`
- `onitsuka tiger kill bill`
- `lululemon original`

Relatório anterior validou volumes P1 aproximados: Nike Mind 001 18,1k; New Balance 204L 9,9k; Mexico 66 6,6k. A recomendação é tratar esses termos como **P1 de GEO/Search**, porque misturam demanda, ticket e intenção comercial.

### AI Search / ChatGPT

**Consulta:** “Onde comprar New Balance 204L original no Brasil?”

- ChatGPT recomendou New Balance oficial, Artwalk, Guadalupe, NK Store, Danki, Menina Shoes, Farfetch e Palmtree48.
- A LK **não apareceu no texto principal** como loja confiável.
- A LK apareceu como merchant em produto específico: **“New Balance 204L Arid Timberwolf Bege” — LK Sneakers Apparels — R$ 2.799,99**, em bloco de produtos raros.
- Interpretação: a LK tem algum sinal via Shopping/Merchant, mas falta sinal textual/citável para virar referência editorial.

**Consulta:** “Onde comprar Nike Mind 001 original no Brasil?”

- ChatGPT deu resposta genérica: Nike oficial, Nike Stores, Netshoes, Centauro, Kanui, Authentic Feet e marketplaces.
- LK não citada.
- Interpretação: oportunidade alta porque no Google SERP a LK já aparece; falta reforçar entidade/conteúdo citável.

### Google SERP — DataForSEO mobile BR

**Nike Mind 001 comprar Brasil**

- AI Overview presente no topo.
- LK aparece como orgânico rank group 10 / absolute 12 com PDP `Slide Nike Mind 001 Black Chrome Preto`.
- Concorrentes/players: Nike, Instagram/Tênis Certo, Droper, Mercado Livre, Accio, SneakersBR, JR Tênis.
- Popular Products não mostrou LK entre os principais cards nessa consulta; Droper e outros dominam.

**Onitsuka Tiger Mexico 66 Kill Bill original Brasil**

- Popular Products aparece antes dos orgânicos.
- LK aparece em Popular Products com pelo menos 3 entradas: Kill Bill Amarelo, Kill Bill SD e Kids.
- Orgânico: LK aparece rank group 2 / absolute 3 com collection `Onitsuka Tiger Mexico 66`.
- Concorrentes: Farfetch, Droper, Instagram, Palmtree48, Accio, Enjoei.
- Interpretação: LK tem boa presença transacional, mas pode ganhar mais resposta textual com FAQ e bloco editorial sobre autenticidade/curadoria.

---

## 3. Auditoria técnica pública atual

### Endpoints GEO/AI

- `https://lksneakers.com.br/llms.txt`
  - Status: 200, mas final URL `https://lksneakers.com.br/agents.md`.
  - Conteúdo: instruções genéricas de agentes/UCP/Shop skill.
  - Marcadores P1 encontrados: 0/8.
  - Risco: alto para GEO; LLMs recebem instruções de transação, não mapa comercial da LK.

- `https://lksneakers.com.br/llms-full.txt`
  - Mesmo problema: final URL `https://lksneakers.com.br/agents.md`.
  - Marcadores P1 encontrados: 0/8.

- `https://lksneakers.com.br/tools/seo/llms.txt`
  - Status: 200, conteúdo comercial real, 84k chars.
  - Marcadores P1 encontrados: 4/8.
  - Problema: é um endpoint secundário; o endpoint raiz que agentes procuram está errado.

### Robots

- `robots.txt` permite bots relevantes:
  - GPTBot: Allow `/`, exceto admin/cart/checkouts.
  - ChatGPT-User: Allow `/`.
  - ClaudeBot: Allow `/`.
  - PerplexityBot: Allow `/`.
  - OAI-SearchBot: Allow `/`.
  - Google-Extended: Allow `/`.
- Interpretação: crawl de AI não está bloqueado; o problema é conteúdo/endpoint/citabilidade, não robots.

### Páginas P1 — baseline on-page

- Home:
  - Title: `LK Sneakers São Paulo | Tênis Originais no Jardins — Nike, Adidas, New Balance`
  - H1: `LK Sneakers — Curadoria de Sneakers e Lifestyle Premium | São Paulo`
  - Schema: WebSite, AggregateRating, local/geo/shipping/return policy.
  - H2s comerciais bons na home: New Balance 204L, Nike Mind 001 & 002, Trending Sneakers etc.

- Collections P1:
  - New Balance 204L, Nike Mind, Onitsuka Mexico 66, Adidas Samba Jane, Air Jordan Travis Scott, Lululemon.
  - Status 200, canonical correto, H1 único, BreadcrumbList + CollectionPage + ItemList.
  - Imagens sem alt faltante detectado.
  - **FAQPage ausente em todas as collections auditadas.**
  - **H2 principal detectado quase sempre só `Less noise, more identity.`**

- PDP Kill Bill:
  - Product schema presente.
  - FAQPage presente.
  - BreadcrumbList presente.
  - Title atual muito longo: 89 chars.
  - Boa presença em Popular Products e SERP.

### Lighthouse/DataForSEO OnPage

- Home: Performance 87; SEO 92; Accessibility 92; Best Practices 73; LCP 1.40s; CLS 0.004; byte weight ~3.09MB.
- Collection NB 204L: Performance 92; SEO 92; Accessibility 95; Best Practices 73; LCP 1.36s; CLS 0.11; byte weight ~2.96MB.
- PDP Kill Bill: Performance 95; SEO 92; Accessibility 94; Best Practices 73; LCP 1.16s; CLS 0.002; byte weight ~3.11MB.

Interpretação: performance sintética está boa. O maior ponto técnico é **Best Practices 73** e peso/JS de terceiros; não é o gargalo principal de Growth agora. Atenção ao CLS 0.11 na collection NB 204L.

---

## 4. Scorecard Claude SEO / GEO

### Score geral

- **SEO técnico básico:** 86/100
- **Shopify SEO on-page:** 84/100
- **Schema estruturado:** 78/100
- **E-commerce SEO:** 86/100
- **GEO/AI Search readiness:** 52/100
- **Search demand/commercial prioritization:** 92/100
- **CRO mobile/public confidence:** 72/100
- **Mensuração/QA:** 70/100

**Score consolidado:** 77/100
**Score de oportunidade:** Alto — o site já tem base comercial e técnica; o ganho vem de corrigir GEO e enriquecer P1, não de refazer tudo.

### Por que GEO ficou baixo

- llms raiz quebrado para o objetivo comercial.
- Collections sem FAQPage.
- Poucos H2s semânticos nas collections.
- Poucos blocos “citáveis” com resposta direta a intenção de compra: onde comprar, autenticidade, curadoria, diferença de colorways, como escolher tamanho/modelo, loja física em Jardins.
- ChatGPT ainda recomenda concorrentes no texto principal.

---

## 5. Checklist dos 18 tópicos canônicos

1. **GA4:** Coberto parcialmente via refresh: sessões/CVR por URL P1. Falta funil PDP → carrinho → checkout atualizado nesta auditoria.
2. **GSC:** Coberto parcialmente via refresh: impressões/CTR por URL P1. Falta query-level detalhado atual por página nesta rodada.
3. **GMC:** Coberto por investigação 2026-05-21. Fontes: Content API principal `10636492695`, legacy local `10636384718`, autofeed `10525577766`; top issues: price_updated, strikethrough_price_updated, missing_item_attribute_for_product_type.
4. **Shopify SEO:** Coberto: titles/metas/H1/canonicals bons nas P1; gap em meta curta Nike Mind e title longo Kill Bill.
5. **Shopify CRO/theme:** Coberto publicamente; sem dev-theme visual nesta rodada. CTA/trust blocks precisam validação mobile em preview antes de produção.
6. **GEO/AI Search:** Coberto em profundidade; maior gargalo atual.
7. **PageSpeed/CrUX/CWV:** Lighthouse coberto; CrUX API retornou 404/sem record via probe, então sem field data nesta rodada.
8. **Schema:** Coberto: collections têm CollectionPage/ItemList/Breadcrumb; PDP tem Product/Offer/FAQPage; collections não têm FAQPage.
9. **Reviews/prova social:** Judge.me detectado como entidade; AggregateRating aparece em schema. Falta auditoria de qualidade/volume real de reviews por P1.
10. **Paid media:** Apenas contextual. Não mexido. Influência de demanda considerada, mas sem dados Meta/Google Ads atuais.
11. **Influencer/social demand:** Contextual: Instagram aparece forte em SERP de Nike Mind e Kill Bill. Falta cruzar com FHITS/Pareto/campanhas.
12. **Concorrência/SERP:** Coberto: Nike, New Balance oficial, Artwalk, Guadalupe, NK, Danki, Menina Shoes, Farfetch, Droper, Palmtree48, Accio, Mercado Livre, Instagram.
13. **Google Business/local:** Parcial: home tem posicionamento Jardins/Oscar Freire e local schema. Falta auditoria de GBP/Maps.
14. **Klaviyo/CRM signals:** Não aplicável para esta auditoria SEO/GEO read-only; sem writes/envios.
15. **Catálogo/product data quality:** Parcial via GMC e public schema. Falta GTIN/MPN/brand completeness por P1 nesta rodada.
16. **Conteúdo/taxonomia comercial:** Coberto: collections corretas, mas conteúdo estrutural insuficiente para GEO.
17. **Mensuração/QA de eventos:** Parcial via connector probe; GA4 LK ok, segunda property 403. Falta evento add_to_cart/checkout QA.
18. **Impact review/experimentation:** Recomendado criar baseline e revisão em 7 dias após qualquer mudança.

---

## 6. Fila priorizada de ação

### P0 — Corrigir `llms.txt` e `llms-full.txt` raiz

**Impacto:** Alto para GEO/AI Search.
**Esforço:** Baixo/médio.
**Risco:** Médio, por ser produção; mitigável com backup/rollback.
**Status:** Precisa aprovação explícita atual.

O conteúdo certo já existe parcialmente em `/tools/seo/llms.txt`, mas o root `/llms.txt` e `/llms-full.txt` estão servindo `agents.md`. A correção deve fazer os endpoints raiz entregarem a versão comercial/citável.

Payload recomendado:

- Identidade LK e proposta comercial.
- Loja física Jardins/Oscar Freire.
- Páginas P1: NB 204L, Nike Mind 001, Onitsuka Tiger, Adidas Samba Jane, Travis Scott, Lululemon, Kill Bill.
- Blocos curtos de autenticidade/curadoria/atendimento humano.
- Links canônicos para collections/PDPs.
- FAQ enxuta de compra segura.

### P1 — Adicionar blocos GEO/FAQ nas collections P1 em dev theme

**Impacto:** Alto.
**Esforço:** Médio.
**Risco:** Baixo se feito em dev theme/preview.
**Status:** Pode preparar preview; publicar produção precisa aprovação.

Collections prioritárias:

1. New Balance 204L
2. Nike Mind 001
3. Onitsuka Tiger Mexico 66
4. Onitsuka Tiger todos os modelos
5. Adidas Samba Jane
6. Air Jordan Travis Scott
7. Lululemon

Formato recomendado por página:

- H2: `Comprar [modelo] original na LK Sneakers`
- Bloco citável de 134–167 palavras.
- FAQ com 3 perguntas:
  - Onde comprar [modelo] original no Brasil?
  - A LK trabalha com produtos autênticos?
  - Como escolher tamanho/cor/versão?
- JSON-LD FAQPage ligado ao conteúdo visível.

### P1 — Ajustes SEO pontuais

- Nike Mind 001: meta description curta; expandir para ~150–160 chars com intenção de compra/autenticidade.
- Kill Bill PDP: title muito longo; criar versão mais limpa sem perder termo principal.
- Collections: adicionar H2s semânticos além do bloco de marca.

### P2 — Melhorar presença em ChatGPT/AI Search

- Criar/fortalecer páginas e trechos que respondam “onde comprar X original no Brasil”.
- Adicionar seção de confiança editorial na home/collections.
- Medir novamente em 7 dias: ChatGPT, Perplexity/Gemini se disponível, Google SERP, AI Overview quando retornado.

### P2 — QA de schema/reviews

- Validar se AggregateRating é legítimo e consistente por página.
- Checar se reviews aparecem de forma confiável no HTML público e schema.
- Evitar schema de FAQ sem conteúdo visível equivalente.

### P3 — CRO mobile

- Rodar preview visual mobile das P1 depois da inclusão de blocos.
- Checar: primeiro CTA, preço, parcelamento, frete, trust block, chat humano e prova social.

---

## 7. Approval packet proposto

### Packet A — Produção: root `llms.txt` / `llms-full.txt`

**Pedido de aprovação:** Autorizar correção dos endpoints raiz `https://lksneakers.com.br/llms.txt` e `https://lksneakers.com.br/llms-full.txt` para servirem conteúdo comercial GEO da LK em vez de `agents.md`.

**Sem alterar:** tema production, title/meta visível, preço, estoque, GMC, campanhas, Klaviyo/WhatsApp.

**Backup obrigatório antes:**

- Snapshot de `/llms.txt`, `/llms-full.txt`, `/agents.md` e configuração/app responsável.
- Hash SHA256 antes/depois.
- Registro do caminho técnico alterado.

**Rollback:**

- Restaurar arquivo/config anterior.
- Validar `curl -L https://lksneakers.com.br/llms.txt` e `curl -L https://lksneakers.com.br/llms-full.txt` retornando o conteúdo anterior se necessário.

**Verificação pós:**

- `curl -L` nos dois endpoints.
- Checar presença de 7 marcadores P1.
- Checar que status é 200 e não redireciona para `agents.md`.

### Packet B — Dev theme: blocos GEO + FAQPage nas collections P1

**Pedido de aprovação:** Autorizar implementação em dev theme/preview, sem publish em production, de blocos GEO visíveis e FAQPage nas collections P1.

**Sem alterar:** production theme, preço, estoque, GMC, campanhas, Klaviyo/WhatsApp.

**Rollback:** remover seção/snippet do dev theme ou restaurar backup do arquivo alterado.

**Verificação pós:**

- Preview mobile.
- HTML contém H2/FAQ visíveis.
- JSON-LD FAQPage válido.
- Sem regressão visual premium/minimalista.

### Packet C — SEO fields production posterior

**Não executar agora sem nova aprovação.**
Ajustar meta/title de Nike Mind e Kill Bill só depois de validar texto e rollback.

---

## 8. Próximo passo recomendado

A ordem mais segura e com melhor ROI:

1. Aprovar Packet A para corrigir `llms.txt` e `llms-full.txt` em produção com backup/rollback.
2. Em paralelo, preparar Packet B em dev theme/preview para collections P1.
3. Medir impacto em 7 dias: ChatGPT citations, Google SERP, GSC CTR/impressões, GA4 sessions/CVR.

---

## 9. Custos DataForSEO registrados

- `kw_data_google_ads_search_volume`: USD 0.05
- `serp_organic_live_advanced`: USD 0.006 total nesta auditoria
- `on_page_lighthouse`: USD 0.06
- `ai_optimization_chat_gpt_scraper`: USD 0.02
- Total estimado registrado hoje após auditoria: USD 0.136

---

## 10. Não executado

- Nenhum write Shopify production.
- Nenhum publish de tema.
- Nenhuma alteração de title/meta/descrição pública.
- Nenhum write no Google Merchant Center.
- Nenhuma campanha, email, WhatsApp ou ação customer-facing.
- Nenhuma exposição de segredo.
