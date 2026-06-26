# Ahrefs Full Audit — LK Sneakers

- Generated UTC: 2026-06-18 20:27:43
- Project: **Lksneakers**
- Project ID: `9609836`
- Target: `lksneakers.com.br/`
- Crawl status/date: `Completed` / `2026-06-18T19:46:19Z`
- Health Score: **93**
- Total URLs/items reported: **34329**
- URLs with errors: **2241**
- URLs with warnings: **10047**
- URLs with notices: **10011**
- Fonte: Ahrefs Site Audit API v3 via Doppler; `values_printed=false`
- Escopo: read-only; writes externos = 0

## Veredito executivo

O site está com **Health Score 93**, então não é uma crise técnica ampla. Mas o crawl atual mostra blocos acionáveis que podem afetar UX, crawl budget e conversão: links internos para páginas quebradas, 404/4XX, imagens quebradas/pesadas, páginas órfãs/canonical sem links internos e higiene on-page.

## Distribuição de issues ativas

- **Error**: 7 tipos ativos; soma `crawled`=444
- **Warning**: 5 tipos ativos; soma `crawled`=8904
- **Notice**: 15 tipos ativos; soma `crawled`=14169

## Categorias com issues ativas

- **Other**: 4 issue types; soma `crawled`=13155
- **Links**: 3 issue types; soma `crawled`=8146
- **Content**: 12 issue types; soma `crawled`=1990
- **Images**: 4 issue types; soma `crawled`=167
- **Internal pages**: 2 issue types; soma `crawled`=38
- **External pages**: 2 issue types; soma `crawled`=21

## Prioridades recomendadas

### P0 — Links internos para páginas quebradas / 404 / 4XX
- Evidência: 3 issue types; soma `crawled`=7867
- Por quê: Corrige experiência ruim e reduz desperdício de crawl; melhor via map de origem→destino + redirects/remoção de links.
  - `c64dae3f-d0f4-11e7-8ed1-001e67ed4656` — 404 page | error | crawled=19 | new=19 | change=19
    - Exemplo: 404 https://lksneakers.com.br/collections/samba-duplicata-backup-20260616 | traffic=0.0 | origin=https://lksneakers.com.br/
    - Exemplo: 404 https://lksneakers.com.br/products/bone-nude-project-new-varsity-cinza | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil
    - Exemplo: 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-plum-vinho | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
  - `c64da643-d0f4-11e7-8ed1-001e67ed4656` — 4XX page | error | crawled=19 | new=19 | change=17
    - Exemplo: 404 https://lksneakers.com.br/collections/samba-duplicata-backup-20260616 | traffic=0.0 | origin=https://lksneakers.com.br/
    - Exemplo: 404 https://lksneakers.com.br/products/bone-nude-project-new-varsity-cinza | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil
    - Exemplo: 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-plum-vinho | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
  - `6193420a-00b1-11e8-930a-001e67ed4656` — Page has links to broken page | warning | crawled=7829 | new=7829 | change=7829
    - Exemplo: 200 https://lksneakers.com.br/collections/sneakers?filter.v.option.tamanho=42%2F3 | traffic=0.0 | origin=https://lksneakers.com.br/collections/sneakers
    - Exemplo: 200 https://lksneakers.com.br/collections/comme-des-garcons?filter.v.option.tamanho=37 | traffic=0.0 | origin=https://lksneakers.com.br/collections/comme-des-garcons
    - Exemplo: 200 https://lksneakers.com.br/collections/nike-todos-os-modelos?filter.v.option.tamanho=40%2F40.5 | traffic=0.0 | origin=https://lksneakers.com.br/collections/nike-todos-os-modelos

### P0 — Imagens quebradas
- Evidência: 2 issue types; soma `crawled`=60
- Por quê: Afeta vitrine visual e confiança premium; evidência aponta bug de URL Judge.me renderizada como objeto e imagens externas quebradas.
  - `34412dfa-feb0-11e8-a306-001e67ed4657` — Page has broken image | error | crawled=53 | new=53 | change=53
    - Exemplo: 200 https://lksneakers.com.br/collections/nike-mind-001 | traffic=115.0
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo | traffic=1.0
  - `c0e87084-feaf-11e8-8c05-001e67ed4657` — Image broken | error | crawled=7 | new=7 | change=7
    - Exemplo: 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/camiseta-jacquemus-the-typo-azul
    - Exemplo: 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/camiseta-jacquemus-the-typo-azul
    - Exemplo: 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/air-jordan-4-craft-medium-olive

