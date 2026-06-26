# LK Growth — Google SEO Opportunity Factory — Nike Mind 001/002 — 2026-06-23

**Modo:** read-only / approval packet.  
**Writes externos:** 0. Sem Shopify/theme/GMC/feed/GA4/GSC/Klaviyo/WhatsApp/Ads/preço/estoque/desconto write.  
**values_printed:** false.  
**Rotina:** terça-feira — Google SEO Opportunity Factory.  
**URL foco:** `https://lksneakers.com.br/collections/nike-mind-001`.

## Veredito

Há achado material: a oportunidade Google da semana é consolidar a intenção **Nike Mind 001/002** na collection/hub, porque o GSC mostra demanda alta em posição 4–20 com CTR baixo e distribuição entre PDPs, guia e collection. A collection pública está tecnicamente saudável no básico (HTTP 200, H1 único, canonical, `FAQPage` único), mas o handle `/collections/nike-mind-002` retorna 404; portanto, a melhor decisão agora é fortalecer a collection existente `/collections/nike-mind-001` como hub “Mind 001 e 002” e alinhar PDPs/guia via links internos, sem criar write de produção sem aprovação.

## Fontes verificadas

- **GSC read-only:** `reports/lk-search-console-readonly-router-2026-05-11.json`, regenerado em 2026-06-23; janela `2026-05-24 → 2026-06-20`, property `sc-domain:lksneakers.com.br`, 25.000 linhas query/page, writes 0.
- **Shopify/GA4 decision refresh read-only:** `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.json`, regenerado em 2026-06-23; collection `nike-mind-001` P1, score 98, `decision_grade_refresh_ready_for_preview`.
- **Public HTML QA:** `https://lksneakers.com.br/collections/nike-mind-001` HTTP 200, title/meta/H1/canonical ok, `FAQPage` count 1; `/collections/nike-mind-002` HTTP 404.
- **SERP live fallback:** web search read-only para `nike mind 001 Brasil comprar original` mostrou LK PDP entre os primeiros resultados; para `nike mind 002 Brasil comprar original`, top 5 ficou dominado por Nike/marketplaces/social e não trouxe LK, reforçando gap de hub/intent para Mind 002.
- **DataForSEO:** MCP/tooling não exposto nesta runtime; usei GSC + Shopify/GA4 + public SERP fallback. Não inventei volume/AI visibility.

## Evidência GSC/SERP

### Queries-alvo

| Query | Página | Cliques | Impressões | CTR | Posição | Leitura |
|---|---|---:|---:|---:|---:|---|
| `nike mind 001` | PDP Black Chrome | 4 | 37.295 | 0,01% | 9,1 | alta demanda, CTR crítico |
| `nike mind 001` | PDP Pearl Pink | 11 | 30.808 | 0,04% | 9,0 | canibalização entre PDPs |
| `chinelo nike mind 001` | PDP Black Chrome | 6 | 10.641 | 0,06% | 6,0 | posição boa, snippet fraco |
| `nike mind 001` | Guia Nike Mind 001/002 | 11 | 4.905 | 0,22% | 9,5 | guia aparece, mas não captura bem |
| `nike mind 002` | PDP Black Hyper Crimson | 1 | 1.126 | 0,09% | 10,6 | oportunidade emergente 002 |
| `nike mind 002` | Guia Nike Mind 001/002 | 2 | 572 | 0,35% | 9,8 | guia ajuda, mas não resolve hub |

### Evidência comercial/landing

- Collection `/collections/nike-mind-001`: GA4 133 sessões, 258 views, 0 compras landing na janela do refresh; GSC agregado 79 cliques / 6.532 impressões / CTR 1,21% / posição 7,9.
- Shopify/local spine + refresh: collection Mind 001 com 147 unidades combinadas e R$ 464.158,55 combinados; evidência comercial suficiente para priorizar SEO/CRO. Estoque/Tiny não foi consultado e não entrou como critério.

## Diagnóstico do problema

1. **Canibalização/intenção:** Google distribui `nike mind 001` entre PDPs, guia e collection. Para termo amplo, o usuário provavelmente precisa comparar 001 vs 002 e escolher versão/colorway; PDP isolado é menos adequado que collection/guia.
2. **Mind 002 sem collection própria:** `/collections/nike-mind-002` está 404; para busca `nike mind 002`, a SERP fallback não mostrou LK no top 5, enquanto há PDPs relevantes. Isso sugere que o hub atual precisa declarar melhor o 002 ou, em etapa posterior, avaliar se deve existir collection 002 separada.
3. **Snippet atual bom, mas pouco orientado a decisão:** title/meta atuais já são seguros, porém podem comunicar melhor “guia + compra” e reduzir dúvida entre slide Mind 001 e sneaker Mind 002.
4. **Schema/FAQ:** collection já tem `FAQPage` único, então o packet não é correção de duplicidade; é melhoria de correspondência entre FAQ real-intent, visible FAQ e JSON-LD.

## Auditoria da URL foco

| Campo | Estado atual |
|---|---|
| URL | `https://lksneakers.com.br/collections/nike-mind-001` |
| HTTP | 200 |
| Canonical | `https://lksneakers.com.br/collections/nike-mind-001` |
| Title atual | `Nike Mind 001 e 002 Original no Brasil | LK` — 43 chars |
| Meta atual | `Nike Mind 001 e 002 original no Brasil: compare slides e sneakers Nike Mind com curadoria LK, autenticidade e atendimento humano para escolher modelo.` — 146 chars |
| H1 atual | `Nike Mind 001/002` |
| JSON-LD | 4 blocos; `FAQPage` count 1 |
| Limitação | PageSpeed/CrUX não reexecutado nesta micro-rotina; DataForSEO indisponível na runtime atual |

