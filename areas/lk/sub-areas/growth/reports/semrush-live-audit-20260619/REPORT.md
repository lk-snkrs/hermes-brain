# LK Growth — SEMrush live audit cross-check

- Data UTC: `2026-06-19`
- Escopo: SEMrush API + validação pública read-only; writes externos = 0; estoque consultado = false; values_printed=false
- Fonte SEMrush: `management/v1/projects`, `siteaudit/info`, `snapshots`, `snapshot`, `meta/issues`, `issue/{id}`
- Raw: `semrush-api-with-details.json`; validação pública: `public-validation.json`

## Veredito executivo

- Existem **2 projetos SEMrush** para `lksneakers.com.br`; isso está gerando ruído de leitura.
- Projeto **16150947** é o mais recente: último audit `2026-06-19 03:31 UTC`, score **92**, **0 errors**, 300 warnings, 75 notices. Este deve ser tratado como snapshot primário agora.
- Projeto **29110159** está mais antigo: último audit `2026-06-15 01:09 UTC`, score **85**, 175 errors. Ele ainda mostra `Invalid robots.txt format` e `Structured data markup errors`, mas esses cards não aparecem no snapshot mais recente do outro projeto.
- Coisas novas/reais que o Ahrefs não estava priorizando: **broken external image em artigo**, **llms.txt formatting issue**, **baixa linkagem interna de artigos**, **títulos longos de blog**, **H1/title duplicado em guias** e **links sem texto âncora no menu/home**.
- Falsos positivos/baixo controle: `wa.me` aparece como 429 para SEMrush, mas validação pública com UA normal retornou 200; `checkouts/internal/preloads.js` é recurso interno Shopify bloqueado por design.

## Projeto SEMrush `16150947` — lksneakers.com.br

- Último audit: `2026-06-19 03:31 UTC`
- Status: `FINISHED`; páginas crawled: `99/100`; score: `92`
- Totais info: errors `0`, warnings `300`, notices `75`; broken `0`, blocked `0`, redirected `1`, healthy `8`, haveIssues `90`

### errors

- Nenhum item com count > 0.

### warnings

- `12` — **Broken external links**: count `94`, delta `0`, checks `221`
  - sample: source=https://lksneakers.com.br/products/supreme-x-nike-air-force-1-low-box-logo-white; target=https://wa.me/5511949565000; info=429
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-teddy-bear-pink; target=https://wa.me/5511949565000; info=429
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-rose-whisper; target=https://wa.me/5511949565000; info=429
- `14` — **Broken external images**: count `1`, delta `0`, checks `26`
  - sample: source=https://lksneakers.com.br/blogs/novidades/jordan-1-alaska-v-a-a-o-tenis-que-dominou-a-semana-e-esgotou-em-minutos; target=https://sneakerbardetroit.com/wp-content/uploads/2026/03/Virgil-Abloh-Archive-Air-Jordan-1-High-OG-Alaska-AA3834-100-1.jpg; info=404
- `102` — **Title element is too long**: count `23`, delta `0`, checks `89`
  - sample: source=https://lksneakers.com.br/blogs/novidades/versace-onitsuka-tiger-tai-chi-sakura-collab; info=Versace x Onitsuka Tiger TAI-CHI Sakura: a collab luxo que une sneaker | LK Sneakers
  - sample: source=https://lksneakers.com.br/blogs/novidades/travis-scott-nike-collabs-guia-comprar-brasil; info=Travis Scott x Nike: Todas as Collabs e Onde Comprar no Brasil | LK Sneakers
  - sample: source=https://lksneakers.com.br/blogs/novidades/puma-speedcat-ballet-a-tendencia-sneakerina-que-vai-dominar-2026; info=Puma Speedcat Ballet: A Tendência 'Sneakerina' com 21.000% de Buscas e | LK Sneakers
