# LK Growth — Audit SEO/GEO coleção Nike x Jacquemus Moon Shoe

Data: 2026-05-25  
Status: read-only; nenhum write em Shopify/GMC/ads/Klaviyo/produção.  
URL auditada: https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp

## Veredito executivo

A coleção está acima da média para SEO/GEO: tem URL correta, H1 único, conteúdo editorial na própria coleção, FAQ visível, `CollectionPage`, `ItemList`, `FAQPage`, robots liberando crawlers de IA e presença forte no Google. O maior ganho agora não é “mais texto genérico”; é padronizar a experiência de coleção + source page, corrigir copy operacional e aumentar citabilidade/autoridade para IA.

Prioridade recomendada: preparar preview local/dev da source page `nike-moon-shoe-jacquemus-guia-lk` e ajustar, em pacote separado de aprovação, a meta/copy pública da coleção para remover termos operacionais.

## Evidências consultadas

### Público / HTML

- Status público: 200 via extração pública.
- Title público reportado por web extract/DataForSEO: `Nike x Jacquemus Moon Shoe SP | Collab 2026 | LK Sneakers`.
- Meta pública: `Nike Jacquemus Moon Shoe SP: 6 colorways originais da collab 2026 a partir de R$ 5.000 em 10x. Estoque limitado · Entrega SP · Autenticidade.`
- Canonical: `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp`.
- H1: único — `Nike x Jacquemus Moon Shoe SP`.
- Produtos listados: 6 sneakers.
- Imagens no HTML: 17; sem alt ausente/vazio no parse bruto.
- Schema detectado: `Organization`, `ShoeStore`, `ClothingStore`, `BreadcrumbList`, `CollectionPage`, `ItemList`, `FAQPage`, `Question`, `Answer`, além de políticas/entrega/retorno.
- Robots: permite GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot e OAI-SearchBot; bloqueia crawlers de SEO como Ahrefs/Semrush, o que é aceitável.
- llms.txt existe, mas o documento raiz ainda destaca outras páginas prioritárias e não inclui Moon Shoe como prioridade comercial.

### SERP / demanda

- DataForSEO SERP mobile BR para `Nike Moon Shoe Jacquemus original Brasil`: LK aparece orgânico #1 e em `Popular products` com produtos LK.
- Concorrentes/entidades na SERP: Farfetch, Instagram LK, Etiqueta Única, Jacquemus, FFW, Nike, SneakersBR.
- Keyword volume Google Ads BR:
  - `nike moon shoe jacquemus`: volume médio 50; pico recente 140 em 2026-03, 110 em 2026-04; competição alta.
  - `nike x jacquemus moon shoe`: volume médio 30; pico 90 em 2026-03; competição alta.
  - `nike moon shoe sp jacquemus`: volume médio 20; pico 70 em 2026-03/04; competição alta.
- GSC histórico interno anterior: 166 cliques, 5.872 impressões, CTR 2,83%, posição média 3,0.
- Relatórios internos anteriores: 249–266 unidades e acima de R$ 1,27M–1,30M em proxy/receita combinada.

### AI / GEO

- ChatGPT web search para `onde comprar Nike Moon Shoe Jacquemus original no Brasil`: LK apareceu em produtos/cards via shopping, mas não como fonte textual principal.
- Fontes textuais citadas/privilegiadas por IA: Jacquemus oficial, Nike Brasil e Reddit; resposta também usa marketplaces/lojas como Juicy, Step Up, Diamond, Droper.
- Estado atual da LK: `merchant_card` presente; `text_citation` ainda fraco.

## Scorecard Claude SEO/GEO

- SEO on-page: 82/100
  - Forte: URL, H1, canonical, produtos, conteúdo editorial, alt text, schema básico.
  - Fraco: meta com termo operacional, title possivelmente contaminado no HTML bruto por texto de métodos de pagamento, pouca hierarquia editorial além de H1 + FAQ.

- E-commerce SEO: 78/100
  - Forte: 6 PDPs relacionados, preço/parcelamento visível, Product/ItemList na arquitetura.
  - Fraco: collection ainda não separa claramente decisão por colorway, autenticidade, fit e styling em blocos escaneáveis suficientes para conversão mobile.

- GEO / AI Search: 70/100
  - Forte: robots permite IA, llms.txt existe, FAQ visível, narrativa editorial já presente.
  - Fraco: Moon Shoe não está no llms.txt prioritário, falta source page profunda citável, falta bloco “onde comprar original no Brasil” com resposta direta e fontes, e a LK aparece mais como produto/card do que como autoridade textual.

- Schema: 78/100
  - Forte: `CollectionPage`, `ItemList`, `FAQPage`, `BreadcrumbList` presentes.
  - Ajuste: manter FAQ como conteúdo visível, mas não depender de rich result Google; enriquecer source page com `Article`/`WebPage` quando criada.

- CRO editorial/mobile: 72/100
  - Forte: coleção já tem curadoria e produtos.
  - Fraco: oportunidade de hero editorial compacto, tabela de colorways e FAQ de decisão de compra mais útil.

## Melhorias recomendadas

### P0 — Corrigir copy operacional da meta/snippet

Problema: a meta pública usa `Estoque limitado` e `Entrega SP`. Isso foge do guardrail LK de não usar estoque/prazo como taxonomia pública.

Proposta de meta substituta:

`Nike x Jacquemus Moon Shoe SP na curadoria LK: modelos originais, colorways desejadas, leitura fashion e atendimento humano para confirmar tamanho e prazo.`

Impacto: melhora aderência premium, reduz risco operacional e mantém intenção comercial.

Aprovação necessária: sim, porque altera SEO field/produção Shopify.

### P1 — Publicar somente após preview a source page citável