## Approval packet — proposta concreta

### 1) SEO title

- **Atual:** `Nike Mind 001 e 002 Original no Brasil | LK` — 43 chars
- **Proposto:** `Nike Mind 001 e 002 Original | Guia e Compra LK` — 47 chars
- **Hipótese:** troca “no Brasil” por “Guia e Compra” para refletir intenção mista de comparação + compra, sem perder entidade.

### 2) Meta description

- **Atual:** `Nike Mind 001 e 002 original no Brasil: compare slides e sneakers Nike Mind com curadoria LK, autenticidade e atendimento humano para escolher modelo.` — 146 chars
- **Proposta:** `Compare Nike Mind 001 e 002 originais na LK: slide Mind 001, sneaker Mind 002, colorways raras, curadoria exclusiva e atendimento humano.` — 137 chars
- **Hipótese:** fica mais específico por produto/silhueta e mais escaneável para CTR.

### 3) H1 visível

- **Atual:** `Nike Mind 001/002`
- **Proposto:** `Nike Mind 001 e 002`
- **Risco:** baixo, mas é mudança visível Shopify/tema/conteúdo; precisa aprovação atual.

### 4) Bloco de abertura / copy citável

> A coleção Nike Mind da LK reúne o Mind 001, slide escultural de conforto sensorial, e o Mind 002, versão sneaker de perfil futurista para quem quer a mesma linguagem em uso urbano. A curadoria separa colorways como Black Chrome, Pearl Pink, Black Hyper Crimson, Light Khaki e Thunder Blue, com foco em pares originais, proporção, material e styling premium. Use esta página para comparar 001 vs 002, entender qual silhueta combina com seu uso e, se precisar, conte com atendimento humano para escolher a versão certa.

- **Tamanho:** 517 chars.
- **GEO:** bloco auto-contido, citável e com entidades/colorways; sem promessa de estoque, pronta entrega, prazo ou desconto.

### 5) FAQ — Real Intent Gate

| Pergunta proposta | Fonte de intenção | generic-filler |
|---|---|---|
| Qual a diferença entre Nike Mind 001 e Nike Mind 002? | GSC `nike mind 001`, GSC `nike mind 002`, comparação real entre versões | false |
| O Nike Mind 001 é chinelo, mule ou sneaker? | GSC `chinelo nike mind 001`, SERP/product type dominante | false |
| O Nike Mind 002 funciona para looks de rua? | styling/objeção comercial específica do sneaker 002 | false |
| O Nike Mind tem a forma grande ou pequena? | dúvida específica de calçado/tamanho; responder sem claim absoluto e com atendimento humano | false |
| Onde comprar Nike Mind original no Brasil com segurança? | SERP/GEO/buying-safety + autenticidade específica | false |

**QA schema:** manter 1 FAQ visível e 1 `FAQPage` JSON-LD com perguntas idênticas; remover/evitar FAQ legado duplicado se aparecer no render final.

### 6) Links internos

- De `PDP Mind 001 Black Chrome`, `Pearl Pink` e `Light Smoke Grey` → link contextual para `/collections/nike-mind-001` com âncora `comparar Nike Mind 001 e 002`.
- De PDPs Mind 002 principais → link para `/collections/nike-mind-001` até decidir se `/collections/nike-mind-002` deve existir.
- Do guia `/pages/guia-nike-mind-001-002` → CTA limpo para a collection foco.
- Da collection → manter CTA para o guia editorial quando existir, sem duplicar bloco longo.

## Impacto esperado, risco e rollback

- **Impacto esperado:** aumentar CTR para queries `nike mind 001`, `chinelo nike mind 001` e `nike mind 002`; reduzir canibalização e dar ao Google/LLMs um hub claro de comparação.
- **Meta D+7/D+14:** CTR query `nike mind 001` nos principais URLs sair de 0,01–0,22% para ≥0,40% sem perda de posição média; CTR collection manter/subir acima de 1,21%; manter `FAQPage` único.
- **Risco:** baixo/moderado para SEO fields; médio se mexer em conteúdo visível/layout. Pode haver oscilação temporária de snippet.
- **Rollback:** antes de qualquer write, snapshot de `seo.title`, `seo.description`, H1/description/source body e asset/section se houver tema; reverter campo a campo se CTR/conversão/render piorarem.

## Aprovação necessária

Para executar em produção, Lucas precisa aprovar explicitamente os campos acima e o escopo. Wording sugerido:

> `Aprovo aplicar o packet Nike Mind 001/002 de 2026-06-23 somente na URL/handle /collections/nike-mind-001 e nos links internos listados, com rollback/readback, sem alterar preço, estoque, desconto, campanha, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo.`

## Não executado

- Nenhum write Shopify, theme, GMC/feed, GA4/GSC config, Ads, Klaviyo, WhatsApp, preço, desconto ou estoque.
- Não consultei Tiny/estoque; disponibilidade operacional pertence ao `lk-stock`.
- Não publiquei title/meta/H1/copy/FAQ/schema/internal links; tudo está em preview/approval packet.
