# LK Growth — Auditoria read-only de coleções com copy/SEO fora do guardrail

Data: 2026-06-05  
Escopo: coleções Shopify; leitura read-only Admin API + spot-check público.  
Status: **nenhum write executado**.

## Veredito executivo

Sim, há outras coleções com problemas parecidos com o caso Moon Shoe.

Principais achados:

- **46 coleções** têm termos operacionais em SEO title/description, principalmente `Pronta entrega` / `Pronta entrega SP`.
- **155 coleções** têm termos operacionais no corpo/FAQ público, principalmente `Produtos em estoque` em FAQ de prazo.
- **58 coleções** usam `rodar` no corpo/FAQ de numeração; não é tão grave quanto estoque/prazo, mas foge do tom premium e pode ser trocado por “forma” / “calça” / “ajuste”.
- **13 coleções** sem SEO title customizado no Admin.
- **11 coleções** sem SEO description customizada no Admin.
- **1 coleção** com SEO description longa demais.

Classificação: **audit técnico read-only, decision-grade para identificar problemas de copy/SEO**, mas não prioriza por receita/GA4/GSC ainda.

## Evidência

- Shopify Admin GraphQL: 179 coleções lidas.
- Sitemap público: 178 collection URLs identificadas.
- Spot-check público confirmou que pelo menos uma coleção prioritária (`new-balance-9060`) renderiza em produção meta com `Pronta entrega` e FAQ com `Produtos em estoque`.
- Fetch público também confirmou FAQ operacional em `lancamentos` e `adidas-todos-os-modelos`.

## P0 — SEO/meta crítico com termo operacional

Estas são as candidatas a hotfix editorial porque o termo aparece em metadados, snippet potencial de Google/IA e share cards.

