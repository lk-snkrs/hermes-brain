# LK Growth — Next actions após D+7 limpeza de termos operacionais
Status: executado read-only/local; nenhum write em Shopify/GMC/GA4/GSC/theme/Klaviyo/ads. values_printed=false.
## 1) D+14 agendado
- Cron criado: `lkprodcleanD14`
- Run at: `2026-06-19T19:00:00+00:00`
- Delivery: `origin`
## 2) Medição GA4 PDP funnel
- Probe GA4 por `pagePath + eventName` executado. Baseline: {'view_item': 43130.0, 'add_to_cart': 608.0, 'cart_per_view_pct': 1.41, 'begin_checkout': 0, 'purchase': 0, 'row_count': 1938}; Pós: {'view_item': 44923.0, 'add_to_cart': 517.0, 'cart_per_view_pct': 1.15, 'begin_checkout': 0, 'purchase': 0, 'row_count': 1898}; Delta: {'view_item_delta_pct': 4.2, 'add_to_cart_delta_pct': -15.0, 'cart_per_view_delta_pp': -0.26}.
- Achado: GA4 amarra `view_item` e `add_to_cart` por PDP, mas `begin_checkout` e `purchase` não apareceram vinculados ao `pagePath`. Para ficar decision-grade por PDP, precisa instrumentar `product_handle/item_id` nos eventos de checkout/compra ou reconciliar com Shopify line items por handle.
## 3) Shortlists
### Top Shopify receita pós-7d
- Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom — `tenis-nike-moon-shoe-sp-jacquemus-medium-brown`: 2 un.; R$ 11999.98
- Tênis Nike Vomero Premium Alabaster Amarelo — `tenis-nike-vomero-premium-alabaster-amarelo`: 2 un.; R$ 8999.98
- Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto — `tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto`: 1 un.; R$ 6999.99
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — `nike-moon-shoe-sp-jacquemus-alabaster-amarelo`: 1 un.; R$ 6999.99
- Tênis Nike Moon Shoe SP Jacquemus Off White — `tenis-nike-moon-shoe-sp-jacquemus-off-white`: 1 un.; R$ 5999.99
- Tênis New Balance 204L Sea Salt Linen Bege — `tenis-new-balance-204l-sea-salt-linen-bege`: 2 un.; R$ 5599.98
- Tênis New Balance 204L Mushroom Arid Stone Marrom — `tenis-new-balance-204l-mushroom-arid-stone-marrom`: 2 un.; R$ 5599.98
- Tênis New Balance 204L Arid Timberwolf Bege — `tenis-new-balance-204l-timberwolf-bege`: 2 un.; R$ 5599.98
- Tênis New Balance 9060 Slate Grey Raincloud Cinza — `tenis-new-balance-9060-slate-grey-raincloud-cinza`: 2 un.; R$ 4799.98
- Tênis Alo Yoga ALO Runner Branco — `tenis-alo-yoga-alo-runner-branco`: 2 un.; R$ 4079.98
### Maiores perdas GSC cliques — janela comparável 5d
- Tênis Adidas Tokyo Mary Jane Crystal Sky Cream White Azul — `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`: 6.0 → 0.0 cliques (-6.0)
- Tênis Nike Dunk Low Stranger Things Phantom Branco — `tenis-nike-dunk-low-stranger-things-phantom-branco`: 6.0 → 0 cliques (-6.0)
- Tênis New Balance 204L Mushroom Arid Stone Marrom — `tenis-new-balance-204l-mushroom-arid-stone-marrom`: 4.0 → 0.0 cliques (-4.0)
- Tênis Adidas Samba Jane Chalk White Wonder Quartz Branco — `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco`: 3.0 → 0.0 cliques (-3.0)
- Tênis Nike Mind 002 Light Smoke Grey Cinza — `tenis-nike-mind-002-light-smoke-grey-cinza`: 4.0 → 1.0 cliques (-3.0)
- Tênis Onitsuka Tiger Moage CO Cream Black Bege — `tenis-onitsuka-tiger-moage-co-cream-black-bege`: 3.0 → 0 cliques (-3.0)
- Tênis Onitsuka Tiger Tokuten Charcoal Birch Cinza — `tenis-onitsuka-tiger-tokuten-charcoal-birch-cinza`: 3.0 → 0 cliques (-3.0)
- Óculos de Sol Palm Angels PERI039-1007 Preto — `oculos-de-sol-palm-angels-peri039-1007-preto`: 4.0 → 2.0 cliques (-2.0)
- Óculos Oakley Plantaris TI Raw Titanium Cinza — `oculos-oakley-plantaris-ti-raw-titanium-cinza`: 2.0 → 0.0 cliques (-2.0)
- Saia Alo Yoga Grand Slam Tennis Branco — `saia-alo-yoga-grand-slam-tennis-branco`: 2.0 → 0.0 cliques (-2.0)
### Maiores quedas CTR GSC — mín. 50 impressões nas duas janelas
- Tênis Adidas Samba Jane Chalk White Wonder Quartz Branco — `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco`: CTR 4.69% → 0.0% (-4.69 pp), impr. 64.0 → 50.0
- Pop Mart CryBaby Crying Again Series Vinyl Face Plush Sealed Case (6 Blind Box LACRADAS) — `pop-mart-crybaby-crying-again-series-vinyl-face-plush-sealed-case-6-blind-box-lacradas`: CTR 1.89% → 0.0% (-1.89 pp), impr. 53.0 → 64.0
- Óculos de Sol Palm Angels PERI039-1007 Preto — `oculos-de-sol-palm-angels-peri039-1007-preto`: CTR 2.82% → 1.07% (-1.75 pp), impr. 142.0 → 187.0
- Saia Alo Yoga Grand Slam Tennis Branco — `saia-alo-yoga-grand-slam-tennis-branco`: CTR 1.68% → 0.0% (-1.68 pp), impr. 119.0 → 107.0
- Tênis Alo Yoga Alo Recovery Mode Tênis Pink/White Rosa — `tenis-alo-yoga-alo-recovery-mode-sneaker-pink-wild-rose-rosa-copia`: CTR 2.68% → 1.15% (-1.53 pp), impr. 112.0 → 87.0
- Óculos Oakley Plantaris TI Raw Titanium Cinza — `oculos-oakley-plantaris-ti-raw-titanium-cinza`: CTR 1.08% → 0.0% (-1.08 pp), impr. 185.0 → 140.0
- Tênis Maison Mihara Yasuhiro "Peterson" OG Sole Canvas Low-top Black Preto — `tenis-maison-mihara-yasuhiro-peterson-og-sole-canvas-low-top-black-preto`: CTR 0.99% → 0.0% (-0.99 pp), impr. 101.0 → 114.0
- Tênis Nike Air Jordan 1 Retro Low OG Zion Williamson Voodoo Alternate Azul — `tenis-air-jordan-1-retro-low-og-zion-williamson-voodoo-alternate-azul`: CTR 0.63% → 0.0% (-0.63 pp), impr. 159.0 → 167.0
- Moletom Lululemon Scuba Oversized Full-Zip — `moletom-lululemon-scuba-oversized-full-zip`: CTR 0.54% → 0.0% (-0.54 pp), impr. 184.0 → 117.0
- Tênis Nike Air Jordan 1 Low OG Olive Verde — `tenis-nike-air-jordan-1-low-og-olive-verde`: CTR 0.94% → 0.4% (-0.54 pp), impr. 319.0 → 251.0
### Venda com tráfego caindo — candidatos CRO prioritários
- Tênis Nike Vomero Premium Alabaster Amarelo — `tenis-nike-vomero-premium-alabaster-amarelo`: R$ 8999.98; GA4 Δsess 180.0; GSC Δcliques -2.0
- Tênis Nike Moon Shoe SP Jacquemus Off White — `tenis-nike-moon-shoe-sp-jacquemus-off-white`: R$ 5999.99; GA4 Δsess 10.0; GSC Δcliques -1.0
- Tênis New Balance 204L Sea Salt Linen Bege — `tenis-new-balance-204l-sea-salt-linen-bege`: R$ 5599.98; GA4 Δsess None; GSC Δcliques -1.0
- Tênis New Balance 204L Mushroom Arid Stone Marrom — `tenis-new-balance-204l-mushroom-arid-stone-marrom`: R$ 5599.98; GA4 Δsess 5.0; GSC Δcliques -4.0
- Tênis New Balance 204L Arid Timberwolf Bege — `tenis-new-balance-204l-timberwolf-bege`: R$ 5599.98; GA4 Δsess 223.0; GSC Δcliques -1.0
- Tênis Alo Yoga ALO Runner Branco — `tenis-alo-yoga-alo-runner-branco`: R$ 4079.98; GA4 Δsess None; GSC Δcliques -1.0
- Tênis New Balance 9060 Rich Oak Marrom — `tenis-new-balance-9060-rich-oak-marrom`: R$ 2799.99; GA4 Δsess 139.0; GSC Δcliques -1.0
- Tênis New Balance 9060 Cortado Marrom — `tenis-new-balance-9060-cortado-marrom`: R$ 2399.99; GA4 Δsess None; GSC Δcliques -1.0
- Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — `tenis-onitsuka-tiger-mexico-66-sabot-beige-green-bege`: R$ 2199.99; GA4 Δsess -446.0; GSC Δcliques None
## 4) Copy segura criada
- Drafts internos em `copy-safe-drafts/` para 12 handles prioritários. Não publicados.
- Linguagem: curadoria, autenticidade, atendimento humano, orientação de tamanho, confirmação pelo chat quando necessário.
## 5) PageSpeed/CRO mobile
- https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown: PSI mobile 67; SEO 92; LCP lab 4.1 s; TBT 400 ms; erro None
- https://lksneakers.com.br/products/tenis-nike-vomero-premium-alabaster-amarelo: PSI mobile None; SEO None; LCP lab None; TBT None; erro PageSpeed Insights request timed out (120s). The target page may be very slow.
- https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto: PSI mobile None; SEO None; LCP lab None; TBT None; erro PageSpeed Insights request timed out (120s). The target page may be very slow.
- https://lksneakers.com.br/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo: PSI mobile None; SEO None; LCP lab None; TBT None; erro PageSpeed Insights request timed out (120s). The target page may be very slow.
- https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-off-white: PSI mobile None; SEO None; LCP lab None; TBT None; erro PageSpeed Insights request timed out (120s). The target page may be very slow.
- https://lksneakers.com.br/products/tenis-new-balance-204l-sea-salt-linen-bege: PSI mobile 33; SEO 92; LCP lab 15.9 s; TBT 1,330 ms; erro None

## Approval packets necessários antes de writes
- GA4/GTM/Shopify customer events: instrumentar `product_handle/item_id` em eventos de checkout/compra. Risco baixo-médio; rollback via remover script/event mapping; validar no DebugView/GA4 Realtime e D+7.
- PDP copy: publicar apenas nos handles priorizados após aprovação explícita; rollback via restaurar body_html/SEO backup; validar QA termos vetados + GSC/Shopify D+7.
- Theme/PageSpeed: testar em dev theme primeiro redução/defer de JS/CSS não crítico e otimização hero image/LCP; rollback por duplicata/tema anterior; validar PSI mobile + browser QA + Shopify add_to_cart.
