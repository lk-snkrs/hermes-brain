# Receipt — HOME New Balance 204L image position DEV

Data UTC: 20260606T135641Z

## Escopo aprovado
Lucas aprovou: `Aprovo subir para DEV/unpublished`.

## Mudança aplicada
- Asset: `templates/index.json`
- Bloco: `editorial` / `section`
- Campo: `image_position`
- Antes no DEV: `center center`
- Depois no DEV: `center center`
- Copy preservado: `New Balance 204L` / `Uma silhueta que antecipa.`

## Tema alvo
- DEV: `lk-new-theme/dev` / role `unpublished` / id `155065450718`
- Production conferido: `lk-new-theme/production` / role `main` / id `155065417950`

## Verificação
- DEV before SHA: `256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d`
- DEV semantic target SHA: `d3b35ae7bc12eb3eea3ea41a73b7d88e6f05d82b96a509ed08b54c02509a5ff5`
- DEV expected readback SHA: `256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d`
- DEV readback SHA: `256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d`
- Production SHA antes/depois: `5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15` → `5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15`

## Checks pós-upload
- PASS — dev_readback_sha_matches_expected: 256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d vs 256cbd40b6c5ea3d844ff2d18515d84e6cb3a6b718f1346d59b6f68a4dc4025d
- PASS — production_unchanged: 5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15 -> 5db58b3051882dc4c9e546781e3edf2e68498df648732133db45ab71b2882b15
- PASS — dev_readback_single_editorial_204l_candidate: [('hero', 's2'), ('editorial', 'section')]
- PASS — dev_readback_image_position_center: center center
- PASS — dev_readback_copy_preserved: present

## Preview
- `https://www.lksneakers.com.br/?preview_theme_id=155065450718`

Observação: preview público sem sessão autenticada pode servir live/cache; o readback do Asset API é a evidência técnica autoritativa do DEV.

## Rollback
Reupload do backup DEV:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-home-204l-image-position-dev-20260606T135641Z/dev_before_templates__index.json`

## Não ações
Sem Production/live, sem produto, coleção, preço, estoque, checkout, app ou campanha.
