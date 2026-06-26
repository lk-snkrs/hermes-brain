# LK catalog badges sync

Data: 2026-05-29T13:09:49.445517+00:00
Modo: apply

## Evidência
- Menu: `main-menu`
- Coleções alvo no menu: `48`
- Produtos escaneados: `2316`
- Produtos com mudança planejada: `17`
- NEW 90d encontrados: `193`
- GA4: `{"available": true, "rows_total": 2422, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat "Special" 100% & 400% Set Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-special-100-400-set-toy-art-multi-color`): +[best-seller--collectibles] / -[-]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat "Special" 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-special-1000-toy-art-multi-color`): +[best-seller--collectibles] / -[-]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat #10 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-10-1000-toy-art-multi-color`): +[best-seller--collectibles] / -[-]
- MEDICOM TOY - Bearbrick Jean-Michel Basquiat #7 1000% Toy Art Multi-Color (`medicom-toy-bearbrick-jean-michel-basquiat-7-1000-toy-art-multi-color`): +[best-seller--collectibles] / -[-]
- MEDICOM TOY - Bearbrick Series 49 100% Toy Art (`medicom-toy-be-rbrick-series-49-100-toy-art`): +[best-seller--collectibles] / -[-]
- Pop Mart CryBaby Crying Again Series Vinyl Face Plush Sealed Case (6 Blind Box LACRADAS) (`pop-mart-crybaby-crying-again-series-vinyl-face-plush-sealed-case-6-blind-box-lacradas`): +[best-seller--pop-mart] / -[-]
- Pop Mart Labubu The Monsters - Zimomo Angel In Clouds Vinyl Face Doll Branco (59cm) (`pop-mart-labubu-the-monsters-zimomo-angel-in-clouds-vinyl-face-doll-branco-59cm`): +[-] / -[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart]
- Pop Mart Labubu The Monsters Big into Energy Series Love Vinyl Plush Pingente (`pop-mart-labubu-the-monsters-have-a-seat-baba-vinyl-plush-pingente-copia`): +[-] / -[best-seller--labubu]
- Pop Mart Labubu The Monsters Big into Energy Series Luck Vinyl Plush Pingente (`pop-mart-labubu-the-monsters-coca-cola-series-happy-factor-vinyl-plush-pingente-copia`): +[-] / -[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart]
- Pop Mart Labubu The Monsters Coca Cola Series Happy Factor Vinyl Plush Pingente (`pop-mart-labubu-the-monsters-big-into-energy-series-love-vinyl-plush-pingente-copia`): +[-] / -[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart]
- Pop Mart Labubu The Monsters Have a Seat BABA Vinyl Plush Pingente (`pop-mart-labubu-the-monsters-have-a-seat-hehe-vinyl-plush-pingente-copia`): +[-] / -[best-seller--labubu]
- Pop Mart Labubu The Monsters Have a Seat DUODUO Vinyl Plush (Secret) (`pop-mart-labubu-the-monsters-have-a-seat-duoduo-vinyl-plush-secret`): +[-] / -[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart]
- Pop Mart Labubu The Monsters Zimomo I Found You Vinyl Doll + Tote Bag Marrom (59cm) (`pop-mart-labubu-the-monsters-zimomo-i-found-you-vinyl-doll-tote-bag-marrom-59cm`): +[-] / -[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart]
- Pop Mart Minnie - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-minnie-mickey-family-cute-together-keychain-series-figures-aberto`): +[best-seller--pop-mart] / -[-]
- Pop Mart Pluto - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-pluto-mickey-family-cute-together-keychain-series-figures-aberto`): +[best-seller--pop-mart] / -[-]
- Pop Mart Secret Huguinho, Zezinho, Luizinho - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-secret-huguinho-zezinho-luizinho-mickey-family-cute-together-keychain-series-figures-aberto`): +[best-seller--pop-mart] / -[-]
- Pop Mart Teco - Mickey Family Cute Together Keychain Series Figures (Aberto) (`pop-mart-teco-mickey-family-cute-together-keychain-series-figures-aberto`): +[best-seller--pop-mart] / -[-]

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T130949Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.