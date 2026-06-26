# LK GMC P2A Next Online Preview — 2026-05-13

Status: `read_only_preview_no_write`

## Escopo
- Somente `online:pt:BR:*`.
- Exclui `local:LIA_*`.
- Campos candidatos: `productAttributes.googleProductCategory` + `productAttributes.productTypes`.
- Sem título, preço, disponibilidade, imagem/link, Shopify, Tiny ou feed.

## Resumo
- Elegíveis online: 10576
- Piloto recomendado: 250
- Buckets elegíveis: {'Apparel & Accessories > Shoes / Tênis': 9018, 'Apparel & Accessories > Clothing > Shirts & Tops / Camiseta': 570, 'Apparel & Accessories > Clothing > Outerwear / Moletom/Jaqueta': 464, 'Apparel & Accessories > Clothing > Pants / Calça': 381, 'Luggage & Bags > Handbags, Wallets & Cases / Bolsa/Carteira': 51, 'Apparel & Accessories > Clothing Accessories > Hats / Boné': 48, 'Apparel & Accessories > Clothing > Shorts / Shorts': 44}
- Buckets do piloto: {'Apparel & Accessories > Clothing > Shirts & Tops / Camiseta': 250}

## Approval recomendado
`Aprovo aplicar P2A next wave piloto em 250 produtos online no GMC via Merchant API v1, apenas googleProductCategory e productTypes, com rollback e verificação.`

## Amostra do piloto
- `online:pt:BR:5627606835540697766` — Camiseta Aimé Leon Dore ALD Golf Swing Coconut Milk Off White - Tamanho M → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:FW24CT001S-1` — Camiseta Aimé Leon Dore Embroidered Logo Preto → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:FW24CT001S-2` — Camiseta Aimé Leon Dore Embroidered Logo Preto → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:FW24CT001S-3` — Camiseta Aimé Leon Dore Embroidered Logo Preto → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2515934-L` — Camiseta Aimé Leon Dore Musician Graphic Preta → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2515934-M` — Camiseta Aimé Leon Dore Musician Graphic Preta → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2515934-S` — Camiseta Aimé Leon Dore Musician Graphic Preta → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2515934-XL` — Camiseta Aimé Leon Dore Musician Graphic Preta → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-3381470-G` — Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-3381470-M` — Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-3381470-P` — Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-9318238-G` — Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-9318238-M` — Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-9318238-P` — Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2352094-L` — Camiseta Aimé Leon Dore Queens Crest Pocket Pine Grove Verde → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2352094-M` — Camiseta Aimé Leon Dore Queens Crest Pocket Pine Grove Verde → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2352094-S` — Camiseta Aimé Leon Dore Queens Crest Pocket Pine Grove Verde → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:ALD-2352094-XL` — Camiseta Aimé Leon Dore Queens Crest Pocket Pine Grove Verde → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:Aime3-1` — Camiseta Aimé Leon Dore Sound Branco → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta
- `online:pt:BR:Aime3-2` — Camiseta Aimé Leon Dore Sound Branco → Apparel & Accessories > Clothing > Shirts & Tops / Camiseta

## Não executado
- merchant_write
- local_inventory_write
- shopify_write
- tiny_write
- price_update
- availability_update
- title_update
- image_or_link_update
- feed_fetch_or_upload
- campaign_or_message_send
