# AI Visibility / LKGOC — Onda C prioritização

- Data UTC: `2026-06-19T13:31:06.684247+00:00`
- Escopo: read-only; writes externos=0; values_printed=false
- Claude SEO aplicado como checklist: on-page, ecommerce, content/E-E-A-T e GEO/AEO citável.

## Ordem recomendada
### P0 — /collections/adidas-handball-spezial
- Título Shopify: Adidas Handball Spezial
- Produtos na coleção: 15
- SEO atual: title=`Adidas Handball Spezial - LK`; meta=`Compre Adidas Handball Spezial na LK Sneakers. Curadoria LK · 100% originais · Parcele em 10x · Loja Jardins SP.`
- Demanda: adidas spezial — Google SV 40500; AI SV 33; Google +22% mensal; AI estável/alto
- Modo: AI Visibility + collection SEO cleanup
- Por que: maior demanda Google da lista e coleção com 15 produtos; SEO atual ainda usa linguagem operacional antiga.

### P0 — /collections/new-balance-1906r
- Título Shopify: New Balance 1906R
- Produtos na coleção: 11
- SEO atual: title=`New Balance 1906R | Comprar Original na LK Sneakers`; meta=`New Balance 1906R originais na LK Sneakers. Amortecimento ABZORB SBS e design retro-futurista. Envio para todo o Brasil com garantia de autenticidade.`
- Demanda: new balance 1906 — Google SV 9900; AI SV 2; evergreen transacional
- Modo: AI Visibility + cluster 1906R/1906L
- Por que: demanda transacional forte, 1906R+1906L somam boa superfície; limpar promessa de envio/frete no SEO legado.

### P1 — /collections/onitsuka-tiger-mexico-66
- Título Shopify: Onitsuka Tiger Mexico 66
- Produtos na coleção: 102
- SEO atual: title=`Onitsuka Tiger Mexico 66 Original | LK Sneakers`; meta=`Onitsuka Tiger Mexico 66 original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- Demanda: onitsuka tiger mexico 66 — Google SV 8100; AI SV 7; Google +22% mensal, +49% trimestral
- Modo: LKGOC/AI refresh focado no modelo
- Por que: 102 produtos e demanda em alta; fortalecer modelo específico além da página geral Onitsuka.

### P1 — /collections/new-balance-204l
- Título Shopify: New Balance 204L
- Produtos na coleção: 32
- SEO atual: title=`New Balance 204L Original | LK Sneakers`; meta=`New Balance 204L original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- Demanda: new balance 204l — Google SV 12100; AI SV None; YoY explosivo; já coberto parcialmente
- Modo: impact refresh / reforço citável
- Por que: 32 produtos e demanda muito alta; já coberto, então foco é revisão e impacto, não nova base.

### P2 — /collections/crocs-relampago-mcqueen
- Título Shopify: Crocs Relâmpago McQueen
- Produtos na coleção: 1
- SEO atual: title=`Crocs Relâmpago McQueen Original | LK Sneakers`; meta=`Compre Crocs Relâmpago McQueen original na LK Sneakers: curadoria premium, autenticidade garantida, atendimento humano e até 10x sem juros.`
- Demanda: crocs relampago mcqueen — Google SV 33100; AI SV 36; Google +49% mensal; AI 36
- Modo: AI Visibility defensivo + snippet cleanup
- Por que: demanda enorme, mas só 1 produto; bom para captura de intenção, risco de fricção por baixa profundidade de catálogo.

### P2 — /collections/asics-gel-kayano-14
- Título Shopify: Asics Gel-Kayano 14
- Produtos na coleção: 3
- SEO atual: title=`ASICS Gel-Kayano 14 Original | LK Sneakers`; meta=`ASICS Gel-Kayano 14 original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- Demanda: asics gel kayano 14 — Google SV 8100; AI SV 2; Google +23% mensal
- Modo: AI Visibility lite
- Por que: demanda boa, porém só 3 produtos; executar se houver plano comercial de ampliar sortimento.

## Gates
- Produção Shopify/SEO/llms público só com aprovação explícita de Lucas por onda/coleção.
- DEV/unpublished permitido apenas para preview LKGOC, com verificação de `role: unpublished`.
- Rollback: backup de descriptionHtml + SEO antes de qualquer write.