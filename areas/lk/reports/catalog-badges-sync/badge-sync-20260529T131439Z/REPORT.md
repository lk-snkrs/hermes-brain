# LK catalog badges sync

Data: 2026-05-29T13:14:39.837213+00:00
Modo: apply

## Evidência
- Menu: `main-menu`
- Coleções alvo no menu: `48`
- Produtos escaneados: `2316`
- Produtos com mudança planejada: `57`
- NEW 90d encontrados: `193`
- GA4: `{"available": true, "rows_total": 2422, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- adidas Taekwondo Mei Ballet Branco e Preto (`adidas-taekwondo-mei-ballet-branco-e-preto`): +[best-seller--ballet-core] / -[-]
- Boné 5 Panel Aimé Leon Dore Unisphere Azul (`bone-5-panel-aime-leon-dore-unisphere-azul`): +[-] / -[best-seller--aime-leon-dore]
- Boné 5 Panel Aimé Leon Dore Unisphere Branco (`bone-5-panel-aime-leon-dore-unisphere-branco`): +[-] / -[best-seller--aime-leon-dore, best-seller--roupas]
- Boné Kith Script Logo Classic Boné Canvas Bege Branco (`bone-kith-script-logo-classic-cap-canvas-bege-branco`): +[-] / -[best-seller--kith]
- Boné Kith Script Logo Classic Boné Nocturnal Branco/Azul (`bone-kith-script-logo-classic-cap-nocturnal`): +[-] / -[best-seller--kith]
- Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul (`camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul`): +[best-seller--aime-leon-dore] / -[-]
- Camiseta Aimé Leon Dore Unisphere Black White Preto (`camiseta-aime-leon-dore-unisphere-black-white-preto`): +[best-seller--aime-leon-dore] / -[-]
- Camiseta Kith Brush Vintage Boxy Alex Nocturnal Azul Marinho (`camiseta-kith-brush-vintage-boxy-alex-nocturnal-azul-marinho`): +[best-seller--kith] / -[-]
- Camiseta Kith Brush Vintage Boxy Alex Silk Off White (`camiseta-kith-brush-vintage-boxy-alex-silk-off-white`): +[best-seller--kith] / -[-]
- Camiseta Kith Signature Rose Jones Black Preto (`camiseta-kith-signature-rose-jones-black-preto`): +[best-seller--kith] / -[-]
- Jason Markk Delicates Cleaning Brush (`jason-markk-delicates-cleaning-brush`): +[-] / -[best-seller--jason-markk]
- Jason Markk Durables Cleaning Brush (`jason-markk-durables-cleaning-brush`): +[-] / -[best-seller--jason-markk]
- Jason Markk Essential Kit de Limpeza (`jason-markk-essential-kit`): +[-] / -[best-seller--jason-markk]
- KAWS Companion Flayed Open Edition Vinyl Figure Black Toy Art Preto (`kaws-companion-flayed-open-edition-vinyl-figure-black-toy-art-preto`): +[-] / -[best-seller--kaws]
- KAWS Holiday Shanghai Vinyl Figure Grey Toy Art Cinza (`kaws-holiday-shanghai-vinyl-figure-grey-toy-art-cinza`): +[best-seller--kaws] / -[-]
- KAWS Holiday Thailand Vinyl Figure Black Toy Art Preto (`kaws-holiday-thailand-vinyl-figure-black-toy-art-preto`): +[best-seller--kaws] / -[-]
- KAWS THE PROMISE Vinyl Figure Grey Toy Art Cinza (`kaws-the-promise-vinyl-figure-grey-toy-art-cinza`): +[-] / -[best-seller--kaws]
- Lip Case Rhode By Hailey Bieber Limited Edition Shade Amarelo (`lip-case-rhode-by-hailey-bieber-limited-edition-shade-amarelo`): +[best-seller--rhode] / -[-]
- MEDICOM TOY - Bearbrick Breaking Bad Pink Bear 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-breaking-bad-pink-bear-1000-toy-art-multi-color`): +[best-seller--be-rbrick] / -[-]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat "Special" 100% & 400% Set Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-special-100-400-set-toy-art-multi-color`): +[-] / -[best-seller--be-rbrick, best-seller--collectibles]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat "Special" 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-special-1000-toy-art-multi-color`): +[-] / -[best-seller--be-rbrick, best-seller--collectibles]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat #7 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-7-1000-toy-art-multi-color`): +[-] / -[best-seller--be-rbrick, best-seller--collectibles]
- MEDICOM TOY - Bearbrick Katsushika Hokusai (Thirty-six Views of Tomitake, Fine Wind, Clear Morning) 1000% Toy Art Multi- (`medicom-toy-bearbrick-katsushika-hokusai-thirty-six-views-of-tomitake-fine-wind-clear-morning-1000-toy-art-multi`): +[best-seller--be-rbrick] / -[-]
- MEDICOM TOY - Bearbrick Keith Haring #8 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-keith-haring-8-1000-toy-art-multi-color`): +[best-seller--be-rbrick] / -[-]
- MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado) (`medicom-toy-bearbrick-series-48-100-toy-art-blind-box-lacrado`): +[-] / -[best-seller--be-rbrick, best-seller--collectibles]
- MEDICOM TOY - BEARBRICK The Batman 100％ e 400％ Toy Art Multi-Color (`medicom-toy-be-rbrick-the-batman-100-e-400-toy-art-multi-color`): +[best-seller--be-rbrick] / -[-]
- Moletom Alo Yoga Cropped Serenity Coverup Black Preto (`moletom-alo-yoga-cropped-serenity-coverup-black-preto`): +[-] / -[best-seller--moletom-1]
- Moletom Alo Yoga Cropped Serenity Coverup Bluestone Azul (`moletom-alo-yoga-cropped-serenity-coverup-bluestone-azul`): +[-] / -[best-seller--moletom-1]
- Moletom Slyce Off Court Off White (`moletom-slyce-off-court-off-white`): +[best-seller--moletom-1] / -[-]
- Moletom Slyce Off Court Stadium Verde (`moletom-slyce-off-court-stadium-verde`): +[best-seller--moletom-1] / -[-]
- Pop Mart Disney Mickey Family Together Series Plush Keychain Sealed Case (8 Blind Box) Lacrado (`pop-mart-disney-mickey-family-together-series-plush-keychain-sealed-case-8-blind-box-lacrado`): +[-] / -[best-seller--mickey-family-keychain, best-seller--pop-mart]
- Pop Mart Labubu The Monsters Coca Cola Series Surprise Shake Vinyl Plush Figure Pingente (`pop-mart-labubu-the-monsters-coca-cola-series-surprise-shake-vinyl-plush-figure-pingente`): +[best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters Coca-Cola Series Little Snowman Figure (`pop-mart-labubu-the-monsters-coca-cola-series-little-snowman-figure`): +[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters Coca-Cola Series Look What I Found Figure (`pop-mart-labubu-the-monsters-coca-cola-series-look-what-i-found-figure`): +[best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters Coca-Cola Series Snowy Mountain Figure (`pop-mart-labubu-the-monsters-coca-cola-series-snowy-mountain-figure`): +[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters Coca-Cola Series Special Sofa Figure (`pop-mart-labubu-the-monsters-coca-cola-series-special-sofa-figure`): +[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters Coca-Cola Series Super Surprise Figure (`pop-mart-labubu-the-monsters-coca-cola-series-super-surprise-figure`): +[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart] / -[-]
- Pop Mart Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-mickey-family-cute-together-keychain-series-figures-aberto`): +[-] / -[best-seller--mickey-family-keychain]
- Pop Mart Minnie - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-minnie-mickey-family-cute-together-keychain-series-figures-aberto`): +[-] / -[best-seller--mickey-family-keychain, best-seller--pop-mart]
- Pop Mart Pateta - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-pateta-mickey-family-cute-together-keychain-series-figures-aberto`): +[-] / -[best-seller--mickey-family-keychain]
- ... e mais `17` produtos.

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T131439Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.