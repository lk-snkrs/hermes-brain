# LK GMC P1 Attribute Completion — Remaining Wave3 Preview, 2026-05-13

Status: `gmc_p1_attribute_remaining_wave3_preview_read_only`

## Escopo
- Reconsulta fresh read-only de Merchant products/productstatuses.
- Classificação dos required attributes remanescentes depois da Onda 2.
- Join local com Shopify snapshot por offer_id/SKU ou variant_id quando possível.
- Nenhum write/delete/feed/fetch.

## Resultado executivo
- Merchant products atuais: 23241
- Productstatuses atuais: 23241
- Rows com required attributes atuais: 232
- Instâncias de required attributes atuais: 363
- Rows com match Shopify local: 102

## Required attrs por atributo
- color: 183
- size: 83
- price: 35
- age group: 31
- gender: 31

## Buckets Onda 3
- blocked_no_safe_suggestion: 201
- candidate_wave3_price_review_do_not_apply_without_price_policy: 31

## Amostras por bucket
### blocked_no_safe_suggestion
- `online:pt:BR:12887836741223739253` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:16599698222138562820` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:4086849490768644696` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:5390248129051651686` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:6234067398750979457` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:8419194273885247483` — 34 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:2243578831328686793` — 35 — missing=['size'] — sugestão={} — evidência={}
- `online:pt:BR:5328214585182033036` — 35 — missing=['size'] — sugestão={} — evidência={}
### candidate_wave3_price_review_do_not_apply_without_price_policy
- `online:pt:BR:11810372920072143991` — 40 — missing=['age group', 'color', 'gender', 'price'] — sugestão={'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:7958216211561773980` — Bolsa Aimé Leon Dore x Porsche Commuter Preto | LK Sneakers — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Preto', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:14088693984092512857` — Boné 6 Panel Aimé Leon Dore Embroidered Logo Branco — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Branco', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:8532426969879844901` — Boné Aimé Leon Dore Micro Logo Pristine Off White — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Off White / Branco', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:1624428988081867066` — Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo | LK Sneaker — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Amarelo / Dourado', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:8888219390173948734` — Boné Aimé Leon Dore x Porsche Nylon Logo Pine Grove Verde — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Verde', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:10591784840915585992` — Boné Saint Studio Art Department Azul - LK — missing=['age group', 'color', 'gender', 'price'] — sugestão={'color': 'Azul', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}
- `online:pt:BR:2258634078163248862` — Calça Chino Saint Studio Supima Preto — missing=['age group', 'color', 'gender', 'price', 'size'] — sugestão={'color': 'Preto', 'ageGroup': 'adult', 'gender': 'unisex'} — evidência={'color': 'title_color_token_low_to_medium_confidence', 'ageGroup': 'default_review_required', 'gender': 'default_review_required'}

## Próximo passo seguro
- Preparar executor dry-run apenas para um bucket de alta confiança, preferencialmente `candidate_wave3_color_tag_high_confidence`, sem apply até nova aprovação inline.

## Não executado
- merchant_write
- merchant_delete
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_or_local_inventory_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
