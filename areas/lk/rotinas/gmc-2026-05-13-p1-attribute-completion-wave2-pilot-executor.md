# LK GMC P1 Attribute Completion — Onda 2 Pilot Executor, 2026-05-13

Status: `gmc_p1_attribute_wave2_pilot_apply_verified`

## Escopo
- Modo: `apply`
- Onda: 2, piloto conservador.
- Campos alvo: `sizes`, `ageGroup`, `gender`.
- Valores default aceitos no piloto: `ageGroup=adult`, `gender=unisex`.
- Canal: `online` apenas.
- Apply produtivo: bloqueado até aprovação inline específica.

## Resultado do preflight
- Rows Onda 2 no packet: 1523
- Merchant products atuais: 23241
- Productstatuses atuais: 23241
- Ready para apply futuro: 969
- Selecionados no piloto se aprovado: 969

## Estados
- blocked_non_default_age_gender: 178
- blocked_suggestion_not_exact_3field: 6
- ready_for_wave2_pilot_apply_if_lucas_approves: 969
- skipped_not_freshly_missing_target_attrs: 370

## Amostra selecionada para piloto
- `online:pt:BR:JQ0567-5` — Tênis Adidas Tokyo Off White Core Black Branco — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['38'], ageGroup=adult, gender=unisex
- `online:pt:BR:JQ0567-6` — Tênis Adidas Tokyo Off White Core Black Branco — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['39'], ageGroup=adult, gender=unisex
- `online:pt:BR:JQ0567-7` — Tênis Adidas Tokyo Off White Core Black Branco — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['40'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5350` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['34'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5352` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5353` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['37'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5354` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['38'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5355` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['39'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5356` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['40'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5357` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['41'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5358` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['42'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5359` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['43'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5360` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['44'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5361` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['45'], ageGroup=adult, gender=unisex
- `online:pt:BR:bb5362` — Tênis Adidas Yeezy Boost 350 Pirate Black 2023 — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['46'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw00100` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['45'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw00101` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['46'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0089` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['34'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0090` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['35'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0091` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['36'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0092` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['37'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0093` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['38'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0094` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['39'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0095` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['40'], ageGroup=adult, gender=unisex
- `online:pt:BR:gw0096` — Tênis Adidas Yeezy Boost 350 V2 Ash Stone Cinza — missing=['age group', 'gender', 'size'] — aplicar se aprovado: size=['41'], ageGroup=adult, gender=unisex

## Aprovação necessária para apply futuro
- Texto exato requerido pelo executor: `Lucas approved GMC P1 Attribute Wave2 pilot apply`
- Recomendação: aplicar primeiro piloto de 50, verificar via `products.get`, depois medir `productstatuses` antes de escalar.

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-completion-wave2-pilot-executor-rollback-20260513T113824Z.json`

## Não executado
- merchant_delete
- merchant_delete
- merchant_price_title_link_image_availability_update
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_or_local_inventory_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