### P1 — Páginas órfãs/canonical sem links internos
- Evidência: 2 issue types; soma `crawled`=317
- Por quê: Consolida sinais em páginas comerciais e melhora descoberta de PDP/collections.
  - `c64d7e96-d0f4-11e7-8ed1-001e67ed4656` — Orphan page (has no incoming internal links) | error | crawled=219 | new=219 | change=219
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-nike-air-jordan-1-low-se-repaired-denim-swoosh-azul | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/products/define-jacket-nulu-rose-gold | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-adidas-samba-og-off-white-core-black-branco | traffic=111.0
  - `c64d3d21-d0f4-11e7-8ed1-001e67ed4656` — Canonical URL has no incoming internal links | error | crawled=98 | new=98 | change=98
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-lucky-green-verde | traffic=3.0
    - Exemplo: 200 https://lksneakers.com.br/products/nike-dunk-low-coast-feminino | traffic=1.0
    - Exemplo: 200 https://lksneakers.com.br/products/nike-dunk-low-blue-paisley | traffic=1.0

### P1 — Peso de imagens/performance
- Evidência: 1 issue types; soma `crawled`=29
- Por quê: Melhora mobile, velocidade percebida e potencialmente conversão.
  - `c64d8113-d0f4-11e7-8ed1-001e67ed4656` — Image file size too large | error | crawled=29 | new=29 | change=29
    - Exemplo: 200 https://lksneakers.com.br/cdn/shop/files/5_6ca8290c-011d-4f84-84f9-f92f1e7bf76e.png | traffic=0.0 | origin=https://lksneakers.com.br/
    - Exemplo: 200 https://lksneakers.com.br/cdn/shop/files/23.png?v=1742844603&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/medicom-toy-bearbrick-jean-michel-basquiat-10-1000-toy-art-multi-color
    - Exemplo: 200 https://lksneakers.com.br/cdn/shop/files/regata-skims-cotton-cami-halite-rosa-lk-43774078391270-1737643.png?v=1756339100&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/regata-skims-cotton-cami-halite-rosa

### P2 — Metadata/conteúdo técnico
- Evidência: 11 issue types; soma `crawled`=1981
- Por quê: Higiene para CTR, snippets e legibilidade SEO/GEO.
  - `c64d56c9-d0f4-11e7-8ed1-001e67ed4656` — Meta description too long | warning | crawled=631 | new=631 | change=631
    - Exemplo: 200 https://lksneakers.com.br/collections/alo-yoga-1 | traffic=117.0
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco | traffic=2.0
    - Exemplo: 200 https://lksneakers.com.br/collections | traffic=0.0 | origin=https://lksneakers.com.br/
  - `c64dac3a-d0f4-11e7-8ed1-001e67ed4656` — Title too long | warning | crawled=353 | new=353 | change=353
    - Exemplo: 200 https://lksneakers.com.br/collections/roupas | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/products/chinelo-havaianas-x-dolce-gabanna-blue-mediterraneo-azul | traffic=2172.0
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-4-rm-x-nygel-sylvester-driveway-grey-cinza | traffic=0.0
  - `c64d5156-d0f4-11e7-8ed1-001e67ed4656` — Meta description too short | warning | crawled=13 | new=13 | change=13
    - Exemplo: 200 https://lksneakers.com.br/pages/lk-rewards | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho | traffic=2.0
    - Exemplo: 200 https://lksneakers.com.br/products/short-alo-yoga-match-point | traffic=0.0
  - `d69246c2-225a-11ec-8456-06d2f2f613d8` — Page and SERP titles do not match | notice | crawled=530 | new=529 | change=530
    - Exemplo: 200 https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos | traffic=1955.0
    - Exemplo: 200 https://lksneakers.com.br/collections/lululemon | traffic=1171.0
    - Exemplo: 200 https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66 | traffic=1145.0
  - `6a46d032-001c-11e8-99f1-001e67ed4656` — Title too long | notice | crawled=269 | new=269 | change=269
    - Exemplo: 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=35 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
    - Exemplo: 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=36 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
    - Exemplo: 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=43 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
  - `02085644-001c-11e8-8e51-001e67ed4656` — Meta description too long | notice | crawled=154 | new=154 | change=154
    - Exemplo: 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=46 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
    - Exemplo: 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=39 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
    - Exemplo: 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=M | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
  - `8d785026-001c-11e8-aa34-001e67ed4656` — Meta description too short | notice | crawled=14 | new=14 | change=14
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho?_pos=12&_fid=c26a1f4de&_ss=c | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.p.vendor=Jordan
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho?_pos=9&_fid=a3bf86fb6&_ss=c&variant=45808978591966 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=43
    - Exemplo: 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-elephant-brown-marrom?_pos=15&_fid=91bd336b9&_ss=c&variant=44801564279006 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=40.5
  - `c64d52ef-d0f4-11e7-8ed1-001e67ed4656` — Multiple H1 tags | notice | crawled=14 | new=14 | change=14
    - Exemplo: 200 https://lksneakers.com.br/pages/sobre-a-lk-sneakers-e-apparels | traffic=2.0
    - Exemplo: 200 https://lksneakers.com.br/pages/autenticidade | traffic=0.0
    - Exemplo: 200 https://lksneakers.com.br/blogs/novidades/lancamentos-sneakers-2026 | traffic=0.0

