# Receipt — HOME New Balance 204L image center DEV

Data UTC: 20260606T135512Z

## Escopo executado
Upload aprovado somente para o tema DEV/unpublished do asset `templates/index.json`.

## Mudança
- `image_position`: `bottom` → `center center`
- Imagem preservada: `DSC03377.jpg`
- Copy preservada: `New Balance 204L` / `Uma silhueta que antecipa.`

## Tema alvo
- DEV: `lk-new-theme/dev` / role `unpublished` / id `155065450718`
- Production conferido: `lk-new-theme/production` / role `main` / id `155065417950`

## Verificação
- DEV raw SHA antes: `5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15`
- DEV raw SHA target local: `3418ffe7458cc0f0fb15c57857c2d07cbf92a97e1788beb938e84034fdee995e`
- DEV raw SHA readback: `256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d`
- Observação: raw SHA target/readback difere porque o Shopify escapou barras em JSON (`shopify:\/\/`); a comparação canônica do JSON parseado bateu.
- Production SHA antes/depois: `5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15` → `5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15`
- Production inalterada: `True`

## Checks pós-upload
- PASS — dev_readback_canonical_json_matches_target: JSON object equal; Shopify escaped slashes in raw source
- PASS — production_unchanged: 5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15 -> 5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15
- PASS — dev_readback_has_center_position: center center
- PASS — dev_readback_preserves_dsc03377: shopify://shop_images/DSC03377.jpg / shopify://shop_images/DSC03377.jpg
- PASS — dev_readback_preserves_copy: New Balance 204L / Uma silhueta que antecipa.

## Preview DEV
https://www.lksneakers.com.br/?preview_theme_id=155065450718

Observação: preview público sem sessão autenticada pode servir live/cache; Asset API readback é a evidência técnica autoritativa do DEV. Probe público: `{"status": 200, "final_url": "https://lksneakers.com.br/", "contains_preview_theme_id_final_url": false, "contains_204l": true, "contains_center_literal": false}`.

## Rollback
Reupload do backup `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/home-204l-image-position-dev-20260606/20260606T135353Z/dev_before_templates__index.json` no mesmo tema DEV e novo readback por JSON canônico/SHA.

## Não ações
Sem Production, sem produto, preço, estoque, checkout, app ou campanha.

## Worker receipt
- demand_classification: Shopify theme / HOME editorial image alignment
- canonical_playbook: Shopify theme/CRO preview-first, DEV write approved, Production separate
- workers_selected: none
- workers_skipped: visual QA worker, deploy worker, GitHub worker
- delegation_tool_used: no
- reason_if_no_delegation: alteração de 1 setting em template JSON, com validação/readback direta suficiente
- owner_agent_final_decision: aplicado somente em DEV/unpublished; aguardar revisão/decisão separada para merge para Production


Artefatos completos: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/home-204l-image-position-dev-20260606/20260606T135353Z`
