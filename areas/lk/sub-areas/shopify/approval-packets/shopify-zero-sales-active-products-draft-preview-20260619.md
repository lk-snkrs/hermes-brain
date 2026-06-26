# Preview — produtos ACTIVE sem compra paga no Shopify Sales OS — 2026-06-19

Status: PREVIEW READ-ONLY. Não executei draft/write Shopify.

## Critério
- Produto Shopify `status=ACTIVE` no readback Admin GraphQL.
- `publishedAt`/`createdAt` usado como contexto de lançamento/idade.
- Zero line items em `shopify_sales_paid_line_items_enriched` no período coberto pelo Sales OS.
- Não usei Shopify inventory como verdade de estoque; `totalInventory` é apenas contexto Shopify.

## Resumo
- active_products: 1825
- paid_products_in_sales_os: 754
- zero_paid_sales_active: 1207
- sales_os_paid_period_min: 2026-01-01T13:08:00Z
- sales_os_paid_period_max: 2026-06-19T12:43:24-03:00
- generated_at_utc: 2026-06-19T18:13:54.876673+00:00
- zero_by_min_age_days: {'0': 1207, '7': 1185, '14': 1181, '30': 1156, '60': 1121, '90': 1066, '120': 1048, '180': 1017}
- top_vendors_zero_sales: [('Nike', 245), ('Jordan', 199), ('Adidas', 150), ('Alo Yoga', 69), ('Onitsuka Tiger', 60), ('New Balance', 44), ('Yeezy', 30), ('LK', 23), ('Skims', 23), ('Dane-se', 22), ('Nude Project', 22), ('Jacquemus', 21), ('Lululemon', 21), ('Slyce', 19), ('Saint Studio', 17), ('Medicom Toy', 17), ('Aimé Leon Dore', 16), ('KAWS', 16), ('Puma', 13), ('Pop Mart', 11)]