### P2 — Externos/redirects/HTTP
- Evidência: 2 issue types; soma `crawled`=21
- Por quê: Limpeza técnica e redução de sinais ruins para crawler/usuário.
  - `c64d89a6-d0f4-11e7-8ed1-001e67ed4656` — External 4XX | notice | crawled=15 | new=15 | change=15
    - Exemplo: 403 https://stockx.com/ | origin=https://lksneakers.com.br/blogs/novidades/como-saber-se-tenis-nike-e-original
    - Exemplo: 403 https://hypebeast.com/search?s=salomon%20xt-6 | origin=https://lksneakers.com.br/pages/guia-salomon-xt-6
    - Exemplo: 403 https://about.nike.com/ | origin=https://lksneakers.com.br/blogs/novidades/como-saber-se-tenis-nike-e-original
  - `c64d8847-d0f4-11e7-8ed1-001e67ed4656` — External 3XX redirect | notice | crawled=6 | new=6 | change=6
    - Exemplo: 302 https://rastreamento.correios.com.br/ | origin=https://lksneakers.com.br/pages/politica-de-frete
    - Exemplo: 307 https://www.salomon.com/ | origin=https://lksneakers.com.br/pages/guia-salomon-xt-6
    - Exemplo: 301 https://www.voguehk.com/en/article/runway/onitsuka-tiger-fall-2026 | origin=https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66

## Top issues ativas por severidade/volume

