# LK catalog badges sync

Data: 2026-05-30T20:21:52.558382+00:00
Modo: preview

## Evidência
- Menu: `main-menu`
- Coleções alvo no menu: `48`
- Produtos escaneados: `2326`
- Produtos com mudança planejada: `233`
- NEW 90d encontrados: `199`
- GA4: `{"available": true, "rows_total": 2425, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- adidas Taekwondo Mei Ballet Branco e Preto (`adidas-taekwondo-mei-ballet-branco-e-preto`): +[-] / -[best-seller--adidas-taekwondo, best-seller--adidas-todos-os-modelos]
- Adidas Taekwondo Mei Ballet Preto e Branco (`adidas-taekwondo-mei-ballet-preto-e-branco`): +[-] / -[best-seller--adidas-taekwondo, best-seller--adidas-todos-os-modelos]
- Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto (`bermuda-saint-studio-alfaiataria-algodao-organico-risca-de-giz-preto`): +[-] / -[best-seller--roupas, best-seller--saint-studio]
- Boné 6 Panel Onitsuka Tiger x Astroboy Washed Verde (`bone-6-panel-onitsuka-tiger-x-astroboy-washed-verde`): +[-] / -[best-seller--onitsuka-tiger-todos-os-modelos, best-seller--roupas]
- Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White (`bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white`): +[-] / -[best-seller--roupas]
- Boné Nude Project New Varsity Bege (`bone-nude-project-new-varsity-bege`): +[best-seller--nude-project] / -[-]
- Calça Aphase Relaxed SweatPants - Stoned Beige Bege (`calca-aphase-relaxed-sweatpants-stoned-beige`): +[-] / -[best-seller--roupas, best-seller--sale]
- Calça Dane-se Touch Linha Verde (`calca-dane-se-touch-linha-verde`): +[-] / -[best-seller--roupas, best-seller--sale]
- Calça Lululemon Align™ High-Rise 25" (`calca-lululemon-align™-high-rise-25`): +[-] / -[best-seller--athleisure, best-seller--lululemon, best-seller--roupas]
- Calça Lululemon Daydrift Regular (`calca-lululemon-daydrift-regular`): +[best-seller--lululemon] / -[-]
- Calça Lululemon Groove Nulu Super-High-Rise Flared Regular (`calca-lululemon-groove-nulu-super-high-rise-flared-regular`): +[-] / -[best-seller--athleisure, best-seller--lululemon, best-seller--roupas]
- Calça Lululemon Scuba Mid-Rise Wide-Leg Regular (`calca-lululemon-scuba-mid-rise-wide-leg-regular`): +[-] / -[best-seller--athleisure, best-seller--roupas]
- Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo (`calca-nude-project-jeans-old-baggy-black-preto`): +[-] / -[best-seller--nude-project, best-seller--roupas]
- Calça Nude Project Jeans Old Baggy Blue Azul (`calca-nude-project-jeans-old-baggy-blue-azul`): +[-] / -[best-seller--roupas]
- Calça Pace Milli Cargo Azul Marinho (`calca-pace-milli-cargo-azul-marinho`): +[-] / -[best-seller--roupas, best-seller--sale]
- Calça Pace Nomo Tailoring Trousers Preto (`calca-pace-nomo-tailoring-trousers-preto`): +[-] / -[best-seller--roupas]
- Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza (`calca-saint-studio-alfaiataria-leve-prega-dupla-cinza`): +[-] / -[best-seller--roupas]
- Calça Saint Studio Jeans Baggy Risca de Giz Azul (`calca-saint-studio-jeans-baggy-risca-de-giz-azul`): +[-] / -[best-seller--roupas]
- Camisa Aphase Check - Dark Blue Azul (`camisa-aphase-check-dark-blue`): +[-] / -[best-seller--roupas, best-seller--sale]
- Camisa Aphase Check - Light Blue Azul (`camisa-aphase-check-light-blue`): +[-] / -[best-seller--roupas, best-seller--sale]
- Camisa Aphase Loose - Mottled Brown Marrom (`camisa-aphase-loose-mottled-brown`): +[-] / -[best-seller--roupas, best-seller--sale]
- Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (`camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- Camiseta Aimé Leon Dore Postcard Cream Bege (`camiseta-aime-leon-dore-postcard-cream-bege`): +[best-seller--aime-leon-dore] / -[-]
- Camiseta Aimé Leon Dore Unisphere Black White Preto (`camiseta-aime-leon-dore-unisphere-black-white-preto`): +[-] / -[best-seller--aime-leon-dore, best-seller--camiseta-1, best-seller--roupas]
- Camiseta Aimé Leon Dore Unisphere Preto (`camiseta-aime-leon-dore-unisphere-preto`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- Camiseta Aimé Leon Dore Unisphere Pristine Off White (`camiseta-aime-leon-dore-unisphere-pristine-off-white`): +[-] / -[best-seller--roupas]
- Camiseta Aimé Leon Dore Unisphere Verde (`camiseta-aime-leon-dore-unisphere-verde`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- Camiseta Ami Paris de Coeur Branco (`camiseta-ami-paris-de-coeur-branco`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta Comme des Garçons Emblem Rhinestone White/Black Branco (`camiseta-comme-des-garcons-emblem-rhinestone-white-black-branco`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta Comme des Garçons PLAY Red Half Heart Branco (`camiseta-comme-des-garcons-play-red-half-heart-branco`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta Dane-se x Rubem Valentim Emblema 78 Bordo (`camiseta-dane-se-x-rubem-valentim-emblema-78-bordo`): +[-] / -[best-seller--camiseta-1, best-seller--collab-com-artistas, best-seller--dane-se, best-seller--roupas, best-seller--sale]
- Camiseta Dane-se x Rubem Valentim Praça da Sé Off White (`camiseta-dane-se-x-rubem-valentim-praca-da-se-off-white`): +[-] / -[best-seller--camiseta-1, best-seller--collab-com-artistas, best-seller--roupas, best-seller--sale]
- Camiseta Dane-se x Rubem Valentim Roma 3 Preto (`camiseta-dane-se-x-rubem-valentim-roma-3-preto`): +[-] / -[best-seller--camiseta-1, best-seller--collab-com-artistas, best-seller--roupas, best-seller--sale]
- Camiseta Fear Of God Essentials Classic Short Sleeve Jet Black Preto (`camiseta-fear-of-god-essentials-classic-short-sleeve-jet-black-preto`): +[-] / -[best-seller--roupas]
- Camiseta KAWS x Uniqlo Warhol UT Graphic 471321 Branco (`camiseta-kaws-x-uniqlo-warhol-ut-graphic-branco`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta KAWS x Uniqlo Warhol UT Graphic 476350 Branco (`camiseta-kaws-x-uniqlo-warhol-ut-graphic-476350-branco`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta KAWS x Uniqlo Warhol UT Graphic 476352 Preto (`camiseta-kaws-x-uniqlo-warhol-ut-graphic-476352-preto`): +[-] / -[best-seller--camiseta-1, best-seller--roupas, best-seller--sale]
- Camiseta Kith Brush Vintage Boxy Alex Nocturnal Azul Marinho (`camiseta-kith-brush-vintage-boxy-alex-nocturnal-azul-marinho`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- Camiseta Kith Brush Vintage Boxy Alex Silk Off White (`camiseta-kith-brush-vintage-boxy-alex-silk-off-white`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- Camiseta Kith Signature Rose Jones Black Preto (`camiseta-kith-signature-rose-jones-black-preto`): +[-] / -[best-seller--camiseta-1, best-seller--roupas]
- ... e mais `193` produtos.

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T202152Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.