# LK catalog badges sync

Data: 2026-05-30T23:30:46.208363+00:00
Modo: apply

## Evidência
- Menus: `main-menu, mega-menu-c-pia-1, mega-menu-mobile`
- Coleções alvo: `140`
- Produtos escaneados: `2326`
- Produtos com mudança planejada: `353`
- NEW 90d encontrados: `199`
- GA4: `{"available": true, "rows_total": 2426, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- adidas Taekwondo Mei Ballet Branco e Preto (`adidas-taekwondo-mei-ballet-branco-e-preto`): +[best-seller--adidas-taekwondo-mei-ballet] / -[best-seller--ballet-core]
- Adidas Taekwondo Mei Ballet Preto e Branco (`adidas-taekwondo-mei-ballet-preto-e-branco`): +[best-seller--adidas-taekwondo-mei-ballet] / -[best-seller--ballet-core]
- Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto (`bermuda-saint-studio-alfaiataria-algodao-organico-risca-de-giz-preto`): +[best-seller--bermuda-streetwear] / -[-]
- Bolsa Jacquemus Le Bambino Mini Flap Bag Ivory Bege (`bolsa-jacquemus-le-bambino-mini-flap-bag-ivory-bege`): +[-] / -[best-seller--jacquemus]
- Bolsa Jacquemus Le Chiquito Noeud Bag Light Pink Rosa (`bolsa-jacquemus-le-chiquito-noeud-bag-light-pink-rosa`): +[-] / -[best-seller--jacquemus]
- Boné 6 Panel Onitsuka Tiger x Astroboy Washed Verde (`bone-6-panel-onitsuka-tiger-x-astroboy-washed-verde`): +[-] / -[best-seller--onitsuka-tiger-x-astroboy]
- Boné Aimé Leon Dore Porsche Nylon Logo Jet Black Preto (`bone-aime-leon-dore-porsche-nylon-logo-jet-black-preto`): +[best-seller--aime-leon-dore-x-porsche] / -[-]
- Boné Aimé Leon Dore Unisphere Verde (`bone-aime-leon-dore-unisphere-verde`): +[best-seller--acessorios, best-seller--bone-streetwear] / -[-]
- Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White (`bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white`): +[best-seller--acessorios, best-seller--aime-leon-dore-x-porsche, best-seller--bone-streetwear] / -[best-seller--aime-leon-dore]
- Boné Alo Yoga Off-Duty Branco (`bone-alo-yoga-off-duty-branco`): +[best-seller--acessorios, best-seller--acessorios-alo-yoga, best-seller--bone-streetwear] / -[-]
- Boné Alo Yoga Off-Duty Preto (`bone-alo-yoga-off-duty-preto`): +[best-seller--acessorios-alo-yoga, best-seller--bone-streetwear] / -[-]
- Boné Lululemon Classic Ball Wordmark (`bone-lululemon-classic-ball-wordmark`): +[best-seller--bone-streetwear] / -[-]
- Boné Nude Project New Varsity Bege (`bone-nude-project-new-varsity-bege`): +[-] / -[best-seller--nude-project]
- Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Black Preto (`calca-alo-yoga-airlift-high-waist-7-8-line-up-legging-black-preto`): +[best-seller--calcas-alo-yoga] / -[-]
- Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Gravel Bege (`calca-alo-yoga-airlift-high-waist-7-8-line-up-legging-gravel-bege`): +[best-seller--calcas-alo-yoga] / -[-]
- Calça Alo Yoga Suit Up Trouser (Long) Azul Marinho (`calca-alo-yoga-suit-up-trouser-long-azul-marinho`): +[best-seller--calcas-alo-yoga] / -[-]
- Calça Alo Yoga Suit Up Trouser (Long) Preto (`calca-alo-yoga-suit-up-trouser-long-preto`): +[best-seller--calca-streetwear, best-seller--calcas-alo-yoga] / -[-]
- Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho (`calca-alo-yoga-suit-up-trouser-regular-azul-marinho`): +[best-seller--calca-streetwear, best-seller--calcas-alo-yoga] / -[-]
- Calça Alo Yoga Suit Up Trouser (Regular) Preto (`calca-alo-yoga-suit-up-trouser-regular-preto`): +[best-seller--calca-streetwear, best-seller--calcas-alo-yoga] / -[-]
- Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex® - Canvas Bege (`calca-carhartt-mens-work-relaxed-fit-rugged-flex®-canvas-bege`): +[best-seller--carhartt] / -[-]
- Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex® - Canvas Marrom (`calca-carhartt-mens-work-relaxed-fit-rugged-flex®-canvas-marrom`): +[best-seller--carhartt] / -[-]
- Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex® - Canvas Preto (`calca-carhartt-mens-work-relaxed-fit-rugged-flex®-canvas-preto`): +[best-seller--carhartt] / -[-]
- Calça de Moletom Alo Yoga Accolade Straight Leg (`calca-de-moletom-alo-yoga-accolade-straight-leg`): +[best-seller--calcas-alo-yoga, best-seller--moletom-alo-yoga] / -[-]
- Calça de Moletom Alo Yoga Musa (`calca-de-moletom-alo-yoga-musa`): +[best-seller--calcas-alo-yoga, best-seller--moletom-alo-yoga] / -[-]
- Calça Fear Of God Essentials Sporty Nylon Relaxed Trackpant Jet Black Preto (`calca-fear-of-god-essentials-sporty-nylon-relaxed-trackpant-jet-black-preto`): +[best-seller--fear-of-god] / -[-]
- Calça Lululemon Daydrift Regular (`calca-lululemon-daydrift-regular`): +[best-seller--calca-streetwear] / -[-]
- Calça Nude Project Jeans Old Baggy Blue Azul (`calca-nude-project-jeans-old-baggy-blue-azul`): +[-] / -[best-seller--nude-project]
- Calça Pace Nomo Tailoring Trousers Preto (`calca-pace-nomo-tailoring-trousers-preto`): +[best-seller--calca-streetwear] / -[-]
- Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza (`calca-saint-studio-alfaiataria-leve-prega-dupla-cinza`): +[best-seller--calca-streetwear] / -[-]
- Calça Saint Studio Alfaiataria Leve Prega Dupla Marrom (`calca-saint-studio-alfaiataria-leve-prega-dupla-marrom`): +[best-seller--calca-streetwear] / -[-]
- Calça Saint Studio Jeans Baggy Risca de Giz Azul (`calca-saint-studio-jeans-baggy-risca-de-giz-azul`): +[best-seller--acessorios, best-seller--calca-streetwear] / -[-]
- Camisa Aphase Check - Dark Blue Azul (`camisa-aphase-check-dark-blue`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Aphase Check - Light Blue Azul (`camisa-aphase-check-light-blue`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Aphase Loose - Mottled Brown Marrom (`camisa-aphase-loose-mottled-brown`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Manga Curta Boxy Saint Studio Egípcio Listrada Marinho (`camisa-manga-curta-boxy-saint-studio-egipcio-listrada-marinho`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Manga Longa Alo Yoga Dreams Cape Down (`camisa-manga-longa-alo-yoga-dreamscape-down`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Pace EOT Cuban Collar Off White (`camisa-pace-eot-cuban-collar-off-white`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Pace Steel Cable Cuban Collar Preto (`camisa-pace-steel-cable-cuban-collar-preto`): +[best-seller--camisa-streetwear] / -[-]
- Camisa Saint Studio Pima Listrada Azul (`camisa-saint-studio-pima-listrada-azul`): +[best-seller--camisa-streetwear] / -[-]
- Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (`camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul`): +[-] / -[best-seller--aime-leon-dore]
- ... e mais `313` produtos.

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T233046Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.