- `105` — **Duplicate content in h1 and title**: count `4`, delta `0`, checks `89`
  - sample: source=https://lksneakers.com.br/blogs/novidades/streetwear-masculino-sao-paulo; info=Streetwear Masculino em São Paulo: Guia LK
  - sample: source=https://lksneakers.com.br/blogs/novidades/lancamentos-sneakers-2026; info=Lançamentos de Sneakers 2026: Drops que Importam | LK
  - sample: source=https://lksneakers.com.br/blogs/novidades/jordan-1-retro-comprar-sao-paulo; info=Comprar Tênis Jordan em São Paulo: Guia LK Sneakers
- `112` — **Low text to HTML ratio**: count `89`, delta `0`, checks `89`
  - sample: source=https://lksneakers.com.br/products/supreme-x-nike-air-force-1-low-box-logo-white; info=0.02
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-teddy-bear-pink; info=0.02
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-rose-whisper; info=0.02
- `130` — **Disallowed internal resources**: count `89`, delta `0`, checks `1245`
  - sample: source=https://lksneakers.com.br/products/supreme-x-nike-air-force-1-low-box-logo-white; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-teddy-bear-pink; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}
  - sample: source=https://lksneakers.com.br/products/nike-dunk-low-rose-whisper; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}

### notices

- `104` — **Multiple h1 tags**: count `7`, delta `0`, checks `89`
  - sample: source=https://lksneakers.com.br/blogs/novidades/streetwear-masculino-sao-paulo; info=2
  - sample: source=https://lksneakers.com.br/blogs/novidades/lancamentos-sneakers-2026; info=2
  - sample: source=https://lksneakers.com.br/blogs/novidades/jordan-1-retro-comprar-sao-paulo; info=2
- `213` — **Pages with only one internal link**: count `49`, delta `0`, checks `90`
  - sample: source=https://lksneakers.com.br/blogs/novidades/yeezy-original-vs-falso-como-autenticar-em-2026
  - sample: source=https://lksneakers.com.br/blogs/novidades/versace-onitsuka-tiger-tai-chi-sakura-collab
  - sample: source=https://lksneakers.com.br/blogs/novidades/test-post
- `216` — **Links with no anchor text**: count `13`, delta `0`, checks `16370`
  - sample: source=https://lksneakers.com.br/; target=/collections/sneakers
  - sample: source=https://lksneakers.com.br/; target=/collections/roupas
  - sample: source=https://lksneakers.com.br/; target=/collections/athleisure
- `219` — **Llms.txt has formatting issues**: count `1`, delta `0`, checks `1`
  - sample: source=https://lksneakers.com.br/llms.txt; info={'errors': [{'errorType': 2}]}
- `223` — **Content not optimized**: count `5`, delta `0`, checks `89`
  - sample: source=https://lksneakers.com.br/blogs/novidades/os-10-sneakers-mais-procurados-no-brasil-em-2026; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}
  - sample: source=https://lksneakers.com.br/blogs/novidades/o-que-e-um-sneaker-original-como-identificar-falsificacoes; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}
  - sample: source=https://lksneakers.com.br/blogs/novidades/nike-dunk-low-vs-adidas-samba-qual-comprar-em-2026; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}

## Projeto SEMrush `29110159` — lksneakers.com.br

- Último audit: `2026-06-15 01:09 UTC`
- Status: `FINISHED`; páginas crawled: `100/100`; score: `85`
- Totais info: errors `175`, warnings `264`, notices `855`; broken `0`, blocked `3`, redirected `2`, healthy `7`, haveIssues `88`

### errors

- `16` — **Invalid robots.txt format**: count `1`, delta `0`, checks `1`
  - sample: source=https://lksneakers.com.br/robots.txt; info=Sitemap: /sitemap.xml