- `c64d7e96-d0f4-11e7-8ed1-001e67ed4656` — **Orphan page (has no incoming internal links)** | error | category=Links | crawled=219 | new=219 | change=219
- `c64d3d21-d0f4-11e7-8ed1-001e67ed4656` — **Canonical URL has no incoming internal links** | error | category=Links | crawled=98 | new=98 | change=98
- `34412dfa-feb0-11e8-a306-001e67ed4657` — **Page has broken image** | error | category=Images | crawled=53 | new=53 | change=53
- `c64d8113-d0f4-11e7-8ed1-001e67ed4656` — **Image file size too large** | error | category=Images | crawled=29 | new=29 | change=29
- `c64dae3f-d0f4-11e7-8ed1-001e67ed4656` — **404 page** | error | category=Internal pages | crawled=19 | new=19 | change=19
- `c64da643-d0f4-11e7-8ed1-001e67ed4656` — **4XX page** | error | category=Internal pages | crawled=19 | new=19 | change=17
- `c0e87084-feaf-11e8-8c05-001e67ed4657` — **Image broken** | error | category=Images | crawled=7 | new=7 | change=7
- `6193420a-00b1-11e8-930a-001e67ed4656` — **Page has links to broken page** | warning | category=Links | crawled=7829 | new=7829 | change=7829
- `c64d56c9-d0f4-11e7-8ed1-001e67ed4656` — **Meta description too long** | warning | category=Content | crawled=631 | new=631 | change=631
- `c64dac3a-d0f4-11e7-8ed1-001e67ed4656` — **Title too long** | warning | category=Content | crawled=353 | new=353 | change=353
- `c64d9be3-d0f4-11e7-8ed1-001e67ed4656` — **Missing alt text** | warning | category=Images | crawled=78 | new=78 | change=78
- `c64d5156-d0f4-11e7-8ed1-001e67ed4656` — **Meta description too short** | warning | category=Content | crawled=13 | new=13 | change=13
- `c22e9647-5a8f-4352-8b38-14cb66d7f101` — **Structured data has schema.org validation error** | notice | category=Other | crawled=10003 | new=10002 | change=10003
- `b23ae498-5dee-4626-930b-9d5facd8a17d` — **Pages to submit to IndexNow** | notice | category=Other | crawled=2175 | new=0 | change=2174
- `c64d8a57-d0f4-11e7-8ed1-001e67ed4656` — **More than three parameters in URL** | notice | category=Other | crawled=976 | new=976 | change=976
- `d69246c2-225a-11ec-8456-06d2f2f613d8` — **Page and SERP titles do not match** | notice | category=Content | crawled=530 | new=529 | change=530
- `6a46d032-001c-11e8-99f1-001e67ed4656` — **Title too long** | notice | category=Content | crawled=269 | new=269 | change=269
- `02085644-001c-11e8-8e51-001e67ed4656` — **Meta description too long** | notice | category=Content | crawled=154 | new=154 | change=154
- `c64d89a6-d0f4-11e7-8ed1-001e67ed4656` — **External 4XX** | notice | category=External pages | crawled=15 | new=15 | change=15
- `8d785026-001c-11e8-aa34-001e67ed4656` — **Meta description too short** | notice | category=Content | crawled=14 | new=14 | change=14
- `c64d52ef-d0f4-11e7-8ed1-001e67ed4656` — **Multiple H1 tags** | notice | category=Content | crawled=14 | new=14 | change=14
- `6048d416-8373-4ba2-bbac-3472997590fb` — **Pages have high AI content levels** | notice | category=Content | crawled=9 | new=0 | change=9
- `c64d8847-d0f4-11e7-8ed1-001e67ed4656` — **External 3XX redirect** | notice | category=External pages | crawled=6 | new=6 | change=6
- `b366c49a-f514-45e5-9d9a-66cfff18f68b` — **Robots.txt rules disallow to crawl** | notice | category=Other | crawled=1 | new=1 | change=1
- `9cb115e3-7380-4f73-9ec0-7628c3393bdd` — **H1 tag changed** | notice | category=Content | crawled=1 | new=0 | change=1
- `7bbfc9eb-ed59-4bba-970d-fd98cc2ac0fe` — **Meta description changed** | notice | category=Content | crawled=1 | new=0 | change=1
- `3f369e7f-85fc-48fc-84b7-9cf28faafffc` — **Title tag changed** | notice | category=Content | crawled=1 | new=0 | change=1

## Amostras principais

### Orphan page (has no incoming internal links)
- `c64d7e96-d0f4-11e7-8ed1-001e67ed4656` | error | category=Links | crawled=219 | sample_api=100
- 200 https://lksneakers.com.br/products/tenis-nike-air-jordan-1-low-se-repaired-denim-swoosh-azul | traffic=0.0
- 200 https://lksneakers.com.br/products/define-jacket-nulu-rose-gold | traffic=0.0
- 200 https://lksneakers.com.br/products/tenis-adidas-samba-og-off-white-core-black-branco | traffic=111.0
- 200 https://lksneakers.com.br/products/nike-dunk-low-pink-foam-black | traffic=1.0
- 200 https://lksneakers.com.br/products/tenis-new-balance-abzorb-2000-black-preto | traffic=0.0

### Canonical URL has no incoming internal links
- `c64d3d21-d0f4-11e7-8ed1-001e67ed4656` | error | category=Links | crawled=98 | sample_api=98
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-lucky-green-verde | traffic=3.0
- 200 https://lksneakers.com.br/products/nike-dunk-low-coast-feminino | traffic=1.0
- 200 https://lksneakers.com.br/products/nike-dunk-low-blue-paisley | traffic=1.0
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-se-craft-inside-out-white-phantom-bege | traffic=0.0
- 200 https://lksneakers.com.br/products/air-jordan-1-elevate-low-se-silver-toe | traffic=5.0

### Page has broken image
- `34412dfa-feb0-11e8-a306-001e67ed4657` | error | category=Images | crawled=53 | sample_api=53
- 200 https://lksneakers.com.br/collections/nike-mind-001 | traffic=115.0
- 200 https://lksneakers.com.br/products/tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho | traffic=0.0
- 200 https://lksneakers.com.br/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo | traffic=1.0
- 200 https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown | traffic=0.0
- 200 https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-white | traffic=0.0