- `lancamentos` — produtos: 2007; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Confira os Lançamentos na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `nike-todos-os-modelos` — produtos: 615; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Nike original no Brasil: 600 modelos (Air Force 1, Dunk, Air Max, Jordan) em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja Jardins SP.
- `camiseta-1` — produtos: 319; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Camisetas streetwear originais: Fear of God, Nude Project, Supreme, Essentials e mais. 300+ modelos em 10x sem juros · Pronta entrega · Frete grátis.
- `adidas-todos-os-modelos` — produtos: 265; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Adidas original no Brasil: 260 modelos (Samba, Gazelle, Campus, SL 72) em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja SP.
- `air-jordan-1` — produtos: 209; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Air Jordan 1 originais: 203 colorways (Low, Mid, High, OG) a partir de R$ 1.300 em 10x sem juros. Pronta entrega · Loja SP · 100% autêntico.
- `todos-special-collections` — produtos: 203; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Collabs raras e edições limitadas: Travis Scott, Off-White, Jacquemus, ALD. 203 peças exclusivas em 10x · Pronta entrega · Autenticidade garantida.
- `athleisure` — produtos: 156; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Athleisure premium: Alo Yoga, Lululemon, Skims e mais. 152 peças originais em 10x sem juros · Pronta entrega · Frete grátis +R$500 · Loja SP.
- `moletom-1` — produtos: 112; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Moletons originais: Fear of God Essentials, Nude Project, Represent, Supreme. 109 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `nude-project` — produtos: 97; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Nude Project original no Brasil: 90 peças streetwear espanhol a partir de R$ 600 em 10x. Moletons, camisetas · Pronta entrega SP · Frete grátis.
- `aime-leon-dore` — produtos: 93; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Aimé Leon Dore original no Brasil: 80 peças e collabs Porsche, New Balance. 10x sem juros · Pronta entrega · Frete grátis +R$500 · Loja SP.
- `bone-streetwear` — produtos: 88; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Bonés streetwear originais: Pace, Aimé Leon Dore, Supreme, Slyce. 78 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500 · Loja SP.
- `acessorios-best-sellers` — produtos: 81; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Acessórios mais desejados: bonés Pace, Aimé Leon Dore, óculos Saint, Labubu. 124 itens em 10x sem juros · Pronta entrega SP · Frete grátis +R$500.
- `cloud-dancer` — produtos: 74; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Cloud Dancer na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `calca-streetwear` — produtos: 70; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Calças streetwear originais: Lululemon Scuba, Alo Yoga, Fear of God, Nude. 70 modelos em 10x sem juros · Pronta entrega · Frete grátis.
- `nike-dunk-sb` — produtos: 69; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Nike Dunk SB originais: Grateful Dead, Jarritos, Concepts, colabs raras. 67 colorways em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `collectibles` — produtos: 66; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Collectibles originais: Labubu, Pop Mart Molly, figuras raras. 66 itens exclusivos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `new-balance-9060` — produtos: 51; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Confira os New Balance 9060 na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `yeezy` — produtos: 40; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Yeezy originais: 40 modelos (Boost 350 V2, Slide, Foam Runner, 500) a partir de R$ 900 em 10x sem juros. Pronta entrega · Loja SP.
- `jacquemus` — produtos: 38; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Jacquemus original no Brasil: bolsas, camisetas, Le Chiquito, Moon Shoe. 35 peças em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `fear-of-god` — produtos: 36; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Fear of God Essentials original: 36 peças streetwear (moletons, camisetas, calças) a partir de R$ 1.200 em 10x sem juros. Pronta entrega SP.
- `adidas-gazelle` — produtos: 32; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Adidas Gazelle originais: 32 colorways clássicos em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja Jardins SP · 100% autêntico.
- `jaqueta-streetwear` — produtos: 31; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Jaquetas streetwear originais: Fear of God Essentials, Nude Project, Represent. 27 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `nike-air-force-1` — produtos: 30; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Nike Air Force 1 originais: Low, Mid e High em todos os colorways a partir de R$ 1.300 em 10x sem juros. Pronta entrega · Loja SP · Autêntico.
- `aime-leon-dore-x-porsche` — produtos: 27; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Aimé Leon Dore x Porsche: 27 peças da collab mais desejada de 2026. Pronta entrega em 10x sem juros · Frete grátis · Autenticidade garantida.
- `dane-se` — produtos: 27; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Dane-se original no Brasil: streetwear nacional premium. 27 peças em 10x sem juros · Pronta entrega · Frete grátis +R$500 · Loja SP.
- `nike-air-max` — produtos: 26; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Nike Air Max originais: 26 modelos clássicos e modernos em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja Jardins SP · 100% autêntico.
- `adidas-gazelle-indoor` — produtos: 23; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Adidas Gazelle Indoor originais: 23 colorways exclusivos em 10x sem juros. Pronta entrega SP · Frete grátis +R$500 · 100% autêntico.
- `calcas-alo-yoga` — produtos: 20; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Calças Alo Yoga originais: Airlift, Accolade, 7/8, todos os colorways. 20 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- `adidas-x-bad-bunny` — produtos: 17; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Adidas x Bad Bunny na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `on-running-cloudsolo` — produtos: 16; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Explore a coleção On Running Cloudsolo na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-handball-spezial` — produtos: 15; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Compre Adidas Handball Spezial na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-taekwondo-mei-ballet` — produtos: 14; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Compre Adidas Taekwondo Mei Ballet na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-tokyo` — produtos: 11; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Compre Adidas Tokyo na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `mickey-family-keychain` — produtos: 11; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Mickey Family Keychain na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `dane-se-x-rubem-valentim` — produtos: 10; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Dane-se x Rubem Valentim na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `havaianas-x-dolce-gabbana` — produtos: 10; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Explore a coleção Havaianas X Dolce & Gabbana na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `acessorios-alo-yoga` — produtos: 6; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Acessórios Alo Yoga na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-animal-pack` — produtos: 6; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Adidas Animal Pack na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `asics-gt-2160` — produtos: 6; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Asics GT-2160 na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `egho-studios` — produtos: 6; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Egho Studios na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-adi2000` — produtos: 5; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Adidas ADI2000 na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `adidas-originals-x-korn` — produtos: 4; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Compre Adidas Originals x KoRn na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `alo-yoga-slipper-recovery` — produtos: 4; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Alo Yoga Slipper Recovery na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `onitsuka-tiger-mexico-66-metallic-series` — produtos: 4; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Compre Onitsuka Tiger Mexico 66 Metallic Series na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `sapatos-saint-studio` — produtos: 4; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
  - SEO desc: Explore a coleção Sapatos - Saint Studio na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.
- `geral-best-sellers` — produtos: 0; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
  - SEO desc: Explore a coleção Geral Best Sellers na LK Sneakers. Pronta entrega · 100% originais · Parcele em 10x · Loja Jardins SP.

## P1 — Corpo/FAQ público com termo operacional

O padrão mais recorrente é FAQ de prazo com `Produtos em estoque: envio...`. Deve virar linguagem de atendimento humano/confirmar prazo, ou ser removido das collections onde não é diferencial comercial.

Top por volume de produtos:

- `ultimos-lancamentos-2` — produtos: 2329; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `lancamentos` — produtos: 2007; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `sneakers` — produtos: 1249; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `roupas` — produtos: 736; issues: blocked_body:produtos em estoque
- `nike-todos-os-modelos` — produtos: 615; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `sale` — produtos: 358; issues: blocked_body:Estoque limitado,produtos em estoque; fit_term_body:rodar
- `camiseta-1` — produtos: 319; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `adidas-todos-os-modelos` — produtos: 265; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `air-jordan` — produtos: 215; issues: blocked_body:produtos em estoque
- `air-jordan-1` — produtos: 209; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `todos-special-collections` — produtos: 203; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `nike-dunk` — produtos: 180; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `onitsuka-tiger-todos-os-modelos` — produtos: 159; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `athleisure` — produtos: 156; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `acessorios` — produtos: 149; issues: blocked_body:produtos em estoque
- `new-balance-todos-os-modelos` — produtos: 139; issues: blocked_body:produtos em estoque
- `alo-yoga-1` — produtos: 115; issues: blocked_body:produtos em estoque; fit_term_body:rodar; seo_desc_long
- `moletom-1` — produtos: 112; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `onitsuka-tiger-mexico-66` — produtos: 101; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `nude-project` — produtos: 97; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque
- `samba` — produtos: 96; issues: blocked_body:produtos em estoque
- `aime-leon-dore` — produtos: 93; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `bone-streetwear` — produtos: 88; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `saint-studio` — produtos: 82; issues: blocked_body:produtos em estoque
- `acessorios-best-sellers` — produtos: 81; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque
- `pace` — produtos: 75; issues: blocked_body:produtos em estoque
- `cloud-dancer` — produtos: 74; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `calca-streetwear` — produtos: 70; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `nike-dunk-sb` — produtos: 69; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `collectibles` — produtos: 66; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `pop-mart` — produtos: 60; issues: blocked_body:produtos em estoque
- `recomendacoes-masculinas-by-helena-lunardelli` — produtos: 53; issues: blocked_body:produtos em estoque
- `supreme` — produtos: 52; issues: blocked_body:produtos em estoque
- `new-balance-9060` — produtos: 51; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `labubu` — produtos: 47; issues: blocked_body:produtos em estoque
- `lululemon` — produtos: 41; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `yeezy` — produtos: 40; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque
- `jacquemus` — produtos: 38; issues: blocked_seo:Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar
- `aphase` — produtos: 38; issues: blocked_body:produtos em estoque; fit_term_body:rodar
- `fear-of-god` — produtos: 36; issues: blocked_seo:Entrega SP,Pronta entrega; blocked_body:produtos em estoque; fit_term_body:rodar

## P1/P2 — campos SEO ausentes ou incompletos

- `air-jordan-1-low` — produtos: 124; issues: seo_desc_missing; seo_title_missing
- `giftable` — produtos: 63; issues: seo_desc_missing; seo_title_missing
- `dia-das-maes-by-lala-noleto` — produtos: 16; issues: seo_desc_missing; seo_title_missing
- `curated-by-caio-bigodi` — produtos: 12; issues: seo_desc_missing; seo_title_missing
- `tenis-alo` — produtos: 12; issues: seo_desc_missing; seo_title_missing
- `by-tamara-rudge` — produtos: 9; issues: seo_desc_missing; seo_title_missing
- `onitsuka-tiger-x-versace` — produtos: 9; issues: blocked_body:produtos em estoque; seo_title_missing
  - SEO desc: Os melhores Onitsuka Tiger x Versace estão na LK Sneakers Jardins SP. 9+ opções originais com garantia de autenticidade e envio em até 2 dias.
- `herit` — produtos: 6; issues: seo_desc_missing; seo_title_missing
- `adidas-by-stella-mccartney` — produtos: 4; issues: seo_desc_missing; seo_title_missing
- `onitsuka-tiger-mexico-66-fringe` — produtos: 3; issues: seo_title_missing
  - SEO desc: Os melhores Onitsuka Tiger Mexico 66 Fringe estão na LK Sneakers Jardins SP. 3+ opções originais com garantia de autenticidade e envio em até 2 dias.
- `crocs-mcqueen` — produtos: 1; issues: seo_desc_missing; seo_title_missing
- `crocs-relampago-mcqueen` — produtos: 1; issues: seo_desc_missing; seo_title_missing
- `tom-sachs-x-nikecraft-general-purpose` — produtos: 1; issues: seo_desc_missing; seo_title_missing

## Outros pontos

### SEO description longa

- `alo-yoga-1` — produtos: 115; issues: blocked_body:produtos em estoque; fit_term_body:rodar; seo_desc_long
  - SEO desc: Alo Yoga original no Brasil. Leggings, tops, jaquetas e acessórios de athleisure premium. Usado por Kendall Jenner e Hailey Bieber. 10x sem juros, frete grátis acima de R$499.

## Recomendação de execução segura

1. **Não aplicar em massa direto.** São muitas coleções; risco de mexer em páginas que não têm demanda ou receita relevante.
2. **Criar lote P0 de hotfix meta** com 10–15 coleções de maior impacto: `lancamentos`, `nike-todos-os-modelos`, `adidas-todos-os-modelos`, `air-jordan-1`, `camiseta-1`, `athleisure`, `bone-streetwear`, `aime-leon-dore`, `new-balance-9060`, `yeezy`, `fear-of-god`, `jacquemus`, `nude-project`, `nike-air-force-1`, `nike-dunk-sb`.
3. **Criar patch de FAQ/template em dev theme** para substituir o bloco genérico de prazo em collections; isso corrige grande parte das 155 ocorrências sem editar cada coleção individualmente, mas precisa preview/rollback.
4. **Separar linguagem de tamanho**: trocar `roda grande/pequeno` por “forma”, “ajuste” ou “numeração” em lote editorial/dev, onde aplicável.
5. Priorizar com GSC/GA4/Shopify antes de produção em massa.

## Aprovação necessária para execução futura

- Alterar SEO title/meta/description de collections em produção: exige aprovação explícita por lote/handles.
- Alterar template/FAQ em production theme: exige dev preview primeiro + aprovação explícita para produção.
- Nenhuma alteração em produto, preço, estoque, GMC, campanhas, Klaviyo ou checkout deve entrar neste pacote.

## Cobertura dos 18 tópicos

- GA4: não usado; necessário para priorização comercial final.
- GSC: não usado; necessário para priorizar por impressões/CTR.
- GMC: não aplicável neste audit de copy/collection.
- Shopify SEO: verificado via Admin SEO fields e HTML público por spot-check.
- Shopify CRO/theme: identificado problema de FAQ/template; sem write.
- GEO/AI Search: risco identificado em snippets/metadados e FAQ citável.
- PageSpeed/CrUX/CWV: não aplicável a este audit.
- Schema: não auditado completo; spot-check focou meta/FAQ textual.
- Reviews: não aplicável.
- Paid media: não usado.
- Influencer/social demand: não usado.
- Concorrência/SERP: não usado.
- Google Business/local: não aplicável.
- Klaviyo/CRM: não usado.
- Catálogo/product data quality: não alterado.
- Conteúdo/taxonomia comercial: foco principal; há termos operacionais fora do guardrail.
- Mensuração/QA de eventos: não aplicável.
- Impact review/experimentation: futuro D+7 após qualquer lote aprovado.