## Candidatos mais antigos / prioritários para revisar
- 1074d | Adidas | Tênis | Tênis ADI2000 Triple Black Preto | handle `adi2000-triple-black` | id 8084012040414 | Shopify inventory ctx 16
- 1074d | Adidas | Tênis | Tênis adidas ADI2000 Chalk White Branco | handle `adidas-adi2000-chalk-white` | id 8084011974878 | Shopify inventory ctx 10
- 1074d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 Dazzling Blue Preto | handle `yeezy-boost-350-v2-dazzling-blue` | id 8084016824542 | Shopify inventory ctx 7
- 1074d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 Salt Verde | handle `yeezy-350-v2-salt` | id 8084017610974 | Shopify inventory ctx 11
- 1074d | Yeezy | Tênis | Tênis Yeezy Foam Runner MX Sand Grey Cinza | handle `yeezy-foam-runner-mx-sand-grey` | id 8084001259742 | Shopify inventory ctx 4
- 1074d | Yeezy | Tênis | Tênis Yeezy Foam Runner Onyx Preto | handle `yeezy-foam-runner-onyx` | id 8084001226974 | Shopify inventory ctx 6
- 1074d | Yeezy | Tênis | Tênis Yeezy Foam Runner Stone Sage Bege | handle `yeezy-foam-runner-stone-sage-924604518` | id 8084014923998 | Shopify inventory ctx 1
- 1074d | Yeezy | Tênis | Tênis Yeezy Slide Boné Branco | handle `yeezy-slide-bone-937693978` | id 8084001030366 | Shopify inventory ctx 1
- 1074d | Yeezy | Tênis | Tênis Yeezy Slide Glow Green Verde | handle `yeezy-slide-glow-green` | id 8084000932062 | Shopify inventory ctx 14
- 1074d | Yeezy | Tênis | Tênis Yeezy Slide Ochre Marrom | handle `yeezy-slide-ochre-925686464` | id 8084013285598 | Shopify inventory ctx 0
- 1064d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 Slate Bege | handle `yeezy-boost-350-v2-slate` | id 8091815215326 | Shopify inventory ctx 11
- 1064d | Yeezy | Tênis | Tênis Yeezy Foam Runner MX Cinder Marrom | handle `yeezy-foam-runner-mx-cinder` | id 8091815608542 | Shopify inventory ctx 11
- 1064d | Yeezy | Tênis | Tênis Yeezy Slide Azure Azul | handle `yeezy-slide-azure` | id 8091815641310 | Shopify inventory ctx 0
- 1064d | Yeezy | Tênis | Tênis Yeezy Slide Pure (2022) Bege | handle `yeezy-slide-pure-2022` | id 8091815084254 | Shopify inventory ctx 4
- 1058d | Yeezy | Tênis | Tênis Yeezy 350 V2 Carbon Beluga Cinza | handle `yeezy-350-v2-carbon-beluga` | id 8097341833438 | Shopify inventory ctx 16
- 1057d | Adidas | Tênis | Tênis Adidas Samba OG White Scarlet Branco | handle `samba-og-white-scarlet` | id 8097486569694 | Shopify inventory ctx 16
- 1051d | Supreme | Camiseta | Camiseta Supreme "Washed Script Black" Preto | handle `supreme-washed-script-short-sleeve-top-black` | id 8101966938334 | Shopify inventory ctx 1
- 1044d | Adidas | Tênis | Tênis Bad Bunny x adidas Campus Brown Marrom | handle `bad-bunny-x-adidas-campus-brown` | id 8106539057374 | Shopify inventory ctx 6
- 1044d | Adidas | Tênis | Tênis adidas Samba OG Green Branco | handle `adidas-samba-og-green` | id 8106533880030 | Shopify inventory ctx 5
- 1009d | Yeezy | Tênis | Tênis Yeezy Foam Runner Carbon Preto | handle `yeezy-foam-runner-carbon` | id 8128031326430 | Shopify inventory ctx 7
- 959d | Adidas | Tênis | Tênis Bad Bunny x adidas Campus Light Cloud White Bege | handle `bad-bunny-x-adidas-campus-light-cloud-white` | id 8186086228190 | Shopify inventory ctx 8
- 934d | Nike | Tênis | Tênis Dunk Low Light Ocean Bliss | handle `dunk-low-light-ocean-bliss` | id 8220211740894 | Shopify inventory ctx 2
- 925d | Nike | Tênis | Tênis Run The Jewels x Dunk Low SB '4/20' Azul | handle `run-the-jewels-x-dunk-low-sb-4-20` | id 8228419240158 | Shopify inventory ctx 11
- 903d | Adidas | Tênis | Tênis adidas Campus 00s Dark Green Verde | handle `adidas-campus-00s-dark-green` | id 8245117845726 | Shopify inventory ctx 8
- 898d | Adidas | Tênis | Tênis The Grinch x adidas Forum Low Green Verde | handle `the-grinch-x-adidas-forum-low-green` | id 8084002472158 | Shopify inventory ctx 0
- 898d | Adidas | Tênis | Tênis Yu-Gi-Oh! x adidas ADI2000 Dark Magician Branco | handle `yu-gi-oh-x-adidas-adi2000-dark-magician` | id 8084000538846 | Shopify inventory ctx 0
- 898d | New Balance | Tênis | Tênis New Balance 550 White Pine Green Branco/Verde | handle `new-balance-550-white-pine-green` | id 8084006895838 | Shopify inventory ctx 4
- 898d | New Balance | Tênis | Tênis New Balance 9060 Mineral Red Truffle Rain Cloud Vermelho | handle `new-balance-9060-mineral-red-truffle-rain-cloud` | id 8084006830302 | Shopify inventory ctx 21
- 898d | Nike | Tênis | Tênis Air Max Plus Black University Blue Preto | handle `air-max-plus-black-university-blue` | id 8084008403166 | Shopify inventory ctx 0
- 898d | Yeezy | Tênis | Tênis Yeezy 500 Blush Bege | handle `yeezy-500-blush` | id 8084001718494 | Shopify inventory ctx 0
- 898d | Yeezy | Tênis | Tênis Yeezy 700 V1 Wave Runner Cinza | handle `yeezy-700-v1-wave-runner` | id 8084001685726 | Shopify inventory ctx 10
- 898d | Yeezy | Tênis | Tênis Yeezy 700 V3 Mono Safflower Amarelo | handle `yeezy-700-v3-mono-safflower` | id 8084001620190 | Shopify inventory ctx 12
- 898d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 MX Oat Multicolor | handle `yeezy-boost-350-v2-mx-oat` | id 8084001358046 | Shopify inventory ctx 3
- 898d | Yeezy | Tênis | Tênis Yeezy Boost 350 v2 Mono Ice Azul | handle `yeezy-boost-350-v2-mono-ice` | id 8084001390814 | Shopify inventory ctx 0
- 898d | Yeezy | Tênis | Tênis Yeezy Foam Runner Sand Bege | handle `yeezy-foam-runner-sand-937693356` | id 8084001063134 | Shopify inventory ctx 1
- 879d | Adidas | Tênis | Tênis Adidas Campus 00s Crystal White Branco | handle `tenis-adidas-campus-00s-crystal-white-branco` | id 8261326209246 | Shopify inventory ctx 1
- 879d | Adidas | Tênis | Tênis Adidas Campus 00s Grey Three Cinza | handle `tenis-adidas-campus-00s-grey-three-cinza` | id 8261328371934 | Shopify inventory ctx 4
- 870d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 Oreo Preto | handle `yeezy-boost-350-v2-oreo` | id 8270263910622 | Shopify inventory ctx 10
- 868d | Adidas | Tênis | Tênis adidas Samba OG "Core Black Wonder" White Preto | handle `tenis-adidas-samba-og-core-black-wonder-white-preto` | id 8272445571294 | Shopify inventory ctx 5
- 868d | Jordan | Tênis | Tênis Nike Air Jordan 1 Low "Dune Red" Vermelho | handle `tenis-jordan-1-low-dune-red-vermelho` | id 8272543187166 | Shopify inventory ctx 9
- 867d | Vans | Tênis | Tênis Vans "Knu Old Skool Black White" Preto | handle `tenis-vans-knu-old-skool-black-white-preto` | id 8272966287582 | Shopify inventory ctx 11
- 854d | Adidas | Tênis | Tênis adidas Gazelle Indor "Active Maroon" Vermelho | handle `tenis-adidas-gazelle-indor-active-marron-vermelho` | id 8281067258078 | Shopify inventory ctx 4
- 848d | Adidas | Tênis | Tênis adidas Gazelle Indor "Beam Pink Solar Red" Rosa | handle `tenis-adidas-gazelle-indor-beam-pink-solar-red-rosa` | id 8284054126814 | Shopify inventory ctx 3
- 834d | Adidas | Tênis | Tênis Adidas Response CL x Bad Bunny Wonder Branco | handle `tenis-adidas-responce-cl-x-bad-bunny-wonder-branco` | id 8305540301022 | Shopify inventory ctx 19
- 834d | Adidas | Tênis | Tênis adidas Campus 00s Ambient Sky Azul | handle `tenis-adidas-campus-00s-ambient-sky-azul` | id 8307080298718 | Shopify inventory ctx 1
- 830d | Adidas | Tênis | Tênis adidas Sambae Cloud White Better Scarlet Branco | handle `tenis-adidas-sambae-cloud-white-better-scarlet-branco` | id 8313339707614 | Shopify inventory ctx 5
- 829d | Essentials | Camiseta | Camiseta Essentials Fear of God Crewneck Jet Black Preto | handle `camiseta-essentials-fear-of-god-crewneck-jet-black-preto` | id 8311696720094 | Shopify inventory ctx 4
- 827d | Adidas | Tênis | Tênis adidas Handball Spezial Preloved Green Verde | handle `tenis-adidas-handball-spezial-preloved-green-verde` | id 8313341083870 | Shopify inventory ctx 4
- 827d | Adidas | Tênis | Tênis adidas Samba OG Cream White Core Black Bege | handle `tenis-adidas-samba-og-cream-white-core-black-bege` | id 8316489466078 | Shopify inventory ctx 5
- 825d | New Balance | Tênis | Tênis New Balance 530 Stoneware Line Branco | handle `tenis-new-balance-530-stoneware-line-branco` | id 8323555393758 | Shopify inventory ctx 0
- 812d | Adidas | Tênis | Tênis adidas Sambae Cloud White Collegiate Green Branco | handle `tenis-adidas-sambae-cloud-white-collegiate-green-branco` | id 8347286896862 | Shopify inventory ctx 8
- 806d | Adidas | Tênis | Tênis adidas Sambae Cloud White Black Branco | handle `tenis-adidas-sambae-cloud-white-branco` | id 8366511096030 | Shopify inventory ctx 4
- 800d | Adidas | Tênis | Tênis adidas Gazelle Indoor Collegiate Green Verde | handle `tenis-adidas-gazelle-indoor-collegiate-green-verde` | id 8382514659550 | Shopify inventory ctx 5
- 790d | Adidas | Tênis | Tênis Campus 00S Wonder Blue Azul | handle `campus-00s-j-wonder-blue` | id 8428412076254 | Shopify inventory ctx 0
- 788d | Adidas | Tênis | Tênis adidas Samba Og Off White Oat Violet Tone Branco | handle `tenis-adidas-samba-og-off-white-oat-violet-tone-branco` | id 8430354497758 | Shopify inventory ctx 3
- 787d | Adidas | Tênis | Tênis adidas Sambae x KSENIASCHNAIDER Black Multicolor Colorido | handle `tenis-adidas-sambae-x-kseniaschnaiderc-black-multicolor-colorido` | id 8382526128350 | Shopify inventory ctx 4
- 780d | Sufgang | Colecionável | Basic Pack 5.8 Sufgang Multicolor | handle `basic-pack-5-8-sufgang-multicolor` | id 8452834328798 | Shopify inventory ctx 0
- 779d | Adidas | Tênis | Tênis adidas Samba Og Collegiate Green Gum Verde | handle `tenis-adidas-samba-og-collegiate-green-gum-verde` | id 8459252236510 | Shopify inventory ctx 8
- 771d | Sufgang | Camiseta | Camiseta Sufgang Basic Pack 5.8 Cinza | handle `camiseta-sufgang-basic-pack-5-8-cinza` | id 8475831566558 | Shopify inventory ctx 0
- 765d | Adidas | Boné | Korn x adidas Boné Preto | handle `pre-venda-korn-x-adidas-bone-preto` | id 8484924031198 | Shopify inventory ctx 0
- 756d | New Balance | Tênis | Tênis New Balance 9060 Nori Verde | handle `tenis-new-balance-9060-nori-verde` | id 8504350671070 | Shopify inventory ctx 9
- 752d | Adidas | Tênis | Tênis adidas Sambae Black White Gum Preto | handle `adidas-sambae-black-white-gum` | id 8512772341982 | Shopify inventory ctx 6
- 751d | Adidas | Tênis | Tênis adidas Samba Og Night Navy Gum Azul Marinho | handle `tenis-adidas-samba-og-night-navy-gum-azul-marinho` | id 8520055292126 | Shopify inventory ctx 0
- 751d | Adidas | Tênis | Tênis adidas Samba x Wales Bonner Wonder Clay Royal Bege | handle `tenis-adidas-samba-x-wales-bonner-wonder-clay-royal-bege` | id 8520085012702 | Shopify inventory ctx 6
- 748d | New Balance | Tênis | Tênis New Balance 530 White Mint Branco | handle `tenis-new-balance-530-white-mint-branco` | id 8525163135198 | Shopify inventory ctx 11
- 743d | Adidas | Meia | Meias Adidas x Korn | handle `pre-venda-meias-adidas-x-korn` | id 8484924096734 | Shopify inventory ctx 0
- 743d | Adidas | Tênis | Tênis adidas Campus 00s Bliss Pink Rosa | handle `tenis-adidas-campus-00s-bliss-pink-rosa` | id 8540730851550 | Shopify inventory ctx 1
- 743d | Adidas | Tênis | Tênis adidas Forum Buckle Low  x Bad Bunny Blue Tint Azul | handle `tenis-adidas-forum-buckle-low-x-bad-bunny-blue-tint-azul` | id 8540743925982 | Shopify inventory ctx 0
- 743d | Adidas | Tênis | Tênis adidas Samba XLG Cloud White Branco | handle `tenis-adidas-samba-xlg-cloud-white-branco` | id 8540758474974 | Shopify inventory ctx 4
- 742d | Adidas | Tênis | Tênis adidas Sambae Cloud White Silver Metallic Gold Branco | handle `tenis-adidas-sambae-cloud-white-silver-metallic-gold-branco` | id 8540749889758 | Shopify inventory ctx 3
- 741d | Adidas | Tênis | Tênis adidas Samba x Humanrace Core Black Cinza | handle `tenis-adidas-samba-x-humanrace-core-black-cinza` | id 8541968105694 | Shopify inventory ctx 3
- 741d | Adidas | Tênis | Tênis adidas Samba x Humanrace Navy Aluminum Cinza | handle `tenis-adidas-samba-x-humanrace-navy-aluminum-cinza` | id 8541966336222 | Shopify inventory ctx 6
- 739d | Adidas | Tênis | Tênis adidas Sambae Core Black Metallic Gold Preto | handle `tenis-adidas-sambae-core-black-metallic-gold-preto` | id 8540754280670 | Shopify inventory ctx 6
- 738d | Yeezy | Tênis | Tênis Yeezy Boost 350 V2 Beluga Cinza | handle `tenis-yeezy-boost-350-v2-beluga-cinza` | id 8545297203422 | Shopify inventory ctx 6
- 735d | Adidas | Tênis | Tênis adidas Campus 00s Scarlet Red Vermelho | handle `tenis-adidas-campus-00s-scarlet-red-vermelho` | id 8553126658270 | Shopify inventory ctx 4
- 728d | Nike | Tênis | Tênis Nike Dunk Low Grey Fog Cinza | handle `nike-dunk-low-grey-fog` | id 8186087112926 | Shopify inventory ctx 6
- 725d | Nike | Tênis | Tênis Nike Dunk Low Sashiko Industrial Blue Azul | handle `tenis-nike-dunk-low-sashiko-industrial-blue-azul` | id 8578477228254 | Shopify inventory ctx 9
- 724d | Jordan | Tênis | Tênis Nike A Ma Maniére x Air Jordan 1 Sail and Burgundy Bege | handle `a-ma-maniere-x-air-jordan-1-sail-and-burgundy` | id 8107019501790 | Shopify inventory ctx 0
- 724d | Jordan | Tênis | Tênis Nike Air Jordan 1 Elevate Low Guava Ice Rosa | handle `air-jordan-1-elevate-low-guava-ice` | id 8098121089246 | Shopify inventory ctx 2
- 724d | Jordan | Tênis | Tênis Nike Air Jordan 1 Elevate Low SE Lucky Green Verde | handle `air-jordan-1-elevate-low-se-lucky-green` | id 8084016005342 | Shopify inventory ctx 4

## Approval scope sugerido
Se aprovado, executar Shopify `productUpdate(status:DRAFT)` apenas nos IDs do CSV/JSON escolhidos, com backup de status anterior e readback Admin. Nenhum preço/estoque/Tiny/tema/campanha será alterado.