### Image file size too large
- `c64d8113-d0f4-11e7-8ed1-001e67ed4656` | error | category=Images | crawled=29 | sample_api=29
- 200 https://lksneakers.com.br/cdn/shop/files/5_6ca8290c-011d-4f84-84f9-f92f1e7bf76e.png | traffic=0.0 | origin=https://lksneakers.com.br/
- 200 https://lksneakers.com.br/cdn/shop/files/23.png?v=1742844603&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/medicom-toy-bearbrick-jean-michel-basquiat-10-1000-toy-art-multi-color
- 200 https://lksneakers.com.br/cdn/shop/files/regata-skims-cotton-cami-halite-rosa-lk-43774078391270-1737643.png?v=1756339100&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/regata-skims-cotton-cami-halite-rosa
- 200 https://lksneakers.com.br/cdn/shop/files/bolsa-lululemon-mini-tote-bag-two-tone-canvas-45l-bege-lk-11680405-560340.png?v=1749167866&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/bolsa-lululemon-mini-tote-bag-two-tone-canvas-4-5l-bege
- 200 https://lksneakers.com.br/cdn/shop/files/camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul-lk-9869374.png?v=1773935411&width=900 | traffic=0.0 | origin=https://lksneakers.com.br/products/camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul

### 404 page
- `c64dae3f-d0f4-11e7-8ed1-001e67ed4656` | error | category=Internal pages | crawled=19 | sample_api=19
- 404 https://lksneakers.com.br/collections/samba-duplicata-backup-20260616 | traffic=0.0 | origin=https://lksneakers.com.br/
- 404 https://lksneakers.com.br/products/bone-nude-project-new-varsity-cinza | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil
- 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-plum-vinho | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
- 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-sycamore-verde | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
- 404 https://lksneakers.com.br/products/bone-nude-project-classique-preto | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil

### 4XX page
- `c64da643-d0f4-11e7-8ed1-001e67ed4656` | error | category=Internal pages | crawled=19 | sample_api=19
- 404 https://lksneakers.com.br/collections/samba-duplicata-backup-20260616 | traffic=0.0 | origin=https://lksneakers.com.br/
- 404 https://lksneakers.com.br/products/bone-nude-project-new-varsity-cinza | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil
- 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-plum-vinho | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
- 404 https://lksneakers.com.br/products/camiseta-essentials-fear-of-god-sycamore-verde | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/fear-of-god-essentials-guia-tamanhos-pecas
- 404 https://lksneakers.com.br/products/bone-nude-project-classique-preto | traffic=0.0 | origin=https://lksneakers.com.br/blogs/novidades/nude-project-marca-espanhola-guia-completo-brasil

### Image broken
- `c0e87084-feaf-11e8-8c05-001e67ed4657` | error | category=Images | crawled=7 | sample_api=7
- 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1779883207__cudipa-_0293__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/camiseta-jacquemus-the-typo-azul
- 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1779883216___uxsng-_0294__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/camiseta-jacquemus-the-typo-azul
- 404 https://lksneakers.com.br/products/{"original"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=1024",%20"small"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=160",%20"compact"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=160",%20"huge"=>"https://judgeme.imgix.net/lk/1773093765__1773093754940-51a9ac25-48de-4cbd-b842-34__original.jpeg?auto=format&w=1024"} | traffic=0.0 | origin=https://lksneakers.com.br/products/air-jordan-4-craft-medium-olive
- 403 https://media.about.nike.com/image-downloads/083a9bb0-c8dd-48f5-b8c5-bce81839b3b0/nike-mind-7.jpg | origin=https://lksneakers.com.br/pages/guia-nike-mind-001-002
- 429 https://sneakerbardetroit.com/wp-content/uploads/2026/03/Virgil-Abloh-Archive-Air-Jordan-1-High-OG-Alaska-AA3834-100-1.jpg | origin=https://lksneakers.com.br/blogs/novidades/jordan-1-alaska-v-a-a-o-tenis-que-dominou-a-semana-e-esgotou-em-minutos

