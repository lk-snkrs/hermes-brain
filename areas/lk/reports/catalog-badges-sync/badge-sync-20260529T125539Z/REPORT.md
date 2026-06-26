# LK catalog badges sync

Data: 2026-05-29T12:55:39.152383+00:00
Modo: preview

## Evidência
- Menu: `main-menu`
- Coleções alvo no menu: `48`
- Produtos escaneados: `2316`
- Produtos com mudança planejada: `91`
- NEW 90d encontrados: `193`
- GA4: `{"available": true, "rows_total": 2422, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- Basic Pack 5.8 Sufgang Multicolor (`basic-pack-5-8-sufgang-multicolor`): +[-] / -[best-seller--sufgang]
- Bermuda Chino Saint Studio Supima Caqui (`bermuda-chino-saint-studio-supima-caqui`): +[-] / -[best-seller--shorts]
- Bota Timberland 6" Premium Waterproof Boot Supreme Black Preto (`bota-timberland-6-premium-waterproof-boot-supreme-black-preto`): +[-] / -[best-seller--supreme]
- Calça Alo Yoga Suit Up Trouser (Long) Preto (`calca-alo-yoga-suit-up-trouser-long-preto`): +[best-seller--athleisure] / -[-]
- Calça Lululemon Scuba Mid-Rise Wide-Leg Regular (`calca-lululemon-scuba-mid-rise-wide-leg-regular`): +[best-seller--lululemon] / -[-]
- Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo (`calca-nude-project-jeans-old-baggy-black-preto`): +[best-seller--nude-project] / -[-]
- Calça Nude Project Jeans Old Baggy Blue Azul (`calca-nude-project-jeans-old-baggy-blue-azul`): +[best-seller--nude-project] / -[-]
- Calça Pace PF SweatPants Preto (`calca-pace-pf-sweatpants-preto`): +[-] / -[best-seller--pace]
- Camisa Aimé Leon Dore Fassianos Half-Zip Cycling Off White (`camisa-aime-leon-dore-fassianos-half-zip-cycling-off-white`): +[-] / -[best-seller--aime-leon-dore]
- Camisa Aphase Check - Dark Blue Azul (`camisa-aphase-check-dark-blue`): +[best-seller--aphase] / -[-]
- Camisa Aphase Check - Light Yellow Bege (`camisa-aphase-check-light-yellow-bege`): +[-] / -[best-seller--aphase]
- Camiseta Aimé Leon Dore Unisphere Preto (`camiseta-aime-leon-dore-unisphere-preto`): +[best-seller--aime-leon-dore] / -[-]
- Camiseta Ami Paris de Coeur Azul (`camiseta-ami-paris-de-coeur-azul`): +[-] / -[best-seller--ami-paris]
- Camiseta Ami Paris de Coeur Preto (`camiseta-ami-paris-de-coeur-preto`): +[-] / -[best-seller--ami-paris]
- Camiseta Ami Paris de Coeur Rouge Azul (`camiseta-ami-paris-de-coeur-rouge-azul`): +[-] / -[best-seller--ami-paris]
- Camiseta Baby Look Nude Project Juicy Cherry Branca (`camiseta-baby-look-nude-projet-juicy-cherry-branca`): +[-] / -[best-seller--nude-project]
- Camiseta Baby Look Nude Project Juicy Cherry Preto (`camiseta-baby-look-nude-projet-juicy-cherry-preto`): +[-] / -[best-seller--nude-project]
- Camiseta Comme des Garçons Emblem Rhinestone White/Red Branco (`camiseta-comme-des-garcons-emblem-rhinestone-white-red-branco`): +[-] / -[best-seller--comme-des-garcons]
- Camiseta Dane-se x Rubem Valentim Pintura Verde (`camiseta-dane-se-x-rubem-valentim-pintura-verde`): +[-] / -[best-seller--dane-se-x-rubem-valentim]
- Camiseta Egho Studios Boxy Faded 'Formigas' Cinza (`camiseta-egho-studios-boxy-faded-formigas-cinza`): +[-] / -[best-seller--egho-studios]
- Camiseta Egho Studios Boxy Faded 'O Culto' Cinza (`camiseta-egho-studios-boxy-faded-o-culto-cinza`): +[-] / -[best-seller--egho-studios]
- Camiseta Egho Studios Boxy Faded Chumbo (`camiseta-egho-studios-boxy-faded-chumbo`): +[-] / -[best-seller--egho-studios]
- Camiseta Egho Studios Boxy Faded Vermelha (`camiseta-egho-studios-boxy-faded-vermelha`): +[-] / -[best-seller--egho-studios]
- Camiseta KAWS x Uniqlo Warhol UT Graphic 47635 Preto (`camiseta-kaws-x-uniqlo-warhol-ut-graphic-47635-preto`): +[-] / -[best-seller--uniqlo-x-kaws]
- Camiseta Manga Longa Pace Relaxed Waffle Knit Preto (`camiseta-manga-longa-pace-relaxed-waffle-knit-preto`): +[-] / -[best-seller--pace]
- Camiseta MASP x Leonilson "Sem Titulo" Bege (`camiseta-masp-x-leonilson-sem-titulo-marrom`): +[-] / -[best-seller--camiseta-1, best-seller--masp, best-seller--masp-x-leonilson, best-seller--roupas]
- Camiseta Nude Project Answer Cinza (`camiseta-nude-projet-answer-cinza`): +[-] / -[best-seller--nude-project]
- Camiseta Nude Project Global Soon Black Preto (`camiseta-nude-project-global-soon-black-preto`): +[best-seller--nude-project] / -[-]
- Camiseta Nude Project Tour Branco (`camiseta-nude-projet-tour-branco`): +[-] / -[best-seller--nude-project]
- Camiseta Pace Buero Washed Black Preto (`camiseta-pace-buero-washed-black-preto`): +[best-seller--camiseta-1] / -[-]
- Camiseta Pace Fold Preta (`camiseta-pace-fold-preta`): +[best-seller--pace] / -[-]
- Camiseta Pace Patavision Off White (`camiseta-pace-patavision-off-white`): +[best-seller--pace] / -[-]
- Camiseta Pace Principles Off White (`camiseta-pace-principles-off-white`): +[-] / -[best-seller--camiseta-1, best-seller--pace]
- Camiseta Saint Studio Boxy Supima Breuer Preto (`camiseta-saint-studio-boxy-supima-breuer-preto`): +[best-seller--camiseta-1] / -[-]
- Camiseta Sufgang Basic Pack 5.8 Cinza (`camiseta-sufgang-basic-pack-5-8-cinza`): +[-] / -[best-seller--sufgang]
- Camiseta Sufgang Stunt Master Azul (`camiseta-sufgang-stunt-master-azul`): +[best-seller--sufgang] / -[-]
- Camiseta Supreme Tyler The Creator Preto (`camiseta-supreme-tyler-the-creator-preto`): +[-] / -[best-seller--supreme]
- Capa de Batom Rhode By Hailey Bieber Grey Cinza (`lip-case-rhode-by-hailey-bieber-grey-cinza`): +[-] / -[best-seller--rhode]
- Comme des Garçons PLAY Red Emblem White Branco (`camiseta-comme-des-garcons-play-branco`): +[-] / -[best-seller--comme-des-garcons]
- Jaqueta Aphase Heavy - Used Black Preto (`jaqueta-aphase-heavy-used-black-preto`): +[-] / -[best-seller--aphase]
- ... e mais `51` produtos.

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T125539Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.