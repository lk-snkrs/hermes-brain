# LK Growth — D+7 PDP CRO/SEO — 2026-06-25

## Veredito

Review 100% read-only. O sinal é **misto/inconclusivo para causalidade**: o bloco CRO publicado está tecnicamente presente, mas a janela pós ainda é curta e vários PDPs têm baixo volume. O QA também encontrou drift em parte dos SEO metafields vs receipt de 2026-06-18 e presença pública de `sob encomenda` nos 9 PDPs SEO-only; isso pede triagem/packet, não correção automática.

## Fontes e janelas

- Baseline: `2026-06-12..2026-06-17`; Pós: `2026-06-19..2026-06-24`; dia de rollout `2026-06-18` excluído.

- GA4: ok=True property_hash=e418eaa944 status baseline/post=200/200.

- GSC: ok=True site=sc-domain:lksneakers.com.br rows baseline/post=168/156.

- Shopify Admin/products: ok=True produtos lidos=17/17; Orders fetched=155.

- Chat: indisponível nesta execução; não usado para verdict. Estoque/Tiny não consultado. values_printed=false.


## Resumo por bucket

| Bucket | PDPs | GA4 views base→pós | ATC rate base→pós | Receita Shopify base→pós | GSC clicks base→pós | GSC impr. base→pós |
|---|---:|---:|---:|---:|---:|---:|
| CRO primeiros 5 | 5 | 797→1001 (+25,6%) | 0,63%→0,90% | R$ 0,00→R$ 1.869,99 (n/a) | 0→0 (n/a) | 0→0 (n/a) |
| CRO rodada 2 | 3 | 769→728 (-5,3%) | 1,17%→0,41% | R$ 0,00→R$ 0,00 (n/a) | 0→0 (n/a) | 0→0 (n/a) |
| SEO-only | 9 | 465→509 (+9,5%) | 0,43%→0,20% | R$ 0,00→R$ 0,00 (n/a) | 2→5 (+150,0%) | 663→824 (+24,3%) |

## QA publicado

- Público HTTP 200: 17/17.

- CRO markers no Admin para 8 PDPs: 8/8 com todos os blocos esperados.

- SEO metafields esperados do receipt 2026-06-18: 4/9 batendo exatamente no Admin; 5/9 estão diferentes no readback atual, provável drift por rodada posterior ou truncamento/normalização de snippet. Não corrigi.

- Termo público `sob encomenda` detectado nos 9 PDPs SEO-only. Nos 8 PDPs CRO alterados, o check público não marcou esse termo. Próximo passo seguro: packet de limpeza editorial/metafield para esses 9, sem tocar estoque/preço/tema.


## Linhas por PDP

| Bucket | Handle | GA4 view_item Δ | ATC rate base→pós | Receita base→pós | GSC clicks Δ | GSC impr. Δ | CTR base→pós | Posição base→pós |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| CRO primeiros 5 | `nike-moon-shoe-sp-jacquemus-alabaster-amarelo` | +42,0% | 0,00%→0,34% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| CRO primeiros 5 | `tenis-adidas-samba-og-crochet-pack-sand-strata-bege` | -19,1% | 1,23%→1,91% | R$ 0,00→R$ 1.869,99 | n/a | n/a | n/a→n/a | n/a→n/a |
| CRO rodada 2 | `tenis-adidas-samba-og-white-floral-embroidery-branco` | +21,0% | 0,00%→0,34% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| CRO primeiros 5 | `tenis-new-balance-1906l-khaki-bege` | +106,3% | 0,00%→1,23% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| SEO-only | `tenis-new-balance-gator-run-timberwolf-bege` | -43,9% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | -60,0% | 0,00%→0,00% | 5.0→6.0 |
| SEO-only | `tenis-nike-vomero-premium-particle-rose-burgundy-rosa` | +2,8% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | -56,0% | 0,00%→0,00% | 6.7835820895522385→5.932203389830509 |
| CRO rodada 2 | `tenis-nike-vomero-premium-sail-coconut-milk-branco` | -25,1% | 1,06%→0,71% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| SEO-only | `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` | +19,3% | 1,20%→0,00% | R$ 0,00→R$ 0,00 | n/a | +47,1% | 0,00%→2,00% | 3.2058823529411766→5.5 |
| SEO-only | `tenis-nike-vomero-premium-volt-tint-sapphire-verde` | +0,0% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | +100,0% | +80,9% | 0,34%→0,38% | 6.310580204778157→9.511320754716982 |
| SEO-only | `tenis-nike-vomero-premium-white-lapis-total-orange-off-white` | +13,6% | 1,69%→1,49% | R$ 0,00→R$ 0,00 | n/a | -26,9% | 0,00%→0,00% | 4.038461538461538→2.6315789473684212 |
| SEO-only | `tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja` | +134,6% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | +0,0% | -11,2% | 0,66%→0,74% | 3.8289473684210527→4.948148148148148 |
| SEO-only | `tenis-nike-x-tom-sachs-mars-yard-3-0-bege` | -25,0% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | +110,0% | 0,00%→4,76% | 6.8→3.619047619047619 |
| CRO rodada 2 | `tenis-onitsuka-tiger-mexico-66-paraty-birch-cream-bege` | +2,0% | 3,38%→0,00% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| CRO primeiros 5 | `tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege` | +48,6% | 0,00%→0,37% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| CRO primeiros 5 | `tenis-onitsuka-tiger-mexico-66-sabot-crystal-pink-cream-rosa` | +150,0% | 25,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | n/a | n/a→n/a | n/a→n/a |
| SEO-only | `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom` | +22,2% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | n/a | 0,00%→0,00% | n/a→n/a |
| SEO-only | `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green` | +12,5% | 0,00%→0,00% | R$ 0,00→R$ 0,00 | n/a | -11,1% | 0,00%→0,00% | 2.5555555555555554→2.625 |

## Próximos approvals recomendados

- Sem rollback automático: não há evidência suficiente para reverter o CRO. Há, porém, QA negativo nos SEO-only: drift em 5/9 SEO metafields vs receipt e termo `sob encomenda` público em 9/9; tratar como novo packet de limpeza/normalização, não execução direta.

- Medir D+14 com janela cheia e checar queries/PDPs que tiveram impressões sem CTR.

- Preparar approval packet apenas para ajustes incrementais em PDPs com views/impressões relevantes e ATC/CTR abaixo da baseline; qualquer novo write Shopify/tema/GMC/Klaviyo/ads exige aprovação atual.


## Non-actions

- external_writes=0; Shopify/GMC/GA4/GSC/theme/Klaviyo/ads writes=0; estoque/Tiny=0; secrets values printed=0.