URL proposta: `/pages/nike-moon-shoe-jacquemus-guia-lk`.

Função: responder perguntas informacionais que a coleção não deve carregar sozinha.

Estrutura recomendada:

1. O que é o Nike Moon Shoe?
2. Por que o modelo é importante para a Nike?
3. Como Jacquemus reinterpretou o Moon Shoe?
4. Colorways: Alabaster, Off Noir, University Red, Off White/Sail, Medium Brown, Pale Pink.
5. Como escolher tamanho/cor com atendimento humano.
6. Onde comprar Nike Moon Shoe Jacquemus original no Brasil.
7. Como a LK verifica/seleciona pares originais.
8. FAQ citável.
9. CTA para coleção.

Impacto: aumentar chance de `text_citation` em ChatGPT/Perplexity/AI Overview e proteger a coleção contra excesso de texto.

Aprovação necessária: preview local/dev não; publicação Shopify sim.

### P1 — Atualizar llms.txt para incluir Moon Shoe como priority page

O llms.txt existe e é bom, mas não destaca a coleção Moon Shoe. Adicionar:

`Nike x Jacquemus Moon Shoe SP original — https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp — coleção LK de pares originais da collab Nike/Jacquemus, com foco em curadoria, história do Moon Shoe, colorways e atendimento humano para confirmação de tamanho e prazo.`

Após source page live, incluir também:

`Guia Nike Moon Shoe Jacquemus — https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk — fonte editorial LK sobre origem Bowerman, solado waffle, releitura Jacquemus, colorways e autenticidade.`

Aprovação necessária: sim, se for alterar arquivo público/tema/app.

### P1 — Repensar FAQ

FAQ atual deve sair do genérico e virar FAQ de decisão + citabilidade.

Perguntas recomendadas:

- O que é o Nike x Jacquemus Moon Shoe?
- Por que o Moon Shoe Jacquemus é tão desejado?
- O Nike Moon Shoe Jacquemus é feminino ou unissex?
- Como ele calça: mais sneaker ou mais sapatilha?
- Qual colorway escolher: Alabaster, Off Noir, University Red, Off White, Medium Brown ou Pale Pink?
- Como saber se o Nike Moon Shoe Jacquemus é original?
- Onde comprar Nike Moon Shoe Jacquemus original no Brasil?
- Como a LK seleciona os pares Nike x Jacquemus?

Guardrail: não mencionar restrições regionais, pronta entrega, encomenda ou estoque como promessa pública.

### P2 — Melhorar a coleção como landing comercial

Adicionar/validar em preview:

- Hero mobile com 3 linhas + imagem editorial/on-foot quando possível.
- Tabela curta de colorways.
- Bloco “como escolher” por intenção: minimalista, statement, editorial, tons terrosos.
- CTA para atendimento humano sem prometer disponibilidade.
- Link claro para source page editorial.
- Remover qualquer moldura bege e manter estética branca/off-white minimalista.

### P2 — Schema no padrão correto

Na coleção:

- manter `CollectionPage`, `ItemList`, `BreadcrumbList`;
- revisar se `FAQPage` está 100% espelhado no conteúdo visível;
- não tratar FAQ schema como canal principal de rich result, pois Google restringe FAQ rich result a gov/health.

Na source page:

- `WebPage` + `Article` + `BreadcrumbList` + `Organization`;
- opcionalmente `FAQPage` se FAQ estiver visível, como apoio sem expectativa de rich result Google.

## Checklist 18 tópicos canônicos

- GA4: dado interno anterior usado; não reconsultado neste turno.
- GSC: dado histórico usado; não reconsultado via API neste turno.
- GMC: não aplicável ao audit textual da collection; produtos aparecem em Popular Products/merchant cards.
- Shopify SEO: auditado via HTML público/title/meta/canonical/H1.
- Shopify CRO/theme: audit visual não executado em browser; recomendações mobile baseadas em conteúdo/estrutura pública e guardrails LK.
- GEO/AI Search: auditado com robots, llms.txt e ChatGPT scraper.
- PageSpeed/CrUX/CWV: não medido neste turno; pendente se for para production-grade theme audit.
- Schema: auditado via HTML bruto.
- Reviews/prova social: Judge.me detectado no HTML/config; impacto específico na coleção não medido.
- Paid media: não alterado; sinais internos anteriores indicam campanha Jacquemus forte.
- Influencer/social demand: campanha/Instagram aparecem como contexto; não auditado profundamente.
- Concorrência/SERP: auditado via DataForSEO SERP.
- Google Business/local: não aplicável à coleção, exceto entidade LK/Jardins já presente no schema/llms.
- Klaviyo/CRM signals: não alterado; não auditado neste turno.
- Catálogo/product data quality: produtos e links públicos auditados; GTIN/SKU não auditados.
- Conteúdo/taxonomia comercial: auditado; principal gap é source page + FAQ decisório.
- Mensuração/QA de eventos: não auditado neste turno.
- Impact review/experimentation: recomendado D+7 após qualquer mudança aprovada.

## Risco / rollback

- Risco baixo para preparação local/dev.
- Risco médio para alterar SEO/meta pública, porque pode impactar snippet de uma página que já ranqueia bem.
- Rollback para SEO fields: snapshot do title/meta/body atual antes de qualquer update; readback Admin + verificação pública; reversão imediata se snippet/copy ficarem fora do padrão.

## Próxima decisão recomendada

Aprovar apenas preparação de preview local/dev:

`Aprovo preparar o preview local/dev da source page Nike Moon Shoe Jacquemus e do ajuste de FAQ/meta da coleção, sem publicar em produção e sem alterar preço, estoque, GMC, campanhas, Klaviyo ou WhatsApp.`
