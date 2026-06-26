# LK GMC P1 Attribute Completion — Post-Apply Onda 1 + Onda 2 Review, 2026-05-13

Status: `gmc_p1_attribute_post_apply_onda1_verified_wave2_review_ready_no_write`

## O que foi feito
- Reconsulta read-only de Merchant products e productstatuses.
- Medição pós-apply dos 60 IDs da Onda 1.
- Preparação de amostra revisável da Onda 2, sem apply.

## Onda 1 — resultado pós-propagação
- IDs aplicados na Onda 1: 60
- Produtos ainda presentes: 60
- `sizes` esperado confirmado agora: 60/60
- IDs ainda com issue fresh de `size`: 0
- IDs ainda com qualquer required-attribute issue: 0

## Onda 2 — estado read-only
- Rows no packet Onda 2: 1523
- Estados fresh:
  - blocked_missing_suggested_size: 51
  - candidate_wave2_review_default_adult_unisex_size: 1285
  - review_non_default_age_gender: 187
- Missing attrs fresh na Onda 2:
  - age group: 1469
  - color: 54
  - gender: 1469
  - size: 1463

## Amostra revisável Onda 2
- `online:pt:BR:ST68` — Bermuda Saint Studio Alfaiataria Algodão Orgânico Risca de Giz Preto — missing=['age group', 'gender', 'size'] — sugestão: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:YR0065` — Calça Pace Nomo Tailoring Trousers Preto — missing=['age group', 'gender', 'size'] — sugestão: size=['S/P'], ageGroup=adult, gender=unisex
- `online:pt:BR:ST63` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — missing=['age group', 'gender', 'size'] — sugestão: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:ST85` — Camisa Saint Studio Pima Listrada Azul — missing=['age group', 'gender', 'size'] — sugestão: size=['L/G'], ageGroup=adult, gender=unisex
- `online:pt:BR:5209-1` — Camiseta Dane-se x Rubem Valentim Emblema 78 Bordo — missing=['age group', 'gender', 'size'] — sugestão: size=['G/L'], ageGroup=adult, gender=unisex
- `online:pt:BR:5362-2` — Camiseta Oversized Dane-se Pare, Respire Off White — missing=['age group', 'gender', 'size'] — sugestão: size=['M'], ageGroup=adult, gender=unisex
- `online:pt:BR:YR0044` — Camiseta Pace Buero Off White — missing=['age group', 'gender', 'size'] — sugestão: size=['L/G'], ageGroup=adult, gender=unisex
- `online:pt:BR:ST51` — Camiseta Saint Studio Boxy Supima Mid Century Branco — missing=['age group', 'gender', 'size'] — sugestão: size=['L/G'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLCRCVNV-1` — Camiseta Slyce Racquet Club Azul Marinho — missing=['age group', 'gender', 'size'] — sugestão: size=['P/S'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLCRBVOW-1` — Camiseta Slyce Racquet Club Bordada Off White — missing=['age group', 'gender', 'size'] — sugestão: size=['P/S'], ageGroup=adult, gender=unisex
- `online:pt:BR:4150233_0090_356-1` — Chinelo Havaianas Top Dolce & Gabbana Banano Verde — missing=['age group', 'gender', 'size'] — sugestão: size=['35/36'], ageGroup=adult, gender=unisex
- `online:pt:BR:2000415173436-1` — Mule Lululemon SwayDay Blissful Pink Rosa — missing=['age group', 'gender', 'size'] — sugestão: size=['34'], ageGroup=adult, gender=unisex
- `online:pt:BR:1183C233-250-1` — Onitsuka Tiger Mexico 66 Paraty Natural Navy Bege — missing=['age group', 'gender', 'size'] — sugestão: size=['34'], ageGroup=adult, gender=unisex
- `online:pt:BR:1183C468020-1` — Onitsuka Tiger Mexico 66 SD Metallic Series Metropolis Cream Cinza — missing=['age group', 'gender', 'size'] — sugestão: size=['34'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLPTMCS-1` — Polo Slyce On Season TM Verde — missing=['age group', 'gender', 'size'] — sugestão: size=['M'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLFTPVNV-1` — Pulôver Slyce Frenchterry Zipper Azul Marinho — missing=['age group', 'gender', 'size'] — sugestão: size=['M'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLFTPVOW-1` — Pulôver Slyce Frenchterry Zipper Off White — missing=['age group', 'gender', 'size'] — sugestão: size=['M'], ageGroup=adult, gender=unisex
- `online:pt:BR:w6525r_01-3` — Short Alo Yoga 5" Airbrush Double Up Azul Marinho — missing=['age group', 'gender', 'size'] — sugestão: size=['S/P'], ageGroup=adult, gender=unisex
- `online:pt:BR:ST73` — Shorts Saint Studio Everywear Caqui Bege — missing=['age group', 'gender', 'size'] — sugestão: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:ST78` — Shorts Saint Studio Everywear Preto — missing=['age group', 'gender', 'size'] — sugestão: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLFTSVOW-1` — Shorts Slyce Frenchterry Off White — missing=['age group', 'gender', 'size'] — sugestão: size=['P/S'], ageGroup=adult, gender=unisex
- `online:pt:BR:SLSTMCS-1` — Shorts Slyce On Season TM Verde — missing=['age group', 'gender', 'size'] — sugestão: size=['M'], ageGroup=adult, gender=unisex
- `online:pt:BR:HQ4307-601` — Slide Nike Mind 001 'Team Red' Vermelho — missing=['age group', 'gender', 'size'] — sugestão: size=['38'], ageGroup=adult, gender=unisex
- `online:pt:BR:HQ4307-301-37` — Slide Nike Mind 001 Geode Teal Verde — missing=['age group', 'gender', 'size'] — sugestão: size=['37'], ageGroup=adult, gender=unisex
- `online:pt:BR:HQ4307-100-34` — Slide Nike Mind 001 Sail Bege — missing=['age group', 'gender', 'size'] — sugestão: size=['34'], ageGroup=adult, gender=unisex

## Guardrail
- A Onda 2 continua como `review/no-write`: usa default `adult/unisex` + tamanho por Shopify, mas ainda precisa aprovação explícita antes de qualquer apply.

## Não executado
- merchant_write
- merchant_delete
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