- `45` — **Structured data that contains markup errors**: count `174`, delta `0`, checks `397`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco; target=J:15:/:-179495925; info={'item': 'LOCAL_BUSINESS', 'fields': [{'cause': 'NOT_RECOGNIZED', 'names': ['shippingDetails'], 'nestedRel': None}]}
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco; target=J:30:/:-179495925; info={'item': 'ORGANIZATION', 'fields': [{'cause': 'NOT_RECOGNIZED', 'names': ['shippingDetails'], 'nestedRel': None}, {'cause': 'REQUIRED', 'names': ['returnPolicyCountry'], 'nestedRel': 'MerchantReturnPolicy'}]}
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; target=J:30:/:-179495925; info={'item': 'ORGANIZATION', 'fields': [{'cause': 'NOT_RECOGNIZED', 'names': ['shippingDetails'], 'nestedRel': None}, {'cause': 'REQUIRED', 'names': ['returnPolicyCountry'], 'nestedRel': 'MerchantReturnPolicy'}]}

### warnings

- `12` — **Broken external links**: count `87`, delta `0`, checks `185`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco; target=https://wa.me/5511949565000; info=429
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; target=https://wa.me/5511949565000; info=429
  - sample: source=https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco; target=https://wa.me/5511949565000; info=429
- `102` — **Title element is too long**: count `2`, delta `0`, checks `87`
  - sample: source=https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-cloud-white-ivory-branco; info=Tênis Adidas by Stella McCartney Sportswear X Trainers Cloud White Ivory Branco por R$ 3.699,99 em até 10x | LK Sneakers
  - sample: source=https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-brown-mauve-gum; info=Tênis Adidas by Stella McCartney Sportswear X Trainers Brown Mauve Gum por R$ 3.699,99 em até 10x | LK Sneakers
- `112` — **Low text to HTML ratio**: count `87`, delta `0`, checks `87`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco; info=0.02
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; info=0.02
  - sample: source=https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco; info=0.01
- `130` — **Disallowed internal resources**: count `87`, delta `0`, checks `3040`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}
  - sample: source=https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco; target=https://lksneakers.com.br/checkouts/internal/preloads.js?locale=pt-BR&default_configuration_id=3291709662; info={'tag': 'script'}
- `135` — **Unminified JavaScript and CSS files**: count `1`, delta `0`, checks `964`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; target=https://lksneakers.com.br/cdn/shop/t/91/assets/lk-360-viewer.js?v=63948012626773803741774459500; info={'resourceType': 'javascript'}

### notices

- `4` — **Blocked from crawling**: count `3`, delta `0`, checks `90`
  - sample: source=https://lksneakers.com.br/search?options[unavailable_products]=last&options[prefix]=last&options[fields]=title,vendor,product_type,variants.title&q=lip tints
  - sample: source=https://lksneakers.com.br/cart
  - sample: source=https://lksneakers.com.br/account
- `213` — **Pages with only one internal link**: count `3`, delta `0`, checks `87`
  - sample: source=https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-cloud-white-ivory-branco
  - sample: source=https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-brown-mauve-gum
  - sample: source=https://lksneakers.com.br/collections/nike-air-max?filter.v.option.tamanho=40
- `216` — **Links with no anchor text**: count `845`, delta `0`, checks `19692`
  - sample: source=https://lksneakers.com.br/collections/uniqlo-x-kaws; target=/collections/uniqlo-x-kaws?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F3
  - sample: source=https://lksneakers.com.br/collections/uniqlo-x-kaws; target=/collections/uniqlo-x-kaws?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F1
  - sample: source=https://lksneakers.com.br/collections/uniqlo-x-kaws; target=/collections/uniqlo-x-kaws?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F3
- `223` — **Content not optimized**: count `4`, delta `0`, checks `87`
  - sample: source=https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}
  - sample: source=https://lksneakers.com.br/pages/onitsuka-tiger-vs-asics-gel-1130; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}
  - sample: source=https://lksneakers.com.br/pages/new-balance-530-vs-2002r; info={'integrations': {'contentAudit': False}, 'errors': [{'errorType': 2}]}

## Validação pública e classificação

### Real / acionar

