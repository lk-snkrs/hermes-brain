# LK GMC P2 SEO/Category Read-only Preview — 2026-05-13

Status: `readonly_preview_no_writes`

## Veredito
- P1 está limpo; P2 seguro agora é preparar categorização (`googleProductCategory`/`product_type`) e reparos de título, sem aplicar ainda.
- Este relatório é preview/read-only; não houve write no Merchant, Shopify, Tiny, banco, feed ou campanha.

## Saúde atual GMC
- Produtos online analisados: 11668
- Productstatuses lidos: 23245
- Issue counts top: {'price_updated': 1011, 'strikethrough_price_updated': 489, 'restricted_gtin': 102, 'landing_page_error': 63, 'image_single_color': 8, 'image_link_broken': 8, 'reserved_gtin': 6, 'condition_updated_from_detected': 4, 'restricted_nfs_policy_violation': 4, 'coupon_gtin': 3}

## Buckets P2
- P2A categoria/product_type candidata: 2425
- P2B reparo crítico de título: 35
- P2C melhoria/revisão de título: 11328
- Sem ação P2 detectada: 185

## Categorias sugeridas — top buckets
- 1517: `Apparel & Accessories > Shoes` / `Calçados`
- 440: `Apparel & Accessories > Clothing > Shirts & Tops` / `Vestuário > Tops/Camisetas`
- 192: `Apparel & Accessories > Clothing > Shorts` / `Vestuário > Shorts`
- 126: `Apparel & Accessories > Clothing > Outerwear` / `Vestuário > Moletons/Hoodies`
- 53: `Apparel & Accessories > Clothing > Outerwear` / `Vestuário > Jaquetas/Casacos`
- 52: `Apparel & Accessories > Clothing Accessories` / `Acessórios`
- 31: `Apparel & Accessories > Clothing Accessories > Hats` / `Acessórios > Bonés`
- 10: `Apparel & Accessories > Clothing > Pants` / `Vestuário > Calças`
- 4: `Luggage & Bags > Handbags, Wallets & Cases` / `Acessórios > Bolsas`

## Amostras P2B — título crítico
- `online:pt:BR:5706324928133224313` — título atual: "39" → motivo: critical_generic_or_size_only_title, duplicate_title_group_2
- `online:pt:BR:6036386056472256840` — título atual: "37" → motivo: critical_generic_or_size_only_title, duplicate_title_group_4
- `online:pt:BR:3048242206072553507` — título atual: "42" → motivo: critical_generic_or_size_only_title, duplicate_title_group_3
- `online:pt:BR:6234067398750979457` — título atual: "34" → motivo: critical_generic_or_size_only_title, duplicate_title_group_6
- `online:pt:BR:11810372920072143991` — título atual: "40" → motivo: critical_generic_or_size_only_title, duplicate_title_group_3
- `online:pt:BR:16599698222138562820` — título atual: "34" → motivo: critical_generic_or_size_only_title, duplicate_title_group_6
- `online:pt:BR:1863698749035586532` — título atual: "44" → motivo: critical_generic_or_size_only_title
- `online:pt:BR:4531110532523186885` — título atual: "39" → motivo: critical_generic_or_size_only_title, duplicate_title_group_2
- `online:pt:BR:2198938218729451562` — título atual: "37" → motivo: critical_generic_or_size_only_title, duplicate_title_group_4
- `online:pt:BR:14252480804615463970` — título atual: "41" → motivo: critical_generic_or_size_only_title

## Amostras P2A — categoria/product_type
- `online:pt:BR:JI3185-7` — "Tênis Adidas Samba OG Cream White Cardboard Creme" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)
- `online:pt:BR:13632296688851150214` — "Pop Mart Labubu The Monsters Have a Seat HEHE Vinyl Plush Pingente" → `Apparel & Accessories > Clothing Accessories` / `Acessórios` (title accessory token)
- `online:pt:BR:HV0823-100-5` — "Tênis Nike Air Jordan 4 Retro Forget Me Not Azul" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)
- `online:pt:BR:BQ6472104-1` — "Tênis Nike Air Jordan 1 Mid Kentucky Blue Azul" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)
- `online:pt:BR:FV5029-010-43` — "Tênis Nike Air Jordan 4 Retro 'Black Cat' Preto" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)
- `online:pt:BR:43774078391040` — "Camiseta Skims Manga Longa Cotton Jersey Light Heather Grey Cinza" → `Apparel & Accessories > Clothing > Shirts & Tops` / `Vestuário > Tops/Camisetas` (title apparel top token)
- `online:pt:BR:43774078391770` — "Polo Skims Baby Tee Worn in Jersey Snow Branco" → `Apparel & Accessories > Clothing > Shirts & Tops` / `Vestuário > Tops/Camisetas` (title apparel top token)
- `online:pt:BR:HV0823-100-6` — "Tênis Nike Air Jordan 4 Retro Forget Me Not Azul" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)
- `online:pt:BR:LAB04` — "Pop Mart Labubu The Monsters Tasty Macarons Sea Salt Cocount Vinyl Plush Pingente" → `Apparel & Accessories > Clothing Accessories` / `Acessórios` (title accessory token)
- `online:pt:BR:1183C428.200-10` — "Tênis Onitsuka Tiger California 78 EX Putty/Green Bege" → `Apparel & Accessories > Shoes` / `Calçados` (title sneaker-shoe/model token)

## Próximo pacote seguro recomendado
1. P2A: executor dry-run para `googleProductCategory` + `productTypes` somente, nos buckets de alta confiança por token de título.
2. P2B: pacote manual/revisão para títulos críticos genéricos como tamanho/cor isolada, usando Shopify/Data Spine/link como fonte antes de write.
3. P2C: deixar melhorias amplas de título para depois; risco maior de mexer em SEO/catálogo sem necessidade.

## Não executado
- merchant_write
- shopify_write
- feed_fetch_or_upload
- database_write
- campaign_or_message_send
- external_marketplace_call