### Page has links to broken page
- `6193420a-00b1-11e8-930a-001e67ed4656` | warning | category=Links | crawled=7829 | sample_api=100
- 200 https://lksneakers.com.br/collections/sneakers?filter.v.option.tamanho=42%2F3 | traffic=0.0 | origin=https://lksneakers.com.br/collections/sneakers
- 200 https://lksneakers.com.br/collections/comme-des-garcons?filter.v.option.tamanho=37 | traffic=0.0 | origin=https://lksneakers.com.br/collections/comme-des-garcons
- 200 https://lksneakers.com.br/collections/nike-todos-os-modelos?filter.v.option.tamanho=40%2F40.5 | traffic=0.0 | origin=https://lksneakers.com.br/collections/nike-todos-os-modelos
- 200 https://lksneakers.com.br/collections/lululemon?filter.v.option.tamanho=43 | traffic=0.0 | origin=https://lksneakers.com.br/collections/lululemon
- 200 https://lksneakers.com.br/collections/maison-mihara-todos-os-modelos?filter.v.option.tamanho=37 | traffic=0.0 | origin=https://lksneakers.com.br/collections/maison-mihara-todos-os-modelos

### Meta description too long
- `c64d56c9-d0f4-11e7-8ed1-001e67ed4656` | warning | category=Content | crawled=631 | sample_api=100
- 200 https://lksneakers.com.br/collections/alo-yoga-1 | traffic=117.0
- 200 https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco | traffic=2.0
- 200 https://lksneakers.com.br/collections | traffic=0.0 | origin=https://lksneakers.com.br/
- 200 https://lksneakers.com.br/products/tenis-adidas-taekwondo-mei-ballet-preto | traffic=0.0
- 200 https://lksneakers.com.br/products/define-jacket-nulu-rose-gold | traffic=0.0

### Title too long
- `c64dac3a-d0f4-11e7-8ed1-001e67ed4656` | warning | category=Content | crawled=353 | sample_api=100
- 200 https://lksneakers.com.br/collections/roupas | traffic=0.0
- 200 https://lksneakers.com.br/products/chinelo-havaianas-x-dolce-gabanna-blue-mediterraneo-azul | traffic=2172.0
- 200 https://lksneakers.com.br/products/tenis-air-jordan-4-rm-x-nygel-sylvester-driveway-grey-cinza | traffic=0.0
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny | traffic=359.0
- 200 https://lksneakers.com.br/products/tenis-tom-sachs-x-nikecraft-general-purpose-summit-white-branco | traffic=0.0

### Missing alt text
- `c64d9be3-d0f4-11e7-8ed1-001e67ed4656` | warning | category=Images | crawled=78 | sample_api=78
- 200 https://lksneakers.com.br/collections/lululemon | traffic=1171.0
- 200 https://lksneakers.com.br/collections/athleisure | traffic=0.0
- 200 https://lksneakers.com.br/products/short-lululemon-align%E2%84%A2-high-rise-6 | traffic=1.0
- 200 https://lksneakers.com.br/collections/roupas?page=2 | traffic=0.0 | origin=https://lksneakers.com.br/collections/roupas
- 200 https://lksneakers.com.br/products/calca-lululemon-smoothcover-high-rise-tight-25 | traffic=0.0

### Meta description too short
- `c64d5156-d0f4-11e7-8ed1-001e67ed4656` | warning | category=Content | crawled=13 | sample_api=13
- 200 https://lksneakers.com.br/pages/lk-rewards | traffic=0.0
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho | traffic=2.0
- 200 https://lksneakers.com.br/products/short-alo-yoga-match-point | traffic=0.0
- 200 https://lksneakers.com.br/products/camiseta-nude-project-global-soon | traffic=0.0
- 200 https://lksneakers.com.br/products/nike-dunk-low-prm-vintage-team-red | traffic=0.0

### Structured data has schema.org validation error
- `c22e9647-5a8f-4352-8b38-14cb66d7f101` | notice | category=Other | crawled=10003 | sample_api=100
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos | traffic=1955.0
- 200 https://lksneakers.com.br/collections/lululemon | traffic=1171.0
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66 | traffic=1145.0
- 200 https://lksneakers.com.br/collections/nike-dunk | traffic=537.0
- 200 https://lksneakers.com.br/collections/adidas-samba-jane | traffic=547.0

### Pages to submit to IndexNow
- `b23ae498-5dee-4626-930b-9d5facd8a17d` | notice | category=Other | crawled=2175 | sample_api=100
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos | traffic=1955.0
- 200 https://lksneakers.com.br/collections/lululemon | traffic=1171.0
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66 | traffic=1145.0
- 200 https://lksneakers.com.br/collections/nike-dunk | traffic=537.0
- 200 https://lksneakers.com.br/collections/adidas-samba-jane | traffic=547.0