- **Broken external image**: SEMrush current `id 14`, count 1. URL externa `sneakerbardetroit...Alaska...jpg` retornou **404**. Ação: trocar/remover imagem do artigo Jordan Alaska.
- **llms.txt formatting issue**: SEMrush current `id 219`, count 1. Com UA `SemrushBot`/`Googlebot`, `/llms.txt` retorna 200 text/markdown; com UA browser simples retornou 503 Shopify. O arquivo tem blocos e headings duplicados/longos; precisa normalização para padrão llms.txt mais estrito.
- **Títulos longos de blog**: SEMrush current `id 102`, count 23. É fila SEO/GEO editorial; não é crítico técnico, mas pode melhorar CTR e legibilidade.
- **Duplicate H1/title e múltiplos H1 em alguns artigos/guias**: current `id 105` count 4 e `id 104` count 7. Baixo risco, bom pacote de limpeza editorial/theme.
- **Pages with only one internal link**: current `id 213`, count 49. Parece oportunidade real de linkagem interna para clusters editoriais/coleções prioritárias.
- **Links with no anchor text**: current `id 216`, count 13 no projeto atual; samples na home para cards/menu de collections. Vale corrigir via aria-label/texto acessível em dev theme.

### Falso positivo / baixo controle

- **Broken external links para WhatsApp**: current `id 12`, count 94, majoritariamente `https://wa.me/5511949565000` com HTTP 429 para o crawler. Validação pública retornou **200** via `api.whatsapp.com`. Classificar como falso positivo/rate-limit de terceiro, salvo se quisermos trocar CTA para link interno de contato.
- **Disallowed internal resources**: current `id 130`, count 89, target `https://lksneakers.com.br/checkouts/internal/preloads.js...`. É recurso Shopify checkout/internal bloqueado por robots; não mexer sem motivo forte.
- **Low text to HTML ratio**: current `id 112`, count 89, majoritariamente PDP. Sinal de PDP com pouco texto vs HTML de tema, mas não deve virar prioridade sem cruzar receita/GSC/conversão.

### Stale / provavelmente já resolvido ou duplicado

- Projeto 29110159 ainda mostra `Invalid robots.txt format` (id 16) e 174 structured data markup errors (id 45), mas o projeto mais recente 16150947 não mostra esses errors. Tratar como snapshot/projeto duplicado antigo até novo crawl confirmar.
- Validação pública do robots: status 200 text/plain; SEMrush current não acusa formato inválido. Não há ação urgente de robots agora.
- Structured data stale: amostra atual de PDP ainda contém `shippingDetails` em Offer e MerchantReturnPolicy, mas SEMrush current não acusa markup errors; se aparecer de novo no projeto atual, pacote separado de schema em dev theme.

## Prioridade recomendada

1. **P0/P1 leve** — corrigir imagem externa quebrada no artigo Jordan Alaska. Impacto: limpa erro real simples; risco baixo; exige write de conteúdo/blog Shopify.
2. **P1 GEO** — normalizar `/llms.txt`: reduzir duplicidades, manter H1 único, seções claras e compatibilidade com parsers. Exige write em asset/route/theme conforme implementação.
3. **P1 SEO editorial** — pacote 10–20 artigos: encurtar titles, resolver H1 duplicado/múltiplo e adicionar links internos para collections/guias prioritários.
4. **P2 Acessibilidade/theme** — links sem anchor text no menu/home: preparar dev theme patch com `aria-label`/texto acessível e validar Lighthouse/HTML antes de produção.
5. **P2 administrativo** — decidir se um dos dois projetos SEMrush deve ser arquivado/ignorado ou recrawleado, para evitar dupla verdade. Não executei mudança SEMrush.

## Aprovação necessária

- Qualquer correção de blog/conteúdo visível, llms.txt, theme ou configuração SEMrush exige tua aprovação explícita antes de write.
- Posso preparar um pacote de execução em dev/preview para: imagem quebrada + llms.txt + 10 artigos prioritários, sem publicar em produção até aprovação.