### More than three parameters in URL
- `c64d8a57-d0f4-11e7-8ed1-001e67ed4656` | notice | category=Other | crawled=976 | sample_api=100
- 200 https://lksneakers.com.br/products/nike-sb-dunk-low-club-58-gulf?_pos=21&_fid=704ec63ed&_ss=c&variant=44265067577566 | traffic=0.0 | origin=https://lksneakers.com.br/collections/nike-dunk?filter.v.option.tamanho=44
- 200 https://lksneakers.com.br/products/tightbooth-x-nike-sb-dunk-low-pro-black-white?_pos=12&_fid=bf195134b&_ss=c&variant=44656977936606 | traffic=0.0 | origin=https://lksneakers.com.br/collections/nike-dunk?filter.v.option.tamanho=42.5
- 200 https://lksneakers.com.br/products/travis-scott-x-air-jordan-1-low-og-sp-black-phantom?_pos=16&_fid=a3bf86fb6&_ss=c&variant=46832884351198 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=44
- 200 https://lksneakers.com.br/products/tenis-nike-air-force-1-low-valentines-day-2025?_pos=7&_fid=37edca914&_ss=c&variant=46236612264158 | traffic=0.0 | origin=https://lksneakers.com.br/collections/nike-air-force-1?filter.v.option.tamanho=38
- 200 https://lksneakers.com.br/products/travis-scott-x-air-jordan-1-low-og-sp-black-phantom?_pos=19&_fid=a3bf86fb6&_ss=c&variant=46832884285662 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=41

### Page and SERP titles do not match
- `d69246c2-225a-11ec-8456-06d2f2f613d8` | notice | category=Content | crawled=530 | sample_api=100
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos | traffic=1955.0
- 200 https://lksneakers.com.br/collections/lululemon | traffic=1171.0
- 200 https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66 | traffic=1145.0
- 200 https://lksneakers.com.br/collections/nike-dunk | traffic=537.0
- 200 https://lksneakers.com.br/collections/adidas-samba-jane | traffic=547.0

### Title too long
- `6a46d032-001c-11e8-99f1-001e67ed4656` | notice | category=Content | crawled=269 | sample_api=100
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=35 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=36 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.option.tamanho=43 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F1 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny
- 200 https://lksneakers.com.br/collections/adidas-x-bad-bunny?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F14 | traffic=0.0 | origin=https://lksneakers.com.br/collections/adidas-x-bad-bunny

### Meta description too long
- `02085644-001c-11e8-8e51-001e67ed4656` | notice | category=Content | crawled=154 | sample_api=100
- 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=46 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
- 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=39 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
- 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=M | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
- 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.option.tamanho=35 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1
- 200 https://lksneakers.com.br/collections/alo-yoga-1?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F3 | traffic=0.0 | origin=https://lksneakers.com.br/collections/alo-yoga-1

### External 4XX
- `c64d89a6-d0f4-11e7-8ed1-001e67ed4656` | notice | category=External pages | crawled=15 | sample_api=15
- 403 https://stockx.com/ | origin=https://lksneakers.com.br/blogs/novidades/como-saber-se-tenis-nike-e-original
- 403 https://hypebeast.com/search?s=salomon%20xt-6 | origin=https://lksneakers.com.br/pages/guia-salomon-xt-6
- 403 https://about.nike.com/ | origin=https://lksneakers.com.br/blogs/novidades/como-saber-se-tenis-nike-e-original
- 403 https://hypebae.com/2025/9/nike-jacquemus-moon-shoe-collaboration-release-date | origin=https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk
- 403 https://about.nike.com/en/newsroom/reports/fy23-nike-inc-impact-report | origin=https://lksneakers.com.br/blogs/novidades/como-saber-se-tenis-nike-e-original

### Meta description too short
- `8d785026-001c-11e8-aa34-001e67ed4656` | notice | category=Content | crawled=14 | sample_api=14
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho?_pos=12&_fid=c26a1f4de&_ss=c | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.p.vendor=Jordan
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho?_pos=9&_fid=a3bf86fb6&_ss=c&variant=45808978591966 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=43
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-elephant-brown-marrom?_pos=15&_fid=91bd336b9&_ss=c&variant=44801564279006 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=40.5
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-elephant-brown-marrom?_pos=3&_fid=91bd336b4&_ss=c&variant=44801564410078 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=43.5
- 200 https://lksneakers.com.br/products/tenis-air-jordan-1-low-eastside-golf-azul-marinho?_pos=9&_fid=a3bf86fb5&_ss=c&variant=45065945809118 | traffic=0.0 | origin=https://lksneakers.com.br/collections/air-jordan-1?filter.v.option.tamanho=39

### Multiple H1 tags
- `c64d52ef-d0f4-11e7-8ed1-001e67ed4656` | notice | category=Content | crawled=14 | sample_api=14
- 200 https://lksneakers.com.br/pages/sobre-a-lk-sneakers-e-apparels | traffic=2.0
- 200 https://lksneakers.com.br/pages/autenticidade | traffic=0.0
- 200 https://lksneakers.com.br/blogs/novidades/lancamentos-sneakers-2026 | traffic=0.0
- 200 https://lksneakers.com.br/blogs/novidades/streetwear-masculino-sao-paulo | traffic=0.0
- 200 https://lksneakers.com.br/pages/guia-adidas-samba | traffic=0.0

### Pages have high AI content levels
- `6048d416-8373-4ba2-bbac-3472997590fb` | notice | category=Content | crawled=9 | sample_api=9
- 200 https://lksneakers.com.br/pages/guia-de-tamanhos | traffic=102.0
- 200 https://lksneakers.com.br/pages/new-balance-530-vs-2002r | traffic=0.0
- 200 https://lksneakers.com.br/pages/politica-de-privacidade | traffic=0.0
- 200 https://lksneakers.com.br/pages/adidas-samba-vs-campus-00s | traffic=0.0
- 200 https://lksneakers.com.br/pages/crocs-relampago-mcqueen-guia | traffic=385.0

### External 3XX redirect
- `c64d8847-d0f4-11e7-8ed1-001e67ed4656` | notice | category=External pages | crawled=6 | sample_api=6
- 302 https://rastreamento.correios.com.br/ | origin=https://lksneakers.com.br/pages/politica-de-frete
- 307 https://www.salomon.com/ | origin=https://lksneakers.com.br/pages/guia-salomon-xt-6
- 301 https://www.voguehk.com/en/article/runway/onitsuka-tiger-fall-2026 | origin=https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66
- 301 https://www.stockx.com/ | origin=https://lksneakers.com.br/blogs/novidades/feid-x-salomon-xt-4-og-ferxxocalipsis-o-drop-latino-que-mudou-o-jogo-em-2026
- 301 https://www.npd.com/ | origin=https://lksneakers.com.br/blogs/novidades/feid-x-salomon-xt-4-og-ferxxocalipsis-o-drop-latino-que-mudou-o-jogo-em-2026

### Robots.txt rules disallow to crawl
- `b366c49a-f514-45e5-9d9a-66cfff18f68b` | notice | category=Other | crawled=1 | sample_api=1
- 200 https://account.lksneakers.com.br/robots.txt | traffic=0.0

### H1 tag changed
- `9cb115e3-7380-4f73-9ec0-7628c3393bdd` | notice | category=Content | crawled=1 | sample_api=1
- 200 https://lksneakers.com.br/ | traffic=393.0

### Meta description changed
- `7bbfc9eb-ed59-4bba-970d-fd98cc2ac0fe` | notice | category=Content | crawled=1 | sample_api=1
- 200 https://lksneakers.com.br/ | traffic=393.0

### Title tag changed
- `3f369e7f-85fc-48fc-84b7-9cf28faafffc` | notice | category=Content | crawled=1 | sample_api=1
- 200 https://lksneakers.com.br/ | traffic=393.0

## Plano de ação seguro

### Sem aprovação
- Agrupar os CSVs por origem/template: collection, PDP, blog, menu, app Judge.me.
- Preparar proposta de redirects e remoção de links em dev theme.
- Validar se links quebrados vêm de menu, metafield, descrição de produto, snippet de app ou collection filter.

### Com aprovação explícita
- Aplicar redirects Shopify production.
- Alterar tema/snippets/apps em produção.
- Alterar conteúdo visível, titles/metas, links de PDP/collections ou feed/GMC.

### Rollback
- Redirects: export antes/depois + remoção em lote.
- Theme: dev theme primeiro; rollback por theme duplicado/versão anterior.
- Conteúdo/meta: snapshot antes/depois e revisão de impacto em ~7 dias.

## Arquivos salvos
- Pasta: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-full-audit/20260618T202702Z`
- `REPORT.md`
- `issues-summary.csv`
- `issues-normalized.json`
- `selected-page-explorer-details.json`
- `page-explorer-*.csv/json`
- `api-log.json` com status HTTP sem token
